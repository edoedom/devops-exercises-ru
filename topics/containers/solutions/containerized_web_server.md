<a id="containerized-web-server"></a>
# Веб-сервер в контейнере

1. Запустите веб-сервер в контейнере в фоновом режиме и сопоставьте его порт 8080 с портом на хосте.
2. Проверьте, что порт контейнера 8080 опубликован.
3. Обратитесь к веб-серверу с хоста.
4. Теперь запустите то же приложение, сопоставив его порт с портом 8080 на хосте.

<a id="solution"></a>
## Решение

```
$ podman run -d -p 8080 httpd # run the container and bind the port 8080 to a local port
$ podman port -l 8080 # show to which local port the port 8080 on the container, binds to
0.0.0.0:41203
$ curl http://0.0.0.0:41203 # use the port from the output of the previous command

!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
	<head>
		<title>Test Page for the HTTP Server on Red Hat Enterprise Linux</title>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />

$ podman run -d -p 8080:8080 httpd
```
