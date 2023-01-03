# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example of how to use the retry functionality using the various option present in the Python SDK when
# making calls to Oracle Cloud Infrastructure services

import oci

# Default config file and profile
config = oci.config.from_file()
compartment_id = config["tenancy"]

# Define a custom strategy
custom_retry_strategy = oci.retry.RetryStrategyBuilder(
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

# Override Global level Retry Strategy
oci.retry.GLOBAL_RETRY_STRATEGY = custom_retry_strategy

# Service client
identity_client = oci.identity.IdentityClient(config)

# This Operation will use the Global Retry strategy defined above as no retry strategy is provided at client or operation level
response = identity_client.list_users(compartment_id=compartment_id)
print('-' * 15)
print('Listing users')
print('-' * 15)
for user in response.data:
    print(user.name)

# Disable Retry at operation level by passing retry_strategy as oci.retry.NoneRetryStrategy()
# The operation level retry strategy takes precedence over any client level or Global Retry Strategy
# Documentation to see how this works (https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html)
response = identity_client.list_regions(retry_strategy=oci.retry.NoneRetryStrategy())
print('-' * 15)
print('Listing regions')
print('-' * 15)
for region in response.data:
    print(region.name)
