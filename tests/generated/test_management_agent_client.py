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

        cassette_location = os.path.join('generated', 'management_agent_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="team_oci_mgmtagent_macs_ww_grp@oracle.com" jiraProject="MGMTAGENT" opsJiraProject="MGMTAGENT"
def test_create_management_agent_install_key(testing_service_client):
    if not testing_service_client.is_api_enabled('management_agent', 'CreateManagementAgentInstallKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('management_agent', util.camelize('management_agent'), 'CreateManagementAgentInstallKey')
    )

    request_containers = testing_service_client.get_requests(service_name='management_agent', api_name='CreateManagementAgentInstallKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.management_agent.ManagementAgentClient(config, service_endpoint=service_endpoint)
            response = client.create_management_agent_install_key(
                create_management_agent_install_key_details=request.pop(util.camelize('CreateManagementAgentInstallKeyDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'management_agent',
            'CreateManagementAgentInstallKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managementAgentInstallKey',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_mgmtagent_macs_ww_grp@oracle.com" jiraProject="MGMTAGENT" opsJiraProject="MGMTAGENT"
def test_delete_management_agent(testing_service_client):
    if not testing_service_client.is_api_enabled('management_agent', 'DeleteManagementAgent'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('management_agent', util.camelize('management_agent'), 'DeleteManagementAgent')
    )

    request_containers = testing_service_client.get_requests(service_name='management_agent', api_name='DeleteManagementAgent')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.management_agent.ManagementAgentClient(config, service_endpoint=service_endpoint)
            response = client.delete_management_agent(
                management_agent_id=request.pop(util.camelize('managementAgentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'management_agent',
            'DeleteManagementAgent',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_management_agent',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_mgmtagent_macs_ww_grp@oracle.com" jiraProject="MGMTAGENT" opsJiraProject="MGMTAGENT"
def test_delete_management_agent_install_key(testing_service_client):
    if not testing_service_client.is_api_enabled('management_agent', 'DeleteManagementAgentInstallKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('management_agent', util.camelize('management_agent'), 'DeleteManagementAgentInstallKey')
    )

    request_containers = testing_service_client.get_requests(service_name='management_agent', api_name='DeleteManagementAgentInstallKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.management_agent.ManagementAgentClient(config, service_endpoint=service_endpoint)
            response = client.delete_management_agent_install_key(
                management_agent_install_key_id=request.pop(util.camelize('managementAgentInstallKeyId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'management_agent',
            'DeleteManagementAgentInstallKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_management_agent_install_key',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_mgmtagent_macs_ww_grp@oracle.com" jiraProject="MGMTAGENT" opsJiraProject="MGMTAGENT"
def test_delete_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('management_agent', 'DeleteWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('management_agent', util.camelize('management_agent'), 'DeleteWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='management_agent', api_name='DeleteWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.management_agent.ManagementAgentClient(config, service_endpoint=service_endpoint)
            response = client.delete_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'management_agent',
            'DeleteWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_work_request',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_mgmtagent_macs_ww_grp@oracle.com" jiraProject="MGMTAGENT" opsJiraProject="MGMTAGENT"
def test_deploy_plugins(testing_service_client):
    if not testing_service_client.is_api_enabled('management_agent', 'DeployPlugins'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('management_agent', util.camelize('management_agent'), 'DeployPlugins')
    )

    request_containers = testing_service_client.get_requests(service_name='management_agent', api_name='DeployPlugins')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.management_agent.ManagementAgentClient(config, service_endpoint=service_endpoint)
            response = client.deploy_plugins(
                deploy_plugins_details=request.pop(util.camelize('DeployPluginsDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'management_agent',
            'DeployPlugins',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deploy_plugins',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_mgmtagent_macs_ww_grp@oracle.com" jiraProject="MGMTAGENT" opsJiraProject="MGMTAGENT"
def test_get_auto_upgradable_config(testing_service_client):
    if not testing_service_client.is_api_enabled('management_agent', 'GetAutoUpgradableConfig'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('management_agent', util.camelize('management_agent'), 'GetAutoUpgradableConfig')
    )

    request_containers = testing_service_client.get_requests(service_name='management_agent', api_name='GetAutoUpgradableConfig')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.management_agent.ManagementAgentClient(config, service_endpoint=service_endpoint)
            response = client.get_auto_upgradable_config(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'management_agent',
            'GetAutoUpgradableConfig',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autoUpgradableConfig',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_mgmtagent_macs_ww_grp@oracle.com" jiraProject="MGMTAGENT" opsJiraProject="MGMTAGENT"
def test_get_management_agent(testing_service_client):
    if not testing_service_client.is_api_enabled('management_agent', 'GetManagementAgent'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('management_agent', util.camelize('management_agent'), 'GetManagementAgent')
    )

    request_containers = testing_service_client.get_requests(service_name='management_agent', api_name='GetManagementAgent')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.management_agent.ManagementAgentClient(config, service_endpoint=service_endpoint)
            response = client.get_management_agent(
                management_agent_id=request.pop(util.camelize('managementAgentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'management_agent',
            'GetManagementAgent',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managementAgent',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_mgmtagent_macs_ww_grp@oracle.com" jiraProject="MGMTAGENT" opsJiraProject="MGMTAGENT"
def test_get_management_agent_install_key(testing_service_client):
    if not testing_service_client.is_api_enabled('management_agent', 'GetManagementAgentInstallKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('management_agent', util.camelize('management_agent'), 'GetManagementAgentInstallKey')
    )

    request_containers = testing_service_client.get_requests(service_name='management_agent', api_name='GetManagementAgentInstallKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.management_agent.ManagementAgentClient(config, service_endpoint=service_endpoint)
            response = client.get_management_agent_install_key(
                management_agent_install_key_id=request.pop(util.camelize('managementAgentInstallKeyId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'management_agent',
            'GetManagementAgentInstallKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managementAgentInstallKey',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_mgmtagent_macs_ww_grp@oracle.com" jiraProject="MGMTAGENT" opsJiraProject="MGMTAGENT"
def test_get_management_agent_install_key_content(testing_service_client):
    if not testing_service_client.is_api_enabled('management_agent', 'GetManagementAgentInstallKeyContent'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('management_agent', util.camelize('management_agent'), 'GetManagementAgentInstallKeyContent')
    )

    request_containers = testing_service_client.get_requests(service_name='management_agent', api_name='GetManagementAgentInstallKeyContent')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.management_agent.ManagementAgentClient(config, service_endpoint=service_endpoint)
            response = client.get_management_agent_install_key_content(
                management_agent_install_key_id=request.pop(util.camelize('managementAgentInstallKeyId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'management_agent',
            'GetManagementAgentInstallKeyContent',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_mgmtagent_macs_ww_grp@oracle.com" jiraProject="MGMTAGENT" opsJiraProject="MGMTAGENT"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('management_agent', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('management_agent', util.camelize('management_agent'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='management_agent', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.management_agent.ManagementAgentClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'management_agent',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_mgmtagent_macs_ww_grp@oracle.com" jiraProject="MGMTAGENT" opsJiraProject="MGMTAGENT"
def test_list_availability_histories(testing_service_client):
    if not testing_service_client.is_api_enabled('management_agent', 'ListAvailabilityHistories'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('management_agent', util.camelize('management_agent'), 'ListAvailabilityHistories')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='management_agent', api_name='ListAvailabilityHistories')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.management_agent.ManagementAgentClient(config, service_endpoint=service_endpoint)
            response = client.list_availability_histories(
                management_agent_id=request.pop(util.camelize('managementAgentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_availability_histories(
                    management_agent_id=request.pop(util.camelize('managementAgentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_availability_histories(
                        management_agent_id=request.pop(util.camelize('managementAgentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'management_agent',
            'ListAvailabilityHistories',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'availabilityHistorySummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_mgmtagent_macs_ww_grp@oracle.com" jiraProject="MGMTAGENT" opsJiraProject="MGMTAGENT"
def test_list_management_agent_images(testing_service_client):
    if not testing_service_client.is_api_enabled('management_agent', 'ListManagementAgentImages'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('management_agent', util.camelize('management_agent'), 'ListManagementAgentImages')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='management_agent', api_name='ListManagementAgentImages')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.management_agent.ManagementAgentClient(config, service_endpoint=service_endpoint)
            response = client.list_management_agent_images(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_management_agent_images(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_management_agent_images(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'management_agent',
            'ListManagementAgentImages',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managementAgentImageSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_mgmtagent_macs_ww_grp@oracle.com" jiraProject="MGMTAGENT" opsJiraProject="MGMTAGENT"
def test_list_management_agent_install_keys(testing_service_client):
    if not testing_service_client.is_api_enabled('management_agent', 'ListManagementAgentInstallKeys'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('management_agent', util.camelize('management_agent'), 'ListManagementAgentInstallKeys')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='management_agent', api_name='ListManagementAgentInstallKeys')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.management_agent.ManagementAgentClient(config, service_endpoint=service_endpoint)
            response = client.list_management_agent_install_keys(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_management_agent_install_keys(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_management_agent_install_keys(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'management_agent',
            'ListManagementAgentInstallKeys',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managementAgentInstallKeySummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_mgmtagent_macs_ww_grp@oracle.com" jiraProject="MGMTAGENT" opsJiraProject="MGMTAGENT"
def test_list_management_agent_plugins(testing_service_client):
    if not testing_service_client.is_api_enabled('management_agent', 'ListManagementAgentPlugins'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('management_agent', util.camelize('management_agent'), 'ListManagementAgentPlugins')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='management_agent', api_name='ListManagementAgentPlugins')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.management_agent.ManagementAgentClient(config, service_endpoint=service_endpoint)
            response = client.list_management_agent_plugins(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_management_agent_plugins(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_management_agent_plugins(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'management_agent',
            'ListManagementAgentPlugins',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managementAgentPluginSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_mgmtagent_macs_ww_grp@oracle.com" jiraProject="MGMTAGENT" opsJiraProject="MGMTAGENT"
def test_list_management_agents(testing_service_client):
    if not testing_service_client.is_api_enabled('management_agent', 'ListManagementAgents'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('management_agent', util.camelize('management_agent'), 'ListManagementAgents')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='management_agent', api_name='ListManagementAgents')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.management_agent.ManagementAgentClient(config, service_endpoint=service_endpoint)
            response = client.list_management_agents(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_management_agents(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_management_agents(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'management_agent',
            'ListManagementAgents',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managementAgentSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_mgmtagent_macs_ww_grp@oracle.com" jiraProject="MGMTAGENT" opsJiraProject="MGMTAGENT"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('management_agent', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('management_agent', util.camelize('management_agent'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='management_agent', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.management_agent.ManagementAgentClient(config, service_endpoint=service_endpoint)
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
            'management_agent',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestError',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_mgmtagent_macs_ww_grp@oracle.com" jiraProject="MGMTAGENT" opsJiraProject="MGMTAGENT"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('management_agent', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('management_agent', util.camelize('management_agent'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='management_agent', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.management_agent.ManagementAgentClient(config, service_endpoint=service_endpoint)
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
            'management_agent',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntry',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_mgmtagent_macs_ww_grp@oracle.com" jiraProject="MGMTAGENT" opsJiraProject="MGMTAGENT"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('management_agent', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('management_agent', util.camelize('management_agent'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='management_agent', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.management_agent.ManagementAgentClient(config, service_endpoint=service_endpoint)
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
            'management_agent',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_mgmtagent_macs_ww_grp@oracle.com" jiraProject="MGMTAGENT" opsJiraProject="MGMTAGENT"
def test_set_auto_upgradable_config(testing_service_client):
    if not testing_service_client.is_api_enabled('management_agent', 'SetAutoUpgradableConfig'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('management_agent', util.camelize('management_agent'), 'SetAutoUpgradableConfig')
    )

    request_containers = testing_service_client.get_requests(service_name='management_agent', api_name='SetAutoUpgradableConfig')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.management_agent.ManagementAgentClient(config, service_endpoint=service_endpoint)
            response = client.set_auto_upgradable_config(
                set_auto_upgradable_config_details=request.pop(util.camelize('SetAutoUpgradableConfigDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'management_agent',
            'SetAutoUpgradableConfig',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autoUpgradableConfig',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_mgmtagent_macs_ww_grp@oracle.com" jiraProject="MGMTAGENT" opsJiraProject="MGMTAGENT"
def test_summarize_management_agent_counts(testing_service_client):
    if not testing_service_client.is_api_enabled('management_agent', 'SummarizeManagementAgentCounts'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('management_agent', util.camelize('management_agent'), 'SummarizeManagementAgentCounts')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='management_agent', api_name='SummarizeManagementAgentCounts')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.management_agent.ManagementAgentClient(config, service_endpoint=service_endpoint)
            response = client.summarize_management_agent_counts(
                compartment_id=request.pop(util.camelize('compartmentId')),
                group_by=request.pop(util.camelize('groupBy')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_management_agent_counts(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    group_by=request.pop(util.camelize('groupBy')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_management_agent_counts(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        group_by=request.pop(util.camelize('groupBy')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'management_agent',
            'SummarizeManagementAgentCounts',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managementAgentAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_mgmtagent_macs_ww_grp@oracle.com" jiraProject="MGMTAGENT" opsJiraProject="MGMTAGENT"
def test_summarize_management_agent_plugin_counts(testing_service_client):
    if not testing_service_client.is_api_enabled('management_agent', 'SummarizeManagementAgentPluginCounts'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('management_agent', util.camelize('management_agent'), 'SummarizeManagementAgentPluginCounts')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='management_agent', api_name='SummarizeManagementAgentPluginCounts')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.management_agent.ManagementAgentClient(config, service_endpoint=service_endpoint)
            response = client.summarize_management_agent_plugin_counts(
                compartment_id=request.pop(util.camelize('compartmentId')),
                group_by=request.pop(util.camelize('groupBy')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_management_agent_plugin_counts(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    group_by=request.pop(util.camelize('groupBy')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_management_agent_plugin_counts(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        group_by=request.pop(util.camelize('groupBy')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'management_agent',
            'SummarizeManagementAgentPluginCounts',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managementAgentPluginAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_mgmtagent_macs_ww_grp@oracle.com" jiraProject="MGMTAGENT" opsJiraProject="MGMTAGENT"
def test_update_management_agent(testing_service_client):
    if not testing_service_client.is_api_enabled('management_agent', 'UpdateManagementAgent'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('management_agent', util.camelize('management_agent'), 'UpdateManagementAgent')
    )

    request_containers = testing_service_client.get_requests(service_name='management_agent', api_name='UpdateManagementAgent')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.management_agent.ManagementAgentClient(config, service_endpoint=service_endpoint)
            response = client.update_management_agent(
                management_agent_id=request.pop(util.camelize('managementAgentId')),
                update_management_agent_details=request.pop(util.camelize('UpdateManagementAgentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'management_agent',
            'UpdateManagementAgent',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managementAgent',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_mgmtagent_macs_ww_grp@oracle.com" jiraProject="MGMTAGENT" opsJiraProject="MGMTAGENT"
def test_update_management_agent_install_key(testing_service_client):
    if not testing_service_client.is_api_enabled('management_agent', 'UpdateManagementAgentInstallKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('management_agent', util.camelize('management_agent'), 'UpdateManagementAgentInstallKey')
    )

    request_containers = testing_service_client.get_requests(service_name='management_agent', api_name='UpdateManagementAgentInstallKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.management_agent.ManagementAgentClient(config, service_endpoint=service_endpoint)
            response = client.update_management_agent_install_key(
                management_agent_install_key_id=request.pop(util.camelize('managementAgentInstallKeyId')),
                update_management_agent_install_key_details=request.pop(util.camelize('UpdateManagementAgentInstallKeyDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'management_agent',
            'UpdateManagementAgentInstallKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managementAgentInstallKey',
            False,
            False
        )
