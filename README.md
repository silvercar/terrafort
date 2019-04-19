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

First choose which AWS profile and region you want to use:
```
export AWS_PROFILE=my-profile
export AWS_DEFAULT_REGION=us-east-1
```

Then run terrafort:
`terrafort <resource> <id>`

For example:
`terrafort aws_db_instance my_db`

## Resources

This is a list of the resources that are currently supported:

- aws_iam_instance_profile
- aws_instance
- aws_db_instance
- aws_security_group

## Development

```bash
$ virtualenv venv --python=python3
$ . venv/bin/activate
$ pip3 install --editable .
$ terrafort
```