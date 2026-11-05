<a id="jenkins-scripts"></a>
## Скрипты Jenkins

Напишите следующие скрипты:

* Удаление всех заданий, содержащих `REMOVE_ME` в имени.
* Удаление сборок старше 14 дней.

<a id="answer"></a>
### Ответ

* [Удаление заданий с заданной строкой в имени](cicd/solutions/remove_jobs_solution.groovy).
* [Удаление сборок старше 14 дней](cicd/solutions/remove_builds_solution.groovy).

Оба примера запускаются администратором в Script Console и по умолчанию только печатают список (`DRY_RUN = true`). После проверки списка измените значение на `false` для удаления. Для постоянной политики хранения используйте `buildDiscarder(logRotator(daysToKeepStr: '14'))` в Pipeline.
