# Как пользоваться сборником

Сборник сочетает вопросы, объяснения и задания разной сложности. Двигайтесь по результатам практики: название технологии в резюме само по себе не означает, что задача освоена.

| Этап | Материал | Проверяемый результат |
|---|---|---|
| Основа | [Linux](topics/linux/README.md), [Bash](topics/shell/README.md), [Git](topics/git/README.md), [DNS](topics/dns/README.md), [CIDR-практика](topics/network/exercises/cidr/exercise.md) | Найти причину отказа процесса, разобрать права/порты/DNS, восстановить изменение через Git |
| Доставка приложения | [Контейнеры](topics/containers/README.md), [CI/CD](topics/cicd/README.md), [Flask](topics/flask_container_ci/README.md) | Собрать воспроизводимый артефакт и обнаружить регрессию тестами |
| Инфраструктура | [Kubernetes](topics/kubernetes/README.md), [Terraform](topics/terraform/README.md), [Ansible](topics/ansible/README.md) | Объяснить diff/plan, развернуть в учебной среде и проверить rollout/restore |
| Эксплуатация | [SRE](topics/sre/README.md), [наблюдаемость](topics/observability/README.md), [Grafana](topics/grafana/README.md) | Определить пользовательское SLO, обнаружить сбой и проверить восстановление |
| Современные практики | [GitOps](topics/gitops/README.md), [цепочка поставки](topics/software_supply_chain/README.md), [безопасность](topics/security/README.md) | Отличить drift от неисправности приложения; проверить происхождение и полномочия артефакта |
| Потоки событий | [Kafka](topics/kafka/README.md) | Объяснить partition/offset, повторы, lag и границы exactly-once |

Облачный трек выбирайте по своей работе: [AWS](topics/aws/README.md), [Azure](topics/azure/README.md) или [GCP](topics/gcp/README.md). Изучать все облака одновременно не обязательно. Для экзаменов используйте актуальный guide из соответствующего файла certificates, а не только этот набор задач.

## Практика с обратной связью

Начните с [SLO-лаборатории](topics/sre/exercises/error_budget/exercise.md) и двух Flask-приложений. Они проверяются локально без облачного аккаунта. Общий запуск:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
bash scripts/run_ci.sh
```

Для каждого практического задания фиксируйте:

1. Предпосылки: версии, права, окружение и исходные данные.
2. Ожидаемое поведение и способ его наблюдать.
3. Минимальное решение и объяснение компромиссов.
4. Отрицательный сценарий: неверный ввод, отказ зависимости или повтор события.
5. Проверку восстановления и удаление учебных ресурсов.

## Как оценивать ответ

- **0:** термин знаком, но объяснения и проверки нет.
- **1:** объяснение верно, пример работает только при благоприятных условиях.
- **2:** пример воспроизводится; учтены ошибки и ограничения.
- **3:** показаны диагностика, компромиссы, проверка результата и восстановление.

Ответ на вопрос о личном опыте должен описывать реальные действия кандидата. Пример из сборника используйте для тренировки, а не как выдуманную рабочую историю.

## Что подтверждают автоматические проверки

CI проверяет регрессии программ, локальные файлы/якоря, структуру вопросов, синтаксис Python/Bash/YAML/HCL и счётчик. Отдельный job выполняет Terraform init/validate без backend и облачных credentials на GitHub runner. Успешная схема Terraform не подтверждает права аккаунта, наличие ресурсов, стоимость или результат apply.

Тесты не доказывают истинность каждого объяснения. Для изменений квот, API, runtime и экзаменов указывайте источник и дату; учебные среды проверяйте отдельно. Состояние работ и ограничения зафиксированы в [техническом отчёте](TECHNICAL_AUDIT.md).

Для самопроверки используйте случайные вопросы по теме:

```bash
python scripts/random_question.py --list-topics
python scripts/random_question.py --topic sre --skip
python scripts/random_question.py --topic gitops --once --show-answer --seed 42
```

По умолчанию вопросы выбираются из всех разделов. Для главного README задайте `--topic main`; команда работает из любого текущего каталога. `--once` удобен для одной короткой проверки, а фиксированный seed воспроизводит выбор при неизменном содержимом.

Дополнительная практика без облака: [IPv4 CIDR](topics/network/exercises/cidr/exercise.md), [схема доски сообщений](topics/databases/solutions/table_for_message_board_system.md) и [границы SQL-дат](topics/sql/improve_query.md). SQL-тесты выполняют запросы из README и проверяют ошибки целостности на SQLite in-memory; это не замена проверке своей production-СУБД.
