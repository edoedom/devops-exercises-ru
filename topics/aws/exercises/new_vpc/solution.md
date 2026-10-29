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

Для проверки создания VPC в оригинале приведена команда: `aws ec2 describe-vpcs -filters Name=tag:Name,Values=exercise-vpc`.

> Примечание к переводу: в команде исходника опечатка — параметр должен начинаться с двух дефисов: `--filters`.
