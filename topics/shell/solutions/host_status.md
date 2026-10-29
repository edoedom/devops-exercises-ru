<a id="its-alive"></a>
## Проверка доступности узла

<a id="objectives"></a>
### Задание

1. Напишите скрипт, который определяет, доступен ли указанный узел.

<a id="solution"></a>
### Решение

> Примечание к переводу: В исходном примере нужно заменить `<IP Address>` адресом проверяемого узла. Отсутствие ответа на ping не всегда означает отказ узла: ICMP может блокироваться. Код и сообщения программы сохранены из оригинала.

```
#!/usr/bin/env bash
SERVERIP=<IP Address>
NOTIFYEMAIL=test@example.com

ping -c 3 $SERVERIP > /dev/null 2>&1
if [ $? -ne 0 ]
then
   # Use mailer here:
   mailx -s "Server $SERVERIP is down" -t "$NOTIFYEMAIL" < /dev/null
fi
```
