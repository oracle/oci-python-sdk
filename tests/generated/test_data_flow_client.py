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

        cassette_location = os.path.join('generated', 'data_flow_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_change_application_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'ChangeApplicationCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'ChangeApplicationCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='ChangeApplicationCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
            response = client.change_application_compartment(
                application_id=request.pop(util.camelize('applicationId')),
                change_application_compartment_details=request.pop(util.camelize('ChangeApplicationCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_flow',
            'ChangeApplicationCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_application_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_change_private_endpoint_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'ChangePrivateEndpointCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'ChangePrivateEndpointCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='ChangePrivateEndpointCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
            response = client.change_private_endpoint_compartment(
                private_endpoint_id=request.pop(util.camelize('privateEndpointId')),
                change_private_endpoint_compartment_details=request.pop(util.camelize('ChangePrivateEndpointCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_flow',
            'ChangePrivateEndpointCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_private_endpoint_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_change_run_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'ChangeRunCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'ChangeRunCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='ChangeRunCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
            response = client.change_run_compartment(
                run_id=request.pop(util.camelize('runId')),
                change_run_compartment_details=request.pop(util.camelize('ChangeRunCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_flow',
            'ChangeRunCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_run_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_create_application(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'CreateApplication'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'CreateApplication')
    )

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='CreateApplication')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
            response = client.create_application(
                create_application_details=request.pop(util.camelize('CreateApplicationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_flow',
            'CreateApplication',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'application',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_create_private_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'CreatePrivateEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'CreatePrivateEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='CreatePrivateEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
            response = client.create_private_endpoint(
                create_private_endpoint_details=request.pop(util.camelize('CreatePrivateEndpointDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_flow',
            'CreatePrivateEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'privateEndpoint',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_create_run(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'CreateRun'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'CreateRun')
    )

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='CreateRun')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
            response = client.create_run(
                create_run_details=request.pop(util.camelize('CreateRunDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_flow',
            'CreateRun',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'run',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_create_statement(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'CreateStatement'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'CreateStatement')
    )

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='CreateStatement')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
            response = client.create_statement(
                create_statement_details=request.pop(util.camelize('CreateStatementDetails')),
                run_id=request.pop(util.camelize('runId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_flow',
            'CreateStatement',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'statement',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_delete_application(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'DeleteApplication'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'DeleteApplication')
    )

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='DeleteApplication')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
            response = client.delete_application(
                application_id=request.pop(util.camelize('applicationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_flow',
            'DeleteApplication',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_application',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_delete_private_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'DeletePrivateEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'DeletePrivateEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='DeletePrivateEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
            response = client.delete_private_endpoint(
                private_endpoint_id=request.pop(util.camelize('privateEndpointId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_flow',
            'DeletePrivateEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_private_endpoint',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_delete_run(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'DeleteRun'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'DeleteRun')
    )

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='DeleteRun')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
            response = client.delete_run(
                run_id=request.pop(util.camelize('runId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_flow',
            'DeleteRun',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_run',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_delete_statement(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'DeleteStatement'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'DeleteStatement')
    )

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='DeleteStatement')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
            response = client.delete_statement(
                run_id=request.pop(util.camelize('runId')),
                statement_id=request.pop(util.camelize('statementId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_flow',
            'DeleteStatement',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_statement',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_get_application(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'GetApplication'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'GetApplication')
    )

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='GetApplication')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
            response = client.get_application(
                application_id=request.pop(util.camelize('applicationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_flow',
            'GetApplication',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'application',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_get_private_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'GetPrivateEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'GetPrivateEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='GetPrivateEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
            response = client.get_private_endpoint(
                private_endpoint_id=request.pop(util.camelize('privateEndpointId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_flow',
            'GetPrivateEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'privateEndpoint',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_get_run(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'GetRun'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'GetRun')
    )

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='GetRun')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
            response = client.get_run(
                run_id=request.pop(util.camelize('runId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_flow',
            'GetRun',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'run',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_get_run_log(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'GetRunLog'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'GetRunLog')
    )

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='GetRunLog')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
            response = client.get_run_log(
                run_id=request.pop(util.camelize('runId')),
                name=request.pop(util.camelize('name')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_flow',
            'GetRunLog',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_get_statement(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'GetStatement'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'GetStatement')
    )

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='GetStatement')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
            response = client.get_statement(
                run_id=request.pop(util.camelize('runId')),
                statement_id=request.pop(util.camelize('statementId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_flow',
            'GetStatement',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'statement',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_flow',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_list_applications(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'ListApplications'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'ListApplications')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='ListApplications')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
            response = client.list_applications(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_applications(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_applications(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_flow',
            'ListApplications',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'applicationSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_list_private_endpoints(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'ListPrivateEndpoints'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'ListPrivateEndpoints')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='ListPrivateEndpoints')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
            response = client.list_private_endpoints(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_private_endpoints(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_private_endpoints(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_flow',
            'ListPrivateEndpoints',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'privateEndpointCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_list_run_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'ListRunLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'ListRunLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='ListRunLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
            response = client.list_run_logs(
                run_id=request.pop(util.camelize('runId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_run_logs(
                    run_id=request.pop(util.camelize('runId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_run_logs(
                        run_id=request.pop(util.camelize('runId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_flow',
            'ListRunLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'runLogSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_list_runs(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'ListRuns'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'ListRuns')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='ListRuns')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
            response = client.list_runs(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_runs(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_runs(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_flow',
            'ListRuns',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'runSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_list_statements(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'ListStatements'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'ListStatements')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='ListStatements')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
            response = client.list_statements(
                run_id=request.pop(util.camelize('runId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_statements(
                    run_id=request.pop(util.camelize('runId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_statements(
                        run_id=request.pop(util.camelize('runId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_flow',
            'ListStatements',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'statementCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
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
            'data_flow',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestErrorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
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
            'data_flow',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
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
            'data_flow',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_update_application(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'UpdateApplication'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'UpdateApplication')
    )

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='UpdateApplication')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
            response = client.update_application(
                update_application_details=request.pop(util.camelize('UpdateApplicationDetails')),
                application_id=request.pop(util.camelize('applicationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_flow',
            'UpdateApplication',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'application',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_update_private_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'UpdatePrivateEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'UpdatePrivateEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='UpdatePrivateEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
            response = client.update_private_endpoint(
                update_private_endpoint_details=request.pop(util.camelize('UpdatePrivateEndpointDetails')),
                private_endpoint_id=request.pop(util.camelize('privateEndpointId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_flow',
            'UpdatePrivateEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_private_endpoint',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_update_run(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'UpdateRun'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'UpdateRun')
    )

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='UpdateRun')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
            response = client.update_run(
                update_run_details=request.pop(util.camelize('UpdateRunDetails')),
                run_id=request.pop(util.camelize('runId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_flow',
            'UpdateRun',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'run',
            False,
            False
        )
