<a id="kubernetes"></a>
# Kubernetes

<!-- {% raw %} -->

Какова ваша цель?

* Подготовиться к сертификации CKA.
  * Откройте страницу [CKA](CKA.md).
* Изучить Kubernetes, сочетая теорию и практику.
  * Выполняйте [упражнения](#kubernetes-exercises).
  * Отвечайте на [вопросы](#kubernetes-questions).
* Освоить Kubernetes на практике.
  * Выполняйте [упражнения](#kubernetes-exercises).

- [Kubernetes](#kubernetes)
  - [Упражнения Kubernetes](#kubernetes-exercises)
    - [Поды](#pods)
    - [Service](#service)
    - [ReplicaSet](#replicaset)
    - [Метки и селекторы](#labels-and-selectors)
    - [Планировщик](#scheduler)
    - [Kustomize](#kustomize)
  - [Вопросы Kubernetes](#kubernetes-questions)
    - [Основы Kubernetes](#kubernetes-101)
    - [Кластер и архитектура](#cluster-and-architecture)
      - [Kubelet](#kubelet)
      - [Команды для узлов](#nodes-commands)
    - [Поды](#pods-1)
      - [Статические поды](#static-pods)
      - [Команды для подов](#pods-commands)
      - [Диагностика подов](#pods-troubleshooting-and-debugging)
    - [Метки и селекторы](#labels-and-selectors-1)
    - [Deployments](#deployments)
      - [Команды для Deployment](#deployments-commands)
    - [Services](#services)
    - [Ingress](#ingress)
    - [ReplicaSets](#replicasets)
    - [DaemonSet](#daemonset)
      - [Команды для DaemonSet](#daemonset---commands)
    - [StatefulSet](#statefulset)
    - [Хранение данных](#storage)
      - [Тома](#volumes)
    - [Сеть](#networking)
    - [Сетевые политики](#network-policies)
    - [etcd](#etcd)
    - [Пространства имён](#namespaces)
      - [Команды для namespace](#namespaces---commands)
      - [Квоты ресурсов](#resources-quota)
    - [Операторы](#operators)
    - [Секреты](#secrets)
    - [Тома](#volumes-1)
    - [Управление доступом](#access-control)
    - [Паттерны](#patterns)
    - [CronJob](#cronjob)
    - [Разное](#misc)
    - [Gatekeeper](#gatekeeper)
    - [Проверка политик](#policy-testing)
    - [Helm](#helm)
      - [Команды](#commands)
    - [Безопасность](#security)
    - [Сценарии диагностики](#troubleshooting-scenarios)
    - [Istio](#istio)
    - [Контроллеры](#controllers)
    - [Планировщик](#scheduler-1)
      - [Привязка к узлам](#node-affinity)
    - [Ограничения taint](#taints)
    - [Лимиты ресурсов](#resource-limits)
      - [Команды для лимитов ресурсов](#resources-limits---commands)
    - [Мониторинг](#monitoring)
    - [Kustomize](#kustomize-1)
    - [Стратегии развёртывания](#deployment-strategies)
    - [Практические ситуации](#scenarios)

<a id="kubernetes-exercises"></a>
## Упражнения Kubernetes

<a id="pods"></a>
### Поды

|Название|Тема|Цель и инструкции|Решение|Комментарии|
|--------|--------|------|----|----|
|Мой первый под|Поды|[Задание](pods_01.md)|[Решение](solutions/pods_01_solution.md)
|Завершение контейнеров|Поды|[Задание](killing_containers.md)|[Решение](solutions/killing_containers.md)

<a id="service"></a>
### Service

|Название|Тема|Цель и инструкции|Решение|Комментарии|
|--------|--------|------|----|----|
|Создание Service|Service|[Задание](services_01.md)|[Решение](solutions/services_01_solution.md)

<a id="replicaset"></a>
### ReplicaSet

|Название|Тема|Цель и инструкции|Решение|Комментарии|
|--------|--------|------|----|----|
|Создание ReplicaSet|ReplicaSet|[Задание](replicaset_01.md)|[Решение](solutions/replicaset_01_solution.md)
|Управление ReplicaSet|ReplicaSet|[Задание](replicaset_02.md)|[Решение](solutions/replicaset_02_solution.md)
|Селекторы ReplicaSet|ReplicaSet|[Задание](replicaset_03.md)|[Решение](solutions/replicaset_03_solution.md)

<a id="labels-and-selectors"></a>
### Метки и селекторы

|Название|Тема|Цель и инструкции|Решение|Комментарии|
|--------|--------|------|----|----|
|Основы меток и селекторов|Labels, Selectors|[Задание](exercises/labels_and_selectors/exercise.md)|[Решение](exercises/labels_and_selectors/solution.md)
|Селекторы узлов|Labels, Selectors|[Задание](exercises/node_selectors/exercise.md)|[Решение](exercises/node_selectors/solution.md)


<a id="scheduler"></a>
### Планировщик

|Название|Тема|Цель и инструкции|Решение|Комментарии|
|--------|--------|------|----|----|
|Основы taints|Ограничения taint|[Задание](exercises/taints_101/exercise.md)|[Решение](exercises/taints_101/solution.md)

<a id="kustomize"></a>
### Kustomize

|Название|Тема|Цель и инструкции|Решение|Комментарии|
|--------|--------|------|----|----|
|Общие метки|Kustomize|[Задание](exercises/kustomize_common_labels/exercise.md)|[Решение](exercises/kustomize_common_labels/solution.md)

<a id="kubernetes-questions"></a>
## Вопросы Kubernetes

<a id="kubernetes-101"></a>
### Основы Kubernetes

<details>
<summary>Что такое Kubernetes? Зачем его используют организации?</summary><br><b>

Открытая система развёртывания, масштабирования и управления контейнерными приложениями.

Примеры задач:

* Запуск приложения в контейнерах на разных узлах и согласованное применение изменений.
* Обновление сотен контейнеров.
* Увеличение или уменьшение числа экземпляров в зависимости от нагрузки.

</b></details>

<details>
<summary>Когда Kubernetes может быть не нужен?</summary><br><b>

  - Если задача — только управление физическими серверами или низкоуровневой инфраструктурой, Kubernetes сам по себе её не решает.
  - Для небольшой команды и малого числа контейнеров его сложность может быть избыточной. Управляемый сервис снижает нагрузку на эксплуатацию, но решение нужно принимать по требованиям, а не по произвольному числу инженеров.

</b></details>

<details>
<summary>Какие возможности есть у Kubernetes?</summary><br><b>

  - Самовосстановление: проверки состояния и действия при сбоях, например перезапуск контейнера.
  - Балансировка трафика между подходящими подами приложения.
  - Операторы: автоматизация управления приложениями через API и реакции на изменения состояния.
  - Постепенное развёртывание обновлений и возможность отката.
  - Горизонтальное масштабирование по показателям и заданным правилам.
  - Secrets: механизм передачи чувствительных данных с контролем доступа. Сам объект Secret не гарантирует шифрование хранения.

</b></details>

<details>
<summary>Какие объекты Kubernetes вы знаете?</summary><br><b>

  * Pod
  * Service
  * ReplicationController
  * ReplicaSet
  * DaemonSet
  * Namespace
  * ConfigMap
  ...
</b></details>

<details>
<summary>Какие поля нужны в манифесте объекта Kubernetes?</summary><br><b>

`apiVersion`, `kind`, `metadata`; остальные обязательные поля зависят от типа объекта.

</b></details>

<details>
<summary>Что такое kubectl?</summary><br><b>

CLI Kubernetes для работы с кластером: развёртывания приложений, просмотра и управления ресурсами, чтения журналов.

</b></details>

<details>
<summary>Какие объекты обычно нужны для развёртывания приложения?</summary><br><b>

* Deployment — управляет ReplicaSet и через него подами.
* Service — обеспечивает стабильный доступ и направление трафика к подам.
* Ingress — правила входящего HTTP(S)-трафика, реализуемые Ingress-контроллером.

</b></details>

<details>
<summary>Почему нет команды <code>kubectl get containers</code>?</summary><br><b>

Контейнер не является самостоятельным API-объектом Kubernetes. Единица запуска — Pod, содержащий один или несколько контейнеров.

</b></details>

<details>
<summary>Каких рекомендаций по Kubernetes вы придерживаетесь?</summary><br><b>

  - Проверяйте манифесты YAML автоматически в конвейере.
  - Настраивайте requests и limits по потребностям приложения, чтобы управлять размещением и потреблением ресурсов.
  - Используйте метки для группировки и идентификации подов, Deployment и других объектов.

</b></details>

<a id="cluster-and-architecture"></a>
### Кластер и архитектура

<details>
<summary>Что такое кластер Kubernetes?</summary><br><b>

По определению Red Hat, это набор узлов для запуска контейнерных приложений.
Он содержит компоненты управления и вычислительные узлы; в небольшом кластере роли могут совмещаться на одной машине.

Подробнее — [здесь](https://www.redhat.com/en/topics/containers/what-is-a-kubernetes-cluster).
</b></details>

<details>
<summary>Что такое узел (Node)?</summary><br><b>

Физическая или виртуальная машина, предоставляющая ресурсы для запуска подов.<br>
Число узлов рабочей среды выбирают по нагрузке и требованиям отказоустойчивости. Исходник рекомендует минимум три, но это не универсальное требование.
</b></details>

<details>
<summary>За что отвечает управляющий узел?</summary><br><b>

Компоненты управления координируют работу кластера:

* Планирование размещения приложений.
* Поддержание желаемого состояния.
* Развёртывание обновлений.

</b></details>

<details>
<summary>Что в общих чертах происходит при <code>kubectl get nodes</code>?</summary><br><b>

1. Запрос аутентифицируется.
2. API-сервер проверяет права и обрабатывает запрос.
3. Возвращаются сведения об узлах из состояния кластера, хранимого в etcd; возможна выдача через кеш API-сервера.
</b></details>

<details>
<summary>Верно ли, что кластер может иметь ноль управляющих узлов, но обязан иметь хотя бы один рабочий?</summary><br><b>

Неверно. Для работы необходим control plane. Выделенных рабочих узлов может не быть, например при совмещении ролей.

</b></details> 

<details>
<summary>Какие компоненты входят в control plane?</summary><br><b>

  * API Server — API Kubernetes, через который взаимодействуют компоненты.
  * Scheduler — выбирает узел для ещё не назначенного пода.
  * Controller Manager — контроллеры состояния кластера: реплики, узлы и другие ресурсы.
  * etcd — хранилище состояния и конфигурации кластера.

</b></details>

<details>
<summary>Какие компоненты работают на рабочем узле?</summary><br><b>

  * Kubelet — агент управления подами узла и взаимодействия с API-сервером.
  * Kube-proxy — реализация сетевых правил Service; в некоторых сетевых решениях заменяется другим механизмом.
  * Контейнерная среда выполнения с интерфейсом CRI, например containerd или CRI-O. Уточнение: Podman и Docker не являются прямой заменой CRI-runtime без дополнительной интеграции.

</b></details>

<details>
<summary>Разместите компоненты справа в соответствующих местах схемы.<br>
<img src="images/cluster_architecture_exercise.png"/>
</summary><br><b>

Control plane включает API server, etcd, scheduler и controller manager; на worker работают kubelet, container runtime и сетевой dataplane. На исходной схеме ниже runtime не показан. Несколько scheduler/controller-manager обычно используют leader election; это не означает, что каждый независимо назначает все поды. kube-proxy может заменяться иной реализацией dataplane. <img src="images/cluster_architecture_solution.png"/>
</b></details>

<details>
<summary>Как быстро переключать kubectl между несколькими кластерами?</summary><br><b>

`kubectl config use-context`
</b></details>

<details>
<summary>Как ограничить высокое потребление памяти и риск OOM в кластере?</summary><br><b>

Настроить requests и limits, особенно для сторонних приложений. Это ограничивает потребление, но не устраняет сами утечки памяти.
</b></details>

<details>
<summary>Есть ли у вас опыт развёртывания Kubernetes? Опишите основные шаги.</summary><br><b>

1. Подготовить управляющие и рабочие узлы: облачные экземпляры, виртуальные или физические машины.
2. Настроить центр сертификации для TLS-сертификатов компонентов, включая kubelet и etcd.
   1. Создать соответствующие сертификаты и закрытые ключи.
3. Подготовить kubeconfig с адресами API-серверов и данными аутентификации.
4. Подготовить ключ и настройки шифрования сохраняемых данных.
5. Развернуть etcd. Это начало ручного процесса, а не полный перечень установки кластера.
</b></details>

<details>
<summary>Какая команда выводит доступные типы API-ресурсов?</summary><br><b>

`kubectl api-resources`
</b></details>

<details>
<summary>Что делает kubectl get componentstatus?</summary><br><b>

Исторически выводит состояние компонентов control plane. API ComponentStatus устарел, поэтому не следует считать его надёжной полной проверкой современного кластера.
</b></details>

<a id="kubelet"></a>
#### Kubelet

<details>
<summary>Что будет с подами, если остановить kubelet на рабочем узле?</summary><br><b>

Уже запущенные контейнеры могут продолжать работать, но kubelet перестанет управлять ими и отправлять состояние. После тайм-аутов узел признаётся недоступным; контроллеры могут создать заменяющие поды на других узлах. Поды не «переезжают»: создаются новые объекты, а поведение зависит от контроллеров и tolerations.
</b></details>

<a id="nodes-commands"></a>
#### Команды для узлов

<details>
<summary>Выведите все узлы кластера.</summary><br><b>

`kubectl get nodes`

Можно создать псевдоним `alias k=kubectl` и использовать `k get no`.
</b></details>

<details>
<summary>Сохраните список узлов в JSON-файл some_nodes.json.</summary><br><b>

`k get nodes -o json > some_nodes.json`
</b></details>

<details>
<summary>Посмотрите метки одного из узлов.</summary><br><b>

`k get no minikube --show-labels`
</b></details>

<a id="pods-1"></a>
### Поды

<details>
<summary>Что такое Pod?</summary><br><b>

Группа одного или нескольких контейнеров с общими сетевыми ресурсами, подключаемыми томами и спецификацией запуска.

Pod — минимальная единица развёртывания вычислительной нагрузки Kubernetes.

</b></details>

<details>
<summary>Запустите под my-pod из nginx:alpine.</summary><br><b>

`kubectl run my-pod --image=nginx:alpine`

На практике поды обычно создаёт контроллер, например Deployment, а не пользователь напрямую.

Конфигурации подов и Deployment обычно хранят в манифестах, а не только в аргументах CLI.
</b></details>

<details>
<summary>Как вы понимаете фразу «поды не следует создавать напрямую»?</summary><br><b>

Обычно ими управляют Deployment, ReplicaSet и другие контроллеры.

Самостоятельный под после удаления не восстанавливается контроллером. ReplicaSet, напротив, создаёт замену для поддержания заданного числа реплик. Это отличается от перезапуска контейнера внутри существующего пода.
</b></details>

<details>
<summary>Сколько контейнеров может быть в поде?</summary><br><b>

Несколько, хотя распространён вариант с одним основным контейнером приложения.

Например, паттерн sidecar добавляет вспомогательный контейнер для журналирования или другой тесно связанной задачи.
</b></details>

<details>
<summary>Когда нужны несколько контейнеров в одном поде?</summary><br><b>

Например, приложение и отдельные вспомогательные компоненты сбора журналов или мониторинга.<br>
В CI/CD, например Tekton, шаги одной задачи могут выполняться разными контейнерами одного пода.
</b></details>

<details>
<summary>Какие фазы Pod существуют?</summary><br><b>

  * Running — под назначен узлу, контейнеры созданы; хотя бы один работает, запускается или перезапускается.
  * Failed — все контейнеры завершены и хотя бы один завершился неуспешно. `Error` не является отдельной фазой Pod.
  * Succeeded — все контейнеры успешно завершились и не будут перезапускаться.
  * Unknown — состояние пода определить не удалось.
  * Pending — под принят, но подготовка ещё не завершена: например, ожидается назначение узла или скачивание образа.
</b></details>

<details>
<summary>Верно ли, что поды по умолчанию изолированы от любого входящего трафика?</summary><br><b>

Неверно. В модели NetworkPolicy под по умолчанию не изолирован, пока подходящая политика не задаёт изоляцию.
</b></details>

<details>
<summary>Верно ли, что Pending означает, что кластер ещё не принял под?</summary><br><b>

Неверно. Под уже принят, но запуск ещё не завершён, например из-за скачивания образа или ожидания планирования.
</b></details>

<details>
<summary>Верно ли, что контейнеры одного пода могут работать на разных узлах?</summary><br><b>

Неверно. Один под размещается на одном узле.
</b></details>

<details>
<summary>Под показывает ContainerCreating. Как вы это объясните?</summary><br><b>

Это отображаемое kubectl состояние подготовки контейнера, а не отдельная фаза Pod API. Проверьте `kubectl describe pod <имя>` и events: загрузку образа, CNI, подключение томов, Secret/ConfigMap и runtime узла. Только по этой строке причину установить нельзя.
</b></details>

<details>
<summary>Верно ли, что том пода может быть подключён ко всем его контейнерам?</summary><br><b>

Верно.
</b></details>

<details>
<summary>Что происходит при создании пода через kubectl?</summary><br><b>

1. Kubectl отправляет запрос создания в kube-apiserver.
   1. Выполняются аутентификация, авторизация и проверки запроса.
   2. API-сервер сохраняет объект в etcd.
2. Scheduler через API замечает неназначенный под.
3. Scheduler выбирает узел.
   1. Результат назначения должен быть сохранён через API-сервер, а не прямой записью Scheduler в etcd.
4. Scheduler сообщает назначение API-серверу.
5. Kubelet выбранного узла замечает назначенный ему под.
6. Kubelet через CRI поручает среде выполнения подготовить и запустить контейнеры.
7. Kubelet сообщает состояние пода API-серверу.
   1. API-сервер сохраняет обновлённое состояние в etcd.
</b></details>

<details>
<summary>Как проверить запуск после <code>kubectl run web --image nginxinc/nginx-unprivileged</code>?</summary><br><b>

* Посмотрите состояние пода и его контейнеров: `kubectl describe pods <POD_NAME>`.
`Status:       Running`
* Выполните команду внутри контейнера: `kubectl exec web -- ls`.
</b></details>

<details>
<summary>После kubectl run database --image mongo появился CrashLoopBackOff. Как выяснить причину?</summary><br><b>

Контейнер многократно завершается и перезапускается, а Kubernetes увеличивает задержку между попытками.<br>
Возможны ошибки приложения, прав, конфигурации или зависимостей; причины нужно проверять по фактам.

Посмотрите события, состояние и код завершения через `kubectl describe po <POD_NAME>`.

```
 Last State:     Terminated
   Reason:       Error
   Exit Code:    100
```

Прочитайте `kubectl logs <POD_NAME>` и при необходимости журналы предыдущего запуска с `--previous`.
</b></details>

<details>
<summary>Объясните назначение следующих строк:

```
livenessProbe:
  exec:
    command:
    - cat
    - /appStatus
  initialDelaySeconds: 10
  periodSeconds: 5
```
</summary><br><b>

Это liveness probe — проверка, при повторных неудачах которой контейнер перезапускается согласно правилам.<br>
Здесь выполняется `cat /appStatus`. Проверки начинаются через 10 секунд и повторяются каждые 5 секунд. После достижения порога неудач контейнер останавливается, и применяется политика перезапуска.
</b></details>

<details>
<summary>Объясните назначение следующих строк:

```
readinessProbe:
      tcpSocket:
        port: 2017
      initialDelaySeconds: 15
      periodSeconds: 20
```
</summary><br><b>

Это readiness probe: готовность зависит от соединения с портом 2017. Первая проверка через 15 секунд, последующие каждые 20 секунд. Уточнение: проверки продолжаются и после первого успеха, чтобы отслеживать потерю готовности.
</b></details>

<details>
<summary>Что означает ErrImagePull?</summary><br><b>

Не удалось скачать образ, например из-за неверного имени, недоступности реестра или отсутствия доступа.<br>
Подробности: `kubectl describe po <POD_NAME>`.
</b></details>

<details>
<summary>Что происходит при удалении пода?</summary><br><b>

1. При обычном завершении контейнерам отправляется сигнал остановки, обычно TERM; при наличии учитываются lifecycle hooks.
2. Даётся grace period, по умолчанию 30 секунд для завершения пода.
3. По истечении срока оставшиеся процессы завершаются принудительно сигналом KILL.
</b></details>

<details>
<summary>Объясните liveness probes.</summary><br><b>

Они выявляют неработоспособный контейнер и позволяют перезапустить его после установленного порога ошибок.<br>
Например, периодическая команда `cat /app/status` может служить проверкой; её неуспешный результат учитывается согласно настройкам probe.

Подробнее — в [документации Kubernetes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes).
</b></details>

<details>
<summary>Объясните readiness probes.</summary><br><b>

Они показывают kubelet, готов ли контейнер обслуживать трафик.<br>
Например, проверка соединения с портом 8080. Готовность пода зависит от готовности контейнеров и других заданных условий.

Подробнее — в [документации Kubernetes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes).
</b></details>

<details>
<summary>Как readiness влияет на Service?</summary><br><b>

Обычно трафик Service направляется только к готовым конечным точкам. Уточнение: существуют специальные настройки, например `publishNotReadyAddresses`, меняющие это поведение.
</b></details>

<details>
<summary>Почему часто используют один основной контейнер на под?</summary><br><b>

Контейнеры одного пода масштабируются вместе. Если компонентам нужно независимое масштабирование, их удобнее разделить.
</b></details>

<details>
<summary>Верно ли, что назначение узла сохраняется даже для нового пода, созданного вместо отказавшего?</summary><br><b>

Верно.
</b></details>

<details>
<summary>Верно ли, что каждый новый под получает публичный IP?</summary><br><b>

Неверно. Адрес пода относится к сети кластера; его внешняя маршрутизируемость зависит от сетевой архитектуры и не гарантируется.

Для стабильного внешнего доступа обычно используют Service подходящего типа и при необходимости Ingress или иной шлюз.
</b></details>

<a id="static-pods"></a>
#### Статические поды

<details>
<summary>Что такое статические поды?</summary><br><b>

[Kubernetes.io](https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/): поды, которыми kubelet управляет непосредственно на конкретном узле, без управляющего контроллера API. Kubelet следит за ними и перезапускает при отказах; в API может создаваться зеркальное представление.
</b></details>

<details>
<summary>Верно ли, что аналогично статическим подам существуют статические Deployment и ReplicaSet?</summary><br><b>

Неверно.
</b></details>

<details>
<summary>Для чего используют статические поды?</summary><br><b>

Например, для компонентов control plane: kube-apiserver, scheduler и других, которые должны запускаться на определённых узлах независимо от готовности API кластера.
</b></details>

<details>
<summary>Как распознать статический под?</summary><br><b>

У зеркального пода обычно есть суффикс с именем узла. Надёжнее также проверить аннотацию `kubernetes.io/config.mirror` и конфигурацию kubelet.
Примечание исходника: один суффикс имени требует дополнительной проверки.
</b></details>

<details>
<summary>Какой компонент из перечисленных обычно не запускается статическим подом?

* kube-scheduler
* kube-proxy
* kube-apiserver
</summary><br><b>

kube-proxy обычно запускается DaemonSet на подходящих узлах. Это типичная схема, а не безусловное требование для любого способа установки.
</b></details>

<details>
<summary>Где находятся манифесты статических подов?</summary><br><b>

Часто в `/etc/kubernetes/manifests`. Проверьте `staticPodPath` в конфигурации kubelet; в исходнике название параметра местами написано с ошибкой.

Путь конфигурации можно выяснить через `ps -ef | grep kubelet`, проверив аргумент `--config`.

Например: `grep staticPodPath /var/lib/kubelet/config.yaml`.
</b></details>

<details>
<summary>Как удалить статический под?
</summary><br><b>

Определите каталог `staticPodPath` в настройках kubelet.

Удалите соответствующий манифест: `rm <STATIC_POD_PATH>/<POD_DEFINITION_FILE>`.
</b></details>

<a id="pods-commands"></a>
#### Команды для подов

<details>
<summary>Как узнать, на каких узлах работают поды?</summary><br><b>

`kubectl get pods -o wide`
</b></details>

<details>
<summary>Как удалить под?</summary><br><b>

`kubectl delete pod pod_name`
</b></details>

<details>
<summary>Выведите поды с меткой env=prod.</summary><br><b>

`k get po -l env=prod`

Подсчёт: `k get po -l env=prod --no-headers | wc -l`.
</b></details>

<details>
<summary>Как вывести поды текущего пространства имён?</summary><br><b>

`kubectl get po`
</b></details>

<details>
<summary>Как вывести поды всех пространств имён?</summary><br><b>

`kubectl get pods --all-namespaces`
</b></details>

<a id="pods-troubleshooting-and-debugging"></a>
#### Диагностика подов

<details>
<summary>Под остаётся Pending. Какова возможная причина?</summary><br><b>

Например, не работает Scheduler. При доступном в API компоненте его можно искать через `kubectl get po -A | grep scheduler` или в `kube-system`. Также проверьте события пода: возможны нехватка ресурсов и ограничения размещения.
</b></details>

<details>
<summary>Что делает kubectl logs [pod-name]?</summary><br><b>

Выводит журналы контейнера пода.
</b></details>

<details>
<summary>Что делает kubectl describe pod [pod name]?</summary><br><b>

Показывает подробные сведения об объекте и связанные события.
</b></details>

<details>
<summary>Создайте статический под с образом python и командой sleep 2017.</summary><br><b>

Перейдите в каталог статических манифестов, например `cd /etc/kubernetes/manifests`; проверьте путь в конфигурации kubelet.

Создайте там манифест:
`k run some-pod --image=python --restart=Never --dry-run=client -o yaml --command -- sleep 2017 > static-pod.yaml`
</b></details>

<a id="labels-and-selectors-1"></a>
### Метки и селекторы

<details>
<summary>Объясните метки (labels).</summary><br><b>

[Kubernetes.io](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/): пары ключ–значение, прикрепляемые к объектам, например подам. Они задают значимые пользователю идентифицирующие признаки, позволяют группировать и выбирать объекты. Метки можно добавлять и менять; каждый ключ уникален в пределах объекта.
</b></details>

<details>
<summary>Объясните селекторы.</summary><br><b>

Equality-based условия `key=value`, `key!=value` и set-based `in`, `notin`, наличие/отсутствие ключа там, где API их поддерживает. Несколько условий обычно соединяются AND; синтаксис и поддержка зависят от поля, Service selector — карта равенств, а не произвольное выражение.
</b></details>

<details>
<summary>Приведите примеры использования меток.</summary><br><b>

* Планировщик использует метки узлов и правила размещения, чтобы выбирать подходящие узлы подам.
* ReplicaSet выбирает управляемые поды по меткам.
</b></details>

<details>
<summary>Что такое аннотации?</summary><br><b>

[Kubernetes.io](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/): произвольные неидентифицирующие метаданные объекта, доступные инструментам и библиотекам.
</b></details>

<details>
<summary>Чем аннотации отличаются от меток?</summary><br><b>

[Kubernetes.io](Labels can be used to select objects and to find collections of objects that satisfy certain conditions. In contrast, annotations are not used to identify and select objects. The metadata in an annotation can be small or large, structured or unstructured, and can include characters not permitted by labels.): «Метки позволяют выбирать объекты и находить их группы по заданным условиям. Аннотации не предназначены для идентификации и выбора объектов. Данные аннотаций могут быть небольшими или объёмными, структурированными или неструктурированными и содержать символы, недопустимые в метках». Примечание: адрес ссылки в исходнике повреждён.
</b></details>

<details>
<summary>Как посмотреть журналы контейнера в поде?</summary><br><b>

`k logs POD_NAME`
</b></details>

<details>
<summary>В some-pod два контейнера. Что произойдёт при kubectl logs some-pod?</summary><br><b>

Если контейнер не выбран автоматически, нужно указать его: `kubectl logs POD_NAME -c CONTAINER_NAME`. Уточнение: выбор по умолчанию зависит от версии kubectl и аннотаций пода, поэтому безусловное «не сработает» из исходника неверно.
</b></details>

<a id="deployments"></a>
### Deployments

<details>
<summary>Что такое Deployment?</summary><br><b>

Объект декларативного управления экземплярами подов контейнерного приложения.
Позволяет менять число реплик, постепенно обновлять приложение и откатывать шаблон подов к предыдущей ревизии.

Описывает желаемое состояние подов и ReplicaSet.
</b></details>

<details>
<summary>Как создать Deployment с nginx:alpine?</summary><br><b>

`kubectl create deployment my-first-deployment --image=nginx:alpine`

ИЛИ

```
cat << EOF | kubectl create -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:alpine
```
</b></details>

<details>
<summary>Как проверить создание Deployment?</summary><br><b>

`kubectl get deployments` или `kubectl get deploy`.

Команда показывает объекты в выбранном пространстве имён. Само наличие объекта не означает готовность: проверьте READY и AVAILABLE.
</b></details>

<details>
<summary>Как отредактировать Deployment?</summary><br><b>

`kubectl edit deployment <DEPLOYMENT_NAME>`
</b></details>

<details>
<summary>Что произойдёт после изменения образа в Deployment?</summary><br><b>

Начнётся обновление по заданной стратегии: новые поды заменят старые.

Создаётся новый ReplicaSet; после успешного завершения обновления старый обычно масштабируется до нуля.
</b></details>

<details>
<summary>Как удалить Deployment?</summary><br><b>

По имени: `kubectl delete deployment [deployment_name]`.

По манифесту: `kubectl delete -f deployment.yaml`.
</b></details>

<details>
<summary>Что происходит при удалении Deployment?</summary><br><b>

При обычном каскадном удалении удаляются принадлежащие ему ReplicaSet и поды.
</b></details>

<details>
<summary>Что происходит при создании Deployment?</summary><br><b>

При `kubectl create deployment some-deployment --image=nginx`:

1. API-сервер получает запрос создания Deployment.
2. Контроллер создаёт ReplicaSet, который создаёт поды; Scheduler назначает их узлам.
3. Kubelet узла поручает среде выполнения получить образ.
4. Из образа создаются и запускаются контейнеры.
</b></details>

<details>
<summary>Как сделать приложение доступным внутри сети или извне?</summary><br><b>

Через Service подходящего типа.
</b></details>

<details>
<summary>Можно ли использовать Deployment для приложения с состоянием?</summary><br><b>

Можно, если приложение корректно работает с внешним состоянием и идентичность конкретной реплики несущественна. Для устойчивых имён, порядка и привязанных томов часто нужен StatefulSet. Ни Deployment, ни StatefulSet сами не обеспечивают резервное копирование или согласованность БД.
</b></details>

<details>
<summary>Исправьте манифест Deployment:

```yaml
apiVersion: apps/v1
kind: Deploy
metadata:
  creationTimestamp: null
  labels:
    app: dep
  name: dep
spec:
  replicas: 3
  selector:
    matchLabels:
      app: dep
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: dep
    spec:
      containers:
      - image: redis
        name: redis
        resources: {}
status: {}
```
</summary><br><b>

Замените `kind: Deploy` на `kind: Deployment`.
</b></details>

<details>
<summary>Исправьте манифест Deployment:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  creationTimestamp: null
  labels:
    app: dep
  name: dep
spec:
  replicas: 3
  selector:
    matchLabels:
      app: depdep
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: dep
    spec:
      containers:
      - image: redis
        name: redis
        resources: {}
status: {}
```
</summary><br><b>

Селектор не совпадает с меткой: `dep` и `depdep`. Приведите их к одному значению, например `dep`.
</b></details>

<a id="deployments-commands"></a>
#### Команды для Deployment

<details>
<summary>Создайте манифест Deployment dep: образ redis, три реплики.</summary><br><b>

`k create deploy dep -o yaml --image=redis --dry-run=client --replicas 3 > deployment.yaml `

</b></details>

<details>
<summary>Удалите Deployment depdep.</summary><br><b>

`k delete deploy depdep`

</b></details>

<details>
<summary>Создайте Deployment pluck с образом redis и пятью репликами.</summary><br><b>

`kubectl create deployment pluck --image=redis`

`kubectl scale deployment pluck --replicas=5`
</b></details>

<details>
<summary>Создайте Deployment со следующими свойствами:

* Имя blufer
* Образ python
* Три реплики
* Поды размещаются на узле с меткой blufer
</summary><br><b>

`kubectl create deployment blufer --image=python --replicas=3 -o yaml --dry-run=client > deployment.yaml`

Добавьте в `deployment.yaml` следующий раздел:

```
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedlingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: blufer
            operator: Exists
```

`kubectl apply -f deployment.yaml`
</b></details>

<a id="services"></a>
### Services

<details>
<summary>Что такое Service Kubernetes?</summary><br><b>

Абстракция, предоставляющая приложение на наборе подов как сетевой сервис. Подробнее — [здесь](https://kubernetes.io/docs/concepts/services-networking/service).

Она обеспечивает стабильный сетевой доступ к приложению внутри кластера или снаружи в зависимости от типа.
</b></details>

<details>
<summary>Разместите компоненты Service в соответствующих местах схемы.<br>
<img src="images/service_exercise.png"/>
</summary><br><b>

`port` — порт Service для клиентов; `targetPort` — порт backend контейнера; `nodePort` — порт узлов для Service типа NodePort при разрешающей сети. На схеме ниже показана логическая связь, а не отдельный обязательный процесс Service на каждом узле. <img src="images/service_solution.png"/>
</b></details>


<details>
<summary>Как предоставить Deployment alle через LoadBalancer на порту 8080?</summary><br><b>

Императивный способ:

`kubectl expose deployment alle --type=LoadBalancer --port 8080`
</b></details>

<details>
<summary>Верно ли, что Service сохраняется после удаления отдельного пода, поскольку их жизненные циклы независимы?</summary><br><b>

Верно.
</b></details>

<details>
<summary>Как проверить создание Service?</summary><br><b>

`kubectl get svc`
</b></details>

<details>
<summary>Какой тип Service используется по умолчанию?</summary><br><b>

ClusterIP — обычно для доступа внутри кластера.
</b></details>

<details>
<summary>Какие типы Service существуют?</summary><br><b>

* ClusterIP
* NodePort
* LoadBalancer
* ExternalName

Подробнее — [здесь](https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types).
</b></details>

<details>
<summary>Как связаны Service и Deployment?</summary><br><b>

Прямой связи владения нет: Service выбирает поды по меткам, а не обращается к Deployment.
</b></details>

<details>
<summary>Что проверить при создании Service?</summary><br><b>

1. `targetPort` должен соответствовать порту, который действительно слушает приложение; его можно описать в `containerPort`.
2. Под должен соответствовать всем требованиям селектора Service, а не только одной метке.

</b></details>

<details>
<summary>Какой тип Service используется по умолчанию и зачем?</summary><br><b>

ClusterIP предоставляет адрес для доступа внутри кластера. Сам по себе он не является политикой безопасности, запрещающей любые внешние маршруты.

</b></details>

<details>
<summary>Как получить сведения о Service?</summary><br><b>

`kubectl describe service <SERVICE_NAME>`

Сокращённо: `kubectl describe svc ...`.

</b></details>

<details>
<summary>Что делает следующая команда?

```
kubectl expose rs some-replicaset --name=replicaset-svc --target-port=2017 --type=NodePort
```
</summary><br><b>

Создаёт Service `replicaset-svc` для ReplicaSet. Порт приложения — 2017, тип Service — NodePort, предоставляющий доступ через порты узлов при подходящей сетевой доступности.
</b></details>

<details>
<summary>Верно ли, что следующая команда публикует порт только на одном узле, но направляет трафик ко всем подам?

```
kubectl expose rs some-replicaset --name=replicaset-svc --target-port=2017 --type=NodePort
```
</summary><br><b>

Неверно. NodePort обычно доступен на узлах кластера и направляет отдельное соединение к подходящей конечной точке; детали зависят от сетевых настроек и политики трафика.
</b></details>

<details>
<summary>Как проверить, что Service направляет запросы к нужному поду?</summary><br><b>

Сравните адреса конечных точек Service из `kubectl describe service` или EndpointSlice с IP подов из `kubectl get pod -o wide`.
</b></details>

<details>
<summary>Что произойдёт при применении следующего манифеста?

```
apiVersion: v1
kind: Service
metadata:
  name: some-app
spec:
  type: NodePort
  ports:
  - port: 8080
    nodePort: 2017
    protocol: TCP
  selector:
    type: backend
    service: some-app
```
</summary><br><b>

Создаётся Service типа NodePort для доступа к приложению.<br>
`targetPort` приложения — 8080, порт Service — 2017. Если `nodePort` указан явно, он должен входить в разрешённый диапазон; обычно его можно предоставить системе.<br>
Используется TCP, который является протоколом по умолчанию.<br>
Селектор выбирает поды одновременно с метками `type: backend` и `service: some-app`.<br>
</b></details>

<details>
<summary>Как предоставить следующий Service извне?

```
spec:
  selector:
    app: some-app
  ports:
    - protocol: TCP
      port: 8081
      targetPort: 8081
```
</summary><br><b>

Например, добавить `type: LoadBalancer` при наличии реализации балансировщика. Уточнение: явно задавать `nodePort` для этого не обязательно.

```
spec:
  selector:
    app: some-app
  type: LoadBalancer
  ports:
    - protocol: TCP
      port: 8081
      targetPort: 8081
      nodePort: 32412
```
</b></details>

<details>
<summary>Чем направлять внешний HTTP(S)-трафик к сервисам кластера?</summary><br><b>

Ingress
</b></details>

<details>
<summary>Верно ли, что NodePort обычно также получает ClusterIP?</summary><br><b>

Верно.
</b></details>

<details>
<summary>Когда используется тип LoadBalancer?</summary><br><b>

Когда нужен балансировщик, создаваемый поддерживаемой интеграцией, например облачным провайдером.
</b></details>

<details>
<summary>Как сопоставить Service внешнему DNS-имени?</summary><br><b>

Использовать тип `ExternalName`.
</b></details>

<details>
<summary>Опишите создание Service.</summary><br><b>

1. Kubectl отправляет API-серверу запрос создания.
2. Контроллер замечает новый Service.
3. Для Service с селектором формируются сведения о конечных точках; в исходнике используется Endpoints, в современных кластерах — EndpointSlice.
4. По селектору определяются подходящие поды.
5. Kube-proxy или альтернативная реализация обновляет правила направления трафика, например iptables.
6. Кластерный DNS предоставляет запись Service.
</b></details>

<details>
<summary>Как вывести конечные точки приложения?</summary><br><b>

`kubectl get ep <name>`
</b></details>

<details>
<summary>Как узнать данные Service, если доступен только kubectl exec POD_NAME -- ...?</summary><br><b>

Можно проверить `kubectl exec <POD_NAME> -- env`: при включённых service links и наличии Service на момент создания пода там могут быть соответствующие переменные.<br>
Например, `[SERVICE_NAME]_SERVICE_HOST`, `[SERVICE_NAME]_SERVICE_PORT`.
</b></details>

<details>
<summary>Как контейнер впервые подключается к Service по имени? Кто создаёт нужные настройки?</summary><br><b>

  - Программа использует DNS-сервер из `/etc/resolv.conf`.
  - DNS разрешает имя в адрес Service.
  - Сетевые правила, например iptables, направляют трафик на конечную точку.

Кто настраивает компоненты:

  - Kubelet подготавливает DNS-настройки пода при запуске.
  - Кластерный DNS, например CoreDNS, обслуживает запись Service по данным API.
  - Kube-proxy или другой сетевой компонент программирует правила Service.
</b></details>

<details>
<summary>Что происходит при <code>kubectl expose deployment remo --type=LoadBalancer --port 8080</code>?</summary><br><b>

1. Kubectl запрашивает создание Service.
2. При настроенной интеграции соответствующий контроллер создаёт балансировщик у провайдера.
3. Он направляет трафик к приложению через узлы или непосредственно конечные точки — в зависимости от реализации.
</b></details>

<details>
<summary>Как проверить внешний доступ через созданный Service?</summary><br><b>

Например, выполнить `curl <SERVICE IP>:<SERVICE PORT>` с нужной стороны сети.
</b></details>

<details>
<summary>Как в исходнике названы внутренний и внешний механизмы балансировки Kubernetes?</summary><br><b>

Исходник отвечает «Service и Ingress». Уточнение: это упрощение. Service типа LoadBalancer тоже может быть внешним, а Ingress может быть внутренним; Ingress задаёт правила HTTP(S), реализуемые контроллером.
</b></details>

<a id="ingress"></a>
### Ingress

<details>
<summary>Что такое Ingress?</summary><br><b>

По документации Kubernetes, объект правил внешней HTTP(S)-маршрутизации к Service внутри кластера.

Подробнее — [здесь](https://kubernetes.io/docs/concepts/services-networking/ingress/).
</b></details>

<details>
<summary>Дополните конфигурацию, чтобы получить Ingress:

```
metadata:
  name: someapp-ingress
spec:
```
</summary><br><b>
Возможны разные корректные решения.

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: someapp-ingress
spec:
  rules:
  - host: my.host
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: someapp-internal-service
            port:
              number: 8080
```
</b></details>


<details>
<summary>Объясните поля http, host и backend:

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: someapp-ingress
spec:
  rules:
  - host: my.host
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: someapp-internal-service
            port:
              number: 8080
```
</summary><br><b>

`host` — DNS-имя, с которым сопоставляется входящий HTTP-запрос; DNS обычно направляет это имя на адрес контроллера.<br>
`http` содержит правила маршрутизации по путям HTTP-запросов.<br>
`backend.service.name` задаёт Service, `backend.service.port.number` — его порт. В networking.k8s.io/v1 требуется `pathType`; здесь `Prefix` сопоставляет префикс пути. Для обработки нужен установленный Ingress Controller и подходящий IngressClass.
</b></details>

<details>
<summary>Какие проблемы могут возникнуть с wildcard в host Ingress?</summary><br><b>

Уточнение: `host: *` не является допустимым универсальным wildcard-хостом. Допустимы ограниченные шаблоны вида `*.example.com`. Правило без host может принимать запросы к разным именам, поэтому маршруты нужно задавать осознанно; оно само по себе не «роняет весь кластер», как утверждает исходник.
</b></details>

<details>
<summary>Что такое Ingress Controller?</summary><br><b>

Компонент, который наблюдает Ingress и реализует описанные правила в прокси или балансировщике.

Есть разные реализации контроллеров; их установка и поддержка выбираются отдельно от самого API Ingress.
</b></details>

<details>
<summary>Когда используют Ingress?</summary><br><b>

* Несколько поддоменов с разными Service.
* Один домен с разными путями, ведущими к разным приложениям.
</b></details>

<details>
<summary>Как вывести Ingress текущего пространства имён?</summary><br><b>

kubectl get ingress
</b></details>

<details>
<summary>Что такое default backend Ingress?</summary><br><b>

Назначение для запросов, которым не соответствует ни одно правило. Его поведение позволяет задать понятный ответ вместо неожиданной ошибки; настройки зависят от Ingress и контроллера.
</b></details>

<details>
<summary>Как настроить default backend?</summary><br><b>

Создать нужный Service и сослаться на него в `spec.defaultBackend` либо настроить backend по умолчанию самого контроллера. Одного создания Service недостаточно.
</b></details>

<details>
<summary>Как настроить TLS для Ingress?</summary><br><b>

Добавить раздел `tls`, нужные имена хостов и `secretName` сертификата.

```
spec:
  tls:
  - hosts:
    - some_app.com
    secretName: someapp-secret-tls
```
</b></details>

<details>
<summary>Верно ли, что TLS Secret должен находиться в том же namespace, что и Ingress?</summary><br><b>

Верно.
</b></details>

<details>
<summary>Как ограничить сетевой обмен подов на уровне IP и портов?</summary><br><b>

С помощью NetworkPolicy.
</b></details>

<details>
<summary>Как масштабировать Deployment до нескольких экземпляров приложения?</summary><br><b>

Например, до двух:

`kubectl scale deployment <DEPLOYMENT_NAME> --replicas=2`

Можно задать другое число, если приложение поддерживает такое масштабирование.
</b></details>

<a id="replicasets"></a>
### ReplicaSets

<details>
<summary>Для чего нужен ReplicaSet?</summary><br><b>

[kubernetes.io](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset): ReplicaSet поддерживает заданное число реплик подов, обеспечивая наличие нужного количества экземпляров.

Если управляемых подов слишком много, лишние удаляются; если мало — создаются новые.
</b></details>

<details>
<summary>Что делает следующий блок?

```
spec:
  replicas: 2
  selector:
    matchLabels:
      type: backend
  template:
    metadata:
      labels:
        type: backend
    spec:
      containers:
      - name: httpd-yup
        image: httpd
```
</summary><br><b>

Задаёт ReplicaSet для подов с меткой `type: backend` и желаемым числом реплик 2.
</b></details>

<details>
<summary>Что произойдёт, если вручную удалить под ReplicaSet через kubectl delete po?</summary><br><b>

ReplicaSet создаст замену для восстановления желаемого числа реплик.
</b></details>

<details>
<summary>Верно ли, что ReplicaSet с replicas=2 ничего не сделает при наличии трёх управляемых подов?</summary><br><b>

Неверно. Он удалит лишний под, чтобы осталось два.
</b></details>

<details>
<summary>Опишите последовательность создания ReplicaSet.</summary><br><b>

* Клиент отправляет запрос API-серверу.
* Контроллер замечает новый ReplicaSet.
* Создаёт необходимое число объектов Pod по шаблону.
* Scheduler назначает поды узлам через API-сервер.
* Kubelet замечает назначенные своему узлу поды.
* Поручает среде выполнения создать контейнеры.
* Отправляет состояние подов API-серверу.
</b></details>

<details>
<summary>Как вывести ReplicaSet текущего namespace?</summary><br><b>

`kubectl get rs`
</b></details>

<details>
<summary>Можно ли удалить ReplicaSet, сохранив его поды?</summary><br><b>

Да, через orphan-удаление. В исходнике указан старый вариант `--cascade=false`.

`kubectl delete -f rs.yaml --cascade=orphan`
</b></details>

<details>
<summary>Сколько реплик создаётся, если replicas не задано?</summary><br><b>

1
</b></details>

<details>
<summary>Что означает следующий вывод kubectl get rs?

NAME                    DESIRED   CURRENT   READY   AGE
web                     2         2         0       2m23s
</summary><br><b>

У `web` желаемых и существующих реплик две, но готовых — ноль. Это может быть временным состоянием запуска или ошибкой. Изучите `kubectl describe po POD_NAME` и `kubectl logs POD_NAME`; отсутствие готовности не обязательно означает отсутствие работающего процесса.
</b></details>

<details>
<summary>Верно ли, что ReplicaSet управляет только подами, которые создал сам?</summary><br><b>

Неверно. Он может принять подходящие поды без другого управляющего владельца. Уточнение: нельзя произвольно забрать под, уже управляемый другим контроллером.
</b></details>

<details>
<summary>Верно ли, что ReplicaSet ждёт самостоятельного появления подходящих подов?</summary><br><b>

Неверно. Он создаёт недостающие поды.
</b></details>

<details>
<summary>Какое поле spec нужно ReplicaSet для создания подов?</summary><br><b>

`template` задаёт шаблон новых подов. Уточнение: обязательны и другие поля, в частности подходящий `selector`.
</b></details>

<details>
<summary>Как узнать, создал ли ReplicaSet новые поды или нашёл существующие?</summary><br><b>

`kubectl describe rs <ReplicaSet Name>`

Посмотрите `Events` в конце вывода.
</b></details>

<details>
<summary>Верно ли, что удаление ReplicaSet удаляет его поды?</summary><br><b>

При обычном каскадном удалении — да; режим orphan позволяет сохранить зависимые объекты.
</b></details>

<details>
<summary>Верно ли, что удаление выбранной селектором метки пода заставит ReplicaSet создать замену?</summary><br><b>

Да. Под перестаёт соответствовать селектору, и контроллер восполняет недостающую реплику.
</b></details>

<details>
<summary>Как масштабировать Deployment до восьми реплик?</summary><br><b>

kubectl scale deploy <DEPLOYMENT_NAME> --replicas=8
</b></details>

<details>
<summary>Верно ли, что все реплики готовы сразу после команды создания ReplicaSet?</summary><br><b>

Неверно. Запуск занимает время. Проверяйте READY в `kubectl get rs`.
</b></details>

<details>
<summary>Как предоставить ReplicaSet через новый Service?</summary><br><b>

`kubectl expose rs <ReplicaSet Name> --name=<Service Name> --target-port=<Port to expose> --type=NodePort`

Примечания:
  - `target-port` соответствует порту приложения в контейнере.
  - Тип Service выбирается по задаче и не обязан быть NodePort.
</b></details>

<details>
<summary>Исправьте определение ReplicaSet:

```yaml
apiVersion: apps/v1
kind: ReplicaCet
metadata:
  name: redis
  labels:
    app: redis
    tier: cache
spec:
  selector:
    matchLabels:
      tier: cache
  template:
    metadata:
      labels:
        tier: cachy
    spec:
      containers:
      - name: redis
        image: redis
```
</summary><br><b>

Правильное значение kind — `ReplicaSet`, а не `ReplicaCet`.
</b></details>

<details>
<summary>Исправьте определение ReplicaSet:

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: redis
  labels:
    app: redis
    tier: cache
spec:
  selector:
    matchLabels:
      tier: cache
  template:
    metadata:
      labels:
        tier: cachy
    spec:
      containers:
      - name: redis
        image: redis
```
</summary><br><b>

Селектор и метка не совпадают: замените `cachy` на `cache`.
</b></details>

<details>
<summary>Как узнать образ контейнера в ReplicaSet repli?</summary><br><b>

`k describe rs repli | grep -i image`
</b></details>

<details>
<summary>Как проверить готовность подов ReplicaSet repli?</summary><br><b>

`k describe rs repli | grep -i "Pods Status"`
</b></details>

<details>
<summary>Как удалить ReplicaSet rori?</summary><br><b>

`k delete rs rori`
</b></details>

<details>
<summary>Как изменить образ в ReplicaSet rori?</summary><br><b>

`k edit rs rori`. Уточнение: правка шаблона ReplicaSet сама по себе не обновляет уже работающие поды; для управляемого обновления обычно используют Deployment.
</b></details>

<details>
<summary>Увеличьте число реплик rori с двух до пяти.</summary><br><b>

`k scale rs rori --replicas=5`
</b></details>

<details>
<summary>Уменьшите число реплик rori с пяти до одной.</summary><br><b>

`k scale rs rori --replicas=1`
</b></details>

<a id="daemonset"></a>
### DaemonSet

<details>
<summary>Что такое DaemonSet?</summary><br><b>

[Kubernetes.io](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset): обеспечивает экземпляр пода на всех подходящих узлах или их части. При добавлении узлов создаёт поды, при удалении очищает их. Обычное удаление DaemonSet удаляет его поды.
</b></details>

<details>
<summary>Чем ReplicaSet отличается от DaemonSet?</summary><br><b>

ReplicaSet поддерживает заданное число реплик.
DaemonSet поддерживает под на каждом подходящем узле.
</b></details>

<details>
<summary>Для чего используют DaemonSet?</summary><br><b>

* Мониторинг: агент, например Datadog, на каждом узле.
* Сбор журналов с каждого узла.
* Сетевые компоненты, необходимые узлам кластера.
</b></details>

<details>
<summary>Как DaemonSet размещает поды?</summary><br><b>

Исторически использовалось прямое назначение через `nodeName`.

Начиная с перехода, описанного в исходнике для версии 1.12, размещение выполняется обычным Scheduler с node affinity.
</b></details>

<a id="daemonset---commands"></a>
#### Команды для DaemonSet

<details>
<summary>Как вывести DaemonSet текущего namespace?</summary><br><b>

`kubectl get ds`
</b></details>

<a id="statefulset"></a>
### StatefulSet

<details>
<summary>Объясните StatefulSet.</summary><br><b>

Объект управления приложениями с состоянием: развёртывание и масштабирование подов со стабильной идентичностью и правилами порядка операций. [Подробнее](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/).
</b></details>

<a id="storage"></a>
### Хранение данных

<a id="volumes"></a>
#### Тома

<details>
<summary>Что такое том Kubernetes?</summary><br><b>

Хранилище, подключаемое к контейнерам пода. Способ подготовки и жизненный цикл зависят от типа тома.

</b></details>

<details>
<summary>Какие типы томов вы знаете?</summary><br><b>

* `emptyDir` — создаётся для пода на узле и удаляется вместе с этим подом; переживает перезапуск его контейнеров.
* `hostPath` — подключает путь хоста. Требует осторожности из-за доступа к системе, но нужен, например, агентам, читающим `/sys` или `/var/lib`.

</b></details>

<details>
<summary>Какие задачи решают тома?</summary><br><b>

1. Общие файлы для нескольких контейнеров пода.
2. Отделение данных от записываемого слоя контейнера. Для данных, которые должны переживать замену пода, используют постоянные хранилища.

</b></details>

<details>
<summary>Чем эфемерные тома отличаются от постоянных?</summary><br><b>

Жизненный цикл эфемерных томов связан с подом; постоянные тома могут существовать после его удаления.

</b></details>

<details>
<summary>Приведите сценарий для каждого типа:

* emptyDir
* hostPath
</summary><br><b>

* `emptyDir`: временные данные, которые можно потерять при удалении пода, например промежуточные файлы разовой задачи.
* `hostPath`: доступ к данным самого узла, например `/sys` или `/var/lib`.
</b></details>

<a id="networking"></a>
### Сеть

<details>
<summary>Верно ли, что поды разных namespace по умолчанию не могут общаться?</summary><br><b>

Неверно. Само разделение по namespace сетевую связь не запрещает.

Проверьте на примере:

kubectl run test-prod -n prod --image ubuntu -- sleep 2000000000
kubectl run test-dev -n dev --image ubuntu -- sleep 2000000000

Получите IP test-prod: `k describe po test-prod -n prod`.

Откройте оболочку test-dev: `kubectl exec --stdin --tty test-dev -n dev -- /bin/bash`.

Отправьте ping на полученный IP, если утилита доступна и сеть разрешает ICMP. Разные namespace сами по себе трафик не блокируют.

</b></details>

<a id="network-policies"></a>
### Сетевые политики

<details>
<summary>Объясните NetworkPolicy.</summary><br><b>

[kubernetes.io](https://kubernetes.io/docs/concepts/services-networking/network-policies): механизм описания разрешённого взаимодействия подов с сетевыми сущностями.

Политики определяют допустимые входящие и исходящие соединения; для их применения нужен сетевой плагин с поддержкой NetworkPolicy.

</b></details>

<details>
<summary>Когда применяют NetworkPolicy?</summary><br><b>

  - Для ограничения доступа к определённым подам.
  - Для управления потоками между группами подов и другими конечными точками. Уточнение: это не универсальный межсетевой экран между самими узлами.

</b></details>

<details>
<summary>Верно ли, что без NetworkPolicy поду запрещены все соединения?</summary><br><b>

Неверно. По умолчанию под не изолирован политиками.
</b></details>

<details>
<summary>Исходящая политика источника не разрешает соединение, а входящая политика назначения разрешает. Пройдёт ли трафик?</summary><br><b>

Нет. Если соответствующие направления изолированы, разрешение нужно с обеих сторон.
</b></details>

<details>
<summary>Где хранится состояние кластера?</summary><br><b>

etcd
</b></details>

<a id="etcd"></a>
### etcd

<details>
<summary>Что такое etcd?</summary><br><b>

Открытое распределённое хранилище ключей и значений для критически важных данных распределённых систем.

[Подробнее](https://www.redhat.com/en/topics/containers/what-is-etcd).

</b></details>

<details>
<summary>Верно ли, что etcd хранит текущее состояние любого компонента Kubernetes?</summary><br><b>

Верно.
</b></details>

<details>
<summary>Верно ли, что среди основных компонентов Kubernetes напрямую с etcd взаимодействует API-сервер?</summary><br><b>

Верно.
</b></details>

<details>
<summary>Верно ли, что рабочие данные приложений обычно не хранятся в etcd Kubernetes?</summary><br><b>

Верно.
</b></details>

<details>
<summary>Почему выбрано etcd, а не другая SQL- или NoSQL-база?</summary><br><b>

Среди важных свойств:

* Высокая доступность при развёртывании нескольких участников.
* Репликация данных. Уточнение: в Raft есть лидер; утверждение исходника, что любой узел одновременно основной, неточно.
* Согласованность; семантика чтения зависит от выбранного режима.
* Защищённый обмен через TLS.
* Производительность, подходящая для состояния кластера; конкретное число записей в секунду зависит от среды.
</b></details>

<a id="namespaces"></a>
### Пространства имён

<details>
<summary>Что такое namespace?</summary><br><b>

Логическая область имён ресурсов внутри кластера. Позволяет группировать приложения и использовать одинаковые имена объектов одного типа в разных namespace. Это не полная изоляция виртуальных кластеров.
</b></details>

<details>
<a id="namespaces-use-cases"></a>
<summary>Зачем нужны namespace? Чем неудобен один default?</summary><br><b>

С ростом числа приложений труднее ориентироваться. Namespace помогают группировать ресурсы, например мониторинг и средства безопасности.

Можно разделять версии blue/green по namespace, сохраняя доступ к общим сервисам журналирования и мониторинга.

Также удобно разделять команды, чтобы имена ресурсов не конфликтовали. Права доступа и сетевую изоляцию при этом настраивают отдельно.
</b></details>

<details>
<summary>Верно ли, что при удалении namespace его ресурсы переносятся в default?</summary><br><b>

Неверно. Ресурсы этого пространства имён также удаляются.
</b></details>

<details>
<summary>Какие namespace создаются по умолчанию?</summary><br><b>

* default
* kube-system
* kube-public
* kube-node-lease
</b></details>

<details>
<summary>Что находится в kube-system?</summary><br><b>

* API-объекты системных компонентов и, в зависимости от установки, зеркальные поды control plane. Kubectl как клиентский процесс там не «живёт».
* Другие системные компоненты кластера.
</b></details>

<details>
<summary>Верно ли, что namespace задают область ресурсов, но сами по себе не обеспечивают полную изоляцию?</summary><br><b>

Верно. Например, поды разных namespace могут общаться без дополнительных сетевых ограничений.
</b></details>

<a id="namespaces---commands"></a>
#### Команды для namespace

<details>
<summary>Как вывести все namespace?</summary><br><b>

`kubectl get namespaces` или `kubectl get ns`.

</b></details>

<details>
<summary>Создайте namespace alle.</summary><br><b>

`k create ns alle`

</b></details>

<details>
<summary>Посчитайте namespace.</summary><br><b>

`k get ns --no-headers | wc -l`

</b></details>

<details>
<summary>Проверьте число подов в namespace dev.</summary><br><b>

`k get po -n dev`; для подсчёта: `k get po -n dev --no-headers | wc -l`.

</b></details>

<details>
<summary>Создайте под kartos с образом redis в namespace dev.</summary><br><b>

Если namespace ещё нет: `k create ns dev`.

`k run kartos --image=redis -n dev`. В исходнике имя не совпадало с заданием.

</b></details>

<details>
<summary>Как узнать, в каком namespace находится под atreus?</summary><br><b>

`k get po -A | grep atreus`

</b></details>

<details>
<summary>Что находится в kube-public?</summary><br><b>

* В зависимости от установки — ConfigMap с информацией о кластере.
* Данные, предназначенные для публичного чтения; фактический доступ определяется настройками.
</b></details>

<details>
<summary>Как узнать текущий namespace?</summary><br><b>

`kubectl config view --minify -o jsonpath='{..namespace}'`; если поле не задано, обычно используется `default`.
</b></details>

<details>
<summary>Что находится в kube-node-lease?</summary><br><b>

Объекты Lease узлов, обновляемые как свидетельство их доступности.
</b></details>

<details>
<summary>Можно ли ограничивать ресурсы команд с помощью namespace?</summary><br><b>

Да, назначая ResourceQuota и при необходимости LimitRange внутри namespace. Само создание namespace лимиты не устанавливает.
</b></details>

<details>
<summary>Как сменить текущий namespace?</summary><br><b>

`kubectl config set-context --current --namespace=some-namespace`; проверка: `kubectl config view --minify | grep namespace:`.

ИЛИ

`kubens some-namespace`
</b></details>

<a id="resources-quota"></a>
#### Квоты ресурсов

<details>
<summary>Что такое ResourceQuota?</summary><br><b>
  
Ограничение суммарного потребления ресурсов namespace: количества объектов разных типов и запрашиваемых или ограничиваемых вычислительных ресурсов.
</b></details>

<details>
<summary>Как создать ResourceQuota?</summary><br><b>

`kubectl create quota some-quota --hard=cpu=2,pods=2`
</b></details>

<details>
<summary>К каким ресурсам можно обращаться из другого namespace?</summary><br><b>

Например, к сетевым Service при разрешённом доступе.
</b></details>

<details>
<summary>На какой Service и namespace ссылается следующий файл?

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: some-configmap
data:
  some_url: samurai.jack
```
</summary><br><b>

На Service `samurai` в namespace `jack`.
</b></details>

<details>
<summary>Какие объекты не принадлежат namespace?</summary><br><b>

Например, Node и PersistentVolume. Уточнение: PVC, в отличие от PV, имеет namespace.
</b></details>

<details>
<summary>Как вывести типы ресурсов, привязанные к namespace?</summary><br><b>

`kubectl api-resources --namespaced=true`
</b></details>

<details>
<summary>Как создать объект в определённом namespace?</summary><br><b>

Передать параметр: `kubectl apply -f my_component.yaml --namespace=some-namespace`.
Или указать namespace в YAML:

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: some-configmap
  namespace: some-namespace
```

Проверка: `kubectl get configmap -n some-namespace`.
</b></details>

<details>
<summary>Как выполнить ls в существующем поде?</summary><br><b>

kubectl exec some-pod -it -- ls
</b></details>

<details>
<summary>Как создать Service для Deployment?</summary><br><b>

kubectl expose deploy some-deployment --port=80 --target-port=8080
</b></details>

<details>
<summary>Как одной командой создать под и Service?</summary><br><b>

kubectl run nginx --image=nginx --restart=Never --port 80 --expose
</b></details>

<details>
<summary>Подробно объясните <code>kubectl create deployment kubernetes-httpd --image=httpd</code>.</summary><br><b>

kubectl отправляет API запрос создания Deployment с образом httpd и именем kubernetes-httpd; контроллер создаёт ReplicaSet и Pod по шаблону. Это не создаёт Service, Ingress, сохранение данных или публичный URL. Перед production настройте версию образа, ресурсы, security context, probes и стратегию обновления.
</b></details>

<details>
<summary>Зачем Deployment, если поды может создавать ReplicaSet?</summary><br><b>

ReplicaSet поддерживает число подов по шаблону. Deployment управляет версиями ReplicaSet и раскаткой/откатом обновлений. Обычно пользователю удобнее менять Deployment, а не редактировать принадлежащий ему ReplicaSet напрямую.
</b></details>

<details>
<summary>Как вывести типы ресурсов кластерного уровня?</summary><br><b>

kubectl api-resources --namespaced=false
</b></details>

<details>
<summary>Как удалить все поды, фаза которых не Running?</summary><br><b>

kubectl delete pods --field-selector=status.phase!='Running'
</b></details>

<details>
<summary>Как посмотреть потребление ресурсов подами?</summary><br><b>

kubectl top pod
</b></details>

<details>
<summary>Вы подозреваете проблему с подом, но пока не знаете какую. С чего начать?</summary><br><b>

Проверьте `kubectl get pods`; `--all-namespaces` покажет поды всех namespace.<br>

При ошибке изучите `kubectl describe pod [name]` и журналы; для потокового просмотра нескольких подов можно использовать Stern.<br>

Если причина выяснена и допустим перезапуск, исходник предлагает масштабирование Deployment до нуля: `kubectl scale deployment [name] --replicas=0`. Это останавливает все его реплики и создаёт простой.<br>

Затем восстановите исходное число реплик; пример для одной: `kubectl scale deployment [name] --replicas=1`.
</b></details>

<details>
<summary>Что происходит, если контейнер превышает лимит памяти?</summary><br><b>

Ограничение памяти применяется ядром; процесс может быть завершён OOM killer, а контейнер получить состояние OOMKilled.
</b></details>

<details>
<summary>Опишите откат изменений.</summary><br><b>

Для Deployment: `kubectl rollout history deployment/<имя>`, затем `kubectl rollout undo deployment/<имя>` или конкретная revision. Проверьте статус и readiness. Откат Pod template не отменяет миграцию БД, внешние изменения и содержимое независимо изменённых ConfigMap/Secret. При GitOps согласуйте Git, иначе контроллер вернёт декларативную версию.
</b></details>

<details>
<summary>Верно ли, что память — сжимаемый ресурс и контейнер всегда продолжит работу после достижения лимита?</summary><br><b>

Неверно. CPU можно ограничить троттлингом, а нехватка памяти при лимите может привести к OOM-завершению. Достижение значения лимита не означает безусловного мгновенного завершения.
</b></details>

<a id="operators"></a>
### Операторы

<details>
<summary>Что такое оператор Kubernetes?</summary><br><b>

Описание — [здесь](https://kubernetes.io/docs/concepts/extend-kubernetes/operator).

Операторы расширяют Kubernetes с помощью пользовательских ресурсов и контроллеров для управления приложениями и их компонентами.

Их можно рассматривать как специализированные циклы согласования состояния.
</b></details>

<details>
<summary>Зачем нужны операторы?</summary><br><b>

Управление приложением с состоянием сложнее одинаковой замены независимых реплик. Разные экземпляры могут требовать разного порядка обновления и действий. Оператор автоматизирует знания и процедуры, которые иначе выполнял бы администратор.

Это также помогает одинаково выполнять процедуры в нескольких кластерах.
</b></details>

<details>
<summary>Из чего состоит оператор?</summary><br><b>

1. CRD — определение дополнительного типа API-ресурсов, помимо встроенных Pod, Deployment и Service.
2. Контроллер — цикл согласования экземпляров этих ресурсов с реальным состоянием приложения.

</b></details>

<details>
<summary>Объясните CRD.</summary><br><b>

CustomResourceDefinition — объект, добавляющий пользовательский тип ресурса в API Kubernetes.

Примечание исходника: раздел планируется дополнить.

</b></details>

<details>
<summary>Как работает оператор?</summary><br><b>

Наблюдает за изменениями объектов и приложения и выполняет специализированный цикл согласования.

Обычно использует CRD для расширения API.

</b></details>

<details>
<summary>Верно ли, что операторы применяют для приложений с состоянием?</summary><br><b>

Верно.
</b></details>

<details>
<summary>Что такое Operator Lifecycle Manager и зачем он нужен?</summary><br><b>

OLM управляет установкой, обновлением и зависимостями операторов в поддерживаемой экосистеме. Это отдельный компонент, не обязательная встроенная служба каждого Kubernetes-кластера; архитектура и APIs различаются между поколениями OLM. [Operator Framework](https://olm.operatorframework.io/).
</b></details>

<details>
<summary>Что такое Operator Framework?</summary><br><b>

Открытый набор средств создания и автоматизированного управления операторами Kubernetes.

</b></details>

<details>
<summary>Какие компоненты Operator Framework перечислены в исходнике?</summary><br><b>

1. Operator SDK — создание операторов.
2. Operator Lifecycle Manager — установка, обновление и управление жизненным циклом.
3. Operator Metering — исторический компонент отчётности об использовании сервисов операторов.
4. 
</b></details>

<details>
<summary>Подробнее опишите Operator Lifecycle Manager.</summary><br><b>

Часть Operator Framework, расширяющая Kubernetes для декларативной установки, обновления и сопровождения операторов.

</b></details>

<details>
<summary>Что содержит namespace openshift-operator-lifecycle-manager?</summary><br><b>

В описанной конфигурации:

  * catalog-operator — разрешение зависимостей и установка ресурсов каталогов и подписок.
  * olm-operator — развёртывание компонентов по ClusterServiceVersion.

</b></details>

<details>
<summary>Что такое kubeconfig и для чего он нужен?</summary><br><b>
  
Файл настройки доступа клиентов, например kubectl, к Kubernetes.
Хранит сведения о кластерах, пользователях, контекстах, namespace и способах аутентификации.
</b></details>

<details>
<summary>Для создания оператора вы выберете Helm, Go или другое средство?</summary><br><b>
  
Зависит от задач. Для установки и обновлений может хватить Helm-подхода; для сложного жизненного цикла, анализа состояния и автоматического управления часто нужен Go или другой язык контроллеров.
</b></details>

<details>
<summary>Какими средствами создания операторов вы пользуетесь?</summary><br><b>

Ответ зависит от опыта. Примеры:

* Operator Framework
* Kubebuilder
* Controller Runtime
...
</b></details>

<a id="secrets"></a>
### Секреты

<details>
<summary>Объясните Secrets Kubernetes.</summary><br><b>

Объекты для хранения и передачи чувствительных данных: паролей, SSH-ключей и т. п.

</b></details>

<details>
<summary>Как создать Secret из ключа и значения?</summary><br><b>

`kubectl create secret generic some-secret --from-literal=password='donttellmypassword'`

</b></details>

<details>
<summary>Как создать Secret из файла?</summary><br><b>

`kubectl create secret generic some-secret --from-file=/some/file.txt`
</b></details>

<details>
<summary>Что означает type: Opaque? Какие ещё типы Secret существуют?</summary><br><b>

Opaque — тип по умолчанию для произвольных пар ключ–значение.
</b></details>

<details>
<summary>Верно ли, что помещение данных в Secret автоматически делает их защищёнными?</summary><br><b>

Неверно. Контроль доступа и шифрование хранения нужно правильно настроить; Base64 защитой не является.
</b></details>

<details>
<summary>В чём проблема следующего Secret?

```
apiVersion: v1   
kind: Secret
metadata:
    name: some-secret
type: Opaque
data:
    password: mySecretPassword
```
</summary><br><b>

Значение в `data` должно иметь корректное кодирование Base64; это не шифрование.
Например, `echo -n 'mySecretPassword' | base64`. Можно также использовать `stringData` для ввода обычной строки. Уточнение к исходнику: кодирование не скрывает пароль от обладателя манифеста.

</b></details>

<details>
<summary>Что означает следующий фрагмент Deployment?

```
spec:
  containers:
    - name: USER_PASSWORD
      valueFrom:
        secretKeyRef:
          name: some-secret
          key: password
```
</summary><br><b>

Переменная окружения USER_PASSWORD получает значение ключа `password` из Secret `some-secret`.
То есть конфигурация ссылается на значение Kubernetes Secret.

</b></details>

<details>
<summary>Как хранить секреты в Git в зашифрованном виде?</summary><br><b>

Один из вариантов:

1. Подготовить Secret, не добавляя открытый вариант в Git.
2. Зашифровать подходящим инструментом, например kubeseal.
3. Применить зашифрованный объект SealedSecret.
4. Сохранить зашифрованный манифест в Git.
5. Контроллер Sealed Secrets в целевом кластере создаст доступный приложению Secret.
</b></details>

<a id="volumes-1"></a>
### Тома

<details>
<summary>Верно ли, что Kubernetes автоматически сохраняет любые данные после замены пода?</summary><br><b>

Неверно.
</b></details>

<details>
<summary>Что такое PersistentVolume и зачем он нужен?</summary><br><b>

Представление постоянного хранилища, жизненный цикл которого не зависит от отдельного пода.
</b></details>

<details>
<summary>Верно ли, что PersistentVolume обязан быть доступен всем узлам, поскольку под может попасть на любой?</summary><br><b>

Верно.
</b></details>

<details>
<summary>Какие технологии постоянного хранения вы знаете?</summary><br><b>

* NFS
* iSCSI
* CephFS
* ...
</b></details>

<details>
<summary>Что такое PersistentVolumeClaim?</summary><br><b>

Заявка на хранилище: размер, access mode и при необходимости StorageClass. PVC связывается с подходящим PV или запускает динамическое предоставление. PVC namespaced, PV — кластерный; статус Bound ещё не гарантирует успешное монтирование в конкретный Pod.
</b></details>

<details>
<summary>Что такое снимок тома?</summary><br><b>
  
Копия состояния тома на определённый момент времени, поддерживаемая соответствующим хранилищем и драйвером.
</b></details>

<details>
<summary>Верно ли, что Kubernetes сам управляет сохранностью любых данных?</summary><br><b>

Неверно.
</b></details>

<details>
<summary>Объясните StorageClass.</summary><br><b>

Кластерный объект, описывающий provisioner и параметры динамического хранилища, binding mode, reclaim policy и поддержку расширения. Для topology-aware устройств WaitForFirstConsumer помогает учесть размещение Pod. Класс не создаёт диск без работающего provisioner/драйвера.
</b></details>

<details>
<summary>Чем отличаются динамическое и статическое выделение томов?</summary><br><b>
  
При статическом подходе администратор заранее подготавливает PV, например с существующими данными. При динамическом том создаётся по запросу PVC через подходящий StorageClass и provisioner.
</b></details>

<details>
<summary>Объясните режимы доступа к томам.</summary><br><b>

RWO — чтение/запись с одного узла, а не обязательно одного Pod; ROX — чтение с нескольких узлов; RWX — чтение/запись с нескольких; RWOP — один Pod с поддерживаемым CSI. Режимы сопоставляют возможности PV/PVC и не заменяют права ФС и корректность конкурентной записи. [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/).
</b></details>

<details>
<summary>Что такое клонирование томов CSI?</summary><br><b>

Создание нового тома по содержимому существующего PVC через dataSource. Требует поддержки CSI-драйвера, корректных ограничений класса/режима/размера и namespace. Клон не является продолжающейся репликацией и сам не заменяет политику backup. [Volume cloning](https://kubernetes.io/docs/concepts/storage/volume-pvc-datasource/).
</b></details>

<details>
<summary>Объясните эфемерные тома.</summary><br><b>

Тома с жизненным циклом, связанным с Pod, для временных данных или доставки конфигурации. Перезапуск контейнера и удаление Pod — разные события: emptyDir сохраняется при первом и удаляется при втором. Generic ephemeral volume может использовать динамически созданный PVC.
</b></details>

<details>
<summary>Какие эфемерные тома поддерживает Kubernetes?</summary><br><b>

emptyDir, configMap, secret, downwardAPI; CSI ephemeral и generic ephemeral при поддержке драйвера; новые типы вроде image volume зависят от версии и feature support. Не все они одинаково учитываются в локальном ephemeral-storage лимите. [Ephemeral volumes](https://kubernetes.io/docs/concepts/storage/ephemeral-volumes/).
</b></details>

<details>
<summary>Что такое reclaim policy?</summary><br><b>

Определяет судьбу PV/хранилища после освобождения PVC: Retain сохраняет для ручной обработки, Delete удаляет связанные ресурсы при поддержке provisioner. Устаревший Recycle не рекомендуют. Удаление PVC с Delete может уничтожить данные; проверяйте политику и backup заранее.
</b></details>

<details>
<summary>Какие политики освобождения томов существуют?</summary><br><b>

* Retain
* Recycle — устаревший вариант, сохранённый в перечне исходника.
* Delete
</b></details>

<a id="access-control"></a>
### Управление доступом

<details>
<summary>Что такое RBAC?</summary><br><b>
 
Ролевое управление доступом: наборы разрешений определяют, что пользователи, группы и ServiceAccount могут делать с API-ресурсами в namespace или на уровне кластера.
</b></details>

<details>
<summary>Объясните Role и RoleBinding.</summary><br><b>

Role задаёт разрешения на namespaced-ресурсы в namespace; RoleBinding назначает Role или применимую ClusterRole субъектам в namespace. ClusterRole/ClusterRoleBinding имеют другую область. Проверяйте доступ через `kubectl auth can-i`; избегайте wildcard и выдачи bind/escalate без необходимости.
</b></details>

<details>
<summary>Чем Role отличается от ClusterRole?</summary><br><b>
  
Role существует в namespace. ClusterRole — кластерный объект правил; область выданных прав зависит и от привязки RoleBinding или ClusterRoleBinding.
</b></details>

<details>
<summary>Что такое ServiceAccount и когда он нужен?</summary><br><b>

[Kubernetes.io](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account): идентичность для процессов, работающих в поде.

Пример:
Конвейеру сборки могут понадобиться API-права и доступ к реестру. Ему назначают отдельный ServiceAccount и необходимые разрешения; доступ к внешнему реестру настраивается отдельно.
</b></details>

<details>
<summary>Что будет, если при создании пода ServiceAccount не указан?</summary><br><b>

Обычно назначается ServiceAccount `default` его namespace.
</b></details>

<details>
<summary>Чем ServiceAccount отличается от обычного пользователя?</summary><br><b>

  - ServiceAccount — объект конкретного namespace; обычные пользовательские идентичности не являются такими объектами.
  - ServiceAccount обычно используется рабочими нагрузками; пользователи представляют людей и внешние клиенты.
</b></details>

<details>
<summary>Как вывести ServiceAccount?</summary><br><b>

`kubectl get serviceaccounts`
</b></details>

<details>
<summary>Что такое security context?</summary><br><b>

[kubernetes.io](https://kubernetes.io/docs/tasks/configure-pod-container/security-context): настройки привилегий и контроля доступа пода или контейнера.
</b></details>

<a id="patterns"></a>
### Паттерны



<a id="cronjob"></a>
### CronJob

<details>
<summary>Что такое CronJob и для чего он нужен?</summary><br><b>
  
Создаёт Job по повторяющемуся расписанию в формате cron, подобно строке crontab.
</b></details>

<details>
<summary>Какая проблема возможна со следующей конфигурацией и как её исправить?

```
apiVersion: batch/v1
kind: CronJob
metadata:
  name: some-cron-job
spec:
  schedule: '*/1 * * * *'
  startingDeadlineSeconds: 10
  concurrencyPolicy: Allow
```
</summary><br><b>

При `concurrencyPolicy: Allow` очередная задача может стартовать, пока предыдущая ещё работает. Если задачи зависают, активные выполнения могут накапливаться. Уточнение: очистка уже завершённых ошибочных Job регулируется отдельными настройками истории.
Для ограничения пересечений используйте `Forbid` или `Replace`, исходя из требований приложения.
</b></details>

<details>
<summary>В чём проблема следующего CronJob и как её исправить?

```
apiVersion: batch/v1
kind: CronJob
metadata:
  name: "some-cron-job"
spec:
  schedule: '*/1 * * * *'
jobTemplate:
  spec:
    template:
      spec:
      restartPolicy: Never
      concurrencyPolicy: Forbid
      successfulJobsHistoryLimit: 1
      failedJobsHistoryLimit: 1
```
</summary><br><b>

Следующие поля ошибочно размещены внутри шаблона:

```
concurrencyPolicy: Forbid
successfulJobsHistoryLimit: 1
failedJobsHistoryLimit: 1
```

Они не окажутся корректными полями CronJob; API может отклонить или обработать неизвестные поля согласно режиму проверки. Уточнение: лимиты истории Job не являются лимитами памяти контейнера.<br>
Перенесите эти поля в `spec` CronJob рядом с `schedule`.
Также `jobTemplate` должен находиться внутри `spec`, `restartPolicy` — внутри спецификации пода, а шаблон должен содержать контейнер. Исправленный минимальный вариант:

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: some-cron-job
spec:
  schedule: "*/1 * * * *"
  concurrencyPolicy: Forbid
  successfulJobsHistoryLimit: 1
  failedJobsHistoryLimit: 1
  jobTemplate:
    spec:
      template:
        spec:
          restartPolicy: Never
          containers:
            - name: task
              image: busybox:1.37
              command: ["sh", "-c", "date"]
```

Задания должны быть идемпотентными: расписание не даёт гарантии exactly-once. [Миграция API](https://kubernetes.io/docs/reference/using-api/deprecation-guide/).

</b></details>

<a id="misc"></a>
###  Разное

<details>
<summary>Чем императивное управление отличается от декларативного?</summary><br><b>

Императивно задают действие, например create/scale; декларативно — желаемое состояние, которое контроллеры и apply согласуют с текущим. Один объект не стоит бесконтрольно управлять несколькими способами: возможны конфликты field ownership и GitOps.
</b></details>

<details>
<summary>Что означает обнаружение сервисов в Kubernetes?</summary><br><b>

Клиенты находят Service через DNS и/или предусмотренные переменные окружения; DNS обычно обслуживает CoreDNS. EndpointSlice связывает Service с backend-адресами при наличии селектора/контроллера. Headless Service может возвращать адреса endpoint вместо виртуального IP; доступность зависит также от readiness и сетевых политик.
</b></details>

<details>
<summary>Несколько команд используют один кластер. Как ограничить потребление ресурсов каждой?</summary><br><b>

Разделить их по namespace и настроить ResourceQuota и LimitRange. Namespace также помогают избегать конфликтов имён.
</b></details>

<details>
<summary>Что делает kube-proxy?</summary><br><b>
Реализует часть сетевой модели Service, поддерживая правила направления трафика на узлах.
</b></details>

<details>
<summary>Для чего нужны ResourceQuota и как их применять?</summary><br><b>

Объект ResourceQuota ограничивает суммарное использование/число выбранных ресурсов в namespace. Создайте квоту, согласуйте requests/limits и LimitRange, затем проверьте отказ избыточной заявки и `kubectl describe quota`. Квота не гарантирует физической ёмкости узлов и не заменяет распределение по командам/RBAC.
</b></details>

<details>
<summary>Объясните ConfigMap.</summary><br><b>

Отделяет несекретную конфигурацию от образа и описания приложения.
Позволяет менять данные без пересборки образа. Уточнение: автоматическое применение изменений без перезапуска зависит от способа подключения и способности приложения перечитывать настройки.

Полезен для:
* Общих настроек нескольких подов.
* Хранения конфигурации отдельным объектом.
</b></details>

<details>
<summary>Как использовать ConfigMap?</summary><br><b>

1. Создать из пар ключ–значение, файла или env-файла.
2. Подключить, например как том пода.
</b></details>

<details>
<summary>Верно ли, что учётные данные стоит хранить в ConfigMap?</summary><br><b>

Неверно. Используйте Secret с надлежащей защитой.
</b></details>

<details>
<summary>Что такое HorizontalPodAutoscaler?</summary><br><b>

Контроллер, изменяющий число реплик поддерживаемой рабочей нагрузки по метрикам, чтобы адаптировать её к спросу.
</b></details>

<details>
<summary>Удаляется ли под мгновенно после команды удаления?</summary><br><b>

Обычно нет. API помечает удаление, kubelet выполняет остановку с grace period и hooks; finalizers могут задержать завершение. Force deletion удаляет API-объект без гарантии, что процесс на недоступном узле уже остановился, что особенно опасно для stateful workloads.
</b></details>

<details>
<summary>Что означает cloud-native?</summary><br><b>
Подход к созданию и эксплуатации приложений, использующий возможности распределённых облачных систем.
</b></details>

<details>
<summary>Объясните подходы pets и cattle к инфраструктуре применительно к Kubernetes.</summary><br><b>

Pets — индивидуальные узлы с ручным уходом; cattle — заменяемые экземпляры, восстанавливаемые из описания. Kubernetes поддерживает декларативную заменяемость, но состояние и уникальная идентичность не исчезают автоматически: StatefulSet и диски требуют отдельного проектирования.
</b></details>

<details>
<summary>Как развернуть контейнерное веб-приложение, доступное по публичному URL?</summary><br><b>

Соберите и опубликуйте образ, создайте Deployment с ресурсами/probes и Service, затем поддерживаемый Gateway/Ingress или LoadBalancer. Настройте DNS, TLS, права, сетевые политики и наблюдаемость. Публичный адрес не появляется просто от `containerPort`; необходима соответствующая внешняя инфраструктура.
</b></details>

<details>
<summary>Как диагностировать кластер, если приложения перестали быть доступны?</summary><br><b>

Определите масштаб и последние изменения, проверьте клиентский DNS/TLS → внешний LB/Gateway → Service/EndpointSlice → readiness и контейнеры → узлы/CNI/хранилище. Используйте events, логи, describe и проверки внутри namespace. Изменяйте один подтверждённый фактор за раз; restart всего кластера может скрыть причину и расширить отказ.
</b></details>

<details>
<summary>Что такое CRD и для чего они используются?</summary><br><b>

CustomResourceDefinition добавляет тип Kubernetes API со схемой и правилами валидации. Объекты custom resource хранят желаемое состояние; контроллер реализует действие. Создание CRD без контроллера не создаёт внешнюю инфраструктуру. Учитывайте versions, conversion, RBAC и жизненный цикл данных.
</b></details>

<details>
<summary>Как работает планирование подов?</summary><br><b>

Kube-scheduler:
1. Анализирует требования неназначенного пода.
2. Выбирает подходящий узел с учётом ресурсов и ограничений.
3. Назначает под выбранному узлу.

Подробнее — [здесь](https://www.youtube.com/watch?v=rDCWxkvPlAw).
</b></details>

<details>
<summary>Как используются метки и селекторы?</summary><br><b>

Метки — пары ключ–значение для организации объектов; селекторы выбирают наборы по условиям. Они используются Service, ReplicaSet и другими механизмами. Не помещайте секреты в labels; изменение меток может неожиданно изменить принадлежность трафика и контроллера.
</b></details>

<details>
<summary>Какие классы QoS существуют?</summary><br><b>

* Guaranteed
* Burstable
* BestEffort
</b></details>

<details>
<summary>Что такое метки и зачем они нужны?</summary><br><b>
  
Пары ключ–значение с идентифицирующими метаданными объектов Kubernetes.
</b></details>

<details>
<summary>Объясните селекторы.</summary><br><b>

Equality-based условия `key=value`, `key!=value` и set-based `in`, `notin`, наличие/отсутствие ключа там, где API их поддерживает. Несколько условий обычно соединяются AND; синтаксис и поддержка зависят от поля, Service selector — карта равенств, а не произвольное выражение.
</b></details>

<details>
<summary>Что такое kubeconfig?</summary><br><b>

Файл конфигурации клиентов: clusters, users, contexts и текущий context. Он может содержать credentials или исполняемый auth plugin, поэтому не считайте недоверенный kubeconfig безопасным. Перед командой проверьте context/namespace и храните файл с ограниченными правами.
</b></details>

<a id="gatekeeper"></a>
### Gatekeeper

<details>
<summary>Что такое Gatekeeper?</summary><br><b>

[Документация Gatekeeper](https://open-policy-agent.github.io/gatekeeper/website/docs): контроллер применения политик на основе CRD и Open Policy Agent. В исходнике описан validating webhook; доступные возможности зависят от версии.
</b></details>

<details>
<summary>Как работает Gatekeeper?</summary><br><b>

В процессе admission настроенный webhook проверяет подходящие запросы по политикам OPA. При нарушении возвращает отказ с объяснением; разрешённый запрос продолжает обработку. Уточнение: это не обязательная проверка любого запроса чтения API.
</b></details>

<a id="policy-testing"></a>
### Проверка политик

<details>
<summary>Что такое Conftest?</summary><br><b>

Средство проверки структурированных файлов по политикам, в том числе манифестов Kubernetes.<br>
Обычно применяется в CI или локальных проверках перед фиксацией изменений.
</b></details>

<details>
<summary>Что такое Datree и чем он отличается от Conftest?</summary><br><b>

В исходнике он описан как средство проверки политик с готовым набором правил; это описание инструмента на момент написания материала.
</b></details>

<a id="helm"></a>
### Helm

<details>
<summary>Что такое Helm?</summary><br><b>

Пакетный менеджер Kubernetes: упаковывает шаблоны манифестов, распространяет их и управляет установками в кластере.

Аналогия — пакетные менеджеры ОС: dnf в Fedora/RHEL и apt в Ubuntu. Автор исходника шутливо предлагает отдельно обсудить, почему читатель может не использовать Linux.
</b></details>

<details>
<summary>Зачем нужен Helm? Приведите сценарии.</summary><br><b>

Приложению могут понадобиться Secret, Service, ConfigMap и другие манифесты. Helm объединяет их в параметризованный пакет, упрощая повторную установку и распространение.

Например, один chart можно устанавливать в dev, staging и production с разными значениями вместо ручного применения множества YAML.

Или опубликовать chart, чтобы сообщество легко разворачивало ваше приложение.
</b></details>

<details>
<summary>Что такое Helm chart?</summary><br><b>

Пакет шаблонов, метаданных и настроек Kubernetes. Его можно получить из репозитория или создать и опубликовать самостоятельно.
</b></details>

<details>
<summary>Почему Helm называют шаблонизатором?</summary><br><b>

Для похожих конфигураций задаётся общий шаблон, а меняющиеся значения передаются параметрами. Например:

```
apiVersion: v1
kind: Pod
metadata:
  name: {[ .Values.name ]}
spec:
  containers:
  - name: {{ .Values.container.name }}
  image: {{ .Values.container.image }}
  port: {{ .Values.container.port }}
```

Значения находятся в отдельном файле:

```
name: some-app
container:
  name: some-app-container
  image: some-app-image
  port: 1991
```
</b></details>

<details>
<summary>Когда полезны шаблоны Helm?</summary><br><b>

* Развёртывание одного приложения в разных средах.
* CI/CD
</b></details>

<details>
<summary>Объясните структуру каталога chart.</summary><br><b>

someChart/ — каталог chart.
  Chart.yaml — метаданные.
  values.yaml — значения для шаблонов.
  charts/ — зависимости.
  templates/ — шаблоны.
</b></details>

<details>
<summary>Как Helm управляет релизами?</summary><br><b>

Позволяет устанавливать, обновлять, удалять релизы и откатывать их ревизии. В Helm 2 использовался серверный Tiller; в Helm 3 его убрали, изменив модель взаимодействия и безопасности.
</b></details>

<a id="commands"></a>
#### Команды

<details>
<summary>Как искать charts?</summary><br><b>

`helm search hub [some_keyword]`
</b></details>

<details>
<summary>Можно ли переопределить values.yaml при установке?</summary><br><b>
Да, например другим файлом значений:
`helm install RELEASE_NAME CHART_NAME --values=override-values.yaml`

Или аргументом: `helm install RELEASE_NAME CHART_NAME --set some_key=some_value`.
</b></details>

<details>
<summary>Как вывести установленные релизы?</summary><br><b>

`helm ls` или `helm list`.
</b></details>

<details>
<summary>Как выполнить откат?</summary><br><b>

`helm rollback RELEASE_NAME REVISION_ID`
</b></details>

<details>
<summary>Как посмотреть историю ревизий релиза?</summary><br><b>

`helm history RELEASE_NAME`
</b></details>

<details>
<summary>Как обновить релиз?</summary><br><b>

`helm upgrade RELEASE_NAME CHART_NAME`
</b></details>

<a id="security"></a>
### Безопасность

<details>
<summary>Каких рекомендаций по безопасности кластера вы придерживаетесь?</summary><br><b>

  * Защищайте межсервисный обмен, например mutual TLS через Istio.
  * Группируйте ресурсы по namespace и отдельно настраивайте изоляцию.
  * Используйте поддерживаемую CRI-среду выполнения. Уточнение: удаление dockershim не означает запрета Docker-образов или Docker как инструмента сборки.
  * Проверяйте изменения и манифесты автоматически; исходник приводит Datree как один из примеров.
  * Ограничивайте права через RBAC и допустимые конфигурации через admission-политики, например Gatekeeper.
  * Применяйте NetworkPolicy с поддерживающей их сетевой реализацией.
  * Отслеживайте угрозы, например средствами вроде Falco.
</b></details>

<a id="troubleshooting-scenarios"></a>
### Сценарии диагностики

<details>
<summary>Поды находятся в Pending. Что проверить?</summary><br><b>

Начните с `kubectl describe pod <pod name>`.<br>
Возможные причины:
  * Недостаточно ресурсов: расширьте кластер или скорректируйте запросы.
  * Ограничения квоты: проверьте события и допустимые ресурсы. Квота часто мешает самому созданию объектов, а не только размещению уже существующего пода.
  * Ожидание PVC или подготовки хранилища.

Через `get pods -o wide` проверьте назначение узла. Если его нет, исследуйте Scheduler и ограничения размещения.
</b></details>

<details>
<summary>Пользователи не могут обратиться к приложению в поде. Что проверить?</summary><br><b>

Один из вариантов — начать со состояния пода.
1. Если он Pending, выясните причину через `kubectl describe pod <pod name>`.
Примечание исходника: ответ не завершён.
</b></details>

<a id="istio"></a>
### Istio

<details>
<summary>Что такое Istio и зачем он нужен?</summary><br><b>
  
Открытая service mesh для распределённых микросервисных приложений. Помогает защищать, соединять и наблюдать сервисы.
</b></details>

<a id="controllers"></a>
### Контроллеры

<details>
<summary>Что такое контроллеры?</summary><br><b>

[Kubernetes.io](https://kubernetes.io/docs/concepts/architecture/controller): циклы, наблюдающие состояние кластера и выполняющие или запрашивающие изменения, чтобы приблизить фактическое состояние к желаемому.
</b></details>

<details>
<summary>Назовите два контроллера.</summary><br><b>

1. Контроллер узлов отслеживает их доступность и обновляет состояние. При отказах связанные механизмы могут инициировать выселение подов с учётом тайм-аутов.
2. Контроллер репликации поддерживает заданное количество реплик подов.
</b></details>

<details>
<summary>Какой процесс запускает встроенные контроллеры?</summary><br><b>

Kube-Controller-Manager
</b></details>

<details>
<summary>Что такое цикл управления и как он работает?</summary><br><b>

Объяснение — [здесь](https://www.youtube.com/watch?v=i9V4oCa5f9I).
</b></details>

<details>
<summary>Назовите этапы цикла управления.</summary><br><b>

- Observe — наблюдение текущего состояния.
- Diff — определение отличий от желаемого.
- Act — действия для устранения отличий.
</b></details>

<a id="scheduler-1"></a>
### Планировщик

<details>
<summary>Верно ли, что Scheduler и выбирает узел, и запускает контейнеры пода?</summary><br><b>

Неверно. Scheduler выбирает узел; kubelet через среду выполнения организует запуск контейнеров.
</b></details>

<details>
<summary>Как назначить под узлу node1?</summary><br><b>

`k run some-pod --image=redis -o yaml --dry-run=client > pod.yaml`

Откройте `vi pod.yaml` и добавьте:

```
spec:
  nodeName: node1
```

`k apply -f pod.yaml`

Если node1 отсутствует, под не сможет запуститься на нём и останется Pending.
</b></details>

<a id="node-affinity"></a>
#### Привязка к узлам

<details>
<summary>Через node affinity разместите под на узле, у которого region равно asia или emea.</summary><br><b>

`vi pod.yaml`

```yaml
affinity:
  nodeAffinity:
    requiredDuringSchedlingIgnoredDuringExecution:
      nodeSelectorTerms:
      - matchExpressions:
        - key: region
          operator: In
          values:
          - asia
          - emea
```
</b></details>

<details>
<summary>Через node affinity запретите размещение пода на узле с region=neverland.</summary><br><b>

`vi pod.yaml`

```yaml
affinity:
  nodeAffinity:
    requiredDuringSchedlingIgnoredDuringExecution:
      nodeSelectorTerms:
      - matchExpressions:
        - key: region
          operator: NotIn
          values:
          - neverland
```
</b></details>

<details>
<summary>Верно ли, что requiredDuringSchedulingIgnoredDuringExecution запрещает размещение при невыполнении условия?</summary><br><b>

Верно.
</b></details>

<details>
<summary>Верно ли, что preferredDuringSchedulingIgnoredDuringExecution запрещает размещение при невыполнении предпочтения?</summary><br><b>

Неверно. Scheduler предпочитает подходящий узел, но может выбрать другой, если обязательные требования соблюдены.
</b></details>

<details>
<summary>Можно ли запускать несколько планировщиков?</summary><br><b>

Да. Например, дополнительный экземпляр с командой следующего вида:

```
spec:
  containers:
  - command:
    - kube-scheduler
    - --address=127.0.0.1
    - --leader-elect=true
    - --scheduler-name=some-custom-scheduler
...
```
</b></details>

<details>
<summary>Как определить, какой планировщик назначил конкретный под?</summary><br><b>

Проверьте события через `kubectl get events` и поле `spec.schedulerName` пода.
</b></details>

<details>
<summary>Как назначить новый под пользовательскому планировщику?</summary><br><b>

Добавьте в spec пода:

```
spec:
  schedulerName: some-custom-scheduler
```
</b></details>

<a id="taints"></a>
### Ограничения taint

<details>
<summary>Проверьте taints узла master.</summary><br><b>

`k describe no master | grep -i taints`
</b></details>

<details>
<summary>Добавьте узлу taint app=web с эффектом NoSchedule и проверьте результат.</summary><br><b>

`k taint node minikube app=web:NoSchedule`

`k describe no minikube | grep -i taints`
</b></details>

<details>
<summary>На единственном узле задан app=web:NoSchedule. Что будет после kubectl run some-pod --image=redis?</summary><br><b>

Без подходящего toleration под останется Pending: доступный узел имеет непереносимый им taint.
</b></details>

<details>
<summary>Как запустить этот под при taint app=web:NoSchedule на единственном узле?</summary><br><b>

Выполните `kubectl edit po some-pod` и добавьте toleration:

```
  - effect: NoSchedule
    key: app
    operator: Equal
    value: web
```

Сохраните изменения. Если других препятствий нет, под будет назначен и запущен.
</b></details>

<details>
<summary>Удалите существующий taint узла.</summary><br><b>

`k taint node minikube app=web:NoSchedule-`
</b></details>

<details>
<summary>Какие эффекты taint существуют?</summary><br><b>

`NoSchedule` — не назначать новые поды без подходящего toleration.
`PreferNoSchedule` — по возможности избегать размещения таких подов.
`NoExecute` — также выселять уже работающие поды без подходящего toleration, с учётом `tolerationSeconds`. `NoSchedule` существующие поды не выселяет.
</b></details>

<a id="resource-limits"></a>
### Лимиты ресурсов

<details>
<summary>Зачем задавать лимиты ресурсов?</summary><br><b>

* Чтобы ограничить потребление выше допустимого для приложения уровня.
* Чтобы одна нагрузка не вытеснила остальные приложения кластера.
</b></details>

<details>
<summary>Верно ли, что лимит 2 ГБ автоматически делится пополам между двумя контейнерами пода?</summary><br><b>

Нет. В обычной конфигурации `containers[].resources` лимиты задаются каждому контейнеру отдельно. Даже при поддержке ресурсов уровня пода автоматическое равное деление не подразумевается.
</b></details>

<a id="resources-limits---commands"></a>
#### Команды для лимитов ресурсов

<details>
<summary>Проверьте лимиты одного из подов.</summary><br><b>

`kubectl describe po <POD_NAME> | grep -i limits`
</b></details>

<details>
<summary>Создайте под yay с образом python и requests: память 64Mi, CPU 250m.</summary><br><b>

`kubectl run yay --image=python --dry-run=client -o yaml > pod.yaml`

`vi pod.yaml`

```
spec:
  containers:
  - image: python
    imagePullPolicy: Always
    name: yay
    resources:
      requests:
        cpu: 250m
        memory: 64Mi
```

`kubectl apply -f pod.yaml`
</b></details>

<details>
<summary>Создайте под yay2 с образом python, requests 64Mi и 250m, limits 128Mi и 500m.</summary><br><b>

`kubectl run yay2 --image=python --dry-run=client -o yaml > pod.yaml`

`vi pod.yaml`

```
spec:
  containers:
  - image: python
    imagePullPolicy: Always
    name: yay2
    resources:
      limits:
        cpu: 500m
        memory: 128Mi
      requests:
        cpu: 250m
        memory: 64Mi
```

`kubectl apply -f pod.yaml`
</b></details>

<a id="monitoring"></a>
### Мониторинг

<details>
<summary>Какие средства мониторинга Kubernetes вы знаете?</summary><br><b>

Есть открытые и коммерческие решения с разными задачами. Например:

* metrics-server — сбор текущих метрик ресурсов для API метрик; данные не являются долгосрочной историей мониторинга.
* Datadog — коммерческая платформа.
* Prometheus — открытая система мониторинга.

</b></details>

<details>
<summary>Как используемое вами решение наблюдает Kubernetes?</summary><br><b>

Зависит от решения. Например:

* metrics-server получает показатели ресурсов от kubelet и предоставляет их через Metrics API; это компонент для текущих метрик, а не полноценный долговременный мониторинг.
После установки можно использовать `kubectl top node` и `kubectl top pod`.

Примечание исходника: добавить описание других решений.

</b></details>

<a id="kustomize-1"></a>
### Kustomize

<details>
<summary>Что такое Kustomize?</summary><br><b>

Средство декларативного составления и изменения Kubernetes-манифестов через base/overlays, patches, generators и transformations. `kubectl kustomize` показывает результат, `kubectl apply -k` применяет. Это не шаблонизатор Helm; внимательно проверяйте итоговый YAML и версии встроенного Kustomize.
</b></details>

<details>
<summary>Зачем нужен Kustomize? Приведите примеры.</summary><br><b>

* Несколько команд используют общую конфигурацию приложения, но каждой нужна своя аннотация владельца.
  * Без механизма настройки пришлось бы копировать и менять исходные файлы, если нужного параметра нет в chart.
  * Kustomize позволяет применять изменения поверх базовых манифестов без полного копирования.
* Нужно добавить патч, не меняя исходные файлы приложения.
  * Опишите изменения в `kustomization.yaml`, сохранив базовые файлы.
</b></details>

<details>
<summary>Как в общих чертах работает Kustomize?</summary><br><b>

1. Создайте `kustomization.yaml` в нужном каталоге.
   1. Укажите ресурсы и преобразования.
2. Выполните `kustomize build APP_PATH`. Уточнение: в исходнике используется имя `kustomization.yml`; стандартное поддерживаемое имя — `kustomization.yaml` или иной документированный вариант.
</b></details>

<a id="deployment-strategies"></a>
### Стратегии развёртывания

<details>
<summary>Какие стратегии развёртывания вы знаете?</summary><br><b>

* Blue/Green: новая версия запускается рядом со старой, затем трафик переключается на неё.
* Canary: на новую версию сначала направляется только часть трафика, затем доля постепенно увеличивается.
</b></details>

<details>
<summary>Подробно объясните Blue/Green.</summary><br><b>

Шаги:

1. Балансировщик направляет пользовательский трафик на версию 1.

Пользователи → балансировщик → версия 1.

2. Рядом развёртывается версия 2; версия 1 продолжает работать.

Пользователи → балансировщик → версия 1.
Версия 2 пока готовится к обслуживанию трафика.

3. После проверки трафик переключается на версию 2.

Версия 1 остаётся отдельно от основного пользовательского потока.
Пользователи → балансировщик → версия 2.

4. Команда решает, удалить старую версию или оставить для быстрого отката.

Преимущества:
  * Можно быстро переключить трафик обратно, если старая версия сохранена и совместима с данными.
Недостатки:
  * Ошибка новой версии после полного переключения затрагивает всех пользователей.

</b></details>

<details>
<summary>Подробно объясните Canary.</summary><br><b>

Шаги:

1. Балансировщик направляет пользовательский трафик на версию 1.

Пользователи → балансировщик → версия 1.

2. Рядом с версией 1 развёртывается версия 2, получающая небольшую часть трафика.

Балансировщик направляет 95% трафика на версию 1,
а 5% — на версию 2.

3. Если новая версия работает хорошо, её доля увеличивается.

Например, 70% трафика остаётся у версии 1,
а 30% получает версия 2.

4. После успешной проверки весь трафик переключается.

Пользователи → балансировщик → версия 2.


Преимущества:
  * На раннем этапе ошибка новой версии затрагивает только часть пользователей.
Недостатки:
  * Проверка на реальном пользовательском трафике происходит в рабочей среде.

</b></details>

<details>
<summary>Как реализовать canary или blue/green в Kubernetes?</summary><br><b>

Один из вариантов — Argo Rollouts.
</b></details>

<a id="scenarios"></a>
### Практические ситуации

<details>
<summary>Инженер хочет видеть ресурсы только своей команды, а не всей организации. Что использовать?</summary><br><b>

Namespace для группировки и RBAC для ограничения доступа. Подробнее — [в вопросе о namespace](#namespaces-use-cases).
</b></details>

<details>
<summary>Под показывает CrashLoopBackOff. Что это значит и как искать причину?</summary><br><b>

Контейнер повторно завершается; между попытками перезапуска применяется увеличивающаяся задержка.

Возможные причины:
  - Неверная конфигурация, опечатка или неподдерживаемое значение.
  - Недоступная приложению зависимость или ресурс. Ошибки узла и монтирования могут давать другие состояния и требуют отдельной проверки.

Диагностика:

1. `kubectl describe pod POD_NAME`
   1. Изучите `State`, `Last State`, причину и код последнего завершения.
2. Выполните `kubectl logs mypod`, при необходимости добавив `--previous`.
   1. Журналы помогут определить ошибку приложения.
   2. Для нужного контейнера добавьте `-c CONTAINER_NAME`.
</b></details>

<details>
<summary>Как запретить подам с определённой меткой размещаться на одном из узлов?</summary><br><b>

Для такого ограничения задайте подходящие правила node affinity выбранным подам. Уточнение к исходнику: `kubectl taint node node1 app=web:NoSchedule` не выбирает поды по метке `app=web`; он запрещает размещение всех подов без соответствующего toleration.
</b></details>

<details>
<summary>Как ограничить число объектов, например четырьмя ReplicaSet и двумя Service?</summary><br><b>

Настроить ResourceQuota в соответствующем namespace.
</b></details>

<!-- {% endraw %} -->

Примечание: при техническом аудите обновлены примеры Ingress и CronJob; дополнительные изменения отражены в журнале проверки. Справка по уточнениям: https://kubernetes.io/docs/concepts/security/secrets-good-practices/

## Дополнение: Ingress и Gateway API

<details>
<summary>Какой API рассматривать для новой HTTP-маршрутизации?</summary>

Ingress остаётся стабильным API, но его развитие заморожено. Для новых возможностей Kubernetes рекомендует Gateway API. Это набор CRD и контроллеров, а не автоматически работающий компонент любого кластера. GatewayClass выбирает реализацию, Gateway описывает listeners, HTTPRoute задаёт HTTP-маршруты.

Пример маршрута при уже установленном Gateway API и существующем Gateway `web-gateway` с HTTP-listener в том же namespace:

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: someapp
spec:
  parentRefs:
    - name: web-gateway
  hostnames:
    - "app.example.com"
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: /
      backendRefs:
        - name: someapp-internal-service
          port: 8080
```

Создайте Service на указанном порту, настройте DNS и проверьте условия Accepted/ResolvedRefs в status маршрута. Для HTTPS нужны TLS-listener и сертификат. Межпространственные ссылки дополнительно ограничиваются политиками и ReferenceGrant в применимых случаях.

[Gateway API](https://gateway-api.sigs.k8s.io/) · [Статус Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/).
</details>

<details>
<summary>Можно ли выбирать ingress-nginx для новой установки?</summary>

Общественный проект ingress-nginx завершил сопровождение в марте 2026 года: дальнейшие релизы, исправления ошибок и уязвимостей не предусмотрены. Существующие установки могут продолжать работать, но нужен план миграции на поддерживаемый контроллер. Это относится к конкретному проекту ingress-nginx, а не ко всему NGINX, всем Ingress-контроллерам или самому API Ingress.

[Официальное объявление](https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/).
</details>
