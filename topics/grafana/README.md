## Grafana

<details>
<summary>Что такое Grafana?</summary><br><b>

[Документация Grafana](https://grafana.com/docs/grafana/latest/introduction): Grafana — комплекс средств наблюдаемости для мониторинга и анализа метрик, журналов и трассировок. Она позволяет запрашивать и визуализировать данные, настраивать оповещения и разбираться в данных независимо от места их хранения. Создавайте панели мониторинга, исследуйте данные и делитесь результатами с командой, чтобы принимать решения на основе данных.
</b></details>

<details>
<summary>Что такое Grafana Cloud?</summary><br><b>

[Grafana Cloud](https://grafana.com/products/cloud/) — версия Grafana, предоставляемая как облачный сервис. Развёртыванием, администрированием и обслуживанием средств наблюдаемости занимается Grafana Labs. Доступны бесплатные и платные варианты. Можно отправлять данные из существующих источников, например Prometheus и Loki, и визуализировать временные ряды.
</b></details>

<details>
<summary>Что такое Grafana Enterprise?</summary><br><b>

[Grafana Enterprise](https://grafana.com/docs/grafana/latest/enterprise/#enterprise-plugins) — коммерческая версия Grafana с корпоративными возможностями, включая плагины источников данных Enterprise и встроенные средства совместной работы. В неё входят поддержка и обучение от команды Grafana.
</b></details>

<details>
<summary>Какой HTTP-порт Grafana использует по умолчанию?</summary><br><b>

[Начало работы с Grafana](https://grafana.com/docs/grafana/latest/fundamentals/getting-started/): по умолчанию Grafana работает на порту 3000.
</b></details>

<details>
<summary>Как сделать использование HTTPS обязательным?</summary><br><b>

Для прямого TLS настройте `[server]`: `protocol = https`, `cert_file` и `cert_key` с путями к сертификату и приватному ключу, доступным процессу Grafana. Перезапустите сервер. Смена протокола сама по себе не создаёт HTTP→HTTPS redirect на отдельном порту.

В варианте с reverse proxy TLS завершается на нём: настройте сертификат, перенаправление HTTP на HTTPS и корректный внешний `root_url` Grafana. Ограничьте прямой доступ к внутреннему HTTP-порту, иначе HTTPS можно обойти. Проверьте цепочку доверия, имя хоста, проксирование WebSocket и итоговый доступ из браузера.

[Настройки Grafana](https://grafana.com/docs/grafana/latest/setup-grafana/configure-grafana/).
</b></details>

<details>
<summary>Как устанавливать плагины Grafana?</summary><br><b>

[Установка плагинов и CLI](https://grafana.com/docs/grafana/latest/administration/cli/): откройте [каталог плагинов Grafana](https://grafana.com/grafana/plugins/), выберите нужный плагин и перейдите на вкладку установки. Способ установки зависит от размещения сервера:

- Grafana Cloud: в поле **For** на вкладке установки выберите организацию, для которой устанавливается плагин, если вы состоите в нескольких организациях. Нажмите **Install plugin**. Сервис автоматически установит плагин в ваш экземпляр Grafana. Чтобы увидеть его, может потребоваться выйти из учётной записи и войти снова.
- Локальная Grafana: используйте CLI для просмотра доступных плагинов и их установки.

```
grafana cli plugins list-remote
grafana cli plugins install <plugin-id>
```

Также можно скачать архив плагина со вкладки установки и распаковать его в каталог плагинов. Путь к этому каталогу указан в файле конфигурации.

```
 unzip my-plugin-0.2.0.zip -d YOUR_PLUGIN_DIR/my-plugin
```
</b></details>

<details>
<summary>Что такое источник данных (Data source)?</summary><br><b>

[Документация Grafana](https://grafana.com/docs/grafana/latest/datasources/): источник данных — система хранения, из которой Grafana получает данные. Популярные примеры: Prometheus, InfluxDB, Loki и AWS CloudWatch.
</b></details>

<details>
<summary>Что такое конфигурация по умолчанию?</summary><br><b>

[Документация Grafana](https://grafana.com/docs/grafana/latest/administration/configuration/): конфигурация по умолчанию содержит стандартные настройки Grafana. Расположение файлов зависит от операционной системы. Переменная $WORKING_DIR обозначает рабочий каталог Grafana.

- Windows: `$WORKING_DIR/conf/defaults.ini`
- Linux: `/etc/grafana/grafana.ini`
- macOS: `/usr/local/etc/grafana/grafana.ini`

> Примечание к переводу: в оригинале здесь перечислены как файл стандартных значений, так и файлы пользовательской конфигурации. Это разные категории файлов.
</b></details>

<details>
<summary>Как задать пользовательскую конфигурацию Grafana?</summary><br><b>

[Документация Grafana](https://grafana.com/docs/grafana/latest/administration/configuration/): настройки можно переопределить в пользовательском файле конфигурации или через переменные окружения. Способ зависит от среды:

- Windows: рядом с defaults.ini находится файл `sample.ini`. Скопируйте его под именем `custom.ini` и раскомментируйте настройки, которые хотите изменить.
- Linux: отредактируйте `/etc/grafana/grafana.ini`.
- macOS: создайте `custom.ini` в каталоге conf. Для установки через Homebrew в оригинале также предлагается редактировать `conf/defaults.ini`.
- Docker: переопределяйте настройки через переменные окружения. Например, имя экземпляра: `export GF_DEFAULT_INSTANCE_NAME=my-instance`.

> Примечание к переводу: указания по путям и редактированию defaults.ini перенесены из оригинала; перед применением следует сверить их с документацией установленной версии.
</b></details>

<details>
<summary>Какие способы внешней аутентификации поддерживаются изначально?</summary><br><b>

[Документация Grafana](https://grafana.com/docs/grafana/latest/auth/overview/): Grafana Auth — встроенная система аутентификации. По умолчанию включена аутентификация по паролю.

> Примечание к переводу: ответ в оригинале описывает встроенную аутентификацию, но не перечисляет способы внешней аутентификации.
</b></details>

<details>
<summary>Как импортировать панель мониторинга в Grafana?</summary><br><b>

[Импорт панелей](https://grafana.com/docs/grafana/latest/dashboards/export-import/): импорт выполняется через интерфейс Grafana. Нажмите значок **+** на боковой панели, затем **Import**. Доступны следующие варианты:

- Загрузить JSON-файл панели, экспортированный из Grafana или полученный через [HTTP API](https://grafana.com/docs/grafana/latest/http_api/dashboard/#create-update-dashboard).
- Вставить URL панели из [каталога Grafana Dashboards](https://grafana.com/grafana/dashboards/) либо её уникальный идентификатор.
- Вставить JSON-описание панели в соответствующее поле.

Затем нажмите **Load**.
</b></details>

<details>
<summary>В каком формате хранятся панели мониторинга?</summary><br><b>

[Документация Grafana](https://grafana.com/docs/grafana/latest/dashboards/json-model/): панели мониторинга представлены объектами в JSON-файлах. В них хранятся свойства панели мониторинга, метаданные её отдельных панелей и переменные.
</b></details>

<details>
<summary>Как поделиться панелью мониторинга с командой?</summary><br><b>

[Документация Grafana](https://grafana.com/docs/grafana/latest/sharing/share-dashboard/): откройте свой экземпляр Grafana и нажмите значок общего доступа в верхней панели навигации. В описанном интерфейсе появятся три вкладки; по умолчанию открыта вкладка ссылки.

- Прямая ссылка: нажмите **Copy** и отправьте ссылку пользователю Grafana. У него должны быть права на просмотр, например предоставленные через членство в команде.
- Публичный снимок: выберите **Local snapshot**, чтобы опубликовать снимок в своём экземпляре Grafana, либо **Publish to snapshots.raintank.io**, чтобы разместить его во внешнем бесплатном сервисе публикации снимков.

Можно задать срок действия снимка и время ожидания сбора метрик для него.
</b></details>

<details>
<summary>Как организовать панели мониторинга и пользователей в Grafana?</summary><br><b>

[Рекомендации Grafana Labs](https://grafana.com/blog/2022/03/14/how-to-best-organize-your-teams-and-resources-in-grafana/): используйте папки для группировки панелей мониторинга, библиотечных панелей и оповещений. Пользователей объединяйте в команды, чтобы назначать права группе.

- [Папки](https://grafana.com/docs/grafana/latest/dashboards/dashboard_folders/): нажмите **+** на боковой панели, затем **Create folder**. Укажите уникальное имя папки и нажмите **Create**.
- [Команды и пользователи](https://grafana.com/tutorials/create-users-and-teams/): в оригинале для создания команд указано требование прав администратора сервера, после чего приведены шаги создания пользователя:

1. Нажмите значок администратора сервера в виде щита на боковой панели. На вкладке **Users** нажмите **New user**.
2. Введите имя, электронную почту, имя пользователя и пароль. Пользователь сможет изменить пароль позже.
3. Нажмите **Create**, чтобы создать учётную запись.

> Примечание к переводу: эти шаги создают пользователя, а не команду; несоответствие присутствует в оригинале.
</b></details>

<details>
<summary>Как создать оповещение (Alert)?</summary><br><b>

Используйте [Grafana-managed alert rules](https://grafana.com/docs/grafana/latest/alerting/alerting-rules/create-grafana-managed-rule/). Старый workflow через вкладку Alert панели не является действующим общим способом создания правил.

1. Откройте **Alerts & IRM → Alert rules → New alert rule** (названия меню зависят от версии).
2. Выберите источник данных, поддерживающий alerting, задайте запрос, преобразование результата и порог условия; проверьте результат через Preview.
3. Укажите папку, группу и интервал оценки, период ожидания до срабатывания. Настройте поведение при No Data и ошибках запроса.
4. Добавьте labels/annotations и маршрутизацию в contact point напрямую либо через notification policy.
5. Сохраните правило и проверьте тестовую доставку и переходы состояния. Правило может работать независимо от dashboard; связь с панелью необязательна.

Для источников Prometheus/Mimir/Loki различайте правила, вычисляемые Grafana, и data source-managed rules: место выполнения и способ управления ими отличаются.
</b></details>
