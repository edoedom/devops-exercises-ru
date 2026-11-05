<a id="git---squashing-commits---solution"></a>
## Git: объединение коммитов — решение

Используйте новый учебный репозиторий: в этом сценарии будет ровно два неопубликованных коммита.

```bash
mkdir squash_lab && cd squash_lab
git init -b main
git config user.name "Student"
git config user.email "student@example.invalid"
printf 'Mario\n' > new_file
git add -- new_file
git commit -m "New file"
printf 'Mario & Luigi\n' > new_file
git add -- new_file
git commit -m "Added Luigi"
git log --oneline
git status --short
git rev-parse HEAD^{tree}
git rebase -i --root
```

До rebase история содержит два коммита, а status ничего не выводит. Сохраните напечатанный ID дерева для проверки результата.

В редакторе оставьте первую строку `pick`, а вторую измените на `squash`; реальные ID будут другими:

```text
pick 5412076 New file
squash 4016808 Added Luigi
```

Сохраните список, затем в следующем редакторе задайте сообщение итогового коммита. Если нужно отменить незавершённое перебазирование, используйте `git rebase --abort`.

```bash
git rev-list --count HEAD
git show HEAD:new_file
git rev-parse HEAD^{tree}
git status --short
```

Ожидаются один коммит, содержимое `Mario & Luigi`, прежний ID дерева и пустой вывод status. Изменение истории не должно менять итоговые файлы.

Для двух последних коммитов более длинной линейной истории применяется `git rebase -i HEAD~2`. В нашем новом репозитории такого предка нет, поэтому используется `--root`. В существующем репозитории `--root` включает всю достижимую историю: не подменяйте им бездумно выбранный диапазон.

Объединение помогает собрать одну логическую правку из нескольких промежуточных коммитов. Объединить можно и больше двух: оставьте первый `pick`, последующие пометьте `squash` или `fixup` (последний отбрасывает их сообщения). Переписывание опубликованных коммитов требует согласования с командой.

[Документация git rebase](https://git-scm.com/docs/git-rebase).
