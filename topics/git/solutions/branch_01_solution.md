<a id="branch-01---solution"></a>
## Ветки: решение задания 01

Создайте отдельный учебный репозиторий с известной исходной веткой `main`, чтобы не зависеть от имени ветки в настройках компьютера.

```bash
mkdir branch_lab && cd branch_lab
git init -b main
git config user.name "Student"
git config user.email "student@example.invalid"
printf 'main version\n' > file
git add -- file
git commit -m "Create base"
git switch -c dev
printf 'dev version\n' > file
git add -- file
git commit -m "Change file on dev"
git log --oneline main..dev
git log --oneline dev..main
git show main:file
git show dev:file
git switch main
git status --short
```

Проверка: `main..dev` показывает один новый коммит, `dev..main` — ни одного. Версии файла различаются: `main version` и `dev version`. Рабочее дерево после переключения чистое.

`git branch dev` только создаёт ветку; `git switch -c dev` также переключает на неё. Ветки позволяют независимо готовить изменения, например исправление ошибки, не двигая основную ветку до интеграции.
