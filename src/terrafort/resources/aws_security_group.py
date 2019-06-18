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

    def render(self, commands=False):
        """
        Using one template for the security group, and another for rules.
        :return:
        """
        try:
            response = self.ec2.describe_security_groups(GroupIds=[self.group_id])
        except ClientError as error:
            print(error)
            return None

        renderer = Renderer()
        sg_template = 'aws_security_group.tf'
        sg_rule_template = 'aws_security_group_rule.tf'
        if commands:
            sg_template = 'aws_security_group.import.j2'
            sg_rule_template = 'aws_security_group_rule.import.j2'
            renderer = Renderer(fmt_enabled=False)

        group = response['SecurityGroups'][0]

        output = renderer.render(group, sg_template)
        group_id = "${aws_security_group.%s.id}" % group['GroupName']

        renderer.reset_count()  # Need this to add a numeric suffix to each rule name
        for permission in group['IpPermissions']:
            permission['id'] = group_id
            permission['type'] = "ingress"
            permission['name'] = group['GroupName']
            permission['GroupId'] = group['GroupId']
            output += renderer.render(permission, sg_rule_template)

        for permission in group['IpPermissionsEgress']:
            permission['id'] = group_id
            permission['type'] = "egress"
            permission['name'] = group['GroupName']
            permission['GroupId'] = group['GroupId']
            output += renderer.render(permission, sg_rule_template)

        return output
