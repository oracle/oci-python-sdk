# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example of how to use the retry functionality in the Python SDK when
# making calls to Oracle Cloud Infrastructure services. In order to demonstrate this functionality, this script shows
# performing create, update and delete operations against VCNs.
#
# This script takes a single argument:
#
#   * The OCID of the compartment where we'll create the VCN

import oci
import sys


def do_vcn_interactions_with_retries(virtual_network_client, compartment_id, retry_strategy):
    vcn_name = 'python_sdk_example_vcn'
    cidr_block = '10.0.0.0/16'
    result = virtual_network_client.create_vcn(
        oci.core.models.CreateVcnDetails(
            cidr_block=cidr_block,
            display_name=vcn_name,
            compartment_id=compartment_id
        ),
        retry_strategy=retry_strategy
    )

    vcn_response = oci.wait_until(
        virtual_network_client,
        virtual_network_client.get_vcn(result.data.id),
        'lifecycle_state',
        'AVAILABLE',
        max_wait_seconds=300
    )
    vcn = vcn_response.data
    print('Created VCN')
    print('================')
    print(vcn)
    print('\n\n')

    result = virtual_network_client.update_vcn(
        vcn.id,
        oci.core.models.UpdateVcnDetails(display_name='python_sdk_example_vcn_updated'),
        retry_strategy=retry_strategy
    )
    print('Updated VCN')
    print('================')
    print(result.data)
    print('\n\n')

    virtual_network_client.delete_vcn(vcn.id, retry_strategy=retry_strategy)
    oci.wait_until(
        virtual_network_client,
        vcn_response,
        'lifecycle_state',
        'TERMINATED',
        max_wait_seconds=300,
        succeed_on_not_found=True
    )
    print('Deleted VCN')
    print('\n\n')


if len(sys.argv) != 2:
    raise RuntimeError('A compartment OCID must be provided to this script')

compartment_id = sys.argv[1]

# Default config file and profile
config = oci.config.from_file()
virtual_network_client = oci.core.VirtualNetworkClient(config)

# Here we use the default retry strategy. The attributes of this retry strategy are
# documented on this page:
# https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html
do_vcn_interactions_with_retries(virtual_network_client, compartment_id, oci.retry.DEFAULT_RETRY_STRATEGY)

# We can also construct our own retry strategy by using the RetryStrategyBuilder
retry_strategy_via_constructor = oci.retry.RetryStrategyBuilder(
    # Make up to 10 service calls
    max_attempts_check=True,
    max_attempts=10,

    # Don't exceed a total of 600 seconds for all service calls
    total_elapsed_time_check=True,
    total_elapsed_time_seconds=600,

    # Wait 45 seconds between attempts
    retry_max_wait_between_calls_seconds=45,

    # Use 2 seconds as the base number for doing sleep time calculations
    retry_base_sleep_time_seconds=2,

    # Retry on certain service errors:
    #
    #   - 5xx code received for the request
    #   - Any 429 (this is signified by the empty array in the retry config)
    #   - 400s where the code is QuotaExceeded or LimitExceeded
    service_error_check=True,
    service_error_retry_on_any_5xx=True,
    service_error_retry_config={
        400: ['QuotaExceeded', 'LimitExceeded'],
        429: []
    },

    # Use exponential backoff and retry with full jitter, but on throttles use
    # exponential backoff and retry with equal jitter
    backoff_type=oci.retry.BACKOFF_FULL_JITTER_EQUAL_ON_THROTTLE_VALUE
).get_retry_strategy()
do_vcn_interactions_with_retries(virtual_network_client, compartment_id, retry_strategy_via_constructor)

# In addition to providing options in the constructor, we can create a RetryStrategyBuilder
# and use its add_* methods to enable different options. It also includes no_* methods to disable
# options
retry_strategy_builder = oci.retry.RetryStrategyBuilder()
retry_strategy_builder.add_max_attempts(max_attempts=10) \
                      .add_total_elapsed_time(total_elapsed_time_seconds=600) \
                      .add_service_error_check(
                          service_error_retry_on_any_5xx=True,
                          service_error_retry_config={429: []})
do_vcn_interactions_with_retries(virtual_network_client, compartment_id, retry_strategy_builder.get_retry_strategy())
