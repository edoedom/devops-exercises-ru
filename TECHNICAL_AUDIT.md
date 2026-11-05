# Техническая проверка материалов

Проверка начата 5 ноября 2026 года. Перевод исходной версии завершён; техническое обновление — отдельная работа и ещё продолжается.

## Что проверено

Выполнен общий статический поиск по 286 исходным Markdown-файлам: удалённые версии Kubernetes API, некоторые устаревшие команды и квоты, неправильные PromQL-примеры, существование относительных ссылок на файлы. Совпадения проверены вручную: например, `--replicas` допустим у `kubectl create deployment` и `kubectl scale`.

Это не означает проверки каждого утверждения всех файлов. Внешние URL не проходили сплошную сетевую проверку, учебные среды не развёртывались. Числовые ограничения, тарифы и версии следует читать вместе с датой и официальным источником.

## Исправлено в первой партии

| Область | Изменения |
|---|---|
| AWS и два файла сертификаций | Предел объекта S3, отличие от одного PUT; исправлены значения доступности и сохранности классов, добавлен Express One Zone и различия архивных классов |
| Terraform | Нативная блокировка S3 в Terraform 1.10+; DynamoDB locking отмечена устаревшей; права на `.tflock`; кавычки для state-адреса с индексом |
| Terraform: новые вопросы | Декларативные moved/import, sensitive против ephemeral и write-only |
| Kubernetes | Исправлены два манифеста Ingress v1; CronJob переведён на batch/v1; добавлено полное исправленное решение |
| Kubernetes: новые вопросы | Gateway API, HTTPRoute и прекращение сопровождения общественного ingress-nginx |
| Главный README | Рабочие PromQL-примеры increase, vector matching и процента CPU вместо некорректных блоков исходника |
| Docker | Compose V2, ожидание готовности MySQL, поддерживаемые ветки Node.js/Python, multi-stage через wheels, исправлены имя контейнера и запуск shell |
| CI/CD | Убрано условие сборки, пропускавшее изменения зависимостей; исправлены kubectl-команды в упражнении Argo CD |
| Навигация | Исправлены относительные пути в Git, БД, разработке ПО, контейнерах, AWS и OpenShift; удалены ссылки на отсутствующие Jenkins-скрипты с явной отметкой отсутствия решения |
| Пропущенное задание AWS | Вместо TODO описаны API Gateway → Lambda → DynamoDB, IAM-авторизация, требования обработки и тестовые случаи; добавлен порядок реализации |

## Проверки изменений

Два исправленных Ingress, исправленный полный CronJob и новый HTTPRoute разобраны YAML-парсером; проверено расположение существенных полей. После исправления относительных путей повторён поиск отсутствующих файлов. Эти проверки не заменяют server-side validation с конкретным кластером и установленными CRD.

Сборки Docker, Terraform plan/apply, promtool и запуск в облаках не выполнялись. Проверка совместимости с конкретной версией провайдера и фактическое выполнение упражнений ещё нужны.

## Оставшаяся работа

- Последовательная проверка утверждений и полноты ответов во всех разделах, включая Linux, сети, Git, БД, CI/CD и облака.
- Проверка полноты и исполнимости исходных программ и IaC. В частности, заготовка Terraform для Lambda/DynamoDB остаётся незавершённой и пока явно обозначена как заготовка.
- Сверка материалов CKA/AWS/Azure с действующими программами экзаменов; перевод старого конспекта не считается актуальной программой сертификации.
- Проверка внешних ссылок и замена действительно недоступных источников официальными.
- Проверка оставшихся пустых ответов и TODO: не все вопросы исходника имели решения.

## Основные источники

- [Terraform S3 backend](https://developer.hashicorp.com/terraform/language/backend/s3)
- [Секреты Terraform](https://developer.hashicorp.com/terraform/language/manage-sensitive-data)
- [Миграция Kubernetes API](https://kubernetes.io/docs/reference/using-api/deprecation-guide/)
- [Gateway API](https://gateway-api.sigs.k8s.io/)
- [Завершение сопровождения ingress-nginx](https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/)
- [Загрузка объектов S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html)
- [Классы S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)
- [Функции PromQL](https://prometheus.io/docs/prometheus/latest/querying/functions/)
- [Docker Compose: готовность сервисов](https://docs.docker.com/compose/how-tos/startup-order/)
- [Статус Python](https://devguide.python.org/versions/)
- [Статус Node.js](https://nodejs.org/en/about/previous-releases)
