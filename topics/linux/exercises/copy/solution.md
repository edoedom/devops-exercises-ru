<a id="copy-time"></a>
# Копирование файлов и каталогов

<a id="objectives"></a>
## Задание

1. Создайте пустой файл `x` в `/tmp`.
2. Скопируйте его в домашний каталог.
3. Создайте копию файла `x` с именем `y`.
4. Создайте каталог `files` и переместите туда `x` и `y`.
5. Скопируйте каталог files под именем `copy_of_files`.
6. Переименуйте `copy_of_files` в `files2`.
7. Удалите каталоги `files` и `files2`.

<a id="solution"></a>
## Решение

```
touch /tmp/x
cp x ~/
cp x y
mkdir files
mv x files | mv y files
cp -r files copy_of_files
mv copy_of_files files2
rm -rf files files2
```
