# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

import random


def get_exponential_backoff_with_full_jitter_sleep_time(base_sleep_time_seconds, exponent_growth_factor, max_wait_between_calls_seconds, attempt):
    return random.uniform(0, min(base_sleep_time_seconds * (exponent_growth_factor ** attempt), max_wait_between_calls_seconds))


def get_exponential_backoff_with_equal_jitter_sleep_time(base_sleep_time_seconds, exponent_growth_factor, max_wait_between_calls_seconds, attempt):
    exponential_backoff_sleep = min(base_sleep_time_seconds * (exponent_growth_factor ** attempt), max_wait_between_calls_seconds)
    return (exponential_backoff_sleep / 2.0) + random.uniform(0, exponential_backoff_sleep / 2.0)
