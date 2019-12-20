# Code generated. DO NOT EDIT.
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
    if test_config_container.test_mode == 'mock':
        yield
    else:
        # use the default matching logic (link below) with the exception of 'session_agnostic_query_matcher'
        # instead of 'query' matcher (which ignores sessionId in the url)
        # https://vcrpy.readthedocs.io/en/latest/configuration.html#request-matching
        custom_vcr = test_config_container.create_vcr()
        custom_vcr.register_matcher('session_agnostic_query_matcher', session_agnostic_query_matcher)

        cassette_location = os.path.join('generated', 'functions_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="serverless_grp@oracle.com" jiraProject="FAAS" opsJiraProject="FAAS"
def test_change_application_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('functions', 'ChangeApplicationCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('functions', util.camelize('functions_management'), 'ChangeApplicationCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='functions', api_name='ChangeApplicationCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.functions.FunctionsManagementClient(config, service_endpoint=service_endpoint)
            response = client.change_application_compartment(
                application_id=request.pop(util.camelize('applicationId')),
                change_application_compartment_details=request.pop(util.camelize('ChangeApplicationCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'functions',
            'ChangeApplicationCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_application_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="serverless_grp@oracle.com" jiraProject="FAAS" opsJiraProject="FAAS"
def test_create_application(testing_service_client):
    if not testing_service_client.is_api_enabled('functions', 'CreateApplication'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('functions', util.camelize('functions_management'), 'CreateApplication')
    )

    request_containers = testing_service_client.get_requests(service_name='functions', api_name='CreateApplication')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.functions.FunctionsManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_application(
                create_application_details=request.pop(util.camelize('CreateApplicationDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'functions',
            'CreateApplication',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'application',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="serverless_grp@oracle.com" jiraProject="FAAS" opsJiraProject="FAAS"
def test_create_function(testing_service_client):
    if not testing_service_client.is_api_enabled('functions', 'CreateFunction'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('functions', util.camelize('functions_management'), 'CreateFunction')
    )

    request_containers = testing_service_client.get_requests(service_name='functions', api_name='CreateFunction')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.functions.FunctionsManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_function(
                create_function_details=request.pop(util.camelize('CreateFunctionDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'functions',
            'CreateFunction',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'function',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="serverless_grp@oracle.com" jiraProject="FAAS" opsJiraProject="FAAS"
def test_delete_application(testing_service_client):
    if not testing_service_client.is_api_enabled('functions', 'DeleteApplication'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('functions', util.camelize('functions_management'), 'DeleteApplication')
    )

    request_containers = testing_service_client.get_requests(service_name='functions', api_name='DeleteApplication')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.functions.FunctionsManagementClient(config, service_endpoint=service_endpoint)
            response = client.delete_application(
                application_id=request.pop(util.camelize('applicationId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'functions',
            'DeleteApplication',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_application',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="serverless_grp@oracle.com" jiraProject="FAAS" opsJiraProject="FAAS"
def test_delete_function(testing_service_client):
    if not testing_service_client.is_api_enabled('functions', 'DeleteFunction'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('functions', util.camelize('functions_management'), 'DeleteFunction')
    )

    request_containers = testing_service_client.get_requests(service_name='functions', api_name='DeleteFunction')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.functions.FunctionsManagementClient(config, service_endpoint=service_endpoint)
            response = client.delete_function(
                function_id=request.pop(util.camelize('functionId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'functions',
            'DeleteFunction',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_function',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="serverless_grp@oracle.com" jiraProject="FAAS" opsJiraProject="FAAS"
def test_get_application(testing_service_client):
    if not testing_service_client.is_api_enabled('functions', 'GetApplication'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('functions', util.camelize('functions_management'), 'GetApplication')
    )

    request_containers = testing_service_client.get_requests(service_name='functions', api_name='GetApplication')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.functions.FunctionsManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_application(
                application_id=request.pop(util.camelize('applicationId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'functions',
            'GetApplication',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'application',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="serverless_grp@oracle.com" jiraProject="FAAS" opsJiraProject="FAAS"
def test_get_function(testing_service_client):
    if not testing_service_client.is_api_enabled('functions', 'GetFunction'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('functions', util.camelize('functions_management'), 'GetFunction')
    )

    request_containers = testing_service_client.get_requests(service_name='functions', api_name='GetFunction')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.functions.FunctionsManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_function(
                function_id=request.pop(util.camelize('functionId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'functions',
            'GetFunction',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'function',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="serverless_grp@oracle.com" jiraProject="FAAS" opsJiraProject="FAAS"
def test_list_applications(testing_service_client):
    if not testing_service_client.is_api_enabled('functions', 'ListApplications'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('functions', util.camelize('functions_management'), 'ListApplications')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='functions', api_name='ListApplications')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.functions.FunctionsManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_applications(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_applications(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_applications(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'functions',
            'ListApplications',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'applicationSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="serverless_grp@oracle.com" jiraProject="FAAS" opsJiraProject="FAAS"
def test_list_functions(testing_service_client):
    if not testing_service_client.is_api_enabled('functions', 'ListFunctions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('functions', util.camelize('functions_management'), 'ListFunctions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='functions', api_name='ListFunctions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.functions.FunctionsManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_functions(
                application_id=request.pop(util.camelize('applicationId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_functions(
                    application_id=request.pop(util.camelize('applicationId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_functions(
                        application_id=request.pop(util.camelize('applicationId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'functions',
            'ListFunctions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'functionSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="serverless_grp@oracle.com" jiraProject="FAAS" opsJiraProject="FAAS"
def test_update_application(testing_service_client):
    if not testing_service_client.is_api_enabled('functions', 'UpdateApplication'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('functions', util.camelize('functions_management'), 'UpdateApplication')
    )

    request_containers = testing_service_client.get_requests(service_name='functions', api_name='UpdateApplication')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.functions.FunctionsManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_application(
                application_id=request.pop(util.camelize('applicationId')),
                update_application_details=request.pop(util.camelize('UpdateApplicationDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'functions',
            'UpdateApplication',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'application',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="serverless_grp@oracle.com" jiraProject="FAAS" opsJiraProject="FAAS"
def test_update_function(testing_service_client):
    if not testing_service_client.is_api_enabled('functions', 'UpdateFunction'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('functions', util.camelize('functions_management'), 'UpdateFunction')
    )

    request_containers = testing_service_client.get_requests(service_name='functions', api_name='UpdateFunction')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.functions.FunctionsManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_function(
                function_id=request.pop(util.camelize('functionId')),
                update_function_details=request.pop(util.camelize('UpdateFunctionDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'functions',
            'UpdateFunction',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'function',
            False,
            False
        )
