# Code generated. DO NOT EDIT.
# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

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
    if test_config_container.test_mode == 'mock':
        yield
    else:
        # use the default matching logic (link below) with the exception of 'session_agnostic_query_matcher'
        # instead of 'query' matcher (which ignores sessionId in the url)
        # https://vcrpy.readthedocs.io/en/latest/configuration.html#request-matching
        custom_vcr = test_config_container.create_vcr()
        custom_vcr.register_matcher('session_agnostic_query_matcher', session_agnostic_query_matcher)

        cassette_location = os.path.join('generated', 'apm_control_plane_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="apm-control-plane-dev_grp@oracle.com" jiraProject="APM" opsJiraProject="APMSDC"
def test_change_apm_domain_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('apm_control_plane', 'ChangeApmDomainCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apm_control_plane', util.camelize('apm_domain'), 'ChangeApmDomainCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='apm_control_plane', api_name='ChangeApmDomainCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apm_control_plane.ApmDomainClient(config, service_endpoint=service_endpoint)
            response = client.change_apm_domain_compartment(
                apm_domain_id=request.pop(util.camelize('apmDomainId')),
                change_apm_domain_compartment_details=request.pop(util.camelize('ChangeApmDomainCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apm_control_plane',
            'ChangeApmDomainCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_apm_domain_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="apm-control-plane-dev_grp@oracle.com" jiraProject="APM" opsJiraProject="APMSDC"
def test_create_apm_domain(testing_service_client):
    if not testing_service_client.is_api_enabled('apm_control_plane', 'CreateApmDomain'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apm_control_plane', util.camelize('apm_domain'), 'CreateApmDomain')
    )

    request_containers = testing_service_client.get_requests(service_name='apm_control_plane', api_name='CreateApmDomain')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apm_control_plane.ApmDomainClient(config, service_endpoint=service_endpoint)
            response = client.create_apm_domain(
                create_apm_domain_details=request.pop(util.camelize('CreateApmDomainDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apm_control_plane',
            'CreateApmDomain',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_apm_domain',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="apm-control-plane-dev_grp@oracle.com" jiraProject="APM" opsJiraProject="APMSDC"
def test_delete_apm_domain(testing_service_client):
    if not testing_service_client.is_api_enabled('apm_control_plane', 'DeleteApmDomain'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apm_control_plane', util.camelize('apm_domain'), 'DeleteApmDomain')
    )

    request_containers = testing_service_client.get_requests(service_name='apm_control_plane', api_name='DeleteApmDomain')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apm_control_plane.ApmDomainClient(config, service_endpoint=service_endpoint)
            response = client.delete_apm_domain(
                apm_domain_id=request.pop(util.camelize('apmDomainId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apm_control_plane',
            'DeleteApmDomain',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_apm_domain',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="apm-control-plane-dev_grp@oracle.com" jiraProject="APM" opsJiraProject="APMSDC"
def test_generate_data_keys(testing_service_client):
    if not testing_service_client.is_api_enabled('apm_control_plane', 'GenerateDataKeys'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apm_control_plane', util.camelize('apm_domain'), 'GenerateDataKeys')
    )

    request_containers = testing_service_client.get_requests(service_name='apm_control_plane', api_name='GenerateDataKeys')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apm_control_plane.ApmDomainClient(config, service_endpoint=service_endpoint)
            response = client.generate_data_keys(
                generate_data_keys_list_details=request.pop(util.camelize('GenerateDataKeysListDetails')),
                apm_domain_id=request.pop(util.camelize('apmDomainId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apm_control_plane',
            'GenerateDataKeys',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'generate_data_keys',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="apm-control-plane-dev_grp@oracle.com" jiraProject="APM" opsJiraProject="APMSDC"
def test_get_apm_domain(testing_service_client):
    if not testing_service_client.is_api_enabled('apm_control_plane', 'GetApmDomain'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apm_control_plane', util.camelize('apm_domain'), 'GetApmDomain')
    )

    request_containers = testing_service_client.get_requests(service_name='apm_control_plane', api_name='GetApmDomain')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apm_control_plane.ApmDomainClient(config, service_endpoint=service_endpoint)
            response = client.get_apm_domain(
                apm_domain_id=request.pop(util.camelize('apmDomainId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apm_control_plane',
            'GetApmDomain',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'apmDomain',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="apm-control-plane-dev_grp@oracle.com" jiraProject="APM" opsJiraProject="APMSDC"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('apm_control_plane', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apm_control_plane', util.camelize('apm_domain'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='apm_control_plane', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apm_control_plane.ApmDomainClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apm_control_plane',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="apm-control-plane-dev_grp@oracle.com" jiraProject="APM" opsJiraProject="APMSDC"
def test_list_apm_domain_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('apm_control_plane', 'ListApmDomainWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apm_control_plane', util.camelize('apm_domain'), 'ListApmDomainWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='apm_control_plane', api_name='ListApmDomainWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apm_control_plane.ApmDomainClient(config, service_endpoint=service_endpoint)
            response = client.list_apm_domain_work_requests(
                apm_domain_id=request.pop(util.camelize('apmDomainId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_apm_domain_work_requests(
                    apm_domain_id=request.pop(util.camelize('apmDomainId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_apm_domain_work_requests(
                        apm_domain_id=request.pop(util.camelize('apmDomainId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apm_control_plane',
            'ListApmDomainWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="apm-control-plane-dev_grp@oracle.com" jiraProject="APM" opsJiraProject="APMSDC"
def test_list_apm_domains(testing_service_client):
    if not testing_service_client.is_api_enabled('apm_control_plane', 'ListApmDomains'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apm_control_plane', util.camelize('apm_domain'), 'ListApmDomains')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='apm_control_plane', api_name='ListApmDomains')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apm_control_plane.ApmDomainClient(config, service_endpoint=service_endpoint)
            response = client.list_apm_domains(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_apm_domains(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_apm_domains(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apm_control_plane',
            'ListApmDomains',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'apmDomainSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="apm-control-plane-dev_grp@oracle.com" jiraProject="APM" opsJiraProject="APMSDC"
def test_list_data_keys(testing_service_client):
    if not testing_service_client.is_api_enabled('apm_control_plane', 'ListDataKeys'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apm_control_plane', util.camelize('apm_domain'), 'ListDataKeys')
    )

    request_containers = testing_service_client.get_requests(service_name='apm_control_plane', api_name='ListDataKeys')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apm_control_plane.ApmDomainClient(config, service_endpoint=service_endpoint)
            response = client.list_data_keys(
                apm_domain_id=request.pop(util.camelize('apmDomainId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apm_control_plane',
            'ListDataKeys',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataKeySummary',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="apm-control-plane-dev_grp@oracle.com" jiraProject="APM" opsJiraProject="APMSDC"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('apm_control_plane', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apm_control_plane', util.camelize('apm_domain'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='apm_control_plane', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apm_control_plane.ApmDomainClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_errors(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_errors(
                    work_request_id=request.pop(util.camelize('workRequestId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_request_errors(
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apm_control_plane',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestError',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="apm-control-plane-dev_grp@oracle.com" jiraProject="APM" opsJiraProject="APMSDC"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('apm_control_plane', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apm_control_plane', util.camelize('apm_domain'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='apm_control_plane', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apm_control_plane.ApmDomainClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_logs(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_logs(
                    work_request_id=request.pop(util.camelize('workRequestId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_request_logs(
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apm_control_plane',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntry',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="apm-control-plane-dev_grp@oracle.com" jiraProject="APM" opsJiraProject="APMSDC"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('apm_control_plane', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apm_control_plane', util.camelize('apm_domain'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='apm_control_plane', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apm_control_plane.ApmDomainClient(config, service_endpoint=service_endpoint)
            response = client.list_work_requests(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_requests(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_requests(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apm_control_plane',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="apm-control-plane-dev_grp@oracle.com" jiraProject="APM" opsJiraProject="APMSDC"
def test_remove_data_keys(testing_service_client):
    if not testing_service_client.is_api_enabled('apm_control_plane', 'RemoveDataKeys'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apm_control_plane', util.camelize('apm_domain'), 'RemoveDataKeys')
    )

    request_containers = testing_service_client.get_requests(service_name='apm_control_plane', api_name='RemoveDataKeys')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apm_control_plane.ApmDomainClient(config, service_endpoint=service_endpoint)
            response = client.remove_data_keys(
                apm_domain_id=request.pop(util.camelize('apmDomainId')),
                remove_data_keys_list_details=request.pop(util.camelize('RemoveDataKeysListDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apm_control_plane',
            'RemoveDataKeys',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'remove_data_keys',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="apm-control-plane-dev_grp@oracle.com" jiraProject="APM" opsJiraProject="APMSDC"
def test_update_apm_domain(testing_service_client):
    if not testing_service_client.is_api_enabled('apm_control_plane', 'UpdateApmDomain'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apm_control_plane', util.camelize('apm_domain'), 'UpdateApmDomain')
    )

    request_containers = testing_service_client.get_requests(service_name='apm_control_plane', api_name='UpdateApmDomain')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apm_control_plane.ApmDomainClient(config, service_endpoint=service_endpoint)
            response = client.update_apm_domain(
                apm_domain_id=request.pop(util.camelize('apmDomainId')),
                update_apm_domain_details=request.pop(util.camelize('UpdateApmDomainDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apm_control_plane',
            'UpdateApmDomain',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_apm_domain',
            False,
            False
        )
