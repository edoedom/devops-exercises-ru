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
| Навигация | Исправлены относительные пути в Git, БД, разработке ПО, контейнерах, AWS и OpenShift; позднее восстановлены ссылки на Jenkins-решения в topics/cicd/solutions (см. четвёртую партию) |
| Пропущенное задание AWS | Вместо TODO описаны API Gateway → Lambda → DynamoDB, IAM-авторизация, требования обработки и тестовые случаи; добавлен порядок реализации |

## Проверки изменений

Два исправленных Ingress, исправленный полный CronJob и новый HTTPRoute разобраны YAML-парсером; проверено расположение существенных полей. После исправления относительных путей повторён поиск отсутствующих файлов. Эти проверки не заменяют server-side validation с конкретным кластером и установленными CRD.

Сборки Docker, Terraform plan/apply, promtool и запуск в облаках не выполнялись. Проверка совместимости с конкретной версией провайдера и фактическое выполнение упражнений ещё нужны.

## Границы проверки

- Заполнены все исходные вопросы без текстового ответа, но это не означает полной независимой проверки каждого старого утверждения.
- Внешние URL, изображения и все практические задания ещё не проверены исполнением целиком.
- Сертификационные конспекты требуют отдельного сопоставления с действующими программами экзаменов.
- Код проверяется локально; облачное развёртывание, права реального аккаунта и поведение конкретного Kubernetes-кластера не подтверждены.

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

## Вторая партия: Linux, основы и безопасность

Заполнены 172 ранее пустых ответа в Linux (83), Git (1), базах данных (5), разработке (10), Bash (8), CI/CD (1), DevOps (13), безопасности (32) и Ansible (19). Личные вопросы дополнены ориентирами для правдивого ответа, а не выдуманными историями.

Дополнены DNSSEC/DoH/DoT, отрицательное кэширование и диагностика; исправлены стратегии Git, restore, MAC-адреса, load/OOM и диагностика портов. Добавлены вопросы по изоляции транзакций, индексам, резервным копиям и параметрам SQL. Примеры хеш-таблицы проверены на коллизии, обновление, удаление и отсутствующий ключ; проверены Factory/Strategy/Adapter. Новый YAML Ansible разобран, лаборатория namespace прошла bash -n. Привилегированные сетевые операции не исполнялись. Полное тестирование Ansible на целевых ОС ещё требуется.

После этой партии в исходных вопросах осталось 206 пустых ответов. Удаление всех пустот само по себе не будет означать завершения проверки остальных утверждений и исполнимости всех проектов.

Источники дополнений: [Git](https://git-scm.com/docs/merge-strategies), [Linux cgroups](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html), [Bash](https://www.gnu.org/software/bash/manual/bash.html), [PostgreSQL](https://www.postgresql.org/docs/current/transaction-iso.html), [Ansible](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_variables.html), [OAuth Security BCP](https://www.rfc-editor.org/rfc/rfc9700.html), [NIST CMVP](https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules).

## Третья партия: оставшиеся текстовые пробелы

Дополнены оставшиеся 206 вопросов без текстового ответа: 204 действительно пустых ответа и две схемы Kubernetes, у которых исходное решение было только картинкой. Изображения сохранены, к ним добавлено текстовое объяснение. Таким образом, исходный поиск 378 «пустых» случаев включал 376 пустых ответов и два графических решения.

В результате во всех 286 исходных Markdown-файлах не осталось блоков вопроса без текста ответа. Вопросы о личном опыте и работодателе снабжены ориентирами, а не фиктивными ответами кандидата или компании. Добавлены материалы по хранилищам Kubernetes, маршрутизации, system design, Elastic, Azure/Entra и облачным сервисам. Названия Azure AD/ATP актуализированы с сохранением исторического контекста; для CloudSearch отмечена недоступность новым клиентам.

Это завершение заполнения пробелов, а не утверждение, что проверено каждое старое утверждение, каждая картинка и каждый внешний URL. Продолжается проверка исполняемого кода и учебных проектов.

## Четвёртая партия: исполняемые примеры и CI

Исправлены оба Flask-приложения: фабрики приложения, путь к данным, отсутствие внутренних id в ответах, маршруты матрицы, проверка входных данных и коды ошибок. Убрана ненужная зависимость Flask-WTF, используется Flask 3.1. Инструкции соответствуют реальным путям и маршрутам.

Завершён учебный Terraform-проект HTTP API → Lambda → DynamoDB: Python 3.13, IAM-авторизация маршрутов, execution role с ограниченными правами, log retention, обработчик GET/PUT с валидацией. Исправлены Terraform/Pulumi для трёх подсетей, обязательные диск и интерфейс GCP VM, S3 bucket policies вместо ACL, отдельные региональные провайдеры и явное включение публичного чтения.

Переписан пример S3 → Lambda → SNS: отдельные новые ресурсы, корректная упаковка handler, invoke permission от S3, TOPIC_ARN из окружения, все записи события и декодирование ключей. Убраны чужой email, фиксированный аккаунт и чрезмерные managed policies. Облачные скрипты не запускались.

Jenkins-решения найдены в `topics/cicd/solutions`: предыдущая отметка об их отсутствии была неверной. Ссылки восстановлены, примеры удаляют через Jenkins API и сначала печатают список; активные и закреплённые сборки сохраняются. Ansible-развёртывание использует `kubernetes.core.k8s`, один TLS secret, переданный образ сборки и явно выбранный IngressClass вместо неявных зависимостей от nginx/cert-manager и чужого kubeconfig.

Починены счётчик вопросов, случайный выбор, проверки Markdown и импорты тестов. Добавлены воспроизводимый `scripts/run_ci.sh`, зависимости и конфигурация GitHub Actions для Python 3.12/3.13. Счётчик: 2566 вопросов и 108 уникальных ссылок на задания в главном README и README разделов, без повторов сертификаций.

Локальные проверки: 22 теста (10 общих, по 6 у каждого Flask-приложения), AST 25 Python-файлов, разбор 12 Terraform-файлов, YAML и Bash syntax, структура 314 Markdown-файлов полного рабочего дерева. Все эти проверки прошли. Исправлен также пропущенный открывающий details в сохранённом португальском README. Для HCL выполнен terraform fmt.

Terraform 1.13.5 скачан, init загрузил провайдеры, но последующий validate остановился на несовпадении контрольных сумм пакетов с созданным lock-файлом. Проверка контрольных сумм не отключалась; Terraform validate/plan/apply не считаются пройденными. Lock-файлы этого неудачного окружения не публикуются. Провайдерные схемы следует дополнительно проверить в чистом окружении.

Источники: [Flask factories](https://flask.palletsprojects.com/en/stable/patterns/appfactories/), [S3 public access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/granting-public-access.html), [S3 notifications](https://docs.aws.amazon.com/lambda/latest/dg/with-s3.html), [Lambda runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html), [Jenkins Pipeline](https://www.jenkins.io/doc/book/pipeline/syntax/), [Ansible Kubernetes](https://docs.ansible.com/projects/ansible/latest/collections/kubernetes/core/k8s_module.html).
