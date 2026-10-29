<a id="run-forest-run"></a>
## Беги, Форрест, беги!

<a id="objective"></a>
### Цель

Разобраться в политиках перезапуска контейнеров и научиться ими пользоваться.

<a id="requirements"></a>
### Требования

Убедитесь, что Docker установлен и служба запущена.

```
# Fedora/RHEL/CentOS
rpm -qa | grep docker
systemctl status docker
```

<a id="instructions"></a>
### Инструкции

1. Запустите контейнер с образом alpine, именем forest, политикой always и командой sleep 15:

`docker run --restart always --name forest alpine sleep 15`

2. Выполните `docker container ls`. Работает ли контейнер? А через 15 секунд? Почему?

После завершения `sleep 15` Docker снова запускает тот же контейнер, поскольку задана политика always.

3. Как остановить контейнер?

При ручной остановке командой `docker container stop` немедленный автоматический перезапуск не выполняется.

4. Удалите контейнер:

```
docker container stop forest
docker container rm forest
```

5. Запустите его снова с `sleep 600` и убедитесь, что он работает:

```
docker run --restart always --name forest alpine sleep 600
docker container ls
```

6. Перезапустите службу Docker. Работает ли контейнер? Почему?

```
sudo systemctl restart docker
```

Да: политика `always` обеспечивает запуск контейнера после перезапуска службы Docker.

7. Измените политику на `unless-stopped`:

`docker update --restart unless-stopped forest`

8. Остановите контейнер:

`docker container stop forest`

9. Снова перезапустите службу Docker. Работает ли контейнер?

```
sudo systemctl restart docker
```

Нет. При `unless-stopped` контейнер, который был явно остановлен до перезапуска службы, остаётся остановленным.
