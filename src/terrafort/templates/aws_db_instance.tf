resource "aws_db_instance" "{{ resource.DBInstanceIdentifier }}" {

  allocated_storage = "{{ resource.AllocatedStorage }}"
  auto_minor_version_upgrade = "{{ resource.AutoMinorVersionUpgrade }}"
  availability_zone = "{{ resource.AvailabilityZone }}"
  backup_retention_period = "{{ resource.BackupRetentionPeriod }}"
  copy_tags_to_snapshot = "{{ resource.CopyTagsToSnapshot }}"
  identifier = "{{resource.DBInstanceIdentifier }}"
  instance_class = "{{ resource.DBInstanceClass }}"
  name = "{{ resource.DBName }}"

  parameter_group_name = "{{ resource.DBParameterGroups[0].DBParameterGroupName }}"
  db_subnet_group_name = "{{ resource.DBSubnetGroup.DBSubnetGroupName }}"
  deletion_protection = "{{ resource.DeletionProtection }}"
  enabled_cloudwatch_logs_exports = [
    {% for log in resource.EnabledCloudwatchLogsExports %}
    "{{ log }}",
    {% endfor %}
  ]
  port = "{{ resource.Endpoint.Port }}"
  engine = "{{ resource.Engine }}"
  engine_version = "{{ resource.EngineVersion }}"
  iam_database_authentication_enabled = "{{ resource.IAMDatabaseAuthenticationEnabled }}"
  iops = "{{ resource.Iops }}"
  username = "{{ resource.MasterUsername }}"
  monitoring_interval = "{{ resource.MonitoringInterval }}"
  monitoring_role_arn = "{{ resource.MonitoringRoleArn }}"
  multi_az = "{{ resource.MultiAZ }}"
  option_group_name = "{{ resource.OptionGroupMemberships[0].OptionGroupName }}"
  backup_window = "{{ resource.PreferredBackupWindow }}"
  maintenance_window = "{{ resource.PreferredMaintenanceWindow }}"
  publicly_accessible = "{{ resource.PubliclyAccessible }}"
  replicate_source_db = "{{ resource.ReadReplicaSourceDBInstanceIdentifier }}"
  storage_encrypted = "{{ resource.StorageEncrypted }}"
  storage_type = "{{ resource.StorageType }}"
  vpc_security_group_ids = [
    {% for group in resource.VpcSecurityGroups %}
    "{{ group.VpcSecurityGroupId }}",
    {% endfor %}
  ]


  tags {
    {% for tag in resource.Tags %}
    "{{ tag.Key }}" = "{{tag.Value}}"
    {% endfor %}
  }
}