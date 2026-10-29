<a id="shell-scripting---factors"></a>
## Сценарии shell: делители

<a id="objectives"></a>
### Задание

Напишите скрипт, который получает число и выполняет следующие действия:

* Если число делится на 2, выводит `one factor`.
* Если число делится на 3, выводит `one factor...actually two!`.
* Если число не делится ни на 2, ни на 3, выводит само число.

<a id="solution"></a>
### Решение

```
#!/usr/bin/env bash

(( $1 % 2 )) || res="one factor"
(( $1 % 3 )) || res+="...actually two!"

echo ${res:-$1}
```
