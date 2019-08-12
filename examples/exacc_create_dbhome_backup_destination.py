# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

# This script provides an example of how use database CLI in terms of:
#   - Creating a DbHome within a given VmCluster with BackupDestination

# Usage: python exacc_create_dbhome_backup_destination.py <OCID of a VmCluster> <OCID of compartment>

import oci
import sys
import random
import string


def random_string(elements, num):
    result = ''
    for _ in range(num):
        result += random.choice(elements)
    return result


if len(sys.argv) < 3:
    print("Missing arguments! an OCID for a VmCluster and compartment OCID are the required arguments")


vm_cluster_id = sys.argv[1]
db_name = ''.join(random_string(string.ascii_lowercase, 8))
db_unique_name = db_name + '_' + ''.join(random_string(string.ascii_lowercase, 20))
admin_password = '_#' + ''.join(random_string(string.ascii_lowercase + string.ascii_uppercase + string.digits + "_-#", 16))

config = oci.config.from_file()
db_client = oci.database.DatabaseClient(config)
compartment_id = sys.argv[2]


def create_backup_destination():
    backup_destination_request = oci.database.models.CreateNFSBackupDestinationDetails()

    backup_destination_request.compartment_id = compartment_id
    backup_destination_request.display_name = "PYSDK-EXAMPLE"
    backup_destination_request.local_mount_point_path = "Users/path"

    backup_destination_response = db_client.create_backup_destination(
        create_backup_destination_details=backup_destination_request)

    backup_destination = backup_destination_response.data
    print("Created Backup Destination {}".format(backup_destination))

    return backup_destination


backup_destination = create_backup_destination()

backup_destination_details = oci.database.models.BackupDestinationDetails()
backup_destination_details.id = backup_destination.id
backup_destination_details.type = backup_destination_details.TYPE_NFS

backup_destination_list = [backup_destination_details]

db_backup_config = oci.database.models.db_backup_config.DbBackupConfig(
    backup_destination_details=backup_destination_list
)


create_database_details = oci.database.models.CreateDatabaseDetails(
    db_name=db_name,
    db_unique_name=db_unique_name,
    admin_password=admin_password,
    db_backup_config=db_backup_config
)

create_db_home_details = oci.database.models.CreateDbHomeWithVmClusterIdDetails(
    source='VM_CLUSTER_NEW',
    vm_cluster_id=vm_cluster_id,
    display_name=''.join(random_string(string.ascii_lowercase + ' ', 32)),
    db_version='18.0.0.0',
    database=create_database_details
)

response = db_client.create_db_home(create_db_home_details)

print(response.data)
# ExaCC DB_Home with backup destination is created
