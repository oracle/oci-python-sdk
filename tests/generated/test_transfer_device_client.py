# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import pytest
from .. import test_config_container  # noqa: F401
from .. import util
import oci
import oci.exceptions as oci_exception
import os


def session_agnostic_query_matcher(r1, r2):
    r1_query = [x for x in r1.query if x[0] != 'sessionId']
    r2_query = [x for x in r2.query if x[0] != 'sessionId']
    return r1_query == r2_query


@pytest.fixture(autouse=True, scope='function')
def vcr_fixture(request):
    # use the default matching logic (link below) with the exception of 'session_agnostic_query_matcher'
    # instead of 'query' matcher (which ignores sessionId in the url)
    # https://vcrpy.readthedocs.io/en/latest/configuration.html#request-matching
    custom_vcr = test_config_container.create_vcr()
    custom_vcr.register_matcher('session_agnostic_query_matcher', session_agnostic_query_matcher)

    cassette_location = os.path.join('generated', 'dts_{name}.yml'.format(name=request.function.__name__))
    with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
        yield


# IssueRoutingInfo tag="default" email="data_transfer_platform_dev_ww_grp@oracle.com" jiraProject="DTS" opsJiraProject="NONE"
def test_create_transfer_device(testing_service_client):
    if not testing_service_client.is_api_enabled('dts', 'CreateTransferDevice'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dts', util.camelize('transfer_device'), 'CreateTransferDevice')
    )

    request_containers = testing_service_client.get_requests(service_name='dts', api_name='CreateTransferDevice')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dts.TransferDeviceClient(config, service_endpoint=service_endpoint)
            response = client.create_transfer_device(
                id=request.pop(util.camelize('id')),
                create_transfer_device_details=request.pop(util.camelize('create_transfer_device_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dts',
            'CreateTransferDevice',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'newTransferDevice',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="data_transfer_platform_dev_ww_grp@oracle.com" jiraProject="DTS" opsJiraProject="NONE"
def test_delete_transfer_device(testing_service_client):
    if not testing_service_client.is_api_enabled('dts', 'DeleteTransferDevice'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dts', util.camelize('transfer_device'), 'DeleteTransferDevice')
    )

    request_containers = testing_service_client.get_requests(service_name='dts', api_name='DeleteTransferDevice')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dts.TransferDeviceClient(config, service_endpoint=service_endpoint)
            response = client.delete_transfer_device(
                id=request.pop(util.camelize('id')),
                transfer_device_label=request.pop(util.camelize('transfer_device_label')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dts',
            'DeleteTransferDevice',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_transfer_device',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="data_transfer_platform_dev_ww_grp@oracle.com" jiraProject="DTS" opsJiraProject="NONE"
def test_get_transfer_device(testing_service_client):
    if not testing_service_client.is_api_enabled('dts', 'GetTransferDevice'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dts', util.camelize('transfer_device'), 'GetTransferDevice')
    )

    request_containers = testing_service_client.get_requests(service_name='dts', api_name='GetTransferDevice')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dts.TransferDeviceClient(config, service_endpoint=service_endpoint)
            response = client.get_transfer_device(
                id=request.pop(util.camelize('id')),
                transfer_device_label=request.pop(util.camelize('transfer_device_label')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dts',
            'GetTransferDevice',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'transferDevice',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="data_transfer_platform_dev_ww_grp@oracle.com" jiraProject="DTS" opsJiraProject="NONE"
def test_list_transfer_devices(testing_service_client):
    if not testing_service_client.is_api_enabled('dts', 'ListTransferDevices'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dts', util.camelize('transfer_device'), 'ListTransferDevices')
    )

    request_containers = testing_service_client.get_requests(service_name='dts', api_name='ListTransferDevices')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dts.TransferDeviceClient(config, service_endpoint=service_endpoint)
            response = client.list_transfer_devices(
                id=request.pop(util.camelize('id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dts',
            'ListTransferDevices',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'multipleTransferDevices',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="data_transfer_platform_dev_ww_grp@oracle.com" jiraProject="DTS" opsJiraProject="NONE"
def test_update_transfer_device(testing_service_client):
    if not testing_service_client.is_api_enabled('dts', 'UpdateTransferDevice'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dts', util.camelize('transfer_device'), 'UpdateTransferDevice')
    )

    request_containers = testing_service_client.get_requests(service_name='dts', api_name='UpdateTransferDevice')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dts.TransferDeviceClient(config, service_endpoint=service_endpoint)
            response = client.update_transfer_device(
                id=request.pop(util.camelize('id')),
                transfer_device_label=request.pop(util.camelize('transfer_device_label')),
                update_transfer_device_details=request.pop(util.camelize('update_transfer_device_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dts',
            'UpdateTransferDevice',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'transferDevice',
            False,
            False
        )
