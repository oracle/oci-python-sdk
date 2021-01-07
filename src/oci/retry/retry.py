# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# Contains classes for defining and building retry strategies.

from ..exceptions import ServiceError
from . import retry_checkers
from . import retry_sleep_utils

import time

BACKOFF_FULL_JITTER_VALUE = 'full_jitter'
BACKOFF_EQUAL_JITTER_VALUE = 'equal_jitter'
BACKOFF_FULL_JITTER_EQUAL_ON_THROTTLE_VALUE = 'full_jitter_with_equal_on_throttle'

VALID_BACKOFF_TYPES = [BACKOFF_FULL_JITTER_VALUE, BACKOFF_EQUAL_JITTER_VALUE, BACKOFF_FULL_JITTER_EQUAL_ON_THROTTLE_VALUE]


class RetryStrategyBuilder(object):
    """
    A class which can build a retry strategy based on provided criteria. Criteria can be provided at construction time or
    afterwards via using the ``add_*`` (to add/enable criteria) and ``no_*`` (to disable/remove criteria) methods.

    Trying to build a strategy when there are no enabled checks will result in a :py:class:`oci.retry.NoneRetryStrategy`
    being produced.

    This builder is intended as a convenience, but callers are also able to bypass this and construct retry strategies
    directly.
    """

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

        :param Boolean total_elapsed_time_check (optional):
            Whether to enable a check that we don't exceed a certain amount of time when retrying. This is intended
            for scenarios such as "keep retrying for 5 minutes".  If not provided this defaults to False
            (i.e. this check will not be done)

        :param int max_attempts (optional):
            If we are checking that we don't exceed a certain number of attempts, what that number of
            attempts should be. This only applies if we are performing a check on the maximum number of
            attempts and will be ignored otherwise. If we are performing a check on the maximum number of
            attempts and this value is not provided, we will default to a maximum of 5 attempts

        :param int total_elapsed_time_seconds (optional):
            If we are checking that we don't exceed a certain amount of time when retrying, what that amount of
            time should be (in seconds). This only applies if we are perfoming a check on the total elapsed time and will
            be ignored otherwise. If we are performing a check on the total elapsed time and this value is not provided, we
            will default to 300 seconds (5 minutes)

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

        :param int retry_base_sleep_time_seconds (optional):
            For exponential backoff with jitter, the base time to use in our retry calculation in seconds. If not
            provided, this value defaults to 1 second

        :param int retry_exponential_growth_factor (optional):
            For exponential backoff with jitter, the exponent which we will raise to the power of the number of attempts. If
            not provided, this value defaults to 2

        :param int retry_max_wait_between_calls_seconds (optional):
            For exponential backoff with jitter, the maximum amount of time to wait between retries. If not provided, this
            value defaults to 30 seconds

        :param str backoff_type (optional):
            The type of backoff we want to do (e.g. full jitter). The convenience constants in this retry module: ``BACKOFF_FULL_JITTER_VALUE``,
            ``BACKOFF_EQUAL_JITTER_VALUE``, and ``BACKOFF_FULL_JITTER_EQUAL_ON_THROTTLE_VALUE`` can be used as values here. If no value is specified then
            the value ``BACKOFF_FULL_JITTER_EQUAL_ON_THROTTLE_VALUE`` will be used. This will use exponential backoff and full jitter on all retries
            except for throttles, in which case it will use exponential backoff and equal jitter.
        """

        self.max_attempts_check = kwargs.get('max_attempts_check', False)
        self.service_error_check = kwargs.get('service_error_check', False)
        self.total_elapsed_time_check = kwargs.get('total_elapsed_time_check', False)

        self.max_attempts = kwargs.get('max_attempts', None)
        self.total_elapsed_time_seconds = kwargs.get('total_elapsed_time_seconds', None)
        self.service_error_retry_config = kwargs.get('service_error_retry_config', {})
        self.service_error_retry_on_any_5xx = kwargs.get('service_error_retry_on_any_5xx', True)

        self.retry_base_sleep_time_seconds = kwargs.get('retry_base_sleep_time_seconds', 1)
        self.retry_exponential_growth_factor = kwargs.get('retry_exponential_growth_factor', 2)
        self.retry_max_wait_between_calls_seconds = kwargs.get('retry_max_wait_between_calls_seconds', 30)

        self.backoff_type = BACKOFF_FULL_JITTER_EQUAL_ON_THROTTLE_VALUE
        if 'backoff_type' in kwargs:
            if kwargs['backoff_type'] not in VALID_BACKOFF_TYPES:
                raise ValueError('Unrecognized backoff type supplied. Recognized types are: {}'.format(VALID_BACKOFF_TYPES))
            else:
                self.backoff_type = kwargs['backoff_type']

    def add_max_attempts(self, max_attempts=None):
        self.max_attempts_check = True
        if max_attempts:
            self.max_attempts = max_attempts
        return self

    def no_max_attemps(self):
        self.max_attempts_check = False
        return self

    def add_total_elapsed_time(self, total_elapsed_time_seconds=None):
        self.total_elapsed_time_check = True
        if total_elapsed_time_seconds:
            self.total_elapsed_time_seconds = total_elapsed_time_seconds
        return self

    def no_total_elapsed_time(self):
        self.total_elapsed_time_check = False
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
        if not self.max_attempts_check and not self.service_error_check and not self.total_elapsed_time_check:
            return NoneRetryStrategy()

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

        if self.total_elapsed_time_check:
            if self.total_elapsed_time_seconds:
                checkers.append(retry_checkers.TotalTimeExceededRetryChecker(time_limit_seconds=self.total_elapsed_time_seconds))
            else:
                checkers.append(retry_checkers.TotalTimeExceededRetryChecker())

        checker_container = retry_checkers.RetryCheckerContainer(checkers=checkers)

        if self.backoff_type == BACKOFF_FULL_JITTER_VALUE:
            return ExponentialBackoffWithFullJitterRetryStrategy(
                base_sleep_time_seconds=self.retry_base_sleep_time_seconds,
                exponent_growth_factor=self.retry_exponential_growth_factor,
                max_wait_between_calls_seconds=self.retry_max_wait_between_calls_seconds,
                checker_container=checker_container
            )
        elif self.backoff_type == BACKOFF_EQUAL_JITTER_VALUE:
            return ExponentialBackoffWithEqualJitterRetryStrategy(
                base_sleep_time_seconds=self.retry_base_sleep_time_seconds,
                exponent_growth_factor=self.retry_exponential_growth_factor,
                max_wait_between_calls_seconds=self.retry_max_wait_between_calls_seconds,
                checker_container=checker_container
            )
        elif self.backoff_type == BACKOFF_FULL_JITTER_EQUAL_ON_THROTTLE_VALUE:
            return ExponentialBackoffWithFullJitterEqualForThrottlesRetryStrategy(
                base_sleep_time_seconds=self.retry_base_sleep_time_seconds,
                exponent_growth_factor=self.retry_exponential_growth_factor,
                max_wait_between_calls_seconds=self.retry_max_wait_between_calls_seconds,
                checker_container=checker_container
            )
        else:
            raise ValueError('Unrecognized backoff type: {}. Expected one of: {}'.format(self.backoff_type, VALID_BACKOFF_TYPES))


class NoneRetryStrategy(object):
    """
    A strategy that does not retry
    """

    def make_retrying_call(self, func_ref, *func_args, **func_kwargs):
        """
        Calls the function given by func_ref. Any positional (``*func_args``) and keyword (``**func_kwargs``)
        arguments are passed as-is to func_ref.

        :param function func_ref:
            The function that we should call with retries

        :return: the result of calling func_ref
        """
        return func_ref(*func_args, **func_kwargs)


class ExponentialBackoffRetryStrategyBase(object):
    """
    A base retry strategy from which other retry strategies inherit. Implementors can create a subclass of this to define
    their own retry logic. This is primarily useful when an implementor wishes to customize the sleep strategy used - to
    customize the checking logic on whether a retry should be done, implementors can define their own subclasses of
    :py:class:`oci.retry.retry_checkers.BaseRetryChecker` and provide this in the checker container.
    """

    def __init__(self, base_sleep_time_seconds, exponent_growth_factor, max_wait_between_calls_seconds, checker_container, **kwargs):
        """
        Creates a new instance of an exponential backoff with full jitter retry strategy.

        :param int base_sleep_time_seconds:
            The base amount to sleep by, in seconds

        :param int exponent_growth_factor:
            The exponent part of our backoff. We will raise take this value and raising it to the power
            of attemps and then multiply this with base_sleep_time_seconds

        :param int max_wait_between_calls_seconds:
            The maximum time we will wait between calls, in seconds

        :param retry_checkers.RetryCheckerContainer checker_container:
            The checks to run to determine whether a failed call should be retried
        """
        self.base_sleep_time_seconds = base_sleep_time_seconds
        self.exponent_growth_factor = exponent_growth_factor
        self.max_wait_between_calls_seconds = max_wait_between_calls_seconds
        self.checkers = checker_container

    def make_retrying_call(self, func_ref, *func_args, **func_kwargs):
        """
        Calls the function given by func_ref. Any positional (``*func_args``) and keyword (``**func_kwargs``)
        arguments are passed as-is to func_ref.

        :param function func_ref:
            The function that we should call with retries

        :return: the result of calling func_ref
        """
        should_retry = True
        attempt = 0
        start_time = time.time()
        while should_retry:
            try:
                return func_ref(*func_args, **func_kwargs)
            except Exception as e:
                attempt += 1
                if self.checkers.should_retry(exception=e, current_attempt=attempt, total_time_elapsed=(time.time() - start_time)):
                    self.do_sleep(attempt, e)
                else:
                    raise

    def do_sleep(self, attempt, exception):
        raise NotImplementedError('Subclasses should implement this')


class ExponentialBackoffWithFullJitterRetryStrategy(ExponentialBackoffRetryStrategyBase):
    """
    A retry strategy which does exponential backoff and full jitter. Times used are in seconds and
    the strategy can be described as:

    .. code-block:: none

        random(0, min(base_sleep_time_seconds * exponent_growth_factor ** (attempt), max_wait_seconds))

    """

    def __init__(self, base_sleep_time_seconds, exponent_growth_factor, max_wait_between_calls_seconds, checker_container, **kwargs):
        """
        Creates a new instance of an exponential backoff with full jitter retry strategy.

        :param int base_sleep_time_seconds:
            The base amount to sleep by, in seconds

        :param int exponent_growth_factor:
            The exponent part of our backoff. We will raise take this value and raising it to the power
            of attempts and then multiply this with base_sleep_time_seconds

        :param int max_wait_between_calls_seconds:
            The maximum time we will wait between calls, in seconds

        :param retry_checkers.RetryCheckerContainer checker_container:
            The checks to run to determine whether a failed call should be retried
        """
        super(ExponentialBackoffWithFullJitterRetryStrategy, self) \
            .__init__(base_sleep_time_seconds, exponent_growth_factor, max_wait_between_calls_seconds, checker_container, **kwargs)

    def do_sleep(self, attempt, exception):
        sleep_time_subseconds = retry_sleep_utils.get_exponential_backoff_with_full_jitter_sleep_time(
            self.base_sleep_time_seconds, self.exponent_growth_factor, self.max_wait_between_calls_seconds, attempt)
        time.sleep(sleep_time_subseconds)  # time.sleep needs seconds, but can take fractional seconds


class ExponentialBackoffWithEqualJitterRetryStrategy(ExponentialBackoffRetryStrategyBase):
    """
    A retry strategy which does exponential backoff and equal jitter. Times used are in seconds and
    the strategy can be described as:

    .. code-block:: none

        exponential_backoff_sleep = min(base_sleep_time_seconds * exponent_growth_factor ** (attempt), max_wait_seconds)
        sleep_with_jitter = (exponential_backoff_sleep / 2) + random(0, exponential_backoff_sleep / 2)

    """

    def __init__(self, base_sleep_time_seconds, exponent_growth_factor, max_wait_between_calls_seconds, checker_container, **kwargs):
        """
        Creates a new instance of an exponential backoff with equal jitter retry strategy.

        :param int base_sleep_time_seconds:
            The base amount to sleep by, in seconds

        :param int exponent_growth_factor:
            The exponent part of our backoff. We will raise take this value and raising it to the power
            of attemps and then multiply this with base_sleep_time_seconds

        :param int max_wait_between_calls_seconds:
            The maximum time we will wait between calls, in seconds

        :param retry_checkers.RetryCheckerContainer checker_container:
            The checks to run to determine whether a failed call should be retried
        """
        super(ExponentialBackoffWithEqualJitterRetryStrategy, self) \
            .__init__(base_sleep_time_seconds, exponent_growth_factor, max_wait_between_calls_seconds, checker_container, **kwargs)

    def do_sleep(self, attempt, exception):
        sleep_time_seconds = retry_sleep_utils.get_exponential_backoff_with_equal_jitter_sleep_time(self.base_sleep_time_seconds, self.exponent_growth_factor, self.max_wait_between_calls_seconds, attempt)
        time.sleep(sleep_time_seconds)


class ExponentialBackoffWithFullJitterEqualForThrottlesRetryStrategy(ExponentialBackoffRetryStrategyBase):
    """
    A retry strategy that does exponential backoff and full jitter for most retries, but uses exponential backoff with
    equal jitter for throttles. This provides a reasonable distribution of retry times for most retryable error cases,
    but for throttles guarantees some sleep time
    """

    def __init__(self, base_sleep_time_seconds, exponent_growth_factor, max_wait_between_calls_seconds, checker_container, **kwargs):
        """
        Creates a new instance of the retry strategy.

        :param int base_sleep_time_seconds:
            The base amount to sleep by, in seconds

        :param int exponent_growth_factor:
            The exponent part of our backoff. We will raise take this value and raising it to the power
            of attemps and then multiply this with base_sleep_time_seconds

        :param int max_wait_between_calls_seconds:
            The maximum time we will wait between calls, in seconds

        :param retry_checkers.RetryCheckerContainer checker_container:
            The checks to run to determine whether a failed call should be retried
        """
        super(ExponentialBackoffWithFullJitterEqualForThrottlesRetryStrategy, self) \
            .__init__(base_sleep_time_seconds, exponent_growth_factor, max_wait_between_calls_seconds, checker_container, **kwargs)

    def do_sleep(self, attempt, exception):
        if isinstance(exception, ServiceError):
            if exception.status == 429:
                sleep_time_seconds = retry_sleep_utils.get_exponential_backoff_with_equal_jitter_sleep_time(
                    self.base_sleep_time_seconds, self.exponent_growth_factor, self.max_wait_between_calls_seconds, attempt)
            else:
                sleep_time_seconds = retry_sleep_utils.get_exponential_backoff_with_full_jitter_sleep_time(
                    self.base_sleep_time_seconds, self.exponent_growth_factor, self.max_wait_between_calls_seconds, attempt)
        else:
            sleep_time_seconds = retry_sleep_utils.get_exponential_backoff_with_full_jitter_sleep_time(
                self.base_sleep_time_seconds, self.exponent_growth_factor, self.max_wait_between_calls_seconds, attempt)

        time.sleep(sleep_time_seconds)
