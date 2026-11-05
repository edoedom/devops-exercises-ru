# S3 → Lambda → SNS

Пример создаёт отдельный закрытый бакет, Lambda на Python 3.13, SNS topic, email subscription, execution role и log group. SNS присылает уведомление о создании объекта. Нужны AWS CLI v2 с настроенными credentials, `jq`, `zip`, Python 3 и права на создание этих ресурсов. Используйте учебный аккаунт; ресурсы оплачиваются по тарифам AWS.

Из каталога этого примера:

```bash
export AWS_REGION=us-east-1
export EMAIL_ADDRESS=you@example.com
bash aws_s3_event_trigger.sh
```

Подтвердите подписку по ссылке из письма SNS. Затем загрузите файл командой, напечатанной скриптом. Скрипт не загружает объект до подтверждения подписки и не использует существующие бакеты. Сохраните напечатанные имена ресурсов для очистки. Если создание прервалось, удалите уже созданные ресурсы вручную; автоматического отката нет.

Обработчик читает `TOPIC_ARN`, обрабатывает все записи и декодирует ключи S3. Доставка S3/Lambda допускает повторы; одно событие может вызвать несколько писем. Для бизнес-операций нужен отдельный механизм идемпотентности.

После работы отключите notifications у созданного бакета, удалите тестовые объекты и бакет, Lambda, SNS topic с подпиской, log group, inline policy `lab-permissions` и IAM role. Не используйте массовую очистку для других ресурсов аккаунта.

Источники: [S3 trigger и permissions](https://docs.aws.amazon.com/lambda/latest/dg/with-s3.html), [структура события S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/notification-content-structure.html).
