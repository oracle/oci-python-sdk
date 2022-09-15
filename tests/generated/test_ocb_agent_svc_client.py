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

        cassette_location = os.path.join('generated', 'cloud_bridge_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_add_agent_dependency(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'AddAgentDependency'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('ocb_agent_svc'), 'AddAgentDependency')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='AddAgentDependency')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.OcbAgentSvcClient(config, service_endpoint=service_endpoint)
            response = client.add_agent_dependency(
                environment_id=request.pop(util.camelize('environmentId')),
                add_agent_dependency_details=request.pop(util.camelize('AddAgentDependencyDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'AddAgentDependency',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'environment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_change_agent_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'ChangeAgentCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('ocb_agent_svc'), 'ChangeAgentCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='ChangeAgentCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.OcbAgentSvcClient(config, service_endpoint=service_endpoint)
            response = client.change_agent_compartment(
                agent_id=request.pop(util.camelize('agentId')),
                change_agent_compartment_details=request.pop(util.camelize('ChangeAgentCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'ChangeAgentCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_agent_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_change_agent_dependency_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'ChangeAgentDependencyCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('ocb_agent_svc'), 'ChangeAgentDependencyCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='ChangeAgentDependencyCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.OcbAgentSvcClient(config, service_endpoint=service_endpoint)
            response = client.change_agent_dependency_compartment(
                agent_dependency_id=request.pop(util.camelize('agentDependencyId')),
                change_agent_dependency_compartment_details=request.pop(util.camelize('ChangeAgentDependencyCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'ChangeAgentDependencyCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_agent_dependency_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_change_environment_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'ChangeEnvironmentCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('ocb_agent_svc'), 'ChangeEnvironmentCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='ChangeEnvironmentCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.OcbAgentSvcClient(config, service_endpoint=service_endpoint)
            response = client.change_environment_compartment(
                environment_id=request.pop(util.camelize('environmentId')),
                change_environment_compartment_details=request.pop(util.camelize('ChangeEnvironmentCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'ChangeEnvironmentCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_environment_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_create_agent(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'CreateAgent'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('ocb_agent_svc'), 'CreateAgent')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='CreateAgent')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.OcbAgentSvcClient(config, service_endpoint=service_endpoint)
            response = client.create_agent(
                create_agent_details=request.pop(util.camelize('CreateAgentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'CreateAgent',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'agent',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_create_agent_dependency(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'CreateAgentDependency'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('ocb_agent_svc'), 'CreateAgentDependency')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='CreateAgentDependency')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.OcbAgentSvcClient(config, service_endpoint=service_endpoint)
            response = client.create_agent_dependency(
                create_agent_dependency_details=request.pop(util.camelize('CreateAgentDependencyDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'CreateAgentDependency',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'agentDependency',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_create_environment(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'CreateEnvironment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('ocb_agent_svc'), 'CreateEnvironment')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='CreateEnvironment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.OcbAgentSvcClient(config, service_endpoint=service_endpoint)
            response = client.create_environment(
                create_environment_details=request.pop(util.camelize('CreateEnvironmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'CreateEnvironment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'environment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_delete_agent(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'DeleteAgent'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('ocb_agent_svc'), 'DeleteAgent')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='DeleteAgent')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.OcbAgentSvcClient(config, service_endpoint=service_endpoint)
            response = client.delete_agent(
                agent_id=request.pop(util.camelize('agentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'DeleteAgent',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_agent',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_delete_agent_dependency(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'DeleteAgentDependency'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('ocb_agent_svc'), 'DeleteAgentDependency')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='DeleteAgentDependency')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.OcbAgentSvcClient(config, service_endpoint=service_endpoint)
            response = client.delete_agent_dependency(
                agent_dependency_id=request.pop(util.camelize('agentDependencyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'DeleteAgentDependency',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_agent_dependency',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_delete_environment(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'DeleteEnvironment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('ocb_agent_svc'), 'DeleteEnvironment')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='DeleteEnvironment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.OcbAgentSvcClient(config, service_endpoint=service_endpoint)
            response = client.delete_environment(
                environment_id=request.pop(util.camelize('environmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'DeleteEnvironment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_environment',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_agent(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'GetAgent'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('ocb_agent_svc'), 'GetAgent')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='GetAgent')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.OcbAgentSvcClient(config, service_endpoint=service_endpoint)
            response = client.get_agent(
                agent_id=request.pop(util.camelize('agentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'GetAgent',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'agent',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_agent_dependency(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'GetAgentDependency'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('ocb_agent_svc'), 'GetAgentDependency')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='GetAgentDependency')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.OcbAgentSvcClient(config, service_endpoint=service_endpoint)
            response = client.get_agent_dependency(
                agent_dependency_id=request.pop(util.camelize('agentDependencyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'GetAgentDependency',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'agentDependency',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_environment(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'GetEnvironment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('ocb_agent_svc'), 'GetEnvironment')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='GetEnvironment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.OcbAgentSvcClient(config, service_endpoint=service_endpoint)
            response = client.get_environment(
                environment_id=request.pop(util.camelize('environmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'GetEnvironment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'environment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_plugin(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'GetPlugin'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('ocb_agent_svc'), 'GetPlugin')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='GetPlugin')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.OcbAgentSvcClient(config, service_endpoint=service_endpoint)
            response = client.get_plugin(
                agent_id=request.pop(util.camelize('agentId')),
                plugin_name=request.pop(util.camelize('pluginName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'GetPlugin',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'plugin',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_agent_dependencies(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'ListAgentDependencies'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('ocb_agent_svc'), 'ListAgentDependencies')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='ListAgentDependencies')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.OcbAgentSvcClient(config, service_endpoint=service_endpoint)
            response = client.list_agent_dependencies(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_agent_dependencies(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_agent_dependencies(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'ListAgentDependencies',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'agentDependencyCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_agents(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'ListAgents'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('ocb_agent_svc'), 'ListAgents')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='ListAgents')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.OcbAgentSvcClient(config, service_endpoint=service_endpoint)
            response = client.list_agents(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_agents(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_agents(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'ListAgents',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'agentCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_appliance_images(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'ListApplianceImages'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('ocb_agent_svc'), 'ListApplianceImages')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='ListApplianceImages')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.OcbAgentSvcClient(config, service_endpoint=service_endpoint)
            response = client.list_appliance_images(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_appliance_images(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_appliance_images(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'ListApplianceImages',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'applianceImageCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_environments(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'ListEnvironments'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('ocb_agent_svc'), 'ListEnvironments')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='ListEnvironments')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.OcbAgentSvcClient(config, service_endpoint=service_endpoint)
            response = client.list_environments(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_environments(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_environments(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'ListEnvironments',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'environmentCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_remove_agent_dependency(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'RemoveAgentDependency'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('ocb_agent_svc'), 'RemoveAgentDependency')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='RemoveAgentDependency')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.OcbAgentSvcClient(config, service_endpoint=service_endpoint)
            response = client.remove_agent_dependency(
                environment_id=request.pop(util.camelize('environmentId')),
                remove_agent_dependency_details=request.pop(util.camelize('RemoveAgentDependencyDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'RemoveAgentDependency',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'environment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_update_agent(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'UpdateAgent'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('ocb_agent_svc'), 'UpdateAgent')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='UpdateAgent')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.OcbAgentSvcClient(config, service_endpoint=service_endpoint)
            response = client.update_agent(
                agent_id=request.pop(util.camelize('agentId')),
                update_agent_details=request.pop(util.camelize('UpdateAgentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'UpdateAgent',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'agent',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_update_agent_dependency(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'UpdateAgentDependency'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('ocb_agent_svc'), 'UpdateAgentDependency')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='UpdateAgentDependency')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.OcbAgentSvcClient(config, service_endpoint=service_endpoint)
            response = client.update_agent_dependency(
                agent_dependency_id=request.pop(util.camelize('agentDependencyId')),
                update_agent_dependency_details=request.pop(util.camelize('UpdateAgentDependencyDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'UpdateAgentDependency',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_agent_dependency',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_update_environment(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'UpdateEnvironment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('ocb_agent_svc'), 'UpdateEnvironment')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='UpdateEnvironment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.OcbAgentSvcClient(config, service_endpoint=service_endpoint)
            response = client.update_environment(
                environment_id=request.pop(util.camelize('environmentId')),
                update_environment_details=request.pop(util.camelize('UpdateEnvironmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'UpdateEnvironment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'environment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_update_plugin(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'UpdatePlugin'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('ocb_agent_svc'), 'UpdatePlugin')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='UpdatePlugin')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.OcbAgentSvcClient(config, service_endpoint=service_endpoint)
            response = client.update_plugin(
                agent_id=request.pop(util.camelize('agentId')),
                plugin_name=request.pop(util.camelize('pluginName')),
                update_plugin_details=request.pop(util.camelize('UpdatePluginDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'UpdatePlugin',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'plugin',
            False,
            False
        )
