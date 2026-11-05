# Решение: API Gateway, Lambda и DynamoDB

Это порядок реализации задания, а не готовый автоматически развёртываемый проект.

1. Создайте DynamoDB-таблицу `users` с ключом `id` (String) и billing mode `PAY_PER_REQUEST`. Для запросов по `id` GSI по login не требуется.
2. Создайте execution role Lambda с доверенным сервисом `lambda.amazonaws.com`. Для таблицы разрешите `dynamodb:GetItem` и `dynamodb:PutItem` только на ARN этой таблицы; отдельно разрешите запись в нужную CloudWatch Logs log group. Provisioning-права и execution role — разные вещи.
3. Создайте Lambda на поддерживаемом runtime и задайте `TABLE_NAME`. Обработчик должен разбирать `event.requestContext.http.method`, `pathParameters.id` и `body`. Для base64-тела сначала декодируйте `body`, если `isBase64Encoded` равно true.
4. Для PUT проверьте JSON, тип и длину login. Запишите объект `{id, login}` через SDK; PUT заменяет существующую запись с этим ключом. Для GET вызовите GetItem; если сразу после PUT требуется актуальное чтение, задайте `ConsistentRead=true`.
5. Возвращайте объект ответа с `statusCode`, заголовком `content-type: application/json` и строкой JSON в `body`. Обрабатывайте ошибки SDK: детали пишите в защищённый журнал, клиенту отдавайте контролируемый 5xx.
6. Создайте HTTP API, Lambda proxy integration с payload format `2.0` и маршруты `PUT /users/{id}`, `GET /users/{id}`. Выдайте API Gateway право вызвать Lambda с ограничением SourceArn нужным API.
7. Для обоих маршрутов задайте `AWS_IAM`. Клиенту предоставьте `execute-api:Invoke` только для нужных маршрутов. Настройте stage/deployment и используйте подписанные SigV4-запросы. Для браузерного frontend отдельно спроектируйте аутентификацию и CORS; не вкладывайте постоянные AWS-ключи в JavaScript.
8. Проверьте: без подписи — отказ; PUT с неверным JSON — 400; корректный PUT — 200; GET существующего id — 200; неизвестного — 404. Проверьте, что execution role не может читать чужую таблицу.
9. Удалите API, функцию, учебную таблицу, созданные роли и log group. Сохранённые журналы могут продолжать занимать место.

[Lambda proxy integration и payload 2.0](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html) · [IAM-доступ к HTTP API](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-access-control-iam.html) · [Согласованность DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html).
