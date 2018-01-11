# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from . import retry_checkers

import random
import time


class RetryStrategyBuilder(object):
    """
    A class which can build a retry strategy based on provided criteria. Criteria can be provided at construction time or
    afterwards via using the add_* (to add/enable criteria) and no_* (to disable/remove criteria) methods.

    When calculating the delay between retries, we use exponential backoff with full jitter as the default strategy
    vended by this builder.
    """
    BACKOFF_FULL_JITTER = 'full_jitter'

    def __init__(self, **kwargs):
        """
        Creates a new builder and initializes it based on any provided parameters.

        :param Boolean max_attempts_check (optional):
            Whether to enable a check that we don't exceed a certain number of attempts. If not provided
            this defaults to False (i.e. this check will not be done)

        :param Boolean service_error_check (optional):
            Whether to enable a check that will retry on connection errors, timeouts and service errors
            which match given combinations of HTTP statuses and textual error codes. If not provided
            this defaults to False (i.e. this check will not be done)

        :param int max_atttemps (optional):
            If we are checking that we don't exceed a certain number of attempts, what that number of
            attempts should be. This only applies if we are performing a check on the maximum number of
            attempts and will be ignored otherwise. If we are performing a check on the maximum number of
            attempts and this value is not provided, we will default to a maximum of 5 attempts

        :param dict service_error_retry_config (optional):
            If we are checking on service errors, we can configure what HTTP statuses (e.g. 429) to retry on and, optionally,
            whether the textual code (e.g. TooManyRequests) matches a given value.

            This is a dictionary where the key is an integer representing the HTTP status, and the value is a list(str) where we
            will test if the textual code in the service error is a member of the list. If an empty list is provided, then only
            the numeric status is checked for retry purposes.

            If we are performing a check on service errors and this value is not provided, then by default we will retry on
            HTTP 429's (throttles) without any textual code check.

        :param Boolean service_error_retry_on_any_5xx (optional):
            If we are checking on service errors, whether to retry on any HTTP 5xx received from the service. If
            we are performing a check on service errors and this value is not provided, it defaults to True (retry on any 5xx)

        :param int retry_base_sleep_time_millis (optional):
            For exponential backoff with jitter, the base time to use in our retry calculation in milliseconds. If not
            provided, this value defaults to 1000ms (i.e. 1 second)

        :param int retry_exponential_growth_factor (optional):
            For exponential backoff with jitter, the exponent which we will raise to the power of the number of attempts. If
            not provided, this value defaults to 2

        :param int retry_max_wait_time_millis (optional):
            For exponential backoff with jitter, the maximum amount of time to wait between retries. If not provided, this
            value defaults to 8000ms (i.e. 8 seconds)

        :param str backoff_type (optional):
            The type of backoff we want to do (e.g. full jitter). Currently the only supported value is 'full_jitter' (the convenience
            constant BACKOFF_FULL_JITTER in this class can also be used)
        """

        self.max_attempts_check = kwargs.get('max_attempts_check', False)
        self.service_error_check = kwargs.get('service_error_check', False)

        self.max_attempts = kwargs.get('max_attempts', None)
        self.service_error_retry_config = kwargs.get('service_error_retry_config', {})
        self.service_error_retry_on_any_5xx = kwargs.get('service_error_retry_on_any_5xx', True)

        self.retry_base_sleep_time_millis = kwargs.get('retry_base_sleep_time_millis', 1000)
        self.retry_exponential_growth_factor = kwargs.get('retry_exponential_growth_factor', 2)
        self.retry_max_wait_time_millis = kwargs.get('retry_max_wait_time_millis', 8000)

        if 'backoff_type' in kwargs and kwargs['backoff_type'] != self.BACKOFF_FULL_JITTER:
            raise ValueError('Currently full_jitter is the only supported backoff type')

    def add_max_attempts(self, max_attempts=None):
        self.max_attempts_check = True
        if max_attempts:
            self.max_attempts = max_attempts
        return self

    def no_max_attemps(self):
        self.max_attempts_check = False
        return self

    def add_service_error_check(self, **kwargs):
        self.service_error_check = True

        if 'service_error_retry_config' in kwargs:
            self.service_error_retry_config = kwargs['service_error_retry_config']
        elif 'service_error_status' in kwargs and 'service_error_codes' in kwargs:
            self.service_error_retry_config[kwargs['service_error_status']] = kwargs['service_error_codes']

        if 'service_error_retry_on_any_5xx' in kwargs:
            self.service_error_retry_on_any_5xx = kwargs['service_error_retry_on_any_5xx']

        return self

    def no_service_error_check(self):
        self.service_error_check = False
        return self

    def get_retry_strategy(self):
        checkers = []

        if self.max_attempts_check:
            if self.max_attempts:
                checkers.append(retry_checkers.LimitBasedRetryChecker(max_attempts=self.max_attempts))
            else:
                checkers.append(retry_checkers.LimitBasedRetryChecker())

        if self.service_error_check:
            if self.service_error_retry_config:
                checkers.append(
                    retry_checkers.TimeoutConnectionAndServiceErrorRetryChecker(
                        service_error_retry_config=self.service_error_retry_config,
                        retry_any_5xx=self.service_error_retry_on_any_5xx
                    )
                )
            else:
                checkers.append(retry_checkers.TimeoutConnectionAndServiceErrorRetryChecker(retry_any_5xx=self.service_error_retry_on_any_5xx))

        checker_container = retry_checkers.RetryCheckerContainer(checkers=checkers)

        return ExponentialBackoffWithFullJitterRetryStrategy(
            base_sleep_time_millis=self.retry_base_sleep_time_millis,
            exponent_growth_factor=self.retry_exponential_growth_factor,
            max_wait_millis=self.retry_max_wait_time_millis,
            checker_container=checker_container
        )


class ExponentialBackoffWithFullJitterRetryStrategy(object):
    """
    A retry strategy which does exponential backoff and full jitter. Times used are in milliseconds and
    the strategy can be described as:

    .. code-block:: none

        random(0, min(base_sleep_time_millis * exponent_growth_factor ** (attempt), max_wait_millis))

    """

    def __init__(self, base_sleep_time_millis, exponent_growth_factor, max_wait_millis, checker_container, **kwargs):
        """
        Creates a new instance of an exponential backoff with full jitter retry strategy.

        :param int base_sleep_time_millis:
            The base amount to sleep by, in milliseconds

        :param int exponent_growth_factor:
            The exponent part of our backoff. We will raise take this value and raising it to the power
            of attemps and then multiply this with base_sleep_time_millis

        :param int max_wait_millis:
            The maximum time we will wait between calls

        :param retry_checkers.RetryCheckerContainer checker_container:
            The checks to run to determine whether a failed call should be retried
        """
        self.base_sleep_time_millis = base_sleep_time_millis
        self.exponent_growth_factor = exponent_growth_factor
        self.max_wait_millis = max_wait_millis
        self.checkers = checker_container

    def make_retrying_call(self, func_ref, *func_args, **func_kwargs):
        """
        Calls the function given by func_ref. Any positional (*func_args) and keyword (**func_kwargs)
        arguments are passed as-is to func_ref.

        :param function func_ref:
            The function that we should call with retries

        :return: the result of calling func_ref
        """
        should_retry = True
        attempt = 0
        while should_retry:
            try:
                return func_ref(*func_args, **func_kwargs)
            except Exception as e:
                attempt += 1
                if self.checkers.should_retry(exception=e, current_attempt=attempt):
                    self.do_sleep(attempt)
                else:
                    raise

    def do_sleep(self, attempt):
        sleep_time_millis = random.uniform(0, min(self.base_sleep_time_millis * (self.exponent_growth_factor ** attempt), self.max_wait_millis))
        time.sleep(sleep_time_millis / 1000.0)  # time.sleep needs seconds, but can take fractional seconds
