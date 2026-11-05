<a id="linux"></a>
# Linux

<a id="linux-master-application"></a>
## Приложение Linux Master

Полностью бесплатное приложение для проверки знаний Linux.
Примечание: разработано владельцем репозитория.

<a href="https://play.google.com/store/apps/details?id=com.codingshell.linuxmaster"><img src="../../images/linux_master.jpeg"/></a>

- [Linux](#linux)
  - [Приложение Linux Master](#linux-master-application)
  - [Упражнения Linux](#linux-exercises)
    - [Основы](#basics)
    - [Разное](#misc)
  - [Вопросы Linux](#linux-questions)
    - [Основы Linux](#linux-101)
    - [Перенаправление ввода-вывода](#io-redirection)
    - [Стандарт иерархии файловой системы](#filesystem-hierarchy-standard)
    - [Права доступа](#permissions)
    - [Практические ситуации](#scenarios)
    - [Systemd](#systemd)
    - [Диагностика и отладка](#troubleshooting-and-debugging)
      - [Практические ситуации](#scenarios-1)
    - [Ядро](#kernel)
    - [SSH](#ssh)
    - [Шаблоны имён и подстановочные символы](#globbing--wildcards)
    - [Процесс загрузки](#boot-process)
    - [Диски и файловые системы](#disk-and-filesystem)
    - [Анализ производительности](#performance-analysis)
    - [Процессы](#processes)
    - [Безопасность](#security)
    - [Сеть](#networking)
    - [DNS](#dns)
    - [Пакеты](#packaging)
    - [DNF](#dnf)
    - [Приложения и сервисы](#applications-and-services)
    - [Пользователи и группы](#users-and-groups)
    - [Оборудование](#hardware)
    - [Пространства имён](#namespaces)
    - [Виртуализация](#virtualization)
    - [AWK](#awk)
    - [Системные вызовы](#system-calls)
    - [Файловые системы и файлы](#filesystem--files)
    - [Расширенные сетевые вопросы](#advanced-networking)
    - [Память](#memory)
    - [Дистрибутивы](#distributions)
    - [Sed](#sed)
    - [Разное](#misc-1)

<a id="linux-exercises"></a>
## Упражнения Linux

<a id="basics"></a>
### Основы

|Название|Тема|Цель и инструкции|Решение|Комментарии|
|--------|--------|------|----|----|
|Навигация|cd, pwd|[Задание](exercises/navigation/README.md)|[Решение](exercises/navigation/solution.md)
|Создание и удаление|touch, rm, mkdir|[Задание](exercises/create_remove/README.md)|[Решение](exercises/create_remove/solution.md)
|Копирование|touch, cp, ls|[Задание](exercises/copy/README.md)|[Решение](exercises/copy/solution.md)

<a id="misc"></a>
### Разное

|Название|Тема|Цель и инструкции|Решение|Комментарии|
|--------|--------|------|----|----|
|Подсчёт уникальных значений||[Задание](exercises/uniqe_count/README.md)|[Решение](exercises/uniqe_count/solution.md)

<a id="linux-questions"></a>
## Вопросы Linux

<a id="linux-101"></a>
### Основы Linux

<details>
<summary>Что такое Linux?</summary><br><b>

[Википедия](https://en.wikipedia.org/wiki/Linux): семейство Unix-подобных операционных систем с открытым исходным кодом на основе ядра Linux, впервые опубликованного Линусом Торвальдсом 17 сентября 1991 года. Обычно Linux распространяется в составе дистрибутива.

[Red Hat](https://www.redhat.com/en/topics/linux/what-is-linux): Linux — открытая ОС, которая управляет оборудованием и ресурсами компьютера: процессором, памятью и хранилищем. ОС связывает приложения с физическими ресурсами.

</b></details>

<details>
<summary>Объясните назначение каждой команды и приведите пример использования:

  * touch
  * ls
  * rm
  * cat
  * cp
  * mkdir
  * pwd
  * cd
</summary><br><b>

  * `touch` — обновляет временные метки; при отсутствии файла обычно создаёт его.
  * `ls` — выводит файлы и каталоги.
  * `rm` — удаляет файлы и каталоги.
  * `cat` — читает и объединяет содержимое файлов; с перенаправлением позволяет записать результат в файл.
  * `cp` — копирует файлы и каталоги.
  * `mkdir` — создаёт каталоги.
  * `pwd` — выводит текущий рабочий каталог.
  * `cd` — меняет рабочий каталог.
</b></details>

<details>
<summary>Что делают следующие команды?

  * cd /
  * cd ~
  * cd
  * cd ..
  * cd .
  * cd -
</summary><br><b>

  * `cd /` — перейти в корневой каталог.
  * `cd ~` — перейти в домашний каталог.
  * `cd` — перейти в домашний каталог.
  * `cd ..` — перейти в родительский каталог.
  * `cd .` — остаться в текущем каталоге.
  * `cd -` — вернуться в предыдущий рабочий каталог.
</b></details>

<details>
<summary>Некоторые команды поддерживают -r или -R. Что означает этот параметр? Приведите пример.</summary><br><b>

Для ряда команд он включает рекурсивную обработку. Например, `ls -R` выводит содержимое всего дерева каталогов:

/dir1/
  dir2/
    file1
    file2
  dir3/
    file3

Для этого дерева: `ls -R /dir1`.
</b></details>

<details>
<summary>Объясните поля вывода ls -l.</summary><br><b>
Это подробный список. Слева направо:

* Тип и права, число жёстких ссылок, владелец, группа, размер, время последнего изменения и имя файла или каталога.
</b></details>

<details>
<summary>Что такое скрытые файлы и каталоги? Как их вывести?</summary><br><b>

Имена, начинающиеся с точки, обычный `ls` скрывает. Пример — `.bashrc` с настройками оболочки. Для вывода используйте `ls -a`. Уточнение: `KUBECONFIG` обычно обозначает переменную окружения, а не стандартный файл `.KUBECONFIG`.
</b></details>

<details>
<summary>Что делают операторы > и < с вводом и выводом программы?</summary><br><b>
`<` направляет файл в стандартный ввод, а `>` записывает стандартный вывод в файл с его перезаписью.

`myProgram < input.txt > executionOutput.txt`
</b></details>

<details>
<summary>Объясните назначение каждой команды и приведите пример использования:

  * sed
  * grep
  * cut
  * awk
</summary><br><b>

  - `sed` — потоковый редактор. Например, замена слова: `sed -i 's/salad/burger/g' FILE`.
  - `grep` — поиск строк по тексту или шаблону:
    - Строки со словом: `grep 'word' file.md`.
    - Число совпавших строк: `grep -c 'This is a string' file.md`. Это не число всех вхождений внутри строк.
  - `cut` — выделение частей каждой строки:
    - Синтаксис: `cut OPTION [FILE]`.
    - Первые два байта: `cut -b 1-2 file.md`; для слова `word` результат — `wo`.
  - `awk` — язык обработки текста и извлечения данных, позволяющий преобразовывать строки файла.
    - Синтаксис: `awk [OPTIONS] [FILTER] [FILE]`.
Пример: `awk -F ',' '{print $1}' file.csv` выводит первое поле каждой строки простого CSV. Полноценный разбор CSV с кавычками требует дополнительных средств.
</b></details>

<details>
<summary>Как переименовать файл или каталог?</summary><br><b>

Командой `mv`.
</b></details>

<details>
<summary>Какие команды вы используете в следующих случаях?

  * Удалить каталог с файлами
  * Показать содержимое файла
  * Предоставить всем доступ к /tmp/x
  * Перейти в домашний каталог
  * Заменить все good на great в /tmp/y</summary><br><b>

  - `rm -rf dir`
   - `cat` или `less`
  - `chmod 777 /tmp/x`
  - `cd ~`
  - `sed -i s/good/great/g /tmp/y`
</b></details>

<details>
<summary>Как узнать путь к команде?</summary><br><b>

  * whereis
  * which
</b></details>

<details>
<summary>Чем отличаются эти команды? Совпадёт ли вывод?

```
echo hello world
echo "hello world"
```
</summary><br><b>

В первом случае `echo` получает два аргумента, во втором — одну строку `hello world`. Вывод совпадёт.
</b></details>

<details>
<summary>Что такое конвейер и как его создать?</summary><br><b>

Конвейер передаёт стандартный вывод одной команды на стандартный ввод другой: `cat /etc/services | wc -l`.
</b></details>

<details>
<summary>Исправьте команды:

  * sed "s/1/2/g' /tmp/myFile
  * find . -iname \*.yaml -exec sed -i "s/1/2/g" {} ;
</summary><br><b>

```
sed 's/1/2/g' /tmp/myFile  # sed "s/1/2/g" is also fine
find . -iname "*.yaml" -exec sed -i "s/1/2/g" {} \;
```
</b></details>

<details>
<summary>Как посмотреть ранее выполненные команды?</summary><br><b>

Использовать `history` или файл `.bash_history`.
  * Стрелка вверх также позволяет просматривать предыдущие команды.
</b></details>

<details>
<summary>При запуске df выводится command not found. Каковы причины и решение?</summary><br><b>
</b>
<p><b>
Возможно, изменён `$PATH` и в нём отсутствует каталог команды, например `/bin` или `/usr/bin`.
Причиной могут быть неверные изменения `.bash_profile` или других файлов настройки оболочки.
В таком случае исправьте `$PATH`.

Варианты:

1. Добавить нужный каталог, например `PATH="$PATH:/usr/bin"`. В исходнике был ошибочный путь `/user/bin`.
2. Восстановить окружение из резервной копии.
3. Сравнить с настройками `$PATH` по умолчанию для дистрибутива.

Это не единственная возможная причина: влияют настройки оболочки,
права, отсутствие программы, ошибки установки или сборки. Универсального ответа нет.
</b>
</p>
</details>

<details>
<summary>Как запускать задачи по расписанию?</summary><br><b>

Для повторяющихся задач используется cron; `at` обычно планирует однократный запуск.
Формат задания cron:

`*/30 * * * * bash myscript.sh` — запуск каждые 30 минут.

`<минута> <час> <день месяца> <месяц> <день недели> <команда>`

Редактирование таблицы заданий: `crontab -e`.

В системах с systemd можно использовать таймеры systemd.
</b></details>

<a name="questions-linux-redirection"></a>
<a id="io-redirection"></a>
### Перенаправление ввода-вывода

<details>
<summary>Объясните перенаправление ввода-вывода Linux.</summary><br><b>
Оно меняет стандартные источники ввода и назначения вывода программы: файлы, устройства или другие команды.

Примеры:
 * Перенаправление стандартного вывода stdout:
  <code>ls > filelist.txt</code>
* Перенаправление стандартных ошибок stderr:
  <code>ls /some/nonexistent/directory 2> error.txt</code>
* Добавление в конец файла:
  <code>echo "hello" >> myfile.txt</code>
* Перенаправление стандартного ввода stdin:
  <code>sort < unsorted.txt</code>
* Конвейер `|`:
  <code>ls | grep "\.txt$"</code>         
</b></details>

<details>
<summary>Покажите перенаправление stdout.</summary><br><b>

<code>ls > ls_output.txt</code>
</b></details>

<details>
<summary>Покажите перенаправление stderr.</summary><br><b>

<code>yippiekaiyay 2> ls_output.txt</code>
</b></details>

<details>
<summary>Покажите перенаправление stderr в stdout.</summary><br><b>

`command 2>&1`. Уточнение: приведённое в исходнике `yippiekaiyay &> file` направляет оба потока в файл.
</b></details>

<details>
<summary>Каков результат <code>yippiekaiyay 1>&2 die_hard</code>?</summary><br><b>

Если команды нет, сообщение примерно такое: `yippikaiyay: command not found...`.<br>
Файл `die_hard` не создаётся: это аргумент команды, а не назначение перенаправления.
</b></details>

<a name="questions-linux-fhs"></a>
<a id="filesystem-hierarchy-standard"></a>
### Стандарт иерархии файловой системы

<details>
<summary>Что означает / в стандарте FHS?</summary><br><b>

Корень файловой системы, начало дерева каталогов.
</b></details>

<details>
<summary>Что находится по следующим путям?

  - /bin, /sbin, /usr/bin и /usr/sbin
  - /etc
  - /home
  - /var
  - /tmp</summary><br><b>

  * Исполняемые файлы.
  * Конфигурационные файлы.
  * Домашние каталоги пользователей.
  * Изменяемые данные, например журналы.
  * Временные файлы.
</b></details>

<details>
<summary>Чем /tmp отличается от других каталогов?</summary><br><b>

Его содержимое может очищаться автоматически, в том числе при перезагрузке; конкретные правила зависят от системы.
</b></details>

<details>
<summary>Какие сведения доступны в /proc?</summary><br><b>
 
Информация о процессах, ядре и ресурсах системы; часть файлов служит интерфейсом управления параметрами ядра.
</b></details>

<details>
<summary>Чем /proc отличается от обычных файловых систем?</summary><br><b>
Это виртуальная файловая система, через которую ядро предоставляет информацию о процессах и системных ресурсах.
</b></details>

<details>
<summary>Верно ли, что создавать файлы в /proc может только root?</summary><br><b>

Неверно. Пользователи не создают там обычные файлы напрямую: записи формирует ядро в результате соответствующих операций.
</b></details>

<details>
<summary>Что содержит /proc/cmdline?</summary><br><b>

Командную строку параметров, переданных ядру при загрузке.
</b></details>

<details>
<summary>Где представлены устройства системы, например блочные?</summary><br><b>
  /dev
</b></details>

<a name="questions-linux-permissions"></a>
<a id="permissions"></a>
### Права доступа

<details>
<summary>Как изменить права файла?</summary><br><b>

Командой `chmod`.
</b></details>

<details>
<summary>Что означают следующие права?

  * 777
  * 644
  * 750</summary><br><b>

<pre>
777 — владельцу, группе и остальным доступны чтение (4), запись (2) и выполнение (1).
644 — владельцу чтение и запись (6), группе и остальным только чтение (4).
750 — владельцу все права (7), группе чтение и выполнение (5), остальным ничего (0).
</pre>
</b></details>

<details>
<summary>Что делает <code>chmod +x some_file</code>?</summary><br><b>
Добавляет право выполнения. Если класс пользователей не указан, при выборе затрагиваемых битов учитывается umask; для явного назначения всем используйте `a+x`.
</b></details>

<details>
<summary>Объясните setgid и setuid.</summary><br><b>

* setuid у исполняемого файла позволяет процессу получить эффективный UID владельца файла при запуске, с учётом ограничений системы.
* setgid у исполняемого файла аналогично задаёт эффективную группу владельца; у каталогов имеет особое значение для наследования группы.
</b></details>

<details>
<summary>Зачем нужен sticky bit?</summary><br><b>
На каталоге он ограничивает удаление и переименование файлов: обычно это может делать владелец файла, владелец каталога или привилегированный пользователь. Он не запрещает изменение содержимого файла при наличии права записи.
</b></details>

<details>
<summary>Что делают следующие команды?

  - chmod
  - chown
  - chgrp</summary><br><b>

  * `chmod` — меняет права доступа.
  * `chown` — меняет владельца файлов и каталогов.
  * `chgrp` — меняет группу объекта файловой системы.
</b></details>

<details>
<summary>Что такое sudo и как его настроить?</summary><br><b>
`sudo` позволяет выполнять команды с правами другого пользователя, обычно root, в соответствии с настроенной политикой.

Пакет есть во многих дистрибутивах. В Debian/Ubuntu при необходимости установите его через `apt-get install sudo` с административными правами. Правила обычно редактируют через `visudo`.

</b></details>

<details>
<summary>Верно ли, что для установки пакетов в систему нужны права root или sudo?</summary><br><b>

Верно.
</b></details>

<details>
<summary>Что такое ACL и когда они полезны?</summary><br><b>
Access Control Lists дают более точные права для отдельных пользователей и групп. Просмотр: `getfacl /absolute/file/path`; изменение: `setfacl -m` с нужной записью и путём.
  
</b></details>

<details>
<summary>Назовите минимум три причины, по которым не удаётся создать файл.</summary><br><b>

* Закончилось место.
* Закончились inode.
* Нет необходимых прав.
</b></details>

<details>
<summary>Пользователь выполнил <code>chmod -x $(which chmod)</code>. Как восстановить выполнение chmod?</summary><br><b>

Например, `sudo setfacl -m u::rx /usr/bin/chmod` возвращает чтение и выполнение владельцу файла. Затем владелец, обычно root, может восстановить нужные права через chmod. Уточнение: `u::rx` не означает выдачу прав всем пользователям; путь следует проверить.
</b></details>

<a name="questions-linux-scenarios"></a>
<a id="scenarios"></a>
### Практические ситуации

<details>
<summary>Как скопировать файл на удалённый Linux-хост?</summary><br><b>

Есть несколько способов; автор предпочитает `rsync`.
</b></details>

<details>
<summary>Как сгенерировать случайную строку?</summary><br><b>

Например, `cat /proc/sys/kernel/random/uuid`.
</b></details>

<details>
<summary>Как сгенерировать случайную строку из семи символов?</summary><br><b>

`mkpasswd -l 7`
</b></details>

<a name="questions-linux-systemd"></a>
<a id="systemd"></a>
### Systemd

<details>
<summary>Что такое systemd?</summary><br>
<b>
systemd — система инициализации и управления сервисами; её основной процесс работает как демон.

Демон — фоновая программа без постоянного непосредственного управления пользователем,
хотя пользователь может взаимодействовать с ней через соответствующие интерфейсы.

systemd управляет сервисами и процессами, зависимостями, журналом, блокировками действий и другими компонентами системы.

В упрощённой модели слоёв systemd находится над ядром Linux.<br>
Оборудование → ядро → демоны, системные библиотеки, графическая подсистема.
</b>
</details>

<details>
<summary>Как запустить или остановить сервис?</summary><br><b>

Запуск: `systemctl start <service name>`.
Остановка: `systemctl stop <service name>`.
</b></details>

<details>
<summary>Как проверить состояние сервиса?</summary><br><b>

`systemctl status <service name>`
</b></details>

<details>
<summary>Как посмотреть журналы в системе с systemd?</summary><br><b>

<code>journalctl</code>
</b></details>

<details>
<summary>Как оформить процесс или приложение как сервис?</summary><br><b>
Создать unit-файл `/etc/systemd/system/service-name.service` с параметрами запуска и управления сервисом. Подробности — <a href="https://medium.com/@benmorel/creating-a-linux-service-with-systemd-611b5c8b91d6">здесь</a>.
</b></details>

<a id="troubleshooting-and-debugging"></a>
### Диагностика и отладка

<details>
<summary>Где находятся системные журналы?</summary><br><b>

/var/log
</b></details>

<details>
<summary>Как следить за дописываемым содержимым файла?</summary><br><b>

tail -f <file_name>
</b></details>

<details>
<summary>Чем вы диагностируете сетевые проблемы?</summary><br><b>

`dstat -t` помогает сопоставлять активность системы, сети и дисков во времени.
`netstat -tnlaup` показывает слушающие порты и связанные процессы при достаточных правах.
`lsof -i -P` также помогает сопоставить сетевые соединения с процессами.
`ngrep -d any metafilter` ищет совпадения с шаблоном в содержимом пакетов.
`tcpdump` захватывает пакеты.
Wireshark анализирует сетевой трафик и предоставляет графический интерфейс.
</b></details>

<details>
<summary>Чем вы диагностируете проблемы дисков и файловых систем?</summary><br><b>

`dstat -t` помогает сопоставлять активность системы, сети и дисков во времени.
`opensnoop` позволяет наблюдать, какие файлы открываются, в реальном времени.
</b></details>

<details>
<summary>Чем вы диагностируете проблемы процессов?</summary><br><b>

`strace` показывает системные вызовы программы и помогает понять её поведение.
</b></details>

<details>
<summary>Чем вы диагностируете проблемы CPU?</summary><br><b>

`top` показывает загрузку CPU процессами.
`perf` позволяет профилировать выполнение и выяснять, на что расходуются процессорные циклы.
Flame graphs визуализируют профиль выполнения: http://www.brendangregg.com/flamegraphs.html.
</b></details>

<details>
<summary>Пользователь жалуется: «Система тормозит». Что делать?</summary><br><b>

* Проверить необычную активность в `top`.
* Через `dstat -t` оценить активность диска и сети.
* Проверить сетевые показатели через `sar` с подходящими параметрами.
* Проверить ввод-вывод через `iostat`.
</b></details>

<details>
<summary>Объясните вывод iostat.</summary><br><b>
</b></details>

<details>
<summary>Как отлаживать исполняемые файлы?</summary><br><b>
</b></details>

<details>
<summary>Чем нагрузка CPU (load) отличается от его использования (utilization)?</summary><br><b>
</b></details>

<details>
<summary>Как измерить время выполнения программы?</summary><br><b>
</b></details>

<a id="scenarios-1"></a>
#### Практические ситуации

<details>
<summary>Известен путь файла, в который пишет ненужный процесс. Как найти и завершить этот процесс?</summary><br><b>

1. Выполните `lsof <FILE_PATH>`.
2. Проверьте найденный PID и выполните `kill <PID>`.

</b></details>

<a id="kernel"></a>
### Ядро

<details>
<summary>Что такое ядро и что оно делает?</summary><br><b>

Ядро — часть ОС, отвечающая, в частности, за:

  * Распределение памяти.
  * Планирование процессов.
  * Управление выполнением на CPU.
</b></details>

<details>
<summary>Как узнать версию ядра?</summary><br><b>

Командой `uname -a`.
</b></details>

<details>
<summary>Что такое модуль ядра Linux и как его загрузить?</summary><br><b>

Модуль — код, динамически добавляющий функции ядру, например поддержку оборудования или файловых систем. Ядро Linux монолитное, но модули расширяют его без полной пересборки и обычно без перезагрузки.
</b></details>

<details>
<summary>Чем пространство пользователя отличается от пространства ядра?</summary><br><b>

Ядро работает в защищённом пространстве памяти, чтобы пользовательские программы не могли произвольно изменять его данные и нарушать работу системы.
Пользовательские команды и приложения работают в пользовательском пространстве. Такое разделение защищает ядро от ошибок и вмешательства приложений.

Для доступа к ресурсам ОС приложения обращаются к ядру через системные вызовы.
</b></details>

<details>
<summary>На каких этапах можно менять конфигурацию ядра?</summary><br><b>

  * При сборке.
  * При загрузке.
  * Во время работы.
</b></details>

<details>
<summary>Где найти конфигурацию сборки ядра?</summary><br><b>

Обычно в `/boot/config-<kernel version>.<os release>.<arch>`; точное имя зависит от дистрибутива.
</b></details>

<details>
<summary>Где посмотреть командную строку, переданную ядру при загрузке?</summary><br><b>

`/proc/cmdline`
</b></details>

<details>
<summary>Как вывести параметры ядра, доступные во время работы?</summary><br><b>

`sysctl -a`
</b></details>

<details>
<summary>Может ли вывод sysctl -a отличаться для обычного пользователя и root?</summary><br><b>

Да. Обычному пользователю могут быть недоступны некоторые параметры, которые root способен прочитать.
</b></details>

<details>
<summary>Как включить маршрутизацию IPv4 в ядре?</summary><br><b>

`sudo sysctl net.ipv4.ip_forward=1`

Для сохранения после перезагрузки добавьте `net.ipv4.ip_forward = 1` в поддерживаемый системой конфигурационный файл sysctl, например `/etc/sysctl.conf`.

Другой способ немедленного изменения: `echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward`.
</b></details>

<details>
<summary>Как sysctl изменяет параметры ядра во время работы?</summary><br><b>

Трассировка `strace` показывает запись в соответствующие файлы `/proc/sys/`.

Раньше существовал системный вызов sysctl; этот интерфейс устарел.
</b></details>

<details>
<summary>Как сохранить параметры ядра после перезагрузки?</summary><br><b>

Записать их в конфигурацию, применяемую при загрузке. `systemd-sysctl` читает файлы `sysctl.d`; обработка `/etc/sysctl.conf` зависит от дистрибутива. Уточнение: один только запуск `sysctl` изменение не сохраняет.
</b></details>

<details>
<summary>Влияет ли изменение параметров ядра внутри контейнера на хост?</summary><br><b>

Зависит от параметра и пространств имён. Некоторые параметры изолированы, другие глобальны; привилегированный контейнер способен затронуть хост. Уточнение к исходнику: собственное представление `/proc` не гарантирует изоляцию всех параметров общего ядра.
</b></details>

<a name="questions-linux-ssh"></a>
<a id="ssh"></a>
### SSH

<details>
<summary>Что такое SSH? Как проверить, работает ли SSH-сервер?</summary><br><b>

[Википедия](https://en.wikipedia.org/wiki/SSH_(Secure_Shell)): SSH, или Secure Shell, — криптографический сетевой протокол для безопасной работы сетевых сервисов через незащищённую сеть.

[Hostinger.com](https://www.hostinger.com/tutorials/ssh-tutorial-how-does-ssh-work): протокол удалённого администрирования, позволяющий управлять серверами через интернет.

На сервере работает демон SSH. Проверка зависит от системы, например `systemctl status sshd`.
</b></details>

<details>
<summary>Почему SSH безопаснее Telnet?</summary><br><b>

Telnet передаёт данные, включая пароли, открытым текстом. SSH шифрует соединение, защищая содержимое от перехвата.
</b></details>

<details>
<summary>Что хранится в ~/.ssh/known_hosts?</summary><br><b>

Известные клиенту открытые ключи SSH-хостов. Они позволяют проверять подлинность сервера при последующих подключениях. Уточнение: это не список ключей клиентов для входа на сервер.
</b></details>

<details>
<summary>Что означает Host key verification failed при подключении SSH?</summary><br><b>

Клиент не смог подтвердить ключ хоста. Например, ключ сервера изменился и не совпадает с записью в `~/.ssh/known_hosts`; причину изменения нужно проверить.
</b></details>

<details>
<summary>Чем отличаются SSH и SSL?</summary><br><b>
</b></details>

<details>
<summary>Для чего используется ssh-keygen?</summary><br><b>

Для создания и обслуживания ключей SSH. Пара состоит из закрытого и открытого ключа. В исходнике перечислены следующие алгоритмы; их поддержка зависит от версии:
- dsa
- ecdsa
- ecdsa-sk
- ed25519
- ed25519-sk
- rsa (в исходнике указан как вариант по умолчанию)

Для некоторых алгоритмов можно задать размер ключа. Следующая команда создаёт RSA-ключ длиной 4096 бит:
```
$ ssh-keygen -t rsa -b 4096
```

Пример вывода:
```
Generating public/private rsa key pair.
Enter file in which to save the key (/home/user/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/user/.ssh/id_rsa
Your public key has been saved in /home/user/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:f5MOGnhzYfC0ZCHvbSXXiRiNVYETjxpHcXD5xSojx+M user@mac-book-pro
The key's randomart image is:
+---[RSA 4096]----+
|        . ..+***o|
|         o o++*o+|
|        . =+.++++|
|         B.oX+. .|
|        S *=o+   |
|       . o oE.   |
|      . + + +    |
|       . = + .   |
|        .   .    |
+----[SHA256]-----+
```

Размер существующего ключа можно проверить так:
```
$ ssh-keygen -l -f /home/user/.ssh/id_rsa
```

Ожидаемый вид вывода:
```
4096 SHA256:f5MOGnhzYfC0ZCHvbSXXiRiNVYETjxpHcXD5xSojx+M user@mac-book-pro (RSA)
```
Он показывает RSA-ключ длиной 4096 бит.

Объяснение параметров `-l` и `-f`:
```
-l          Show the fingerprint of the key file.
-f filename Filename of the key file.
```

Подробнее: [Как определить размер SSH-ключа — Superuser](https://superuser.com/a/139311).
</b></details>

<details>
<summary>Что такое перенаправление портов SSH?</summary><br><b>
</b></details>

<a name="questions-linux-wildcards"></a>
<a id="globbing--wildcards"></a>
### Шаблоны имён и подстановочные символы

<details>
<summary>Что такое globbing — раскрытие шаблонов имён файлов?</summary><br><b>
</b></details>

<details>
<summary>Что такое подстановочные символы? Приведите пример.</summary><br><b>
</b></details>

<details>
<summary>Какие имена сопоставляются шаблону <code>ls [XYZ]</code>?</summary><br><b>
</b></details>

<details>
<summary>Какие имена сопоставляются шаблону <code>ls [^XYZ]</code>?</summary><br><b>
</b></details>

<details>
<summary>Какие имена сопоставляются шаблону <code>ls [0-5]</code>?</summary><br><b>
</b></details>

<details>
<summary>Чему соответствуют следующие шаблоны?

  - ?
  - *</summary><br><b>

  * `?` — одному символу.
  * `*` — нулю или нескольким символам.
</b></details>

<details>
<summary>Что ищет каждая команда grep?

  * <code>grep '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' some_file</code>
  * <code>grep -E "error|failure" some_file</code>
  * <code>grep '[0-9]$' some_file</code>
</summary><br><b>

1. Строку вида IPv4-адреса. Уточнение: выражение не проверяет допустимость октетов 0–255.
2. `error` или `failure`.
3. Строки, оканчивающиеся цифрой.
</b></details>

<details>
<summary>Какие строки выберет `grep '\baaa\b'` из следующего текста? Сама команда без -n номера не выводит.

aaa
bbb
ccc.aaa
aaaaaa</summary><br><b>

Первая и третья строки.
</b></details>

<details>
<summary>Чем отличаются одинарные и двойные кавычки?</summary><br><b>
</b></details>

<details>
<summary>Что такое экранирование? Какой символ для него используется?</summary><br><b>
</b></details>

<details>
<summary>Что такое код завершения? Какие коды вы знаете?</summary><br><b>

Код завершения — значение, которое дочерний процесс возвращает
родительскому после завершения.

Обычно 0 означает успех, а любое ненулевое значение, включая 1, — ошибку или иной особый результат.
Конкретный смысл зависит от программы.

Дополнительное объяснение: https://shapeshed.com/unix-exit-codes.
</b></details>

<a name="questions-linux-boot"></a>
<a id="boot-process"></a>
### Процесс загрузки

<details>
<summary>Расскажите о процессе загрузки Linux.</summary><br><b>

Иначе говоря, что происходит от включения сервера до появления приглашения командной строки?
</b></details>

<details>
<summary>Что такое GRUB2?</summary><br><b>
</b></details>

<details>
<summary>Что такое Secure Boot?</summary><br><b>
</b></details>

<details>
<summary>Что находится в /boot?</summary><br><b>
</b></details>

<a name="questions-linux-disk-fs"></a>
<a id="disk-and-filesystem"></a>
### Диски и файловые системы

<details>
<summary>Что такое inode?</summary><br><b>

Структура данных файловой системы, связанная с файлом или каталогом
и содержащая его метаданные: размер, владельца, права и другие сведения.
</b></details>

<details>
<summary>Чего нет в inode?

  * Числа ссылок
  * Размера файла
  * Имени файла
  * Временных меток</summary><br><b>

Имени файла: сопоставление имени и inode хранится в каталоге.
</b></details>

<details>
<summary>Как посмотреть текущие монтирования?</summary><br><b>

Выполнить `mount`.
</b></details>

<details>
<summary>Команда mount ничего не вывела. Где ещё посмотреть монтирования?</summary><br><b>

`cat /proc/mounts`
</b></details>

<details>
<summary>Чем символическая ссылка отличается от жёсткой?</summary><br><b>

Жёсткая ссылка — ещё одно имя того же файла с тем же inode.
Символическая ссылка имеет отдельный inode и хранит путь к цели.
</b></details>

<details>
<summary>Верно ли, что обычный пользователь может создать жёсткую ссылку на каталог?</summary><br><b>

Неверно.
</b></details>

<details>
<summary>Верно ли, что символическая ссылка может указывать в другую файловую систему?</summary><br><b>

Верно.
</b></details>

<details>
<summary>Верно ли, что каталог всегда имеет минимум две жёсткие ссылки?</summary><br><b>

В классической Unix-модели — да: учитываются имя каталога в родительском каталоге и запись `.`. Однако это не универсальное правило для всех файловых систем.
</b></details>

<details>
<summary>Что произойдёт с символической и жёсткой ссылками при удалении исходного имени файла?</summary><br><b>
</b></details>

<details>
<summary>Как узнать тип файловой системы /home?</summary><br><b>

Например, `df -T`.
</b></details>

<details>
<summary>Что такое раздел swap и зачем он нужен?</summary><br><b>
</b></details>

<details>
<summary>Как создать:

  - Пустой файл
  - Файл с текстом без редактора
  - Файл заданного размера?</summary><br><b>
  
  * touch new_file.txt
  * `cat > new_file`, затем ввод текста; `Ctrl+D` завершает ввод.
  * truncate -s <size> new_file.txt
</b></details>

<details>
<summary>Создание файла завершается ошибкой File system is full, но df показывает только 20% занятого места. В чём может быть причина?</summary><br><b>
</b></details>

<details>
<summary>Как узнать размер каталога?</summary><br><b>

`du -sh`
</b></details>

<details>
<summary>Что такое LVM?</summary><br><b>
</b></details>

<details>
<summary>Объясните понятия LVM:

  * PV
  * VG
  * LV</summary><br><b>


</b></details>

<details>
<summary>Что такое NFS и для чего его используют?</summary><br><b>
</b></details>

<details>
<summary>Для чего нужен RAID? Чем отличаются RAID 0, 1, 5 и 10?</summary><br><b>
</b></details>

<details>
<summary>Опишите расширение диска и файловой системы.</summary><br><b>
</b></details>

<details>
<summary>Что такое ленивое размонтирование (lazy umount)?</summary><br><b>
</b></details>

<details>
<summary>Что такое tmpfs?</summary><br><b>
</b></details>

<details>
<summary>Что содержат следующие журналы?

  * /var/log/messages
  * /var/log/boot.log</summary><br><b>
</b></details>

<details>
<summary>Верно ли, что /tmp и /var/tmp очищаются при загрузке?</summary><br><b>

Неверно. `/var/tmp` предназначен для временных файлов, сохраняемых между перезагрузками; `/tmp` может очищаться при загрузке. Точные правила очистки зависят от системы.
</b></details>

<a name="questions-linux-performance-analysis"></a>
<a id="performance-analysis"></a>
### Анализ производительности

<details>
<summary>Как узнать текущую среднюю нагрузку (load average)?</summary><br><b>

Через `uptime` или `top`.
</b></details>

<details>
<summary>Что означают три значения load average, например 1.43, 2.34, 2.78?</summary><br><b>

Подробное объяснение — в [этой статье](http://www.brendangregg.com/blog/2017-08-08/linux-load-averages.html).
</b></details>

<details>
<summary>Как посмотреть использование ресурсов процессами?</summary><br><b>

pidstat
</b></details>

<details>
<summary>Как проверить дисковый ввод-вывод?</summary><br><b>

`iostat -xz 1`
</b></details>

<details>
<summary>Как проверить доступную память системы и потребление памяти процессами?</summary><br><b>

Командами `top` и `free`.
</b></details>

<details>
<summary>Как посмотреть статистику TCP?</summary><br><b>

sar -n TCP,ETCP 1
</b></details>

<a name="questions-linux-processes"></a>
<a id="processes"></a>
### Процессы

<details>
<summary>Как вывести все процессы системы?</summary><br><b>

Например, `ps aux` выводит подробный список, включая фоновые процессы.
</b></details>

<details>
<summary>Как запустить процесс в фоне и зачем это нужно?</summary><br><b>

Добавить `&` в конце команды.
Это полезно для долгих или постоянно работающих задач:
оболочка остаётся доступной, не ожидая их завершения.
</b></details>

<details>
<summary>Как узнать, сколько памяти использует определённый процесс?</summary><br><b>
<code>
mem()
{                                                                                                      
    ps -eo rss,pid,euser,args:100 --sort %mem | grep -v grep | grep -i $@ | awk '{printf $1/1024 "MB"; $1=""; print }'
}
</code>
[Источник](https://stackoverflow.com/questions/3853655/in-linux-how-to-tell-how-much-memory-processes-are-using).
</b></details>

<details>
<summary>Какой сигнал по умолчанию отправляет kill PID?</summary><br><b>
<pre>
SIGTERM (15). Процесс может обработать его
и завершиться корректно, сохранив нужные данные
и освободив ресурсы.
</pre>
</b></details>

<details>
<summary>Какие сигналы вы знаете?</summary><br><b>

SIGTERM — запрос на завершение по умолчанию для kill.
SIGHUP — часто используется приложениями для перечитывания конфигурации.
SIGKILL — принудительное завершение; сигнал нельзя перехватить или игнорировать.

Список сигналов: `kill -l`.
</b></details>

<details>
<summary>Что делает kill 0?</summary><br><b>
Отправляет сигнал по умолчанию процессам текущей группы. Уточнение: это не проверка существования процесса — для неё используется сигнал 0, как в следующем вопросе.
</b></details>

<details>
<summary>Что делает <code>kill -0 PID</code>?</summary><br><b>
Проверяет существование процесса и возможность послать ему сигнал, не отправляя реального сигнала.
</b></details>

<details>
<summary>Что такое trap?</summary><br><b>
Механизм оболочки для обработки сигналов и событий заданными действиями, например очисткой ресурсов перед завершением.

</b></details>

<details>
<summary>Процесс останавливается каждые несколько дней. Как выяснить причину?</summary><br><b>
Проверить журналы приложения и системы, например `/var/log/messages` или `journalctl`, а также историю потребления ресурсов и нагрузки.
</b></details>

<details>
<summary>Что происходит при нажатии Ctrl+C?</summary><br><b>
Терминал обычно отправляет SIGINT всей группе процессов переднего плана.
</b></details>

<details>
<summary>Что такое демон Linux?</summary><br><b>

Фоновый процесс, часто ожидающий запросов или определённых событий.
Примеры: sshd, crond, rpcbind.
</b></details>

<details>
<summary>Какие состояния процесса бывают в Linux?</summary><br><b>
<pre>
Выполняется или готов к выполнению (R).
Непрерываемое ожидание (D), часто связанное с вводом-выводом.
Прерываемый сон (S).
Остановлен (T).
Завершён (X/x).
Зомби (Z).
</pre>
</b></details>

<details>
<summary>Как завершить процесс в состоянии D?</summary><br><b>
Пока он находится в непрерываемом ожидании, сигнал завершения обычно не обрабатывается. Сначала нужно устранить причину ожидания; после выхода из него сигнал может сработать. Перезагрузка — крайний вариант, а не всегда единственный способ, как утверждается в исходнике.
</b></details>

<details>
<summary>Что такое процесс-зомби?</summary><br><b>

Процесс уже завершён, но его запись с кодом выхода ещё не забрана родителем.

Родитель должен вызвать `wait()` или аналогичный интерфейс. Если он этого не делает, запись завершённого дочернего процесса остаётся в таблице процессов.
</b></details>

<details>
<summary>Как избавиться от процессов-зомби?</summary><br><b>

`kill -9` не поможет: процесс уже завершён.

Можно послать родителю `kill -s SIGCHLD [parent_pid]`, чтобы его обработчик попытался собрать статусы детей. Это сработает только при корректной реализации обработчика; сигнал не завершает детей сам по себе.

Другой вариант — корректно завершить родителя. Осиротевших потомков примет init или subreaper, который сможет забрать их статусы.
</b></details>

<details>
<summary>Как найти все:

  * Процессы определённого пользователя
  * Процессы Java
  * Процессы-зомби
</summary><br><b>

Если используете `ps` с параметрами, объясните назначение каждого из них.
</b></details>

<details>
<summary>Что такое процесс init?</summary><br><b>
Первый пользовательский процесс, запускаемый ядром, с PID 1. Он работает до выключения и является корнем дерева пользовательских процессов.
</b></details>

<details>
<summary>Опишите создание процессов.</summary><br><b>
</b></details>

<details>
<summary>Как изменить приоритет процесса и зачем?</summary><br><b>
`nice` задаёт значение nice при запуске, `renice` меняет его для существующего процесса. Диапазон обычно от -20 до 19; меньшее число означает более высокий приоритет.

Например, CPU-интенсивной фоновой задаче можно снизить приоритет, чтобы другие процессы получали больше процессорного времени.
</b></details>

<details>
<summary>Как устанавливается и завершается сетевое соединение?</summary><br><b>
Для TCP клиент создаёт сокет через `socket()` и вызывает `connect()` с адресом сервера. Установление TCP-соединения включает трёхстороннее рукопожатие.

После установления стороны обмениваются данными через `read()`, `write()` и другие операции. Для закрытия используется `close()`; завершение TCP имеет собственный обмен сегментами.
</b></details>

<details>
<summary>Что делают strace и ltrace?</summary><br><b>
`strace` отслеживает системные вызовы и сигналы процесса, помогая диагностировать зависания и сбои.

`ltrace` отслеживает вызовы функций динамических библиотек и их аргументы, помогая разбирать проблемы библиотечного уровня.

</b></details>

<details>
<summary>Найдите файлы с расширением .yml и замените в них 1 на 2.</summary><br><b>

find /some_dir -iname \*.yml -print0 | xargs -0 -r sed -i "s/1/2/g"
</b></details>

<details>
<summary>Команда ls сообщает: /lib/ld-linux-armhf.so.3 no such file or directory. В чём причина?</summary><br><b>

Не найден требуемый динамический загрузчик; например, исполняемый файл собран для несовместимой архитектуры.
</b></details>

<details>
<summary>Как разделить файл из 50 строк на два по 25?</summary><br><b>

`split -l 25 some_file`.
</b></details>

<details>
<summary>Что такое файловый дескриптор? Какие дескрипторы вы знаете?</summary><br><b>
В исходнике здесь отдельно упомянут Kerberos; к описанию файловых дескрипторов это не относится.
Файловый дескриптор — целочисленный идентификатор открытого объекта в таблице дескрипторов процесса.

Стандартные дескрипторы Unix/Linux:

  * 0 — стандартный ввод.
  * 1 — стандартный вывод.
  * 2 — стандартный поток ошибок.

Подробнее: https://www.computerhope.com/jargon/f/file-descriptor.htm.
</b></details>

<details>
<summary>Что такое NTP и для чего он нужен?</summary><br><b>
</b></details>

<details>
<summary>Объясните механизм OOM ядра.</summary><br><b>
</b></details>

<a name="questions-linux-security"></a>
<a id="security"></a>
### Безопасность

<details>
<summary>Что такое chroot? Когда его стоит использовать?</summary><br><b>
</b></details>

<details>
<summary>Что такое SELinux?</summary><br><b>
</b></details>

<details>
<summary>Что такое Kerberos?</summary><br><b>
</b></details>

<details>
<summary>Что такое nftables?</summary><br><b>
</b></details>

<details>
<summary>За что отвечает демон firewalld?</summary><br><b>
</b></details>

<details>
<summary>Есть ли у вас опыт усиления защиты серверов? Опишите процесс.</summary><br><b>
</b></details>

<details>
<summary>Как создать закрытый ключ центра сертификации?</summary><br><b>

Например, через OpenSSL:

`openssl genrsa -aes256 -out ca-private-key.pem 4096`
</b></details>

<details>
<summary>Как создать самоподписанный сертификат CA (в исходнике назван открытым ключом)?</summary><br><b>

`openssl req -new -x509 -days 730 -key [private key file name] -sha256 -out ca.pem`

С закрытым ключом из предыдущего вопроса:

`openssl req -new -x509 -days 730 -key ca-private-key.pem -sha256 -out ca.pem`
</b></details>

<details>
<summary>Покажите кодирование и декодирование данных в Linux.</summary><br><b>

Кодирование: `echo -n "some password" | base64`.
Декодирование: `echo -n "c29tZSBwYXNzd29yZA==" | base64 -d`. Уточнение: в исходнике отсутствовал `-d`. Base64 — кодирование, не шифрование.
</b></details>

<a name="questions-linux-networking"></a>
<a id="networking"></a>
### Сеть

<details>
<summary>Как вывести все сетевые интерфейсы?</summary><br><b>

```
ip link show
```
</b></details>

<details>
<summary>Что такое loopback-интерфейс lo?</summary><br><b>

Виртуальный интерфейс для связи системы с самой собой. Используется для локальных сервисов, диагностики и тестирования.
</b></details>

<details>
<summary>Для чего нужны следующие команды?

  * ip addr
  * ip route
  * ip link
  * ping
  * netstat
  * traceroute</summary><br><b>
</b></details>

<details>
<summary>Что такое сетевое пространство имён и зачем оно нужно?</summary><br><b>
</b></details>

<details>
<summary>Как проверить, используется ли определённый порт?</summary><br><b>

Например, одной из следующих команд:

```
netstat -tnlp | grep <port_number>
lsof -i -n -P | grep <port_number>
```
</b></details>

<details>
<summary>Как превратить Linux-сервер в маршрутизатор?</summary><br><b>
</b></details>

<details>
<summary>Что такое виртуальный IP и когда он нужен?</summary><br><b>
</b></details>

<details>
<summary>Верно ли, что MAC-адрес интерфейса назначается ОС?</summary><br><b>

Неверно.
</b></details>

<details>
<summary>Может ли система иметь несколько шлюзов по умолчанию?</summary><br><b>

Технически — да.
</b></details>

<details>
<summary>Что такое Telnet и почему его не стоит использовать для удалённого администрирования?</summary><br><b>

Клиент-серверный протокол, позволяющий, в частности, открыть командную строку удалённого компьютера.
Обычно передаёт данные открытым текстом без шифрования, поэтому не защищает обмен клиента и сервера.
</b></details>

<details>
<summary>Что такое таблица маршрутизации и как её посмотреть?</summary><br><b>
</b></details>

<details>
<summary>Как отправить HTTP-запрос из оболочки?</summary><br><b>
<br>
Один из вариантов — `nc`.<br>
</b></details>

<details>
<summary>Что такое анализаторы пакетов? Какими вы пользовались и для чего?</summary><br><b>
Средства захвата и анализа сетевого трафика. Некоторые инструменты также умеют формировать пакеты, но это отдельная возможность, не обязательная для анализатора.
</b></details>

<details>
<summary>Как вывести активные соединения?</summary><br><b>
</b></details>

<details>
<summary>Как инициировать обнаружение соседей IPv6?</summary><br><b>

В исходнике предложен `ping6 ff02::1`: это запрос всем узлам локального канала; обычно нужно указать интерфейс. Это не универсальная замена протоколу Neighbor Discovery.
</b></details>

<details>
<summary>Что такое объединение интерфейсов (bonding) и как его настроить в Linux?</summary><br><b>
</b></details>

<details>
<summary>Какие режимы bonding вы знаете?</summary><br><b>

Например:

  * balance-rr — циклическое распределение пакетов.
  * active-backup — один активный интерфейс, остальные резервные.
  * balance-tlb — адаптивная балансировка передачи.
  * balance-alb — адаптивная балансировка нагрузки.
</b></details>

<details>
<summary>Что такое сетевой мост и как его добавить в Linux?</summary><br><b>
</b></details>

<a name="questions-linux-dns"></a>
<a id="dns"></a>
### DNS

<details>
<summary>Как узнать имя хоста?</summary><br><b>

`cat /etc/hostname`

Также используйте `hostnamectl` или `hostname`. Файл обычно содержит постоянное имя; действующее имя может отличаться.
</b></details>

<details>
<summary>Для чего нужен /etc/resolv.conf и что он содержит?</summary><br><b>
</b></details>

<details>
<summary>Какими командами вы выполняете DNS-запросы и диагностику DNS?</summary><br><b>

Например:

 * <code>dig</code>
 * <code>host</code>
 * <code>nslookup</code>
</b></details>

<details>
<summary>Команда <code>dig codingshell.com</code> вернула:

```
ANSWER SECTION:
codingshell.com.	3515	IN	A	185.199.109.153
```

Что означает число 3515?
</summary><br><b>

Это TTL записи. При разрешении имени DNS-резолвер получает данные от DNS-сервера.<br>
TTL определяет, сколько секунд запись допускается хранить в кеше: здесь 3515. Пока срок не истёк, кеширующий резолвер может отвечать без повторного обращения за этой записью. Наличие кеша именно в ОС зависит от её настройки.
</b></details>

<details>

<summary>Как через nmcli задать DNS-сервер 8.8.8.8 для подключения?</summary><br><b>

1. Найдите имя подключения:
    ```
    # nmcli con show
    NAME         UUID                                  TYPE      DEVICE
    System ens5  8126c120-a964-e959-ff98-ac4973344505  ethernet  ens5
    System eth0  5fb06bd0-0bb0-7ffb-45f1-d6edd65f3e03  ethernet  --
    ```
    В примере это `System ens5`; изменим его настройки.

2. Задайте DNS 8.8.8.8:
    ```
    # nmcli con mod "System ens5" ipv4.dns "8.8.8.8"
    ```

3. Повторно активируйте подключение, чтобы применить изменения:
    ```
    nmcli con up "System ens5"
    ```

4. Проверьте настройки:
    ```
    cat /etc/resolv.conf
    nmcli -f ipv4.dns con show "System ens5"
    ```
</b>

</details>
 
<a name="questions-linux-packaging"></a>
<a id="packaging"></a>
### Пакеты

<details>
<summary>Есть ли у вас опыт сборки пакетов? Объясните процесс.</summary><br><b>
</b></details>

<details>
<summary>Как устанавливать и удалять пакеты в вашем дистрибутиве?</summary><br><b>

Зависит от дистрибутива.

В Fedora/CentOS/RHEL/Rocky используются `rpm` и соответствующий пакетный менеджер, например `dnf`.
В Ubuntu — `apt`.
</b></details>

<details>
<summary>Объясните формат spec для RPM: что он должен и может содержать?</summary><br><b>
</b></details>

<details>
<summary>Как посмотреть содержимое пакета без установки?</summary><br><b>
</b></details>

<details>
<summary>Как узнать, какому пакету принадлежит файл? Проблема ли, если он не относится ни к одному пакету?</summary><br><b>
</b></details>

<details>
<summary>Где находятся настройки репозиториев в вашем дистрибутиве?</summary><br><b>
</b></details>

<details>
<summary>Что такое архив и как его создать в Linux?</summary><br><b>
</b></details>

<details>
<summary>Как извлечь содержимое архива?</summary><br><b>
</b></details>

<details>
<summary>Зачем нужны пакетные менеджеры? Почему недостаточно публиковать архивы?</summary><br><b>

Они управляют жизненным циклом пакетов: установкой, удалением и обновлением.<br>
В описании пакета можно задавать размещение файлов и действия до и после установки.
</b></details>

<a name="questions-linux-dnf"></a>
<a id="dnf"></a>
### DNF

<details>
<summary>Что такое DNF?</summary><br><b>

Из [репозитория проекта](https://github.com/rpm-software-management/dnf):

Dandified YUM (DNF) — преемник YUM, использующий RPM, libsolv и hawkey для управления пакетами. Это описание версии из исходника.

Официальная [документация](https://dnf.readthedocs.io/en/latest/).

</b></details>

<details>
<summary>Как найти пакет, предоставляющий /usr/bin/git, даже если он не установлен?</summary><br><b>

dnf provides /usr/bin/git
</b></details>

<a name="questions-linux-apps-and-services"></a>
<a id="applications-and-services"></a>
### Приложения и сервисы

<details>
<summary>Что содержится в /etc/services?</summary><br><b>
</b></details>

<details>
<summary>Как обеспечить запуск сервиса после перезагрузки или сбоя?</summary><br><b>

Зависит от системы инициализации.

Systemd: `systemctl enable [service_name]` включает автозапуск. Для восстановления после сбоя отдельно настраивают `Restart=`.
System V: настройка через `update-rc.d` и, для подходящих систем, запись `respawn` в `/etc/inittab`. Строка `id:5678:respawn:/bin/sh /path/to/app` из исходника требует адаптации к допустимым уровням запуска системы.
Upstart: конфигурация задания в `/etc/init/service.conf`.
</b></details>

<details>
<summary>Почему ssh 127.0.0.1 может вернуть connection refused?</summary><br><b>

1. SSH-сервер не установлен.
2. SSH-сервер не запущен или не слушает этот адрес и порт.
</b></details>

<details>
<summary>Как вывести динамические библиотеки, необходимые программе? Зачем это нужно?</summary><br><b>
</b></details>

<details>
<summary>Что такое CUPS?</summary><br><b>
</b></details>

<details>
<summary>Какие веб-серверы вы знаете?</summary><br><b>

Nginx, Apache httpd.
</b></details>

<a name="questions-linux-users-and-groups"></a>
<a id="users-and-groups"></a>
### Пользователи и группы

<details>
<summary>Что такое суперпользователь root и чем он отличается от обычного пользователя?</summary><br><b>
</b></details>

<details>
<summary>Как создать пользователя? Где хранятся его данные?</summary><br>

Команда `useradd`.

Синтаксис:
`useradd [options] Username`

Основные файлы локальных учётных записей:

1. `/etc/passwd` — имя, UID, GID, оболочка и другие сведения.

2. `/etc/shadow` — хеш пароля и параметры его действия; это не обратимое шифрование пароля.
</details>

<details>
<summary>Где хранятся сведения о группах?</summary><br>

В `/etc/group`: имя, GID и список дополнительных участников. В исходнике путь ошибочно указан как `/etc/groups`.
</details>

<details>
<summary>Как задать или изменить пароль пользователя?</summary><br>

`passwd <username>`.
</details>

<details>
<summary>Где хранятся пароли? Доступны ли они всем?</summary><br>

Хеши локальных паролей находятся в `/etc/shadow`. Доступ ограничен привилегированными пользователями и разрешёнными системными компонентами.
</details>

<details>
<summary>Можно ли создать пользователя без adduser/useradd?</summary><br>

Да, вручную согласовав записи учётных файлов. Ниже упрощённый пример исходника; для реальной системы нужны также корректные shadow-записи, права и домашний каталог.

Например, пользователь `john`:

Шаг 1. Добавить запись в `/etc/passwd`:

`echo "john:x:2001:2001::/home/john:/bin/bash" >> /etc/passwd` 

Шаг 2. Добавить нужную основную группу в `/etc/group`. Уточнение: совпадение её имени с именем пользователя необязательно.

`echo "john:x:2001:" >> /etc/group`

Шаг 3. Проверить запись:

`id john`

</details>

<details>
<summary>Что хранится в /etc/passwd? Объясните каждое поле.</summary><br>

Каждая запись содержит семь полей:

`username:password:UID:GID:Comment:home directory:shell`

`username` — имя пользователя.

`password` — обычно `x`, означающий хранение хеша в `/etc/shadow`, а не самого пароля в этом поле.

`UID` — идентификатор пользователя.

`GID` — идентификатор основной группы.

`Comment` — описание пользователя.

`home directory` — абсолютный путь домашнего каталога; его создание зависит от параметров команды создания пользователя.

`shell` — абсолютный путь входной оболочки.
</details>

<details>
<summary>Как создать пользователя без интерактивного входа?</summary><br><b>

`adduser user_name --shell=/bin/false --no-create-home`
Также можно изменить оболочку существующего пользователя; ручную правку `/etc/passwd` следует выполнять подходящими средствами.
</b></details>

<details>
<summary>Как переключиться на другого пользователя или root?</summary><br><b>

Командой `su`.
Для входного окружения root: `su -`.
</b></details>

<details>
<summary>Какой UID у root и обычных пользователей?</summary><br>

У root UID 0.

Границы для обычных пользователей задаются `UID_MIN` и `UID_MAX` в `/etc/login.defs`. В примере исходника:
`UID_MIN` — `1000`.
`UID_MAX` — `60000`.

Настройки можно менять; меньшие UID обычно используются системными аккаунтами.
Таким образом, в приведённой конфигурации обычные UID начинаются с 1000; значения зависят от дистрибутива.
</details>

<details>
<summary>Что делать, если вы забыли пароль root?</summary><br><b>

Переустановка ОС — не ожидаемый ответ :)
</b></details>

<details>
<summary>Что такое /etc/skel?</summary><br>

Каталог шаблонных файлов и подкаталогов, копируемых в домашний каталог при создании пользователя соответствующими средствами.
</details>

<details>
<summary>Как посмотреть историю входов в систему?</summary><br><b>

Командой `last`.
</b></details>

<details>
<summary>Объясните назначение команд:

  * useradd
  * usermod
  * whoami
  * id</summary><br><b>

  `useradd` — создание пользователя.
  `usermod` — изменение его настроек.
  `whoami` — имя текущего эффективного пользователя.
  `id` — идентификаторы пользователя и групп.
</b></details>

<details>
<summary>Почему grep $(whoami) /etc/passwd может ничего не вывести?</summary><br><b>

Пользователь может поступать из LDAP или другого внешнего источника, а не локального файла.<br>
Проверьте через `getent passwd`.
</b></details>

<a name="questions-linux-hardware"></a>
<a id="hardware"></a>
### Оборудование

<details>
<summary>Где посмотреть сведения о процессорах?</summary><br><b>

/proc/cpuinfo

Количество доступных процессоров также показывает `nproc`.
</b></details>

<details>
<summary>Как вывести сведения о BIOS, плате, процессоре и RAM?</summary><br><b>

`dmidecode` — в исходнике была опечатка.
</b></details>

<details>
<summary>Как вывести информацию о блочных устройствах?</summary><br><b>

lsblk
</b></details>

<details>
<summary>Верно ли, что приложения в пользовательском пространстве не имеют неограниченного доступа к оборудованию?</summary><br><b>

Верно. Привилегированные операции контролируются ядром.
</b></details>

<a name="questions-linux-namespaces"></a>
<a id="namespaces"></a>
### Пространства имён

<details>
<summary>Какие пространства имён есть в Linux?</summary><br><b>

  - PID — отдельное представление идентификаторов процессов.
  - Mount — изоляция и управление точками монтирования.
  - Network — изоляция сетевых ресурсов: таблиц маршрутизации, интерфейсов, ARP-таблиц и т. д.
  - UTS — изоляция имени хоста и доменного имени NIS.
  - IPC — изоляция механизмов межпроцессного взаимодействия.
  - User — изоляция идентификаторов пользователей и групп.
  - Time — отдельные представления некоторых системных часов. Это не полная виртуализация всех часов системы.
</b></details>

<details>
<summary>Верно ли, что первый процесс пространства PID получает внутри него PID 1?</summary><br><b>

Верно. В родительском пространстве у него другой PID.
</b></details>

<details>
<summary>Верно ли, что дочернее пространство PID видит процессы родительского, а родительское не видит дочерних?</summary><br><b>

Неверно: наоборот. Родительское видит процессы дочернего пространства, а дочернее не видит процессы за своими границами.
</b></details>

<details>
<summary>Верно ли, что два только что созданных сетевых пространства имён сразу могут обмениваться ping?</summary><br><b>

Неверно. У каждого свои интерфейсы и маршруты; связь нужно организовать, например парой veth и необходимой адресацией, при необходимости используя мост.
</b></details>

<details>
<summary>Верно ли, что UTS позволяет процессам на одном хосте видеть разные имена хостов и доменов?</summary><br><b>

Верно.
</b></details>

<details>
<summary>Верно ли, что в дочернем пользовательском пространстве нельзя иметь UID 0?</summary><br><b>

Неверно. Внутри него может быть UID 0, сопоставленный другому UID снаружи.
</b></details>

<details>
<summary>Зачем нужны пространства имён времени?</summary><br><b>

Они позволяют процессам иметь отдельные смещения некоторых часов системы; это не независимая настройка всех видов системного времени.
</b></details>

<a name="questions-linux-virtualization"></a>
<a id="virtualization"></a>
### Виртуализация

<details>
<summary>Какие решения виртуализации доступны для Linux?</summary><br><b>

  * [KVM](https://www.linux-kvm.org/page/Main_Page)
  * [XEN](http://www.xen.org/)
  * [VirtualBox](https://www.virtualbox.org/)
  * [Linux-VServer](http://linux-vserver.org/Welcome_to_Linux-VServer.org)
  * [User-mode Linux](http://user-mode-linux.sourceforge.net/)
  * ...
</b></details>

<details>
<summary>Что такое KVM?</summary><br><b>

Открытая технология виртуализации на основе ядра Linux, в том числе для x86 с аппаратной поддержкой виртуализации.

Официальная [документация](https://www.linux-kvm.org/page/Main_Page).
Дополнительное чтение:
  * [Статья Red Hat: что такое KVM?](https://www.redhat.com/en/topics/virtualization/what-is-KVM)
</b></details>

<details>
<summary>Что такое libvirt?</summary><br><b>

Набор открытых средств и API управления виртуализацией; поддерживает KVM, Xen, LXC и другие технологии.

Официальная [документация](https://libvirt.org/).
[Поддерживаемые драйверы](https://libvirt.org/drivers.html).
</b></details>

<a name="questions-linux-awk"></a>
<a id="awk"></a>
### AWK

<details>
<summary>Что делает awk? Использовали ли вы его и для чего?</summary><br><b>

По определению Википедии, AWK — предметно-ориентированный язык обработки текста, часто применяемый для извлечения данных и построения отчётов.
</b></details>

<details>
<summary>Как вывести четвёртое поле файла?</summary><br><b>

`awk '{print $4}' file`
</b></details>

<details>
<summary>Как вывести строки длиннее 79 символов?</summary><br><b>

`awk 'length($0) > 79' file`
</b></details>

<details>
<summary>Что делает lsof? Для чего вы его использовали?</summary><br><b>
</b></details>

<details>
<summary>Чем отличаются find и locate?</summary><br><b>
</b></details>

<details>
<summary>Как пользовательский процесс выполняет привилегированную операцию, например чтение диска?</summary><br><b>

Через системные вызовы.
</b></details>

<a name="questions-linux-system-calls"></a>
<a id="system-calls"></a>
### Системные вызовы

<details>
<summary>Что такое системный вызов? Какие вызовы вы знаете?</summary><br><b>
</b></details>

<details>
<summary>Как программа выполняет системный вызов?</summary><br><b>

- Специальная инструкция переводит выполнение в режим ядра через предусмотренную точку входа.
- Ядро проверяет запрос и выполняет разрешённую операцию. Программа не получает произвольных прав ядра.
- Инструкция возврата переводит выполнение обратно в пользовательский режим.
</b></details>

<details>
<summary>Объясните fork().</summary><br><b>

Создаёт дочерний процесс на основе вызывающего с собственным PID. Многие свойства наследуются, но есть исключения, например блокировки памяти и незавершённые асинхронные операции ввода-вывода.
</b></details>

<details>
<summary>Что возвращает fork()?</summary><br><b>

  - При успехе: PID ребёнка родителю и 0 ребёнку.
  - При ошибке: -1 родителю.
</b></details>

<details>
<summary>Назовите причину ошибки fork().</summary><br><b>

Например, недостаточно памяти для нового процесса.
</b></details>

<details>
<summary>Зачем нужен wait()?</summary><br><b>

Родитель ожидает изменение состояния ребёнка и получает его статус завершения.
Если не забирать статусы завершившихся детей, могут оставаться процессы-зомби.
</b></details>

<details>
<summary>Как ядро уведомляет родителя о завершении ребёнка?</summary><br><b>

Отправляет SIGCHLD.
</b></details>

<details>
<summary>Чем waitpid() отличается от wait()?</summary><br><b>

Позволяет выбирать конкретного ребёнка или группу и задавать параметры ожидания. Неблокирующий режим включается `WNOHANG`; он не является безусловным.<br>
Так можно ожидать нужного ребёнка, не забирая статусы других, например при реализации библиотечной функции `system()`.
</b></details>

<details>
<summary>Верно ли, что wait() не возвращается до завершения ребёнка?</summary><br><b>

Обычно он ждёт подходящего изменения состояния, но может вернуться раньше, например при ошибке или прерывании сигналом.
</b></details>

<details>
<summary>Объясните семейство exec().</summary><br><b>

Заменяет выполняемую программу новой в том же процессе.<br>
ОС загружает код и данные указанного исполняемого файла, формирует новое адресное пространство, стек, аргументы и окружение, затем начинает выполнение новой программы.
</b></details>

<details>
<summary>Верно ли, что успешный exec() не возвращается?</summary><br><b>

Верно.<br>
Прежняя программа заменена, поэтому вернуться в вызывающий код уже невозможно.
</b></details>

<details>
<summary>Какие системные вызовы используются для чтения содержимого каталога?</summary><br><b>
</b></details>

<details>
<summary>Какие системные вызовы участвуют в запуске нового процесса?</summary><br><b>

Например, `fork()` создаёт процесс, `exec()` заменяет его программу, а `wait()` используется родителем для ожидания и получения статуса.
</b></details>

<details>
<summary>Что делает execve()?</summary><br><b>

Запускает программу по заданному пути, заменяя текущую. Цель — исполняемый файл или поддерживаемый скрипт.
</b></details>

<details>
<summary>Что возвращает malloc()?</summary><br><b>
</b></details>

<details>
<summary>Объясните pipe(). Для чего он нужен?</summary><br><b>

[Реализация Unix-конвейера](https://toroid.org/unix-pipe-implementation).

Канал обеспечивает однонаправленную связь процессов: у него есть конец для записи и конец для чтения.
`pipe(2)` возвращает два файловых дескриптора — для чтения и записи соответственно.
</b></details>

<details>
<summary>Что происходит при выполнении <code>ls -l</code>?</summary><br><b>

* Оболочка читает ввод; например, реализация может использовать `getline()` для чтения строки в буфер.
* Разбирает строку на команду и аргументы: `{"ls", "-l", NULL}`.
* Выполняет необходимые раскрытия, например `*.c`.

* Запускает программу, которая читает записи каталога, например через библиотечную `readdir()`. Это упрощённая схема, конкретные вызовы зависят от реализации.

Примечания:

* `getline()` — библиотечная функция чтения строки из потока в буфер.
</b></details>

<details>
<summary>Что происходит при выполнении <code>ls -l *.log</code>?</summary><br><b>
</b></details>

<details>
<summary>Что делает библиотечная функция readdir()?</summary><br><b>
</b></details>

<details>
<summary>Что делает <code>alias x=y</code>?</summary><br><b>
</b></details>

<details>
<summary>Зачем разделять создание процесса через fork() и запуск программы через exec(), а не использовать один вызов?</summary><br><b>

Это даёт гибкость: между `fork()` и `exec()` оболочка может изменить окружение, дескрипторы и другие параметры будущей программы.
</b></details>

<details>
<summary>Кратко опишите выполнение команды оболочкой.</summary><br><b>

Для внешней команды оболочка ищет исполняемый файл, обычно по PATH, создаёт дочерний процесс через `fork()` и запускает программу через вариант `exec()`. Для обычной команды переднего плана она ожидает завершения через `wait()` или аналог, затем снова выводит приглашение. Встроенные команды и фоновые задания обрабатываются иначе.
</b></details>

<a name="questions-linux-fs-files"></a>
<a id="filesystem--files"></a>
### Файловые системы и файлы

<details>
<summary>Как создать файл заданного размера?</summary><br><b>

Несколько способов:

  * dd if=/dev/urandom of=new_file.txt bs=2MB count=1
  * truncate -s 2M new_file.txt
  * fallocate -l 2097152 new_file.txt
</b></details>

<details>
<summary>Что делает следующий блок?

```
open("/my/file") = 5
read(5, "file content")
```
</summary><br><b>

Показанные вызовы читают `/my/file`; 5 — файловый дескриптор.
</b></details>

<details>
<summary>Назовите три способа удалить файл или очистить его содержимое.</summary><br><b>
</b></details>

<details>
<summary>Чем процесс отличается от потока?</summary><br><b>
</b></details>

<details>
<summary>Что такое переключение контекста?</summary><br><b>

По [Википедии](https://en.wikipedia.org/wiki/Context_switch), это сохранение состояния процесса или потока, позволяющее позднее восстановить его и продолжить выполнение.
</b></details>

<details>
<summary>На сервере высокий load average, но нет процесса с большим потреблением CPU. Как это возможно?</summary><br><b>
</b></details>

<a name="questions-linux-advanced-networking"></a>
<a id="advanced-networking"></a>
### Расширенные сетевые вопросы

<details>
<summary>В выводе ip a есть устройство lo. Что это и зачем оно нужно?</summary><br><b>
</b></details>

<details>
<summary>Что делает traceroute и как он работает?</summary><br><b>

В исходнике также предлагается вопрос об изменяемом поле TCP-заголовка. Уточнение: ключевой механизм traceroute связан с TTL заголовка IP или Hop Limit IPv6, а не полем TCP.
</b></details>

<details>
<summary>Что такое bonding? Какие режимы вы знаете?</summary><br><b>
</b></details>

<details>
<summary>Как соединить два сетевых пространства имён, чтобы между их интерфейсами проходил ping?</summary><br><b>
</b></details>

<details>
<summary>Что такое cgroups?</summary><br><b>
</b></details>

<details>
<summary>Объясните дескриптор процесса и структуру task_struct.</summary><br><b>
</b></details>

<details>
<summary>Чем потоки отличаются от процессов?</summary><br><b>
</b></details>

<details>
<summary>Объясните потоки ядра.</summary><br><b>
</b></details>

<details>
<summary>Что происходит при системном вызове socket()?</summary><br><b>

Статья по теме: https://ops.tips/blog/how-linux-creates-sockets.
</b></details>

<details>
<summary>Выполняющийся скрипт случайно удалили. Можно ли восстановить его, пока он работает?</summary><br><b>
Иногда да — если процесс ещё держит удалённый файл открытым. Его можно прочитать через `/proc`. Уточнение: наличие процесса само по себе не гарантирует доступность всего текста скрипта.
1. Найдите PID:
```
ps aux | grep yourscriptname.sh
```
Замените `yourscriptname.sh` именем скрипта.
2. Проверьте `/proc/<PID>/fd/` и найдите дескриптор удалённого файла. В исходнике ошибочно предполагается, что это обычно 0 или 1: номер нужно определить по фактическим ссылкам.

Скопируйте содержимое найденного дескриптора в новый файл. В примере ниже номер дескриптора необходимо заменить на проверенный:
```
cp /proc/<PID>/fd/0 /path_to_restore_your_file/yourscriptname.sh
```
Подставьте настоящий PID и путь восстановления вместо значений примера.

</b></details>

<a name="questions-linux-memory"></a>
<a id="memory"></a>
### Память

<details>
<summary>Чем отличаются MemFree и MemAvailable в /proc/meminfo?</summary><br><b>

MemFree — физическая память, которая сейчас не используется.
MemAvailable — оценка памяти, доступной новым нагрузкам без подкачки, с учётом свободной памяти, освобождаемого файлового кеша и других возвращаемых ресурсов.
</b></details>

<details>
<summary>Чем отличаются paging и swapping?</summary><br><b>
</b></details>

<details>
<summary>Что такое OOM killer?</summary><br><b>
</b></details>

<a name="questions-linux-distributions"></a>
<a id="distributions"></a>
### Дистрибутивы

<details>
<summary>Что такое дистрибутив Linux?</summary><br><b>
</b></details>

<details>
<summary>Какие дистрибутивы Linux вы знаете?</summary><br><b>
</b></details>

<details>
<summary>Из каких компонентов состоит дистрибутив?</summary><br><b>

* Ядро.
* Утилиты.
* Сервисы.
* Средства установки и управления ПО.
</b></details>

<a name="questions-linux-sed"></a>
<a id="sed"></a>
### Sed

<details>
<summary>Извлеките дату с помощью sed: <code>201.7.19.90 - - [05/Jun/1985:13:42:99 +0000] "GET /site HTTP/1.1" 200 32421</code>.</summary><br><b>

`echo $line | sed 's/.*\[//g;s/].*//g;s/:.*//g'`
</b></details>

<a name="questions-linux-misc"></a>
<a id="misc-1"></a>
### Разное

<details>
<summary>Что такое дистрибутив Linux?</summary><br><b>

* Дистрибутив — набор пакетов: ядро, GNU-инструменты, сторонние приложения и другое ПО.
* Сведения о выпуске часто находятся в `/etc/*-release`.
    * Например, `/etc/redhat-release` в Red Hat и `/etc/os-release` в Amazon Linux.
    * Во многих дистрибутивах доступна команда `lsb_release`.
</b></details>

<details>
<summary>Назовите пять команд из двух букв.</summary><br><b>

ls, wc, dd, df, du, ps, ip, cp, cd ...
</b></details>

<details>
<summary>Какими способами создать пустой файл?</summary><br><b>

  * touch new_file
  * `: > new_file`. Уточнение: `echo "" > new_file` из исходника записывает перевод строки, а не ноль байт.
</b></details>

<details>
<summary>Как cd - узнаёт предыдущий каталог?</summary><br><b>

$OLDPWD
</b></details>

<details>
<summary>Назовите три способа вывести имена файлов текущего каталога.</summary><br><b>

* ls
* find .
* echo *
</b></details>

<details>
<summary>Как посчитать строки и слова в файле?</summary><br><b>

Командой `wc`.

1. Число строк:
```wc -l```

2. Число слов:
```wc -w```
</b></details>

<details>
<summary>В /etc/bashrc задано x=2, а в ~/.bashrc — x=6. Вы входите в систему. Каково значение x?</summary><br><b>
</b></details>

<details>
<summary>Чем отличаются man и info?</summary><br><b>

Объяснение — [здесь](https://askubuntu.com/questions/9325/what-is-the-difference-between-man-and-info-documentation).
</b></details>

<details>
<summary>Что такое переменные окружения? Как вывести их все?</summary><br><b>
</b></details>

<details>
<summary>Что такое устройство TTY?</summary><br><b>
</b></details>

<details>
<summary>Как создать переменную окружения?</summary><br><b>

`X=2` задаёт переменную оболочки. Чтобы её наследовали дочерние процессы, используйте `export X=2`. Это не делает значение постоянным для всех будущих сеансов.
</b></details>

<details>
<summary>Что означает двойной дефис --?</summary><br><b>

Во многих командах он обозначает конец параметров. Например, `git checkout -- some_file` восстанавливает файл, отделяя путь от параметров.
</b></details>

<details>
<summary>Подстановочные шаблоны раскрываются в пользовательском пространстве или в ядре?</summary><br><b>
</b></details>

<details>
<summary>Где обычно появляется файл нового подключённого устройства?</summary><br><b>

/dev
</b></details>

<details>
<summary>Почему man разделён на секции? Чем они отличаются?</summary><br><b>
</b></details>

<details>
<summary>Что такое User-mode Linux?</summary><br><b>
Уточнение: User-mode Linux — запуск ядра Linux как пользовательского процесса на Linux-хосте. Исходный ответ ниже вместо этого описывает обычный пользовательский режим процессора.

В пользовательском режиме приложение обращается к оборудованию через системные интерфейсы ОС, что защищает системные ресурсы от произвольного вмешательства.

Каждый процесс имеет изолированное виртуальное адресное пространство, ограничивающее доступ к чужой памяти.

Режим ядра, напротив, предоставляет ОС привилегированные возможности работы с оборудованием и управления ресурсами.

</b></details>

<details>
<summary>Под какой лицензией распространяется ядро Linux?</summary><br><b>

GPL v2
</b></details>

Примечание к переводу: примеры в блоках кода сохранены из исходной версии. Отдельные технические неточности уточнены в пояснениях. Справка по уточнениям: https://man7.org/linux/man-pages/man2/kill.2.html
