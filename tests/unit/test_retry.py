# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from oci._vendor.requests.exceptions import Timeout
from oci._vendor.requests.exceptions import ConnectionError as RequestsConnectionError

import oci
import oci.retry
import pytest
import time


def test_limit_retry_checker():
    checker = oci.retry.retry_checkers.LimitBasedRetryChecker()
    assert 5 == checker.max_attempts  # Should default to 5

    assert checker.should_retry(current_attempt=1)  # retry if we failed the first attempt
    assert checker.should_retry(current_attempt=4)  # since we have made 4 attempts, we're allowed one more
    assert not checker.should_retry(current_attempt=5)  # we made 5 tries and couldn't do it, no more are allowed

    checker = oci.retry.retry_checkers.LimitBasedRetryChecker(max_attempts=1)
    assert not checker.should_retry(current_attempt=1)  # we are only allowed 1 attempt, so no more are allowed
    assert not checker.should_retry(current_attempt=5000)


def test_service_error_checker_timeouts():
    checker = oci.retry.retry_checkers.TimeoutConnectionAndServiceErrorRetryChecker()
    assert checker.retry_any_5xx
    assert checker.service_error_retry_config == {-1: [], 429: []}

    assert checker.should_retry(exception=Timeout())
    assert checker.should_retry(exception=RequestsConnectionError())
    assert checker.should_retry(exception=oci.exceptions.RequestException())
    assert checker.should_retry(exception=oci.exceptions.ConnectTimeout())
    assert not checker.should_retry(exception=RuntimeError())
    # This is inside a try block because ConnectionError exists in Python 3 and not in Python 2
    try:
        assert checker.should_retry(exception=ConnectionError())
    except NameError:
        pass

    service_error_429 = oci.exceptions.ServiceError(429, 'TooManyRequests', {}, None)
    service_error_500 = oci.exceptions.ServiceError(500, 'SomeCode', {}, None)
    service_error_502 = oci.exceptions.ServiceError(502, 'SomeCode', {}, None)
    assert checker.should_retry(exception=service_error_429)
    assert checker.should_retry(exception=service_error_500)
    assert checker.should_retry(exception=service_error_502)

    checker = oci.retry.retry_checkers.TimeoutConnectionAndServiceErrorRetryChecker(
        service_error_retry_config={502: [], 429: ['OnlyThisCode']},
        retry_any_5xx=False
    )
    assert not checker.should_retry(exception=service_error_429)
    assert not checker.should_retry(exception=service_error_500)
    assert checker.should_retry(exception=service_error_502)

    service_error_429.code = 'OnlyThisCode'
    assert checker.should_retry(exception=service_error_429)


def test_total_time_limit_exceeded_retry_checker():
    checker = oci.retry.retry_checkers.TotalTimeExceededRetryChecker()
    assert checker.should_retry(total_time_elapsed=299)
    assert not checker.should_retry(total_time_elapsed=300)

    checker = oci.retry.retry_checkers.TotalTimeExceededRetryChecker(time_limit_seconds=20)
    assert checker.should_retry(total_time_elapsed=19)
    assert not checker.should_retry(total_time_elapsed=20)
    assert not checker.should_retry(total_time_elapsed=25)


def test_checker_container():
    checkers = [
        oci.retry.retry_checkers.LimitBasedRetryChecker(),
        oci.retry.retry_checkers.TimeoutConnectionAndServiceErrorRetryChecker()
    ]
    checker_container = oci.retry.retry_checkers.RetryCheckerContainer(checkers=checkers)

    assert not checker_container.should_retry(exception=RequestsConnectionError(), current_attempt=7)  # limit failed, service error passed
    # This is inside a try block because ConnectionError exists in Python 3 and not in Python 2
    try:
        assert not checker_container.should_retry(exception=ConnectionError(), current_attempt=7)  # limit failed, service error passed
    except NameError:
        pass
    assert not checker_container.should_retry(exception=RuntimeError(), current_attempt=3)  # limit passed, service error failed
    assert checker_container.should_retry(exception=oci.exceptions.ServiceError(429, 'TooManyRequests', {}, None), current_attempt=1)  # both checks pass
    assert checker_container.should_retry(exception=oci.exceptions.ServiceError(500, 'InternalServerError', {}, None), current_attempt=3)  # both checks pass


def test_retry_strategy_builder():
    retry_strategy = oci.retry.RetryStrategyBuilder().add_max_attempts().add_service_error_check().get_retry_strategy()
    retrying_call = MakeRetryingCall(exception_to_throw=RuntimeError(), return_sucess_on_call_number=3)

    with pytest.raises(RuntimeError):
        retry_strategy.make_retrying_call(retrying_call.do_call)
    assert retrying_call.current_calls == 1

    retrying_call.reset()
    retrying_call.exception_to_throw = RequestsConnectionError()
    # This is inside a try block because ConnectionError exists in Python 3 and not in Python 2
    try:
        retrying_call.exception_to_throw = ConnectionError()
    except NameError:
        pass
    assert retry_strategy.make_retrying_call(retrying_call.do_call)
    assert retrying_call.current_calls == 3

    retrying_call.reset()
    retrying_call.exception_to_throw = Timeout()
    assert retry_strategy.make_retrying_call(retrying_call.do_call)
    assert retrying_call.current_calls == 3

    retrying_call.reset()
    retrying_call.exception_to_throw = oci.exceptions.ServiceError(502, 'SomeCode', {}, None)
    retrying_call.return_sucess_on_call_number = 10
    with pytest.raises(oci.exceptions.ServiceError) as e:
        retry_strategy.make_retrying_call(retrying_call.do_call)
    assert retrying_call.current_calls == 5  # we should have failed out after we hit the limit as per the retry strategy
    assert e.value.status == 502
    assert e.value.code == 'SomeCode'

    retrying_call.reset()
    retrying_call.return_sucess_on_call_number = 4
    assert retry_strategy.make_retrying_call(retrying_call.do_call)
    assert retrying_call.current_calls == 4

    retrying_call.reset()
    retrying_call.return_sucess_on_call_number = 5  # Boundary for the limit check
    assert retry_strategy.make_retrying_call(retrying_call.do_call)
    assert retrying_call.current_calls == 5

    retrying_call.reset()
    retrying_call.exception_to_throw = oci.exceptions.ServiceError(404, 'NotFound', {}, None)
    with pytest.raises(oci.exceptions.ServiceError) as e:
        retry_strategy.make_retrying_call(retrying_call.do_call)
    assert retrying_call.current_calls == 1  # should have failed after the first call
    assert e.value.status == 404
    assert e.value.code == 'NotFound'

    retrying_call.reset()
    retrying_call.exception_to_throw = oci.exceptions.ServiceError(429, 'NotFound', {}, None)
    assert retry_strategy.make_retrying_call(retrying_call.do_call)
    assert retrying_call.current_calls == 5


def test_retry_strategy_none_retry_strategy():
    retry_strategy = oci.retry.NoneRetryStrategy()
    retrying_call = MakeRetryingCall(exception_to_throw=oci.exceptions.ServiceError(429, 'NotFound', {}, None), return_sucess_on_call_number=50)
    with pytest.raises(oci.exceptions.ServiceError) as e:
        retry_strategy.make_retrying_call(retrying_call.do_call)
    assert e.value.status == 429
    assert retrying_call.current_calls == 1

    retrying_call = MakeRetryingCall(exception_to_throw=None, return_sucess_on_call_number=1)
    result = retry_strategy.make_retrying_call(retrying_call.do_call)
    assert result
    assert retrying_call.current_calls == 1


def test_retry_strategy_builder_with_total_elapsed_time():
    retry_strategy = oci.retry.RetryStrategyBuilder().add_service_error_check().add_total_elapsed_time(total_elapsed_time_seconds=20).get_retry_strategy()
    retrying_call = MakeRetryingCall(exception_to_throw=oci.exceptions.ServiceError(429, 'NotFound', {}, None), return_sucess_on_call_number=50)

    start = time.time()
    with pytest.raises(oci.exceptions.ServiceError) as e:
        retry_strategy.make_retrying_call(retrying_call.do_call)
    elapsed = time.time() - start
    assert e.value.status == 429
    assert retrying_call.current_calls < 50
    assert elapsed < 60


def test_retry_strategy_builder_different_types():
    builder = oci.retry.RetryStrategyBuilder()
    assert isinstance(builder.get_retry_strategy(), oci.retry.NoneRetryStrategy)

    assert isinstance(oci.retry.DEFAULT_RETRY_STRATEGY, oci.retry.ExponentialBackoffWithFullJitterEqualForThrottlesRetryStrategy)

    builder.add_max_attempts()

    builder.backoff_type = oci.retry.BACKOFF_FULL_JITTER_VALUE
    assert isinstance(builder.get_retry_strategy(), oci.retry.ExponentialBackoffWithFullJitterRetryStrategy)

    builder.backoff_type = oci.retry.BACKOFF_EQUAL_JITTER_VALUE
    assert isinstance(builder.get_retry_strategy(), oci.retry.ExponentialBackoffWithEqualJitterRetryStrategy)

    builder.backoff_type = oci.retry.BACKOFF_FULL_JITTER_EQUAL_ON_THROTTLE_VALUE
    assert isinstance(builder.get_retry_strategy(), oci.retry.ExponentialBackoffWithFullJitterEqualForThrottlesRetryStrategy)


# A utility class which can make retrying calls and track how many calls it made
class MakeRetryingCall(object):
    def __init__(self, exception_to_throw, return_sucess_on_call_number):
        self.exception_to_throw = exception_to_throw
        self.return_sucess_on_call_number = return_sucess_on_call_number
        self.current_calls = 0

    def reset(self):
        self.current_calls = 0

    def do_call(self):
        self.current_calls += 1

        if self.current_calls == self.return_sucess_on_call_number:
            return True
        else:
            raise self.exception_to_throw
