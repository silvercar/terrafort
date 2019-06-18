"""
Terrafort
Generate terraform templates for specific resources
"""

import click

from .providers.aws import Aws


@click.group()
@click.option('--commands',
              is_flag=True,
              help="Output import commands instead of a terraform template")
@click.version_option()
@click.pass_context
def cli(ctx, commands=False):
    ctx.obj = {'commands':  commands}


cli.add_command(Aws.aws_db_instance)
cli.add_command(Aws.aws_iam_instance_profile)
cli.add_command(Aws.aws_instance)
cli.add_command(Aws.aws_security_group)

if __name__ == "__main__":
    # pylint: disable=unexpected-keyword-arg,no-value-for-parameter
    cli(obj={})
