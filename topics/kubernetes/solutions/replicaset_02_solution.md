<a id="replicaset-02---solution"></a>
## ReplicaSet 02: решение

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

3. Удалите ReplicaSet, сохранив созданные им поды.

```
kubectl delete -f rs.yaml --cascade=orphan
```

4. Убедитесь, что ReplicaSet удалён, а поды продолжают работать.

```
kubectl get rs # no replicas
kubectl get po # Pods still running
```

5. Снова создайте тот же ReplicaSet без изменения конфигурации.

```
kubectl apply -f rs.yaml
```

6. Убедитесь, что ReplicaSet использовал существующие поды, а не создал новые.

```
kubectl describe rs web  # You should see there are no new events and if you list the pods with 'kubectl get po -f rs.yaml` you'll see they have the same names
```
