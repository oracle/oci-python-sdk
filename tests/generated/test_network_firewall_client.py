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

        cassette_location = os.path.join('generated', 'network_firewall_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="oci_ngfw_ww_grp@oracle.com" jiraProject="NGFW" opsJiraProject="JIRA-OPS"
def test_cancel_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('network_firewall', 'CancelWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_firewall', util.camelize('network_firewall'), 'CancelWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='network_firewall', api_name='CancelWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_firewall.NetworkFirewallClient(config, service_endpoint=service_endpoint)
            response = client.cancel_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_firewall',
            'CancelWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cancel_work_request',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ngfw_ww_grp@oracle.com" jiraProject="NGFW" opsJiraProject="JIRA-OPS"
def test_change_network_firewall_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('network_firewall', 'ChangeNetworkFirewallCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_firewall', util.camelize('network_firewall'), 'ChangeNetworkFirewallCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='network_firewall', api_name='ChangeNetworkFirewallCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_firewall.NetworkFirewallClient(config, service_endpoint=service_endpoint)
            response = client.change_network_firewall_compartment(
                network_firewall_id=request.pop(util.camelize('networkFirewallId')),
                change_network_firewall_compartment_details=request.pop(util.camelize('ChangeNetworkFirewallCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_firewall',
            'ChangeNetworkFirewallCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_network_firewall_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ngfw_ww_grp@oracle.com" jiraProject="NGFW" opsJiraProject="JIRA-OPS"
def test_change_network_firewall_policy_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('network_firewall', 'ChangeNetworkFirewallPolicyCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_firewall', util.camelize('network_firewall'), 'ChangeNetworkFirewallPolicyCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='network_firewall', api_name='ChangeNetworkFirewallPolicyCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_firewall.NetworkFirewallClient(config, service_endpoint=service_endpoint)
            response = client.change_network_firewall_policy_compartment(
                network_firewall_policy_id=request.pop(util.camelize('networkFirewallPolicyId')),
                change_network_firewall_policy_compartment_details=request.pop(util.camelize('ChangeNetworkFirewallPolicyCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_firewall',
            'ChangeNetworkFirewallPolicyCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_network_firewall_policy_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ngfw_ww_grp@oracle.com" jiraProject="NGFW" opsJiraProject="JIRA-OPS"
def test_create_network_firewall(testing_service_client):
    if not testing_service_client.is_api_enabled('network_firewall', 'CreateNetworkFirewall'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_firewall', util.camelize('network_firewall'), 'CreateNetworkFirewall')
    )

    request_containers = testing_service_client.get_requests(service_name='network_firewall', api_name='CreateNetworkFirewall')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_firewall.NetworkFirewallClient(config, service_endpoint=service_endpoint)
            response = client.create_network_firewall(
                create_network_firewall_details=request.pop(util.camelize('CreateNetworkFirewallDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_firewall',
            'CreateNetworkFirewall',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'networkFirewall',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ngfw_ww_grp@oracle.com" jiraProject="NGFW" opsJiraProject="JIRA-OPS"
def test_create_network_firewall_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('network_firewall', 'CreateNetworkFirewallPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_firewall', util.camelize('network_firewall'), 'CreateNetworkFirewallPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='network_firewall', api_name='CreateNetworkFirewallPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_firewall.NetworkFirewallClient(config, service_endpoint=service_endpoint)
            response = client.create_network_firewall_policy(
                create_network_firewall_policy_details=request.pop(util.camelize('CreateNetworkFirewallPolicyDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_firewall',
            'CreateNetworkFirewallPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'networkFirewallPolicy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ngfw_ww_grp@oracle.com" jiraProject="NGFW" opsJiraProject="JIRA-OPS"
def test_delete_network_firewall(testing_service_client):
    if not testing_service_client.is_api_enabled('network_firewall', 'DeleteNetworkFirewall'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_firewall', util.camelize('network_firewall'), 'DeleteNetworkFirewall')
    )

    request_containers = testing_service_client.get_requests(service_name='network_firewall', api_name='DeleteNetworkFirewall')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_firewall.NetworkFirewallClient(config, service_endpoint=service_endpoint)
            response = client.delete_network_firewall(
                network_firewall_id=request.pop(util.camelize('networkFirewallId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_firewall',
            'DeleteNetworkFirewall',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_network_firewall',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ngfw_ww_grp@oracle.com" jiraProject="NGFW" opsJiraProject="JIRA-OPS"
def test_delete_network_firewall_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('network_firewall', 'DeleteNetworkFirewallPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_firewall', util.camelize('network_firewall'), 'DeleteNetworkFirewallPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='network_firewall', api_name='DeleteNetworkFirewallPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_firewall.NetworkFirewallClient(config, service_endpoint=service_endpoint)
            response = client.delete_network_firewall_policy(
                network_firewall_policy_id=request.pop(util.camelize('networkFirewallPolicyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_firewall',
            'DeleteNetworkFirewallPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_network_firewall_policy',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ngfw_ww_grp@oracle.com" jiraProject="NGFW" opsJiraProject="JIRA-OPS"
def test_get_network_firewall(testing_service_client):
    if not testing_service_client.is_api_enabled('network_firewall', 'GetNetworkFirewall'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_firewall', util.camelize('network_firewall'), 'GetNetworkFirewall')
    )

    request_containers = testing_service_client.get_requests(service_name='network_firewall', api_name='GetNetworkFirewall')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_firewall.NetworkFirewallClient(config, service_endpoint=service_endpoint)
            response = client.get_network_firewall(
                network_firewall_id=request.pop(util.camelize('networkFirewallId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_firewall',
            'GetNetworkFirewall',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'networkFirewall',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ngfw_ww_grp@oracle.com" jiraProject="NGFW" opsJiraProject="JIRA-OPS"
def test_get_network_firewall_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('network_firewall', 'GetNetworkFirewallPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_firewall', util.camelize('network_firewall'), 'GetNetworkFirewallPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='network_firewall', api_name='GetNetworkFirewallPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_firewall.NetworkFirewallClient(config, service_endpoint=service_endpoint)
            response = client.get_network_firewall_policy(
                network_firewall_policy_id=request.pop(util.camelize('networkFirewallPolicyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_firewall',
            'GetNetworkFirewallPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'networkFirewallPolicy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ngfw_ww_grp@oracle.com" jiraProject="NGFW" opsJiraProject="JIRA-OPS"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('network_firewall', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_firewall', util.camelize('network_firewall'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='network_firewall', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_firewall.NetworkFirewallClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_firewall',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ngfw_ww_grp@oracle.com" jiraProject="NGFW" opsJiraProject="JIRA-OPS"
def test_list_network_firewall_policies(testing_service_client):
    if not testing_service_client.is_api_enabled('network_firewall', 'ListNetworkFirewallPolicies'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_firewall', util.camelize('network_firewall'), 'ListNetworkFirewallPolicies')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='network_firewall', api_name='ListNetworkFirewallPolicies')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_firewall.NetworkFirewallClient(config, service_endpoint=service_endpoint)
            response = client.list_network_firewall_policies(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_network_firewall_policies(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_network_firewall_policies(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_firewall',
            'ListNetworkFirewallPolicies',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'networkFirewallPolicySummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_ngfw_ww_grp@oracle.com" jiraProject="NGFW" opsJiraProject="JIRA-OPS"
def test_list_network_firewalls(testing_service_client):
    if not testing_service_client.is_api_enabled('network_firewall', 'ListNetworkFirewalls'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_firewall', util.camelize('network_firewall'), 'ListNetworkFirewalls')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='network_firewall', api_name='ListNetworkFirewalls')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_firewall.NetworkFirewallClient(config, service_endpoint=service_endpoint)
            response = client.list_network_firewalls(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_network_firewalls(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_network_firewalls(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_firewall',
            'ListNetworkFirewalls',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'networkFirewallCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_ngfw_ww_grp@oracle.com" jiraProject="NGFW" opsJiraProject="JIRA-OPS"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('network_firewall', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_firewall', util.camelize('network_firewall'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='network_firewall', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_firewall.NetworkFirewallClient(config, service_endpoint=service_endpoint)
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
            'network_firewall',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestErrorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_ngfw_ww_grp@oracle.com" jiraProject="NGFW" opsJiraProject="JIRA-OPS"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('network_firewall', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_firewall', util.camelize('network_firewall'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='network_firewall', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_firewall.NetworkFirewallClient(config, service_endpoint=service_endpoint)
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
            'network_firewall',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_ngfw_ww_grp@oracle.com" jiraProject="NGFW" opsJiraProject="JIRA-OPS"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('network_firewall', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_firewall', util.camelize('network_firewall'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='network_firewall', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_firewall.NetworkFirewallClient(config, service_endpoint=service_endpoint)
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
            'network_firewall',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_ngfw_ww_grp@oracle.com" jiraProject="NGFW" opsJiraProject="JIRA-OPS"
def test_update_network_firewall(testing_service_client):
    if not testing_service_client.is_api_enabled('network_firewall', 'UpdateNetworkFirewall'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_firewall', util.camelize('network_firewall'), 'UpdateNetworkFirewall')
    )

    request_containers = testing_service_client.get_requests(service_name='network_firewall', api_name='UpdateNetworkFirewall')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_firewall.NetworkFirewallClient(config, service_endpoint=service_endpoint)
            response = client.update_network_firewall(
                network_firewall_id=request.pop(util.camelize('networkFirewallId')),
                update_network_firewall_details=request.pop(util.camelize('UpdateNetworkFirewallDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_firewall',
            'UpdateNetworkFirewall',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_network_firewall',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ngfw_ww_grp@oracle.com" jiraProject="NGFW" opsJiraProject="JIRA-OPS"
def test_update_network_firewall_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('network_firewall', 'UpdateNetworkFirewallPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_firewall', util.camelize('network_firewall'), 'UpdateNetworkFirewallPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='network_firewall', api_name='UpdateNetworkFirewallPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_firewall.NetworkFirewallClient(config, service_endpoint=service_endpoint)
            response = client.update_network_firewall_policy(
                network_firewall_policy_id=request.pop(util.camelize('networkFirewallPolicyId')),
                update_network_firewall_policy_details=request.pop(util.camelize('UpdateNetworkFirewallPolicyDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_firewall',
            'UpdateNetworkFirewallPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_network_firewall_policy',
            False,
            False
        )
