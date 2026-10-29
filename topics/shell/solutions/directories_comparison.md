<a id="directories-comparison"></a>
## Сравнение каталогов

<a id="objectives"></a>
### Задание

1. Скрипт получает два каталога в качестве аргументов и должен вывести различия между ними.

<a id="solution-1"></a>
### Решение 1

Предположим, скрипт Bash называется ```dirdiff.sh```.

```
#!/bin/bash

if test $# -ne 2
then
	echo -e "USAGE: ./dirdiff.sh directory1 directory2"
	exit 1
fi

# check for the checksums. 
# If both the checksums same, then both directories are same
if test `ls -1 $1 | sort | md5sum | awk -F "  " '{print $1}'` == `ls -1 $2 | sort | md5sum | awk -F "  " '{print $1}'`
then
	echo -e "No difference between the 2 directories"
	exit 0
fi

diff -q $1 $2
```

<a id="solution-2"></a>
### Решение 2

С помощью GNU find и diff можно рекурсивно сравнить каталоги.

```shell
diff --recursive directory1 directory2
```
