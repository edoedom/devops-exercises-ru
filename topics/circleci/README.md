<a id="circle-ci"></a>
# CircleCI

<a id="circle-ci-questions"></a>
## Вопросы по CircleCI

<a id="circle-ci-101"></a>
### Основы CircleCI

<details>
<summary>Что такое CircleCI?</summary><br><b>

[CircleCI](https://circleci.com) — платформа непрерывной интеграции и доставки, которую можно использовать для внедрения практик DevOps.
</b></details>

<details>
<summary>Какие преимущества есть у CircleCI?</summary><br><b>

[Документация CircleCI](https://circleci.com/docs/about-circleci) перечисляет следующие возможности:

* Подключение по SSH к заданию для диагностики проблем сборки.
* Параллельное выполнение, настраиваемое в .circleci/config.yml.
* Кеширование данных для повторного использования между заданиями.
* Собственные исполнители для нестандартных платформ.
* Ресурсы Arm для исполнителя machine.
* Переиспользуемые пакеты конфигурации orbs для интеграций.
* Готовые образы Docker для различных языков.
* API для получения сведений о заданиях и рабочих процессах.
* CLI для локальной работы с расширенными инструментами.
* Обнаружение нестабильных тестов с помощью Test Insights.
</b></details>

<details>
<summary>Объясните понятия Pipeline, Workflow, Jobs и Steps.</summary><br><b>

* Pipeline: полная конфигурация процесса CI/CD. В оригинале здесь указан файл .circleci/config.yaml; ниже в том же исходнике используется .circleci/config.yml.
* Workflow: организация выполнения заданий и их зависимостей, особенно когда заданий несколько.
* Jobs: задания, состоящие из одного или нескольких шагов CI/CD.
* Steps: отдельные действия и выполняемые команды.
</b></details>

<details>
<summary>Что такое Orb?</summary><br><b>

[Документация CircleCI](https://circleci.com/developer/orbs): Orb — пакет конфигурации CircleCI, которым можно делиться и который упрощает настройку сборок.

Orbs могут публиковаться в общем реестре или быть закрытыми в рамках организации.
</b></details>

<a id="circle-ci-hands-on-101"></a>
### Практика CircleCI: основы

<details>
<summary>Где в проекте определяется конвейер CircleCI?</summary><br><b>

`.circleci/config.yml`
</b></details>

<details>
<summary>Объясните следующий файл конфигурации.

```
version: 2.1

jobs:
  say-hello:
    docker:
      - image: cimg/base:stable
    steps:
      - checkout
      - run:
          name: "Say hello"
          command: "echo Hello, World!"
workflows:
  say-hello-workflow:
    jobs:
      - say-hello
```
</summary><br><b>

Конфигурация создаёт одно задание: оно получает код проекта и выполняет `echo Hello, World!`. Задание работает в контейнере из образа `cimg/base:stable`.
</b></details>
