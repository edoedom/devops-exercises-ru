<a id="sync-app---cluster"></a>
# Синхронизация приложения с кластером

<a id="requirements"></a>
## Требования

1. Работающий кластер Kubernetes с установленным Argo CD.
2. Развёрнутое в кластере приложение, отслеживаемое Argo CD.

<a id="objectives"></a>
## Задание

1. Убедитесь, что Argo CD отслеживает приложение и его состояние синхронизировано.
2. Измените приложение командой `kubectl`. Например:
   1. Измените тег образа.
   2. Измените количество реплик.
   3. Можно даже удалить ресурс.
3. Проверьте состояние приложения в Argo CD.
4. Синхронизируйте состояние приложения.

<a id="solution"></a>
## Решение

<a id="ui"></a>
### Веб-интерфейс

1. Откройте приложение:
   1. Убедитесь, что оно синхронизировано и имеет состояние healthy.
2. Внесите изменение и проверьте ресурсы кластера:
   1. `kubectl scale deployment/<DEPLOYMENT_NAME> --replicas=0`
   2. `kubectl get replicasets`
3. Вернитесь в интерфейс и проверьте состояние:
   1. Если оно всё ещё синхронизировано, нажмите **Refresh**.
   2. Приложение должно перейти в состояние out-of-sync.
   3. Нажмите **Sync**, затем **Synchronize**.

> Команды исправлены: тип ресурса указан явно. При включённом auto-sync/self-heal Argo CD может автоматически вернуть реплики раньше ручной синхронизации; для этой части упражнения отключите self-heal в тестовом приложении.

<a id="cli"></a>
### CLI

```
# Check app state and verify it's in sync
argocd app get app-demo

# Run the following k8s commands (or any other commands that will change the state of your app)
kubectl scale deployment/<DEPLOYMENT_NAME> --replicas=0
kubectl get replicasets

# Check app state again
argocd app get app-demo

# Sync app state
argocd app sync app-demo
argocd app wait app-demo
```
