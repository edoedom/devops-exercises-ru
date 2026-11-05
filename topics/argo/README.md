<a id="argo"></a>
# Argo

<!-- {% raw %} -->

- [Argo](#argo)
  - [Упражнения по Argo CD](#argocd-exercises)
    - [Основы Argo CD](#argocd-101)
    - [Секреты Argo CD](#argocd-secrets)
    - [Argo CD и Helm](#argocd-helm)
    - [Argo Rollouts](#argo-rollouts)
  - [Вопросы по Argo CD](#argocd-questions)
    - [Основы Argo CD](#argocd-101-1)
    - [Практические основы Argo CD](#practical-argocd-101)
      - [CLI](#cli)
    - [Настройка Argo CD](#argocd-configuration)
    - [Продвинутые вопросы по Argo CD](#advanced-argocd)
    - [Работоспособность приложений](#argocd-application-health)
    - [Синхронизация](#argocd-syncs)
    - [Argo CD и Helm](#argocd-and-helm)
  - [Вопросы по Argo Rollouts](#argo-rollouts-questions)
    - [Основы Argo Rollouts](#argo-rollouts-101)
    - [Продвинутые вопросы по Rollouts](#argo-advanced-rollouts)
    - [Команды Argo Rollouts](#argo-rollouts-commands)

<a id="argocd-exercises"></a>
## Упражнения по Argo CD

<a id="argocd-101"></a>
### Основы Argo CD

|Название|Тема|Цель и инструкции|Решение|Комментарии|
|--------|--------|------|----|----|
| Создание приложения | Приложения | [Задание](exercises/app_creation/exercise.md) | [Решение](exercises/app_creation/solution.md)
| Синхронизация приложения — Git | Синхронизация | [Задание](exercises/sync_app_git/exercise.md) | [Решение](exercises/sync_app_git/solution.md)
| Синхронизация приложения — кластер | Синхронизация | [Задание](exercises/sync_app_cluster/exercise.md) | [Решение](exercises/sync_app_cluster/solution.md)

<a id="argocd-secrets"></a>
### Секреты Argo CD

|Название|Тема|Цель и инструкции|Решение|Комментарии|
|--------|--------|------|----|----|
| Основы работы с секретами | Секреты | [Задание](exercises/secrets_101/exercise.md) | [Решение](exercises/secrets_101/solution.md)

<a id="argocd-helm"></a>
### Argo CD и Helm

|Название|Тема|Цель и инструкции|Решение|Комментарии|
|--------|--------|------|----|----|
| Приложение Helm в Argo CD | Секреты | [Задание](exercises/argocd_helm_app/exercise.md) | [Решение](exercises/argocd_helm_app/solution.md)

<a id="argo-rollouts"></a>
### Argo Rollouts

|Название|Тема|Цель и инструкции|Решение|Комментарии|
|--------|--------|------|----|----|
| Сине-зелёное развёртывание | Rollouts | [Задание](exercises/blue_green_rollout/exercise.md) | [Решение](exercises/blue_green_rollout/solution.md)
| Канареечное развёртывание | Rollouts | [Задание](exercises/canary_rollout/exercise.md) | [Решение](exercises/canary_rollout/solution.md)

<a id="argocd-questions"></a>
## Вопросы по Argo CD

<a id="argocd-101-1"></a>
### Основы Argo CD

<details>
<summary>Что такое Argo CD?</summary><br><b>

[Argo CD](https://argo-cd.readthedocs.io/en/stable): декларативный инструмент непрерывной доставки для Kubernetes, использующий GitOps.

Обоснование такого подхода: определения приложений, настройки и среды должны описываться декларативно и храниться под контролем версий. Развёртывание и управление жизненным циклом должны быть автоматизированными, доступными для аудита и понятными.
</b></details>

<details>
<summary>До Argo CD существовало множество систем CI/CD: Jenkins, TeamCity, CircleCI и другие. Что нового даёт Argo CD?</summary><br><b>

Argo CD отвечает за CD; система CI по-прежнему нужна. Он работает в Kubernetes, интегрирован в его экосистему и создан специально для этой платформы.

Сравним с Jenkins. Для развёртывания через Jenkins обычно нужно установить инструменты Kubernetes и настроить доступ, например для kubectl. Argo CD уже содержит механизмы взаимодействия с Kubernetes; после установки настраиваются его разрешения и подключения.

В Jenkins учётные данные обычно подключаются к конкретным конвейерам, даже если определены централизованно. В Argo CD доступ к управляемым кластерам и приложениям организован как часть его конфигурации.

Для проверки состояния развёрнутого приложения в Jenkins обычно добавляют отдельные шаги конвейера. Argo CD постоянно сравнивает желаемое и фактическое состояние, показывая ресурсы и расхождения. Для этого ему не обязательно работать в том же пространстве имён или даже в том же кластере, что приложение.

Возврат к предыдущей конфигурации упрощается благодаря Git: можно отменить изменение в репозитории, после чего Argo CD синхронизирует кластер. Сам принцип хранения версий конфигурации применим и с Jenkins.
</b></details>

<details>
<summary>Приведите пример процесса разработки с Argo CD.</summary><br><b>

1. Разработчик отправляет изменение в репозиторий приложения.
2. Запускается конвейер Jenkins с проверками CI.
3. После успешных проверок из нового кода собирается образ.
4. Образ отправляется в реестр.
5. В отдельном репозитории конфигурации обновляются манифесты Kubernetes.
6. Argo CD замечает изменение в этом репозитории и применяет его согласно политике синхронизации.
</b></details>

<details>
<summary>Верно ли, что Argo CD поддерживает только YAML Kubernetes, но не Helm и Kustomize?</summary><br><b>

Нет. Поддерживаются обычные YAML-манифесты Kubernetes, чарты Helm и Kustomize.
</b></details>

<details>
<summary>Что означает GitOps-репозиторий в контексте Argo CD?</summary><br><b>

Репозиторий с конфигурацией приложений, обновляемый процессами CI/CD или инженерами DevOps и SRE. Argo CD следит за ним и использует как источник желаемого состояния.
</b></details>

<details>
<summary>Каковы преимущества GitOps?</summary><br><b>

* Конфигурация хранится в одном месте в виде кода: её можно просматривать, изменять и воспроизводить.
* Все работают через общий процесс изменений, поэтому больше участников проверяют конфигурацию.
* Настройки можно повторно использовать для разработки и тестирования без ручного воспроизведения команд.
* Есть единый источник истины. При включённом самовосстановлении ручные отклонения в кластере приводятся к состоянию из Git.
</b></details>

<details>
<summary>Инженер Сорина вручную изменила кластер вопреки конфигурации в отслеживаемом репозитории. Что произойдёт?</summary><br><b>

Argo CD обнаружит расхождение. Если включены автоматическая синхронизация и self-heal, он восстановит состояние из Git, перезаписав ручные изменения. Без соответствующих настроек автоматическое исправление не гарантируется.
</b></details>

<details>
<summary>Инженер Нейт спрашивает, можно ли не отменять автоматически ручные изменения кластера. Что вы ответите?</summary><br><b>

Да. Можно отключить автоматическое исправление таких расхождений и вместо него настроить уведомления.
</b></details>

<details>
<summary>Как Argo CD упрощает аварийное восстановление кластера?</summary><br><b>

Представьте, что облачный кластер вышел из строя. Если его конфигурация хранится в GitOps-репозитории, можно подготовить новый кластер, подключить его к Argo CD и применить ту же конфигурацию.

Так восстанавливается описанное в Git состояние ресурсов. Данные приложений и другие внешние зависимости требуют отдельного восстановления.
</b></details>

<details>
<summary>Элла считает преимуществом Argo CD то, что он расширяет Kubernetes. Сара возражает: Jenkins тоже можно установить в кластер. Кто прав?</summary><br><b>

Элла указывает на более глубокую интеграцию, чем просто размещение приложения в кластере. Argo CD использует пользовательские ресурсы и контроллеры Kubernetes для наблюдения и согласования состояния; данные этих ресурсов хранятся средствами Kubernetes в etcd.
</b></details>

<details>
<summary>Как называется основной ресурс Argo CD?</summary><br><b>

Application.
</b></details>

<details>
<summary>Что такое Application в Argo CD?</summary><br><b>

Пользовательский ресурс, описывающий развёртывание приложения и синхронизацию его ресурсов с кластером Kubernetes. Его тип определяется CRD.
</b></details>

<details>
<summary>Как Argo CD упрощает управление доступом к изменениям кластера?</summary><br><b>

Можно управлять правами на отправку кода, ревью и слияние в Git для людей и сервисов, а применение изменений поручить Argo CD. Это снижает необходимость выдавать каждому прямой доступ к кластеру.

При этом самому Argo CD всё равно нужны корректно настроенные разрешения Kubernetes и собственные правила доступа. Утверждение оригинала о полном отсутствии необходимости в ClusterRole слишком категорично.
</b></details>

<a id="practical-argocd-101"></a>
### Практические основы Argo CD

<details>
<summary>Объясните назначение раздела YAML ресурса Application.

```YAML
source:
  repoURL: https://github.com/bregman-arie/devops-exercises
  targetRevision: HEAD
  path: main
```
</summary><br><b>

Он определяет репозиторий Git, из которого нужно брать желаемое состояние.
</b></details>

<details>
<summary>Объясните назначение раздела YAML ресурса Application.

```YAML
destination:
  server: http://some.kubernetes.cluster.svc
  namespace: devopsExercises
```
</summary><br><b>

Он определяет кластер Kubernetes, в который нужно синхронизировать приложение из отслеживаемого репозитория.
</b></details>

<details>
<summary>Какой ресурс использовать для логического объединения нескольких приложений?</summary><br><b>

AppProject. В оригинале опечатка: AddProject.
</b></details>

<details>
<summary>Верно ли, что период синхронизации Argo CD равен трём часам?</summary><br><b>

Нет. В исходнике указан интервал проверки три минуты, а не три часа. Фактическое значение зависит от версии и настроек.
</b></details>

<details>
<summary>Что Argo CD делает при периодической проверке состояния?</summary><br><b>

1. Получает приложения для проверки и их настройки синхронизации.
2. Получает состояние соответствующих репозиториев Git.
3. Сравнивает желаемое состояние с состоянием кластера.
   * При расхождении приложение помечается OutOfSync; дальнейшие действия зависят от настроек.
   * При совпадении — Synced.
</b></details>

<details>
<summary>Вы настроили новое приложение в пространстве имён yay, но kubectl get ns yay сообщает, что такого пространства нет. Почему?</summary><br><b>

Само указание отсутствующего пространства имён не создаёт его. Для этого нужно явно включить Auto-create namespace либо управлять ресурсом Namespace.

Можно выполнить `kubectl create namespace NAMESPACE_NAME`, но для GitOps предпочтительно хранить нужную конфигурацию в Git.
</b></details>

<a id="cli"></a>
#### CLI

<details>
<summary>Создайте приложение со следующими параметрами:

* Имя: some-app.
* Репозиторий: https://fake.repo.address.
* Путь: ./app_path.
* Пространство имён: default.
* Кластер: my.kubernetes.cluster.
</summary><br><b>

```
argocd app create some-app \
--project  \
--repo https://fake.repo.address \
--path ./app_path \
--dest-namespace default \
--dest-server my.kubernetes.cluster
```
</b></details>

<details>
<summary>Выведите все приложения Argo CD.</summary><br><b>

`argocd app list`
</b></details>

<details>
<summary>Выведите подробные сведения о приложении some-app.</summary><br><b>

`argocd app get some-app`
</b></details>

<details>
<summary>Как добавить внешний кластер под управление Argo CD?</summary><br><b>

Сначала выберите контекст из `kubectl config get-contexts`, затем выполните `argocd cluster add CONTEXT_NAME`. Аргумент — имя контекста kubeconfig, а не произвольный URL API server. Проверьте целевой кластер и требуемые права: команда может создать ServiceAccount и RBAC для управления кластером.

[Команда cluster add](https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd_cluster_add/).
</b></details>

<details>
<summary>Как вывести все управляемые кластеры?</summary><br><b>

`argocd cluster list`
</b></details>

<a id="argocd-configuration"></a>
### Настройка Argo CD

<details>
<summary>Можно ли изменить стандартный интервал проверки состояния Argo CD?</summary><br><b>

Да. В ConfigMap argocd-cm добавьте:

```
data:
  timeout.reconciliation: 300s
```

Значение задаёт нужную продолжительность, в данном случае в секундах.
</b></details>

<details>
<summary>Что произойдёт при <code>timeout.reconciliation: 0s</code>?</summary><br><b>

Отключится периодический опрос репозитория по этому таймеру. Это не означает отключения всех способов синхронизации, как можно понять из исходного ответа.
</b></details>

<a id="advanced-argocd"></a>
### Продвинутые вопросы по Argo CD

<details>
<summary>Что такое шаблон App of Apps?</summary><br><b>

Подход сообщества Argo для управления несколькими приложениями: корневое приложение управляет ресурсами дочерних Application.

Вместо отдельного создания каждого приложения корневое приложение указывает на репозиторий с их описаниями.
</b></details>

<details>
<summary>Приведите сценарии использования App of Apps.</summary><br><b>

* Подготовка кластера: установка нескольких приложений для начальной настройки Kubernetes.
* Несколько сред: развёртывание вариантов одного приложения с небольшими отличиями, например для тестирования разных возможностей.
* Несколько кластеров: размещение одного приложения в разных кластерах, подключённых к Argo CD.
</b></details>

<details>
<summary>Верно ли, что Argo CD нужно установить в каждый управляемый кластер?</summary><br><b>

Нет. Один экземпляр Argo CD может управлять внешними кластерами, в которых он не установлен.
</b></details>

<details>
<summary>Есть кластеры dev, staging и prod. Любое изменение GitOps-репозитория обновляет все три. В чём проблема и как её решить?</summary><br><b>

Обычно не следует одновременно обновлять тестовые среды и рабочую среду: изменения должны пройти проверку.

Варианты:

1. Разделить среды по веткам: сначала development, после тестирования staging, затем production.
2. Использовать overlays и Kustomize, чтобы конвейер CI управлял тем, в какую среду попадут изменения.
</b></details>

<a id="argocd-application-health"></a>
### Работоспособность приложений Argo CD

<details>
<summary>Какие состояния работоспособности приложения существуют?</summary><br><b>

* Healthy — ресурс работоспособен.
* Missing — ресурс отсутствует в кластере.
* Suspended — работа ресурса приостановлена.
* Progressing — ресурс ещё не достиг рабочего состояния, но движется или может перейти к нему.
* Degraded — ресурс работает некорректно.
* Unknown — состояние неизвестно.
</b></details>

<details>
<summary>Верно ли, что Deployment считается работоспособным, если поды запущены?</summary><br><b>

Не совсем. Для Deployment, StatefulSet, ReplicaSet и DaemonSet проверяется достижение ожидаемого состояния, включая нужное количество готовых реплик; одного факта запуска подов недостаточно.
</b></details>

<details>
<summary>Верно ли, что Ingress считается работоспособным, если список status.loadBalancer.ingress содержит хотя бы одно значение?</summary><br><b>

Да, это описанная в исходнике стандартная проверка.
</b></details>

<details>
<summary>Как определяется работоспособность пользовательских ресурсов Kubernetes?</summary><br><b>

Проверки можно описывать скриптами Lua.

Примеры: https://github.com/argoproj/argo-cd/tree/master/resource_customizations
</b></details>

<a id="argocd-syncs"></a>
### Синхронизация Argo CD

<details>
<summary>Чем отличается ручная синхронизация от автоматической?</summary><br><b>

При автоматической синхронизации Argo CD применяет обнаруженные изменения Git, приводя фактическое состояние к желаемому.

При ручной синхронизации он показывает расхождение, но применение изменений нужно запустить отдельно.
</b></details>

<details>
<summary>Что такое auto-pruning?</summary><br><b>

При включённой автоматической очистке Argo CD удаляет управляемые ресурсы, исчезнувшие из желаемого состояния репозитория.

Без неё удаление описания из Git само по себе не приводит к автоматическому удалению ресурса.
</b></details>

<details>
<summary>Что такое self-heal в Argo CD?</summary><br><b>

Восстановление желаемого состояния кластера после ручных изменений, создавших расхождение с конфигурацией Git.
</b></details>

<a id="argocd-and-helm"></a>
### Argo CD и Helm

<details>
<summary>Как Argo CD поддерживает Helm?</summary><br><b>

Он может использовать упакованный чарт Helm как источник манифестов и отслеживать подходящие версии согласно конфигурации приложения.
</b></details>

<details>
<summary>Верно ли, что приложение из чарта Helm под управлением Argo CD не является обычным релизом Helm?</summary><br><b>

Да. Argo CD использует Helm для генерации манифестов, а жизненным циклом управляет самостоятельно. Поэтому `helm ls` не покажет его как созданный Helm релиз: соответствующие метаданные релиза не создаются.
</b></details>

<a id="argo-rollouts-questions"></a>
## Вопросы по Argo Rollouts

<a id="argo-rollouts-101"></a>
### Основы Argo Rollouts

<details>
<summary>Что такое Argo Rollouts?</summary><br><b>

Контроллер Kubernetes для развёртывания приложений по разным стратегиям, включая сине-зелёную и канареечную.

Также поддерживает A/B-тесты, автоматический откат и анализ метрик.
</b></details>

<details>
<summary>Что происходит при развёртывании новой версии через Argo Rollouts?</summary><br><b>

* Создаётся новый ReplicaSet для новой версии приложения.
* Старая версия продолжает работать согласно стратегии развёртывания.
* В исходнике также указано состояние OutOfSync в Argo CD; оно возникает при расхождении фактической конфигурации с Git и не является обязательным следствием любого rollout.
</b></details>

<details>
<summary>Верно ли, что для Argo Rollouts обязательно нужен Argo CD?</summary><br><b>

Нет. Они хорошо сочетаются, но могут использоваться независимо.
</b></details>

<a id="argo-advanced-rollouts"></a>
### Продвинутые вопросы по Rollouts

<details>
<summary>После каждого выпуска Скотт вручную запускает дымовые тесты, наблюдает за развёртыванием и при проблемах делает откат. Что можно улучшить?</summary><br><b>

Автоматизировать решение об откате. Argo Rollouts поддерживает источники метрик, например Datadog и New Relic. По их данным можно задать условия успешности и неуспешности развёртывания.
</b></details>

<details>
<summary>Что означает Analysis в Argo Rollouts?</summary><br><b>

Механизм анализа, выполняемого вместе с развёртыванием: он задаёт метрики, условия и пороговые значения для решения о продолжении или прекращении выпуска. Конфигурация описывается шаблоном анализа, а выполнение — отдельным ресурсом.
</b></details>

<details>
<summary>Объясните конфигурацию.

```yaml
apiVersion: argoproj.io/v1alpha1
kind: AnalysisTemplate
metadata:
  name: success-rate
spec:
  args:
  - name: service-name
  metrics:
  - name: success-rate
    interval: 4m
    count: 3
    successCondition: result[0] >= 0.90
    provider:
      prometheus:
        address: http:/some-prometheus-instance:80
        query: sum(response_status{app="{{args.service-name}}",role="canary",status=~"2.*"})/sum(response_status{app="{{args.service-name}}",role="canary"}
```
</summary><br><b>

Анализ получает метрику из Prometheus и сравнивает результат с порогом 0,90. При выполнении условия успеха развёртывание может продолжиться; при признании анализа неуспешным канареечное развёртывание прекращается согласно его настройкам. Точная обработка граничного значения определяется выражением в приведённом коде.
</b></details>

<a id="argo-rollouts-commands"></a>
### Команды Argo Rollouts

<details>
<summary>Как вывести список Rollout?</summary><br><b>

`kubectl argo rollouts list rollouts`
</b></details>

<details>
<summary>Как получить сведения о Rollout определённого приложения?</summary><br><b>

`kubectl argo rollouts get rollout SOME-APP`
</b></details>

<details>
<summary>Как проверить состояние Rollout?</summary><br><b>

`kubectl argo rollouts status SOME-APP`
</b></details>

<details>
<summary>Как развернуть новую версию с другим тегом образа?</summary><br><b>

`kubectl argo rollouts set image SOME-APP web-app=some/registry/and/image:v2.0`
</b></details>

<details>
<summary>Как вручную продвинуть новую версию приложения?</summary><br><b>

`kubectl argo rollouts promote SOME-APP`
</b></details>

<details>
<summary>Как наблюдать за развёртыванием?</summary><br><b>

`kubectl argo rollouts get rollout SOME-APP --watch`
</b></details>

<!-- {% endraw %} -->
