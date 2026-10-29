<a id="launch-ec2-instance"></a>
# Запуск экземпляра EC2

<a id="requirements"></a>
## Требования

* Учётная запись AWS.

<a id="objectives"></a>
## Задание

1. Напишите конфигурацию Terraform для запуска экземпляра EC2.
2. Выполните команды, применяющие конфигурацию и создающие экземпляр.
3. Что произойдёт, если снова выполнить `terraform apply`?
4. Удалите созданный экземпляр с помощью Terraform.

<a id="solution"></a>
## Решение

```
mkdir exercise

cat << EOT >> main.tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region  = "us-west-2"
}

resource "aws_instance" "app_server" {
  ami           = "ami-830c94e3"
  instance_type = "t2.micro"

  tags = {
    Name = "ExampleAppServerInstance"
  }
}
EOT

terraform init
terraform validate
terraform plan

# You should see this line at the end: Plan: 1 to add, 0 to change, 0 to destroy

terraform apply -auto-approve

# You should see the following output:
# aws_instance.app_server: Creation complete after 49s [id=i-004651a9d4427d236

# Running 'terraform apply' again won't change anything as
# Terraform will compare actual infrastructure to your
# configuration and won't find any difference. You should see the following line:
# Apply complete! Resources: 0 added, 0 changed, 0 destroyed.

# Remove instance
terraform destroy -auto-approve

# Destroy complete! Resources: 1 destroyed.
```
