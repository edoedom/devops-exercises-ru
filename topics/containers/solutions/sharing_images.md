<a id="sharing-images"></a>
# Передача образов

<a id="requirements"></a>
## Требования

Нужен хотя бы один локальный образ. Проверьте это командой `podman image ls`.<br>
Если образов нет, выполните `podman pull httpd`.

<a id="objectives"></a>
## Задание

1. Выберите образ и сохраните его в архив.
2. Проверьте размер архива. Отличается ли он от размера образа? Если да, в чём разница? Если нет, почему?
3. Скопируйте архив на удалённый узел.
4. Загрузите образ из архива.
5. Убедитесь, что образ загружен и присутствует на удалённом узле.

<a id="solution"></a>
## Решение

```
# Save image as an archive
podman save -o httpd.tar httpd

# Check archive and image sizes
du -sh httpd.tar # output: 143MB
podman image ls | grep httpd # output: 149MB
# The archive is obviously smaller than the image itself (6MB difference)

# Copy the archive to a remote host
rsync -azc httpd.tar USER@REMOTE_HOST_FQDN:/tmp/

# Load the image
podman load -i /tmp/httpd.tar

# Verify it exists on the system after loading
podman image ls
```
