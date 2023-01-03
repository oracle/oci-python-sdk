# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

try:
    import unittest.mock as mock
except ImportError:
    import mock

from oci._vendor.requests.exceptions import Timeout
from oci._vendor.requests.exceptions import ConnectionError as RequestsConnectionError

import oci
import oci.retry
import pytest
import time

from oci.exceptions import ServiceError
from oci.retry import RetryStrategyBuilder
from oci.util import should_record_body_position_for_retry, record_body_position_for_rewind, rewind_body
import tests.util


def test_limit_retry_checker():
    checker = oci.retry.retry_checkers.LimitBasedRetryChecker()
    assert 8 == checker.max_attempts  # Should default to 5

    assert checker.should_retry(current_attempt=1)  # retry if we failed the first attempt
    assert checker.should_retry(current_attempt=4)  # since we have made 4 attempts, we're allowed one more
    assert not checker.should_retry(current_attempt=8)  # we made 5 tries and couldn't do it, no more are allowed

    checker = oci.retry.retry_checkers.LimitBasedRetryChecker(max_attempts=1)
    assert not checker.should_retry(current_attempt=1)  # we are only allowed 1 attempt, so no more are allowed
    assert not checker.should_retry(current_attempt=5000)


def test_service_error_checker_timeouts():
    checker = oci.retry.retry_checkers.TimeoutConnectionAndServiceErrorRetryChecker()
    assert checker.retry_any_5xx
    assert checker.service_error_retry_config == {-1: [], 409: ['IncorrectState'], 429: []}

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
    service_error_501 = oci.exceptions.ServiceError(501, 'SomeCode', {}, None)
    service_error_502 = oci.exceptions.ServiceError(502, 'SomeCode', {}, None)
    assert checker.should_retry(exception=service_error_429)
    assert checker.should_retry(exception=service_error_500)
    assert not checker.should_retry(exception=service_error_501)
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
    assert not checker.should_retry(total_time_elapsed=600)

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

    assert not checker_container.should_retry(exception=RequestsConnectionError(), current_attempt=8)  # limit failed, service error passed
    # This is inside a try block because ConnectionError exists in Python 3 and not in Python 2
    try:
        assert not checker_container.should_retry(exception=ConnectionError(), current_attempt=8)  # limit failed, service error passed
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
    assert retrying_call.current_calls == 8  # we should have failed out after we hit the limit as per the retry strategy
    assert e.value.status == 502
    assert e.value.code == 'SomeCode'

    retrying_call.reset()
    retrying_call.return_sucess_on_call_number = 4
    assert retry_strategy.make_retrying_call(retrying_call.do_call)
    assert retrying_call.current_calls == 4

    retrying_call.reset()
    retrying_call.return_sucess_on_call_number = 8  # Boundary for the limit check
    assert retry_strategy.make_retrying_call(retrying_call.do_call)
    assert retrying_call.current_calls == 8

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
    assert retrying_call.current_calls == 8


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
    assert isinstance(builder.get_retry_strategy(), oci.retry.ExponentialBackOffWithDecorrelatedJitterRetryStrategy)

    assert isinstance(oci.retry.DEFAULT_RETRY_STRATEGY, oci.retry.ExponentialBackOffWithDecorrelatedJitterRetryStrategy)

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


# -------------------- Test retries for file-like bodies --------------------
class FileLikeBody:
    def __init__(self,
                 no_read=None,
                 no_seek=None,
                 bad_seek=None,
                 no_tell=None,
                 bad_tell=None):
        if not no_read:
            self.read = mock.Mock()

        if not no_seek:
            if bad_seek:
                mock_seek = mock.Mock()
                mock_seek.side_effect = IOError
                self.seek = mock_seek
            else:
                mock_seek = mock.Mock()
                self.seek = mock_seek

        if not no_tell:
            if bad_tell:
                mock_tell = mock.Mock()
                mock_tell.side_effect = OSError
                self.tell = mock_tell
            else:
                mock_tell = mock.Mock()
                mock_tell.return_value = 5
                self.tell = mock_tell


# A class to simulate sending file-like bodies with retry
class MockClient:
    def __init__(self):
        self.attempts = 0
        self.retry_strategy = RetryStrategyBuilder(max_attempts=2,
                                                   service_error_check=True,
                                                   service_error_retry_on_any_5xx=True,
                                                   max_attempts_check=True).get_retry_strategy()
        self.body_position = None

    # This method throws ServiceError on the first attempt, forcing retries
    def call_api(self, body):
        self.attempts += 1
        if self.attempts <= 1:
            if getattr(body, 'seek', None) and getattr(body, 'tell', None):
                # Pretend that we're sending the body
                try:
                    body.seek(100)
                    current_position = body.tell()
                    assert current_position == 100
                except (IOError, OSError):
                    pass
            # Fail on first attempt
            raise ServiceError(500, "blah", {}, "blah")

        self.body_position = body.tell()


def test_failed_retries_for_binary_files():
    test_file = tests.util.get_resource_path('test_image.png')

    # In order to force code the file-like body code path, mock the method in retrying_call as call_api
    mock_client = MockClient()
    # Put an object
    with open(test_file, 'rb') as file:
        mock_client.retry_strategy.make_retrying_call(mock_client.call_api, body=file)

    # On the second attempt, make sure that the body is rewound
    assert mock_client.attempts == 2
    assert mock_client.body_position == 0


def test_failed_retries_for_text_files():
    test_file = tests.util.get_resource_path('config')

    # In order to force code the file-like body code path, mock the method in retrying_call as call_api
    mock_client = MockClient()
    # Put an object
    with open(test_file, 'r') as file:
        mock_client.retry_strategy.make_retrying_call(mock_client.call_api, body=file)

    # On the second attempt, make sure that the body is rewound
    assert mock_client.attempts == 2
    assert mock_client.body_position == 0


# File-like bodies which cannot be rewound should not be retried
def test_failed_retries_for_bad_bodies():
    no_tell_body = FileLikeBody(no_tell=True)
    no_seek_body = FileLikeBody(no_seek=True)
    bad_tell_body = FileLikeBody(bad_tell=True)
    bad_seek_body = FileLikeBody(bad_seek=True)

    # In order to force code the file-like body code path, mock the method in retrying_call as call_api
    for body in (no_tell_body, no_seek_body, bad_tell_body, bad_seek_body):
        mock_client = MockClient()
        with pytest.raises(ServiceError):
            mock_client.retry_strategy.make_retrying_call(mock_client.call_api, body=body)
        assert mock_client.attempts == 1


# -------------------- Test retry utils --------------------
def test_should_record_body_position_for_retry():
    mock_client = mock.Mock()
    mock_client.__name__ = "BaseClient"
    mock_client.mock_method = mock.Mock()
    mock_client.mock_method.__name__ = "call_api"
    mock_body = mock.Mock()
    mock_body.read = mock.Mock()

    # Happy case, the func_ref is call_api and the func_kwargs have a body with attribute 'read'
    assert should_record_body_position_for_retry(mock_client.mock_method, body=mock_body)

    # Body does not have "read" attribute
    assert not should_record_body_position_for_retry(mock_client.mock_method, body='12345')

    # pass body but the method name is different
    mock_client.mock_method.__name__ = "a_different_method"
    assert not should_record_body_position_for_retry(mock_client.mock_method, body=mock_body)


def test_record_body_position_for_retry():
    # Happy case, the body supports tell and there is no error
    is_body_retryable, body_position = record_body_position_for_rewind(body=FileLikeBody())
    assert is_body_retryable
    assert body_position == 5

    # Case when the body does not support tell, we should not retry
    is_body_retryable, body_position = record_body_position_for_rewind(body=FileLikeBody(no_tell=True))
    assert not is_body_retryable
    assert not body_position

    # Case when tell raises error, we should not retry
    is_body_retryable, body_position = record_body_position_for_rewind(body=FileLikeBody(bad_tell=True))
    assert not is_body_retryable
    assert not body_position


def test_rewind_body_for_retry():
    # Happy case, the body supports seek and there is no error
    should_retry = rewind_body(body=FileLikeBody(), body_position=5)
    assert should_retry

    # Case when the body does not support seek, we should not retry
    should_retry = rewind_body(body=FileLikeBody(no_seek=True), body_position=5)
    assert not should_retry

    # Case when seek raises error, we should not retry
    should_retry = rewind_body(body=FileLikeBody(bad_seek=True), body_position=5)
    assert not should_retry
