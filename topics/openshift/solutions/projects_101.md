<a id="openshift---projects-101"></a>
## OpenShift: основы работы с проектами

<a id="objectives"></a>
### Задание

Выполните следующие действия, желательно в только что развёрнутом кластере:

1. Войдите в кластер OpenShift.
2. Выведите список всех проектов.
3. Создайте проект с именем `neverland`.
4. Посмотрите сводное состояние текущего проекта.

<a id="solution"></a>
### Решение

```
oc login -u YOUR_USER -p YOUR_PASSWORD_OR_TOKEN
oc get projects # Empty output in new cluster
oc new-project neverland
oc status
```
