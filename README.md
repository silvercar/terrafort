# Terrafort

[![CircleCI](https://circleci.com/gh/silvercar/terrafort/tree/master.svg?style=svg)](https://circleci.com/gh/silvercar/terrafort/tree/master)

Terraform + Import = Terrafort!

Terrafort creates terraform templates for existing resources. Unlike other tools like [terraforming](http://terraforming.dtan4.net/),
Terrafort allows you to create templates for individual resources instead of entire resource groups.

Terrafort will not interact with any terraform state files, but some resources are capable of
generating `terraform import` commands for you. Example:

```bash
$ terrafort --commands aws_security_group sg-12345
terraform import aws_security_group.my-sg sg-12345
terraform import aws_security_group_rule.my-sg-1 sg-12345_ingress_tcp_6379_6379_sg-0abcd123

```

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
`terrafort [--commands] <resource> <id>`

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