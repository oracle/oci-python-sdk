# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example of how to use composite operations in the Python SDK. Composite operations provide
# convenience methods for operations which would otherwise need to be chained together.  For example, instead of performing an action
# on a resource and then using a waiter to wait for the resource to enter a given state, you can call a single method in
# a composite operation class to accomplish the same functionality.
#
# This example will use VCNs, subnets and load balancers to demonstrate composite operation functionality.
#
# This script accepts three arguments:
#   - The first argument is the compartment where we'll create the load balancer and related resources
#   - The second argument is the first availability domain where we'll create a subnet
#   - The third argument is a second (different) availability domain where we'll create a subnet

import oci
import sys


def create_vcn_and_subnets(virtual_network_client_composite_ops, compartment_id, first_ad, second_ad):
    # Here we use a composite operation to create a VCN and wait for it to enter the given state. Note that the
    # states are passed as an array so it is possible to wait on multiple states. The waiter will complete
    # (and the method will return) once the resource enters ANY of the provided states.
    get_vcn_response = virtual_network_client_composite_ops.create_vcn_and_wait_for_state(
        oci.core.models.CreateVcnDetails(
            cidr_block='10.0.0.0/16',
            display_name='PySdkCompositeOpExample',
            compartment_id=compartment_id
        ),
        [oci.core.models.Vcn.LIFECYCLE_STATE_AVAILABLE]
    )
    vcn = get_vcn_response.data
    print('Created VCN')

    get_subnet_response = virtual_network_client_composite_ops.create_subnet_and_wait_for_state(
        oci.core.models.CreateSubnetDetails(
            compartment_id=compartment_id,
            availability_domain=first_ad,
            display_name='PySdkCompositeOpsExampleSubnet1',
            vcn_id=vcn.id,
            cidr_block='10.0.0.0/24'
        ),
        [oci.core.models.Subnet.LIFECYCLE_STATE_AVAILABLE]
    )
    subnet_one = get_subnet_response.data
    print('Created Subnet 1')

    get_subnet_response = virtual_network_client_composite_ops.create_subnet_and_wait_for_state(
        oci.core.models.CreateSubnetDetails(
            compartment_id=compartment_id,
            availability_domain=second_ad,
            display_name='PySdkCompositeOpsExampleSubnet2',
            vcn_id=vcn.id,
            cidr_block='10.0.1.0/24'
        ),
        [oci.core.models.Subnet.LIFECYCLE_STATE_AVAILABLE]
    )
    subnet_two = get_subnet_response.data
    print('Created Subnet 2')

    return {'vcn': vcn, 'subnets': [subnet_one, subnet_two]}


def delete_vcn_and_subnets(virtual_network_client_composite_ops, vcn_and_subnets):
    vcn = vcn_and_subnets['vcn']
    subnet_one = vcn_and_subnets['subnets'][0]
    subnet_two = vcn_and_subnets['subnets'][1]

    virtual_network_client_composite_ops.delete_subnet_and_wait_for_state(
        subnet_one.id,
        [oci.core.models.Subnet.LIFECYCLE_STATE_TERMINATED]
    )
    print('Deleted Subnet 1')

    virtual_network_client_composite_ops.delete_subnet_and_wait_for_state(
        subnet_two.id,
        [oci.core.models.Subnet.LIFECYCLE_STATE_TERMINATED]
    )
    print('Deleted Subnet 2')

    virtual_network_client_composite_ops.delete_vcn_and_wait_for_state(
        vcn.id,
        [oci.core.models.Vcn.LIFECYCLE_STATE_TERMINATED]
    )
    print('Deleted VCN')


# Default config file and profile
config = oci.config.from_file()
load_balancer_client = oci.load_balancer.LoadBalancerClient(config)
load_balancer_client_composite_ops = oci.load_balancer.LoadBalancerClientCompositeOperations(load_balancer_client)
virtual_network_client = oci.core.VirtualNetworkClient(config)
virtual_network_client_composite_ops = oci.core.VirtualNetworkClientCompositeOperations(virtual_network_client)

if len(sys.argv) != 4:
    raise RuntimeError('This script needs to be provided a compartment ID and two availability domains')

compartment_id = sys.argv[1]
first_ad = sys.argv[2]
second_ad = sys.argv[3]

vcn_and_subnets = create_vcn_and_subnets(virtual_network_client_composite_ops, compartment_id, first_ad, second_ad)

# Load Balancer operations return work requests so when using composite operations we have to wait for the state of the
# work request (e.g. for it to succeed) rather than the state of the load balancer. However, as a convenience, when the
# composite operation completes we'll return information on the load balancer (if possible) rather than the work
# request
get_load_balancer_response = load_balancer_client_composite_ops.create_load_balancer_and_wait_for_state(
    oci.load_balancer.models.CreateLoadBalancerDetails(
        compartment_id=compartment_id,
        display_name='PySdkCompositeOpsExample',
        shape_name='100Mbps',
        subnet_ids=[s.id for s in vcn_and_subnets['subnets']]
    ),
    [oci.load_balancer.models.WorkRequest.LIFECYCLE_STATE_SUCCEEDED]
)
print('Created Load Balancer')

# Deleting a load balancer also returns a work request, so in this composite operation we have to wait on the
# state of the work request rather than the state of the load balancer
load_balancer_client_composite_ops.delete_load_balancer_and_wait_for_state(
    get_load_balancer_response.data.id,
    [oci.load_balancer.models.WorkRequest.LIFECYCLE_STATE_SUCCEEDED]
)
print('Deleted Load Balancer')

delete_vcn_and_subnets(virtual_network_client_composite_ops, vcn_and_subnets)
