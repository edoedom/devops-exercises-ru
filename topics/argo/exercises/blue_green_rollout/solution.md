<a id="argo-rollouts---bluegreen"></a>
# Argo Rollouts: blue-green

<a id="requirements"></a>
## Требования

1. Работающий кластер Kubernetes.
2. CLI Argo Rollouts.
3. Развёрнутое приложение определённой версии.

<a id="objectives"></a>
## Задание

1. Установите контроллер Argo Rollouts.
2. Напишите и примените манифест Rollout со стратегией blue-green:
   1. Задайте три реплики.
   2. Отключите автоматическое продвижение новой версии.
3. Посмотрите список Rollout.
4. Разверните новую версию приложения любым способом.
   1. Проверьте состояние развёртывания.

<a id="solution"></a>
## Решение

Установка:

1. `kubectl create namespace argo-rollouts`
   1. `kubectl apply -n argo-rollouts -f https://github.com/argoproj/argo-rollouts/releases/latest/download/install.yaml`
2. Ресурс Rollout:

```
---
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
  name: some-app
spec:
  replicas: 3
  strategy:
    blueGreen:     
      autoPromotionEnabled: false
  selector:
    matchLabels:
      app: some-web-app
  template:
    metadata:
      labels:
        app: some-web-app
    spec:
      containers:
      - name: web-app
        image: some/registry/and/image:v1.0
        ports:
        - name: http
          containerPort: 8080
          protocol: TCP
```

3. `kubectl argo rollouts list rollouts`
4. `kubectl argo rollouts set image SOME-APP web-app=some/registry/and/image:v2.0`
   1. `kubectl argo rollouts get rollout some-app --watch`
