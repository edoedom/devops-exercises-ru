<a id="containerize-an-application"></a>
## Упаковка приложения в контейнер

1. Клонируйте проект с открытым исходным кодом. Несколько вариантов:

```
https://github.com/bregman-arie/node-hello-world
https://github.com/bregman-arie/flask-hello-world
```

`git clone https://github.com/bregman-arie/node-hello-world`

2. Напишите Dockerfile для сборки образа приложения. Базовый образ можно выбрать любой.

```
FROM alpine
LABEL maintainer="your name/email"
RUN apk add --update nodejs npm
COPY . /src
WORKDIR /src
RUN npm install
EXPOSE 3000
ENTRYPOINT ["node", "./app.js"]
```

3. Соберите образ по этому Dockerfile:

`docker image build -t web_app:latest .`

4. Убедитесь, что образ существует:

`docker image ls`

5. Необязательно: отправьте образ в реестр.

```
docker login
docker image tag web_app:latest <your username>/web_app:latest
# Verify with "docker image ls"
docker image push <your username>/web_app:latest
```

6. Запустите приложение:

```
docker container run -d -p 80:3000 web_app:latest
```

7. Убедитесь, что приложение работает:

```
docker container ls
docker logs <container ID/name>
# In the browser, go to 127.0.0.1:80
```
