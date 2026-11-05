<a id="openshift"></a>
## OpenShift

<a id="openshift-exercises"></a>
### Упражнения по OpenShift

|Название|Тема|Цель и инструкции|Решение|Комментарии|
|--------|--------|------|----|----|
| Основы проектов | Проекты | [Задание](projects_101.md) | [Решение](solutions/projects_101.md)
| Моё первое приложение | Приложения | [Задание](solutions/my_first_app.md#objectives) | [Решение](solutions/my_first_app.md)

<a id="openshift-self-assessment"></a>
### Самопроверка по OpenShift

* [Основы OpenShift](#Openshift-101)
* [Архитектура OpenShift](#Openshift-architecture)
* [Практические основы OpenShift](#Openshift-hands-on-basics)
* [Проекты OpenShift](#Openshift-projects)

<a name="openshift-101"></a>
<a id="openshift-101"></a>
### Основы OpenShift

<details>
<summary>Что такое OpenShift?</summary><br><b>

OpenShift — платформа оркестрации контейнеров на основе Kubernetes.<br>
Она позволяет развёртывать приложения с небольшими затратами на администрирование.
</b></details>

<details>
<summary>Как OpenShift связан с Kubernetes?</summary><br><b>

OpenShift построен на Kubernetes и добавляет собственные ресурсы к его встроенным ресурсам.
</b></details>

<details>
<summary>Верно ли, что OpenShift — решение IaaS, то есть инфраструктура как услуга?</summary><br><b>

Нет. OpenShift относится к PaaS — платформе как услуге.
</b></details>

<details>
<summary>Верно ли, что CLI OpenShift поддерживает возможности kubectl и предоставляет дополнительные функции?</summary><br><b>

Да.
</b></details>

<details>
<summary>Какие возможности OpenShift добавляет к Kubernetes?</summary><br><b>

* Интерфейс: единый пользовательский интерфейс из коробки.
* Маршруты: простой способ открыть доступ к сервисам.
* Поддержка разработки: CI/CD через OpenShift Pipelines, встроенный реестр контейнеров и средства сборки образов из исходного кода.
</b></details>

<details>
<summary>Верно ли, что для запуска контейнеров в OpenShift нужны права root?</summary><br><b>

Нет. OpenShift по умолчанию поддерживает запуск контейнеров без прав root.
</b></details>

<a name="openshift-architecture"></a>
<a id="openshift---architecture"></a>
## OpenShift — архитектура

<details>
<summary>Какие типы узлов есть в OpenShift?</summary><br><b>

* Рабочие узлы (workers): на них выполняются пользовательские приложения.
* Управляющие узлы (masters): отвечают за управление кластером.
</b></details>

<details>
<summary>Какой компонент определяет размещение подов?</summary><br><b>

Планировщик (scheduler).
</b></details>

<details>
<summary>За что ещё отвечает планировщик, кроме размещения подов?</summary><br><b>

Он способствует высокой доступности приложений, распределяя реплики подов между рабочими узлами.
</b></details>

<a name="openshift-hands-on-basics"></a>
<a id="openshift---hands-on-basics"></a>
## OpenShift — практические основы

<details>
<summary>OpenShift поддерживает много ресурсов. Как получить их список?</summary><br><b>

`oc api-resources`
</b></details>

<details>
<summary>Объясните назначение CLI OpenShift: <code>oc</code> и <code>odo</code>.</summary><br><b>

oc используется как для создания приложений, так и для администрирования кластера OpenShift.<br>
odo предназначен для управления приложениями с точки зрения разработчика и не предназначен для администрирования кластера.
</b></details>

<a name="openshift-projects"></a>
<a id="openshift---projects"></a>
## OpenShift — проекты

<details>
<summary>Что такое проект OpenShift?</summary><br><b>

Проект OpenShift — пространство имён Kubernetes с аннотациями.<br>
Проще говоря, это изолированная среда, в которой пользователи организуют свои ресурсы: Pod, Deployment, Service и другие.
</b></details>

<details>
<summary>Как вывести все проекты? Что означает столбец STATUS в списке?</summary><br><b>

`oc get projects` выводит список проектов. Столбец STATUS позволяет увидеть, какие из них сейчас активны.
</b></details>

<details>
<summary>Как назначить новому участнику команды роль admin в вашем проекте OpenShift?</summary><br><b>

`oc adm policy add-role-to-user <role> <user> -n <project>`
</b></details>

<a id="openshift---applications"></a>
#### OpenShift — приложения

<details>
<summary>Как создать приложение MySQL из образа Docker Hub?</summary><br><b>

`oc new-app mysql`
</b></details>

<a id="openshift---images"></a>
#### OpenShift — образы

<details>
<summary>Что такое поток образов (image stream)?</summary><br><b>
</b></details>

<details>
<summary>Как лучше запускать несколько сред OpenShift и управлять ими?</summary><br><b>

В исходнике предлагается федерация.
</b></details>

<a id="openshift---federation"></a>
#### OpenShift — федерация

<details>
<summary>Что такое федерация OpenShift?</summary><br><b>

Управление сервисами и рабочими нагрузками нескольких независимых кластеров и их развёртывание через единый API.
</b></details>

<details>
<summary>Объясните термины в контексте федерации:

* Multi Cluster.
* Federated Cluster.
* Host Cluster.
* Member Cluster.
</summary><br><b>

* Multi Cluster — несколько независимо развёрнутых кластеров, не знающих друг о друге.
* Federated Cluster — несколько кластеров под управлением плоскости управления федерации OpenShift.
* Host Cluster — кластер, в котором работает плоскость управления федерации.
* Member Cluster — кластер, входящий в федерацию и подключённый к её плоскости управления.
</b></details>

<a id="openshift---storage"></a>
## OpenShift — хранение данных

<details>
<summary>Что такое устройство хранения данных? Какие устройства бывают?</summary><br><b>

* Жёсткие диски.
* SSD.
* USB-накопители.
* Магнитные ленты.
</b></details>

<details>
<summary>Что такое время произвольного доступа?</summary><br><b>

Время, необходимое накопителю для доступа к месту хранения данных и чтения одного блока или сектора.

Дополнительный вопрос: каково это время у SSD и магнитного диска?
В исходнике приведены ориентиры: около 10 мс для магнитного диска и 0,08–0,16 мс для SSD. Конкретные значения зависят от устройства и нагрузки.
</b></details>

<a id="openshift---pods"></a>
#### OpenShift — поды

<details>
<summary>Что происходит, если под перестаёт работать из-за аварийного завершения контейнера?</summary><br><b>

В исходнике перезапуск приписан управляющему узлу. Точнее: kubelet на рабочем узле перезапускает контейнер согласно restartPolicy. Если нужен новый под взамен удалённого или утраченного, его создаёт соответствующий контроллер.
</b></details>

<details>
<summary>Что происходит, если контейнер пода слишком часто завершается с ошибкой?</summary><br><b>

Между повторными запусками применяется увеличивающаяся задержка — backoff; это может отображаться как CrashLoopBackOff. В исходнике это упрощённо описано как временный отказ от перезапуска «плохого» пода управляющим узлом.
</b></details>

<details>
<summary>Как узнать, на каком узле работает под?</summary><br><b>

`oc get po -o wide`
</b></details>

<a id="openshift---services"></a>
#### OpenShift — сервисы

<details>
<summary>Объясните назначение и преимущества сервисов.</summary><br><b>

* Сервисы задают способ доступа к наборам подов.<br>
* Они обеспечивают связь между приложениями.
* Предоставляют приложениям стабильные внутренние IP-адреса и имена хостов.
* Позволяют выполнять базовую внутреннюю балансировку нагрузки.
</b></details>

<a id="openshift---labels"></a>
#### OpenShift — метки

<details>
<summary>Что такое метки и когда их используют?</summary><br><b>

* Метки позволяют группировать и выбирать объекты API.
* Это пары «ключ — значение» в метаданных объектов.
* Типичный пример — объединение подов, сервисов и развёртываний одного приложения.
</b></details>

<a id="openshift---service-accounts"></a>
#### OpenShift — сервисные учётные записи

<details>
<summary>Как вывести список сервисных учётных записей?</summary><br><b>

`oc get serviceaccounts`
</b></details>

<a id="openshift---networking"></a>
#### OpenShift — сеть

<details>
<summary>Что такое Route?</summary><br><b>

Route открывает внешний доступ к сервису, назначая ему доступное извне имя хоста.
</b></details>

<details>
<summary>Из чего состоит Route?</summary><br><b>

* Имя.
* Указание сервиса.
* Необязательные настройки безопасности.
</b></details>

<details>
<summary>Верно ли, что контейнер маршрутизатора может работать только на управляющем узле?</summary><br><b>

Нет. Он может работать и на других узлах.
</b></details>

<details>
<summary>Приведите пример работы маршрутизатора.</summary><br><b>

1. Клиент обращается по адресу приложения OpenShift.
2. DNS разрешает имя в адрес узла с маршрутизатором.
3. Маршрутизатор проверяет наличие маршрута.
4. Маршрутизатор проксирует запрос внутреннему поду.
</b></details>

<a id="openshift---security"></a>
#### OpenShift — безопасность

<details>
<summary>Что такое Security Context Constraints?</summary><br><b>

[Документация OpenShift](https://docs.openshift.com/container-platform/4.7/authentication/managing-security-context-constraints.html): подобно тому, как RBAC управляет доступом пользователей, ограничения контекста безопасности (SCC) позволяют администраторам управлять разрешениями подов.
</b></details>

<details>
<summary>Как дать пользователю user1 возможность просматривать проект wonderland, если у вас есть необходимые полномочия?</summary><br><b>

`oc adm policy add-role-to-user view user1 -n wonderland`
</b></details>

<details>
<summary>Как проверить текущий контекст?</summary><br><b>

`oc whoami --show-context`
</b></details>

<a id="openshift---serverless"></a>
#### OpenShift — бессерверные вычисления

<details>
<summary>Что такое OpenShift Serverless?</summary><br><b>

* Serverless — модель облачных вычислений, в которой выделение ресурсов и масштабирование выполняются платформой, позволяя разработчикам сосредоточиться на приложении.
* OpenShift Serverless обеспечивает динамическое масштабирование и создание приложений, реагирующих на события из Kubernetes, облачных сервисов и локальной инфраструктуры.
* OpenShift Serverless основан на проекте Knative.
</b></details>

<details>
<summary>Какие источники событий можно использовать с OpenShift Serverless?</summary><br><b>

* Kafka.
* API Kubernetes.
* AWS Kinesis.
* AWS SQS.
* JIRA.
* Slack.

OpenShift поддерживает и другие источники.
</b></details>

<details>
<summary>Объясните, что такое бессерверные функции.</summary><br><b>
</b></details>

<details>
<summary>Чем бессерверные контейнеры отличаются от бессерверных функций?</summary><br><b>
</b></details>

<a id="openshift---misc"></a>
#### OpenShift — разное

<details>
<summary>Что такое Replication Controller?</summary><br><b>

Контроллер репликации поддерживает заданное количество подов.<br>
Если подов больше, чем требуется, он удаляет лишние.<br>
Если меньше — создаёт недостающие.
</b></details>
