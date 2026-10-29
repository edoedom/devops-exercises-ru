<a id="iam-aws---create-a-user"></a>
## AWS IAM: создание пользователя

<a id="objectives"></a>
### Задание

Для повседневной работы в AWS не рекомендуется использовать корневую учётную запись. В этом упражнении создайте отдельного пользователя с правами администратора.

1. Создайте пользователя с возможностью входа по паролю.
2. Добавьте его в группу admin и прикрепите к группе политику Administrator Access.
3. Назначьте пользователю тег с ключом `Role` и значением `DevOps`.

<a id="solution"></a>
### Решение

1. Откройте AWS IAM.
2. В разделе **Access Management** выберите **Users**.
3. Нажмите **Add users**.
4. Введите имя пользователя, например mario.
5. Выберите тип учётных данных **Password**.
6. Задайте собственный пароль для консоли и нажмите **Next**.
7. Нажмите **Add user to group**.
8. Укажите имя группы admin.
9. Выберите политику AdministratorAccess и нажмите **Create group**.
10. Нажмите **Next: Tags**.
11. Добавьте тег с ключом `Role` и значением `DevOps`.
12. Нажмите **Review**, затем **Create user**.

**Решение с Terraform:**

```
 
resource "aws_iam_group_membership" "team" {
  name = "tf-testing-group-membership"

  users = [
    aws_iam_user.newuser.name,

  ]

  group = aws_iam_group.admin.name
}

resource "aws_iam_group_policy_attachment" "test-attach" {
  group      = aws_iam_group.admin.name
  policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess"
}
resource "aws_iam_group" "admin" {
  name = "admin"
}

resource "aws_iam_user" "newuser" {
  name = "newuser"
  path = "/system/"

  tags = {
    Role = "DevOps"
  }
}
```
