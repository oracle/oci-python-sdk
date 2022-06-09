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

        cassette_location = os.path.join('generated', 'governance_rules_control_plane_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="acc_customer_tools_us_grp@oracle.com" jiraProject="ACCMGMT" opsJiraProject="ACCMGMT"
def test_create_governance_rule(testing_service_client):
    if not testing_service_client.is_api_enabled('governance_rules_control_plane', 'CreateGovernanceRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('governance_rules_control_plane', util.camelize('governance_rule'), 'CreateGovernanceRule')
    )

    request_containers = testing_service_client.get_requests(service_name='governance_rules_control_plane', api_name='CreateGovernanceRule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.governance_rules_control_plane.GovernanceRuleClient(config, service_endpoint=service_endpoint)
            response = client.create_governance_rule(
                create_governance_rule_details=request.pop(util.camelize('CreateGovernanceRuleDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'governance_rules_control_plane',
            'CreateGovernanceRule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'governanceRule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="acc_customer_tools_us_grp@oracle.com" jiraProject="ACCMGMT" opsJiraProject="ACCMGMT"
def test_create_inclusion_criterion(testing_service_client):
    if not testing_service_client.is_api_enabled('governance_rules_control_plane', 'CreateInclusionCriterion'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('governance_rules_control_plane', util.camelize('governance_rule'), 'CreateInclusionCriterion')
    )

    request_containers = testing_service_client.get_requests(service_name='governance_rules_control_plane', api_name='CreateInclusionCriterion')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.governance_rules_control_plane.GovernanceRuleClient(config, service_endpoint=service_endpoint)
            response = client.create_inclusion_criterion(
                create_inclusion_criterion_details=request.pop(util.camelize('CreateInclusionCriterionDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'governance_rules_control_plane',
            'CreateInclusionCriterion',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'inclusionCriterion',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="acc_customer_tools_us_grp@oracle.com" jiraProject="ACCMGMT" opsJiraProject="ACCMGMT"
def test_delete_governance_rule(testing_service_client):
    if not testing_service_client.is_api_enabled('governance_rules_control_plane', 'DeleteGovernanceRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('governance_rules_control_plane', util.camelize('governance_rule'), 'DeleteGovernanceRule')
    )

    request_containers = testing_service_client.get_requests(service_name='governance_rules_control_plane', api_name='DeleteGovernanceRule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.governance_rules_control_plane.GovernanceRuleClient(config, service_endpoint=service_endpoint)
            response = client.delete_governance_rule(
                governance_rule_id=request.pop(util.camelize('governanceRuleId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'governance_rules_control_plane',
            'DeleteGovernanceRule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_governance_rule',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="acc_customer_tools_us_grp@oracle.com" jiraProject="ACCMGMT" opsJiraProject="ACCMGMT"
def test_delete_inclusion_criterion(testing_service_client):
    if not testing_service_client.is_api_enabled('governance_rules_control_plane', 'DeleteInclusionCriterion'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('governance_rules_control_plane', util.camelize('governance_rule'), 'DeleteInclusionCriterion')
    )

    request_containers = testing_service_client.get_requests(service_name='governance_rules_control_plane', api_name='DeleteInclusionCriterion')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.governance_rules_control_plane.GovernanceRuleClient(config, service_endpoint=service_endpoint)
            response = client.delete_inclusion_criterion(
                inclusion_criterion_id=request.pop(util.camelize('inclusionCriterionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'governance_rules_control_plane',
            'DeleteInclusionCriterion',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_inclusion_criterion',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="acc_customer_tools_us_grp@oracle.com" jiraProject="ACCMGMT" opsJiraProject="ACCMGMT"
def test_get_enforced_governance_rule(testing_service_client):
    if not testing_service_client.is_api_enabled('governance_rules_control_plane', 'GetEnforcedGovernanceRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('governance_rules_control_plane', util.camelize('governance_rule'), 'GetEnforcedGovernanceRule')
    )

    request_containers = testing_service_client.get_requests(service_name='governance_rules_control_plane', api_name='GetEnforcedGovernanceRule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.governance_rules_control_plane.GovernanceRuleClient(config, service_endpoint=service_endpoint)
            response = client.get_enforced_governance_rule(
                enforced_governance_rule_id=request.pop(util.camelize('enforcedGovernanceRuleId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'governance_rules_control_plane',
            'GetEnforcedGovernanceRule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'enforcedGovernanceRule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="acc_customer_tools_us_grp@oracle.com" jiraProject="ACCMGMT" opsJiraProject="ACCMGMT"
def test_get_governance_rule(testing_service_client):
    if not testing_service_client.is_api_enabled('governance_rules_control_plane', 'GetGovernanceRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('governance_rules_control_plane', util.camelize('governance_rule'), 'GetGovernanceRule')
    )

    request_containers = testing_service_client.get_requests(service_name='governance_rules_control_plane', api_name='GetGovernanceRule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.governance_rules_control_plane.GovernanceRuleClient(config, service_endpoint=service_endpoint)
            response = client.get_governance_rule(
                governance_rule_id=request.pop(util.camelize('governanceRuleId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'governance_rules_control_plane',
            'GetGovernanceRule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'governanceRule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="acc_customer_tools_us_grp@oracle.com" jiraProject="ACCMGMT" opsJiraProject="ACCMGMT"
def test_get_inclusion_criterion(testing_service_client):
    if not testing_service_client.is_api_enabled('governance_rules_control_plane', 'GetInclusionCriterion'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('governance_rules_control_plane', util.camelize('governance_rule'), 'GetInclusionCriterion')
    )

    request_containers = testing_service_client.get_requests(service_name='governance_rules_control_plane', api_name='GetInclusionCriterion')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.governance_rules_control_plane.GovernanceRuleClient(config, service_endpoint=service_endpoint)
            response = client.get_inclusion_criterion(
                inclusion_criterion_id=request.pop(util.camelize('inclusionCriterionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'governance_rules_control_plane',
            'GetInclusionCriterion',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'inclusionCriterion',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="acc_customer_tools_us_grp@oracle.com" jiraProject="ACCMGMT" opsJiraProject="ACCMGMT"
def test_get_tenancy_attachment(testing_service_client):
    if not testing_service_client.is_api_enabled('governance_rules_control_plane', 'GetTenancyAttachment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('governance_rules_control_plane', util.camelize('governance_rule'), 'GetTenancyAttachment')
    )

    request_containers = testing_service_client.get_requests(service_name='governance_rules_control_plane', api_name='GetTenancyAttachment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.governance_rules_control_plane.GovernanceRuleClient(config, service_endpoint=service_endpoint)
            response = client.get_tenancy_attachment(
                tenancy_attachment_id=request.pop(util.camelize('tenancyAttachmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'governance_rules_control_plane',
            'GetTenancyAttachment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'tenancyAttachment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="acc_customer_tools_us_grp@oracle.com" jiraProject="ACCMGMT" opsJiraProject="ACCMGMT"
def test_list_enforced_governance_rules(testing_service_client):
    if not testing_service_client.is_api_enabled('governance_rules_control_plane', 'ListEnforcedGovernanceRules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('governance_rules_control_plane', util.camelize('governance_rule'), 'ListEnforcedGovernanceRules')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='governance_rules_control_plane', api_name='ListEnforcedGovernanceRules')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.governance_rules_control_plane.GovernanceRuleClient(config, service_endpoint=service_endpoint)
            response = client.list_enforced_governance_rules(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_enforced_governance_rules(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_enforced_governance_rules(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'governance_rules_control_plane',
            'ListEnforcedGovernanceRules',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'enforcedGovernanceRuleCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="acc_customer_tools_us_grp@oracle.com" jiraProject="ACCMGMT" opsJiraProject="ACCMGMT"
def test_list_governance_rules(testing_service_client):
    if not testing_service_client.is_api_enabled('governance_rules_control_plane', 'ListGovernanceRules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('governance_rules_control_plane', util.camelize('governance_rule'), 'ListGovernanceRules')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='governance_rules_control_plane', api_name='ListGovernanceRules')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.governance_rules_control_plane.GovernanceRuleClient(config, service_endpoint=service_endpoint)
            response = client.list_governance_rules(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_governance_rules(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_governance_rules(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'governance_rules_control_plane',
            'ListGovernanceRules',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'governanceRuleCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="acc_customer_tools_us_grp@oracle.com" jiraProject="ACCMGMT" opsJiraProject="ACCMGMT"
def test_list_inclusion_criteria(testing_service_client):
    if not testing_service_client.is_api_enabled('governance_rules_control_plane', 'ListInclusionCriteria'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('governance_rules_control_plane', util.camelize('governance_rule'), 'ListInclusionCriteria')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='governance_rules_control_plane', api_name='ListInclusionCriteria')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.governance_rules_control_plane.GovernanceRuleClient(config, service_endpoint=service_endpoint)
            response = client.list_inclusion_criteria(
                governance_rule_id=request.pop(util.camelize('governanceRuleId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_inclusion_criteria(
                    governance_rule_id=request.pop(util.camelize('governanceRuleId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_inclusion_criteria(
                        governance_rule_id=request.pop(util.camelize('governanceRuleId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'governance_rules_control_plane',
            'ListInclusionCriteria',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'inclusionCriterionCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="acc_customer_tools_us_grp@oracle.com" jiraProject="ACCMGMT" opsJiraProject="ACCMGMT"
def test_list_tenancy_attachments(testing_service_client):
    if not testing_service_client.is_api_enabled('governance_rules_control_plane', 'ListTenancyAttachments'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('governance_rules_control_plane', util.camelize('governance_rule'), 'ListTenancyAttachments')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='governance_rules_control_plane', api_name='ListTenancyAttachments')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.governance_rules_control_plane.GovernanceRuleClient(config, service_endpoint=service_endpoint)
            response = client.list_tenancy_attachments(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_tenancy_attachments(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_tenancy_attachments(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'governance_rules_control_plane',
            'ListTenancyAttachments',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'tenancyAttachmentCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="acc_customer_tools_us_grp@oracle.com" jiraProject="ACCMGMT" opsJiraProject="ACCMGMT"
def test_retry_governance_rule(testing_service_client):
    if not testing_service_client.is_api_enabled('governance_rules_control_plane', 'RetryGovernanceRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('governance_rules_control_plane', util.camelize('governance_rule'), 'RetryGovernanceRule')
    )

    request_containers = testing_service_client.get_requests(service_name='governance_rules_control_plane', api_name='RetryGovernanceRule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.governance_rules_control_plane.GovernanceRuleClient(config, service_endpoint=service_endpoint)
            response = client.retry_governance_rule(
                governance_rule_id=request.pop(util.camelize('governanceRuleId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'governance_rules_control_plane',
            'RetryGovernanceRule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'retry_governance_rule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="acc_customer_tools_us_grp@oracle.com" jiraProject="ACCMGMT" opsJiraProject="ACCMGMT"
def test_retry_tenancy_attachment(testing_service_client):
    if not testing_service_client.is_api_enabled('governance_rules_control_plane', 'RetryTenancyAttachment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('governance_rules_control_plane', util.camelize('governance_rule'), 'RetryTenancyAttachment')
    )

    request_containers = testing_service_client.get_requests(service_name='governance_rules_control_plane', api_name='RetryTenancyAttachment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.governance_rules_control_plane.GovernanceRuleClient(config, service_endpoint=service_endpoint)
            response = client.retry_tenancy_attachment(
                tenancy_attachment_id=request.pop(util.camelize('tenancyAttachmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'governance_rules_control_plane',
            'RetryTenancyAttachment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'retry_tenancy_attachment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="acc_customer_tools_us_grp@oracle.com" jiraProject="ACCMGMT" opsJiraProject="ACCMGMT"
def test_update_governance_rule(testing_service_client):
    if not testing_service_client.is_api_enabled('governance_rules_control_plane', 'UpdateGovernanceRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('governance_rules_control_plane', util.camelize('governance_rule'), 'UpdateGovernanceRule')
    )

    request_containers = testing_service_client.get_requests(service_name='governance_rules_control_plane', api_name='UpdateGovernanceRule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.governance_rules_control_plane.GovernanceRuleClient(config, service_endpoint=service_endpoint)
            response = client.update_governance_rule(
                governance_rule_id=request.pop(util.camelize('governanceRuleId')),
                update_governance_rule_details=request.pop(util.camelize('UpdateGovernanceRuleDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'governance_rules_control_plane',
            'UpdateGovernanceRule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_governance_rule',
            False,
            False
        )
