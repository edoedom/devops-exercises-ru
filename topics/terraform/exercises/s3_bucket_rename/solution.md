<a id="rename-s3-bucket"></a>
# Изменение имени бакета S3

<a id="requirements"></a>
## Требования

* Существующий бакет S3, управляемый Terraform.

Если его нет, используйте следующий блок и выполните `terraform apply`:

```terraform
resource "aws_s3_bucket" "some_bucket" {
    bucket = "some-old-bucket"
}
```

Внимание: имена бакетов S3 должны быть глобально уникальными. Вероятно, потребуется изменить имя в примере, если оно уже занято.

<a id="objectives"></a>
## Задание

1. Измените имя существующего бакета S3 и убедитесь, что он по-прежнему управляется Terraform.

<a id="solution"></a>
## Решение

```sh
# A bucket name is immutable in AWS so we'll have to create a new bucket
aws s3 mb s3://some-new-bucket-123

# Sync old bucket to new bucket
aws s3 sync s3://some-old-bucket s3://some-new-bucket-123

# Option 1 (remove and import)

## Remove the old bucket from Terraform's state
terraform state rm aws_s3_bucket.some_bucket

## Import new bucket to Terraform's state
terraform import aws_s3_bucket.some_bucket some-new-bucket-123

: '
aws_s3_bucket.some_bucket: Refreshing state... [id=some-new-bucket-123]

Import successful!
The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.
'

# Option 2 (move)

## Move the old bucket from Terraform's state to the new one
terraform state mv aws_s3_bucket.some_bucket some-new-bucket-123

: '
Move "aws_s3_bucket.some_bucket" to "aws_s3_bucket.some-new-bucket-123"
Successfully moved 1 object(s).
'

# Modify Terraform file

# Modify the Terraform definition to include the new name
# resource "aws_s3_bucket" "some_bucket" {
#    bucket = "some-new-bucket-123"
# }

# Remove old bucket
aws s3 rm s3://some-old-bucket --recursive
aws s3 rb s3://some-old-bucket
```
