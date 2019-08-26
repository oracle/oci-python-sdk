# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

# This script provides an example of how use database CLI in terms of:
#   - Creating a DbHome within a given VmCluster

# Usage: python exacc_dbhome_create_example.py <OCID of a VmCluster>

import oci
import sys
import random
import string


def random_string(elements, num):
    result = ''
    for _ in range(num):
        result += random.choice(elements)
    return result


if len(sys.argv) < 2:
    print("Missing argument! an OCID for a VmCluster")

vm_cluster_id = sys.argv[1]
db_name = ''.join(random_string(string.ascii_lowercase, 8))
db_unique_name = db_name + '_' + ''.join(random_string(string.ascii_lowercase, 20))
admin_password = '_#' + ''.join(random_string(string.ascii_lowercase + string.ascii_uppercase + string.digits + "_-#", 16))

config = oci.config.from_file()
client = oci.database.DatabaseClient(config)

create_database_details = oci.database.models.CreateDatabaseDetails(
    db_name=db_name,
    db_unique_name=db_unique_name,
    admin_password=admin_password
)

create_db_home_details = oci.database.models.CreateDbHomeWithVmClusterIdDetails(
    source='VM_CLUSTER_NEW',
    vm_cluster_id=vm_cluster_id,
    display_name=''.join(random_string(string.ascii_lowercase + ' ', 32)),
    db_version='18.0.0.0',
    database=create_database_details
)

response = client.create_db_home(create_db_home_details)

print(response.data)
