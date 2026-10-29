<a id="sync-app---git"></a>
# Синхронизация приложения с Git

<a id="requirements"></a>
## Требования

1. Репозиторий с манифестами Kubernetes.
2. Работающий кластер Kubernetes с установленным Argo CD.

<a id="objectives"></a>
## Задание

1. Через CLI или веб-интерфейс создайте приложение:
   1. Имя: app-demo.
   2. Проект: project-demo.
   3. Пространство имён Kubernetes: default.
2. Синхронизируйте приложение.
3. Проверьте его развёртывание командой `kubectl get deploy` в пространстве имён `default`.
4. Измените один из манифестов в репозитории, например тег образа в Deployment.
5. Вернитесь в Argo CD и проверьте состояние приложения.
6. Синхронизируйте состояние приложения.

<a id="solution"></a>
## Решение

[Посмотреть решение](solution.md).

<a id="ui"></a>
### Веб-интерфейс

1. Нажмите **New App**:
   1. Имя: `app-demo`.
   2. Проект: `project-demo`.
   3. В источнике укажите URL репозитория GitHub с манифестами и путь к приложению.
   4. В назначении укажите адрес кластера и пространство имён `default`.
   5. Нажмите **Create**.
2. Откройте приложение, нажмите **Sync**, затем **Synchronize**.
3. Измените манифесты в Git и выполните:
   1. `git add .`
   2. `git commit -a`
   3. `git push origin <BRANCH_NAME>`
4. Вернитесь в интерфейс Argo CD:
   1. Состояние должно стать out-of-sync. При необходимости нажмите **Refresh**.
   2. Через **App diff** можно посмотреть изменения, вызвавшие рассинхронизацию.
5. Нажмите **Sync → Synchronize**.

<a id="cli"></a>
### CLI

```
argocd app create app-demo \
--project project-demo \
--repo https://fake.repo.address \
--path ./some_app_path \
--dest-namespace default \
--dest-server my.kubernetes.cluster

# In the Git repo
cd <git repo>
vi <k8s manifest>
git add .
git commit -a
git push origin <BRANCH_NAME>

# Check app state
argocd app get app-demo

# Sync app state
argocd app sync app-demo
argocd app wait app-demo
```
