<a id="app-creation"></a>
# Создание приложения

<a id="requirements"></a>
## Требования

1. Репозиторий с манифестами Kubernetes.
2. Работающий кластер Kubernetes с установленным Argo CD.

<a id="objectives"></a>
## Задание

1. Через CLI или веб-интерфейс создайте приложение:
   1. Имя: app-demo.
   2. Проект: app-project.
   3. URL репозитория: адрес вашего репозитория с манифестами Kubernetes.
   4. Пространство имён: default.
2. Проверьте, что приложение создано.
3. Синхронизируйте приложение.
4. Убедитесь, что ресурсы Kubernetes созданы.
5. Удалите приложение.

<a id="solution"></a>
## Решение

<a id="ui"></a>
### Веб-интерфейс

1. Нажмите **New App**:
   1. Имя приложения: `app-demo`.
   2. Проект: `app-project`.
   3. В разделе источника укажите URL репозитория GitHub с манифестами Kubernetes и путь к приложению.
   4. В разделе назначения укажите адрес кластера Kubernetes и пространство имён `default`.
   5. Нажмите **Create**.
2. В карточке app-demo нажмите **Sync**, затем **Synchronize**.
3. Убедитесь, что ресурсы созданы: `kubectl get deployments`.
4. Удалите приложение.

<a id="cli"></a>
### CLI

```
argocd app create app-demo \
--project app-project \
--repo https://fake.repo.address \
--path ./some_app_path \
--dest-namespace default \
--dest-server my.kubernetes.cluster

# Check app state
argocd app list
argocd app get app-demo

# Sync app state
argocd app sync app-demo
argocd app wait app-demo

# Verify kubernetes resources were created
kubectl get deployments

# Delete the app
argocd app delete app-demo
```
