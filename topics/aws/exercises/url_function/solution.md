<a id="url-function"></a>
## Вызов функции по URL

Создайте простую функцию AWS Lambda, которая вызывается при открытии URL в браузере.

<a id="solution"></a>
### Решение

<a id="define-a-function"></a>
#### Создание функции

1. В консоли Lambda нажмите `Create function`:
   1. Укажите имя, например `urlFunction`.
   2. Выберите среду выполнения `Python3`.
   3. Назначьте существующую роль IAM или создайте новую. В исходном примере выбран вариант **Create a new role from AWS policy templates**.
   4. В **Policy Templates** выберите **Simple Microservice Permissions**.
2. В редакторе введите код, аналогичный следующему.

<a id="functions-code"></a>
#### Код функции

```
import json


def lambda_handler(event, context):
    firstName = event['name']
    return 'Hello ' + firstName
```

3. Нажмите **Create Function**.

<a id="define-a-test"></a>
#### Создание теста

1. Нажмите **Test**.
2. Выберите **Create new test event**.
3. Укажите имя события, например TestEvent.
4. Задайте ключи для проверки:

```
{
  "name": 'Spyro'
}
```

5. Нажмите **Create**.

<a id="test-the-function"></a>
#### Проверка функции

1. Выберите событие `TestEvent`.
2. Нажмите `Test`.
3. Должно появиться сообщение вроде `Execution result: succeeded`.
4. В AWS CloudWatch должен появиться соответствующий поток журнала.

<a id="define-a-trigger"></a>
#### Создание триггера

Настройте вызов функции при открытии URL в браузере.

1. В консоли API Gateway выберите **New API Option**.
2. Задайте имя и описание API, затем нажмите **Create**.
3. Выберите **Actions → Create Resource**.
4. Укажите имя ресурса и путь, например /hello, затем нажмите **Create Resource**.
5. Выберите ресурс и нажмите **Create Method**.
6. Тип интеграции: **Lambda Function**. Укажите имя созданной функции и тот же регион.
7. Подтвердите настройки и необходимые разрешения.
8. Откройте ресурс и измените **Body Mapping Templates**, добавив:

```
{ "name": "$input.params('name')" }
```

9. Сохраните изменения и выберите **Actions → Deploy API**.

<a id="running-the-function"></a>
#### Вызов функции

1. В меню **Stages** консоли API Gateway выберите API и метод GET.
2. Откройте URL вызова. Возможно, потребуется добавить параметр, например `.../hello?name=mario`.
3. В браузере должно появиться `Hello Mario`.
