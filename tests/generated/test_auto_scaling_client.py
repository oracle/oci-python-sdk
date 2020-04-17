# Code generated. DO NOT EDIT.
# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
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

        cassette_location = os.path.join('generated', 'autoscaling_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="instance_dev_us_grp@oracle.com" jiraProject="CIM" opsJiraProject="COM"
def test_change_auto_scaling_configuration_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('autoscaling', 'ChangeAutoScalingConfigurationCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('autoscaling', util.camelize('auto_scaling'), 'ChangeAutoScalingConfigurationCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='autoscaling', api_name='ChangeAutoScalingConfigurationCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.autoscaling.AutoScalingClient(config, service_endpoint=service_endpoint)
            response = client.change_auto_scaling_configuration_compartment(
                auto_scaling_configuration_id=request.pop(util.camelize('autoScalingConfigurationId')),
                change_compartment_details=request.pop(util.camelize('ChangeCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'autoscaling',
            'ChangeAutoScalingConfigurationCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_auto_scaling_configuration_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="instance_dev_us_grp@oracle.com" jiraProject="CIM" opsJiraProject="COM"
def test_create_auto_scaling_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('autoscaling', 'CreateAutoScalingConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('autoscaling', util.camelize('auto_scaling'), 'CreateAutoScalingConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='autoscaling', api_name='CreateAutoScalingConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.autoscaling.AutoScalingClient(config, service_endpoint=service_endpoint)
            response = client.create_auto_scaling_configuration(
                create_auto_scaling_configuration_details=request.pop(util.camelize('CreateAutoScalingConfigurationDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'autoscaling',
            'CreateAutoScalingConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autoScalingConfiguration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="instance_dev_us_grp@oracle.com" jiraProject="CIM" opsJiraProject="COM"
def test_create_auto_scaling_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('autoscaling', 'CreateAutoScalingPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('autoscaling', util.camelize('auto_scaling'), 'CreateAutoScalingPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='autoscaling', api_name='CreateAutoScalingPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.autoscaling.AutoScalingClient(config, service_endpoint=service_endpoint)
            response = client.create_auto_scaling_policy(
                auto_scaling_configuration_id=request.pop(util.camelize('autoScalingConfigurationId')),
                create_auto_scaling_policy_details=request.pop(util.camelize('CreateAutoScalingPolicyDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'autoscaling',
            'CreateAutoScalingPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autoScalingPolicy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="instance_dev_us_grp@oracle.com" jiraProject="CIM" opsJiraProject="COM"
def test_delete_auto_scaling_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('autoscaling', 'DeleteAutoScalingConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('autoscaling', util.camelize('auto_scaling'), 'DeleteAutoScalingConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='autoscaling', api_name='DeleteAutoScalingConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.autoscaling.AutoScalingClient(config, service_endpoint=service_endpoint)
            response = client.delete_auto_scaling_configuration(
                auto_scaling_configuration_id=request.pop(util.camelize('autoScalingConfigurationId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'autoscaling',
            'DeleteAutoScalingConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_auto_scaling_configuration',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="instance_dev_us_grp@oracle.com" jiraProject="CIM" opsJiraProject="COM"
def test_delete_auto_scaling_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('autoscaling', 'DeleteAutoScalingPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('autoscaling', util.camelize('auto_scaling'), 'DeleteAutoScalingPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='autoscaling', api_name='DeleteAutoScalingPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.autoscaling.AutoScalingClient(config, service_endpoint=service_endpoint)
            response = client.delete_auto_scaling_policy(
                auto_scaling_configuration_id=request.pop(util.camelize('autoScalingConfigurationId')),
                auto_scaling_policy_id=request.pop(util.camelize('autoScalingPolicyId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'autoscaling',
            'DeleteAutoScalingPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_auto_scaling_policy',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="instance_dev_us_grp@oracle.com" jiraProject="CIM" opsJiraProject="COM"
def test_get_auto_scaling_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('autoscaling', 'GetAutoScalingConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('autoscaling', util.camelize('auto_scaling'), 'GetAutoScalingConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='autoscaling', api_name='GetAutoScalingConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.autoscaling.AutoScalingClient(config, service_endpoint=service_endpoint)
            response = client.get_auto_scaling_configuration(
                auto_scaling_configuration_id=request.pop(util.camelize('autoScalingConfigurationId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'autoscaling',
            'GetAutoScalingConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autoScalingConfiguration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="instance_dev_us_grp@oracle.com" jiraProject="CIM" opsJiraProject="COM"
def test_get_auto_scaling_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('autoscaling', 'GetAutoScalingPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('autoscaling', util.camelize('auto_scaling'), 'GetAutoScalingPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='autoscaling', api_name='GetAutoScalingPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.autoscaling.AutoScalingClient(config, service_endpoint=service_endpoint)
            response = client.get_auto_scaling_policy(
                auto_scaling_configuration_id=request.pop(util.camelize('autoScalingConfigurationId')),
                auto_scaling_policy_id=request.pop(util.camelize('autoScalingPolicyId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'autoscaling',
            'GetAutoScalingPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autoScalingPolicy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="instance_dev_us_grp@oracle.com" jiraProject="CIM" opsJiraProject="COM"
def test_list_auto_scaling_configurations(testing_service_client):
    if not testing_service_client.is_api_enabled('autoscaling', 'ListAutoScalingConfigurations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('autoscaling', util.camelize('auto_scaling'), 'ListAutoScalingConfigurations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='autoscaling', api_name='ListAutoScalingConfigurations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.autoscaling.AutoScalingClient(config, service_endpoint=service_endpoint)
            response = client.list_auto_scaling_configurations(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_auto_scaling_configurations(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_auto_scaling_configurations(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'autoscaling',
            'ListAutoScalingConfigurations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autoScalingConfigurationSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="instance_dev_us_grp@oracle.com" jiraProject="CIM" opsJiraProject="COM"
def test_list_auto_scaling_policies(testing_service_client):
    if not testing_service_client.is_api_enabled('autoscaling', 'ListAutoScalingPolicies'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('autoscaling', util.camelize('auto_scaling'), 'ListAutoScalingPolicies')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='autoscaling', api_name='ListAutoScalingPolicies')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.autoscaling.AutoScalingClient(config, service_endpoint=service_endpoint)
            response = client.list_auto_scaling_policies(
                auto_scaling_configuration_id=request.pop(util.camelize('autoScalingConfigurationId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_auto_scaling_policies(
                    auto_scaling_configuration_id=request.pop(util.camelize('autoScalingConfigurationId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_auto_scaling_policies(
                        auto_scaling_configuration_id=request.pop(util.camelize('autoScalingConfigurationId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'autoscaling',
            'ListAutoScalingPolicies',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autoScalingPolicySummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="instance_dev_us_grp@oracle.com" jiraProject="CIM" opsJiraProject="COM"
def test_update_auto_scaling_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('autoscaling', 'UpdateAutoScalingConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('autoscaling', util.camelize('auto_scaling'), 'UpdateAutoScalingConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='autoscaling', api_name='UpdateAutoScalingConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.autoscaling.AutoScalingClient(config, service_endpoint=service_endpoint)
            response = client.update_auto_scaling_configuration(
                auto_scaling_configuration_id=request.pop(util.camelize('autoScalingConfigurationId')),
                update_auto_scaling_configuration_details=request.pop(util.camelize('UpdateAutoScalingConfigurationDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'autoscaling',
            'UpdateAutoScalingConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autoScalingConfiguration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="instance_dev_us_grp@oracle.com" jiraProject="CIM" opsJiraProject="COM"
def test_update_auto_scaling_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('autoscaling', 'UpdateAutoScalingPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('autoscaling', util.camelize('auto_scaling'), 'UpdateAutoScalingPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='autoscaling', api_name='UpdateAutoScalingPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.autoscaling.AutoScalingClient(config, service_endpoint=service_endpoint)
            response = client.update_auto_scaling_policy(
                auto_scaling_configuration_id=request.pop(util.camelize('autoScalingConfigurationId')),
                auto_scaling_policy_id=request.pop(util.camelize('autoScalingPolicyId')),
                update_auto_scaling_policy_details=request.pop(util.camelize('UpdateAutoScalingPolicyDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'autoscaling',
            'UpdateAutoScalingPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autoScalingPolicy',
            False,
            False
        )
