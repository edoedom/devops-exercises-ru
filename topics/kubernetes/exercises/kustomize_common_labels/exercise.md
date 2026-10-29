<a id="kustomize---common-labels"></a>
# Kustomize: общие метки

<a id="requirements"></a>
## Требования

1. Работающий кластер Kubernetes.
2. kubectl версии 1.14 или выше.

<a id="objectives"></a>
## Задание

В текущем каталоге находится приложение, состоящее из Deployment и Service.

1. Напишите файл kustomization.yml, который добавит обоим ресурсам метку `team-name: aces`.
2. Выполните команду Kustomize для формирования манифестов Kubernetes с этой меткой.

<a id="solution"></a>
## Решение

[Посмотреть решение](solution.md).
