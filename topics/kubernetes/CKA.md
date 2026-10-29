<a id="cka-certified-kubernetes-administrator"></a>
# CKA — сертифицированный администратор Kubernetes

- [CKA — сертифицированный администратор Kubernetes](#cka-certified-kubernetes-administrator)
  - [Подготовка](#setup)
  - [Поды](#pods)
    - [Поиск неисправностей подов](#troubleshooting-pods)
  - [Пространства имён](#namespaces)
  - [Узлы](#nodes)
  - [Сервисы](#services)
  - [Наборы реплик](#replicasets)
    - [Поиск неисправностей ReplicaSet](#troubleshooting-replicasets)
  - [Развёртывания](#deployments)
    - [Поиск неисправностей Deployment](#troubleshooting-deployments)
  - [Планировщик](#scheduler)
    - [Привязка к узлам](#node-affinity)
  - [Метки и селекторы](#labels-and-selectors)
    - [Селектор узла](#node-selector)
  - [Ограничения taint](#taints)
  - [Ограничения ресурсов](#resources-limits)
  - [Мониторинг](#monitoring)
  - [Планировщик](#scheduler-1)

<a id="setup"></a>
## Подготовка

* Разверните кластер Kubernetes одним из способов:
  1. Minikube — простой бесплатный локальный кластер.
  2. Управляемый кластер EKS, GKE или AKS.
* Настройте псевдонимы команд:

```
alias k=kubectl
alias kd=kubectl delete
alias kds=kubectl describe
alias ke=kubectl edit
alias kr=kubectl run
alias kg=kubectl get
```

<a id="pods"></a>
## Поды

<details>
<summary>Выведите все поды текущего пространства имён.</summary><br><b>

`kubectl get pods`

Создайте псевдоним `alias k=kubectl` и привыкайте к сокращению `k get po`.
</b></details>

<details>
<summary>Запустите под nginx-test из образа nginx.</summary><br><b>

`k run nginx-test --image=nginx`
</b></details>

<details>
<summary>Как удалить под nginx-test?</summary><br><b>

`k delete po nginx-test`
</b></details>

<details>
<summary>В каком пространстве имён работает под etcd? Выведите поды этого пространства.</summary><br><b>

`k get po -n kube-system`

Если пространство неизвестно, выполните `k get po -A | grep etc` и найдите нужный под. Это относится к кластерам, где etcd виден как под.
</b></details>

<details>
<summary>Выведите поды всех пространств имён.</summary><br><b>

`k get po -A`

Полная форма: `kubectl get pods --all-namespaces`.
</b></details>

<details>
<summary>Напишите YAML пода с двумя контейнерами и создайте под из файла. Образы выберите самостоятельно.</summary><br><b>

```
cat > pod.yaml <<EOL
apiVersion: v1
kind: Pod
metadata:
  name: test
spec:
  containers:
  - image: alpine
    name: alpine
  - image: nginx-unprivileged
    name: nginx-unprivileged
EOL

k create -f pod.yaml
```

Необязательно помнить весь YAML наизусть: основу можно получить командой `kubectl run some-pod --image=redis -o yaml --dry-run=client > pod.yaml`. А длинные команды лучше освоить практикой ;)
</b></details>

<details>
<summary>С помощью kubectl создайте YAML пода, не запуская сам под. Используйте любой образ.</summary><br><b>

`k run some-pod -o yaml --image nginx-unprivileged --dry-run=client > pod.yaml`
</b></details>

<details>
<summary>Как проверить корректность манифеста?</summary><br><b>

Параметр dry-run позволяет проверить запрос без создания ресурса. Для серверной проверки используйте:

`k create -f YAML_FILE --dry-run=server`

В исходнике приведён старый вариант `--dry-run` без значения.
</b></details>

<details>
<summary>Как узнать образ, используемый подом?</summary><br><b>

`k describe po <POD_NAME> | grep -i image`
</b></details>

<details>
<summary>Как проверить количество контейнеров в поде?</summary><br><b>

Выполните `k get po POD_NAME` и посмотрите столбец READY: он показывает число готовых контейнеров и их общее число.

Подробности: `k describe po POD_NAME`.
</b></details>

<details>
<summary>Запустите под remo с последним образом redis и меткой year=2017.</summary><br><b>

`k run remo --image=redis:latest -l year=2017`
</b></details>

<details>
<summary>Выведите поды вместе с метками.</summary><br><b>

`k get po --show-labels`
</b></details>

<details>
<summary>Удалите под nm.</summary><br><b>

`k delete po nm`
</b></details>

<details>
<summary>Выведите все поды с меткой env=prod.</summary><br><b>

`k get po -l env=prod`

Количество: `k get po -l env=prod --no-headers | wc -l`.
</b></details>

<details>
<summary>Создайте статический под из образа python, выполняющий sleep 2017.</summary><br><b>

Перейдите в каталог статических манифестов kubelet: `cd /etc/kubernetes/manifests`. Проверьте путь в конфигурации kubelet.

Создайте в нём манифест:

`k run some-pod --image=python --restart=Never --dry-run=client -o yaml --command -- sleep 2017 > static-pod.yaml`

Параметры генерации должны стоять до `--`, отделяющего команду контейнера; порядок из исходника исправлен.
</b></details>

<details>
<summary>Как удалить статический под?</summary><br><b>

Найдите каталог по параметру staticPodPath в конфигурации kubelet.

Удалите из него соответствующий манифест: `rm <STATIC_POD_PATH>/<POD_DEFINITION_FILE>`.
</b></details>

<a id="troubleshooting-pods"></a>
### Поиск неисправностей подов

<details>
<summary>Под показывает CrashLoopBackOff. Что это значит и как найти причину?</summary><br><b>

Контейнер повторно завершается с ошибкой, а kubelet увеличивает задержку между попытками запуска.

Возможные причины: неверная конфигурация, опечатки, неподдерживаемые значения или недоступность зависимости приложения. Проблемы планирования узла и монтирования тома могут приводить к другим состояниям, поэтому их нужно различать.

1. Выполните `kubectl describe pod POD_NAME`. Посмотрите State и Last State: там могут быть причина и код предыдущего завершения.
2. Выполните `kubectl logs mypod`; для нужного контейнера добавьте `-c CONTAINER_NAME`. Для предыдущего экземпляра контейнера полезен `--previous`.
3. Проверьте `kubectl get events`.
</b></details>

<details>
<summary>Что означает ImagePullBackOff?</summary><br><b>

Не удаётся скачать образ. Возможно, имя указано неверно или образ отсутствует в реестре. Возможны также проблемы сети и авторизации.

Посмотрите `kubectl describe po POD_NAME`.
</b></details>

<details>
<summary>Как узнать, на каком узле работает под?</summary><br><b>

`k get po POD_NAME -o wide`
</b></details>

<details>
<summary>Выполните kubectl run ohno --image=sheris. Удалось ли запустить под? Исправьте проблему без удаления пода, используя любой подходящий образ.</summary><br><b>

В исходном примере образ sheris недоступен.

Выполните `kubectl edit pod ohno` и замените `image: sheris` на `image: redis` либо другой существующий образ.
</b></details>

<details>
<summary>Под остаётся в Pending. В чём может быть причина?</summary><br><b>

Одна из причин — неработающий планировщик, который должен назначить под узлу. Проверьте `kubectl get po -A | grep scheduler` или пространство kube-system.
</b></details>

<details>
<summary>Как посмотреть журналы контейнера в поде?</summary><br><b>

`k logs POD_NAME`
</b></details>

<details>
<summary>В some-pod два контейнера. Что произойдёт при kubectl logs some-pod?</summary><br><b>

Чтобы однозначно выбрать контейнер, используйте `kubectl logs POD_NAME -c CONTAINER_NAME`. Поведение без `-c` зависит от наличия настройки контейнера по умолчанию и версии клиента; утверждение исходника об обязательной ошибке слишком категорично.
</b></details>

<a id="namespaces"></a>
## Пространства имён

<details>
<summary>Выведите все пространства имён.</summary><br><b>

`k get ns`
</b></details>

<details>
<summary>Создайте пространство имён alle.</summary><br><b>

`k create ns alle`
</b></details>

<details>
<summary>Подсчитайте пространства имён.</summary><br><b>

`k get ns --no-headers | wc -l`
</b></details>

<details>
<summary>Проверьте количество подов в пространстве dev.</summary><br><b>

`k get po -n dev`

Для численного результата: `k get po -n dev --no-headers | wc -l`.
</b></details>

<details>
<summary>Создайте под kartos в пространстве dev из образа redis.</summary><br><b>

Если пространства нет: `k create ns dev`.

`k run kartos --image=redis -n dev`

В исходном решении имя kratos не совпадало с условием; здесь использовано kartos.
</b></details>

<details>
<summary>Как найти пространство имён пода atreus?</summary><br><b>

`k get po -A | grep atreus`
</b></details>

<a id="nodes"></a>
## Узлы

<details>
<summary>Выведите все узлы кластера.</summary><br><b>

`kubectl get nodes`

После `alias k=kubectl` можно использовать `k get no`.
</b></details>

<details>
<summary>Сохраните список узлов в формате JSON в some_nodes.json.</summary><br><b>

`k get nodes -o json > some_nodes.json`
</b></details>

<details>
<summary>Проверьте метки одного из узлов.</summary><br><b>

`k get no minikube --show-labels`
</b></details>

<a id="services"></a>
## Сервисы

<details>
<summary>Проверьте количество сервисов текущего пространства имён.</summary><br><b>

`k get svc`
</b></details>

<details>
<summary>Создайте внутренний сервис sevi для доступа к приложению web на порту 1991.</summary><br><b>

`kubectl expose pod web --port=1991 --name=sevi`
</b></details>

<details>
<summary>По какому имени обратиться к app-service внутри того же пространства имён?</summary><br><b>

`app-service`
</b></details>

<details>
<summary>Как узнать targetPort сервиса?</summary><br><b>

`k describe svc <SERVICE_NAME>`
</b></details>

<details>
<summary>Как посмотреть конечные точки сервиса?</summary><br><b>

`k describe svc <SERVICE_NAME>`
</b></details>

<details>
<summary>По какому имени обратиться к app-service в другом пространстве имён dev?</summary><br><b>

`app-service.dev.svc.cluster.local`
</b></details>

<details>
<summary>Создайте сервис для подов развёртывания со следующими параметрами:

* Deployment: jabulik.
* Целевой порт: 8080.
* Тип сервиса: NodePort.
* Селектор: jabulik-app.
* Порт сервиса: 8080.
</summary><br><b>

`kubectl expose deployment jabulik --name=jabulik-service --target-port=8080 --type=NodePort --port=8080 --dry-run=client -o yaml > svc.yaml`

Откройте `vi svc.yaml` и проверьте, что селектор соответствует меткам подов jabulik-app.

`k apply -f svc.yaml`

Опечатка перенаправления `->` из оригинала исправлена на `>`.
</b></details>

<a id="replicasets"></a>
## Наборы реплик

<details>
<summary>Как посмотреть ReplicaSet текущего пространства имён?</summary><br><b>

`k get rs`
</b></details>

<details>
<summary>ReplicaSet должен поддерживать три пода. Вы удалили один. Что произойдёт?</summary><br><b>

Контроллер создаст замену, чтобы снова получить три пода. Достижение рабочего состояния зависит от доступности ресурсов и успешного запуска.
</b></details>

<details>
<summary>Как узнать образ контейнера в ReplicaSet repli?</summary><br><b>

`k describe rs repli | grep -i image`
</b></details>

<details>
<summary>Как проверить состояние подов ReplicaSet repli?</summary><br><b>

`k describe rs repli | grep -i "Pods Status"`

Учтите, что Running и Ready — разные признаки; число готовых реплик также доступно в `k get rs repli`.
</b></details>

<details>
<summary>Как удалить ReplicaSet rori?</summary><br><b>

`k delete rs rori`
</b></details>

<details>
<summary>Как изменить образ в ReplicaSet rori?</summary><br><b>

`k edit rs rori`

В оригинале опечатка edis. Изменение шаблона ReplicaSet само по себе не обновляет уже существующие поды.
</b></details>

<details>
<summary>Увеличьте число реплик rori с двух до пяти.</summary><br><b>

`k scale rs rori --replicas=5`
</b></details>

<details>
<summary>Уменьшите число реплик rori с пяти до одной.</summary><br><b>

`k scale rs rori --replicas=1`
</b></details>

<a id="troubleshooting-replicasets"></a>
### Поиск неисправностей ReplicaSet

<details>
<summary>Исправьте определение ReplicaSet.

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

Значение kind должно быть ReplicaSet, а не ReplicaCet :)
</b></details>

<details>
<summary>Исправьте определение ReplicaSet.

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

Селектор не совпадает с меткой: cache и cachy. Замените cachy на cache.
</b></details>

<a id="deployments"></a>
## Развёртывания

<details>
<summary>Как вывести Deployment текущего пространства имён?</summary><br><b>

`k get deploy`
</b></details>

<details>
<summary>Как узнать образ, используемый Deployment?</summary><br><b>

`k describe deploy <DEPLOYMENT_NAME> | grep image`
</b></details>

<details>
<summary>Создайте манифест Deployment dep с тремя репликами из образа redis.</summary><br><b>

`k create deploy dep -o yaml --image=redis --dry-run=client --replicas 3 > deployment.yaml`
</b></details>

<details>
<summary>Удалите Deployment depdep.</summary><br><b>

`k delete deploy depdep`
</b></details>

<details>
<summary>Создайте Deployment pluck из образа redis с пятью репликами.</summary><br><b>

`kubectl create deployment pluck --image=redis --replicas=5`
</b></details>

<details>
<summary>Создайте Deployment:

* Имя blufer.
* Образ python.
* Три реплики.
* Поды должны размещаться на узле с соответствующей меткой blufer.
</summary><br><b>

`kubectl create deployment blufer --image=python --replicas=3 -o yaml --dry-run=client > deployment.yaml`

Откройте `vi deployment.yaml` и добавьте раздел:

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

<a id="troubleshooting-deployments"></a>
### Поиск неисправностей Deployment

<details>
<summary>Исправьте манифест Deployment.

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
<summary>Исправьте манифест Deployment.

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

Селектор не совпадает с меткой: dep и depdep. Замените depdep на dep.
</b></details>

<a id="scheduler"></a>
## Планировщик

<details>
<summary>Как назначить под узлу node1?</summary><br><b>

`k run some-pod --image=redis -o yaml --dry-run=client > pod.yaml`

В исходнике опечатка в имени образа redix. Откройте `vi pod.yaml` и добавьте:

```
spec:
  nodeName: node1
```

`k apply -f pod.yaml`

Если node1 отсутствует, под останется в Pending.
</b></details>

<a id="node-affinity"></a>
### Привязка к узлам

<details>
<summary>С помощью node affinity разрешите размещение пода на узлах с меткой region, равной asia или emea.</summary><br><b>

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
<summary>С помощью node affinity запретите размещение пода на узлах с region=neverland.</summary><br><b>

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

<a id="labels-and-selectors"></a>
## Метки и селекторы

<details>
<summary>Как вывести поды с меткой app=web?</summary><br><b>

`k get po -l app=web`
</b></details>

<details>
<summary>Как вывести объекты с меткой env=staging?</summary><br><b>

`k get all -l env=staging`

Здесь all — группа распространённых типов ресурсов, а не буквально все существующие типы API.
</b></details>

<details>
<summary>Как вывести Deployment с метками env=prod и type=web?</summary><br><b>

`k get deploy -l env=prod,type=web`
</b></details>

<a id="node-selector"></a>
### Селектор узла

<details>
<summary>Назначьте одному из узлов метку hw=max.</summary><br><b>

`kubectl label nodes some-node hw=max`
</b></details>

<details>
<summary>Создайте под some-pod из образа redis с селектором узла hw=max.</summary><br><b>

```
kubectl run some-pod --image=redis --dry-run=client -o yaml > pod.yaml

vi pod.yaml

spec:
  nodeSelector:
    hw: max

kubectl apply -f pod.yaml
```
</b></details>

<details>
<summary>Почему возможностей nodeSelector бывает недостаточно?</summary><br><b>

Предположим, подходит значение hw=max или hw=min. Простой nodeSelector не выражает такой выбор. Для более гибких условий используйте node affinity.
</b></details>

<a id="taints"></a>
## Ограничения taint

<details>
<summary>Проверьте taint узла master.</summary><br><b>

`k describe no master | grep -i taints`
</b></details>

<details>
<summary>Добавьте узлу taint с ключом app, значением web и эффектом NoSchedule. Проверьте результат.</summary><br><b>

`k taint node minikube app=web:NoSchedule`

`k describe no minikube | grep -i taints`
</b></details>

<details>
<summary>Вы назначили единственному узлу taint командой k taint node minikube app=web:NoSchedule и запустили kubectl run some-pod --image=redis. Что произойдёт?</summary><br><b>

Под без подходящего toleration останется в Pending, поскольку единственный узел имеет это ограничение.
</b></details>

<details>
<summary>Как исправить Pending пода some-pod, если единственный узел имеет app=web:NoSchedule?</summary><br><b>

Откройте `kubectl edit po some-pod` и добавьте:

```
  - effect: NoSchedule
    key: app
    operator: Equal
    value: web
```

Сохраните изменения. При отсутствии других препятствий под сможет запуститься.
</b></details>

<details>
<summary>Удалите существующий taint с узла.</summary><br><b>

`k taint node minikube app=web:NoSchedule-`
</b></details>

<a id="resources-limits"></a>
## Ограничения ресурсов

<details>
<summary>Проверьте наличие лимитов ресурсов у пода.</summary><br><b>

`kubectl describe po <POD_NAME> | grep -i limits`
</b></details>

<details>
<summary>Запустите под yay из образа python с запросом 64Mi памяти и 250m CPU.</summary><br><b>

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
<summary>Запустите yay2 из образа python: requests — 64Mi памяти и 250m CPU, limits — 128Mi памяти и 500m CPU.</summary><br><b>

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
## Мониторинг

<details>
<summary>Разверните metrics-server.</summary><br><b>

`kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml`
</b></details>

<details>
<summary>С помощью metrics-server посмотрите потребление ресурсов:

* Узлами кластера.
* Подами.
</summary><br><b>

* Узлы: `kubectl top nodes`.
* Поды: `kubectl top pods`.
</b></details>

<a id="scheduler-1"></a>
## Планировщик

<details>
<summary>Можно ли развернуть несколько планировщиков?</summary><br><b>

Да. Дополнительный планировщик можно запустить отдельным подом с командой, подобной следующей:

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
<summary>Как при наличии нескольких планировщиков определить, какой назначил под узлу?</summary><br><b>

Посмотрите события с помощью `kubectl get events`.
</b></details>

<details>
<summary>Как поручить размещение нового пода пользовательскому планировщику?</summary><br><b>

Добавьте в spec пода:

```
spec:
  schedulerName: some-custom-scheduler
```
</b></details>
