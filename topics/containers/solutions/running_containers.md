<a id="running-containers"></a>
## Запуск контейнеров

<a id="objective"></a>
### Цель

Научиться запускать, останавливать и удалять контейнеры.

<a id="requirements"></a>
### Требования

Убедитесь, что установлен Podman, Docker или другой движок контейнеров.

<a id="instructions"></a>
### Инструкции

1. Запустите контейнер из nginx:latest: `podman container run nginx:latest`.
2. Проверьте, что он работает: `podman container ls`.
3. Запустите ещё один контейнер из ubuntu:latest и подключитесь к его терминалу: `podman container run -it ubuntu:latest /bin/bash`.
4. Снова выведите список: `podman container ls`. В этом примере должны работать два контейнера.
5. Остановите контейнеры. Внимание: `podman stop $(podman container ls -q)` остановит все работающие контейнеры хоста. Для отдельного контейнера используйте `podman stop [container id/name]`.
6. Удалите контейнеры. Внимание: `podman rm $(podman container ls -q -a)` попытается удалить все контейнеры хоста, включая не относящиеся к упражнению. Для отдельного контейнера используйте `podman rm [container id/name]`.
