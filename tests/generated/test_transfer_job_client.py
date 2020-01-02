# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

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
def test_change_transfer_job_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('dts', 'ChangeTransferJobCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dts', util.camelize('transfer_job'), 'ChangeTransferJobCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='dts', api_name='ChangeTransferJobCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dts.TransferJobClient(config, service_endpoint=service_endpoint)
            response = client.change_transfer_job_compartment(
                transfer_job_id=request.pop(util.camelize('transfer_job_id')),
                change_transfer_job_compartment_details=request.pop(util.camelize('change_transfer_job_compartment_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dts',
            'ChangeTransferJobCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_transfer_job_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="data_transfer_platform_dev_ww_grp@oracle.com" jiraProject="BDTS" opsJiraProject="DTS"
def test_create_transfer_job(testing_service_client):
    if not testing_service_client.is_api_enabled('dts', 'CreateTransferJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dts', util.camelize('transfer_job'), 'CreateTransferJob')
    )

    request_containers = testing_service_client.get_requests(service_name='dts', api_name='CreateTransferJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dts.TransferJobClient(config, service_endpoint=service_endpoint)
            response = client.create_transfer_job(
                create_transfer_job_details=request.pop(util.camelize('create_transfer_job_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dts',
            'CreateTransferJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'transferJob',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="data_transfer_platform_dev_ww_grp@oracle.com" jiraProject="BDTS" opsJiraProject="DTS"
def test_delete_transfer_job(testing_service_client):
    if not testing_service_client.is_api_enabled('dts', 'DeleteTransferJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dts', util.camelize('transfer_job'), 'DeleteTransferJob')
    )

    request_containers = testing_service_client.get_requests(service_name='dts', api_name='DeleteTransferJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dts.TransferJobClient(config, service_endpoint=service_endpoint)
            response = client.delete_transfer_job(
                id=request.pop(util.camelize('id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dts',
            'DeleteTransferJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_transfer_job',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="data_transfer_platform_dev_ww_grp@oracle.com" jiraProject="BDTS" opsJiraProject="DTS"
def test_get_transfer_job(testing_service_client):
    if not testing_service_client.is_api_enabled('dts', 'GetTransferJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dts', util.camelize('transfer_job'), 'GetTransferJob')
    )

    request_containers = testing_service_client.get_requests(service_name='dts', api_name='GetTransferJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dts.TransferJobClient(config, service_endpoint=service_endpoint)
            response = client.get_transfer_job(
                id=request.pop(util.camelize('id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dts',
            'GetTransferJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'transferJob',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="data_transfer_platform_dev_ww_grp@oracle.com" jiraProject="BDTS" opsJiraProject="DTS"
def test_list_transfer_jobs(testing_service_client):
    if not testing_service_client.is_api_enabled('dts', 'ListTransferJobs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dts', util.camelize('transfer_job'), 'ListTransferJobs')
    )

    request_containers = testing_service_client.get_requests(service_name='dts', api_name='ListTransferJobs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dts.TransferJobClient(config, service_endpoint=service_endpoint)
            response = client.list_transfer_jobs(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dts',
            'ListTransferJobs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'transferJobSummary',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="data_transfer_platform_dev_ww_grp@oracle.com" jiraProject="BDTS" opsJiraProject="DTS"
def test_update_transfer_job(testing_service_client):
    if not testing_service_client.is_api_enabled('dts', 'UpdateTransferJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dts', util.camelize('transfer_job'), 'UpdateTransferJob')
    )

    request_containers = testing_service_client.get_requests(service_name='dts', api_name='UpdateTransferJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dts.TransferJobClient(config, service_endpoint=service_endpoint)
            response = client.update_transfer_job(
                id=request.pop(util.camelize('id')),
                update_transfer_job_details=request.pop(util.camelize('update_transfer_job_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dts',
            'UpdateTransferJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'transferJob',
            False,
            False
        )
