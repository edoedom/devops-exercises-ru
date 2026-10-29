<a id="ci-for-open-source-project"></a>
## CI для проекта с открытым исходным кодом

1. Выберите проект на GitHub и создайте его форк.
2. Создайте для форка конвейер CI.
3. Добавьте проверки, подходящие проекту. Например:
   * Для Python-проекта — проверку соответствия PEP 8.
   * Если есть модульные тесты — их запуск в составе CI.
4. В отдельном файле опишите проверки и объясните, почему выбрали их. Можно также описать возникшие вопросы, трудности и принятые решения.

<a id="bonus"></a>
### Дополнительное задание

Упакуйте приложение в контейнер с помощью любого движка, например Docker или Podman.<br>
После успешного запуска предложите Dockerfile исходному проекту. Учитывайте, что сопровождающему проекта такое изменение может быть не нужно.

<a id="suggestions-for-projects"></a>
### Примеры проектов

В оригинале следующие проекты перечислены как проекты без CI на момент составления списка.

Примечание автора: все проекты, кроме первого, найдены скриптом по определённым параметрам.

* [Этот репозиторий](https://github.com/bregman-arie/devops-exercises) — автор предлагает помочь с настройкой CI.
* [image retrieval platform](https://github.com/skx6/image_retrieval_platform)
* [FollowSpot](https://github.com/jenbrissman/FollowSpot)
* [Pyrin](https://github.com/mononobi/pyrin)
* [food-detection-yolov5](https://github.com/lannguyen0910/food-detection-yolov5)
* [Lifely](https://github.com/sagnik1511/Lifely)
