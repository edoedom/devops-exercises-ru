<a id="node-selectors"></a>
# Селекторы узлов

<a id="objectives"></a>
## Задание

1. Добавьте метку `hw=max` одному из узлов кластера.
2. Создайте и запустите под `some-pod` из образа `redis`, настроив селектор узлов `hw=max`.
3. Объясните ограничения селекторов узлов.

<a id="solution"></a>
## Решение

[Посмотреть решение](solution.md).

1. `kubectl label nodes some-node hw=max`
2. Создайте под:

```
kubectl run some-pod --image=redis --dry-run=client -o yaml > pod.yaml

vi pod.yaml

spec:
  nodeSelector:
    hw: max

kubectl apply -f pod.yaml
```

3. Предположим, что под нужно размещать на узлах, у которых hw равно max или min, а не только max. Простой механизм nodeSelector не позволяет выразить такое условие. Для этого стоит рассмотреть `node affinity`.
