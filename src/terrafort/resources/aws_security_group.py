import boto3
from botocore.exceptions import ClientError

from terrafort.renderer import Renderer


class AwsSecurityGroup:
    """
    Render a template for a security group and all its rules. Will create
    one aws_security_group_rule resource per rule.
    """

    def __init__(self, group_id):
        self.ec2 = boto3.client('ec2')
        self.group_id = group_id

    def render(self):
        """
        Using one template for the security group, and another for rules.
        :return:
        """
        try:
            response = self.ec2.describe_security_groups(GroupIds=[self.group_id])
        except ClientError as error:
            print(error)
            return None

        group = response['SecurityGroups'][0]

        renderer = Renderer()

        output = renderer.render(group, 'aws_security_group.tf')

        renderer.reset_count()  # Need this to add a numeric suffix to each rule name
        for permission in group['IpPermissions']:
            permission['id'] = group['GroupId']
            permission['type'] = "ingress"
            permission['name'] = group['GroupName']
            output += renderer.render(permission, 'aws_security_group_rule.tf')

        for permission in group['IpPermissionsEgress']:
            permission['id'] = group['GroupId']
            permission['type'] = "egress"
            permission['name'] = group['GroupName']
            output += renderer.render(permission, 'aws_security_group_rule.tf')

        return output
