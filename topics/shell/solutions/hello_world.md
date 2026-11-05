<a id="shell-scripting---hello-world"></a>
## Привет, мир

<a id="objectives"></a>
### Задание

[Условие](../hello_world.md).

<a id="solution"></a>
### Решение

[Исполняемый пример](scripts/hello_world.sh) — единственный источник кода; именно его запускают автоматические тесты.

Без аргументов записывает `Hello World` и перевод строки в `amazing_output.txt`. Повторный запуск перезаписывает файл.

Запуск из корня репозитория:

```bash
bash topics/shell/solutions/scripts/hello_world.sh
```

Ошибки входных данных выводятся в stderr с кодом 2. Нужны Bash 4.4+ и GNU/Linux; общие требования описаны в [разделе Bash](../README.md).
