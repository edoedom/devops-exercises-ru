import json
import pulumi
import pulumi_aws as aws

config = pulumi.Config()
public_read = config.get_bool("enablePublicRead") or False
private_region = aws.Provider("private-region", region="eu-west-2")
public_region = aws.Provider("public-region", region="eu-west-1")
private_opts = pulumi.ResourceOptions(provider=private_region)
public_opts = pulumi.ResourceOptions(provider=public_region)

private = aws.s3.BucketV2("private-bucket", opts=private_opts)
aws.s3.BucketOwnershipControls("private-ownership", bucket=private.id,
    rule={"object_ownership": "BucketOwnerEnforced"}, opts=private_opts)
aws.s3.BucketPublicAccessBlock("private-access", bucket=private.id,
    block_public_acls=True, ignore_public_acls=True,
    block_public_policy=True, restrict_public_buckets=True, opts=private_opts)
aws.s3.BucketObjectv2("example", bucket=private.id, key="example.txt",
    content="Учебный файл", opts=private_opts)

public = aws.s3.BucketV2("public-bucket", opts=public_opts)
aws.s3.BucketOwnershipControls("public-ownership", bucket=public.id,
    rule={"object_ownership": "BucketOwnerEnforced"}, opts=public_opts)
aws.s3.BucketVersioningV2("public-versioning", bucket=public.id,
    versioning_configuration={"status": "Enabled"}, opts=public_opts)
access = aws.s3.BucketPublicAccessBlock("public-access", bucket=public.id,
    block_public_acls=True, ignore_public_acls=True,
    block_public_policy=not public_read, restrict_public_buckets=not public_read,
    opts=public_opts)
if public_read:
    aws.s3.BucketPolicy("public-read", bucket=public.id,
        policy=public.arn.apply(lambda arn: json.dumps({
            "Version": "2012-10-17", "Statement": [{"Effect": "Allow",
            "Principal": "*", "Action": "s3:GetObject", "Resource": arn + "/*"}]})),
        opts=pulumi.ResourceOptions(provider=public_region, depends_on=[access]))
pulumi.export("privateBucket", private.id)
pulumi.export("publicBucket", public.id)
