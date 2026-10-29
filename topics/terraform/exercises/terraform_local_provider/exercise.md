<a id="local-provider"></a>
# Провайдер Local

<a id="objectives"></a>
## Задание

Научитесь выполнять основные команды Terraform.

1. Создайте каталог my_first_run.
2. Создайте в нём main.tf со следующим содержимым:

```terraform
resource "local_file" "mario_local_file" {
    content  = "It's a me, Mario!"
    filename = "/tmp/who_is_it.txt"
}
```

3. Выполните `terraform init`. Что сделала команда?
4. Выполните `terraform plan`. Какие действия планирует Terraform?
5. Выполните `terraform apply` и убедитесь, что файл создан.

<a id="solution"></a>
## Решение

[Посмотреть решение](solution.md).
