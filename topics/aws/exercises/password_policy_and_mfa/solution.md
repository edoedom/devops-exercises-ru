<a id="aws-iam---password-policy--mfa"></a>
## AWS IAM: парольная политика и MFA

Примечание: выполняйте задание только в том случае, если понимаете назначение изменений и их последствия для своей учётной записи.

<a id="objectives"></a>
### Задание

1. Создайте парольную политику со следующими требованиями:
   1. Минимальная длина: 8 символов.
   2. Хотя бы одна цифра.
   3. Запрет повторного использования паролей.
2. Включите MFA для учётной записи.

<a id="solution"></a>
### Решение

Парольная политика:

1. Откройте IAM.
2. Выберите **Access management → Account settings**.
3. Нажмите **Change password policy**:
   1. Включите **Enforce minimum password length** и задайте 8 символов.
   2. Включите **Require at least one number**.
   3. Включите **Prevent password reuse**.
4. Нажмите **Save changes**.

MFA:

1. Нажмите имя учётной записи.
2. Откройте **My Security Credentials**.
3. Раскройте **Multi-factor authentication (MFA)** и нажмите **Activate MFA**.
4. Выберите тип устройства.
5. Выполните инструкции настройки и нажмите **Assign MFA**.

**Решение с Terraform:**

```
resource "aws_iam_account_password_policy" "strict" {
  minimum_password_length        = 8
  require_numbers                = true
  allow_users_to_change_password = true
  password_reuse_prevention      = 1
}
```

**Примечание:** в данном решении Terraform используется для парольной политики; MFA предлагается настроить через веб-интерфейс. В оригинале это сформулировано как общий запрет настройки MFA через Terraform, но приведённый пример сам по себе такого вывода не подтверждает.
