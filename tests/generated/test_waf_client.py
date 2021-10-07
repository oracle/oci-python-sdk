# Code generated. DO NOT EDIT.
# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
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

        cassette_location = os.path.join('generated', 'waf_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="ociwaf_portal_lt_grp@oracle.com" jiraProject="WAFAPI" opsJiraProject="WAF"
def test_change_network_address_list_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('waf', 'ChangeNetworkAddressListCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waf', util.camelize('waf'), 'ChangeNetworkAddressListCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='waf', api_name='ChangeNetworkAddressListCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waf.WafClient(config, service_endpoint=service_endpoint)
            response = client.change_network_address_list_compartment(
                network_address_list_id=request.pop(util.camelize('networkAddressListId')),
                change_network_address_list_compartment_details=request.pop(util.camelize('ChangeNetworkAddressListCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waf',
            'ChangeNetworkAddressListCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_network_address_list_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="ociwaf_portal_lt_grp@oracle.com" jiraProject="WAFAPI" opsJiraProject="WAF"
def test_change_web_app_firewall_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('waf', 'ChangeWebAppFirewallCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waf', util.camelize('waf'), 'ChangeWebAppFirewallCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='waf', api_name='ChangeWebAppFirewallCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waf.WafClient(config, service_endpoint=service_endpoint)
            response = client.change_web_app_firewall_compartment(
                web_app_firewall_id=request.pop(util.camelize('webAppFirewallId')),
                change_web_app_firewall_compartment_details=request.pop(util.camelize('ChangeWebAppFirewallCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waf',
            'ChangeWebAppFirewallCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_web_app_firewall_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="ociwaf_portal_lt_grp@oracle.com" jiraProject="WAFAPI" opsJiraProject="WAF"
def test_change_web_app_firewall_policy_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('waf', 'ChangeWebAppFirewallPolicyCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waf', util.camelize('waf'), 'ChangeWebAppFirewallPolicyCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='waf', api_name='ChangeWebAppFirewallPolicyCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waf.WafClient(config, service_endpoint=service_endpoint)
            response = client.change_web_app_firewall_policy_compartment(
                web_app_firewall_policy_id=request.pop(util.camelize('webAppFirewallPolicyId')),
                change_web_app_firewall_policy_compartment_details=request.pop(util.camelize('ChangeWebAppFirewallPolicyCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waf',
            'ChangeWebAppFirewallPolicyCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_web_app_firewall_policy_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="ociwaf_portal_lt_grp@oracle.com" jiraProject="WAFAPI" opsJiraProject="WAF"
def test_create_network_address_list(testing_service_client):
    if not testing_service_client.is_api_enabled('waf', 'CreateNetworkAddressList'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waf', util.camelize('waf'), 'CreateNetworkAddressList')
    )

    request_containers = testing_service_client.get_requests(service_name='waf', api_name='CreateNetworkAddressList')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waf.WafClient(config, service_endpoint=service_endpoint)
            response = client.create_network_address_list(
                create_network_address_list_details=request.pop(util.camelize('CreateNetworkAddressListDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waf',
            'CreateNetworkAddressList',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'networkAddressList',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="ociwaf_portal_lt_grp@oracle.com" jiraProject="WAFAPI" opsJiraProject="WAF"
def test_create_web_app_firewall(testing_service_client):
    if not testing_service_client.is_api_enabled('waf', 'CreateWebAppFirewall'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waf', util.camelize('waf'), 'CreateWebAppFirewall')
    )

    request_containers = testing_service_client.get_requests(service_name='waf', api_name='CreateWebAppFirewall')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waf.WafClient(config, service_endpoint=service_endpoint)
            response = client.create_web_app_firewall(
                create_web_app_firewall_details=request.pop(util.camelize('CreateWebAppFirewallDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waf',
            'CreateWebAppFirewall',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'webAppFirewall',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="ociwaf_portal_lt_grp@oracle.com" jiraProject="WAFAPI" opsJiraProject="WAF"
def test_create_web_app_firewall_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('waf', 'CreateWebAppFirewallPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waf', util.camelize('waf'), 'CreateWebAppFirewallPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='waf', api_name='CreateWebAppFirewallPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waf.WafClient(config, service_endpoint=service_endpoint)
            response = client.create_web_app_firewall_policy(
                create_web_app_firewall_policy_details=request.pop(util.camelize('CreateWebAppFirewallPolicyDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waf',
            'CreateWebAppFirewallPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'webAppFirewallPolicy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="ociwaf_portal_lt_grp@oracle.com" jiraProject="WAFAPI" opsJiraProject="WAF"
def test_delete_network_address_list(testing_service_client):
    if not testing_service_client.is_api_enabled('waf', 'DeleteNetworkAddressList'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waf', util.camelize('waf'), 'DeleteNetworkAddressList')
    )

    request_containers = testing_service_client.get_requests(service_name='waf', api_name='DeleteNetworkAddressList')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waf.WafClient(config, service_endpoint=service_endpoint)
            response = client.delete_network_address_list(
                network_address_list_id=request.pop(util.camelize('networkAddressListId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waf',
            'DeleteNetworkAddressList',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_network_address_list',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="ociwaf_portal_lt_grp@oracle.com" jiraProject="WAFAPI" opsJiraProject="WAF"
def test_delete_web_app_firewall(testing_service_client):
    if not testing_service_client.is_api_enabled('waf', 'DeleteWebAppFirewall'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waf', util.camelize('waf'), 'DeleteWebAppFirewall')
    )

    request_containers = testing_service_client.get_requests(service_name='waf', api_name='DeleteWebAppFirewall')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waf.WafClient(config, service_endpoint=service_endpoint)
            response = client.delete_web_app_firewall(
                web_app_firewall_id=request.pop(util.camelize('webAppFirewallId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waf',
            'DeleteWebAppFirewall',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_web_app_firewall',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="ociwaf_portal_lt_grp@oracle.com" jiraProject="WAFAPI" opsJiraProject="WAF"
def test_delete_web_app_firewall_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('waf', 'DeleteWebAppFirewallPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waf', util.camelize('waf'), 'DeleteWebAppFirewallPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='waf', api_name='DeleteWebAppFirewallPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waf.WafClient(config, service_endpoint=service_endpoint)
            response = client.delete_web_app_firewall_policy(
                web_app_firewall_policy_id=request.pop(util.camelize('webAppFirewallPolicyId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waf',
            'DeleteWebAppFirewallPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_web_app_firewall_policy',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="ociwaf_portal_lt_grp@oracle.com" jiraProject="WAFAPI" opsJiraProject="WAF"
def test_get_network_address_list(testing_service_client):
    if not testing_service_client.is_api_enabled('waf', 'GetNetworkAddressList'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waf', util.camelize('waf'), 'GetNetworkAddressList')
    )

    request_containers = testing_service_client.get_requests(service_name='waf', api_name='GetNetworkAddressList')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waf.WafClient(config, service_endpoint=service_endpoint)
            response = client.get_network_address_list(
                network_address_list_id=request.pop(util.camelize('networkAddressListId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waf',
            'GetNetworkAddressList',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'networkAddressList',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="ociwaf_portal_lt_grp@oracle.com" jiraProject="WAFAPI" opsJiraProject="WAF"
def test_get_web_app_firewall(testing_service_client):
    if not testing_service_client.is_api_enabled('waf', 'GetWebAppFirewall'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waf', util.camelize('waf'), 'GetWebAppFirewall')
    )

    request_containers = testing_service_client.get_requests(service_name='waf', api_name='GetWebAppFirewall')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waf.WafClient(config, service_endpoint=service_endpoint)
            response = client.get_web_app_firewall(
                web_app_firewall_id=request.pop(util.camelize('webAppFirewallId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waf',
            'GetWebAppFirewall',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'webAppFirewall',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="ociwaf_portal_lt_grp@oracle.com" jiraProject="WAFAPI" opsJiraProject="WAF"
def test_get_web_app_firewall_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('waf', 'GetWebAppFirewallPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waf', util.camelize('waf'), 'GetWebAppFirewallPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='waf', api_name='GetWebAppFirewallPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waf.WafClient(config, service_endpoint=service_endpoint)
            response = client.get_web_app_firewall_policy(
                web_app_firewall_policy_id=request.pop(util.camelize('webAppFirewallPolicyId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waf',
            'GetWebAppFirewallPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'webAppFirewallPolicy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="ociwaf_portal_lt_grp@oracle.com" jiraProject="WAFAPI" opsJiraProject="WAF"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('waf', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waf', util.camelize('waf'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='waf', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waf.WafClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waf',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="ociwaf_portal_lt_grp@oracle.com" jiraProject="WAFAPI" opsJiraProject="WAF"
def test_list_network_address_lists(testing_service_client):
    if not testing_service_client.is_api_enabled('waf', 'ListNetworkAddressLists'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waf', util.camelize('waf'), 'ListNetworkAddressLists')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='waf', api_name='ListNetworkAddressLists')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waf.WafClient(config, service_endpoint=service_endpoint)
            response = client.list_network_address_lists(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_network_address_lists(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_network_address_lists(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waf',
            'ListNetworkAddressLists',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'networkAddressListCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="ociwaf_portal_lt_grp@oracle.com" jiraProject="WAFAPI" opsJiraProject="WAF"
def test_list_protection_capabilities(testing_service_client):
    if not testing_service_client.is_api_enabled('waf', 'ListProtectionCapabilities'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waf', util.camelize('waf'), 'ListProtectionCapabilities')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='waf', api_name='ListProtectionCapabilities')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waf.WafClient(config, service_endpoint=service_endpoint)
            response = client.list_protection_capabilities(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_protection_capabilities(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_protection_capabilities(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waf',
            'ListProtectionCapabilities',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'protectionCapabilityCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="ociwaf_portal_lt_grp@oracle.com" jiraProject="WAFAPI" opsJiraProject="WAF"
def test_list_protection_capability_group_tags(testing_service_client):
    if not testing_service_client.is_api_enabled('waf', 'ListProtectionCapabilityGroupTags'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waf', util.camelize('waf'), 'ListProtectionCapabilityGroupTags')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='waf', api_name='ListProtectionCapabilityGroupTags')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waf.WafClient(config, service_endpoint=service_endpoint)
            response = client.list_protection_capability_group_tags(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_protection_capability_group_tags(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_protection_capability_group_tags(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waf',
            'ListProtectionCapabilityGroupTags',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'protectionCapabilityGroupTagCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="ociwaf_portal_lt_grp@oracle.com" jiraProject="WAFAPI" opsJiraProject="WAF"
def test_list_web_app_firewall_policies(testing_service_client):
    if not testing_service_client.is_api_enabled('waf', 'ListWebAppFirewallPolicies'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waf', util.camelize('waf'), 'ListWebAppFirewallPolicies')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='waf', api_name='ListWebAppFirewallPolicies')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waf.WafClient(config, service_endpoint=service_endpoint)
            response = client.list_web_app_firewall_policies(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_web_app_firewall_policies(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_web_app_firewall_policies(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waf',
            'ListWebAppFirewallPolicies',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'webAppFirewallPolicyCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="ociwaf_portal_lt_grp@oracle.com" jiraProject="WAFAPI" opsJiraProject="WAF"
def test_list_web_app_firewalls(testing_service_client):
    if not testing_service_client.is_api_enabled('waf', 'ListWebAppFirewalls'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waf', util.camelize('waf'), 'ListWebAppFirewalls')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='waf', api_name='ListWebAppFirewalls')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waf.WafClient(config, service_endpoint=service_endpoint)
            response = client.list_web_app_firewalls(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_web_app_firewalls(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_web_app_firewalls(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waf',
            'ListWebAppFirewalls',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'webAppFirewallCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="ociwaf_portal_lt_grp@oracle.com" jiraProject="WAFAPI" opsJiraProject="WAF"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('waf', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waf', util.camelize('waf'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='waf', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waf.WafClient(config, service_endpoint=service_endpoint)
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
            'waf',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestErrorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="ociwaf_portal_lt_grp@oracle.com" jiraProject="WAFAPI" opsJiraProject="WAF"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('waf', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waf', util.camelize('waf'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='waf', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waf.WafClient(config, service_endpoint=service_endpoint)
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
            'waf',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="ociwaf_portal_lt_grp@oracle.com" jiraProject="WAFAPI" opsJiraProject="WAF"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('waf', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waf', util.camelize('waf'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='waf', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waf.WafClient(config, service_endpoint=service_endpoint)
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
            'waf',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="ociwaf_portal_lt_grp@oracle.com" jiraProject="WAFAPI" opsJiraProject="WAF"
def test_update_network_address_list(testing_service_client):
    if not testing_service_client.is_api_enabled('waf', 'UpdateNetworkAddressList'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waf', util.camelize('waf'), 'UpdateNetworkAddressList')
    )

    request_containers = testing_service_client.get_requests(service_name='waf', api_name='UpdateNetworkAddressList')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waf.WafClient(config, service_endpoint=service_endpoint)
            response = client.update_network_address_list(
                network_address_list_id=request.pop(util.camelize('networkAddressListId')),
                update_network_address_list_details=request.pop(util.camelize('UpdateNetworkAddressListDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waf',
            'UpdateNetworkAddressList',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_network_address_list',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="ociwaf_portal_lt_grp@oracle.com" jiraProject="WAFAPI" opsJiraProject="WAF"
def test_update_web_app_firewall(testing_service_client):
    if not testing_service_client.is_api_enabled('waf', 'UpdateWebAppFirewall'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waf', util.camelize('waf'), 'UpdateWebAppFirewall')
    )

    request_containers = testing_service_client.get_requests(service_name='waf', api_name='UpdateWebAppFirewall')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waf.WafClient(config, service_endpoint=service_endpoint)
            response = client.update_web_app_firewall(
                web_app_firewall_id=request.pop(util.camelize('webAppFirewallId')),
                update_web_app_firewall_details=request.pop(util.camelize('UpdateWebAppFirewallDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waf',
            'UpdateWebAppFirewall',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_web_app_firewall',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="ociwaf_portal_lt_grp@oracle.com" jiraProject="WAFAPI" opsJiraProject="WAF"
def test_update_web_app_firewall_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('waf', 'UpdateWebAppFirewallPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waf', util.camelize('waf'), 'UpdateWebAppFirewallPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='waf', api_name='UpdateWebAppFirewallPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waf.WafClient(config, service_endpoint=service_endpoint)
            response = client.update_web_app_firewall_policy(
                web_app_firewall_policy_id=request.pop(util.camelize('webAppFirewallPolicyId')),
                update_web_app_firewall_policy_details=request.pop(util.camelize('UpdateWebAppFirewallPolicyDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waf',
            'UpdateWebAppFirewallPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_web_app_firewall_policy',
            False,
            False
        )
