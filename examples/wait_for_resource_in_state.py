# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides an example on how to use waiters in the Python SDK to block/wait until a resource (e.g. an instance, a VCN)
# reaches a certain state.

import oci

# Default config file and profile
config = oci.config.from_file()
compartment_id = '<Your compartment OCID here>'
availability_domain = '<An availability domain, e.g. crmS:IAD-AD-1, here>'
second_availability_domain = '<An availability domain, e.g. crmS:IAD-AD-2, here. This should be different to availability_domain>'

virtual_network_client = oci.core.VirtualNetworkClient(config)
load_balancer_client = oci.load_balancer.LoadBalancerClient(config)

# This creates a VCN and then waits until the VCN's lifecycle state is AVAILABLE
print('Creating VCN')
result = virtual_network_client.create_vcn(oci.core.models.CreateVcnDetails(cidr_block='10.0.0.0/16', display_name='WaitForResourceExampleVcn', compartment_id=compartment_id))
vcn_ocid = result.data.id
get_vcn_response = virtual_network_client.get_vcn(vcn_ocid)
wait_until_vcn_available_response = oci.wait_until(virtual_network_client, get_vcn_response, 'lifecycle_state', 'AVAILABLE')
print(wait_until_vcn_available_response.data)

# This creates a subnet in the VCN and waits until the subnet's lifecycle state is AVAILABLE
print('Creating Subnet 1')
result = virtual_network_client.create_subnet(
    oci.core.models.CreateSubnetDetails(
        compartment_id=compartment_id,
        availability_domain=availability_domain,
        display_name='WaitForResourceExampleSubnet',
        vcn_id=vcn_ocid,
        cidr_block='10.0.0.0/24'
    )
)
subnet_ocid = result.data.id
get_subnet_response = virtual_network_client.get_subnet(subnet_ocid)
wait_until_subnet_available_response = oci.wait_until(virtual_network_client, get_subnet_response, 'lifecycle_state', 'AVAILABLE')
print(wait_until_subnet_available_response.data)

# Here we use a variation of the wait_until function where instead of specifying the property and state we can pass in a function reference (either
# a reference to a defined function or a lambda) that returns a truthy value if the waiter should stop waiting and a falsey value if the waiter
# should continue waiting. This function will receive a single argument, which is the response received from calling the GET service operation.
#
# Using a function reference may be useful if you need logic other than a straight equality check on an attribute (e.g. checking that an attribute is
# in one of a possible number of states)
print('Creating Subnet 2')
result = virtual_network_client.create_subnet(
    oci.core.models.CreateSubnetDetails(
        compartment_id=compartment_id,
        availability_domain=second_availability_domain,
        display_name='WaitForResourceExampleSubnet2',
        vcn_id=vcn_ocid,
        cidr_block='10.0.1.0/24'
    )
)
subnet_two_ocid = result.data.id
get_subnet_two_response = virtual_network_client.get_subnet(subnet_two_ocid)
wait_until_subnet_two_available_response = oci.wait_until(virtual_network_client, get_subnet_two_response, evaluate_response=lambda r: r.data.lifecycle_state == 'AVAILABLE')
print(wait_until_subnet_two_available_response.data)

# Now we create a load balancer and wait until it has been created. Load balancers work slightly differently in that the create_load_balancer call
# returns a work request and it is the work request whose state we should wait on (we wait until it has succeeded)
print('Creating Load Balancer')
create_load_balancer_details = oci.load_balancer.models.CreateLoadBalancerDetails(
    compartment_id=compartment_id,
    display_name='WaitForResourceExampleLB',
    shape_name='100Mbps',
    subnet_ids=[subnet_ocid, subnet_two_ocid],
    backend_sets={
        'WaitExampleBackSet': oci.load_balancer.models.BackendSetDetails(
            policy='ROUND_ROBIN',
            health_checker=oci.load_balancer.models.HealthCheckerDetails(
                protocol='HTTP',
                url_path='/',
                port=80,
                retries=1,
                timeout_in_millis=100,
                interval_in_millis=1000,
            ),
            session_persistence_configuration=oci.load_balancer.models.SessionPersistenceConfigurationDetails(cookie_name='*', disable_fallback=False)
        )
    }
)
result = load_balancer_client.create_load_balancer(create_load_balancer_details)
work_request_id = result.headers['opc-work-request-id']
get_work_request_response = load_balancer_client.get_work_request(work_request_id)
wait_until_succeeded_response = oci.wait_until(load_balancer_client, get_work_request_response, 'lifecycle_state', 'SUCCEEDED')
print(wait_until_succeeded_response.data)
load_balancer_ocid = get_work_request_response.data.load_balancer_id

# Here we delete the load balancer. Note that on the waiter we use the optional succeed_on_not_found and set it to True. This meants that if we get a
# 404 back from the service when checking the load balancer's state, instead of throwing an exception we will return successfully. This flag will typically
# only be useful for delete/terminate scenarios and its normal default is False.
print('Deleting Load Balancer')
get_load_balancer_response = load_balancer_client.get_load_balancer(load_balancer_ocid)
load_balancer_client.delete_backend_set(load_balancer_ocid, 'WaitExampleBackSet')
load_balancer_client.delete_load_balancer(load_balancer_ocid)
oci.wait_until(load_balancer_client, get_load_balancer_response, 'lifecycle_state', 'TERMINATED', succeed_on_not_found=True)

print('Deleting Subnet 1')
get_subnet_response = virtual_network_client.get_subnet(subnet_ocid)
virtual_network_client.delete_subnet(subnet_ocid)
oci.wait_until(virtual_network_client, get_subnet_response, 'lifecycle_state', 'TERMINATED', succeed_on_not_found=True)

print('Deleting Subnet 2')
get_subnet_two_response = virtual_network_client.get_subnet(subnet_two_ocid)
virtual_network_client.delete_subnet(subnet_two_ocid)
oci.wait_until(virtual_network_client, get_subnet_two_response, 'lifecycle_state', 'TERMINATED', succeed_on_not_found=True)

print('Deleting VCN')
get_vcn_response = virtual_network_client.get_vcn(vcn_ocid)
virtual_network_client.delete_vcn(vcn_ocid)
oci.wait_until(virtual_network_client, get_vcn_response, 'lifecycle_state', 'TERMINATED', succeed_on_not_found=True)
