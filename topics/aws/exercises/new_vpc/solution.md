<a id="my-first-vpc"></a>
# Первая VPC

<a id="objectives"></a>
## Задание

1. Создайте VPC:
   1. Диапазон CIDR должен вмещать не менее 60 000 узлов.
   2. Имя: `exercise-vpc`.

<a id="solution"></a>
## Решение

<a id="console"></a>
### Консоль

1. В разделе **Virtual Private Cloud** нажмите **Your VPCs**.
2. Нажмите **Create VPC**.
3. Укажите имя exercise-vpc.
4. Задайте IPv4 CIDR: 10.0.0.0/16.
5. Оставьте **Tenancy** равным **Default**.
6. Нажмите **Create VPC**.

<a id="terraform"></a>
### Terraform

[Посмотреть решение](terraform/main.tf).

<a id="pulumi---python"></a>
### Pulumi: Python

[Посмотреть решение](pulumi/__main__.py).

<a id="verify-solution"></a>
### Проверка решения

Проверьте созданную VPC, указав тот же регион, который использовался в IaC:

```bash
aws ec2 describe-vpcs --filters Name=tag:Name,Values=exercise-vpc
```

Перед Terraform задайте AWS credentials/region, затем выполните `terraform init`, `terraform validate`, `terraform plan`. Pulumi-пример требует Python-проект с `pulumi`, `pulumi-aws` и `pulumi config set aws:region REGION`. Оба варианта создают только VPC — без платных NAT Gateway и подсетей. После проверки удалите ресурсы выбранным инструментом (`terraform destroy` или `pulumi destroy`).
