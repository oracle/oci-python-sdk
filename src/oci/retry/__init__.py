# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from .retry import BACKOFF_FULL_JITTER_VALUE, BACKOFF_EQUAL_JITTER_VALUE, BACKOFF_FULL_JITTER_EQUAL_ON_THROTTLE_VALUE
from .retry import RetryStrategyBuilder, NoneRetryStrategy, ExponentialBackoffRetryStrategyBase, ExponentialBackoffWithFullJitterRetryStrategy, ExponentialBackoffWithEqualJitterRetryStrategy, ExponentialBackoffWithFullJitterEqualForThrottlesRetryStrategy
from . import retry_checkers

# A retry strategy which has all options enabled and which will use the default settings for those options
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
