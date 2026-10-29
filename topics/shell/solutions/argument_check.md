<a id="argument-check"></a>
## Проверка аргумента

<a id="objectives"></a>
### Задание

Примечание: считайте, что скрипт запускается с аргументом.

1. Напишите скрипт, который проверяет, равен ли переданный аргумент строке `pizza`.
2. Если равен, выведите `with pineapple?`.
3. Если не равен, выведите `I want pizza!`.

<a id="solution"></a>
### Решение

```
#!/usr/bin/env bash

[[ ${1} == "pizza" ]] && echo "with pineapple?" || echo "I want pizza!"
```
