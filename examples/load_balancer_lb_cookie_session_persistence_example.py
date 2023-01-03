# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example on how to work with session persistance cookies:
#
#   - Creating a session persistance cookie configuration when the load balancer is created
#   - Creating/updating a session persistance cookie configuration as part of a 'create backend-set'
#   - Creating and updating listeners with path route sets
#
# This script accepts two arguments:
#   - The first argument is the compartment where we'll create the load balancer and related resources
#   - The second argument is a subnet to which we'll attach a new example load balancer
#
# A load balancer needs some backing networking resources (at least a VCN and two subnets). For demonstration purposes
# this script will create these resources and delete them upon completion

import oci
import argparse

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('--compartment-id',
                    help='compartment ID in which to perform the operation',
                    required=True)
parser.add_argument('--subnet-id',
                    help='name of the first AD in the format nnNN:PHX-AD-1',
                    required=True)

args = parser.parse_args()


# As part of creating a load balancer, we may configure loadbalancer cookie session persistence when defining
# a backend set.

def create_load_balancer(load_balancer_client_composite_ops, compartment_id, subnet_id):
    create_load_balancer_response = load_balancer_client_composite_ops.create_load_balancer_and_wait_for_state(
        oci.load_balancer.models.CreateLoadBalancerDetails(
            compartment_id=compartment_id,
            display_name='pythonSDKExampleLB',
            shape_name='100Mbps',
            subnet_ids=[subnet_id],
            is_private=True,
            backend_sets={
                'backendset1': oci.load_balancer.models.BackendSetDetails(
                    policy='ROUND_ROBIN',
                    health_checker=oci.load_balancer.models.HealthCheckerDetails(
                        protocol='HTTP',
                        url_path='/',
                        port=80,
                        retries=1,
                        timeout_in_millis=100,
                        interval_in_millis=1000
                    ),
                    backends=[
                        oci.load_balancer.models.BackendDetails(
                            ip_address='10.11.10.11',
                            port=80,
                            weight=1,
                            backup=False,
                            drain=False,
                            offline=False
                        ),
                        oci.load_balancer.models.BackendDetails(
                            ip_address='10.11.13.12',
                            port=80,
                            weight=1,
                            backup=False,
                            drain=False,
                            offline=False
                        )
                    ],
                    lb_cookie_session_persistence_configuration=oci.load_balancer.models.LBCookieSessionPersistenceConfigurationDetails(
                        cookie_name='X-Oracle-OCI-lb_persist_cookie_1',
                        disable_fallback=False,
                        domain='mydomain.com',
                        path='/path',
                        max_age_in_seconds=180,
                        is_secure=False,
                        is_http_only=True
                    )
                )
            },
            listeners={
                'listener1': oci.load_balancer.models.ListenerDetails(
                    default_backend_set_name='backendset1',
                    port=80,
                    protocol='HTTP'
                )
            }
        ),
        wait_for_states=[oci.load_balancer.models.WorkRequest.LIFECYCLE_STATE_SUCCEEDED]
    )
    return create_load_balancer_response


# Default config file and profile
config = oci.config.from_file()
load_balancer_client = oci.load_balancer.LoadBalancerClient(config)
load_balancer_client_composite_ops = oci.load_balancer.LoadBalancerClientCompositeOperations(load_balancer_client)
virtual_network_client = oci.core.VirtualNetworkClient(config)
virtual_network_client_composite_ops = oci.core.VirtualNetworkClientCompositeOperations(virtual_network_client)

compartment_id = args.compartment_id
subnet_id = args.subnet_id

print('\n================================\n')
print("Attempting to create a load balancer")
load_balancer = create_load_balancer(load_balancer_client_composite_ops, compartment_id, subnet_id)
load_balancer_ocid = load_balancer.data.id
# CreateLoadBalancer gives us a work request we can check. This work request will be SUCCEEDED once the load
# balancer has been created

print('\n================================\n')
print('Created load balancer {}'.format(load_balancer.data))

# We can also get an individual backend set to review the LB cookie session persistence.
backend_set = load_balancer_client.get_backend_set(load_balancer_ocid, 'backendset1').data
print('\n================================\n')
print('Single backend set:\n{}'.format(backend_set))

# We can create another backend set on the load balancer with lb cookie session persistance configuration.
# Note that this returns a work request which will be SUCCEEDED once the backend set has been created
load_balancer_client_composite_ops.create_backend_set_and_wait_for_state(
    oci.load_balancer.models.CreateBackendSetDetails(
        name='backendset2',
        policy='ROUND_ROBIN',
        backends=[
            oci.load_balancer.models.BackendDetails(
                ip_address='10.11.10.5',
                port=8080,
                weight=1,
                backup=False,
                drain=False,
                offline=False
            ),
            oci.load_balancer.models.BackendDetails(
                ip_address='10.11.10.25',
                port=8080,
                weight=3,
                backup=True,
                drain=False,
                offline=False
            )
        ],
        health_checker=oci.load_balancer.models.HealthCheckerDetails(
            protocol='HTTP',
            url_path='/testurl2',
            port=8080,
            retries=10,
            timeout_in_millis=100,
            interval_in_millis=1000
        ),
        lb_cookie_session_persistence_configuration=oci.load_balancer.models.LBCookieSessionPersistenceConfigurationDetails(
            cookie_name='X-Oracle-OCI-lb_persist_cookie_2',
            disable_fallback=True,
            domain='mydomain.com',
            path='/cookie_path',
            max_age_in_seconds=300,
            is_secure=False,
            is_http_only=True
        )
    ),
    load_balancer_ocid,
    wait_for_states=[oci.load_balancer.models.WorkRequest.LIFECYCLE_STATE_SUCCEEDED])

backend_sets = load_balancer_client.list_backend_sets(load_balancer_ocid)
print('\n================================\n')
print('Backend sets in the load balancer after creating another set:\n{}'.format(backend_sets.data))

# We can update a backend set with session persistance cookie configuration.
# In this example, we remove the LB cookie session persistence configuration by setting that parameter to null.

print('Updating backendset1')
print('\n================================\n')
load_balancer_client_composite_ops.update_backend_set_and_wait_for_state(
    oci.load_balancer.models.UpdateBackendSetDetails(
        policy='ROUND_ROBIN',
        health_checker=oci.load_balancer.models.HealthCheckerDetails(
            protocol='HTTP',
            url_path='/',
            port=80,
            retries=1,
            timeout_in_millis=100,
            interval_in_millis=1000
        ),
        backends=[
            oci.load_balancer.models.BackendDetails(
                ip_address='10.11.10.11',
                port=80,
                weight=1,
                backup=False,
                drain=False,
                offline=False
            ),
            oci.load_balancer.models.BackendDetails(
                ip_address='10.11.13.12',
                port=80,
                weight=1,
                backup=False,
                drain=False,
                offline=False
            )
        ],
        lb_cookie_session_persistence_configuration=None
    ),
    load_balancer_ocid,
    'backendset1',
    wait_for_states=[oci.load_balancer.models.WorkRequest.LIFECYCLE_STATE_SUCCEEDED]
)

backend_sets = load_balancer_client.list_backend_sets(load_balancer_ocid)
print('\n================================\n')
print('Backend sets in the load balancer after removing LB cookie session persistence from backendset2:\n{}'.format(backend_sets.data))

# We now delete the load balancer
print("Attempting to delete load balancer {}".format(load_balancer_ocid))
print('\n================================\n')
load_balancer_client_composite_ops.delete_load_balancer_and_wait_for_state(
    load_balancer_ocid,
    wait_for_states=[oci.load_balancer.models.WorkRequest.LIFECYCLE_STATE_SUCCEEDED])
print('Deleted Load Balancer')

print('Script finished')
