<a id="argocd-helm-app"></a>
# Приложение Argo CD на основе Helm

<a id="requirements"></a>
## Требования

1. Работающий кластер Kubernetes.
2. Argo CD, установленный в этом кластере.
3. Репозиторий с Helm-чартом.

<a id="objectives"></a>
## Задание

1. Создайте приложение в Argo CD, указав репозиторий своего Helm-чарта.

<a id="solution"></a>
## Решение

```
argocd app create some-app \
--project default \
--repo https://repo-with-helm-chart
--path "./helm" \
--sync-policy auto \
--dest-namespace default \
--dest-server https://kubernetes.cluster
```
