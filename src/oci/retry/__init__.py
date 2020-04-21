# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .retry import BACKOFF_FULL_JITTER_VALUE, BACKOFF_EQUAL_JITTER_VALUE, BACKOFF_FULL_JITTER_EQUAL_ON_THROTTLE_VALUE
from .retry import RetryStrategyBuilder, NoneRetryStrategy, ExponentialBackoffRetryStrategyBase, ExponentialBackoffWithFullJitterRetryStrategy, ExponentialBackoffWithEqualJitterRetryStrategy, ExponentialBackoffWithFullJitterEqualForThrottlesRetryStrategy
from . import retry_checkers

#: A retry strategy which has all options enabled and which will use the default settings for those options. These
#: defaults are:
#:
#: * 5 total attempts
#: * Total allowed elapsed time for all requests of 300 seconds (5 minutes)
#: * Exponential backoff with jitter using a base time of 1 second, an exponent of 2 and a maximum wait time between calls of 30 seconds
#: * Exponential backoff with equal jitter is used for throttles as this guarantees some sleep time between attempts
#: * Exponential backoff with full jitter is used for other scenarios where we need to retry (e.g. timeouts, HTTP 5xx)
#: * Retries on the following exception types: timeouts and connection errors, HTTP 429s (throttles), any HTTP 5xx
DEFAULT_RETRY_STRATEGY = RetryStrategyBuilder().add_max_attempts() \
                                               .add_total_elapsed_time() \
                                               .add_service_error_check() \
                                               .get_retry_strategy()

__all__ = [
    "retry_checkers", "RetryStrategyBuilder", "NoneRetryStrategy", "ExponentialBackoffRetryStrategyBase",
    "ExponentialBackoffWithFullJitterRetryStrategy", "ExponentialBackoffWithEqualJitterRetryStrategy",
    "ExponentialBackoffWithFullJitterEqualForThrottlesRetryStrategy",
    "DEFAULT_RETRY_STRATEGY",
    "BACKOFF_FULL_JITTER_VALUE", "BACKOFF_EQUAL_JITTER_VALUE", "BACKOFF_FULL_JITTER_EQUAL_ON_THROTTLE_VALUE"
]
