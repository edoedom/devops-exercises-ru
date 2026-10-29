<a id="argocd-secrets-101"></a>
# Argo CD: основы работы с секретами

<a id="requirements"></a>
## Требования

1. Работающий кластер Kubernetes.
2. Манифесты Kubernetes приложения, содержащие секреты.
3. Установленная утилита kubeseal.

<a id="objectives"></a>
## Задание

1. Установите контроллер Bitnami Sealed Secrets как приложение Argo CD.
2. Зашифруйте секреты и добавьте их в репозиторий с манифестами Kubernetes.
3. Создайте приложение, использующее зашифрованные секреты.

<a id="solution"></a>
## Решение

1. Нажмите **New App** и задайте параметры:
   1. Имя: controller.
   2. Проект: default.
   3. Политика синхронизации: automatic.
   4. URL репозитория: адрес манифестов контроллера Bitnami Sealed Secrets.
   5. Пространство имён: kube-system.
2. Для каждого секрета выполните: `kubeseal < some/secret.yml > sealed_secrets/some/encrypted_secret.yaml -o yaml`.
3. Нажмите **New App** и задайте параметры приложения:
   1. Имя: some-app.
   2. Проект: default.
   3. Политика синхронизации: automatic.
   4. URL репозитория: адрес манифестов Kubernetes, включая зашифрованные секреты.
   5. Пространство имён: default.
