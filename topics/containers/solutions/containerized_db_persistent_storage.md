<a id="containerized-db-with-persistent-storage"></a>
# База данных в контейнере с постоянным хранилищем

1. Запустите контейнер с любой базой данных, например MySQL, PostgreSQL или MongoDB.
   1. Храните данные базы в каталоге хоста, смонтированном в контейнер, вместо хранения в файловом слое контейнера.
   2. Объясните преимущества хранения данных на хосте по сравнению с хранением внутри контейнера.
2. Убедитесь, что контейнер работает.

<a id="solution"></a>
## Решение

```
# Create the directory for the DB on host
mkdir -pv ~/local/mysql
sudo semanage fcontext -a -t container_file_t '/home/USERNAME/local/mysql(/.*)?'
sudo restorecon -R /home/USERNAME/local/mysql

# Run the container
podman run --name mysql -e MYSQL_USER=mario -e MYSQL_PASSWORD=tooManyMushrooms -e MYSQL_DATABASE=university -e MYSQL_ROOT_PASSWORD=MushroomsPizza -d mysql -v /home/USERNAME/local/mysql:/var/lib/mysql/db

# Verify it's running
podman ps
```

Хранение данных на хосте позволяет сохранить содержимое базы при удалении контейнера или освобождении его файлового слоя.
