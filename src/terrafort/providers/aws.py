import click

from terrafort.resources.aws_db_instance import AwsDbInstance
from terrafort.resources.aws_iam_instance_profile import AwsIamInstanceProfile
from terrafort.resources.aws_instance import AwsInstance
from terrafort.resources.aws_security_group import AwsSecurityGroup


class Aws:

    @staticmethod
    @click.command('aws_security_group')
    @click.argument('group_id')
    @click.pass_obj
    def aws_security_group(ctx, group_id):
        """
        Create aws_security_group and all the attached aws_security_group_rules
        :param group_id:
        :return:
        """

        sg = AwsSecurityGroup(group_id)
        print(sg.render(ctx['commands']))


    @staticmethod
    @click.command('aws_instance')
    @click.argument('instance_id')
    def aws_instance(instance_id):
        """
        Create aws_instance
        """

        instance = AwsInstance(instance_id)
        print(instance.render())

    @staticmethod
    @click.command('aws_db_instance')
    @click.argument('db_identifier')
    def aws_db_instance(db_identifier):
        """
        Create aws_db_instance
        """

        instance = AwsDbInstance(db_identifier)
        print(instance.render())

    @staticmethod
    @click.command('aws_iam_instance_profile')
    @click.argument('profile_name')
    def aws_iam_instance_profile(profile_name):
        """
        Create aws_iam_instance_profile
        """
        template = AwsIamInstanceProfile(profile_name)
        print(template.render())
