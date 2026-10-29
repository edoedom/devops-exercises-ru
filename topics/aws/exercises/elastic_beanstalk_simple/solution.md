<a id="aws-elastic-beanstalk---nodejs"></a>
## AWS Elastic Beanstalk: Node.js

<a id="prerequisites"></a>
### Предварительная подготовка

1. Убедитесь, что в package.json приложения определена команда npm start, например:

```
{

  "name": "application-name",
  "version": "0.0.1",
  "private": true,
  "scripts": {
    "start": "node app"
  },
  "dependencies": {
    "express": "3.1.0",
    "jade": "*",
    "mysql": "*",
    "async": "*",
    "node-uuid": "*"
} 
```

2. Создайте ZIP-архив приложения. Архивируйте сами файлы, а не родительскую папку, например:

```
\Parent - (exclude the folder itself from the the zip)
- file1 - (include in zip)
- subfolder1 (include in zip)
- file2 (include in zip)
- file3 (include in zip)
```

<a id="solution"></a>
### Решение

1. Создайте среду через **New Environment**.
2. Выберите **Web Server Environment**.
3. В разделе создания среды веб-сервера заполните **Application Name**.
4. В разделе информации о среде:
   * Заполните **Environment Name**.
   * Для домена оставьте автоматически сформированное значение.
5. В качестве платформы выберите Node.js.
6. В разделе **Application Code** загрузите ZIP-архив с локального компьютера.
7. Нажмите **Create Environment**.
8. Дождитесь запуска среды.
9. Проверьте сайт: откройте вкладку **Applications**, выберите созданное приложение Node.js и нажмите выделенный URL.

<a id="documentation"></a>
### Документация

[Начало работы с Node.js в Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/nodejs-getstarted.html)
