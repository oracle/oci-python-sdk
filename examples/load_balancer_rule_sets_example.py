# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example on how to work with rule sets on a load balancer by:
#
#   - Create a rule set when the load balancer is created
#   - Creating/updating rules and rule sets after a load balancer has been created
#       (via the CreateRuleSet and UpdateRuleSet operations)
#   - Creating and updating listeners withrule sets
#
# This script accepts three arguments:
#   --compartment-id is the compartment where we'll create the load balancer and related resources
#   --first-ad is the first availability domain where we'll create a subnet
#   --second-ad is a second (different) availability domain where we'll create a subnet
#
# A load balancer needs some backing networking resources (at least a VCN and two subnets). For demonstration purposes
# this script will create these resources (as well as the load balancer) and delete them upon completion

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
parser.add_argument('--vcn-id',
                    help='id of a valid VCN within your tenancy',
                    required=True)

args = parser.parse_args()


# As part of creating a load balancer, we can create rule sets. Note that this 'rule_sets' object is a dictionary
# where each key is the rule set name and the value is the information on what routes are in the set.
#
# Additionally, when creating a listener as part of load balancer creation we may specify one or more rule
# sets for that listener. This 'rule_sets' property of the listener is a list of names, which needs to correspond
# to the rule set names we specify earlier. In this example we create a single rule set, and thus the listener
# will have specify a list with a single element for its 'rule_sets' property.
def create_load_balancer(load_balancer_client_composite_ops, compartment_id, subnet_id):
    create_load_balancer_response = load_balancer_client_composite_ops.create_load_balancer_and_wait_for_state(
        oci.load_balancer.models.CreateLoadBalancerDetails(
            compartment_id=compartment_id,
            display_name='pythonSDKExampleLB',
            shape_name='100Mbps',
            subnet_ids=[subnet_id],
            is_private=True,
            backend_sets={
                'backend1': oci.load_balancer.models.BackendSetDetails(
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
                'backend2': oci.load_balancer.models.BackendSetDetails(
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
            rule_sets={
                'ruleset1': oci.load_balancer.models.RuleSetDetails(
                    items=[
                        oci.load_balancer.models.AddHttpRequestHeaderRule(
                            header='backend-1',
                            value='/example/1'),
                        oci.load_balancer.models.ExtendHttpResponseHeaderValueRule(
                            header='extend-response-header-example',
                            prefix='prefix-to-extend-with',
                            suffix='suffix-to-extend-with'),
                        oci.load_balancer.models.RemoveHttpRequestHeaderRule(
                            header='remove-request-header'),
                        oci.load_balancer.models.ControlAccessUsingHttpMethodsRule(
                            allowed_methods=["PUT", "POST"],
                            status_code=403)

                    ]
                )
            },
            listeners={
                'listener1': oci.load_balancer.models.ListenerDetails(
                    default_backend_set_name='backend1',
                    # Note this name must match the rule set name specified above
                    rule_set_names=['ruleset1'],
                    port=80,
                    protocol='HTTP'
                )
            }
        ),
        [oci.load_balancer.models.WorkRequest.LIFECYCLE_STATE_SUCCEEDED]
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
vcn_id = args.vcn_id

print('\n================================\n')
print("Attempting to create a load balancer")
load_balancer = create_load_balancer(load_balancer_client_composite_ops, compartment_id, subnet_id)
load_balancer_ocid = load_balancer.data.id
# CreateLoadBalancer gives us a work request we can check. This work request will be SUCCEEDED once the load
# balancer has been created

print('\n================================\n')
print('Created load balancer {}'.format(load_balancer.data))

# we can list the listener_rules on the load balancer
listener_rules = load_balancer_client.list_listener_rules(load_balancer_ocid, "listener1")
print('\n================================\n')
print('The listenerRuleSummary for the listener on the current load balancer:\n{}'.format(listener_rules.data))

# We can list the rule sets on the load balancer
rule_sets = load_balancer_client.list_rule_sets(load_balancer_ocid)
print('\n================================\n')
print('All rule sets from the load balancer:\n{}'.format(rule_sets.data))

# We can also get an individual rule set
rule_set = load_balancer_client.get_rule_set(load_balancer_ocid, 'ruleset1').data
print('\n================================\n')
print('Single rule set:\n{}'.format(rule_set))

# We can create another rule set on the load balancer. Note that this also returns a work request which
# we be SUCCEEDED once the rule set has been created
load_balancer_client_composite_ops.create_rule_set_and_wait_for_state(
    load_balancer_ocid,
    oci.load_balancer.models.CreateRuleSetDetails(
        # This name needs to be unique amongst the rule sets on the load balancer
        name='ruleset2',
        items=[
            oci.load_balancer.models.AddHttpRequestHeaderRule(
                header="rule-set-2-add-http-request",
                value="rule-set-2-add-http-request-value"
            ),
            oci.load_balancer.models.ControlAccessUsingHttpMethodsRule(
                allowed_methods=["GET", "PROPFIND"],
                status_code=400
            )
        ]
    ),
    wait_for_states=[oci.load_balancer.models.WorkRequest.LIFECYCLE_STATE_SUCCEEDED])

print('\n================================\n')
print('Rule set: Using Rule Sets for Access Control\n{}'.format(rule_set))
# We can create a rule set on the load balancer with rules specifically geared towards access control.
# Note that this also returns a work request which will be SUCCEEDED once the rule set has been created.
load_balancer_client_composite_ops.create_rule_set_and_wait_for_state(
    load_balancer_ocid,
    oci.load_balancer.models.CreateRuleSetDetails(
        # The name of the rule set must be unique across all rule sets on the load balancer
        name='ruleset3',
        items=[
            oci.load_balancer.models.AllowRule(
                description="Allow traffic from internet clients",
                conditions=[
                    oci.load_balancer.models.SourceIpAddressCondition(
                        attribute_value="129.146.39.248/32"
                    )
                ]
            )
        ]
    ),
    wait_for_states=[oci.load_balancer.models.WorkRequest.LIFECYCLE_STATE_SUCCEEDED]
)

rule_set_3 = load_balancer_client.get_rule_set(load_balancer_ocid, 'ruleset3').data
print('Ruleset3 after creation:\n{}'.format(rule_set_3))
print('\n================================\n')

rule_sets = load_balancer_client.list_rule_sets(load_balancer_ocid)
print('\n================================\n')
print('Rule sets in the load balancer after creating a rule set for access control:\n{}'.format(rule_sets.data))


# We can update the rules in a rule set. Note that this is a total replacement, so any routes which you want
# to preserve need to be passed as part of the update.
#
# In this example, we keep one of the rules we defined above (the http method access control). The status code
# will be changed to '500'.
#
# Note that updating a rule also results in a work request that we can wait on until it succeeds

print('Updating ruleset2')
print('\n================================\n')
load_balancer_client_composite_ops.update_rule_set_and_wait_for_state(
    load_balancer_ocid,
    'ruleset2',
    oci.load_balancer.models.UpdateRuleSetDetails(
        # This name needs to be unique amongst the rule sets on the load balancer
        items=[
            oci.load_balancer.models.AddHttpRequestHeaderRule(
                header="rule-set-2-add-http-request",
                value="rule-set-2-add-http-request-value"
            ),
            oci.load_balancer.models.RemoveHttpRequestHeaderRule(
                header="rule-set-2-remove-http-request"
            )
        ]
    ),
    wait_for_states=[oci.load_balancer.models.WorkRequest.LIFECYCLE_STATE_SUCCEEDED]
)

rule_set_2 = load_balancer_client.get_rule_set(load_balancer_ocid, 'ruleset2').data
print('Ruleset2 after update:\n{}'.format(rule_set_2))
print('\n================================\n')

# We can update the rule sets on an existing listener, note that this will overwrite the list
# of currently attached rule sets.
print('Update listener with new rule sets')
print('\n================================\n')
load_balancer_client_composite_ops.update_listener_and_wait_for_state(
    oci.load_balancer.models.UpdateListenerDetails(
        default_backend_set_name='backend2',
        rule_set_names=['ruleset1', 'ruleset2'],
        port=80,
        protocol='HTTP'
    ),
    load_balancer_ocid,
    'listener1',
    wait_for_states=[oci.load_balancer.models.WorkRequest.LIFECYCLE_STATE_SUCCEEDED]
)
load_balancer = load_balancer_client.get_load_balancer(load_balancer_ocid).data
print('Listener after update:\n{}'.format(load_balancer.listeners))
print('\n================================\n')

# We can also create a listener with a rule set
print('Create new listener with rule sets')
print('\n================================\n')
load_balancer_client_composite_ops.create_listener_and_wait_for_state(
    oci.load_balancer.models.CreateListenerDetails(
        name='listener2',
        default_backend_set_name='backend1',
        port=8080,
        protocol='HTTP',
        rule_set_names=['ruleset1', 'ruleset2']
    ),
    load_balancer_ocid,
    wait_for_states=[oci.load_balancer.models.WorkRequest.LIFECYCLE_STATE_SUCCEEDED]
)
load_balancer = load_balancer_client.get_load_balancer(load_balancer_ocid).data
print('Listeners now in load balancer:\n{}'.format(load_balancer.listeners))
print('\n================================\n')

# We now delete the load balancer
print("Attempting to delete load balancer {}".format(load_balancer_ocid))
print('\n================================\n')
load_balancer_client_composite_ops.delete_load_balancer_and_wait_for_state(
    load_balancer_ocid,
    wait_for_states=[oci.load_balancer.models.WorkRequest.LIFECYCLE_STATE_SUCCEEDED])
print('Deleted Load Balancer')

print('Script finished')
