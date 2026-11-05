<a id="apache-kafka"></a>
# Apache Kafka

<a id="kafka-exercises"></a>
## Упражнения по Kafka

Практический сценарий: consumer записал результат в БД и завершился до фиксации offset. Опишите повторную обработку после перезапуска, ключ идемпотентности и атомарность записи. Затем объясните, что изменится при commit до записи в БД. Сверьте ответ с разделом о надёжности ниже.

<a id="kafka-self-assessment"></a>
## Самопроверка по Kafka

* [Основы Kafka](#questions-kafka-101)

<a name="questions-kafka-101"></a>
<a id="kafka-101"></a>
### Основы Kafka

<details>
<summary>Что такое Kafka?</summary><br><b>

[kafka.apache.org](https://kafka.apache.org): Apache Kafka — открытая распределённая платформа потоковой обработки событий. Она применяется для высокопроизводительных конвейеров данных, потоковой аналитики, интеграции данных и критически важных приложений.

Kafka можно представить как распределённый журнал: события записываются, читаются и передаются различным сервисам в большом масштабе и в реальном времени.
</b></details>

<details>
<summary>Для чего используется Kafka?</summary><br><b>

* Электронная коммерция в реальном времени.
* Банковские системы.
* Здравоохранение.
* Автомобильные системы: предупреждения о пробках, опасностях и других событиях.
* Обнаружение мошенничества в реальном времени.
</b></details>

<details>
<summary>Что такое Producer в Kafka?</summary><br><b>

Приложение-производитель, которое публикует данные в кластере Kafka.
</b></details>

<a name="questions-kafka-architecture"></a>
<a id="kafka-architecture"></a>
### Архитектура Kafka

<details>
<summary>Что входит в кластер Kafka?</summary><br><b>

Брокеры хранят и обслуживают разделы топиков. В KRaft контроллеры поддерживают согласованные метаданные через quorum; для production роли брокера и контроллера обычно разделяют. Это разные функции, хотя учебная установка может объединять их в процессе.
</b></details>

<details>
<summary>Какова роль ZooKeeper в Kafka?</summary><br><b>

В Kafka 4.0+ режим ZooKeeper удалён: используется KRaft. В старых кластерах ZooKeeper хранил метаданные и участвовал в координации; назначения лидеров выполнял контроллер Kafka. Это не один и тот же процесс.

Кластер с ZooKeeper нельзя просто обновить до 4.x: сначала выполняют поддерживаемую миграцию в KRaft и проверяют совместимость клиентов, брокеров и metadata version. Порядок зависит от исходной версии.

[Официальное руководство обновления](https://kafka.apache.org/40/getting-started/upgrade/).
</b></details>

## Надёжность и обработка событий

<details>
<summary>Гарантирует ли Kafka порядок всех сообщений топика?</summary>

Порядок определён внутри partition. Между partitions общего порядка нет. Связанные события направляют по одному ключу с учётом partitioner; увеличение числа partitions может изменить распределение ключей. Параллельная обработка потребителем тоже может изменить порядок завершения операций. [Объяснение производителя дистрибутива](https://docs.redhat.com/en/documentation/red_hat_streams_for_apache_kafka/3.0/html/kafka_configuration_tuning/con-consumer-config-properties-str).
</details>

<details>
<summary>Чем offset отличается от подтверждения бизнес-операции?</summary>

Offset задаёт позицию в partition. Committed offset обозначает, откуда группа продолжит после восстановления, обычно следующий номер для чтения. Успешный commit не доказывает, что внешний платёж или запись в БД выполнены. Чтение записи также не удаляет её из топика: retention действует независимо. [Consumer position](https://kafka.apache.org/design/).
</details>

<details>
<summary>Что дают acks=all и min.insync.replicas?</summary>

С `acks=all` подтверждение требует всех текущих ISR, а `min.insync.replicas` задаёт минимально допустимый размер ISR для такой записи. RF=3 и min ISR=2 не означают «всегда ждать ровно две реплики»: если в ISR три, подтверждают все три. При недостаточном ISR запись получает ошибку. Это компромисс доступности записи и устойчивости к потере реплик, а не замена backup. [Topic configs](https://kafka.apache.org/43/configuration/topic-configs/).
</details>

<details>
<summary>Почему идемпотентный producer не исключает двойное списание денег?</summary>

Он устраняет определённые дубликаты повторных отправок producer→Kafka, но не повторное выполнение внешнего эффекта consumer. После записи в БД и сбоя до commit сообщение может прийти снова. Нужны ключ идемпотентности и атомарная фиксация результата/дедупликации в целевой системе. [Границы гарантий](https://kafka.apache.org/design/).
</details>

<details>
<summary>Когда применимы Kafka transactions и read_committed?</summary>

Для атомарной публикации в Kafka и фиксации offsets в одной Kafka-транзакции. Потребитель `read_committed` не выдаёт записи прерванных транзакций. Внешняя БД или HTTP API автоматически в транзакцию Kafka не включаются: требуется согласованный протокол обработки. [Delivery semantics](https://kafka.apache.org/design/).
</details>

<details>
<summary>Как разбирать растущий consumer lag?</summary>

Сначала определите отстающие partitions и скорость изменения lag, проверьте ошибки, rebalances, время обработки, throttling и состояние downstream. Больше consumers в обычной группе не даёт больше активных обработчиков, чем доступных partitions. Lag в сообщениях не равен задержке в секундах; смотрите возраст событий и бизнес-SLO. [Kafka FAQ](https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=109445663).
</details>

<details>
<summary>Чем retention отличается от log compaction?</summary>

Retention удаляет старые сегменты по политике времени/размера. Compaction сохраняет последнее известное значение каждого ключа, но не удаляет старые версии мгновенно. Tombstone обозначает удаление ключа и тоже хранится ограниченное время. Проверьте `cleanup.policy` и окно восстановления потребителя. [Topic configs](https://kafka.apache.org/43/configuration/topic-configs/).
</details>
