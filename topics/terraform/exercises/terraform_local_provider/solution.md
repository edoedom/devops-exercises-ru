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

```sh
# Create a directory
mkdir my_first_run && cd my_first_run

# Create the file 'main.tf'
cat << EOT >>  main.tf
resource "local_file" "mario_local_file" {
    content  = "It's a me, Mario!"
    filename = "/tmp/who_is_it.txt"
}
EOT

# Run 'terraform init'
terraform init
# Running 'ls -la' you'll it created '.terraform' and '.terraform.lock.hcl'
# In addition, it initialized (downloaded and installed) the relevant provider plugins. In this case, the "hashicorp/local"

# Run 'terraform plan'
terraform plan
# It shows what Terraform is going to perform once you'll run 'terraform apply'

<< terraform_plan_output
Terraform will perform the following actions:

  # local_file.mario_local_file will be created
  + resource "local_file" "mario_local_file" {
      + content              = "It's a me, Mario!"
      + directory_permission = "0777"
      + file_permission      = "0777"
      + filename             = "/tmp/who_is_it.txt"
      + id                   = (known after apply)
    }

Plan: 1 to add, 0 to change, 0 to destroy.
terraform_plan_output

# Apply main.tf (it's better to run without -auto-approve if you are new to Terraform)
terraform apply -auto-approve

ls /tmp/who_is_it.txt
# /tmp/who_is_it.txt
```
