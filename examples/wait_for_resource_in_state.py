# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.
#
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
get_vcn_response = oci.wait_until(virtual_network_client, virtual_network_client.get_vcn(vcn_ocid), 'lifecycle_state', 'AVAILABLE')
print(get_vcn_response.data)

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
get_subnet_response = oci.wait_until(virtual_network_client, virtual_network_client.get_subnet(subnet_ocid), 'lifecycle_state', 'AVAILABLE')
print(get_subnet_response.data)

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
get_subnet_response = oci.wait_until(virtual_network_client, virtual_network_client.get_subnet(subnet_two_ocid), 'lifecycle_state', 'AVAILABLE')
print(get_subnet_response.data)

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
get_work_request_response = oci.wait_until(load_balancer_client, load_balancer_client.get_work_request(work_request_id), 'lifecycle_state', 'SUCCEEDED')
print(get_work_request_response.data)
load_balancer_ocid = get_work_request_response.data.load_balancer_id

# Here we delete the load balancer. Note that on the waiter we use the optional succeed_on_not_found and set it to True. This meants that if we get a
# 404 back from the service when checking the load balancer's state, instead of throwing an exception we will return successfully. This flag will typically
# only be useful for delete/terminate scenarios and its normal default is False.
print('Deleting Load Balancer')
load_balancer_client.delete_backend_set(load_balancer_ocid, 'WaitExampleBackSet')
load_balancer_client.delete_load_balancer(load_balancer_ocid)
oci.wait_until(load_balancer_client, load_balancer_client.get_load_balancer(load_balancer_ocid), 'lifecycle_state', 'TERMINATED', succeed_on_not_found=True)

print('Deleting Subnet 1')
virtual_network_client.delete_subnet(subnet_ocid)
oci.wait_until(virtual_network_client, virtual_network_client.get_subnet(subnet_ocid), 'lifecycle_state', 'TERMINATED', succeed_on_not_found=True)

print('Deleting Subnet 2')
virtual_network_client.delete_subnet(subnet_two_ocid)
oci.wait_until(virtual_network_client, virtual_network_client.get_subnet(subnet_two_ocid), 'lifecycle_state', 'TERMINATED', succeed_on_not_found=True)

print('Deleting VCN')
virtual_network_client.delete_vcn(vcn_ocid)
oci.wait_until(virtual_network_client, virtual_network_client.get_vcn(vcn_ocid), 'lifecycle_state', 'TERMINATED', succeed_on_not_found=True)
