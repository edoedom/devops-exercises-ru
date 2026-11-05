<a id="create-buckets"></a>
# Создание бакетов

<a id="objectives"></a>
## Задание

1. Создайте следующие бакеты:
   1. Закрытый бакет:
      1. Регион: eu-west-2.
      2. Загрузите в него один любой файл.
   2. Публичный бакет:
      1. Регион: eu-west-1.
      2. Включите версионирование.

<a id="solution"></a>
## Решение

<a id="console"></a>
### Консоль

Для первого бакета:

1. Откройте S3 в консоли AWS. Если список бакетов не открыт, выберите **Buckets** в левом меню.
2. Нажмите **Create bucket**.
3. Укажите глобально уникальное имя.
4. Выберите регион eu-west-2.
5. Нажмите **Create bucket**.
6. Откройте бакет по его имени.
7. На вкладке **Objects** выберите **Upload → Add files**, укажите файл и нажмите **Upload**.

Для второго бакета:

1. Откройте список бакетов S3.
2. Нажмите **Create bucket**.
3. Укажите глобально уникальное имя.
4. Выберите регион eu-west-1.
5. Оставьте Object Ownership в режиме **Bucket owner enforced**: ACL не нужны.
6. Включите **Bucket Versioning**.
7. Создайте бакет. Для публичного чтения учебных объектов разрешите публичные bucket policies в Block Public Access и добавьте policy с `s3:GetObject` на ARN объектов (`arn:aws:s3:::ИМЯ/*`). Права `ListBucket` для этого не требуются.

Само отключение Block Public Access не выдаёт прав. Ограничения на уровне аккаунта и организации продолжают действовать. Не отключайте общую защиту аккаунта ради упражнения; используйте выделенный учебный аккаунт. Загружайте только данные, предназначенные для публикации.

<a id="terraform"></a>
### Terraform

[Посмотреть решение](terraform/main.tf).

<a id="pulumi---python"></a>
### Pulumi: Python

[Посмотреть решение](pulumi/__main__.py).

Оба примера по умолчанию создают закрытые бакеты. Terraform: `terraform init`, `terraform plan`, затем для публичной части задания `terraform apply -var=enable_public_read=true`. Pulumi: в Python-проекте с зависимостями `pulumi` и `pulumi-aws` задайте `pulumi config set enablePublicRead true` и выполните `pulumi up`. Имена бакетов генерируются с уникальными суффиксами, регионы заданы отдельными provider-конфигурациями.

Проверьте, что анонимный запрос к закрытому объекту отклоняется, а к специально загруженному объекту публичного бакета — разрешён. После упражнения удалите объекты и все их версии, затем выполните `terraform destroy` или `pulumi destroy` для выбранного варианта. Примеры не включают принудительное удаление данных.

Источники: [S3 Block Public Access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/configuring-block-public-access-bucket.html), [Object Ownership](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html).
