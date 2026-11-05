<a id="assign-roles"></a>
# Назначение ролей

<a id="objectives"></a>
## Задание

1. Назначьте участнику своей организации следующие роли:
   1. Compute Storage Admin.
   2. Compute Network Admin.
   3. Compute Security Admin.
2. Проверьте, что роли назначены.

<a id="solution"></a>
## Решение

<a id="console"></a>
### Консоль

1. Откройте **IAM & Admin**.
2. Выберите **IAM**, затем нажмите **Add**:
   1. Выберите учётную запись участника, которому назначаете роли.
   2. В поле выбора роли найдите роли из задания и нажмите **Save**.
3. Участник должен получить возможность просматривать ресурсы Compute Engine в пределах назначенных прав.

<a id="terraform"></a>
### Terraform

[Посмотреть файл main.tf](main.tf).

Terraform создаёт service account в `project_id`, затем добавляет три роли без замены других участников IAM. Нужны права создавать service accounts и изменять IAM проекта; используйте отдельный учебный проект. Передайте `project_id` и `env_id` (например, `dev`) в plan/apply. `google_project_iam_member` добавляет одного участника; authoritative binding/policy могут конфликтовать с такими ресурсами, если управляют той же ролью/политикой. Не применяйте эти широкие учебные роли как готовый профиль production-доступа. После задания удалите созданные bindings и service account через Terraform.
