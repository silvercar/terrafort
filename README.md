# Terrafort

Terraform + Import = Terrafort!

Create terraform templates for existing resources. Unlike other tools like [terraforming](http://terraforming.dtan4.net/),
Terrafort allows you to import individual resources instead of entire resource groups.

## Requirements

- Python 3
- Terraform (only needed to run `terraform fmt` on output)

## Setup

`pip3 install git+https://github.com/silvercar/terrafort`

## Usage

First choose which AWS profile you want to use:
`export AWS_PROFILE=my-profile`

Then run terrafort:
`terrafort <resource> <id>`

## Resources

### Security groups

Create a template containing an `aws_security_group` resource, as well as one `aws_security_group_rule` 
resource for every rule attached to the security group. Each rule will have the same name as the security
group with a number suffix.

Example:

`terrafort sg sg-0123abc >> security_groups.tf`

Then, import the group and rules into the terraform state file:

`terraform import aws_security_group.my-group sg-0123abc`



## Development

```bash
$ virtualenv venv --python=python3
$ . venv/bin/activate
$ pip3 install --editable .
$ terrafort
```