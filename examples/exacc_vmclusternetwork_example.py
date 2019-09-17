# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

# This script provides an example of how use database CLI in terms of:
#   - Creating a Vm Cluster Network at Customer Cloud

# Usage: python exacc_vmclusternetwork_example.py <Compartment OCID> <OCID of the Exadata Infrastructure>

# This script takes the following arguments:
#
#   * The compartment in which infrastructure will be created
#   * OCID of the Exadata Infrastructure


import oci
import sys
import random
import string


def random_string(elements, num):
    result = ''
    for _ in range(num):
        result += random.choice(elements)
    return result


display_name = 'VmCluster_Network_'.join(random_string(string.ascii_lowercase, 8))
if len(sys.argv) < 3:
    print("Missing the required arguments! an OCID of the compartment and OCID of the Exadata Infrastructure")

cidr = '192.168.10.0/16'
domain = 'oracleclient.com'
gateway = '192.168.10.1'
netmask = '255.255.0.0'
prefix = 'exacc'
vlanId = '223'
cidr2 = '172.168.10.0/16'
domain2 = 'oraclebkp.com'
gateway2 = '192.168.10.5'
netmask2 = '255.255.0.0'
prefix2 = 'exacc-bkp'
vlanId2 = '224'

compartment_id = sys.argv[1]
exadata_infrastructure_id = sys.argv[2]


config = oci.config.from_file()
client = oci.database.DatabaseClient(config)
client_composite_ops = oci.database.DatabaseClientCompositeOperations(client)

info_for_network_gen_details1 = oci.database.models.InfoForNetworkGenDetails(
    network_type=oci.database.models.InfoForNetworkGenDetails.NETWORK_TYPE_CLIENT,
    vlan_id=vlanId,
    cidr=cidr,
    gateway=gateway,
    netmask=netmask,
    domain=domain,
    prefix=prefix
)

info_for_network_gen_details2 = oci.database.models.InfoForNetworkGenDetails(
    network_type=oci.database.models.InfoForNetworkGenDetails.NETWORK_TYPE_BACKUP,
    vlan_id=vlanId2,
    cidr=cidr2,
    gateway=gateway2,
    netmask=netmask2,
    domain=domain2,
    prefix=prefix2
)

generate_recommended_network_details = oci.database.models.GenerateRecommendedNetworkDetails(
    compartment_id=compartment_id,
    display_name=display_name,
    networks=[info_for_network_gen_details1, info_for_network_gen_details2]
)


# Create Vm Cluster Network
# We can wait until the Vm Cluster Network is in REQUIRES_VALIDATION state.

life_cycle_creation_succeed_state = oci.database.models.VmClusterNetworkSummary.LIFECYCLE_STATE_REQUIRES_VALIDATION
vm_cluster_network = client_composite_ops.create_vm_cluster_network_and_wait_for_state(exadata_infrastructure_id, generate_recommended_network_details)


vm_cluster_network_ocid = vm_cluster_network.data.id


new_dns = ['210.89.138.33']

update_vm_cluster_network_details = oci.database.models.UpdateVmClusterNetworkDetails(
    dns=new_dns
)

vm_cluster_network_updated = client_composite_ops.update_vm_cluster_network_and_wait_for_state(exadata_infrastructure_id, vm_cluster_network_ocid, update_vm_cluster_network_details, [life_cycle_creation_succeed_state])

print(vm_cluster_network_updated.data)

life_cycle_validation_succeed_state = oci.database.models.VmClusterNetworkSummary.LIFECYCLE_STATE_VALIDATED
vm_cluster_network_validated = client_composite_ops.validate_vm_cluster_network_and_wait_for_state(exadata_infrastructure_id, vm_cluster_network_ocid, [life_cycle_validation_succeed_state])

print(vm_cluster_network_updated.data)

client.delete_vm_cluster_network(exadata_infrastructure_id, vm_cluster_network_ocid)
oci.wait_until(
    client,
    vm_cluster_network_updated,
    'lifecycle_state',
    'TERMINATED',
    succeed_on_not_found=True
)
print('Terminated Vm Cluster Network')
