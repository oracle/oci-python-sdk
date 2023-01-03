# Code generated. DO NOT EDIT.
# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
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

        cassette_location = os.path.join('generated', 'bastion_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="team_oci_bastions_us_grp@oracle.com" jiraProject="BSTN" opsJiraProject="Bastions"
def test_change_bastion_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('bastion', 'ChangeBastionCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bastion', util.camelize('bastion'), 'ChangeBastionCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='bastion', api_name='ChangeBastionCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bastion.BastionClient(config, service_endpoint=service_endpoint)
            response = client.change_bastion_compartment(
                bastion_id=request.pop(util.camelize('bastionId')),
                change_bastion_compartment_details=request.pop(util.camelize('ChangeBastionCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bastion',
            'ChangeBastionCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_bastion_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_bastions_us_grp@oracle.com" jiraProject="BSTN" opsJiraProject="Bastions"
def test_create_bastion(testing_service_client):
    if not testing_service_client.is_api_enabled('bastion', 'CreateBastion'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bastion', util.camelize('bastion'), 'CreateBastion')
    )

    request_containers = testing_service_client.get_requests(service_name='bastion', api_name='CreateBastion')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bastion.BastionClient(config, service_endpoint=service_endpoint)
            response = client.create_bastion(
                create_bastion_details=request.pop(util.camelize('CreateBastionDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bastion',
            'CreateBastion',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bastion',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_bastions_us_grp@oracle.com" jiraProject="BSTN" opsJiraProject="Bastions"
def test_create_session(testing_service_client):
    if not testing_service_client.is_api_enabled('bastion', 'CreateSession'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bastion', util.camelize('bastion'), 'CreateSession')
    )

    request_containers = testing_service_client.get_requests(service_name='bastion', api_name='CreateSession')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bastion.BastionClient(config, service_endpoint=service_endpoint)
            response = client.create_session(
                create_session_details=request.pop(util.camelize('CreateSessionDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bastion',
            'CreateSession',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'session',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_bastions_us_grp@oracle.com" jiraProject="BSTN" opsJiraProject="Bastions"
def test_delete_bastion(testing_service_client):
    if not testing_service_client.is_api_enabled('bastion', 'DeleteBastion'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bastion', util.camelize('bastion'), 'DeleteBastion')
    )

    request_containers = testing_service_client.get_requests(service_name='bastion', api_name='DeleteBastion')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bastion.BastionClient(config, service_endpoint=service_endpoint)
            response = client.delete_bastion(
                bastion_id=request.pop(util.camelize('bastionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bastion',
            'DeleteBastion',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_bastion',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_bastions_us_grp@oracle.com" jiraProject="BSTN" opsJiraProject="Bastions"
def test_delete_session(testing_service_client):
    if not testing_service_client.is_api_enabled('bastion', 'DeleteSession'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bastion', util.camelize('bastion'), 'DeleteSession')
    )

    request_containers = testing_service_client.get_requests(service_name='bastion', api_name='DeleteSession')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bastion.BastionClient(config, service_endpoint=service_endpoint)
            response = client.delete_session(
                session_id=request.pop(util.camelize('sessionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bastion',
            'DeleteSession',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_session',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_bastions_us_grp@oracle.com" jiraProject="BSTN" opsJiraProject="Bastions"
def test_get_bastion(testing_service_client):
    if not testing_service_client.is_api_enabled('bastion', 'GetBastion'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bastion', util.camelize('bastion'), 'GetBastion')
    )

    request_containers = testing_service_client.get_requests(service_name='bastion', api_name='GetBastion')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bastion.BastionClient(config, service_endpoint=service_endpoint)
            response = client.get_bastion(
                bastion_id=request.pop(util.camelize('bastionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bastion',
            'GetBastion',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bastion',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_bastions_us_grp@oracle.com" jiraProject="BSTN" opsJiraProject="Bastions"
def test_get_session(testing_service_client):
    if not testing_service_client.is_api_enabled('bastion', 'GetSession'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bastion', util.camelize('bastion'), 'GetSession')
    )

    request_containers = testing_service_client.get_requests(service_name='bastion', api_name='GetSession')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bastion.BastionClient(config, service_endpoint=service_endpoint)
            response = client.get_session(
                session_id=request.pop(util.camelize('sessionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bastion',
            'GetSession',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'session',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_bastions_us_grp@oracle.com" jiraProject="BSTN" opsJiraProject="Bastions"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('bastion', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bastion', util.camelize('bastion'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='bastion', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bastion.BastionClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bastion',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_bastions_us_grp@oracle.com" jiraProject="BSTN" opsJiraProject="Bastions"
def test_list_bastions(testing_service_client):
    if not testing_service_client.is_api_enabled('bastion', 'ListBastions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bastion', util.camelize('bastion'), 'ListBastions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='bastion', api_name='ListBastions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bastion.BastionClient(config, service_endpoint=service_endpoint)
            response = client.list_bastions(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_bastions(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_bastions(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bastion',
            'ListBastions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bastionSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_bastions_us_grp@oracle.com" jiraProject="BSTN" opsJiraProject="Bastions"
def test_list_sessions(testing_service_client):
    if not testing_service_client.is_api_enabled('bastion', 'ListSessions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bastion', util.camelize('bastion'), 'ListSessions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='bastion', api_name='ListSessions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bastion.BastionClient(config, service_endpoint=service_endpoint)
            response = client.list_sessions(
                bastion_id=request.pop(util.camelize('bastionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_sessions(
                    bastion_id=request.pop(util.camelize('bastionId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_sessions(
                        bastion_id=request.pop(util.camelize('bastionId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bastion',
            'ListSessions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sessionSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_bastions_us_grp@oracle.com" jiraProject="BSTN" opsJiraProject="Bastions"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('bastion', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bastion', util.camelize('bastion'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='bastion', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bastion.BastionClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_errors(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_errors(
                    work_request_id=request.pop(util.camelize('workRequestId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_request_errors(
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bastion',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestError',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_bastions_us_grp@oracle.com" jiraProject="BSTN" opsJiraProject="Bastions"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('bastion', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bastion', util.camelize('bastion'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='bastion', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bastion.BastionClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_logs(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_logs(
                    work_request_id=request.pop(util.camelize('workRequestId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_request_logs(
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bastion',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntry',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_bastions_us_grp@oracle.com" jiraProject="BSTN" opsJiraProject="Bastions"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('bastion', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bastion', util.camelize('bastion'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='bastion', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bastion.BastionClient(config, service_endpoint=service_endpoint)
            response = client.list_work_requests(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_requests(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_requests(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bastion',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_bastions_us_grp@oracle.com" jiraProject="BSTN" opsJiraProject="Bastions"
def test_update_bastion(testing_service_client):
    if not testing_service_client.is_api_enabled('bastion', 'UpdateBastion'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bastion', util.camelize('bastion'), 'UpdateBastion')
    )

    request_containers = testing_service_client.get_requests(service_name='bastion', api_name='UpdateBastion')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bastion.BastionClient(config, service_endpoint=service_endpoint)
            response = client.update_bastion(
                bastion_id=request.pop(util.camelize('bastionId')),
                update_bastion_details=request.pop(util.camelize('UpdateBastionDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bastion',
            'UpdateBastion',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_bastion',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_bastions_us_grp@oracle.com" jiraProject="BSTN" opsJiraProject="Bastions"
def test_update_session(testing_service_client):
    if not testing_service_client.is_api_enabled('bastion', 'UpdateSession'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bastion', util.camelize('bastion'), 'UpdateSession')
    )

    request_containers = testing_service_client.get_requests(service_name='bastion', api_name='UpdateSession')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bastion.BastionClient(config, service_endpoint=service_endpoint)
            response = client.update_session(
                session_id=request.pop(util.camelize('sessionId')),
                update_session_details=request.pop(util.camelize('UpdateSessionDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bastion',
            'UpdateSession',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'session',
            False,
            False
        )
