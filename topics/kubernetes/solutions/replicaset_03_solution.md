<a id="replicaset-03---solution"></a>
## ReplicaSet 03: решение

1. Создайте ReplicaSet с двумя репликами. Для селектора и подов используйте метку type=web.

```
cat >> rs.yaml <<EOL
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: web
  labels:
    app: somewebapp
    type: web
spec:
  replicas: 2
  selector:
    matchLabels:
      type: web
  template:
    metadata:
      labels:
        type: web
    spec:
      containers:
      - name: httpd
        image: registry.redhat.io/rhscl/httpd-24-rhel7
EOL

kubectl apply -f rs.yaml
```

2. Проверьте, что ReplicaSet создан и работают две реплики.

```
kubectl get rs
# OR a more specific way: kubectl get -f rs.yaml
```

3. Выведите список работающих подов и сохраните вывод.

```
kubectl get po > running_pods.txt
```

4. Удалите метку type=web у одного из подов ReplicaSet.

```
kubectl label pod <POD_NAME> type-
```

5. Снова выведите список подов. Стало ли их больше? Почему?

```
Yes, there is an additional Pod running because once the label (used as a matching selector) was removed, the Pod became independent meaning, it's not controlled by the ReplicaSet anymore and the ReplicaSet was missing replicas based on its definition so, it created a new Pod.
```

6. Убедитесь, что ReplicaSet создал новый под.

```
kubectl describe rs web
```
