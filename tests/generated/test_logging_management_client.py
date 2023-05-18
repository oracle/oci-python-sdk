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

        cassette_location = os.path.join('generated', 'logging_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="hydra_dev_us_grp@oracle.com" jiraProject="LOGICP" opsJiraProject="LOGICPOPS"
def test_change_log_group_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('logging', 'ChangeLogGroupCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('logging', util.camelize('logging_management'), 'ChangeLogGroupCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='logging', api_name='ChangeLogGroupCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.logging.LoggingManagementClient(config, service_endpoint=service_endpoint)
            response = client.change_log_group_compartment(
                log_group_id=request.pop(util.camelize('logGroupId')),
                change_log_group_compartment_details=request.pop(util.camelize('ChangeLogGroupCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'logging',
            'ChangeLogGroupCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_log_group_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="hydra_dev_us_grp@oracle.com" jiraProject="LOGICP" opsJiraProject="LOGICPOPS"
def test_change_log_log_group(testing_service_client):
    if not testing_service_client.is_api_enabled('logging', 'ChangeLogLogGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('logging', util.camelize('logging_management'), 'ChangeLogLogGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='logging', api_name='ChangeLogLogGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.logging.LoggingManagementClient(config, service_endpoint=service_endpoint)
            response = client.change_log_log_group(
                log_group_id=request.pop(util.camelize('logGroupId')),
                log_id=request.pop(util.camelize('logId')),
                change_log_log_group_details=request.pop(util.camelize('ChangeLogLogGroupDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'logging',
            'ChangeLogLogGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_log_log_group',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="hydra_dev_us_grp@oracle.com" jiraProject="LOGICP" opsJiraProject="LOGICPOPS"
def test_change_log_saved_search_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('logging', 'ChangeLogSavedSearchCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('logging', util.camelize('logging_management'), 'ChangeLogSavedSearchCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='logging', api_name='ChangeLogSavedSearchCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.logging.LoggingManagementClient(config, service_endpoint=service_endpoint)
            response = client.change_log_saved_search_compartment(
                log_saved_search_id=request.pop(util.camelize('logSavedSearchId')),
                change_log_saved_search_compartment_details=request.pop(util.camelize('ChangeLogSavedSearchCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'logging',
            'ChangeLogSavedSearchCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_log_saved_search_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="hydra_dev_us_grp@oracle.com" jiraProject="LOGICP" opsJiraProject="LOGICPOPS"
def test_change_unified_agent_configuration_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('logging', 'ChangeUnifiedAgentConfigurationCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('logging', util.camelize('logging_management'), 'ChangeUnifiedAgentConfigurationCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='logging', api_name='ChangeUnifiedAgentConfigurationCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.logging.LoggingManagementClient(config, service_endpoint=service_endpoint)
            response = client.change_unified_agent_configuration_compartment(
                unified_agent_configuration_id=request.pop(util.camelize('unifiedAgentConfigurationId')),
                change_unified_agent_configuration_compartment_details=request.pop(util.camelize('ChangeUnifiedAgentConfigurationCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'logging',
            'ChangeUnifiedAgentConfigurationCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_unified_agent_configuration_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="hydra_dev_us_grp@oracle.com" jiraProject="LOGICP" opsJiraProject="LOGICPOPS"
def test_create_log(testing_service_client):
    if not testing_service_client.is_api_enabled('logging', 'CreateLog'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('logging', util.camelize('logging_management'), 'CreateLog')
    )

    request_containers = testing_service_client.get_requests(service_name='logging', api_name='CreateLog')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.logging.LoggingManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_log(
                log_group_id=request.pop(util.camelize('logGroupId')),
                create_log_details=request.pop(util.camelize('CreateLogDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'logging',
            'CreateLog',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_log',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="hydra_dev_us_grp@oracle.com" jiraProject="LOGICP" opsJiraProject="LOGICPOPS"
def test_create_log_group(testing_service_client):
    if not testing_service_client.is_api_enabled('logging', 'CreateLogGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('logging', util.camelize('logging_management'), 'CreateLogGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='logging', api_name='CreateLogGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.logging.LoggingManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_log_group(
                create_log_group_details=request.pop(util.camelize('CreateLogGroupDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'logging',
            'CreateLogGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_log_group',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="hydra_dev_us_grp@oracle.com" jiraProject="LOGICP" opsJiraProject="LOGICPOPS"
def test_create_log_saved_search(testing_service_client):
    if not testing_service_client.is_api_enabled('logging', 'CreateLogSavedSearch'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('logging', util.camelize('logging_management'), 'CreateLogSavedSearch')
    )

    request_containers = testing_service_client.get_requests(service_name='logging', api_name='CreateLogSavedSearch')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.logging.LoggingManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_log_saved_search(
                create_log_saved_search_details=request.pop(util.camelize('CreateLogSavedSearchDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'logging',
            'CreateLogSavedSearch',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logSavedSearch',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="hydra_dev_us_grp@oracle.com" jiraProject="LOGICP" opsJiraProject="LOGICPOPS"
def test_create_unified_agent_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('logging', 'CreateUnifiedAgentConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('logging', util.camelize('logging_management'), 'CreateUnifiedAgentConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='logging', api_name='CreateUnifiedAgentConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.logging.LoggingManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_unified_agent_configuration(
                create_unified_agent_configuration_details=request.pop(util.camelize('CreateUnifiedAgentConfigurationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'logging',
            'CreateUnifiedAgentConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_unified_agent_configuration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="hydra_dev_us_grp@oracle.com" jiraProject="LOGICP" opsJiraProject="LOGICPOPS"
def test_delete_log(testing_service_client):
    if not testing_service_client.is_api_enabled('logging', 'DeleteLog'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('logging', util.camelize('logging_management'), 'DeleteLog')
    )

    request_containers = testing_service_client.get_requests(service_name='logging', api_name='DeleteLog')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.logging.LoggingManagementClient(config, service_endpoint=service_endpoint)
            response = client.delete_log(
                log_group_id=request.pop(util.camelize('logGroupId')),
                log_id=request.pop(util.camelize('logId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'logging',
            'DeleteLog',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_log',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="hydra_dev_us_grp@oracle.com" jiraProject="LOGICP" opsJiraProject="LOGICPOPS"
def test_delete_log_group(testing_service_client):
    if not testing_service_client.is_api_enabled('logging', 'DeleteLogGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('logging', util.camelize('logging_management'), 'DeleteLogGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='logging', api_name='DeleteLogGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.logging.LoggingManagementClient(config, service_endpoint=service_endpoint)
            response = client.delete_log_group(
                log_group_id=request.pop(util.camelize('logGroupId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'logging',
            'DeleteLogGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_log_group',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="hydra_dev_us_grp@oracle.com" jiraProject="LOGICP" opsJiraProject="LOGICPOPS"
def test_delete_log_saved_search(testing_service_client):
    if not testing_service_client.is_api_enabled('logging', 'DeleteLogSavedSearch'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('logging', util.camelize('logging_management'), 'DeleteLogSavedSearch')
    )

    request_containers = testing_service_client.get_requests(service_name='logging', api_name='DeleteLogSavedSearch')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.logging.LoggingManagementClient(config, service_endpoint=service_endpoint)
            response = client.delete_log_saved_search(
                log_saved_search_id=request.pop(util.camelize('logSavedSearchId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'logging',
            'DeleteLogSavedSearch',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_log_saved_search',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="hydra_dev_us_grp@oracle.com" jiraProject="LOGICP" opsJiraProject="LOGICPOPS"
def test_delete_unified_agent_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('logging', 'DeleteUnifiedAgentConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('logging', util.camelize('logging_management'), 'DeleteUnifiedAgentConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='logging', api_name='DeleteUnifiedAgentConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.logging.LoggingManagementClient(config, service_endpoint=service_endpoint)
            response = client.delete_unified_agent_configuration(
                unified_agent_configuration_id=request.pop(util.camelize('unifiedAgentConfigurationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'logging',
            'DeleteUnifiedAgentConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_unified_agent_configuration',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="hydra_dev_us_grp@oracle.com" jiraProject="LOGICP" opsJiraProject="LOGICPOPS"
def test_delete_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('logging', 'DeleteWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('logging', util.camelize('logging_management'), 'DeleteWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='logging', api_name='DeleteWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.logging.LoggingManagementClient(config, service_endpoint=service_endpoint)
            response = client.delete_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'logging',
            'DeleteWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_work_request',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="hydra_dev_us_grp@oracle.com" jiraProject="LOGICP" opsJiraProject="LOGICPOPS"
def test_get_log(testing_service_client):
    if not testing_service_client.is_api_enabled('logging', 'GetLog'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('logging', util.camelize('logging_management'), 'GetLog')
    )

    request_containers = testing_service_client.get_requests(service_name='logging', api_name='GetLog')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.logging.LoggingManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_log(
                log_group_id=request.pop(util.camelize('logGroupId')),
                log_id=request.pop(util.camelize('logId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'logging',
            'GetLog',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'log',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="hydra_dev_us_grp@oracle.com" jiraProject="LOGICP" opsJiraProject="LOGICPOPS"
def test_get_log_group(testing_service_client):
    if not testing_service_client.is_api_enabled('logging', 'GetLogGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('logging', util.camelize('logging_management'), 'GetLogGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='logging', api_name='GetLogGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.logging.LoggingManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_log_group(
                log_group_id=request.pop(util.camelize('logGroupId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'logging',
            'GetLogGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logGroup',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="hydra_dev_us_grp@oracle.com" jiraProject="LOGICP" opsJiraProject="LOGICPOPS"
def test_get_log_saved_search(testing_service_client):
    if not testing_service_client.is_api_enabled('logging', 'GetLogSavedSearch'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('logging', util.camelize('logging_management'), 'GetLogSavedSearch')
    )

    request_containers = testing_service_client.get_requests(service_name='logging', api_name='GetLogSavedSearch')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.logging.LoggingManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_log_saved_search(
                log_saved_search_id=request.pop(util.camelize('logSavedSearchId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'logging',
            'GetLogSavedSearch',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logSavedSearch',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="hydra_dev_us_grp@oracle.com" jiraProject="LOGICP" opsJiraProject="LOGICPOPS"
def test_get_unified_agent_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('logging', 'GetUnifiedAgentConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('logging', util.camelize('logging_management'), 'GetUnifiedAgentConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='logging', api_name='GetUnifiedAgentConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.logging.LoggingManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_unified_agent_configuration(
                unified_agent_configuration_id=request.pop(util.camelize('unifiedAgentConfigurationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'logging',
            'GetUnifiedAgentConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'unifiedAgentConfiguration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="hydra_dev_us_grp@oracle.com" jiraProject="LOGICP" opsJiraProject="LOGICPOPS"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('logging', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('logging', util.camelize('logging_management'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='logging', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.logging.LoggingManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'logging',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="hydra_dev_us_grp@oracle.com" jiraProject="LOGICP" opsJiraProject="LOGICPOPS"
def test_list_log_groups(testing_service_client):
    if not testing_service_client.is_api_enabled('logging', 'ListLogGroups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('logging', util.camelize('logging_management'), 'ListLogGroups')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='logging', api_name='ListLogGroups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.logging.LoggingManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_log_groups(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_log_groups(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_log_groups(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'logging',
            'ListLogGroups',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logGroupSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="hydra_dev_us_grp@oracle.com" jiraProject="LOGICP" opsJiraProject="LOGICPOPS"
def test_list_log_saved_searches(testing_service_client):
    if not testing_service_client.is_api_enabled('logging', 'ListLogSavedSearches'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('logging', util.camelize('logging_management'), 'ListLogSavedSearches')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='logging', api_name='ListLogSavedSearches')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.logging.LoggingManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_log_saved_searches(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_log_saved_searches(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_log_saved_searches(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'logging',
            'ListLogSavedSearches',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logSavedSearchSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="hydra_dev_us_grp@oracle.com" jiraProject="LOGICP" opsJiraProject="LOGICPOPS"
def test_list_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('logging', 'ListLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('logging', util.camelize('logging_management'), 'ListLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='logging', api_name='ListLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.logging.LoggingManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_logs(
                log_group_id=request.pop(util.camelize('logGroupId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_logs(
                    log_group_id=request.pop(util.camelize('logGroupId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_logs(
                        log_group_id=request.pop(util.camelize('logGroupId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'logging',
            'ListLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="hydra_dev_us_grp@oracle.com" jiraProject="LOGICP" opsJiraProject="LOGICPOPS"
def test_list_services(testing_service_client):
    if not testing_service_client.is_api_enabled('logging', 'ListServices'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('logging', util.camelize('logging_management'), 'ListServices')
    )

    request_containers = testing_service_client.get_requests(service_name='logging', api_name='ListServices')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.logging.LoggingManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_services(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'logging',
            'ListServices',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'serviceSummary',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="hydra_dev_us_grp@oracle.com" jiraProject="LOGICP" opsJiraProject="LOGICPOPS"
def test_list_unified_agent_configurations(testing_service_client):
    if not testing_service_client.is_api_enabled('logging', 'ListUnifiedAgentConfigurations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('logging', util.camelize('logging_management'), 'ListUnifiedAgentConfigurations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='logging', api_name='ListUnifiedAgentConfigurations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.logging.LoggingManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_unified_agent_configurations(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_unified_agent_configurations(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_unified_agent_configurations(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'logging',
            'ListUnifiedAgentConfigurations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'unifiedAgentConfigurationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="hydra_dev_us_grp@oracle.com" jiraProject="LOGICP" opsJiraProject="LOGICPOPS"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('logging', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('logging', util.camelize('logging_management'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='logging', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.logging.LoggingManagementClient(config, service_endpoint=service_endpoint)
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
            'logging',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestError',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="hydra_dev_us_grp@oracle.com" jiraProject="LOGICP" opsJiraProject="LOGICPOPS"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('logging', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('logging', util.camelize('logging_management'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='logging', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.logging.LoggingManagementClient(config, service_endpoint=service_endpoint)
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
            'logging',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLog',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="hydra_dev_us_grp@oracle.com" jiraProject="LOGICP" opsJiraProject="LOGICPOPS"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('logging', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('logging', util.camelize('logging_management'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='logging', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.logging.LoggingManagementClient(config, service_endpoint=service_endpoint)
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
            'logging',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="hydra_dev_us_grp@oracle.com" jiraProject="LOGICP" opsJiraProject="LOGICPOPS"
def test_update_log(testing_service_client):
    if not testing_service_client.is_api_enabled('logging', 'UpdateLog'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('logging', util.camelize('logging_management'), 'UpdateLog')
    )

    request_containers = testing_service_client.get_requests(service_name='logging', api_name='UpdateLog')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.logging.LoggingManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_log(
                log_group_id=request.pop(util.camelize('logGroupId')),
                log_id=request.pop(util.camelize('logId')),
                update_log_details=request.pop(util.camelize('UpdateLogDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'logging',
            'UpdateLog',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_log',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="hydra_dev_us_grp@oracle.com" jiraProject="LOGICP" opsJiraProject="LOGICPOPS"
def test_update_log_group(testing_service_client):
    if not testing_service_client.is_api_enabled('logging', 'UpdateLogGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('logging', util.camelize('logging_management'), 'UpdateLogGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='logging', api_name='UpdateLogGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.logging.LoggingManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_log_group(
                log_group_id=request.pop(util.camelize('logGroupId')),
                update_log_group_details=request.pop(util.camelize('UpdateLogGroupDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'logging',
            'UpdateLogGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_log_group',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="hydra_dev_us_grp@oracle.com" jiraProject="LOGICP" opsJiraProject="LOGICPOPS"
def test_update_log_saved_search(testing_service_client):
    if not testing_service_client.is_api_enabled('logging', 'UpdateLogSavedSearch'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('logging', util.camelize('logging_management'), 'UpdateLogSavedSearch')
    )

    request_containers = testing_service_client.get_requests(service_name='logging', api_name='UpdateLogSavedSearch')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.logging.LoggingManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_log_saved_search(
                log_saved_search_id=request.pop(util.camelize('logSavedSearchId')),
                update_log_saved_search_details=request.pop(util.camelize('UpdateLogSavedSearchDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'logging',
            'UpdateLogSavedSearch',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logSavedSearch',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="hydra_dev_us_grp@oracle.com" jiraProject="LOGICP" opsJiraProject="LOGICPOPS"
def test_update_unified_agent_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('logging', 'UpdateUnifiedAgentConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('logging', util.camelize('logging_management'), 'UpdateUnifiedAgentConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='logging', api_name='UpdateUnifiedAgentConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.logging.LoggingManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_unified_agent_configuration(
                unified_agent_configuration_id=request.pop(util.camelize('unifiedAgentConfigurationId')),
                update_unified_agent_configuration_details=request.pop(util.camelize('UpdateUnifiedAgentConfigurationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'logging',
            'UpdateUnifiedAgentConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_unified_agent_configuration',
            False,
            False
        )
