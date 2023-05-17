# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci
import logging
import pytest
from oci.request import Request
from oci.response import Response
from oci.exceptions import ServiceError


def test_composite_operation(caplog):
    mock_request = Request("GET", "https://blahblah.com")
    mock_response_data = MockResponseData("BLAH")
    mock_response = Response("402", {}, mock_response_data, mock_request)
    mock_404_service_error = ServiceError(404, "blah", {}, "blah")

    # Scenario 1: User sends in succeed_on_not_found as True
    mock_client_1 = MockClient(mock_404_service_error)
    mock_composite_client_1 = MockCompositeClient(mock_client_1)
    waiter_kwargs_1 = {"succeed_on_not_found": True}
    result1 = mock_composite_client_1.delete_composite_operation(mock_response, waiter_kwargs_1)
    assert result1 == oci.waiter.WAIT_RESOURCE_NOT_FOUND

    # Scenario 2: User sends in succeed_on_not_found as False
    with pytest.raises(ServiceError):
        mock_client_2 = MockClient(mock_404_service_error)
        mock_composite_client_2 = MockCompositeClient(mock_client_2)
        waiter_kwargs_2 = {"succeed_on_not_found": False}
        mock_composite_client_2.delete_composite_operation(mock_response, waiter_kwargs_2)
    assert "succeed_on_not_found was passed as False" in caplog.text

    # Scenario 3: User does not send in succeed_on_not_found in waiter_kwargs
    mock_client_3 = MockClient(mock_404_service_error)
    mock_composite_client_3 = MockCompositeClient(mock_client_3)
    waiter_kwargs_3 = {}
    result3 = mock_composite_client_3.delete_composite_operation(mock_response, waiter_kwargs_3)
    assert result3 == oci.waiter.WAIT_RESOURCE_NOT_FOUND


class MockResponseData:

    def __init__(self, val):
        self.val = val


class MockBaseClient:

    def __init__(self, service_error):
        self.logger = logging.getLogger("{}.{}".format(__name__, id(self)))
        self.logger.addHandler(logging.NullHandler())
        self.service_error = service_error

    def request(self, request):
        raise self.service_error


class MockClient:

    def __init__(self, service_error):
        self.base_client = MockBaseClient(service_error)


class MockCompositeClient:

    def __init__(self, client):
        self.client = client

    def delete_composite_operation(self, response, waiter_kwargs={}):
        if ("succeed_on_not_found" in waiter_kwargs) and (waiter_kwargs["succeed_on_not_found"] is False):
            self.client.base_client.logger.warning("The waiter kwarg succeed_on_not_found was passed as False for the delete composite, this would result in the operation to fail if the resource is not found! Please, do not pass this kwarg if this was not intended")
        else:
            """
            If the user does not send in this value, we set it to True by default.
            We are doing this because during a delete resource scenario and waiting on its state, the service can
            return a 404 NOT FOUND exception as the resource was deleted and a get on its state would fail
            """
            waiter_kwargs["succeed_on_not_found"] = True
        waiter_result = oci.wait_until(self.client, response, "val", "blah", **waiter_kwargs)
        result_to_return = waiter_result
        return result_to_return
