# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example of how to upate Network Security Group objects
# for a given load balancer using the Python SDK.
#
# USAGE:
# `python examples/update_network_security_groups_example.py --compartment-id 'compartment.ocid' --vcn-id 'vcn.ocid' \
#     --subnet-id 'subnet.ocid.'`
#
# This script will create two Network Security Groups , One ipv6 load balancer.
# Update these nsgs to the newly created load balancer. Delete both the nsgs and then the load balancer.
#
# Required parameters:
#  --compartment-id    # compartment in which to create the NSG
#  --vcn-id    # VCN in which to create the NSG
#  --subnet-id    # Subnet for a new compute instance in the NSG
#

import oci
import argparse

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('--compartment-id',
                    help='compartment ID in which to perform the operation',
                    required=True
                    )
parser.add_argument('--vcn-id',
                    help='OCID of the VCN on which the network security group will be created',
                    required=True
                    )
parser.add_argument('--subnet-id',
                    help='OCID of the Subnet for an instance to be created and added to the network security group',
                    required=True
                    )
args = parser.parse_args()


def create_nsg(virtual_network_client, vcn_id, display_name, compartment_id):
    create_nsg_response = virtual_network_client.create_network_security_group(
        oci.core.models.CreateNetworkSecurityGroupDetails(
            display_name=display_name,
            compartment_id=compartment_id,
            vcn_id=vcn_id
        )
    ).data
    return create_nsg_response


def delete_nsg(virtual_network_client, nsg_id):
    delete_nsg_response = virtual_network_client.delete_network_security_group(nsg_id).data
    return delete_nsg_response


# ---------- assign provided arguments
compartment_id = args.compartment_id
vcn_id = args.vcn_id
subnet_id = args.subnet_id

# ---------- read config from file
config = oci.config.from_file()
load_balancer_client = oci.load_balancer.LoadBalancerClient(config)
load_balancer_client_composite_ops = oci.load_balancer.LoadBalancerClientCompositeOperations(load_balancer_client)
compute_client = oci.core.ComputeClient(config)
virtual_network_client = oci.core.VirtualNetworkClient(config)

# ---------- common varialbes
life_cycle_succeed_state = oci.load_balancer.models.WorkRequest.LIFECYCLE_STATE_SUCCEEDED

print("==================")
print('Going to create a load balancer.')
print("==================")

# Create load balancer
load_balancer = load_balancer_client_composite_ops.create_load_balancer_and_wait_for_state(
    oci.load_balancer.models.CreateLoadBalancerDetails(
        compartment_id=compartment_id,
        display_name='lbr_python-sdk-update_nsg_for_lb_example',
        is_private=True,
        shape_name='100Mbps',
        ip_mode="IPV4",
        subnet_ids=[subnet_id]
    ),
    [life_cycle_succeed_state]
)

load_balancer_ocid = load_balancer.data.id

print('Created Load Balancer %s' % load_balancer_ocid)

# Create Network Security Group objects
print("==================")
print("Creating network security group")
print("==================")
new_nsg_1 = create_nsg(virtual_network_client, vcn_id, 'nsg_python-sdk-update_nsg_for_lb_example_1', compartment_id)
nsg_id_1 = new_nsg_1.id
print("==================")
print("Created network security group {}".format(nsg_id_1))
print("==================")
print("Creating second network security group")
print("==================")
new_nsg_2 = create_nsg(virtual_network_client, vcn_id, "nsg_python-sdk-update_nsg_for_lb_example_2", compartment_id)
nsg_id_2 = new_nsg_2.id
print("==================")
print("Created second network security group {}".format(nsg_id_2))
print("==================")
print("Going to update network security group ids to assosiate with load balacer {}".format(load_balancer_ocid))
print("==================")

# Update nsg api call

load_balancer_client_composite_ops.update_network_security_groups_and_wait_for_state(
    oci.load_balancer.models.UpdateNetworkSecurityGroupsDetails(
        network_security_group_ids=[nsg_id_1, nsg_id_2]
    ),
    load_balancer_ocid,
    wait_for_states=[life_cycle_succeed_state]
)

print("Succesfully updated the load balancer with network security group ids.")

print("==================")

# We now delete the load balancer
print("Attempting to delete load balancer {}".format(load_balancer_ocid))
print('\n================================\n')
load_balancer_client_composite_ops.delete_load_balancer_and_wait_for_state(
    load_balancer_ocid,
    wait_for_states=[life_cycle_succeed_state])
print('Deleted Load Balancer')

# Delete the NSG

print("==================")
print("Deleting nsg {}".format(nsg_id_1))
print("==================")
delete_nsg(
    virtual_network_client,
    nsg_id_1)
print("Succesfully deleted nsg {}".format(nsg_id_1))
print("==================")
print("Deleting nsg {}".format(nsg_id_2))
print("==================")
delete_nsg(
    virtual_network_client,
    nsg_id_2)
print("Succesfully deleted nsg {}".format(nsg_id_2))
print("==================")


print('Script finished.')
