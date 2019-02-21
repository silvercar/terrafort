resource "aws_instance" "{{ resource.InstanceId }}" {
  ami                   = "{{ resource.ImageId }}"
  key_name              = "{{ resource.KeyName }}"
  instance_type         = "{{ resource.InstanceType }}"
  iam_instance_profile  = "{{ resource.iam_instance_profile }}"
  security_groups       = ["{{ resource.SecurityGroups | join('","', attribute='GroupId') }}"]
  subnet_id             = "{{ resource.SubnetId }}"

  tags {
    {% for tag in resource.Tags %} "{{ tag.Key }}" = "{{tag.Value}}"
    {% endfor %}
  }
}