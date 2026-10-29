<a id="taints-101"></a>
# Ограничения планирования taint: основы

<a id="objectives"></a>
## Задание

1. Проверьте наличие taint у любого узла кластера.
2. Добавьте одному из узлов taint с ключом app, значением web и эффектом NoSchedule.
   1. Объясните его действие.
   2. Убедитесь, что taint добавлен.

<a id="solution"></a>
## Решение

1. `kubectl describe no minikube | grep -i taints`
2. `kubectl taint node minikube app=web:NoSchedule`
   1. Новые поды без подходящего toleration не будут планироваться на узел `minikube`.
   2. Проверка: `kubectl describe no minikube | grep -i taints`.
3. Создайте под по следующему примеру:

```
kubectl run some-pod --image=redis
kubectl edit po some-pod
```

```
 - effect: NoSchedule
    key: app
    operator: Equal
    value: web
```

Сохраните изменения и выйдите из редактора. Под должен запуститься.

> Примечание к переводу: в оригинале действие taint ошибочно связывалось с меткой app=web у ресурса. Ограничение зависит от наличия подходящего toleration у пода.
