<a id="labels-and-selectors-101"></a>
# Метки и селекторы: основы

<a id="objectives"></a>
## Задание

1. Как вывести все поды с меткой `app=web`?
2. Как вывести все объекты с меткой `env=staging`?
3. Как вывести все Deployment с метками `env=prod` и `type=web`?

<a id="solution"></a>
## Решение

`k get po -l app=web`
`k get all -l env=staging`
`k get deploy -l env=prod,type=web`

> Примечание к переводу: в исходнике используется сокращение `k`; предполагается, что оно настроено как псевдоним `kubectl`. Команда `get all` охватывает не все существующие типы ресурсов Kubernetes.
