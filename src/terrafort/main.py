"""
Terrafort
Generate terraform templates for specific resources
"""

import click

from terrafort.resources.aws_instance import AwsInstance
from terrafort.resources.aws_security_group import AwsSecurityGroup


class Terrafort:
    """
    Add all commands to this class
    """

    @staticmethod
    @click.command('sg')
    @click.argument('group_id')
    def aws_sg(group_id):
        """
        Create aws_security_group and all the attached aws_security_group_rules
        :param group_id:
        :return:
        """

        sg = AwsSecurityGroup(group_id)
        print(sg.render())

    @staticmethod
    @click.command('instance')
    @click.argument('instance_id')
    def aws_instance(instance_id):
        """
        Create aws_instance
        """

        instance = AwsInstance(instance_id)
        print(instance.render())


@click.group()
def cli():
    pass


cli.add_command(Terrafort.aws_sg)
cli.add_command(Terrafort.aws_instance)
if __name__ == "__main__":
    cli()
