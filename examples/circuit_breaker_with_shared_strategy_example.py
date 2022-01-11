# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

#  This script showcases how to use circuit breaker at client level and share the configuration across multiple clients
# # USAGE:
# `python examples/circuit_breaker_with_shared_strategy_example.py  \
#        --compartment 'foo' \
#        --region1 '<region1>' \
#        --region2 '<region2>' \
#
# This script accepts 3 arguments:
#   - compartment: is the OCID of the compartment to use.
#   - region1: Name of the region to list users
#   - region2: Name of the region2 to list users

import argparse
import oci
from oci.circuit_breaker import CircuitBreakerStrategy


# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('--compartment',
                    help='OCID of Compartment',
                    required=True
                    )
parser.add_argument('--region1',
                    help='Name of Region 1',
                    required=True
                    )
parser.add_argument('--region2',
                    help='Name of Region 2',
                    required=True
                    )
args = parser.parse_args()
compartment = args.compartment
region1 = args.region1
region2 = args.region2


def get_users(client, compartment_id):
    '''
    To retrieve the list of all available regions.
    '''
    user_names = []
    users = client.list_users(compartment_id=compartment_id).data
    for user in users:
        user_names.append(user.name)
    return user_names


def print_users(users_to_print):
    print("=" * 10)
    print("Users")
    print("=" * 10)
    for user in users_to_print:
        print(user)


#  Setting configuration
#  Default path for configuration file is "~/.oci/config"
config = oci.config.from_file()
config['region'] = region1

config2 = config.copy()
config['region'] = region2

# Create a custom Circuit Breaker Strategy. For more info please refer to circuit breaker docs under SDK Behavior
# Please note that in order to share the Circuit Breaker object; the name must be provided otherwise, the CB would be
# two different objects rather than being the same one.
custom_circuit_breaker_strategy = CircuitBreakerStrategy(
    failure_threshold=5,
    recovery_timeout=40,
    failure_statuses_and_codes={
        409: ["IncorrectState", "Conflict"],
        429: []
    },
    name='Example1'
)

identity = oci.identity.IdentityClient(config, circuit_breaker_strategy=custom_circuit_breaker_strategy)
print_users(get_users(client=identity, compartment_id=compartment))

identity2 = oci.identity.IdentityClient(config2, circuit_breaker_strategy=custom_circuit_breaker_strategy)
print_users(get_users(client=identity2, compartment_id=compartment))
