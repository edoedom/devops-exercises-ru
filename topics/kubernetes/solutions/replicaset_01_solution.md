<a id="replicaset-01---solution"></a>
## ReplicaSet 01: решение

1. Создайте ReplicaSet с двумя репликами любого приложения.

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

3. Удалите один из созданных подов.

```
kubectl delete po <POD_NAME>
```

4. Что вы увидите, если теперь выведете список подов?

```
The same number of Pods. Since we defined 2 replicas, the ReplicaSet will make sure to create another Pod that will replace the one you've deleted.
```

5. Удалите созданный ReplicaSet.

```
kubectl delete -f rs.yaml
```

6. Убедитесь, что ReplicaSet удалён.

```
kubectl get rs
# OR a more specific way: kubectl get -f rs.yaml
```
