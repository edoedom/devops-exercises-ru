
<a id="docker-scenario-based-exercises"></a>
# Практические задания по Docker

Этот файл содержит задания по Docker на основе рабочих ситуаций. Они помогают DevOps-инженерам практиковаться в диагностике неисправностей и настройке. Для каждого задания приведён пошаговый ответ.

<a id="question-1-debugging-a-docker-container-failure"></a>
## Задание 1. Диагностика сбоя контейнера Docker

### Вопрос
Вы развёртываете приложение Node.js с помощью Docker. После запуска `docker run -d --name my-node-app -p 3000:3000 my-node-app` контейнер сразу завершается. Команда `docker ps -a` показывает состояние `Exited`. Как найти и устранить причину?

### Ответ
Если контейнер сразу завершается:

1. **Проверьте журналы.** Выполните `docker logs my-node-app`, чтобы увидеть сообщения об ошибках. Частые причины — отсутствующие зависимости (например, ошибка при `npm install`) или неправильная команда запуска.
2. **Изучите параметры контейнера.** Командой `docker inspect my-node-app` проверьте `Config.Cmd` и `Config.Entrypoint`. Убедитесь, что команда, например `node app.js`, корректна.
3. **Проверьте Dockerfile.** Убедитесь, что `CMD` или `ENTRYPOINT` заданы правильно, например `CMD ["node", "app.js"]`. При необходимости исправьте файл и пересоберите образ: `docker build -t my-node-app .`.
4. **Проверьте запуск в интерактивном режиме.** Выполните `docker run --rm -it --entrypoint sh my-node-app`, чтобы вручную запустить приложение, например `node app.js`, и исследовать ошибку.
5. **Проверьте ресурсы.** Используйте `docker stats` для наблюдения за потреблением ресурсов и убедитесь, что на хосте достаточно памяти и процессорного времени.

**Пример исправления:** если в журнале указано `node: command not found`, задайте в Dockerfile базовый образ `FROM node:24-bookworm-slim`, пересоберите образ и повторите запуск.

> Примечание к переводу: исходная команда не задаёт имя контейнера. Для `docker logs` и `docker inspect` используйте фактическое имя или ID из `docker ps -a` либо добавьте при запуске `--name my-node-app`.

### Дополнительные замечания

- Начинайте с `docker logs`: сообщения журнала помогают найти причину.
- Проверяйте состояние и ID контейнера через `docker ps -a`.
- Частые причины сбоев — отсутствующие зависимости и ошибки приложения.

---

<a id="question-2-configuring-a-multi-container-application"></a>
## Задание 2. Настройка приложения из нескольких контейнеров

### Вопрос
Нужно развернуть веб-приложение с серверной частью на Node.js и базой MySQL. Приложение обращается к MySQL по адресу `localhost:3306`, но при отдельном запуске контейнеров через `docker run` они не могут связаться друг с другом. Как настроить их совместную работу?

### Ответ
Чтобы обеспечить взаимодействие контейнеров Node.js и MySQL:

1. **Используйте Docker Compose.** Создайте `docker-compose.yml` с описанием обоих сервисов:
   ```yaml
   services:
     node-app:
       image: my-node-app
       build: .
       ports:
         - "3000:3000"
       depends_on:
         mysql-db:
           condition: service_healthy
       environment:
         - DB_HOST=mysql-db
         - DB_PORT=3306
     mysql-db:
       image: mysql:8.0
       environment:
         - MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD:?set MYSQL_ROOT_PASSWORD}
       healthcheck:
         test: ["CMD", "mysqladmin", "ping", "-h", "127.0.0.1"]
         interval: 5s
         timeout: 3s
         retries: 20
         start_period: 30s
       volumes:
         - mysql-data:/var/lib/mysql
   volumes:
     mysql-data:
   ```
2. **Запустите приложение.** Выполните `docker compose up -d`. Сервис `node-app` подключается к MySQL по имени сервиса `mysql-db`, а не по адресу `localhost`.
3. **Проверьте соединение.** Посмотрите журнал командой `docker compose logs node-app`. Если подключение не установлено, проверьте переменные окружения и готовность MySQL принимать соединения.
4. **Вариант без Compose:** создайте пользовательскую сеть:
   - Создание сети: `docker network create my-app-network`
   - Запуск MySQL: `docker run -d --name mysql-db --network my-app-network -e MYSQL_ROOT_PASSWORD=secret mysql:8.0`
   - Запуск Node.js: `docker run -d --name node-app --network my-app-network -p 3000:3000 -e DB_HOST=mysql-db my-node-app`

### Дополнительные замечания

- Docker Compose упрощает работу с несколькими контейнерами, управляя сетями и зависимостями.
- Передавайте учётные данные базы через переменные окружения, чтобы не записывать их непосредственно в код приложения.

---

<a id="question-3-optimizing-a-dockerfile-for-cicd"></a>
## Задание 3. Оптимизация Dockerfile для CI/CD

### Вопрос
Вы подключаете Python-приложение в Docker к конвейеру CI/CD в Jenkins. Сборка образа занимает много времени и задерживает конвейер. Как ускорить сборку, сохранив работоспособность приложения?

### Ответ
Для ускорения сборок:

1. **Выберите меньший базовый образ.** Замените крупный образ, например `python:3.13`, на `python:3.13-slim`, чтобы уменьшить размер и время загрузки.
   ```dockerfile
   FROM python:3.13-slim
   ```
2. **Используйте кеширование слоёв.** Располагайте инструкции от редко меняющихся к часто меняющимся. Скопируйте `requirements.txt` и установите зависимости до копирования кода приложения:
   ```dockerfile
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   ```
3. **Сократите число слоёв.** Объединяйте связанные команды с помощью `&&`:
   ```dockerfile
   RUN pip install -r requirements.txt && rm -rf /root/.cache/pip
   ```
4. **Используйте многоэтапную сборку.** Если для сборки нужны дополнительные инструменты, отделите этап сборки от итогового образа, чтобы уменьшить его размер:
   ```dockerfile
   FROM python:3.13-slim AS builder
   WORKDIR /build
   COPY requirements.txt .
   RUN pip wheel --wheel-dir /wheels -r requirements.txt

   FROM python:3.13-slim
   WORKDIR /app
   COPY --from=builder /wheels /wheels
   COPY requirements.txt .
   RUN pip install --no-cache-dir --no-index --find-links=/wheels -r requirements.txt \
       && rm -rf /wheels
   COPY . .
   CMD ["python", "app.py"]
   ```
5. **Проверьте результат в Jenkins.** Запускайте сборку каждого изменения; Docker повторно использует неизменившиеся слои. Пропуск только по Dockerfile и *.py пропускает изменения requirements.txt и других входов:
   ```groovy
   pipeline {
       agent any
       stages {
           stage('Build Docker Image') {
               steps { sh 'docker build -t my-python-app .' }
           }
       }
   }
   ```

### Дополнительные замечания

- Исключите ненужные файлы, например `.git` и `tests/`, из контекста сборки через `.dockerignore`.
- Отслеживайте длительность сборок в Jenkins, чтобы оценить результат.

*Автор материала: Lahiru Galhena*

При миграции версии Python/Node.js проверьте совместимость приложения и зависимостей. Python 3.9 и Node.js 18 уже завершили поддержку. Для native wheels может потребоваться компилятор в builder и системные библиотеки в runtime. Для production используйте актуальные исправления выбранной поддерживаемой ветки и фиксируйте digest после проверки.

`depends_on: service_healthy` помогает начальному запуску, но не заменяет повторное подключение приложения после отказа БД. В Compose-примере задайте MYSQL_ROOT_PASSWORD через окружение, не коммитьте секрет; переменные DB_USER/DB_PASSWORD и миграции задаются приложением. Публикация MySQL на хост не нужна для связи внутри сети Compose. Вариант с `secret` ниже — только демонстрация синтаксиса, не пароль для эксплуатации.

[Compose: готовность сервисов](https://docs.docker.com/compose/how-tos/startup-order/) · [Кэш сборки](https://docs.docker.com/build/cache/optimize/) · [Поддержка Python](https://devguide.python.org/versions/) · [Поддержка Node.js](https://nodejs.org/en/about/previous-releases).
