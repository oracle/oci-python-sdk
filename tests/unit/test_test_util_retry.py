# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

try:
    import unittest.mock as mock
except ImportError:
    import mock

import oci
import pytest
import tests.util

from oci._vendor.requests.exceptions import Timeout
from oci._vendor.requests.exceptions import ConnectionError


def test_retry_on_timeouts():
    mock_client = create_mock_client([Timeout(), Timeout(), Timeout()])

    with pytest.raises(Timeout):
        # Decorate and then call the method
        tests.util.simple_retries_decorator(mock_client.mock_method)()

    assert mock_client.mock_method.call_count == 3


def test_retry_on_connetion_errors():
    mock_client = create_mock_client([ConnectionError(), ConnectionError(), ConnectionError()])

    with pytest.raises(ConnectionError):
        tests.util.simple_retries_decorator(mock_client.mock_method)()

    assert mock_client.mock_method.call_count == 3


def test_retry_on_500s():
    mock_client = create_mock_client([
        oci.exceptions.ServiceError(500, "blah", {}, "blah"),
        oci.exceptions.ServiceError(501, "blah", {}, "blah"),
        oci.exceptions.ServiceError(502, "blah", {}, "blah")
    ])

    with pytest.raises(oci.exceptions.ServiceError) as service_error_info:
        tests.util.simple_retries_decorator(mock_client.mock_method)()

    assert mock_client.mock_method.call_count == 3
    assert service_error_info.value.status == 502  # We should throw out the last exception


def test_retry_on_throttles():
    mock_client = create_mock_client([
        oci.exceptions.ServiceError(429, "blah", {}, "blah"),
        oci.exceptions.ServiceError(429, "blah", {}, "blah"),
        oci.exceptions.ServiceError(429, "blah", {}, "blah")
    ])

    with pytest.raises(oci.exceptions.ServiceError) as service_error_info:
        tests.util.simple_retries_decorator(mock_client.mock_method)()

    assert mock_client.mock_method.call_count == 3
    assert service_error_info.value.status == 429


def test_retry_on_conflicts():
    mock_client = create_mock_client([
        oci.exceptions.ServiceError(409, "Conflict", {}, "blah"),
        oci.exceptions.ServiceError(409, "Conflict", {}, "blah"),
        oci.exceptions.ServiceError(409, "Conflict", {}, "blah")
    ])

    with pytest.raises(oci.exceptions.ServiceError) as service_error_info:
        tests.util.simple_retries_decorator(mock_client.mock_method)()

    assert mock_client.mock_method.call_count == 3
    assert service_error_info.value.status == 409
    assert service_error_info.value.code == "Conflict"


def test_no_retry_on_random_exception():
    mock_client = create_mock_client([RuntimeError(), Timeout()])

    with pytest.raises(RuntimeError):
        tests.util.simple_retries_decorator(mock_client.mock_method)()

    assert mock_client.mock_method.call_count == 1


def test_no_retry_on_non_conflict_409s():
    mock_client = create_mock_client([
        oci.exceptions.ServiceError(409, "NoRetry", {}, "blah"),
        oci.exceptions.ServiceError(409, "NoRetry2", {}, "blah"),
        oci.exceptions.ServiceError(409, "NoRetry3", {}, "blah")
    ])

    with pytest.raises(oci.exceptions.ServiceError) as service_error_info:
        tests.util.simple_retries_decorator(mock_client.mock_method)()

    assert mock_client.mock_method.call_count == 1
    assert service_error_info.value.status == 409
    assert service_error_info.value.code == "NoRetry"


def test_no_retry_on_400s():
    mock_client = create_mock_client([
        oci.exceptions.ServiceError(400, "NoRetry", {}, "blah"),
        oci.exceptions.ServiceError(400, "NoRetry2", {}, "blah"),
        oci.exceptions.ServiceError(400, "NoRetry3", {}, "blah")
    ])

    with pytest.raises(oci.exceptions.ServiceError) as service_error_info:
        tests.util.simple_retries_decorator(mock_client.mock_method)()

    assert mock_client.mock_method.call_count == 1
    assert service_error_info.value.status == 400
    assert service_error_info.value.code == "NoRetry"


def create_mock_client(side_effect):
    mock_client = mock.Mock()
    mock_client.mock_method = mock.Mock()
    mock_client.mock_method.__name__ = "mock_method"
    mock_client.mock_method.side_effect = side_effect

    return mock_client
