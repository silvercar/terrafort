import boto3
from botocore.exceptions import ClientError

from terrafort.renderer import Renderer


class AwsDbInstance:
    """
    Create a template for an RDS instance
    """

    def __init__(self, db_identifier):
        self.client = boto3.client('rds')
        self.db_identifier = db_identifier

    def render(self):
        try:
            response = self.client.describe_db_instances(DBInstanceIdentifier=self.db_identifier)
            instance = response['DBInstances'][0]

            tags = self.client.list_tags_for_resource(ResourceName=instance['DBInstanceArn'])
            instance['Tags'] = tags['TagList']
        except ClientError as error:
            print(error)
            return None

        renderer = Renderer()
        output = renderer.render(instance, 'aws_db_instance.tf')

        return output
