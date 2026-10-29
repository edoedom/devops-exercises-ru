<a id="number-of-arguments"></a>
## Количество аргументов

<a id="objectives"></a>
### Задание

* Если передан один аргумент, скрипт должен вывести `Got it: <argument value>`, подставив значение аргумента.
* Если аргументов нет, выведите `Usage: ./<program name> <argument>`.
* Если передано больше одного аргумента, выведите `hey hey...too many!`.

<a id="solution"></a>
### Решение

> Примечание к переводу: В исходном решении при нескольких аргументах возвращается код 1, но требуемое сообщение `hey hey...too many!` не выводится. Код оригинала сохранён.

```
#!/usr/bin/env bash

set -eu

main() {
  case $# in
    0) printf "%s" "Usage: ./<program name> <argument>"; return 1 ;;
    1) printf "%s" "Got it: $1"; return 0 ;;
    *) return 1 ;;
  esac
}

main "$@"
```
