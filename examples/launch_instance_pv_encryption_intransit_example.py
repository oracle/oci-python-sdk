# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example of how to launch an instance with pvEncryptionInTransit on using the Python SDK.
# This script will:
#
#   * Create a VCN, subnet and internet gateway. This will enable the instance to connect to the public internet.
#     If this is not desired then the internet gateway (and associated route rule) don't need to be created.
#   * Launch an instance. Certain assumptions are made about launching the instance
#       - The instance launched will have a shape of VM.Standard2.1
#       - The instance launched will use an Oracle Linux 7.5 image
#
# Resources created by the script will be removed when the script is done.
#
# This script takes the following arguments:
#
#   * The display name for the instance
#   * The compartment which owns the instance
#   * The availability domain where the instance will be launched
#   * The CIDR block for the VCN and subnet (these will use the same CIDR)
#   * The path to the public SSH key which can be used for SSHing into the instance
#   * The KMS key id for boot volume encryption-in-transit

import oci
import os.path
import sys


def create_vcn(virtual_network, compartment_id, cidr_block):
    vcn_name = 'py_sdk_example_vcn'
    result = virtual_network.create_vcn(
        oci.core.models.CreateVcnDetails(
            cidr_block=cidr_block,
            display_name=vcn_name,
            compartment_id=compartment_id
        )
    )
    get_vcn_response = oci.wait_until(
        virtual_network,
        virtual_network.get_vcn(result.data.id),
        'lifecycle_state',
        'AVAILABLE'
    )
    print('Created VCN: {}'.format(get_vcn_response.data.id))

    return get_vcn_response.data


def delete_vcn(virtual_network, vcn):

    vn_composite_ops = oci.core.VirtualNetworkClientCompositeOperations(virtual_network)

    vn_composite_ops.delete_vcn_and_wait_for_state(vcn.id,
                                                   wait_for_states=[oci.core.models.Vcn.LIFECYCLE_STATE_TERMINATED])

    print('Deleted VCN: {}'.format(vcn.id))


def create_subnet(virtual_network, vcn, availability_domain):
    subnet_name = 'py_sdk_example_subnet1'
    result = virtual_network.create_subnet(
        oci.core.models.CreateSubnetDetails(
            compartment_id=vcn.compartment_id,
            availability_domain=availability_domain,
            display_name=subnet_name,
            vcn_id=vcn.id,
            cidr_block=vcn.cidr_block
        )
    )
    get_subnet_response = oci.wait_until(
        virtual_network,
        virtual_network.get_subnet(result.data.id),
        'lifecycle_state',
        'AVAILABLE'
    )
    print('Created Subnet: {}'.format(get_subnet_response.data.id))

    return get_subnet_response.data


def delete_subnet(virtual_network, subnet):
    vn_composite_ops = oci.core.VirtualNetworkClientCompositeOperations(virtual_network)

    vn_composite_ops.delete_subnet_and_wait_for_state(subnet.id,
                                                      wait_for_states=[oci.core.models.Subnet.LIFECYCLE_STATE_TERMINATED])

    print('Deleted Subnet: {}'.format(subnet.id))


def create_internet_gateway(virtual_network, vcn):
    internet_gateway_name = 'py_sdk_example_ig'
    result = virtual_network.create_internet_gateway(
        oci.core.models.CreateInternetGatewayDetails(
            display_name=internet_gateway_name,
            compartment_id=vcn.compartment_id,
            is_enabled=True,
            vcn_id=vcn.id
        )
    )
    get_internet_gateway_response = oci.wait_until(
        virtual_network,
        virtual_network.get_internet_gateway(result.data.id),
        'lifecycle_state',
        'AVAILABLE'
    )
    print('Created internet gateway: {}'.format(get_internet_gateway_response.data.id))

    add_route_rule_to_default_route_table_for_internet_gateway(
        virtual_network,
        vcn,
        get_internet_gateway_response.data
    )

    return get_internet_gateway_response.data


def delete_internet_gateway(virtual_network, internet_gateway):
    vn_composite_ops = oci.core.VirtualNetworkClientCompositeOperations(virtual_network)

    vn_composite_ops.delete_internet_gateway_and_wait_for_state(internet_gateway.id, wait_for_states=[oci.core.models.InternetGateway.LIFECYCLE_STATE_TERMINATED])

    print('Deleted Internet Gateway: {}'.format(internet_gateway.id))


# This makes sure that we use the internet gateway for accessing the internet. See:
# https://docs.cloud.oracle.com/Content/Network/Tasks/managingIGs.htm
# for more information.
#
# As a convenience, we'll add a route rule to the default route table. However, in your
# own code you may opt to use a different route table
def add_route_rule_to_default_route_table_for_internet_gateway(virtual_network, vcn, internet_gateway):
    get_route_table_response = virtual_network.get_route_table(vcn.default_route_table_id)
    route_rules = get_route_table_response.data.route_rules

    print('\nCurrent Route Rules For VCN')
    print('===========================')
    print('{}\n\n'.format(route_rules))

    # Updating route rules will totally replace any current route rules with what we send through.
    # If we wish to preserve any existing route rules, we need to read them out first and then send
    # them back to the service as part of any update
    route_rules.append(
        oci.core.models.RouteRule(
            cidr_block=None,
            destination='0.0.0.0/0',
            destination_type='CIDR_BLOCK',
            network_entity_id=internet_gateway.id
        )
    )

    virtual_network.update_route_table(
        vcn.default_route_table_id,
        oci.core.models.UpdateRouteTableDetails(route_rules=route_rules)
    )

    get_route_table_response = oci.wait_until(
        virtual_network,
        virtual_network.get_route_table(vcn.default_route_table_id),
        'lifecycle_state',
        'AVAILABLE'
    )

    print('\nUpdated Route Rules For VCN')
    print('===========================')
    print('{}\n\n'.format(get_route_table_response.data.route_rules))

    return get_route_table_response.data


def clear_route_rules_from_default_route_table(virtual_network, vcn):
    virtual_network.update_route_table(
        vcn.default_route_table_id,
        oci.core.models.UpdateRouteTableDetails(route_rules=[])
    )
    oci.wait_until(
        virtual_network,
        virtual_network.get_route_table(vcn.default_route_table_id),
        'lifecycle_state',
        'AVAILABLE'
    )
    print('Cleared route rules from route table: {}'.format(vcn.default_route_table_id))


def get_image(compute, operating_system, operating_system_version, shape):
    # Listing images is a paginated call, so we can use the oci.pagination module to get all results
    # without having to manually handle page tokens
    #
    # In this case, we want to find the image for the OS and version we want to run, and which can
    # be used for the shape of instance we want to launch
    list_images_response = oci.pagination.list_call_get_all_results(
        compute.list_images,
        compartment_id,
        operating_system=operating_system,
        operating_system_version=operating_system_version,
        shape=shape
    )

    # For demonstration, we just return the first image but for Production code you should have a better
    # way of determining what is needed
    return list_images_response.data[0]


if len(sys.argv) != 7:
    raise RuntimeError('Invalid number of arguments provided to the script. Consult the script header for required arguments')

instance_display_name = sys.argv[1]
compartment_id = sys.argv[2]
availability_domain = sys.argv[3]
cidr_block = sys.argv[4]
ssh_public_key_path = os.path.expandvars(os.path.expanduser(sys.argv[5]))
kms_key_id = sys.argv[6]

# Default config file and profile
config = oci.config.from_file()
compute_client = oci.core.ComputeClient(config)
virtual_network_client = oci.core.VirtualNetworkClient(config)

vcn = None
subnet = None
internet_gateway = None
try:
    vcn = create_vcn(virtual_network_client, compartment_id, cidr_block)
    subnet = create_subnet(virtual_network_client, vcn, availability_domain)
    internet_gateway = create_internet_gateway(virtual_network_client, vcn)

    image = get_image(compute_client, 'Oracle Linux', '7.5', 'VM.Standard2.1')

    with open(ssh_public_key_path, mode='r') as file:
        ssh_key = file.read()

    # We can use instance metadata to specify the SSH keys to be included in the
    # ~/.ssh/authorized_keys file for the default user on the instance via the special "ssh_authorized_keys" key.
    #
    # We can also provide arbitrary string keys and string values. If you are providing these, you should consider
    # whether defined and freeform tags on an instance would better meet your use case. See:
    # https://docs.cloud.oracle.com/Content/Identity/Concepts/taggingoverview.htm for more information
    # on tagging
    instance_metadata = {
        'ssh_authorized_keys': ssh_key,
        'some_metadata_item': 'some item value'
    }

    # Extended metadata differs from normal metadata in that it can support nested maps/dicts. If you are providing
    # these, you should consider whether defined and freeform tags on an instance would better meet your use case.
    instance_extended_metadata = {
        'string_key_1': 'string_value_1',
        'map_key_1': {
            'string_key_2': 'string_value_2',
            'map_key_2': {
                'string_key_3': 'string_value_3'
            },
            'empty_map_key': {}
        }
    }

    launch_instance_details = oci.core.models.LaunchInstanceDetails(
        display_name=instance_display_name,
        compartment_id=compartment_id,
        availability_domain=availability_domain,
        shape='VM.Standard2.1',
        metadata=instance_metadata,
        extended_metadata=instance_extended_metadata,
        is_pv_encryption_in_transit_enabled=True,
        source_details=oci.core.models.InstanceSourceViaImageDetails(image_id=image.id, kms_key_id=kms_key_id),
        create_vnic_details=oci.core.models.CreateVnicDetails(
            subnet_id=subnet.id
        )
    )

    launch_instance_response = compute_client.launch_instance(launch_instance_details)

    print('\nLaunched instance')
    print('===========================')
    print('{}\n\n'.format(launch_instance_response.data))

    get_instance_response = oci.wait_until(
        compute_client,
        compute_client.get_instance(launch_instance_response.data.id),
        'lifecycle_state',
        'RUNNING'
    )

    print('\nRunning instance')
    print('===========================')
    print('{}\n\n'.format(get_instance_response.data))

    # We can find the private and public IP address of the instance by getting information on its VNIC(s). This
    # relationship is indirect, via the VnicAttachments of an instance

    # Note that listing VNIC attachments is a paginated operation so we can use the oci.pagination module to avoid
    # having to manually deal with page tokens.
    #
    # Since we're only interested in our specific instance, we can pass that as a filter to the list operation
    list_vnic_attachments_response = oci.pagination.list_call_get_all_results(
        compute_client.list_vnic_attachments,
        compartment_id,
        instance_id=get_instance_response.data.id
    )

    vnic = virtual_network_client.get_vnic(list_vnic_attachments_response.data[0].vnic_id).data
    print('\nInstance IP Addresses')
    print('===========================')
    print('Private IP: {}'.format(vnic.private_ip))
    print('Public IP: {}\n\n'.format(vnic.public_ip))

    # Once we're done with the instance, we can terminate it and wait for it to be terminated. We also use
    # succeed_on_not_found for the waiter in case the instance is no longer returned by get_instance calls
    # as that implies our delete/termination has succeeded
    compute_client.terminate_instance(get_instance_response.data.id)
    oci.wait_until(
        compute_client,
        compute_client.get_instance(get_instance_response.data.id),
        'lifecycle_state',
        'TERMINATED',
        succeed_on_not_found=True
    )
finally:
    if internet_gateway:
        # Because the internet gateway is referenced by a route rule, the rule needs to be deleted before
        # we can remove the internet gateway
        clear_route_rules_from_default_route_table(virtual_network_client, vcn)
        delete_internet_gateway(virtual_network_client, internet_gateway)

    if subnet:
        delete_subnet(virtual_network_client, subnet)

    if vcn:
        delete_vcn(virtual_network_client, vcn)
