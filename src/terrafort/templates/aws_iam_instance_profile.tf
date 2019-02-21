resource "aws_iam_instance_profile" "{{ resource.InstanceProfileName }}" {
  name = "{{ resource.InstanceProfileName }}"
  role = "{{ resource.Roles[0].RoleName }}"
}