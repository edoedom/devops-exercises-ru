> Актуализация названий: Azure Active Directory теперь Microsoft Entra ID, Azure ATP — Microsoft Defender for Identity. Windows Server Active Directory не переименован. Старые названия сохранены там, где нужны для понимания исходных команд и исторического контекста.

<a id="azure"></a>
# Azure

- [Azure](#azure)
  - [Вопросы](#questions)
    - [Основы Azure](#azure-101)
    - [Azure Resource Manager](#azure-resource-manager)
    - [Вычисления](#compute)
    - [Сеть](#network)
    - [Хранение данных](#storage)
    - [Безопасность](#security)

<a id="questions"></a>
## Вопросы

<a id="azure-101"></a>
### Основы Azure

<details>
<summary>Что такое портал Azure?</summary><br><b>

[Microsoft Docs](https://docs.microsoft.com/en-us/learn/modules/intro-to-azure-fundamentals/what-is-microsoft-azure): портал Azure — единая веб-консоль, служащая альтернативой инструментам командной строки. Она позволяет управлять подпиской Azure через графический интерфейс.
</b></details>

<details>
<summary>Что такое Azure Marketplace?</summary><br><b>

[Microsoft Docs](https://docs.microsoft.com/en-us/learn/modules/intro-to-azure-fundamentals/what-is-microsoft-azure): Azure Marketplace связывает пользователей с партнёрами Microsoft, независимыми поставщиками ПО и стартапами, предлагающими решения и услуги, оптимизированные для Azure.
</b></details>

<details>
<summary>Объясните, что такое группы доступности и зоны доступности.</summary><br><b>

Группа доступности (availability set) — логическое объединение виртуальных машин, позволяющее Azure учитывать устройство приложения при обеспечении резервирования и доступности. В исходном материале рекомендуется создавать не менее двух ВМ в одной группе для высокой доступности приложения и выполнения SLA Azure 99,95%.
</b></details>

<details>
<summary>Что такое Azure Policy?</summary><br><b>

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/governance/policy/overview): Azure Policy помогает применять стандарты организации и оценивать соответствие им в большом масштабе. Панель соответствия показывает общее состояние среды с возможностью перейти к отдельным ресурсам и политикам. Также сервис позволяет массово исправлять несоответствия существующих ресурсов и автоматически исправлять их для новых.
</b></details>

<details>
<summary>Объясните, что такое управляемые диски Azure.</summary><br><b>

Azure Managed Disks — управляемые блочные тома для ВМ; Azure обслуживает инфраструктуру хранения. Выбирают тип, размер, производительность и резервирование с учётом нагрузки и зоны. Диск не становится общей файловой системой сам по себе. [Managed disks](https://learn.microsoft.com/en-us/azure/virtual-machines/managed-disks-overview).
</b></details>

<a id="azure-resource-manager"></a>
### Azure Resource Manager

<details>
<summary>Что такое Azure Resource Manager?</summary><br><b>

[Документация Azure](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/overview): Azure Resource Manager — сервис развёртывания и управления Azure. Он предоставляет уровень управления, позволяющий создавать, обновлять и удалять ресурсы в учётной записи. Управление доступом, блокировки и теги помогают защищать и организовывать ресурсы после развёртывания.
</b></details>

<details>
<summary>Из каких разделов состоит шаблон ARM?</summary><br><b>

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/overview): шаблон содержит следующие разделы:

* Parameters — значения, передаваемые при развёртывании, чтобы один шаблон можно было использовать в разных средах.
* Variables — повторно используемые значения. Их можно вычислять на основе параметров.
* User-defined functions — пользовательские функции, упрощающие шаблон.
* Resources — развёртываемые ресурсы.
* Outputs — значения, возвращаемые после развёртывания ресурсов.
</b></details>

<details>
<summary>Что такое группа ресурсов Azure?</summary><br><b>

[Документация Azure](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal): группа ресурсов — контейнер для связанных ресурсов решения Azure. Она может включать все ресурсы решения либо только те, которыми нужно управлять совместно.
</b></details>

<a id="compute"></a>
### Вычисления

<details>
<summary>Какие вычислительные сервисы Azure вы знаете?</summary><br><b>

* Azure Virtual Machines.
* Azure Batch.
* Azure Service Fabric.
* Azure Container Instances.
* Azure Virtual Machine Scale Sets.
</b></details>

<details>
<summary>Для чего используется Azure Virtual Machines?</summary><br><b>

Виртуальные машины Azure поддерживают Windows и Linux. На них можно размещать веб-серверы, приложения, резервные копии и базы данных, использовать их как промежуточные серверы доступа или самостоятельно размещаемые агенты Azure для сборки и развёртывания приложений.
</b></details>

<details>
<summary>Для чего используется Azure Virtual Machine Scale Sets?</summary><br><b>

Для масштабирования виртуальных машин Linux или Windows. Сервис позволяет создавать группы ВМ с балансировкой нагрузки и управлять ими. Количество экземпляров может автоматически увеличиваться или уменьшаться в зависимости от спроса либо по расписанию.
</b></details>

<details>
<summary>Для чего используется Azure Functions?</summary><br><b>

Azure Functions — сервис бессерверных вычислений Azure.
</b></details>

<details>
<summary>Что такое Durable Functions в Azure?</summary><br>

[Microsoft Learn](https://docs.microsoft.com/en-us/learn/modules/intro-to-azure-fundamentals/what-is-microsoft-azure): Durable Functions — расширение Azure Functions для написания функций с сохранением состояния в бессерверной вычислительной среде.
</details>

<details>
<summary>Для чего используется Azure Container Instances?</summary><br><b>

Для запуска приложений в контейнерах без необходимости самостоятельно выделять виртуальные машины.
</b></details>

<details>
<summary>Для чего используется Azure Batch?</summary><br><b>

Для запуска приложений параллельных и высокопроизводительных вычислений.
</b></details>

<details>
<summary>Для чего используется Azure Service Fabric?</summary><br><b>

Платформа управления распределёнными приложениями, включая stateful и stateless сервисы и контейнеры. Это отдельная платформа, не другое название AKS; учитывайте поддерживаемые модели приложения и эксплуатационные требования. [Service Fabric](https://learn.microsoft.com/en-us/azure/service-fabric/service-fabric-overview).
</b></details>

<details>
<summary>Для чего используется Azure Kubernetes Service?</summary><br><b>

Управляемый Kubernetes в Azure: сервис обслуживает control plane, но клиент отвечает за нагрузки, права, сеть, настройки node pools и свою часть обновлений. Не является «полностью безадминистраторским» запуском любого приложения. [AKS](https://learn.microsoft.com/en-us/azure/aks/what-is-aks).
</b></details>

<a id="network"></a>
### Сеть

<details>
<summary>Какие сетевые сервисы Azure вы знаете?</summary><br><b>

VNet, subnet, NSG, Load Balancer, Application Gateway, Front Door, VPN Gateway, ExpressRoute, DNS и Private Link. Они решают разные задачи L3/L4/L7, приватного доступа и связности; выбирайте по требованиям. [Azure networking](https://learn.microsoft.com/en-us/azure/networking/fundamentals/networking-overview).
</b></details>

<details>
<summary>Объясните пиринг виртуальных сетей VNet.</summary><br><b>

Пиринг VNet соединяет виртуальные сети, позволяя передавать трафик между их ресурсами по частным IPv4-адресам. Соединение сетей внутри одного региона называется региональным пирингом VNet, а между регионами Azure — глобальным пирингом VNet.
</b></details>

<details>
<summary>Что такое регион Azure?</summary><br><b>

Регион Azure — совокупность центров обработки данных, расположенных в определённой географической области и соединённых выделенной региональной сетью с низкой задержкой.
</b></details>

<details>
<summary>Что такое N-уровневая архитектура?</summary><br><b>

Такая архитектура разделяет приложение на логические слои и физические уровни. У каждого слоя своя ответственность. Физические уровни работают на отдельных машинах. Логическая архитектура может быть закрытой или открытой. Обычно N-уровневые приложения реализуются по модели IaaS: каждый уровень работает на отдельном наборе виртуальных машин.
</b></details>

<a id="storage"></a>
### Хранение данных

<details>
<summary>Какие сервисы хранения Azure вы знаете?</summary><br><b>

Blob Storage, Azure Files, Managed Disks и Queue/Table Storage для соответствующих моделей. Azure SQL/Cosmos DB — сервисы БД, а не разновидности диска. Сравнивайте API, доступность, задержку и стоимость операций, а не только цену гигабайта.
</b></details>

<details>
<summary>Какие варианты хранения данных поддерживает Azure?</summary><br><b>

Объектное, файловое, блочное, очереди и NoSQL-таблицы в составе Azure Storage; также специализированные БД. Резервирование LRS/ZRS/GRS и другие варианты описывают размещение копий, а не тип пользовательского API.
</b></details>

<a id="security"></a>
### Безопасность

<details>
<summary>Что такое Azure Security Center? Назовите его возможности.</summary><br><b>

Сервис мониторинга и защиты от угроз для сервисов Azure. В исходнике перечислены следующие возможности:

* Рекомендации по безопасности на основе использования ресурсов.
* Непрерывное наблюдение за настройками безопасности и сервисами.
* Анализ и выявление потенциальных внешних атак.
* Обнаружение и блокировка вредоносного ПО с применением машинного обучения.
</b></details>

<details>
<summary>Что такое Azure Active Directory?</summary><br><b>

Azure AD — облачный сервис управления удостоверениями. Его можно использовать самостоятельно либо интегрировать с уже работающей службой Active Directory.
</b></details>

<details>
<summary>Что такое Microsoft Defender for Identity (ранее Azure ATP)?</summary><br><b>

Историческое название Azure ATP теперь соответствует Microsoft Defender for Identity — обнаружению и расследованию угроз идентичностям. Не путайте с Defender for Cloud и Microsoft Entra ID Protection. [Microsoft](https://learn.microsoft.com/en-us/defender-for-identity/what-is).
</b></details>

<details>
<summary>Какие компоненты входят в Azure ATP?</summary><br><b>

Для исторической архитектуры Azure ATP — облачный сервис и sensors на поддерживаемых источниках, в частности контроллерах домена; существовал standalone sensor. Современную архитектуру, версии сенсоров и требования проверяйте по Defender for Identity: старую схему нельзя выдавать за универсальную актуальную. [Overview](https://learn.microsoft.com/en-us/defender-for-identity/what-is).
</b></details>

<details>
<summary>Где хранятся журналы Azure Monitor?</summary><br><b>

Azure Monitor Logs организованы в Log Analytics workspaces; маршрутизация platform/resource logs зависит от diagnostic settings и сервиса, возможны также Storage/Event Hubs. Метрики и журналы — разные подсистемы. Retention, регион и права задаются конфигурацией, данные не «всегда хранятся автоматически навсегда».
</b></details>

<details>
<summary>Объясните назначение Azure Site Recovery.</summary><br><b>

Репликация и оркестрация аварийного переключения поддерживаемых нагрузок между площадками/регионами. Нужны recovery plan, проверка зависимостей, тестовый failover и возврат. Site Recovery не заменяет независимые резервные копии. [ASR](https://learn.microsoft.com/en-us/azure/site-recovery/site-recovery-overview).
</b></details>

<details>
<summary>Что делает Azure Advisor?</summary><br><b>

Рекомендации по надёжности, безопасности, производительности, затратам и эксплуатации ресурсов Azure. Их применимость оценивает владелец нагрузки; Advisor не гарантирует автоматически оптимальную архитектуру. [Advisor](https://learn.microsoft.com/en-us/azure/advisor/advisor-overview).
</b></details>

<details>
<summary>Какие протоколы доступны для настройки проверки работоспособности?</summary><br><b>

Вопрос требует назвать сервис. У Azure Load Balancer используются TCP, HTTP и HTTPS probes; у Application Gateway HTTP(S), у Traffic Manager HTTP/HTTPS/TCP. Параметры порта, пути, ожидания и реакции на отказ различаются — нельзя переносить один health-check между всеми сервисами без уточнения.
</b></details>

<details>
<summary>Что такое Microsoft Entra ID (ранее Azure Active Directory)?</summary><br><b>

Вероятно, имеется в виду Azure Active Directory — теперь Microsoft Entra ID, облачная служба идентификации и управления доступом. Это не Windows Server Active Directory и не прямая замена контроллеру домена с теми же протоколами. [Новое название](https://learn.microsoft.com/en-us/entra/fundamentals/new-name).
</b></details>

<details>
<summary>Что такое подписка? Какие бывают типы подписок?</summary><br><b>

Подписка — граница учёта ресурсов, квот, доступа и биллинга, связанная с tenant Microsoft Entra. Предложения могут включать pay-as-you-go, корпоративные и тестовые/учебные; доступность и условия меняются. Management group, subscription и resource group — разные уровни организации, tenant не равен подписке.
</b></details>

<details>
<summary>Объясните назначение сервиса Blob Storage.</summary><br><b>

Объектное хранение неструктурированных данных: файлы, медиа, backup, данные аналитики. Доступ через соответствующие API и уровни доступа; настройте RBAC/SAS, публичность, жизненный цикл и защиту от удаления. Blob не предоставляет автоматически обычную POSIX-семантику диска. [Blob](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction).
</b></details>
