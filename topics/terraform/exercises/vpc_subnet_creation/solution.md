<a id="creating-custom-vpc-and-subnets-with-terraform"></a>
# Создание VPC и подсетей с Terraform

<a id="objectives"></a>
## Задание

1. Создайте VPC с заданным CIDR, например `10.0.0.0/16`.
2. Создайте две подсети с разными диапазонами, например `10.0.0.0/20` и `10.0.16.0/20`.

   Разместите подсети в разных зонах доступности для обеспечения высокой доступности.
3. Убедитесь, что Terraform отслеживает VPC и подсети.

<a id="solution"></a>
## Решение

```sh
# Create a directory for the Terraform configuration
mkdir vpc_subnet_creation && cd vpc_subnet_creation 
```

```sh
# Create the main.tf file with the VPC and subnets configuration
touch main.tf
```

```terraform
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "your-region" # e.g., ap-south-1
}

resource "aws_vpc" "my_custom_vpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "my_custom_vpc_made_with_terraform"
  }
}

resource "aws_subnet" "Subnet_A" {
  cidr_block       = "10.0.0.0/20"
  vpc_id            = aws_vpc.my_custom_vpc.id
  availability_zone = "your-availability-zone-a" # e.g., ap-south-1a
  tags = {
    "Name" = "Subnet A"
  }
}
resource "aws_subnet" "Subnet_B" {
  cidr_block       = "10.0.16.0/20"
  vpc_id            = aws_vpc.my_custom_vpc.id
  availability_zone = "your-availability-zone-b" # e.g., ap-south-1b
  tags = {
    "Name" = "Subnet B"
  }
}
```

```sh
# Initialize Terraform to download the AWS provider
terraform init
```

```sh
# Apply the Terraform configuration to create the VPC and subnets
terraform apply -auto-approve
```
