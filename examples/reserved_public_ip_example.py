# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example on how to work with reserved and ephemeral public IPs in the Python SDK by:
#
#   - Creating a reserved public IP, assigning it to a private IP and unassigning it from a private IP
#   - Creating an ephemeral private IP
#
# This script accepts three arguments:
#   - The first argument is the compartment where we'll create the public IPs and required resources for this script
#   - The second argument is the availability domain where we'll create a subnet and instance
#   - The third argument is the image ID which we'll use to launch the instance
#
# The following supporting resources will be created by this script:
#   - A VCN and subnet
#   - An instance (so we can assign public IPs to VNICs on the instance)
# These supporting resources will be deleted at the end of the script

import oci
import sys


def create_vcn_and_subnet(virtual_network, compartment_id, availability_domain):
    # Create a VCN
    vcn_name = 'python_sdk_test_vcn'
    cidr_block = "10.0.0.0/16"
    result = virtual_network.create_vcn(
        oci.core.models.CreateVcnDetails(
            cidr_block=cidr_block,
            display_name=vcn_name,
            compartment_id=compartment_id
        )
    )

    vcn = oci.wait_until(
        virtual_network,
        virtual_network.get_vcn(result.data.id),
        'lifecycle_state',
        'AVAILABLE',
        max_wait_seconds=300
    ).data
    print('Created VCN')

    # Create a subnet
    subnet_name = 'python_sdk_test_subnet1'
    subnet_cidr_block1 = "10.0.0.0/24"
    result = virtual_network.create_subnet(
        oci.core.models.CreateSubnetDetails(
            compartment_id=compartment_id,
            availability_domain=availability_domain,
            display_name=subnet_name,
            vcn_id=vcn.id,
            cidr_block=subnet_cidr_block1
        )
    )
    subnet = oci.wait_until(
        virtual_network,
        virtual_network.get_subnet(result.data.id),
        'lifecycle_state',
        'AVAILABLE',
        max_wait_seconds=300
    ).data
    print('Created subnet')

    return {'vcn': vcn, 'subnet': subnet}


def delete_vcn_and_subnet(virtual_network, vcn_and_subnet):
    composite_virtual_network = oci.core.VirtualNetworkClientCompositeOperations(virtual_network)
    vcn = vcn_and_subnet['vcn']
    subnet = vcn_and_subnet['subnet']

    composite_virtual_network.delete_subnet_and_wait_for_state(
        subnet.id,
        [oci.core.models.Subnet.LIFECYCLE_STATE_TERMINATED]
    )

    composite_virtual_network.delete_vcn_and_wait_for_state(
        vcn.id,
        [oci.core.models.Vcn.LIFECYCLE_STATE_TERMINATED]
    )


def launch_instance(compute, compartment_id, subnet, image_id):
    create_instance_details = oci.core.models.LaunchInstanceDetails()
    create_instance_details.compartment_id = compartment_id
    create_instance_details.availability_domain = subnet.availability_domain
    create_instance_details.display_name = 'pub_ip_test_instance'
    create_instance_details.create_vnic_details = oci.core.models.CreateVnicDetails(
        subnet_id=subnet.id,
        # We don't assign a public IP here so that we can demonstrate public IP functionality later on
        # in the script
        assign_public_ip=False
    )
    create_instance_details.image_id = image_id
    create_instance_details.shape = 'VM.Standard1.1'

    result = compute.launch_instance(create_instance_details)
    instance_ocid = result.data.id

    get_instance_response = oci.wait_until(
        compute,
        compute.get_instance(instance_ocid),
        'lifecycle_state',
        'RUNNING',
        max_wait_seconds=600
    )
    print('Launched instance')

    return get_instance_response.data


def terminate_instance(compute, instance):
    compute.terminate_instance(instance.id)
    oci.wait_until(
        compute,
        compute.get_instance(instance.id),
        'lifecycle_state',
        'TERMINATED',
        max_wait_seconds=600,
        succeed_on_not_found=True
    )


if len(sys.argv) != 4:
    raise RuntimeError('This script needs to be provided a compartment ID, an availability domain and an image OCID')

compartment_id = sys.argv[1]
availability_domain = sys.argv[2]
image_id = sys.argv[3]

# Default config file and profile
config = oci.config.from_file()
virtual_network = oci.core.VirtualNetworkClient(config)
compute = oci.core.ComputeClient(config)

vcn_and_subnet = create_vcn_and_subnet(virtual_network, compartment_id, availability_domain)
instance = launch_instance(compute, compartment_id, vcn_and_subnet['subnet'], image_id)

# First we'll create a reserved public IP. This does not have to be assigned to a private IP at create time, although
# it can be by specifying a private_ip_id in CreatePublicIpDetails.
create_public_ip_response = virtual_network.create_public_ip(
    oci.core.models.CreatePublicIpDetails(
        compartment_id=compartment_id,
        display_name='py_sdk_example_res_ip',
        lifetime='RESERVED'
    )
)
print('Created Public IP: {}'.format(create_public_ip_response.data))
print('\n================================\n')

# A Public IP has a lifecycle state, so we can wait until it is available or assigned to a private IP. If we
# need to wait on multiple states, we can use the evaluate_response parameter on the waiter.
get_public_ip_response = oci.wait_until(
    virtual_network,
    virtual_network.get_public_ip(create_public_ip_response.data.id),
    evaluate_response=lambda r: r.data.lifecycle_state in ['AVAILABLE', 'ASSIGNED']
)
public_ip = get_public_ip_response.data
print('Public IP after waiting: {}'.format(public_ip))
print('\n================================\n')

# We can list public IPs. When doing this, we need to provide a scope - for reserved public IPs the scope is
# REGION. Since listing public IPs is a paginated operation, we can use the functionality in oci.pagination
# to get all results
all_region_scoped_public_ips = oci.pagination.list_call_get_all_results(
    virtual_network.list_public_ips,
    'REGION',
    compartment_id
)
print('All reserved public IPs: {}'.format(all_region_scoped_public_ips.data))
print('\n================================\n')

# We'll now assign the public IP to the private IP from the instance we launched earlier. First we'll need to
# get the ID of the private IP
vnic_attachments = compute.list_vnic_attachments(compartment_id, instance_id=instance.id).data
vnic_id = vnic_attachments[0].vnic_id
private_ip_id = virtual_network.list_private_ips(vnic_id=vnic_id).data[0].id

# Now we can update the public IP to link it to the private IP. Once the update has been requested, we can
# use a waiter to wait until the public IP enters the appropriate state
virtual_network.update_public_ip(
    public_ip.id,
    oci.core.models.UpdatePublicIpDetails(
        private_ip_id=private_ip_id
    )
)
updated_public_ip = oci.wait_until(
    virtual_network,
    virtual_network.get_public_ip(public_ip.id),
    evaluate_response=lambda r: r.data.lifecycle_state in ['AVAILABLE', 'ASSIGNED']
)
print('Updated public IP: {}'.format(updated_public_ip.data))
print('\n================================\n')

# We can also unassign the public IP from any private IP by passing an empty string as the private_ip_id
# when doing the update. Note that the states we wait on after the update has been requested
virtual_network.update_public_ip(
    public_ip.id,
    oci.core.models.UpdatePublicIpDetails(
        private_ip_id=''
    )
)
updated_public_ip = oci.wait_until(
    virtual_network,
    virtual_network.get_public_ip(public_ip.id),
    evaluate_response=lambda r: r.data.lifecycle_state in ['AVAILABLE', 'UNASSIGNED']
)

# If we are done with the public IP, we can delete it
virtual_network.delete_public_ip(public_ip.id)
print('Deleted reserved public IP')

# We can also create an ephemeral public IP. For this type of public IP we need to assign it to a private IP
# at creation time
create_public_ip_response = virtual_network.create_public_ip(
    oci.core.models.CreatePublicIpDetails(
        compartment_id=compartment_id,
        display_name='py_sdk_example_eph_ip',
        lifetime='EPHEMERAL',
        private_ip_id=private_ip_id
    )
)
print('Created Public IP: {}'.format(create_public_ip_response.data))
print('\n================================\n')

get_public_ip_response = oci.wait_until(
    virtual_network,
    virtual_network.get_public_ip(create_public_ip_response.data.id),
    evaluate_response=lambda r: r.data.lifecycle_state in ['AVAILABLE', 'ASSIGNED']
)
public_ip = get_public_ip_response.data
print('Public IP after waiting: {}'.format(public_ip))
print('\n================================\n')

# We can list public IPs. When doing this, we need to provide a scope - for ephemeral public IPs the scope is
# AVAILABILITY_DOMAIN. We can also provide the availability domain we want to retrieve public IPs for.
# Since listing public IPs is a paginated operation, we can use the functionality in oci.pagination
# to get all results
all_ad_scoped_public_ips = oci.pagination.list_call_get_all_results(
    virtual_network.list_public_ips,
    'AVAILABILITY_DOMAIN',
    compartment_id,
    availability_domain=availability_domain
)
print('All ephemeral public IPs in {}: {}'.format(availability_domain, all_ad_scoped_public_ips.data))
print('\n================================\n')

# We can delete an ephemeral public IP, but it will also disappear when we terminate the instance
terminate_instance(compute, instance)
oci.wait_until(
    virtual_network,
    get_public_ip_response,
    'lifecycle_state',
    'TERMINATED',
    succeed_on_not_found=True
)
print('Terminated instance - ephemeral public IP also deleted')
delete_vcn_and_subnet(virtual_network, vcn_and_subnet)
print('Script finished')
