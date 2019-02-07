from __future__ import print_function

import json

import click
import boto3
import jinja2
from botocore.exceptions import ClientError


@click.group()
def cli():
    pass


@click.command('sg')
@click.argument('id')
def get_security_group(id):
    ec2 = boto3.client('ec2')
    try:
        response = ec2.describe_security_groups(GroupIds=[id])
        group = response['SecurityGroups'][0]
        print(json.dumps(group, indent=4, sort_keys=True))
        # output(group, 'aws_security_group.tf')
        for permission in group['IpPermissions']:
            permission['id'] = group['GroupId']
            permission['type'] = "ingress"
            permission['name'] = group['GroupName']
            output(permission, 'aws_security_group_rule.tf')

        for permission in group['IpPermissionsEgress']:
            permission['id'] = group['GroupId']
            permission['type'] = "egress"
            permission['name'] = group['GroupName']
            output(permission, 'aws_security_group_rule.tf')



        # print(response)
    except ClientError as e:
        print(e)


def output(resource, template_path):
    template_loader = jinja2.FileSystemLoader(searchpath="./templates")
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template(template_path)
    output = template.render(resource=resource)
    print(output)


cli.add_command(get_security_group)

if __name__ == "__main__":
    cli()
