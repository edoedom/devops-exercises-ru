<a id="reverse-a-string---solution"></a>
## Разворот строки: решение

```
my_string[::-1]
```

Более наглядный способ:<br>
<i>Внимание: этот вариант работает очень медленно.</i>

```
def reverse_string(string):
    temp = ""
    for char in string:
        temp =  char + temp
    return temp
```
