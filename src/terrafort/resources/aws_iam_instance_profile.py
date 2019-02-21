import boto3
from botocore.exceptions import ClientError

from terrafort.renderer import Renderer


class AwsIamInstanceProfile:

    def __init__(self, profile_name):
        self.client = boto3.client('iam')
        self.profile_name = profile_name

    def render(self):
        try:
            response = self.client.get_instance_profile(InstanceProfileName=self.profile_name)
        except ClientError as error:
            print(error)
            return None

        profile = response['InstanceProfile']

        renderer = Renderer()
        output = renderer.render(profile, 'aws_iam_instance_profile.tf')

        return output
