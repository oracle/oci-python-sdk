# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example of how to create and modify Network Security Group objects
# for a given VCN and VNIC using the Python SDK.
#
# USAGE:
# `python examples/network_security_groups_example.py --compartment-id 'compartment.ocid' --vcn-id 'vcn.ocid' \
#     --subnet-id 'subnet.ocid.' --image-id 'image.ocid' --availability-domain 'aaBCD:PHX-AD-1' --display-name 'myNSG'`
#
# This script will create two Network Security Groups, assign a set of security rules to the first, create a new compute
# instance with its primary VNIC in the first NSG, attach the second NSG to the primary VNIC of the compute instance,
# remove the VNIC from the NSG, terminate the compute instance, and finally delete the NSG.
#
# Required parameters:
#  --compartment-id    # compartment in which to create the NSG
#  --vcn-id    # VCN in which to create the NSG
#  --subnet-id    # Subnet for a new compute instance in the NSG
#  --image-id    # Image for the new compute instance
#  --availability-domain    # AD for the new compute instance
#
# Optional Parameters:
#  --display-name    # A human-friendly name for the NSG


import oci
import argparse
import time

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
parser.add_argument('--availability-domain',
                    help='The availability domain for an instance to be created and added to the network security group',
                    required=True
                    )
parser.add_argument('--display-name',
                    help='display name for the network security group to be created',
                    required=False,
                    default='python-sdk-create-nsg-example'
                    )
parser.add_argument('--image-id',
                    help='OCID of the disk image to be used to create a new compute instance in the network security group',
                    required=True
                    )
args = parser.parse_args()


def create_nsg(virtual_network_client, vcn_id, display_name):
    create_nsg_response = virtual_network_client.create_network_security_group(
        oci.core.models.CreateNetworkSecurityGroupDetails(
            display_name=display_name,
            compartment_id=compartment_id,
            vcn_id=vcn_id
        )
    ).data
    return create_nsg_response


def update_nsg(virtual_network_client, nsg_id, display_name):
    update_nsg_response = virtual_network_client.update_network_security_group(
        nsg_id,
        oci.core.models.UpdateNetworkSecurityGroupDetails(
            display_name=display_name
        )
    ).data
    return update_nsg_response


def delete_nsg(virtual_network_client, nsg_id):
    delete_nsg_response = virtual_network_client.delete_network_security_group(nsg_id).data
    return delete_nsg_response


def add_nsg_rules(virtual_network_client, nsg_id, target_nsg_id):
    add_nsg_response = virtual_network_client.add_network_security_group_security_rules(
        nsg_id,
        oci.core.models.AddNetworkSecurityGroupSecurityRulesDetails(
            security_rules=[
                oci.core.models.AddSecurityRuleDetails(
                    description="Incoming SSH connections from private network",
                    direction="INGRESS",
                    is_stateless=False,
                    protocol="6",  # 1: ICMP, 6: TCP, 17: UDP, 58: ICMPv6
                    source="10.0.0.0/24",
                    source_type="CIDR_BLOCK",
                    tcp_options=oci.core.models.TcpOptions(destination_port_range=oci.core.models.PortRange(min=22, max=22))),
                oci.core.models.AddSecurityRuleDetails(
                    description="Incoming Internet connections",
                    direction="INGRESS",
                    is_stateless=False,
                    protocol="6",  # 1: ICMP, 6: TCP, 17: UDP, 58: ICMPv6
                    source="0.0.0.0/0",
                    source_type="CIDR_BLOCK",
                    tcp_options=oci.core.models.TcpOptions(destination_port_range=oci.core.models.PortRange(min=443, max=443))),
                oci.core.models.AddSecurityRuleDetails(
                    description="Outgoing connections to app service described by network security group",
                    direction="EGRESS",
                    is_stateless=False,
                    protocol="6",  # 1: ICMP, 6: TCP, 17: UDP, 58: ICMPv6
                    destination=target_nsg_id,
                    destination_type="NETWORK_SECURITY_GROUP",
                    tcp_options=oci.core.models.TcpOptions(destination_port_range=oci.core.models.PortRange(min=8080, max=8080)))
            ])
    ).data
    return add_nsg_response


def remove_nsg_rule(virtual_network_client, nsg_id, rule_id):
    remove_nsg_rule_response = virtual_network_client.remove_network_security_group_security_rules(
        nsg_id,
        oci.core.models.RemoveNetworkSecurityGroupSecurityRulesDetails(
            security_rule_ids=[rule_id])
    ).data
    return remove_nsg_rule_response


def get_nsg(virtual_network_client, nsg_id):
    nsg = virtual_network_client.get_network_security_group(nsg_id).data
    return nsg


def get_nsg_rules(virtual_network_client, nsg_id):
    nsg_rules = virtual_network_client.list_network_security_group_security_rules(nsg_id).data
    return nsg_rules


def update_nsgs_in_vnic(virtual_network_client, nsg_id, nsg_id_2, vnic_id):
    add_nsg_to_vnic_response = virtual_network_client.update_vnic(
        vnic_id,
        oci.core.models.UpdateVnicDetails(
            nsg_ids=[nsg_id, nsg_id_2]
        )
    ).data
    return add_nsg_to_vnic_response


def remove_all_nsgs_from_vnic(virtual_network_client, vnic_id):
    add_nsg_to_vnic_response = virtual_network_client.update_vnic(
        vnic_id,
        oci.core.models.UpdateVnicDetails(
            nsg_ids=[]
        )
    ).data
    return add_nsg_to_vnic_response


def list_vnics_in_nsg(virtual_network_client, nsg_id):
    list_vnics_in_nsg_response = virtual_network_client.list_network_security_group_vnics(
        nsg_id
    ).data
    return list_vnics_in_nsg_response


def launch_instance_in_nsg(virtual_network_client,
                           compute_client,
                           availability_domain,
                           subnet_id,
                           image_id):

    launch_instance_details = oci.core.models.LaunchInstanceDetails(
        display_name="NSG Example Instance",
        compartment_id=compartment_id,
        availability_domain=availability_domain,
        shape='VM.Standard2.1',
        source_details=oci.core.models.InstanceSourceViaImageDetails(image_id=image_id),
        create_vnic_details=oci.core.models.CreateVnicDetails(
            subnet_id=subnet_id,
            nsg_ids=[nsg_id, nsg_id_2]
        )
    )
    launch_instance_response = compute_client.launch_instance(launch_instance_details)
    instance = launch_instance_response.data
    oci.wait_until(
        compute_client,
        compute_client.get_instance(instance.id),
        'lifecycle_state',
        'RUNNING',
        max_wait_seconds=1200,
        succeed_on_not_found=False
    )
    return launch_instance_response


def terminate_instance(compute_client, instance):
    compute_client.terminate_instance(instance.id)
    oci.wait_until(
        compute_client,
        compute_client.get_instance(instance.id),
        'lifecycle_state',
        'TERMINATED',
        max_wait_seconds=1200,
        succeed_on_not_found=True
    )


# ---------- assign provided arguments
compartment_id = args.compartment_id
vcn_id = args.vcn_id
availability_domain = args.availability_domain
display_name = args.display_name
# vnic_id = args.vnic_id
subnet_id = args.subnet_id
image_id = args.image_id


# ---------- read config from file
config = oci.config.from_file()
compute_client = oci.core.ComputeClient(config)
virtual_network_client = oci.core.VirtualNetworkClient(config)

# Create Network Security Group objects
print("==================")
print("Creating network security group")
print("==================")
new_nsg = create_nsg(virtual_network_client, vcn_id, display_name)
nsg_id = new_nsg.id
print("==================")
print("Created network security group {}".format(nsg_id))
print("==================")
time.sleep(2)
print("==================")
print("Creating second network security group")
print("==================")
new_nsg_2 = create_nsg(virtual_network_client, vcn_id, "Second network security group")
nsg_id_2 = new_nsg_2.id
print("==================")
print("Created second network security group {}".format(nsg_id_2))
print("==================")
time.sleep(2)

# Retrieve the network security group and display
print("==================")
print("Retrieving network security group details")
print("==================")
created_nsg = get_nsg(virtual_network_client, nsg_id)
print(created_nsg)
time.sleep(2)

# Add new rules
print("==================")
print("Adding security rules")
print("==================")
add_nsg_rules(
    virtual_network_client,
    nsg_id,
    nsg_id_2)
time.sleep(2)
print("==================")
print("Retrieving rules")
print("==================")
rules = get_nsg_rules(virtual_network_client, nsg_id)
print(rules)
rule_id = rules[0].id
time.sleep(2)

# Remove rule selected above
print("==================")
print("Removing first rule")
print("==================")
remove_nsg_rule(
    virtual_network_client,
    nsg_id,
    rule_id)
updated_rules = get_nsg_rules(virtual_network_client, nsg_id)
print(updated_rules)
time.sleep(2)

# # Launch a new instance with its primary VNIC in the NSG
print("==================")
print("Launching a compute instance with primary VNIC in the network security group")
print("==================")
created_instance = launch_instance_in_nsg(virtual_network_client,
                                          compute_client,
                                          availability_domain,
                                          subnet_id,
                                          image_id).data
print(created_instance)
time.sleep(2)

print("==================")
print("Attaching a second network security group to a VNIC")
print("==================")
vnic_attachments = compute_client.list_vnic_attachments(compartment_id, instance_id=created_instance.id).data
vnic_id = vnic_attachments[0].vnic_id
# Associate an existing VNIC with this NSG
update_nsgs_in_vnic(
    virtual_network_client,
    nsg_id,
    nsg_id_2,
    vnic_id)
time.sleep(2)

print("==================")
print("List all VNICs in the network security group")
print("==================")
vnics_in_nsg = list_vnics_in_nsg(virtual_network_client, nsg_id)
print(vnics_in_nsg)
time.sleep(2)

# Remove NSGs from the existing VNIC
print("==================")
print("Remove all VNICs from the network security group")
print("==================")
remove_all_nsgs_from_vnic(
    virtual_network_client,
    vnic_id)
time.sleep(2)

# Terminate compute instance
print("==================")
print("Terminating compute instance {}".format(created_instance.id))
print("==================")
terminate_instance(compute_client, created_instance)

# Delete the NSG

print("Deleting {}".format(nsg_id))
delete_nsg(
    virtual_network_client,
    nsg_id)
time.sleep(2)
print("Deleting {}".format(nsg_id_2))
delete_nsg(
    virtual_network_client,
    nsg_id_2)
