# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides an example of how use database CLI in terms of:
#   - Retrieving a list of DbHomes within a given VmCluster
#

# Usage: python exacc_dbhome_list_example.py <OCID of a VmCluster>

import oci
import sys

if len(sys.argv) < 2:
    print("Missing argument! an OCID for a VmCluster")

vm_cluster_id = sys.argv[1]

config = oci.config.from_file()
client = oci.database.DatabaseClient(config)

get_vm_cluster_response = client.get_vm_cluster(vm_cluster_id=vm_cluster_id)
compartment_id = get_vm_cluster_response.data.compartment_id

response = client.list_db_homes(vm_cluster_id=vm_cluster_id, compartment_id=compartment_id)

print(response.data)
