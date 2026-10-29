<a id="shell-scripting---hello-world"></a>
## Сценарии shell: Hello World

<a id="objectives"></a>
### Задание

1. Создайте переменную со строкой `Hello World`.
2. Выведите значение этой переменной и перенаправьте вывод в файл `amazing_output.txt`.

<a id="solution"></a>
### Решение

```
#!/usr/bin/env bash

HW_STR="Hello World"
echo $HW_STR > amazing_output.txt
```
