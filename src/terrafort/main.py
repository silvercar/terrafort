from __future__ import print_function

import json

import click
import boto3
import jinja2
import subprocess
from botocore.exceptions import ClientError

counter = 0


@click.group()
def cli():
    pass


@click.command('sg')
@click.argument('id')
def sg(id):
    ec2 = boto3.client('ec2')
    try:
        response = ec2.describe_security_groups(GroupIds=[id])
    except ClientError as e:
        print(e)
        return

    group = response['SecurityGroups'][0]
    # print(json.dumps(group, indent=4, sort_keys=True))

    output = render(group, 'aws_security_group.tf')

    reset_count()  # Need this to add a numeric suffix to each rule name
    for num, permission in enumerate(group['IpPermissions']):
        permission['id'] = group['GroupId']
        permission['type'] = "ingress"
        permission['name'] = group['GroupName']
        output += render(permission, 'aws_security_group_rule.tf')

    for permission in group['IpPermissionsEgress']:
        permission['id'] = group['GroupId']
        permission['type'] = "egress"
        permission['name'] = group['GroupName']
        output += render(permission, 'aws_security_group_rule.tf')

    formatted = fmt(output)

    print(formatted)


def count():
    global counter
    counter = counter + 1
    return counter


def reset_count():
    global counter
    counter = 0


def render(resource, template_path):
    template_loader = jinja2.FileSystemLoader(searchpath="./templates")
    template_env = jinja2.Environment(loader=template_loader)
    template_env.globals['count'] = count
    template = template_env.get_template(template_path)
    rendered = template.render(resource=resource)
    return rendered


def fmt(content):
    formatted = subprocess.run(["terraform", "fmt", "-"], stdout=subprocess.PIPE, input=content, encoding='ascii')
    return formatted.stdout


cli.add_command(sg)

if __name__ == "__main__":
    cli()
