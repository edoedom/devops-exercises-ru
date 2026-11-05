import pulumi
import pulumi_aws as aws

config = pulumi.Config()
vpc_id = config.require("vpcId")
zones = aws.get_availability_zones(state="available").names
if len(zones) < 3:
    raise ValueError("Exercise requires three available availability zones")

for index in range(3):
    subnet = aws.ec2.Subnet(
        f"NewSubnet{index + 1}",
        vpc_id=vpc_id,
        cidr_block=f"10.0.{index}.0/24",
        availability_zone=zones[index],
        tags={"Name": f"NewSubnet{index + 1}"},
    )
    pulumi.export(f"subnet{index + 1}Id", subnet.id)

# Set aws:region and vpcId; the chosen VPC must contain the CIDRs and have no overlaps.
