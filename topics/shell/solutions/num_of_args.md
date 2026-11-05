<a id="number-of-arguments"></a>
## Количество аргументов

<a id="objectives"></a>
### Задание

[Условие](../num_of_args.md).

<a id="solution"></a>
### Решение

[Исполняемый пример](scripts/num_of_args.sh) — единственный источник кода; именно его запускают автоматические тесты.

Использует `case`: без аргументов печатает подсказку в stderr и завершает работу с кодом 2; с одним — `Got it: ` и аргумент; с несколькими — `hey hey...too many!` в stderr и код 2.

Запуск из корня репозитория:

```bash
bash topics/shell/solutions/scripts/num_of_args.sh "one argument"
```

Ошибки входных данных выводятся в stderr с кодом 2. Нужны Bash 4.4+ и GNU/Linux; общие требования описаны в [разделе Bash](../README.md).
