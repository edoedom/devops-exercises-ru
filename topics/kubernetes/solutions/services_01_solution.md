<a id="services-01---solution"></a>
## Сервисы: решение задания 01

```
kubectl run nginx --image=nginx --restart=Never --port=80 --labels="app=dev-nginx"

cat << EOF > nginx-service.yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: dev-nginx
  ports:
    - protocol: TCP
      port: 80
      targetPort: 9372
EOF
```
