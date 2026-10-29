<a id="multi-stage-builds"></a>
## Многоэтапная сборка

<a id="objective"></a>
### Цель

Разобраться в многоэтапной сборке образов.

<a id="instructions"></a>
### Инструкции

1. Не собирая образ и не запуская контейнеры, преобразуйте следующий Dockerfile в многоэтапный:

```
FROM nginx
RUN apt-get update \
 && apt-get install -y curl python build-essential \
 && apt-get install -y nodejs \
 && apt-get clean -y
RUN mkdir -p /my_app
ADD ./config/nginx/docker.conf /etc/nginx/nginx.conf
ADD ./config/nginx/k8s.conf /etc/nginx/nginx.conf.k8s
ADD app/ /my_cool_app
WORKDIR /my_cool_app
RUN npm install -g ember-cli
RUN npm install -g bower
RUN apt-get update && apt-get install -y git \
 && npm install \
 && bower install \
RUN ember build — environment=prod
CMD [ “/root/nginx-app.sh”, “nginx”, “-g”, “daemon off;” ]
```

2. Каковы преимущества многоэтапной сборки?

<a id="solution"></a>
### Решение

1. Один из вариантов решения; обратите внимание на перенос приложения с первого этапа:

```
FROM node:6
RUN mkdir -p /my_cool_app
RUN npm install -g ember-cli
RUN npm install -g bower
WORKDIR /my_cool_app
RUN npm install
ADD app/ /my_cool_app
RUN bower install
RUN ember build — environment=prod

FROM nginx
RUN mkdir -p /my_cool_app
ADD ./config/nginx/docker.conf /etc/nginx/nginx.conf
ADD ./config/nginx/k8s.conf /etc/nginx/nginx.conf.k8s
# Copy build artifacts from the first stage
COPY — from=0 /my_cool_app/dist /my_cool_app/dist
WORKDIR /my_cool_app
CMD [ “/root/nginx-app.sh”, “nginx”, “-g”, “daemon off;” ]
```

2. Многоэтапная сборка позволяет получать меньшие образы, разделяя процесс сборки на этапы. Итоговый образ содержит приложение и необходимые для его работы компоненты, но не инструменты сборки.
