terraform {
  required_version = ">= 1.10"
  required_providers {
    aws = { source = "hashicorp/aws", version = ">= 6.0, < 7.0" }
  }
}
provider "aws" {
  region = "eu-west-2"
}
provider "aws" {
  alias  = "public"
  region = "eu-west-1"
}
variable "enable_public_read" {
  type        = bool
  default     = false
  description = "Explicitly allow anonymous GetObject for the public exercise bucket."
}
resource "aws_s3_bucket" "private_bucket" {
  bucket_prefix = "devops-private-"
}
resource "aws_s3_bucket_ownership_controls" "private" {
  bucket = aws_s3_bucket.private_bucket.id
  rule { object_ownership = "BucketOwnerEnforced" }
}
resource "aws_s3_bucket_public_access_block" "private" {
  bucket                  = aws_s3_bucket.private_bucket.id
  block_public_acls       = true
  ignore_public_acls      = true
  block_public_policy     = true
  restrict_public_buckets = true
}
resource "aws_s3_object" "bucket_object" {
  bucket  = aws_s3_bucket.private_bucket.id
  key     = "example.txt"
  content = "Учебный файл"
}
resource "aws_s3_bucket" "public_bucket" {
  provider      = aws.public
  bucket_prefix = "devops-public-"
}
resource "aws_s3_bucket_ownership_controls" "public" {
  provider = aws.public
  bucket   = aws_s3_bucket.public_bucket.id
  rule { object_ownership = "BucketOwnerEnforced" }
}
resource "aws_s3_bucket_versioning" "public" {
  provider = aws.public
  bucket   = aws_s3_bucket.public_bucket.id
  versioning_configuration { status = "Enabled" }
}
resource "aws_s3_bucket_public_access_block" "public" {
  provider                = aws.public
  bucket                  = aws_s3_bucket.public_bucket.id
  block_public_acls       = true
  ignore_public_acls      = true
  block_public_policy     = !var.enable_public_read
  restrict_public_buckets = !var.enable_public_read
}
resource "aws_s3_bucket_policy" "public_read" {
  provider = aws.public
  count    = var.enable_public_read ? 1 : 0
  bucket   = aws_s3_bucket.public_bucket.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = "*"
      Action    = "s3:GetObject"
      Resource  = "${aws_s3_bucket.public_bucket.arn}/*"
    }]
  })
  depends_on = [aws_s3_bucket_public_access_block.public]
}
output "private_bucket" { value = aws_s3_bucket.private_bucket.id }
output "public_bucket" { value = aws_s3_bucket.public_bucket.id }
