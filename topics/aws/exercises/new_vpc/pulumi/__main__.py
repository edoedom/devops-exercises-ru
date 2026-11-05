import pulumi
import pulumi_aws as aws

# Только VPC: подсети, NAT Gateway и Internet Gateway в этом задании не нужны.
vpc = aws.ec2.Vpc("exercise-vpc", cidr_block="10.0.0.0/16",
                 tags={"Name": "exercise-vpc"})
pulumi.export("vpc_id", vpc.id)
