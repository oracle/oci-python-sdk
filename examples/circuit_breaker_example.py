# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

#  This script showcases how to use circuit breaker at client level and retrieve all regions from a tenancy
import oci
from oci.circuit_breaker import CircuitBreakerStrategy, NoCircuitBreakerStrategy
import logging


def get_regions(client):
    '''
    To retrieve the list of all available regions.
    '''
    list_of_regions = []
    list_regions_response = client.list_regions()
    for r in list_regions_response.data:
        list_of_regions.append(r.name)
    return list_of_regions


def print_regions(regions_to_print):
    print("=" * 20)
    print("Regions")
    print("=" * 20)
    for region in regions_to_print:
        print(region)


#  Setting configuration
#  Default path for configuration file is "~/.oci/config"
config = oci.config.from_file()
config['log_requests'] = True
logging.basicConfig()

# Create a Global Circuit Breaker Strategy and use the convenient DEFAULT_CIRCUIT_BREAKER_STRATEGY
oci.circuit_breaker.GLOBAL_CIRCUIT_BREAKER_STRATEGY = oci.circuit_breaker.DEFAULT_CIRCUIT_BREAKER_STRATEGY

#  Initiate the client with the locally available config and global circuit breaker strategy
identity = oci.identity.IdentityClient(config)
regions = get_regions(client=identity)
print_regions(regions)

# Create a custom Circuit Breaker Strategy. For more info please refer to circuit breaker docs under SDK Behavior
circuit_breaker_strategy = CircuitBreakerStrategy(
    failure_threshold=5,
    recovery_timeout=40,
    failure_statuses_and_codes={
        409: ["IncorrectState", "Conflict"],
        429: []
    }
)

#  Initiate the client with the locally available config and custom client level circuit breaker strategy
identity2 = oci.identity.IdentityClient(config, circuit_breaker_strategy=circuit_breaker_strategy)
regions = get_regions(client=identity2)
print_regions(regions)

#  Initiate the client with the locally available config and no circuit breaker strategy
identity3 = oci.identity.IdentityClient(config, circuit_breaker_strategy=NoCircuitBreakerStrategy())
regions = get_regions(client=identity3)
print_regions(regions)
