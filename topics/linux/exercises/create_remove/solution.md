<a id="create--destroy"></a>
# Создание и удаление

<a id="objectives"></a>
## Задание

1. Создайте файл `x`.
2. Создайте каталог `content`.
3. Переместите файл `x` в каталог `content`.
4. Создайте в каталоге `content` файл `y`.
5. Создайте внутри `content` структуру каталогов `dir1/dir2/dir3`.
6. Удалите каталог content.

<a id="solution"></a>
## Решение

```
touch x
mkdir content
mv x content
touch content/y
mkdir -p content/dir1/dir2/dir3
rm -rf content
```
