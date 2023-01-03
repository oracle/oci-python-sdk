# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example of changing a load balancer's compartment, and
# requires an existing load balancer, as well as a compartment to move that load balancer
# into. This compartment cannot be the one in which the load balancer currently exists.
# For an example of creating a load balancer, please refer to 'load_balancer_rule_sets_example.py'.
# For further information on load balancers please see:
#   https://docs.cloud.oracle.com/iaas/Content/Balance/Concepts/balanceoverview.htm
# This script accepts two arguments:
#   - The first argument is the load balancer to move
#   - The second argument is the destination compartment for the load balancer.
#

import oci
import argparse

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('--compartment-id',
                    help='OCID of the destination compartment',
                    required=True)
parser.add_argument('--load-balancer-id',
                    help='OCID of the load balancer to move',
                    required=True)

args = parser.parse_args()

# Default config file and profile
config = oci.config.from_file()
load_balancer_client = oci.load_balancer.LoadBalancerClient(config)
load_balancer_client_composite_ops = oci.load_balancer.LoadBalancerClientCompositeOperations(load_balancer_client)

compartment_id = args.compartment_id
load_balancer_id = args.load_balancer_id

print('\n================================\n')
print("Moving load balancer " + load_balancer_id + " to compartment " + compartment_id + ".")
load_balancer_client_composite_ops.change_load_balancer_compartment_and_wait_for_state(
    load_balancer_id,
    oci.load_balancer.models.ChangeLoadBalancerCompartmentDetails(
        compartment_id=compartment_id
    ),
    wait_for_states=[oci.load_balancer.models.WorkRequest.LIFECYCLE_STATE_SUCCEEDED])
print("Change compartment operation complete.")
load_balancer = load_balancer_client.get_load_balancer(load_balancer_id).data
print('Load balancer details:\n{}'.format(load_balancer))
print('Script complete.')
