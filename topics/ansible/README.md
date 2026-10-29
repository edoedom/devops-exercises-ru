<a id="ansible"></a>
## Ansible

<!-- {% raw %} -->

<a id="ansible-exercises"></a>
### Упражнения по Ansible

|Название|Тема|Цель и инструкции|Решение|Комментарии|
|--------|--------|------|----|----|
| Моя первая задача | Задачи | [Задание](my_first_task.md) | [Решение](solutions/my_first_task.md)
| Обновление пакетов | Задачи | [Задание](update_upgrade_task.md) | [Решение](solutions/update_upgrade_task.md)
| Мой первый плейбук | Плейбуки | [Задание](my_first_playbook.md) | [Решение](solutions/my_first_playbook.md)

<a id="ansible-self-assessment"></a>
### Самопроверка по Ansible

<details>
<summary>Опишите компоненты Ansible и связи между ними:

* Задача (task).
* Инвентарь (inventory).
* Модуль (module).
* Сценарий (play).
* Плейбук (playbook).
* Роль (role).
</summary><br><b>

Задача — вызов конкретного модуля Ansible.

Модуль — единица кода, выполняемая Ansible на локальном или удалённом узле. Модули группируются по категориям: базы данных, файлы, сети и другие.

Инвентарь определяет узлы и группы узлов, на которых выполняются задачи. Его формат зависит от используемых плагинов; распространены INI и YAML.

Play — набор задач для указанных узлов.

Плейбук — один или несколько play. Они могут выполняться на одинаковых или разных узлах.

Роль объединяет ресурсы по определённой функции или сервису для повторного использования. В роли есть каталоги переменных, значений по умолчанию, файлов, шаблонов, обработчиков, задач и метаданных. Для использования роль указывается в плейбуке.
</b></details>

<details>
<summary>Чем Ansible отличается от других инструментов автоматизации, например Chef и Puppet?</summary><br><b>

* Не требует постоянного агента на управляемом узле.
* Имеет небольшие требования для типичных Linux-задач: Python и SSH.
* По умолчанию использует модель push; поддерживается и pull.
* Ориентирован на простоту использования.
</b></details>

<details>
<summary>Верно ли, что Ansible следует подходу изменяемой инфраструктуры?</summary><br><b>

Да, это его типичный способ применения. При неизменяемой инфраструктуре компоненты заменяют, а не меняют на месте.<br>
Ansible позволяет изменять конфигурацию существующих компонентов. У такого подхода есть недостатки, например дрейф конфигурации: по разным причинам компоненты могут оказаться в разных состояниях.
</b></details>

<details>
<summary>Верно ли, что Ansible использует декларативный стиль для описания желаемого состояния?</summary><br><b>

В оригинале дан ответ «нет, процедурный». Точнее: порядок задач в плейбуке процедурный, но многие модули декларативно задают желаемое состояние ресурса, например наличие пакета или файла.
</b></details>

<details>
<summary>Для какой автоматизации вы не стали бы использовать Ansible и почему?</summary><br><b>

Ansible умеет создавать инфраструктурные ресурсы, но для таких задач иногда предпочитают инструменты с другим подходом к управлению состоянием.

Ansible по умолчанию не ведёт общий файл состояния инфраструктуры. Например, задача создания пяти экземпляров при повторном запуске может создать ещё пять, если модуль и его параметры не обеспечивают проверку существующих ресурсов. Другие инструменты могут определить, что из пяти нужных экземпляров существует четыре, и создать только один недостающий.

Поведение Ansible зависит от конкретного модуля и параметров: отсутствие общего state-файла само по себе не означает, что все задачи создания ресурсов неидемпотентны.
</b></details>

<details>
<summary>Как вывести список модулей и получить описание конкретного модуля?</summary><br><b>

1. Открыть документацию Ansible.
2. Использовать `ansible-doc -l` для списка и `ansible-doc [module_name]` для подробного описания.
</b></details>

<a id="ansible---inventory"></a>
#### Ansible — инвентарь

<details>
<summary>Что такое файл инвентаря и как его определить?</summary><br><b>

Он задаёт узлы и группы узлов, на которых выполняются задачи Ansible.

Пример:

```
192.168.1.2
192.168.1.3
192.168.1.4

[web_servers]
190.40.2.20
190.40.2.21
190.40.2.22
```
</b></details>

<details>
<summary>Что такое динамический инвентарь и когда он нужен?</summary><br><b>

Он получает сведения об узлах из внешних источников, например облачных платформ и CMDB.

Особенно полезен, когда узлы автоматически создаются и удаляются, а вручную отслеживать каждое изменение нецелесообразно.
</b></details>

<a id="ansible---variables"></a>
#### Ansible — переменные

<details>
<summary>Измените задачу: вместо zlib используйте переменную, а если она не определена — значение zlib по умолчанию.

```
- name: Install a package
  package:
    name: "zlib"
    state: present
```
</summary><br><b>

```
- name: Install a package
  package:
    name: "{{ package_name|default('zlib') }}"
    state: present
```
</b></details>

<details>
<summary>Как сделать переменную use_var необязательной?

```
- name: Install a package
  package:
    name: "zlib"
    state: present
    use: "{{ use_var }}"
```
</summary><br><b>

С помощью `default(omit)`:

```
- name: Install a package
  package:
    name: "zlib"
    state: present
    use: "{{ use_var|default(omit) }}"
```
</b></details>

<details>
<summary>Что произойдёт при выполнении следующего play?</summary><br><b>

```
---
- name: Print information about my host
  hosts: localhost
  gather_facts: 'no'
  tasks:
      - name: Print hostname
        debug:
            msg: "It's me, {{ ansible_hostname }}"
```

Всегда внимательно изучайте предложенный код. Здесь используется факт `ansible_hostname` — информация об управляемом узле. Но сбор фактов отключён через `gather_facts: no`, поэтому при отсутствии заранее доступного факта переменная окажется неопределённой и задача завершится ошибкой.
</b></details>

<details>
<summary>Когда в выражении `{{ lookup('env', 'BEST_YEAR') | default('2017', true) }}` будет использовано значение 2017?</summary><br><b>

Когда значение переменной окружения BEST_YEAR пустое или другое ложное значение.
</b></details>

<details>
<summary>Если переменная равна 1, нужно использовать one, иначе — two. Как это сделать?</summary><br><b>

`{{ (certain_variable == 1) | ternary("one", "two") }}`
</b></details>

<details>
<summary>Переменная содержит строку True. Как преобразовать её в логическое значение?</summary><br><b>

`{{ some_string_var | bool }}`
</b></details>

<details>
<summary>Как выполнить плейбук только на определённой минорной версии ОС?</summary><br><b>
</b></details>

<details>
<summary>Для чего нужна директива become?</summary><br><b>
</b></details>

<details>
<summary>Что такое факты и как посмотреть все факты узла?</summary><br><b>
</b></details>

<details>
<summary>Что произойдёт при выполнении задачи? Как её исправить?

```
- hosts: localhost
  tasks:
      - name: Install zlib
        package:
          name: zlib
          state: present
```
</summary><br><b>
</b></details>

<details>
<summary>Назовите не менее трёх хороших практик Ansible.</summary><br><b>
</b></details>

<details>
<summary>Объясните структуру каталогов роли Ansible.</summary><br><b>
</b></details>

<details>
<summary>Для чего в Ansible нужны блоки?</summary><br><b>
</b></details>

<details>
<summary>Как вы обрабатываете ошибки в Ansible?</summary><br><b>
</b></details>

<details>
<summary>Как выполнить определённую команду, если задача завершилась ошибкой?</summary><br><b>
</b></details>

<details>
<summary>Напишите плейбук, устанавливающий zlib и vim на всех узлах, где существует файл /tmp/mario.</summary><br><b>

```
---
- hosts: all
  vars:
      mario_file: /tmp/mario
      package_list:
          - 'zlib'
          - 'vim'
  tasks:
      - name: Check for mario file
        stat:
            path: "{{ mario_file }}"
        register: mario_f

      - name: Install zlib and vim if mario file exists
        become: "yes"
        package:
            name: "{{ item }}"
            state: present
        with_items: "{{ package_list }}"
        when: mario_f.stat.exists
```
</b></details>

<details>
<summary>Одной задачей проверьте существование на узле всех файлов из переменной files_list.</summary><br><b>

```
- name: Ensure all files exist
  assert:
    that:
      - item.stat.exists
  loop: "{{ files_list }}"
```
</b></details>

<details>
<summary>Напишите плейбук, создающий файл /tmp/system_info на всех узлах, кроме группы controllers, со следующим содержимым.</summary><br><b>

```
  I'm <HOSTNAME> and my operating system is <OS>
  ```

Замените HOSTNAME и OS фактическими значениями для каждого узла.

Плейбук для создания файла system_info:

```
---
- name: Deploy /tmp/system_info file
  hosts: all:!controllers
  tasks:
      - name: Deploy /tmp/system_info
        template:
            src: system_info.j2
            dest: /tmp/system_info
```

Содержимое шаблона system_info.j2:

```
# {{ ansible_managed }}
I'm {{ ansible_hostname }} and my operating system is {{ ansible_distribution }
```
</b></details>

<details>
<summary>Переменная whoami определена в нескольких местах:

* Значения роли по умолчанию: whoami: mario.
* Extra vars, переданные через -e: whoami: toad.
* Факты узла: whoami: luigi.
* Переменные инвентаря: whoami: browser.

Какое значение будет выбрано согласно приоритетам?</summary><br><b>

Правильный ответ — toad.

Приоритет определяет, какое значение побеждает, если переменная задана в нескольких местах. Даже если вы пока с этим не сталкивались, понимать порядок переопределения полезно.

В данном примере: extra vars → факты узла → переменные инвентаря → значения роли по умолчанию.

В исходнике приведён следующий порядок от меньшего приоритета к большему:

1. Параметры командной строки, например `-u user`.
2. Значения роли по умолчанию [[1\]](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#id15).
3. Переменные групп из файла или скрипта инвентаря [[2\]](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#id16).
4. group_vars/all инвентаря [[3\]](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#id17).
5. group_vars/all плейбука [[3\]](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#id17).
6. group_vars/* инвентаря [[3\]](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#id17).
7. group_vars/* плейбука [[3\]](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#id17).
8. Переменные узлов из файла или скрипта инвентаря [[2\]](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#id16).
9. host_vars/* инвентаря [[3\]](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#id17).
10. host_vars/* плейбука [[3\]](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#id17).
11. Факты узла и кешированные set_facts [[4\]](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#id18).
12. vars уровня play.
13. vars_prompt уровня play.
14. vars_files уровня play.
15. Переменные роли из role/vars/main.yml.
16. Переменные блока — только для задач внутри блока.
17. Переменные задачи — только для этой задачи.
18. include_vars.
19. set_facts и зарегистрированные переменные.
20. Параметры роли и include_role.
21. Параметры include.
22. Extra vars — наивысший приоритет.

Полный список: [переменные плейбуков](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#ansible-variable-precedence). В исходнике также отмечены существенные различия между Ansible 1.x и 2.x.
</b></details>

<details>
<summary>Определите, верны ли утверждения:

* Модуль — набор задач.
* Лучше использовать shell или command вместо специализированного модуля.
* Факты узла переопределяют переменные play.
* Роль может включать vars, meta и handlers.
* Динамический инвентарь формируется из внешних источников.
* Хорошая практика — отступ в два пробела вместо четырёх.
* notify запускает обработчики.
* hosts: all:!controllers означает запуск только на узлах группы controllers.
</summary><br><b>
</b></details>

<details>
<summary>Объясните разницу между forks, serial и throttle.</summary><br><b>

`serial` задаёт размер группы узлов, на которой выполняется весь play перед переходом к следующей группе. При `serial: 1` узлы обрабатываются по одному.

`forks=1` ограничивает параллелизм одним рабочим процессом. При стандартной линейной стратегии сначала одна задача выполняется на всех узлах, а затем начинается следующая. В исходнике указано стандартное значение forks, равное 5.

```
[defaults]
forks = 30
```

```
- hosts: webservers
  serial: 1
  tasks:
    - name: ...
```

`throttle` дополнительно ограничивает количество одновременно выполняющих задачу рабочих процессов в пределах ограничений forks и serial. Это полезно для ресурсоёмких задач и API с ограничением частоты запросов.

```
tasks:
- command: /path/to/cpu_intensive_command
  throttle: 1
```
</b></details>

<details>
<summary>Что такое ansible-pull и чем он отличается от ansible-playbook?</summary><br><b>
</b></details>

<details>
<summary>Что такое Ansible Vault?</summary><br><b>
</b></details>

<details>
<summary>Покажите использование в Ansible:

* Условий.
* Циклов.
</summary><br><b>
</b></details>

<details>
<summary>Что такое фильтры? Писали ли вы собственные фильтры?</summary><br><b>
</b></details>

<details>
<summary>Напишите фильтр, делающий первую букву строки заглавной.</summary><br><b>

```
def cap(self, string):
    return string.capitalize()
```
</b></details>

<details>
<summary>Как выполнить задачу только в случае, если предыдущая задача что-то изменила?</summary><br><b>
</b></details>

<details>
<summary>Что такое callback-плагины и для чего их используют?</summary><br><b>
</b></details>

<details>
<summary>Чем отличаются include_task и import_task?</summary><br><b>
</b></details>

<details>
<summary>Файл /tmp/exercise содержит:

```
Goku = 9001
Vegeta = 5200
Trunks = 6000
Gotenks = 32
```

Одной задачей замените содержимое на:

```
Goku = 9001
Vegeta = 250
Trunks = 40
Gotenks = 32
```
</summary><br><b>

```
- name: Change saiyans levels
  lineinfile:
    dest: /tmp/exercise
    regexp: "{{ item.regexp }}"
    line: "{{ item.line }}"
  with_items:
    - { regexp: '^Vegeta', line: 'Vegeta = 250' }
    - { regexp: '^Trunks', line: 'Trunks = 40' }
    ...
```
</b></details>

<a id="ansible---execution-and-strategy"></a>
#### Ansible — выполнение и стратегии

<details>
<summary>Верно ли, что по умолчанию Ansible выполняет все задачи play на одном узле и только затем переходит к следующему?</summary><br><b>

Нет. При стандартной стратегии одна задача выполняется на всех узлах, после чего начинается следующая. В исходнике указано пять рабочих процессов по умолчанию.<br>
Такое поведение определяется настраиваемой стратегией выполнения.
</b></details>

<details>
<summary>Что такое стратегия Ansible? Какая стратегия используется по умолчанию?</summary><br><b>

Стратегия определяет порядок выполнения задач на узлах. Стандартная стратегия linear выполняет каждую задачу на всех узлах перед переходом к следующей.
</b></details>

<details>
<summary>Какие стратегии Ansible вы знаете?</summary><br><b>

* Linear: стандартная, каждая задача выполняется на всех узлах перед следующей.
* Free: каждый узел проходит задачи до конца play независимо и настолько быстро, насколько возможно.
* Debug: интерактивное выполнение для отладки, как описано в исходнике.
</b></details>

<details>
<summary>Для чего нужно ключевое слово <code>serial</code>?</summary><br><b>

Оно задаёт количество или долю узлов, на которых нужно выполнить весь play перед переходом к следующей группе.

Пример:

```
- name: Some play
  hosts: databases
  serial: 4
```

Если в группе восемь узлов, весь play сначала выполняется на четырёх, затем на остальных четырёх.
</b></details>

<a id="ansible-testing"></a>
#### Тестирование Ansible

<details>
<summary>Как вы тестируете проекты на Ansible?</summary><br><b>
</b></details>

<details>
<summary>Что такое Molecule и как он работает?</summary><br><b>

Molecule используется для разработки и тестирования ролей Ansible. Он позволяет проверять роли на разных дистрибутивах Linux. Это помогает убедиться в корректности автоматизации и сохранять уверенность в её работе при дальнейшем сопровождении роли.
</b></details>

<details>
<summary>Тесты Ansible сообщают idempotence test failed. Что это означает и почему идемпотентность важна?</summary><br><b>
</b></details>

<a id="ansible---debugging"></a>
#### Ansible — отладка

<details>
<summary>Как узнать тип переменной в плейбуке?</summary><br><b>

`{{ some_var | type_debug }}`
</b></details>

<a id="ansible---collections"></a>
#### Ansible — коллекции

<details>
<summary>Что такое коллекции Ansible?</summary><br><b>

Это способ упаковывать и распространять модули, роли, плагины и документацию в структурированном формате. Коллекции упрощают организацию и распространение кода автоматизации, особенно в сложных средах.
</b></details>

<details>
<summary>Зачем использовать коллекции Ansible?</summary><br><b>

* Модульные компоненты для повторного использования.
* Удобное управление собственными и сторонними модулями.
* Стандартный способ распространения материалов автоматизации.
* Поддержка управления версиями и зависимостями.
</b></details>

<!-- {% endraw %} -->
