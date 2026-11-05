<a id="git-commit-01---solution"></a>
## Git: решение задания «Коммит 01»

Работайте в новом учебном каталоге. Локальные имя и email ниже — учебные значения; для рабочих коммитов укажите свои.

```bash
mkdir my_repo && cd my_repo
git init -b main
git config user.name "Student"
git config user.email "student@example.invalid"
printf 'hello commit\n' > file
git add -- file
git commit -m "Create first file"
git log -1 --oneline
git show HEAD:file
git status --short
```

Последние команды показывают коммит, содержимое `hello commit` и чистое рабочее дерево (пустой вывод status). `git add` подготавливает снимок, `git commit` сохраняет его. Флаг `-a` не добавляет новые неотслеживаемые файлы и здесь не нужен.

Коммиты сохраняют проверяемые состояния проекта; посмотреть последнее изменение можно также через `git show HEAD`.
