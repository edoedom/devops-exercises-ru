<a id="hello-function---solution"></a>
## Функция приветствия: решение

<a id="exercise"></a>
### Задание

Создайте простую функцию AWS Lambda, которая получает имя и возвращает `Hello <NAME>`, подставляя полученное имя.

<a id="solution"></a>
### Решение

<a id="define-a-function"></a>
#### Создание функции

1. В консоли Lambda нажмите `Create function`:
   1. Задайте имя, например `BasicFunction`.
   2. Выберите среду выполнения `Python3`.
   3. Назначьте существующую роль IAM или создайте новую. В исходном примере выбран вариант **Create a new role from AWS policy templates**.
   4. В **Policy Templates** выберите **Simple Microservice Permissions**.
2. В появившемся редакторе введите код, аналогичный следующему.

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
3. Укажите **Event name**, например TestEvent.
4. Задайте ключи тестового события:

```
{
  "name": 'Spyro'
}
```

5. Нажмите **Create**.

<a id="test-the-function"></a>
#### Проверка функции

1. Выберите созданное событие `TestEvent`.
2. Нажмите `Test`.
3. Должно появиться сообщение вроде `Execution result: succeeded`.
4. В AWS CloudWatch должен появиться соответствующий поток журнала.
