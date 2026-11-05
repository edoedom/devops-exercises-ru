<a id="create-a-project"></a>
# Создание проекта

<a id="objectives"></a>
## Задание

1. Создайте проект с глобально уникальным project ID.

<a id="solution"></a>
## Решение

<a id="console"></a>
### Консоль

1. Нажмите **New Project** на верхней панели. Если проект уже выбран, сначала нажмите его имя, затем **New Project**. Другой вариант — найти **Create Project** через строку поиска.
2. Введите отображаемое имя и проверьте project ID. Именно ID должен быть глобально уникальным; отображаемые имена могут повторяться.
3. При необходимости выберите организацию.
4. При необходимости укажите папку.
5. Нажмите **Create**.

<a id="terraform"></a>
### Terraform

[Посмотреть решение](main.tf).

Для Terraform нужны Application Default Credentials с правом создания проекта. Выполните `terraform init`, `terraform validate`, затем `terraform plan -var=project_id=YOUR_UNIQUE_ID`. Если работаете в организации, дополнительно передайте её числовой `organization_id`. Конфигурация не создаёт папку, не привязывает billing account и не развёртывает платные сервисы. Для них требуются отдельные настройки и права.

`deletion_policy = "PREVENT"` защищает проект от случайного уничтожения. Для удаления именно учебного проекта сначала осознанно измените политику на `DELETE`, примените изменение, проверьте список ресурсов и затем выполните `terraform destroy`. Существующий проект импортируют, а не создают заново.

Источник: [google_project](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_project).
