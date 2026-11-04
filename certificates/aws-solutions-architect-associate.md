<a id="aws---solutions-architect-associate"></a>
## AWS — Solutions Architect Associate

Последнее обновление исходника: 2021 год. Это перевод исторической версии: сведения об услугах, ограничениях и экзаменах могут быть устаревшими.

<a id="aws-global-infrastructure"></a>
#### Глобальная инфраструктура AWS

<details>
<summary>Объясните следующие понятия:

  * Зона доступности
  * Регион
  * Пограничная точка присутствия (edge location)</summary><br><b>

Регионы AWS — отдельные географические области по всему миру, в которых размещены центры обработки данных. Регионы изолированы друг от друга.<br>

В каждом регионе есть несколько изолированных зон доступности (Availability Zones, AZ). Размещение ресурсов в нескольких зонах позволяет сохранить доступность при отказе одной из них.<br>

Пограничные точки присутствия используются сетью доставки контента для кеширования данных, снижения задержек и ускорения доставки пользователям. Они расположены в крупных городах по всему миру.
</b></details>

<a id="aws---iam"></a>
#### AWS — IAM

<details>
<summary>Что такое IAM? Какие возможности он предоставляет?</summary><br><b>

Подробнее — [здесь](https://aws.amazon.com/iam)
IAM используется для управления пользователями, группами, политиками доступа и ролями.
</b></details>

<details>
<summary>Верно ли, что настройки IAM задаются глобально, а не отдельно для каждого региона?</summary><br><b>

Верно.
</b></details>

<details>
<summary>Верно ли, что при создании аккаунта AWS автоматически создаётся корневой пользователь (root), которого рекомендуется использовать совместно внутри организации?</summary><br><b>

Неверно. В исходнике рекомендуется создавать отдельных пользователей вместо повседневного использования root. Общий доступ к учётным данным root предоставлять не следует.
</b></details>

<details>
<summary>Верно ли, что группы AWS IAM могут содержать только пользователей, но не другие группы?</summary><br><b>

Верно.
</b></details>

<details>
<summary>Верно ли, что пользователь AWS IAM может входить только в одну группу?</summary><br><b>

Неверно. Пользователь может входить в несколько групп.
</b></details>

<details>
<summary>Что такое роли?</summary><br><b>

Роль позволяет предоставить необходимые разрешения, например одному сервису AWS для обращения к другому. Роли можно назначать ресурсам AWS.
Например, роль может разрешать экземпляру EC2 читать и записывать объекты в бакете S3.
</b></details>

<details>
<summary>Что такое политики?</summary><br><b>

Политики — документы в формате JSON, описывающие разрешения: какие действия может выполнять пользователь, группа или роль.
</b></details>

<details>
<summary>Пользователь не может получить доступ к бакету S3. В чём может быть причина?</summary><br><b>

Причин может быть несколько. Одна из них — отсутствие разрешающей политики. В таком случае администратору нужно назначить пользователю политику, разрешающую необходимый доступ к бакету S3.
</b></details>

<details>
<summary>Что нужно использовать, чтобы:

  * Предоставить одному сервису или ресурсу доступ к другому?
  * Предоставить пользователю доступ к ресурсам или сервисам?</summary><br><b>

  * Роль.
  * Политику.
</b></details>

<details>
<summary>Какие разрешения есть у нового пользователя?</summary><br><b>

В исходнике: «Только доступ для входа». Уточнение: вход возможен при настроенных учётных данных; разрешения на работу с ресурсами необходимо предоставить отдельно.
</b></details>


<a id="aws-networking"></a>
#### Сетевые возможности AWS

<details>
<summary>Что такое VPC?</summary><br><b>

Логически изолированная часть облака AWS, в которой можно запускать ресурсы в определённой вами виртуальной сети.
Подробнее — [здесь](https://aws.amazon.com/vpc).
</b></details>

<details>
<summary>Верно ли, что VPC охватывает несколько регионов?</summary><br><b>

Неверно.
</b></details>

<details>
<summary>Верно ли, что подсети одной VPC могут находиться в разных зонах доступности?</summary><br><b>

Верно. При этом каждая отдельная подсеть должна целиком находиться в одной зоне доступности.
</b></details>

<details>
<summary>Что такое интернет-шлюз (Internet Gateway)?</summary><br><b>

Согласно документации AWS, это компонент, обеспечивающий связь экземпляров в VPC с интернетом.
Подробнее — [здесь](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html)
</b></details>

<details>
<summary>Верно ли, что NACL разрешают или запрещают трафик на уровне подсети?</summary><br><b>

Верно.
</b></details>

<details>
<summary>Верно ли, что к одной VPC можно подключить несколько интернет-шлюзов?</summary><br><b>

Неверно. К одной VPC можно подключить только один интернет-шлюз.
</b></details>

<details>
<summary>Верно ли, что таблицы маршрутизации используются для разрешения или запрета трафика из интернета к экземплярам AWS?</summary><br><b>

Неверно.
</b></details>

<details>
<summary>Объясните назначение групп безопасности и сетевых ACL.</summary><br><b>

* NACL — уровень защиты на уровне подсети.
* Группа безопасности — уровень защиты на уровне экземпляра.

Подробнее — [здесь](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html) and [here](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)
</b></details>

<details>
<summary>Что такое AWS Direct Connect?</summary><br><b>

Позволяет соединить корпоративную сеть с сетью AWS.
</b></details>

<a id="aws-compute"></a>
#### Вычислительные ресурсы AWS

<details>
<summary>Что такое EC2?</summary><br><b>

Веб-сервис, предоставляющий защищённые вычислительные мощности в облаке с возможностью изменения их объёма.
Подробнее — [здесь](https://aws.amazon.com/ec2)
</b></details>

<details>
<summary>Верно ли, что EC2 — региональный сервис?</summary><br><b>

Верно. В отличие, например, от глобального сервиса IAM, EC2 работает в рамках региона.
</b></details>

<details>
<summary>Что такое AMI?</summary><br><b>

Amazon Machine Image (AMI) — образ, содержащий информацию, необходимую для запуска экземпляра.
Подробнее — [здесь](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)
</b></details>

<details>
<summary>Из каких источников можно получить AMI?</summary><br><b>

* Собственные AMI — образы, которые вы создаёте сами.
* AWS Marketplace — платные AMI, обычно с предустановленным лицензируемым ПО.
* AMI сообщества — бесплатные образы.
</b></details>

<details>
<summary>Что такое тип экземпляра?</summary><br><b>

Выбранный тип экземпляра определяет характеристики аппаратных ресурсов, предоставляемых экземпляру.
Подробнее — [здесь](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html)
</b></details>

<details>
<summary>Верно ли, что в AWS доступны следующие типы экземпляров?

  * Оптимизированные для вычислений
  * Оптимизированные для сети
  * Оптимизированные для веб-приложений</summary><br><b>

Ответ исходника: неверно; из перечисленного выделяется категория экземпляров, оптимизированных для вычислений. Названия категорий не следует путать с отдельными типами экземпляров с улучшенными сетевыми характеристиками.
</b></details>

<details>
<summary>Что такое EBS?</summary><br><b>

EBS предоставляет тома блочного хранения для экземпляров EC2. Они ведут себя как обычные неформатированные блочные устройства.
Подробнее — [здесь](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html)
</b></details>

<details>
<summary>Какие модели оплаты EC2 существуют?</summary><br><b>

On-Demand — оплата по установленному почасовому или посекундному тарифу без долгосрочных обязательств. Экземпляр можно создать или завершить в любой момент.
Reserved — в исходнике описаны как резервирование мощности на фиксированный срок со скидкой. Уточнение: условия скидки и резервирования мощности зависят от варианта Reserved Instance; это не покупка физического экземпляра.
Spot — использование свободных мощностей по цене Spot. В исходнике упоминается исторический механизм ставок; это описание не следует принимать за актуальную схему аукциона.
Dedicated Hosts — физические серверы EC2, выделенные для вашего использования.
</b></details>

<details>
<summary>Что такое группы безопасности?</summary><br><b>

Группа безопасности работает как виртуальный межсетевой экран, управляющий трафиком для одного или нескольких экземпляров.
Подробнее — [здесь](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html)
</b></details>

<details>
<summary>Что можно подключить к экземпляру EC2 для хранения данных?</summary><br><b>

EBS
</b></details>

<details>
<summary>Какие типы зарезервированных экземпляров EC2 (RI) существуют?</summary><br><b>

Standard RI — значительная скидка; подходят для стабильной нагрузки.
Convertible RI — скидка и возможность изменения характеристик RI; подходят для стабильной нагрузки.
Scheduled RI — запуск в зарезервированные временные интервалы. Это исторический вариант, перечисленный в исходнике 2021 года.

Подробнее — [здесь](https://aws.amazon.com/ec2/pricing/reserved-instances)
</b></details>

<a id="aws-containers"></a>
#### Контейнеры в AWS

<details>
<summary>Что такое Amazon ECS?</summary><br><b>

Определение Amazon: Amazon Elastic Container Service (ECS) — полностью управляемый сервис оркестрации контейнеров. В исходнике Duolingo, Samsung, GE и Cook Pad приведены как примеры компаний, использующих ECS для критически важных приложений благодаря его безопасности, надёжности и масштабируемости.

Подробнее — [здесь](https://aws.amazon.com/ecs)
</b></details>

<details>
<summary>Что такое Amazon ECR?</summary><br><b>

Определение Amazon: Amazon Elastic Container Registry (ECR) — полностью управляемый реестр контейнерных образов Docker, упрощающий их хранение, администрирование и развёртывание.

Подробнее — [здесь](https://aws.amazon.com/ecr)
</b></details>

<details>
<summary>Что такое AWS Fargate?</summary><br><b>

Определение Amazon: AWS Fargate — бессерверная вычислительная платформа для контейнеров, работающая с Amazon Elastic Container Service (ECS) и Amazon Elastic Kubernetes Service (EKS).

Подробнее — [здесь](https://aws.amazon.com/fargate)
</b></details>

<a id="aws-storage"></a>
#### Хранение данных в AWS
 
<details>
<summary>Объясните, что такое AWS S3.</summary><br><b>

Название S3 образовано от трёх слов на S: Simple Storage Service.
S3 — быстрое, масштабируемое и надёжное объектное хранилище. В исходнике указан максимальный размер одного загружаемого, скачиваемого или хранимого объекта — 5 ТБ; это ограничение приведено для версии материала 2021 года.

Подробнее — [здесь](https://aws.amazon.com/s3) 
</b></details>

<details>
<summary>Что такое бакет?</summary><br><b>

Бакет S3 — ресурс для хранения объектов с данными. Для простоты его можно сравнить с папкой файловой системы, хотя модель хранения S3 объектная.
</b></details>

<details>
<summary>Верно ли, что имя бакета должно быть глобально уникальным?</summary><br><b>

Верно.
</b></details>

<details>
<summary>Объясните понятия папки и объекта применительно к бакетам.</summary><br><b>

* Папка — представление вложенной структуры внутри бакета S3.
* Объект — хранящиеся в бакете данные, которые в исходнике для простоты названы файлами.
</b></details>

<details>
<summary>Объясните следующие понятия:

  * Жизненный цикл объектов
  * Совместный доступ к объектам
  * Версионирование объектов</summary><br><b>

  * Жизненный цикл — переход объектов между классами хранения по заданным временным правилам.
  * Совместный доступ — предоставление доступа к объектам по URL.
  * Версионирование — управление несколькими версиями одного объекта.
</b></details>

<details>
<summary>Объясните разницу между сохранностью (durability) и доступностью (availability) объектов.</summary><br><b>

Сохранность объекта — вероятность того, что он не будет утрачен за год, выраженная в процентах.
Доступность объекта — доля времени за год, в течение которого объект доступен, выраженная в процентах.
</b></details>

<details>
<summary>Что такое класс хранения? Какие классы существуют?</summary><br><b>

Каждому объекту назначается класс хранения, от которого зависят характеристики доступности, сохранности и стоимость.
В исходнике 2021 года перечислены следующие классы и показатели. Значения сохранены как часть исторического материала; отдельные цифры в исходнике требуют проверки и не должны использоваться как актуальная спецификация сервиса:
  * Standard:
    * Универсальное хранение, прежде всего данных, к которым часто обращаются.
    * В исходнике назван самым дорогим классом хранения.
    * Сохранность — 11 девяток.
    * Доступность — 99% (так указано в исходнике).
    * Класс хранения по умолчанию.

  * Standard-IA (редкий доступ)
    * Долгосрочное хранение редко используемых данных, которые должны быть доступны сразу при обращении.
    * Сохранность — 11 девяток.
    * Доступность — 99,90%.

  * One Zone-IA (редкий доступ):
    * Долгосрочное хранение редко используемых, некритичных данных.
    * Дешевле классов Standard и Standard-IA.
    * Сохранность — 99% (так указано в исходнике).
    * Доступность — 99,50%.
    
  * Intelligent-Tiering:
    * Долгосрочно хранимые данные с меняющимся или неизвестным характером обращений. Данные автоматически перемещаются на подходящий уровень хранения в зависимости от использования.
    * Стоимость зависит от используемого уровня хранения.
    * Сохранность — 11 девяток.
    * Доступность — 99,90%.

  * Glacier: архивные данные со временем извлечения от нескольких минут до нескольких часов.
  * Glacier Deep Archive: архивные данные, к которым обращаются крайне редко или не обращаются вовсе; извлечение занимает часы.
  * Glacier и Glacier Deep Archive:
    * Самые дешёвые классы из перечисленных в исходнике.
    * Сохранность — 9 девяток (так указано в исходнике).

Подробнее — [здесь](https://aws.amazon.com/s3/storage-classes)

</b></details>

<details>
<summary>Заказчик хочет переместить редко используемые данные из Standard в самый дешёвый класс хранения. Какой класс следует выбрать?

  * One Zone-IA
  * Glacier Deep Archive
  * Intelligent-Tiering</summary><br><b>

Glacier Deep Archive
</b></details>

<details>
<summary>Какие варианты извлечения данных Glacier доступны пользователю?</summary><br><b>

Expedited (ускоренное), Standard (стандартное) и Bulk (массовое).
</b></details>

<details>
<summary>Верно ли, что каждый аккаунт AWS может хранить до 500 ПБ данных, а дополнительный объём оплачивается по двойному тарифу?</summary><br><b>

Неверно. Такого ограничения общей ёмкости нет.
</b></details>

<details>
<summary>Объясните, что такое Storage Gateway.</summary><br><b>

AWS Storage Gateway — гибридный сервис хранения, обеспечивающий доступ из локальной инфраструктуры к практически неограниченному облачному хранилищу.
Подробнее — [здесь](https://aws.amazon.com/storagegateway)
</b></details>

<details>
<summary>Объясните следующие варианты развёртывания Storage Gateway:

  * File Gateway
  * Volume Gateway
  * Tape Gateway</summary><br><b>

Подробнее — [здесь](https://aws.amazon.com/storagegateway/faqs)
</b></details>

<details>
<summary>Чем отличаются stored volumes и cached volumes?</summary><br><b>

Stored volumes — данные находятся в ЦОД заказчика и периодически резервируются в AWS.
Cached volumes — данные находятся в облаке AWS, а для быстрого доступа кешируются в ЦОД заказчика.
</b></details>

<details>
<summary>Что такое Amazon S3 Transfer Acceleration?</summary><br><b>

Определение AWS: Amazon S3 Transfer Acceleration обеспечивает быструю, простую и защищённую передачу файлов на большие расстояния между клиентом и бакетом S3.

Подробнее — [здесь](https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration.html)
</b></details>

<details>
<summary>Что такое Amazon EFS?</summary><br><b>

Определение Amazon: Amazon Elastic File System (EFS) — простая, масштабируемая, полностью управляемая эластичная файловая система NFS для облачных сервисов AWS и локальных ресурсов.

Подробнее — [здесь](https://aws.amazon.com/efs)
</b></details>

<details>
<summary>Что такое AWS Snowmobile?</summary><br><b>

AWS Snowmobile — описанный в исходнике сервис переноса чрезвычайно больших объёмов данных в AWS, вплоть до эксабайтного масштаба.

Подробнее — [здесь](https://aws.amazon.com/snowmobile)
</b></details>

<a id="aws-elb"></a>
##### AWS ELB

<details>
<summary>Что такое ELB (Elastic Load Balancing)?</summary><br><b>

Определение AWS: Elastic Load Balancing автоматически распределяет входящий трафик приложения между несколькими целями: экземплярами Amazon EC2, контейнерами, IP-адресами и функциями Lambda.

Подробнее — [здесь](https://aws.amazon.com/elasticloadbalancing)
</b></details>

<details>
<summary>Что такое автоматическое масштабирование?</summary><br><b>

Определение AWS: AWS Auto Scaling отслеживает приложения и автоматически изменяет объём ресурсов, поддерживая стабильную и предсказуемую производительность при минимально возможных затратах.

Подробнее — [здесь](https://aws.amazon.com/autoscaling)
</b></details>

<details>
<summary>Верно ли, что автоматическое масштабирование только добавляет ресурсы, например экземпляры, но не удаляет их?</summary><br><b>

Неверно. Оно регулирует объём ресурсов, в том числе уменьшает их количество в зависимости от нагрузки и производительности.
</b></details>

<details>
<summary>Какие типы балансировщиков нагрузки поддерживаются для EC2 и для чего они используются?</summary><br><b>

  * Application Load Balancer — трафик прикладного уровня, L7.
  * Network Load Balancer — высокая производительность или статический IP-адрес.
  * Classic Load Balancer — в исходнике представлен как недорогой вариант для тестовых сред и разработки; это историческая рекомендация, а не актуальное сравнение стоимости.
</b></details>

<a id="aws-dns"></a>
#### AWS DNS

<details>
<summary>Что такое Route 53?</summary><br><b>

Amazon Route 53 — высокодоступный и масштабируемый облачный DNS-сервис.
Некоторые возможности Route 53:
  * Регистрация доменов.
  * DNS — разрешение доменных имён.
  * Проверки работоспособности — контроль доступности приложения.

Подробнее — [здесь](https://aws.amazon.com/route53)
</b></details>

<a id="aws-cloudfront"></a>
#### AWS CloudFront

<details>
<summary>Объясните, что такое CloudFront.</summary><br><b>

Определение AWS: Amazon CloudFront — быстрая сеть доставки контента (CDN), которая безопасно доставляет данные, видео, приложения и API пользователям по всему миру с низкой задержкой и высокой скоростью, предоставляя удобную для разработчиков среду.

Подробнее — [здесь](https://aws.amazon.com/cloudfront)
</b></details>

<details>
<summary>Объясните следующие понятия:

  * Источник контента (origin)
  * Пограничная точка присутствия (edge location)
  * Конфигурация доставки (distribution)</summary><br><b>
</b></details>

<a id="aws-monitoring--logging"></a>
#### Мониторинг и журналирование в AWS

<details>
<summary>Что такое AWS CloudWatch?</summary><br><b>

Определение AWS: Amazon CloudWatch — сервис мониторинга и наблюдаемости.

Подробнее — [здесь](https://aws.amazon.com/cloudwatch)
</b></details>

<details>
<summary>Что такое AWS CloudTrail?</summary><br><b>

Определение AWS: AWS CloudTrail — сервис для управления аккаунтом AWS, контроля соответствия требованиям, операционного аудита и аудита рисков.

Подробнее — [здесь](https://aws.amazon.com/cloudtrail)
</b></details>

<details>
<summary>Что такое Simple Notification Service?</summary><br><b>

Определение AWS: высокодоступный, надёжный, защищённый и полностью управляемый сервис обмена сообщениями по модели публикации и подписки (pub/sub), позволяющий уменьшить связанность микросервисов, распределённых систем и бессерверных приложений.

Подробнее — [здесь](https://aws.amazon.com/sns)
</b></details>

<details>
<summary>Объясните следующие понятия SNS:

  * Темы (topics)
  * Подписчики (subscribers)
  * Издатели (publishers)</summary><br><b>

  * Темы — используются для группировки нескольких конечных точек.
  * Подписчики — конечные точки, которым доставляются сообщения темы.
  * Издатели — источники сообщений: события, люди и т. д.
</b></details>

<a id="aws-security"></a>
#### Безопасность в AWS

<details>
<summary>Что такое модель разделённой ответственности? За что в этой модели отвечает AWS, а за что — пользователь?</summary><br><b>

Модель разделённой ответственности определяет зоны ответственности заказчика и AWS.

Подробнее — [здесь](https://aws.amazon.com/compliance/shared-responsibility-model)
</b></details>

<details>
<summary>Верно ли, что в модели разделённой ответственности Amazon отвечает за физические процессоры и группы безопасности экземпляров?</summary><br><b>

Неверно. Amazon отвечает за оборудование своих площадок, но группы безопасности создают и администрируют пользователи.
</b></details>

<details>
<summary>Объясните понятие Shared Controls в модели разделённой ответственности.</summary><br><b>

Определение AWS: общие меры контроля применяются и к инфраструктуре, и к среде заказчика, но в разных контекстах. AWS обеспечивает их реализацию для инфраструктуры, а заказчик должен реализовать соответствующие меры в своей среде использования сервисов AWS.

Подробнее — [здесь](https://aws.amazon.com/compliance/shared-responsibility-model)
</b></details>

<details>
<summary>Что такое программа AWS по обеспечению соответствия требованиям?</summary><br><b>
</b></details>

<details>
<summary>Что такое AWS Artifact?</summary><br><b>

Определение AWS: AWS Artifact — централизованный источник информации о соответствии требованиям. Он предоставляет по запросу доступ к отчётам AWS о безопасности и соответствии, а также к отдельным онлайн-соглашениям.

Подробнее — [здесь](https://aws.amazon.com/artifact)
</b></details>

<details>
<summary>Что такое AWS Inspector?</summary><br><b>

Определение AWS из исходника: Amazon Inspector — сервис автоматической оценки безопасности приложений в AWS и их соответствия требованиям. Он выявляет уязвимости, доступность для атак и отклонения от рекомендуемых практик.

Подробнее — [здесь](https://aws.amazon.com/inspector)
</b></details>

<details>
<summary>Что такое AWS GuardDuty?</summary><br><b>
</b></details>

<details>
<summary>Что такое AWS Shield?</summary><br><b>

Определение AWS: AWS Shield — управляемый сервис защиты приложений AWS от распределённых атак типа «отказ в обслуживании» (DDoS).
</b></details>

<details>
<summary>Что такое AWS WAF? Приведите пример использования и назовите ресурсы или сервисы, с которыми он работает.</summary><br><b>
</b></details>

<details>
<summary>Для чего используется AWS VPN?</summary><br><b>
</b></details>

<details>
<summary>Чем отличаются Site-to-Site VPN и Client VPN?</summary><br><b>
</b></details>

<details>
<summary>Что такое AWS CloudHSM?</summary><br><b>

Определение Amazon: AWS CloudHSM — облачный аппаратный модуль безопасности (HSM), позволяющий создавать и использовать собственные ключи шифрования в облаке AWS.

Подробнее — [здесь](https://aws.amazon.com/cloudhsm)
</b></details>

<details>
<summary>Верно ли, что AWS Inspector может выполнять оценку безопасности как сети, так и хостов?</summary><br><b>

Верно.
</b></details>

<details>
<summary>Что такое политика допустимого использования AWS (Acceptable Use Policy)?</summary><br><b>

Она описывает запрещённые способы использования веб-сервисов AWS.
Подробнее — [здесь](https://aws.amazon.com/aup)
</b></details>

<details>
<summary>Что такое AWS Key Management Service (KMS)?</summary><br><b>

Определение AWS: KMS упрощает создание криптографических ключей, управление ими и контроль их использования в сервисах AWS и собственных приложениях.
Подробнее — [здесь](https://aws.amazon.com/kms)
</b></details>

<details>
<summary>Верно ли, что пользователю запрещено проводить тестирование на проникновение для любых сервисов AWS?</summary><br><b>

Неверно. В исходнике EC2, CloudFront и RDS приведены как примеры сервисов, для которых такое тестирование разрешено. Конкретные действия должны соответствовать действующим правилам AWS и разрешённому объёму тестирования.
</b></details>

<details>
<summary>Верно ли, что DDoS-атака — пример разрешённого действия при тестировании на проникновение?</summary><br><b>

Неверно.
</b></details>

<details>
<summary>Верно ли, что ключ доступа AWS Access Key — это MFA-устройство для защиты ресурсов AWS?</summary><br><b>

Неверно. Пример MFA-устройства — аппаратный ключ безопасности, а не программный ключ доступа AWS.
</b></details>

<details>
<summary>Что такое Amazon Cognito?</summary><br><b>

Определение Amazon: Amazon Cognito обеспечивает аутентификацию и авторизацию пользователей веб-приложений и мобильных приложений.

Подробнее — [здесь](https://docs.aws.amazon.com/cognito/index.html)
</b></details>

<details>
<summary>Что такое AWS ACM?</summary><br><b>

Определение Amazon: AWS Certificate Manager позволяет получать, администрировать и развёртывать публичные и частные сертификаты SSL/TLS для сервисов AWS и подключённых внутренних ресурсов.

Подробнее — [здесь](https://aws.amazon.com/certificate-manager)
</b></details>

<a id="aws-databases"></a>
#### Базы данных AWS

<details>
<summary>Что такое AWS RDS?</summary><br><b>
</b></details>

<details>
<summary>Что такое AWS DynamoDB?</summary><br><b>
</b></details>

<details>
<summary>Объясните возможность восстановления на определённый момент времени (Point-in-Time Recovery) в DynamoDB.</summary><br><b>

Определение Amazon: можно создавать резервные копии таблиц DynamoDB по запросу либо включить непрерывное резервное копирование с возможностью восстановления на определённый момент времени. Резервному копированию по запросу посвящён раздел On-Demand Backup and Restore for DynamoDB.

Подробнее — [здесь](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/PointInTimeRecovery.html)
</b></details>

<details>
<summary>Объясните, что такое глобальные таблицы (Global Tables) DynamoDB.</summary><br><b>

Определение Amazon: глобальная таблица — набор из одной или нескольких таблиц-реплик, принадлежащих одному аккаунту AWS.

Подробнее — [здесь](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_HowItWorks.html)
</b></details>

<details>
<summary>Что такое DynamoDB Accelerator?</summary><br><b>

Определение Amazon: DynamoDB Accelerator (DAX) — полностью управляемый высокодоступный кеш в памяти для DynamoDB, который, согласно описанию исходника, позволяет повысить производительность до 10 раз и сократить задержки с миллисекунд до микросекунд.

Подробнее — [здесь](https://aws.amazon.com/dynamodb/dax)
</b></details>

<details>
<summary>Что такое AWS Redshift и чем он отличается от RDS?</summary><br><b>

Облачное аналитическое хранилище данных.
</b></details>

<details>
<summary>Что такое AWS ElastiCache? В каких случаях его используют?</summary><br><b>

Amazon ElastiCache в исходнике описан как полностью управляемое хранилище данных в памяти на основе Redis или Memcached.
Он подходит, например, для двухуровневых веб-приложений: часто запрашиваемые данные хранятся в ElastiCache, что сокращает время ответа.
</b></details>

<details>
<summary>Что такое Amazon Aurora?</summary><br><b>

Реляционная база данных, совместимая с MySQL и PostgreSQL. В исходнике она также названа предлагаемым по умолчанию вариантом при создании БД через RDS; это описание интерфейса на момент написания материала.
Подходит, например, для двухуровневых веб-приложений с уровнем БД MySQL или PostgreSQL, которым требуется автоматическое резервное копирование.
</b></details>

<details>
<summary>Что такое Amazon DocumentDB?</summary><br><b>

Определение Amazon: Amazon DocumentDB — быстрый, масштабируемый, высокодоступный и полностью управляемый сервис документных БД с совместимостью с MongoDB. Он упрощает хранение, запросы и индексирование JSON-данных.

Подробнее — [здесь](https://aws.amazon.com/documentdb)
</b></details>

<details>
<summary>Для чего используется AWS Database Migration Service?</summary><br><b>
</b></details>

<details>
<summary>Какой тип хранилища использует Amazon RDS?</summary><br><b>

EBS
</b></details>

<details>
<summary>Объясните назначение реплик чтения Amazon RDS.</summary><br><b>

Определение AWS: реплики чтения Amazon RDS повышают производительность и надёжность экземпляров БД. Они позволяют масштабировать нагрузки с большим количеством операций чтения за пределы возможностей одного экземпляра.
Подробнее — [здесь](https://aws.amazon.com/rds/features/read-replicas)
</b></details>

<a id="aws-serverless-compute"></a>
#### Бессерверные вычисления AWS

<details>
<summary>Объясните, что такое AWS Lambda.</summary><br><b>

Определение AWS: AWS Lambda позволяет выполнять код без выделения серверов и управления ими. Оплачивается потреблённое вычислительное время.

Подробнее — [здесь](https://aws.amazon.com/lambda)
</b></details>

<details>
<summary>Верно ли, что в AWS Lambda оплата начисляется всё время существования функции, независимо от того, выполняется ли она?</summary><br><b>

Неверно. В описанной в исходнике модели оплата связана с выполнением кода.
</b></details>

<details>
<summary>Какой из следующих наборов языков поддерживает Lambda согласно исходнику?

  * R, Swift, Rust, Kotlin
  * Python, Ruby, Go 
  * Python, Ruby, PHP</summary><br><b>

  * Python, Ruby, Go 
</b></details>

<a id="identify-the-service-or-tool"></a>
#### Определите сервис или инструмент

<details>
<summary>Что использовать для автоматизации развёртывания кода или ПО?</summary><br><b>

AWS CodeDeploy
</b></details>

<details>
<summary>Что использовать для удобного создания похожих сред и ресурсов AWS для разных заказчиков?</summary><br><b>

CloudFormation
</b></details>

<details>
<summary>Какой сервис использовать для создания сайта или веб-приложения?</summary><br><b>

Lightsail
</b></details>

<details>
<summary>Какой инструмент поможет выбрать между Reserved Instances и On-Demand Instances?</summary><br><b>

Cost Explorer
</b></details>

<details>
<summary>Что использовать для проверки количества непривязанных адресов Elastic IP?</summary><br><b>

Trusted Advisor
</b></details>

<details>
<summary>Какой сервис позволяет переносить большие объёмы данных, измеряемые петабайтами, в облако AWS и из него?</summary><br><b>

AWS Snowball
</b></details>

<details>
<summary>Что предоставляет виртуальную сеть, выделенную для вашего аккаунта AWS?</summary><br><b>

VPC
</b></details>

<details>
<summary>Что использовать для автоматического резервного копирования приложения с уровнем БД MySQL?</summary><br><b>

Amazon Aurora
</b></details>

<details>
<summary>Что использовать для переноса локальной базы данных в AWS?</summary><br><b>

AWS Database Migration Service (DMS)
</b></details>

<details>
<summary>Что использовать, чтобы выяснить, почему определённые экземпляры EC2 были завершены?</summary><br><b>

AWS CloudTrail
</b></details>

<details>
<summary>Что использовать в качестве SQL-базы данных?</summary><br><b>

AWS RDS
</b></details>

<details>
<summary>Что использовать в качестве NoSQL-базы данных?</summary><br><b>

AWS DynamoDB
</b></details>

<details>
<summary>Что использовать для интерактивного выполнения SQL-запросов к данным в S3?</summary><br><b>

AWS Athena
</b></details>

<details>
<summary>Что использовать для добавления анализа изображений и видео в приложение?</summary><br><b>

AWS Rekognition
</b></details>

<details>
<summary>Какой сервис использовать для отладки приложений и устранения проблем с производительностью?</summary><br><b>

AWS X-Ray
</b></details>

<details>
<summary>Какой сервис используется для отправки уведомлений?</summary><br><b>

SNS
</b></details>

<details>
<summary>Какой сервис использовать для обнаружения вредоносной активности и несанкционированных действий в аккаунтах и рабочих нагрузках AWS?</summary><br><b>

Amazon GuardDuty
</b></details>

<details>
<summary>Какой сервис использовать для централизованного управления оплатой, доступом, соответствием требованиям и безопасностью в нескольких аккаунтах AWS?</summary><br><b>

AWS Organizations
</b></details>

<details>
<summary>Какой сервис использовать для защиты веб-приложения?</summary><br><b>

AWS WAF
</b></details>

<details>
<summary>Вы хотите отслеживать состояние ресурсов в разных сервисах. Какой сервис для этого использовать?</summary><br><b>

CloudWatch
</b></details>

<details>
<summary>Какой сервис использовать для оценки безопасности?</summary><br><b>

AWS Inspector
</b></details>

<details>
<summary>Какой сервис использовать для создания DNS-записи?</summary><br><b>

Route 53
</b></details>

<details>
<summary>Что использовать, если нужна полностью управляемая документная база данных?</summary><br><b>

Amazon DocumentDB
</b></details>

<details>
<summary>Какой сервис использовать для добавления управления доступом, регистрации и входа пользователей в веб-приложение или мобильное приложение?</summary><br><b>

AWS Cognito
</b></details>

<details>
<summary>Какой сервис использовать, если нужна очередь сообщений?</summary><br><b>

Simple Queue Service (SQS)
</b></details>

<details>
<summary>Какой сервис использовать, если нужна управляемая защита от DDoS?</summary><br><b>

AWS Shield
</b></details>

<details>
<summary>Какой сервис использовать для хранения часто запрашиваемых данных с низкой задержкой доступа?</summary><br><b>

ElastiCache
</b></details>

<details>
<summary>Что использовать для передачи файлов на большие расстояния между клиентом и бакетом S3?</summary><br><b>

Amazon S3 Transfer Acceleration
</b></details>

<a id="aws-billing--support"></a>
#### Оплата и поддержка AWS

<details>
<summary>Что такое AWS Organizations?</summary><br><b>

Определение AWS: AWS Organizations помогает централизованно управлять средой по мере роста и масштабирования рабочих нагрузок в AWS.
Подробнее — [здесь](https://aws.amazon.com/organizations)
</b></details>

<details>
<summary>Объясните модель оплаты AWS.</summary><br><b>

Основной принцип — pay-as-you-go: вы платите за используемые ресурсы в период их использования.
В S3 оплачиваются, в частности: 1) объём хранимых данных; 2) запросы PUT, POST и другие.
Стоимость EC2 зависит от варианта приобретения (On-Demand, Spot и т. д.), типа экземпляра, типа AMI и выбранного региона.

Подробнее — [здесь](https://aws.amazon.com/pricing)
</b></details>

<details>
<summary>Как оценить расходы на AWS, например для сравнения с локальной инфраструктурой?</summary><br><b>

* Калькулятор совокупной стоимости владения (TCO).
* AWS Simple Calculator — название инструмента в исходнике.
* Cost Explorer
</b></details>

<details>
<summary>Что входит в базовую поддержку AWS согласно исходнику?</summary><br><b>

* Круглосуточное обслуживание клиентов.
* Trusted Advisor
* AWS Personal Health Dashboard.
</b></details>

<details>
<summary>Как начисляется плата за экземпляры EC2?</summary><br><b>
</b></details>

<details>
<summary>Для чего используется AWS Pricing Calculator?</summary><br><b>
</b></details>

<details>
<summary>Что такое Amazon Connect?</summary><br><b>

Определение Amazon: Amazon Connect — простой в использовании облачный контакт-центр с поддержкой разных каналов связи, помогающий компаниям улучшать обслуживание клиентов при меньших затратах.

Подробнее — [здесь](https://aws.amazon.com/connect)
</b></details>

<details>
<summary>Кто такие APN Consulting Partners?</summary><br><b>

Определение Amazon: APN Consulting Partners — компании, оказывающие профессиональные услуги заказчикам любого масштаба. Они помогают проектировать, создавать, переносить и администрировать рабочие нагрузки и приложения в AWS, ускоряя переход в облако.

Подробнее — [здесь](https://aws.amazon.com/partners/consulting)
</b></details>

<details>
<summary>В каком варианте перечислены уровни поддержки AWS в порядке возрастания согласно исходнику? В оригинале они неточно названы типами аккаунтов.

  * Basic, Developer, Business, Enterprise
  * Newbie, Intermediate, Pro, Enterprise
  * Developer, Basic, Business, Enterprise
  * Beginner, Pro, Intermediate Enterprise</summary><br><b>

  * Basic, Developer, Business, Enterprise
</b></details>

<details>
<summary>Верно ли, что регион влияет на стоимость EC2?</summary><br><b>

Верно. Тарифы зависят от выбранного региона.
</b></details>

<details>
<summary>Что такое AWS Infrastructure Event Management?</summary><br><b>

Определение AWS из исходника: AWS Infrastructure Event Management — программа для клиентов Enterprise Support, а за дополнительную плату — и Business Support. Она помогает подготовиться к масштабным событиям: запуску продукта или приложения, миграции инфраструктуры и маркетинговым мероприятиям.
</b></details>

<a id="aws-automation"></a>
#### Автоматизация в AWS

<details>
<summary>Что такое AWS CodeDeploy?</summary><br><b>

Определение Amazon: AWS CodeDeploy — полностью управляемый сервис, автоматизирующий развёртывание ПО на разных вычислительных платформах, включая Amazon EC2, AWS Fargate, AWS Lambda и локальные серверы.

Подробнее — [здесь](https://aws.amazon.com/codedeploy)
</b></details>

<details>
<summary>Объясните, что такое CloudFormation.</summary><br><b>
</b></details>

<a id="aws-misc"></a>
#### Прочие сервисы AWS

<details>
<summary>Что такое AWS Lightsail?</summary><br><b>

Определение AWS: Lightsail — простая облачная платформа со всем необходимым для создания приложения или сайта и доступным ежемесячным тарифом.
</b></details>

<details>
<summary>Что такое AWS Rekognition?</summary><br><b>

Определение AWS: Amazon Rekognition упрощает добавление анализа изображений и видео в приложения. Он использует проверенные масштабируемые технологии глубокого обучения и не требует от пользователя специальных знаний машинного обучения.

Подробнее — [здесь](https://aws.amazon.com/rekognition)
</b></details>

<details>
<summary>Для чего используются AWS Resource Groups?</summary><br><b>

Определение Amazon: группы ресурсов позволяют упорядочить ресурсы AWS и упрощают управление большим количеством ресурсов и автоматизацию задач над ними.

Подробнее — [здесь](https://docs.aws.amazon.com/ARG/latest/userguide/welcome.html)
</b></details>

<details>
<summary>Что такое AWS Global Accelerator?</summary><br><b>

Определение Amazon: AWS Global Accelerator — сервис, повышающий доступность и производительность приложений для пользователей в отдельных регионах или по всему миру.

Подробнее — [здесь](https://aws.amazon.com/global-accelerator)
</b></details>

<details>
<summary>Что такое AWS Config?</summary><br><b>

Определение Amazon: AWS Config позволяет оценивать и проверять конфигурации ресурсов AWS и проводить их аудит.

Подробнее — [здесь](https://aws.amazon.com/config)
</b></details>

<details>
<summary>Что такое AWS X-Ray?</summary><br><b>

Определение AWS: AWS X-Ray помогает разработчикам анализировать и отлаживать распределённые приложения в рабочей среде, в том числе приложения с микросервисной архитектурой.
Подробнее — [здесь](https://aws.amazon.com/xray)
</b></details>

<details>
<summary>Что такое AWS OpsWorks?</summary><br><b>

Определение Amazon из исходника: AWS OpsWorks — сервис управления конфигурацией, предоставляющий управляемые экземпляры Chef и Puppet.

Подробнее — [здесь](https://aws.amazon.com/opsworks)
</b></details>

<details>
<summary>Что такое AWS Service Catalog?</summary><br><b>

Определение Amazon: AWS Service Catalog позволяет организациям создавать и администрировать каталоги ИТ-сервисов, одобренных для использования в AWS.

Подробнее — [здесь](https://aws.amazon.com/servicecatalog)
</b></details>

<details>
<summary>Что такое AWS CAF?</summary><br><b>

Определение Amazon: AWS Professional Services разработала Cloud Adoption Framework (AWS CAF), чтобы помочь организациям спланировать и ускорить успешный переход в облако.

Подробнее — [здесь](https://aws.amazon.com/professional-services/CAF)
</b></details>

<details>
<summary>Что такое AWS Cloud9?</summary><br><b>

Определение AWS: AWS Cloud9 — облачная интегрированная среда разработки (IDE), позволяющая писать, запускать и отлаживать код в браузере.
</b></details>

<details>
<summary>Что такое AWS Application Discovery Service?</summary><br><b>

Определение Amazon: AWS Application Discovery Service помогает корпоративным заказчикам планировать миграцию, собирая сведения об их локальных центрах обработки данных.

Подробнее — [здесь](https://aws.amazon.com/application-discovery)
</b></details>

<details>
<summary>Что такое Trusted Advisor?</summary><br><b>
</b></details>

<details>
<summary>Что такое AWS Well-Architected Framework и на каких принципах он основан?</summary><br><b>

Определение AWS из исходника 2021 года: Well-Architected Framework помогает облачным архитекторам создавать безопасную, производительную, устойчивую и эффективную инфраструктуру приложений. В этой версии перечислены пять принципов: операционное совершенство, безопасность, надёжность, эффективность производительности и оптимизация затрат.

Подробнее — [здесь](https://aws.amazon.com/architecture/well-architected)
</b></details>

<details>
<summary>Какие сервисы AWS являются бессерверными или имеют бессерверный вариант?</summary><br><b>

AWS Lambda
AWS Athena
</b></details>

<details>
<summary>Что такое AWS EMR?</summary><br><b>

Определение AWS: платформа больших данных для обработки огромных объёмов информации с помощью инструментов с открытым исходным кодом: Apache Spark, Apache Hive, Apache HBase, Apache Flink, Apache Hudi и Presto.

Подробнее — [здесь](https://aws.amazon.com/emr)
</b></details>

<details>
<summary>Что такое AWS Athena?</summary><br><b>

Amazon Athena — сервис интерактивных запросов, упрощающий анализ данных в Amazon S3 с помощью стандартного SQL.

Подробнее — [здесь](https://aws.amazon.com/athena)
</b></details>

<details>
<summary>Что такое Amazon Cloud Directory?</summary><br><b>

Определение Amazon: Amazon Cloud Directory — высокодоступное многопользовательское хранилище каталогов в AWS. Каталоги автоматически масштабируются до сотен миллионов объектов в соответствии с потребностями приложений.

Подробнее — [здесь](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/what_is_cloud_directory.html)
</b></details>

<details>
<summary>Что такое AWS Elastic Beanstalk?</summary><br><b>

Определение AWS: AWS Elastic Beanstalk — простой сервис развёртывания и масштабирования веб-приложений и сервисов. Достаточно загрузить код, и Elastic Beanstalk автоматически выполняет развёртывание.

Подробнее — [здесь](https://aws.amazon.com/elasticbeanstalk)
</b></details>

<details>
<summary>Что такое AWS SWF?</summary><br><b>

Определение Amazon: Amazon SWF помогает создавать, запускать и масштабировать фоновые задания с параллельными или последовательными шагами. Его можно рассматривать как полностью управляемую облачную систему отслеживания состояния и координации задач.

Подробнее — [здесь](https://aws.amazon.com/swf)
</b></details>

<details>
<summary>Что такое Simple Queue Service (SQS)?</summary><br><b>

Определение AWS: Amazon Simple Queue Service (SQS) — полностью управляемый сервис очередей сообщений, позволяющий уменьшить связанность и масштабировать микросервисы, распределённые системы и бессерверные приложения.

Подробнее — [здесь](https://aws.amazon.com/sqs)
</b></details>

<a id="aws-disaster-recovery"></a>
#### Аварийное восстановление в AWS

<details>
<summary>Что означают RTO и RPO в контексте аварийного восстановления?</summary><br><b>

RTO — максимально допустимое время недоступности приложения.

RPO — максимально допустимая глубина потери данных при инциденте, выраженная во времени.
</b></details>

<details>
<summary>Какие подходы к аварийному восстановлению поддерживает AWS?</summary><br><b>

* Холодный резерв (Cold Method) — периодическое резервное копирование с хранением копий за пределами основной площадки.<br>
* Pilot Light — репликация данных в среду, минимальный набор компонентов которой постоянно работает.
* Тёплый резерв (Warm Standby) — постоянно работающая уменьшенная копия рабочей среды.
* Несколько площадок (Multi-site) — постоянно работающая дублирующая среда.
</b></details>

<details>
<summary>Какой вариант аварийного восстановления предполагает наибольший простой, а какой — наименьший?</summary><br><b>

Наименьший — Multi-site.
Наибольший — холодный резерв.
</b></details>

<a id="final-note"></a>
### Напоследок

Удачи! У вас всё получится :)
