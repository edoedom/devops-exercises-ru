<a id="containerized-db"></a>
# База данных в контейнере

1. Запустите контейнер с любой базой данных, например MySQL, PostgreSQL или MongoDB.
2. Убедитесь, что контейнер работает.
3. Подключитесь к контейнеру и создайте таблицу для студентов или коллекцию, если это соответствует выбранной СУБД.
4. Добавьте строку или документ с данными студента.
5. Проверьте, что данные добавлены.

<a id="solution"></a>
## Решение

```
# Run the container
podman run --name mysql -e MYSQL_USER=mario -e MYSQL_PASSWORD=tooManyMushrooms -e MYSQL_DATABASE=university -e MYSQL_ROOT_PASSWORD=MushroomsPizza -d mysql

# Verify it's running
podman ps

# Add student row to the database
podman exec -it mysql /bin/bash
mysql -u root
use university;
CREATE TABLE Students (id int NOT NULL, name varchar(255) DEFAULT NULL, PRIMARY KEY (id));
insert into Projects (id, name) values (1,'Luigi');
select * from Students;
```
