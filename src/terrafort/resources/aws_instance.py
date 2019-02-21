import boto3
from botocore.exceptions import ClientError

from terrafort.renderer import Renderer


class AwsInstance:
    """
    Create a template for an EC2 instance
    """

    def __init__(self, instance_id):
        self.ec2 = boto3.client('ec2')
        self.instance_id = instance_id

    def render(self):
        try:
            response = self.ec2.describe_instances(InstanceIds=[self.instance_id])
        except ClientError as error:
            print(error)
            return None

        instance = response['Reservations'][0]['Instances'][0]

        renderer = Renderer()
        output = renderer.render(instance, 'aws_instance.tf')

        return output
