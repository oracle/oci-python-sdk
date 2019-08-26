# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

# This script provides an example of how use database CLI in terms of:
#   - Creating a Vm Cluster Network at Customer Cloud

# Usage: python exacc_vmcluster_example.py <Compartment OCID> <OCID of the Exadata Infrastructure> <OCID of the Vm Cluster Network> <The path to the public SSH key>

# This script takes the following arguments:
#
#   * The compartment in which infrastructure will be created
#   * OCID of the Exadata Infrastructure


import oci
import os.path
import sys
import random
import string


def random_string(elements, num):
    result = ''
    for _ in range(num):
        result += random.choice(elements)
    return result


display_name = 'VmCluster_Network_'.join(random_string(string.ascii_lowercase, 8))
if len(sys.argv) < 5:
    print("Missing the required arguments! an OCID of the compartment, OCID of the Exadata Infrastructure, OCID of the Vm Cluster Network  and The path to the public SSH key which can be used for SSHing into the Vm Cluster")

cpuCoreCount = 22
giVersion = '18.0.0.0'
displayName = 'vmcluster'


compartment_id = sys.argv[1]
exadata_infrastructure_id = sys.argv[2]
vm_cluster_network_id = sys.argv[3]
ssh_public_key_path = os.path.expandvars(os.path.expanduser(sys.argv[4]))


config = oci.config.from_file()
client = oci.database.DatabaseClient(config)
client_composite_ops = oci.database.DatabaseClientCompositeOperations(client)

with open(ssh_public_key_path, mode='r') as file:
    ssh_key = file.read()

create_vm_cluster_details = oci.database.models.CreateVmClusterDetails(
    compartment_id=compartment_id,
    cpu_core_count=cpuCoreCount,
    display_name=displayName,
    exadata_infrastructure_id=exadata_infrastructure_id,
    gi_version=giVersion,
    ssh_public_keys=[ssh_key],
    vm_cluster_network_id=vm_cluster_network_id
)


# Create Vm Cluster
# We can wait until the Vm Cluster is in AVAILABLE state.

life_cycle_creation_succeed_state = oci.database.models.VmClusterSummary.LIFECYCLE_STATE_AVAILABLE
vm_cluster = client_composite_ops.create_vm_cluster_and_wait_for_state(create_vm_cluster_details)


vm_cluster_ocid = vm_cluster.data.id

new_license_model = oci.database.models.UpdateVmClusterDetailsLICENSE_MODEL_LICENSE_INCLUDED

update_vm_cluster_details = oci.database.models.UpdateVmClusterDetails(
    license_model=new_license_model
)

vm_cluster_updated = client_composite_ops.update_vm_cluster_and_wait_for_state(vm_cluster_ocid, update_vm_cluster_details, [life_cycle_creation_succeed_state])

print(vm_cluster_updated.data)

life_cycle_deletion_succeed_state = oci.database.models.VmClusterSummary.LIFECYCLE_STATE_TERMINATED
vm_cluster_deleted = client_composite_ops.delete_vm_cluster_and_wait_for_state(vm_cluster_ocid, [life_cycle_deletion_succeed_state])

print(vm_cluster_deleted.data)

print('Terminated Vm Cluster')
