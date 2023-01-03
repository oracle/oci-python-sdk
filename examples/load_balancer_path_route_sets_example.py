# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example on how to work with path route sets on a load balancer by:
#
#   - Creating path route sets when the load balancer is created
#   - Creating/updating path route after a load balancer has been created (via the CreatePathRouteSet and UpdatePathRouteSet operations)
#   - Creating and updating listeners with path route sets
#
# This script accepts three arguments:
#   - The first argument is the compartment where we'll create the load balancer and related resources
#   - The second argument is the first availability domain where we'll create a subnet
#   - The third argument is a second (different) availability domain where we'll create a subnet
#
# A load balancer needs some backing networking resources (at least a VCN and two subnets). For demonstration purposes
# this script will create these resources and delete them upon completion

import oci
import sys


def create_vcn_and_subnets(virtual_network, compartment_id, first_ad, second_ad):
    # Create a VCN
    vcn_name = 'python_sdk_test_lb_vcn'
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
    subnet_name = 'python_sdk_test_lb_subnet1'
    subnet_cidr_block1 = "10.0.0.0/24"
    result = virtual_network.create_subnet(
        oci.core.models.CreateSubnetDetails(
            compartment_id=compartment_id,
            availability_domain=first_ad,
            display_name=subnet_name,
            vcn_id=vcn.id,
            cidr_block=subnet_cidr_block1
        )
    )
    subnet_one = oci.wait_until(
        virtual_network,
        virtual_network.get_subnet(result.data.id),
        'lifecycle_state',
        'AVAILABLE',
        max_wait_seconds=300
    ).data
    print('Created Subnet 1')

    # Create another subnet
    subnet_name = 'python_sdk_test_lb_subnet2'
    subnet_cidr_block2 = "10.0.1.0/24"
    result = virtual_network.create_subnet(
        oci.core.models.CreateSubnetDetails(
            compartment_id=compartment_id,
            availability_domain=second_ad,
            display_name=subnet_name,
            vcn_id=vcn.id,
            cidr_block=subnet_cidr_block2
        )
    )
    subnet_two = oci.wait_until(
        virtual_network,
        virtual_network.get_subnet(result.data.id),
        'lifecycle_state',
        'AVAILABLE',
        max_wait_seconds=300
    ).data
    print('Created Subnet 2')

    return {'vcn': vcn, 'subnets': [subnet_one, subnet_two]}


def delete_vcn_and_subnets(virtual_network, vcn_and_subnets):
    vcn = vcn_and_subnets['vcn']
    subnet_one = vcn_and_subnets['subnets'][0]
    subnet_two = vcn_and_subnets['subnets'][1]

    composite_virtual_network = oci.core.VirtualNetworkClientCompositeOperations(virtual_network)
    composite_virtual_network.delete_subnet_and_wait_for_state(
        subnet_one.id,
        [oci.core.models.Subnet.LIFECYCLE_STATE_TERMINATED]
    )
    composite_virtual_network.delete_subnet_and_wait_for_state(
        subnet_two.id,
        [oci.core.models.Subnet.LIFECYCLE_STATE_TERMINATED]
    )

    composite_virtual_network.delete_vcn_and_wait_for_state(
        vcn.id,
        [oci.core.models.Vcn.LIFECYCLE_STATE_TERMINATED]
    )


# Default config file and profile
config = oci.config.from_file()
load_balancer_client = oci.load_balancer.LoadBalancerClient(config)
virtual_network_client = oci.core.VirtualNetworkClient(config)

if len(sys.argv) != 4:
    raise RuntimeError('This script needs to be provided a compartment ID and two availability domains')

compartment_id = sys.argv[1]
first_ad = sys.argv[2]
second_ad = sys.argv[3]

vcn_and_subnets = create_vcn_and_subnets(virtual_network_client, compartment_id, first_ad, second_ad)
subnets = vcn_and_subnets['subnets']

# As part of creating a load balancer, we can create path route sets. Note that this is a dictionary where each
# key is the path route set name and the value is the information on what routes are in the set.
#
# Additionally, when creating a listener as part of load balancer creation we can specify the path route
# set for that listener. This path route set needs to correspond to one of the ones we'll create as part of
# load balancer creation.
response = load_balancer_client.create_load_balancer(
    oci.load_balancer.models.CreateLoadBalancerDetails(
        compartment_id=compartment_id,
        display_name='PathRouteSetLB',
        shape_name='100Mbps',
        subnet_ids=[subnets[0].id, subnets[1].id],
        backend_sets={
            'backend-1': oci.load_balancer.models.BackendSetDetails(
                policy='ROUND_ROBIN',
                health_checker=oci.load_balancer.models.HealthCheckerDetails(
                    protocol='HTTP',
                    url_path='/',
                    port=80,
                    retries=1,
                    timeout_in_millis=100,
                    interval_in_millis=1000
                ),
                session_persistence_configuration=oci.load_balancer.models.SessionPersistenceConfigurationDetails(
                    cookie_name='*',
                    disable_fallback=False
                )
            ),
            'backend-2': oci.load_balancer.models.BackendSetDetails(
                policy='ROUND_ROBIN',
                health_checker=oci.load_balancer.models.HealthCheckerDetails(
                    protocol='HTTP',
                    url_path='/testurl2',
                    port=80,
                    retries=1,
                    timeout_in_millis=100,
                    interval_in_millis=1000
                )
            )
        },
        path_route_sets={
            'path-route-set-1': oci.load_balancer.models.PathRouteSetDetails(
                path_routes=[
                    oci.load_balancer.models.PathRoute(
                        # Note that this name matches one of the backend sets specified in the backend_sets dict
                        backend_set_name='backend-1',
                        path='/example/1',
                        path_match_type=oci.load_balancer.models.PathMatchType(match_type='PREFIX_MATCH')
                    ),
                    oci.load_balancer.models.PathRoute(
                        backend_set_name='backend-1',
                        path='/other/path/2',
                        path_match_type=oci.load_balancer.models.PathMatchType(match_type='EXACT_MATCH')
                    )
                ]
            )
        },
        listeners={
            'listener1': oci.load_balancer.models.ListenerDetails(
                default_backend_set_name='backend-1',
                # This path route set name corresponds to a name/key in the path_route_sets dict
                path_route_set_name='path-route-set-1',
                port=80,
                protocol='HTTP'
            )
        }
    )
)

# CreateLoadBalancer gives us a work request we can check. This work request will be SUCCEEDED once the load
# balancer has been created
work_request_id = response.headers['opc-work-request-id']
oci.wait_until(load_balancer_client, load_balancer_client.get_work_request(work_request_id), 'lifecycle_state', 'SUCCEEDED', max_wait_seconds=300)
response = load_balancer_client.get_work_request(work_request_id)
load_balancer_ocid = response.data.load_balancer_id
print('Load balancer created')
print('\n================================\n')

# We can list the path route sets on the load balancer
path_route_sets = load_balancer_client.list_path_route_sets(load_balancer_ocid)
print('Path route sets from list:\n{}'.format(path_route_sets.data))
print('\n================================\n')

# We can also get an individual path route set
path_route_set = load_balancer_client.get_path_route_set(load_balancer_ocid, 'path-route-set-1').data
print('Path route set from GET:\n{}'.format(path_route_set))
print('\n================================\n')

# And it's accessible via the load balancer itself
load_balancer = load_balancer_client.get_load_balancer(load_balancer_ocid).data
print('Load balancer details:\n{}'.format(load_balancer))
print('\n================================\n')

# We can create another path route set on the load balancer. Note that this also returns a work request which
# we be SUCCEEDED once the path route set has been created
response = load_balancer_client.create_path_route_set(
    oci.load_balancer.models.CreatePathRouteSetDetails(
        # This name needs to be unique amongst the path route sets on the load balancer
        name='path-route-set-2',
        path_routes=[
            oci.load_balancer.models.PathRoute(
                # Note that this needs to correspond to a backend set on the load balancer
                backend_set_name='backend-2',
                path='/example3/4',
                path_match_type=oci.load_balancer.models.PathMatchType(match_type='EXACT_MATCH')
            ),
            oci.load_balancer.models.PathRoute(
                backend_set_name='backend-2',
                path='/some/kind/of/path',
                path_match_type=oci.load_balancer.models.PathMatchType(match_type='EXACT_MATCH')
            )
        ]
    ),
    load_balancer_ocid
)
work_request_id = response.headers['opc-work-request-id']
oci.wait_until(load_balancer_client, load_balancer_client.get_work_request(work_request_id), 'lifecycle_state', 'SUCCEEDED', max_wait_seconds=300)

path_route_sets = load_balancer_client.list_path_route_sets(load_balancer_ocid)
print('Path route sets from list after creating another set:\n{}'.format(path_route_sets.data))
print('\n================================\n')

# We can update the routes on a path route set. Note that this is a total replacement, so any routes which you want
# to preserve need to be passed as part of the update.
#
# In this example, we keep one of the path routes we defined above (the one for path /example3/4). The route for
# /some/kind/of/path will be removed as part of this update.
#
# Note that updating a path route also results in a work request that we can wait on until it succeeds
response = load_balancer_client.update_path_route_set(
    oci.load_balancer.models.UpdatePathRouteSetDetails(
        path_routes=[
            oci.load_balancer.models.PathRoute(
                backend_set_name='backend-2',
                path='/example3/4',
                path_match_type=oci.load_balancer.models.PathMatchType(match_type='EXACT_MATCH')
            ),
            oci.load_balancer.models.PathRoute(
                backend_set_name='backend-2',
                path='/a/different/path',
                path_match_type=oci.load_balancer.models.PathMatchType(match_type='EXACT_MATCH')
            )
        ]
    ),
    load_balancer_ocid,
    'path-route-set-2'
)
work_request_id = response.headers['opc-work-request-id']
oci.wait_until(load_balancer_client, load_balancer_client.get_work_request(work_request_id), 'lifecycle_state', 'SUCCEEDED', max_wait_seconds=300)

path_route_set = load_balancer_client.get_path_route_set(load_balancer_ocid, 'path-route-set-2').data
print('Path route set after update:\n{}'.format(path_route_set))
print('\n================================\n')

# We can update the path route set on an existing listener
response = load_balancer_client.update_listener(
    oci.load_balancer.models.UpdateListenerDetails(
        default_backend_set_name='backend-2',
        path_route_set_name='path-route-set-2',
        port=80,
        protocol='HTTP'
    ),
    load_balancer_ocid,
    'listener1'
)
work_request_id = response.headers['opc-work-request-id']
oci.wait_until(load_balancer_client, load_balancer_client.get_work_request(work_request_id), 'lifecycle_state', 'SUCCEEDED', max_wait_seconds=300)

load_balancer = load_balancer_client.get_load_balancer(load_balancer_ocid).data
print('Listener after update:\n{}'.format(load_balancer.listeners))
print('\n================================\n')

# We can also create a listener with a path route set

response = load_balancer_client.create_listener(
    oci.load_balancer.models.CreateListenerDetails(
        name='listener2',
        default_backend_set_name='backend-1',
        port=8080,
        protocol='HTTP',
        path_route_set_name='path-route-set-1'
    ),
    load_balancer_ocid
)
work_request_id = response.headers['opc-work-request-id']
oci.wait_until(load_balancer_client, load_balancer_client.get_work_request(work_request_id), 'lifecycle_state', 'SUCCEEDED', max_wait_seconds=300)

load_balancer = load_balancer_client.get_load_balancer(load_balancer_ocid).data
print('Listener after create new listener:\n{}'.format(load_balancer.listeners))
print('\n================================\n')

# We now delete the load balancer
response = load_balancer_client.delete_load_balancer(load_balancer_ocid)
work_request_id = response.headers['opc-work-request-id']
oci.wait_until(load_balancer_client, load_balancer_client.get_work_request(work_request_id), 'lifecycle_state', 'SUCCEEDED', max_wait_seconds=300)
print('Deleted Load Balancer')

delete_vcn_and_subnets(virtual_network_client, vcn_and_subnets)
print('Deleted VCN and subnets')
print('Script finished')
