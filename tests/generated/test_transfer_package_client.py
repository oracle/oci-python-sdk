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


# IssueRoutingInfo tag="default" email="data_transfer_platform_dev_ww_grp@oracle.com" jiraProject="BDTS" opsJiraProject="DTS"
def test_attach_devices_to_transfer_package(testing_service_client):
    if not testing_service_client.is_api_enabled('dts', 'AttachDevicesToTransferPackage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dts', util.camelize('transfer_package'), 'AttachDevicesToTransferPackage')
    )

    request_containers = testing_service_client.get_requests(service_name='dts', api_name='AttachDevicesToTransferPackage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dts.TransferPackageClient(config, service_endpoint=service_endpoint)
            response = client.attach_devices_to_transfer_package(
                id=request.pop(util.camelize('id')),
                transfer_package_label=request.pop(util.camelize('transfer_package_label')),
                attach_devices_details=request.pop(util.camelize('attach_devices_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dts',
            'AttachDevicesToTransferPackage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'attach_devices_to_transfer_package',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="data_transfer_platform_dev_ww_grp@oracle.com" jiraProject="BDTS" opsJiraProject="DTS"
def test_create_transfer_package(testing_service_client):
    if not testing_service_client.is_api_enabled('dts', 'CreateTransferPackage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dts', util.camelize('transfer_package'), 'CreateTransferPackage')
    )

    request_containers = testing_service_client.get_requests(service_name='dts', api_name='CreateTransferPackage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dts.TransferPackageClient(config, service_endpoint=service_endpoint)
            response = client.create_transfer_package(
                id=request.pop(util.camelize('id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dts',
            'CreateTransferPackage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'transferPackage',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="data_transfer_platform_dev_ww_grp@oracle.com" jiraProject="BDTS" opsJiraProject="DTS"
def test_delete_transfer_package(testing_service_client):
    if not testing_service_client.is_api_enabled('dts', 'DeleteTransferPackage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dts', util.camelize('transfer_package'), 'DeleteTransferPackage')
    )

    request_containers = testing_service_client.get_requests(service_name='dts', api_name='DeleteTransferPackage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dts.TransferPackageClient(config, service_endpoint=service_endpoint)
            response = client.delete_transfer_package(
                id=request.pop(util.camelize('id')),
                transfer_package_label=request.pop(util.camelize('transfer_package_label')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dts',
            'DeleteTransferPackage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_transfer_package',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="data_transfer_platform_dev_ww_grp@oracle.com" jiraProject="BDTS" opsJiraProject="DTS"
def test_detach_devices_from_transfer_package(testing_service_client):
    if not testing_service_client.is_api_enabled('dts', 'DetachDevicesFromTransferPackage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dts', util.camelize('transfer_package'), 'DetachDevicesFromTransferPackage')
    )

    request_containers = testing_service_client.get_requests(service_name='dts', api_name='DetachDevicesFromTransferPackage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dts.TransferPackageClient(config, service_endpoint=service_endpoint)
            response = client.detach_devices_from_transfer_package(
                id=request.pop(util.camelize('id')),
                transfer_package_label=request.pop(util.camelize('transfer_package_label')),
                detach_devices_details=request.pop(util.camelize('detach_devices_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dts',
            'DetachDevicesFromTransferPackage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'detach_devices_from_transfer_package',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="data_transfer_platform_dev_ww_grp@oracle.com" jiraProject="BDTS" opsJiraProject="DTS"
def test_get_transfer_package(testing_service_client):
    if not testing_service_client.is_api_enabled('dts', 'GetTransferPackage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dts', util.camelize('transfer_package'), 'GetTransferPackage')
    )

    request_containers = testing_service_client.get_requests(service_name='dts', api_name='GetTransferPackage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dts.TransferPackageClient(config, service_endpoint=service_endpoint)
            response = client.get_transfer_package(
                id=request.pop(util.camelize('id')),
                transfer_package_label=request.pop(util.camelize('transfer_package_label')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dts',
            'GetTransferPackage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'transferPackage',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="data_transfer_platform_dev_ww_grp@oracle.com" jiraProject="BDTS" opsJiraProject="DTS"
def test_list_transfer_packages(testing_service_client):
    if not testing_service_client.is_api_enabled('dts', 'ListTransferPackages'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dts', util.camelize('transfer_package'), 'ListTransferPackages')
    )

    request_containers = testing_service_client.get_requests(service_name='dts', api_name='ListTransferPackages')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dts.TransferPackageClient(config, service_endpoint=service_endpoint)
            response = client.list_transfer_packages(
                id=request.pop(util.camelize('id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dts',
            'ListTransferPackages',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'multipleTransferPackages',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="data_transfer_platform_dev_ww_grp@oracle.com" jiraProject="BDTS" opsJiraProject="DTS"
def test_update_transfer_package(testing_service_client):
    if not testing_service_client.is_api_enabled('dts', 'UpdateTransferPackage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dts', util.camelize('transfer_package'), 'UpdateTransferPackage')
    )

    request_containers = testing_service_client.get_requests(service_name='dts', api_name='UpdateTransferPackage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dts.TransferPackageClient(config, service_endpoint=service_endpoint)
            response = client.update_transfer_package(
                id=request.pop(util.camelize('id')),
                transfer_package_label=request.pop(util.camelize('transfer_package_label')),
                update_transfer_package_details=request.pop(util.camelize('update_transfer_package_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dts',
            'UpdateTransferPackage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'transferPackage',
            False,
            False
        )
