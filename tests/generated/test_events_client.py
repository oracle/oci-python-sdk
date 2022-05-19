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

        cassette_location = os.path.join('generated', 'events_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="oci_events_dev_grp@oracle.com" jiraProject="https://jira.oci.oraclecorp.com/projects/CLEV" opsJiraProject="https://jira-sd.mc1.oracleiaas.com/projects/CLEV"
def test_change_rule_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('events', 'ChangeRuleCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('events', util.camelize('events'), 'ChangeRuleCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='events', api_name='ChangeRuleCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.events.EventsClient(config, service_endpoint=service_endpoint)
            response = client.change_rule_compartment(
                rule_id=request.pop(util.camelize('ruleId')),
                change_rule_compartment_details=request.pop(util.camelize('ChangeRuleCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'events',
            'ChangeRuleCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_rule_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_events_dev_grp@oracle.com" jiraProject="https://jira.oci.oraclecorp.com/projects/CLEV" opsJiraProject="https://jira-sd.mc1.oracleiaas.com/projects/CLEV"
def test_create_rule(testing_service_client):
    if not testing_service_client.is_api_enabled('events', 'CreateRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('events', util.camelize('events'), 'CreateRule')
    )

    request_containers = testing_service_client.get_requests(service_name='events', api_name='CreateRule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.events.EventsClient(config, service_endpoint=service_endpoint)
            response = client.create_rule(
                create_rule_details=request.pop(util.camelize('CreateRuleDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'events',
            'CreateRule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'rule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_events_dev_grp@oracle.com" jiraProject="https://jira.oci.oraclecorp.com/projects/CLEV" opsJiraProject="https://jira-sd.mc1.oracleiaas.com/projects/CLEV"
def test_delete_rule(testing_service_client):
    if not testing_service_client.is_api_enabled('events', 'DeleteRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('events', util.camelize('events'), 'DeleteRule')
    )

    request_containers = testing_service_client.get_requests(service_name='events', api_name='DeleteRule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.events.EventsClient(config, service_endpoint=service_endpoint)
            response = client.delete_rule(
                rule_id=request.pop(util.camelize('ruleId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'events',
            'DeleteRule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_rule',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_events_dev_grp@oracle.com" jiraProject="https://jira.oci.oraclecorp.com/projects/CLEV" opsJiraProject="https://jira-sd.mc1.oracleiaas.com/projects/CLEV"
def test_get_rule(testing_service_client):
    if not testing_service_client.is_api_enabled('events', 'GetRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('events', util.camelize('events'), 'GetRule')
    )

    request_containers = testing_service_client.get_requests(service_name='events', api_name='GetRule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.events.EventsClient(config, service_endpoint=service_endpoint)
            response = client.get_rule(
                rule_id=request.pop(util.camelize('ruleId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'events',
            'GetRule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'rule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_events_dev_grp@oracle.com" jiraProject="https://jira.oci.oraclecorp.com/projects/CLEV" opsJiraProject="https://jira-sd.mc1.oracleiaas.com/projects/CLEV"
def test_list_rules(testing_service_client):
    if not testing_service_client.is_api_enabled('events', 'ListRules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('events', util.camelize('events'), 'ListRules')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='events', api_name='ListRules')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.events.EventsClient(config, service_endpoint=service_endpoint)
            response = client.list_rules(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_rules(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_rules(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'events',
            'ListRules',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'ruleSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_events_dev_grp@oracle.com" jiraProject="https://jira.oci.oraclecorp.com/projects/CLEV" opsJiraProject="https://jira-sd.mc1.oracleiaas.com/projects/CLEV"
def test_update_rule(testing_service_client):
    if not testing_service_client.is_api_enabled('events', 'UpdateRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('events', util.camelize('events'), 'UpdateRule')
    )

    request_containers = testing_service_client.get_requests(service_name='events', api_name='UpdateRule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.events.EventsClient(config, service_endpoint=service_endpoint)
            response = client.update_rule(
                rule_id=request.pop(util.camelize('ruleId')),
                update_rule_details=request.pop(util.camelize('UpdateRuleDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'events',
            'UpdateRule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'rule',
            False,
            False
        )
