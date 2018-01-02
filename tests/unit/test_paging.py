from requests.exceptions import Timeout
from requests.exceptions import ConnectionError

import oci
import oci.pagination
import oci.pagination.internal
import os
import pytest

PAGE_SIZE = 10


def test_manual_paging(identity, config):
    request_number = 0
    previous_first_ocid = None
    next_page = None

    while True:
        if request_number == 0:
            response = identity.list_users(config["tenancy"], limit=PAGE_SIZE)
        else:
            response = identity.list_users(config["tenancy"], limit=PAGE_SIZE, page=next_page)

        if not response.has_next_page:
            break

        next_page = response.next_page
        request_number += 1
        assert response.status == 200
        assert previous_first_ocid != response.data[0].id

        previous_first_ocid = response.data[0].id

    # Make sure we've at least looked at a couple pages.
    assert request_number > 1


def test_pagination_get_all_results(identity, config):
    all_users_response = oci.pagination.list_call_get_all_results(identity.list_users, config["tenancy"])
    assert not all_users_response.has_next_page
    assert len(all_users_response.data) > 0

    found_test_user = False
    for user in all_users_response.data:
        if user.id == config["user"]:
            found_test_user = True
            break
    assert found_test_user


def test_pagination_get_up_to_limit(identity, config):
    # There may not be 70 users, so only check that we get no more than what we ask for
    list_users_response = oci.pagination.list_call_get_up_to_limit(identity.list_users, 70, 10, config["tenancy"])
    assert len(list_users_response.data) <= 70

    # There should always be at least one user, so asking for one should get us exactly one
    list_users_response = oci.pagination.list_call_get_up_to_limit(identity.list_users, 1, 1, config["tenancy"])
    assert list_users_response.has_next_page
    assert len(list_users_response.data) == 1


def test_pagination_get_up_to_limit_none_limit(identity, config):
    list_users_response = oci.pagination.list_call_get_up_to_limit(identity.list_users, None, 10, config["tenancy"])
    assert list_users_response.has_next_page
    assert len(list_users_response.data) <= 10


def test_pagination_get_all_yields(identity, config):
    all_users = []
    found_test_user = True
    for user in oci.pagination.list_call_get_all_results_generator(identity.list_users, 'record', config["tenancy"]):
        assert user.id is not None
        assert user.name is not None
        all_users.append(user)
        if config["user"] == user.id:
            found_test_user = True

    assert len(all_users) > 1
    assert found_test_user

    all_users_response = oci.pagination.list_call_get_all_results(identity.list_users, config["tenancy"])

    # Some jitter in case other tests are adding/removing users, but they should be close to each other
    assert abs(len(all_users_response.data) - len(all_users)) < 5


def test_pagination_get_up_to_limit_yields_none_limit(identity, config):
    num_iterations = 0
    call_result = None
    for response in oci.pagination.list_call_get_up_to_limit_generator(identity.list_users, None, 10, 'response', config["tenancy"]):
        call_result = response
        num_iterations += 1

    assert num_iterations == 1  # Since we had a none limit, yield a single page
    assert len(call_result.data) > 1
    assert len(call_result.data) <= 10

    users = []
    num_iterations = 0
    for user in oci.pagination.list_call_get_up_to_limit_generator(identity.list_users, None, 10, 'record', config["tenancy"]):
        assert user.id is not None
        assert user.name is not None
        num_iterations += 1
        users.append(user)
    assert num_iterations == len(users)
    assert len(users) == len(call_result.data)


def test_pagination_get_up_to_limit_yields(identity, config):
    num_iterations = 0
    users_from_response_gen = []
    for response in oci.pagination.list_call_get_up_to_limit_generator(identity.list_users, 70, 10, 'response', config["tenancy"]):
        num_iterations += 1
        users_from_response_gen.extend(response.data)
    assert num_iterations > 1
    assert num_iterations <= 7
    assert len(users_from_response_gen) <= 70

    users = []
    num_iterations = 0
    for user in oci.pagination.list_call_get_up_to_limit_generator(identity.list_users, 70, 10, 'record', config["tenancy"]):
        assert user.id is not None
        assert user.name is not None
        num_iterations += 1
        users.append(user)
    assert num_iterations > 1
    assert num_iterations <= 70
    assert len(users_from_response_gen) == len(users)

    users = []
    num_iterations = 0
    for user in oci.pagination.list_call_get_up_to_limit_generator(identity.list_users, 1, 1, 'record', config["tenancy"]):
        assert user.id is not None
        assert user.name is not None
        num_iterations += 1
        users.append(user)
    assert len(users) == 1
    assert num_iterations == 1


def test_pagination_when_no_data_exists(compute):
    all_records_eager = oci.pagination.list_call_get_all_results(compute.list_images, os.environ.get("OCI_PYSDK_COMPARTMENT_ID"), operating_system='superman fake os')
    limit_records_eager = oci.pagination.list_call_get_up_to_limit(compute.list_images, 20, 5, os.environ.get("OCI_PYSDK_COMPARTMENT_ID"), operating_system='superman fake os')

    assert len(all_records_eager.data) == 0
    assert len(limit_records_eager.data) == 0

    num_iterations = 0
    call_result = None
    for response in oci.pagination.list_call_get_all_results_generator(compute.list_images, 'response', os.environ.get("OCI_PYSDK_COMPARTMENT_ID"), operating_system='superman fake os'):
        num_iterations += 1
        call_result = response
    assert num_iterations == 1
    assert len(call_result.data) == 0

    num_iterations = 0
    call_result = None
    for response in oci.pagination.list_call_get_up_to_limit_generator(compute.list_images, 20, 5, 'response', os.environ.get("OCI_PYSDK_COMPARTMENT_ID"), operating_system='superman fake os'):
        num_iterations += 1
        call_result = response
    assert num_iterations == 1
    assert len(call_result.data) == 0

    num_iterations = 0
    records = []
    for image in oci.pagination.list_call_get_all_results_generator(compute.list_images, 'record', os.environ.get("OCI_PYSDK_COMPARTMENT_ID"), operating_system='superman fake os'):
        num_iterations += 1
        records.append(image)
    assert num_iterations == 0
    assert len(records) == 0

    num_iterations = 0
    records = []
    for image in oci.pagination.list_call_get_up_to_limit_generator(compute.list_images, 20, 5, 'record', os.environ.get("OCI_PYSDK_COMPARTMENT_ID"), operating_system='superman fake os'):
        num_iterations += 1
        records.append(image)
    assert num_iterations == 0
    assert len(records) == 0


def test_pagination_internal_limit_retry_checker():
    checker = oci.pagination.internal.retry_checkers.LimitBasedRetryChecker()
    assert 5 == checker.max_attempts  # Should default to 5

    assert checker.should_retry(current_attempt=1)  # retry if we failed the first attempt
    assert checker.should_retry(current_attempt=4)  # since we have made 4 attempts, we're allowed one more
    assert not checker.should_retry(current_attempt=5)  # we made 5 tries and couldn't do it, no more are allowed

    checker = oci.pagination.internal.retry_checkers.LimitBasedRetryChecker(max_attempts=1)
    assert not checker.should_retry(current_attempt=1)  # we are only allowed 1 attempt, so no more are allowed
    assert not checker.should_retry(current_attempt=5000)


def test_pagination_internal_service_error_checker_timeouts():
    checker = oci.pagination.internal.retry_checkers.TimeoutConnectionAndServiceErrorRetryChecker()
    assert checker.retry_any_5xx
    assert checker.service_error_retry_config == {-1: [], 429: []}

    assert checker.should_retry(exception=Timeout())
    assert checker.should_retry(exception=ConnectionError())
    assert not checker.should_retry(exception=RuntimeError())

    service_error_429 = oci.exceptions.ServiceError(429, 'TooManyRequests', {}, None)
    service_error_500 = oci.exceptions.ServiceError(500, 'SomeCode', {}, None)
    service_error_502 = oci.exceptions.ServiceError(502, 'SomeCode', {}, None)
    assert checker.should_retry(exception=service_error_429)
    assert checker.should_retry(exception=service_error_500)
    assert checker.should_retry(exception=service_error_502)

    checker = oci.pagination.internal.retry_checkers.TimeoutConnectionAndServiceErrorRetryChecker(
        service_error_retry_config={502: [], 429: ['OnlyThisCode']},
        retry_any_5xx=False
    )
    assert not checker.should_retry(exception=service_error_429)
    assert not checker.should_retry(exception=service_error_500)
    assert checker.should_retry(exception=service_error_502)

    service_error_429.code = 'OnlyThisCode'
    assert checker.should_retry(exception=service_error_429)


def test_pagination_internal_checker_container():
    checkers = [
        oci.pagination.internal.retry_checkers.LimitBasedRetryChecker(),
        oci.pagination.internal.retry_checkers.TimeoutConnectionAndServiceErrorRetryChecker()
    ]
    checker_container = oci.pagination.internal.retry_checkers.RetryCheckerContainer(checkers=checkers)

    assert not checker_container.should_retry(exception=ConnectionError(), current_attempt=7)  # limit failed, service error passed
    assert not checker_container.should_retry(exception=RuntimeError(), current_attempt=3)  # limit passed, service error failed
    assert checker_container.should_retry(exception=oci.exceptions.ServiceError(429, 'TooManyRequests', {}, None), current_attempt=1)  # both checks pass
    assert checker_container.should_retry(exception=oci.exceptions.ServiceError(500, 'InternalServerError', {}, None), current_attempt=3)  # both checks pass


def test_pagination_internal_retry_strategy_builder():
    retry_strategy = oci.pagination.internal.retry.RetryStrategyBuilder().add_max_attempts().add_service_error_check().get_retry_strategy()
    retrying_call = MakeRetryingCall(exception_to_throw=RuntimeError(), return_sucess_on_call_number=3)

    with pytest.raises(RuntimeError):
        retry_strategy.make_retrying_call(retrying_call.do_call)
    assert retrying_call.current_calls == 1

    retrying_call.reset()
    retrying_call.exception_to_throw = ConnectionError()
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
