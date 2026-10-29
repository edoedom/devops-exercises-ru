<a id="unique-count"></a>
# Подсчёт повторений

<a id="objectives"></a>
## Задание

В этом каталоге находится файл `ip_list` со списком IP-адресов. Определите, какой адрес встречается в нём чаще всего.

<a id="solution"></a>
# Решение

`sort ip_list | cut -d' ' -f1 | uniq -c | sort -n | tail -1`
