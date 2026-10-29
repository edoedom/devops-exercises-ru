<a id="create-images-on-the-fly"></a>
# Создание образа из работающего контейнера

<a id="requirements"></a>
## Требования

Нужен хотя бы один локальный образ. Проверьте это командой `podman image ls`.<br>
Если образов нет, выполните `podman pull nginx:alpine`.

<a id="objectives"></a>
## Задание

1. Запустите контейнер из образа веб-сервера, например httpd или nginx:
   * Сопоставьте порт контейнера 80 с портом хоста 80.
   * Используйте фоновый режим.
   * Имя контейнера: nginx_container.
2. Убедитесь, что веб-сервер работает и доступен.
3. Создайте HTML-файл со следующим содержимым и скопируйте его в контейнер по пути, где он будет использоваться как индексная страница:

```
<html>
<head>
<title>It's a me</title>
</head>
<body>
<h1>Mario</h1>
</body>
```

4. Создайте образ из работающего контейнера с именем nginx_mario.
5. Назначьте образу тег mario.
6. Удалите исходный контейнер и убедитесь, что он удалён.
7. Запустите новый контейнер из созданного образа с теми же параметрами, что и исходный.
8. Выполните `curl 127.0.0.1:80`. Что вы видите?
9. Выполните `podman diff` для нового образа и объясните вывод.

> Примечание к переводу: в пункте 5 исходника ошибочно говорится о теге контейнера вместо образа, а в пункте 6 имя контейнера меняется с nginx_container на container_nginx. В переводе эти несоответствия устранены.

<a id="solution"></a>
## Решение

```
# Run the container
podman run --name nginx_container -d -p 80:80 nginx:alpine

# Verify web server is running
curl 127.0.0.1:80
    #  <!DOCTYPE html>
    #  <html>
    #  <head>
    #  <title>Welcome to nginx!</title>

# Create index.html file
cat <<EOT >>index.html
<html>
<head>
<title>It's a me</title>
</head>
<body>
<h1>Mario</h1>
</body>
EOT

# Copy index.html to the container
podman cp index.html nginx_container:/usr/share/nginx/html/index.html

# Create a new image out of the running container
podman commit nginx_container nginx_mario

# Tag the image
podman image ls
# localhost/nginx_mario     latest   dc7ed2343521   52 seconds ago   25 MB
podman tag dc7ed2343521 mario

# Remove the container
podman stop nginx_container
podman rm nginx_container
podman ps -a # no container 'nginx_container'

# Create a container out of the image 
podman run -d -p 80:80 nginx_mario

# Check the container created from the new image
curl 127.0.0.1:80
#<html>
#<head>
#<title>It's a me</title>
#</head>
#<body>
#<h1>Mario</h1>
#</body>

# Run diff
podman diff nginx_mario

C /etc
C /etc/nginx/conf.d
C /etc/nginx/conf.d/default.conf
A /run/nginx.pid
C /usr/share/nginx/html
C /usr/share/nginx/html/index.html
C /var/cache/nginx
C /var
C /var/cache
A /var/cache/nginx/client_temp
A /var/cache/nginx/fastcgi_temp
A /var/cache/nginx/proxy_temp
A /var/cache/nginx/scgi_temp
A /var/cache/nginx/uwsgi_temp

# We've set new index.html which explains why it's changed (C)
# We also created the image while the web server is running, which explains all the files created under /var
```
