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

        cassette_location = os.path.join('generated', 'waa_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="ociwaa_portal_lt_grp@oracle.com" jiraProject="WAAAPI" opsJiraProject="WAA"
def test_change_web_app_acceleration_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('waa', 'ChangeWebAppAccelerationCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waa', util.camelize('waa'), 'ChangeWebAppAccelerationCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='waa', api_name='ChangeWebAppAccelerationCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waa.WaaClient(config, service_endpoint=service_endpoint)
            response = client.change_web_app_acceleration_compartment(
                web_app_acceleration_id=request.pop(util.camelize('webAppAccelerationId')),
                change_web_app_acceleration_compartment_details=request.pop(util.camelize('ChangeWebAppAccelerationCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waa',
            'ChangeWebAppAccelerationCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_web_app_acceleration_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="ociwaa_portal_lt_grp@oracle.com" jiraProject="WAAAPI" opsJiraProject="WAA"
def test_change_web_app_acceleration_policy_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('waa', 'ChangeWebAppAccelerationPolicyCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waa', util.camelize('waa'), 'ChangeWebAppAccelerationPolicyCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='waa', api_name='ChangeWebAppAccelerationPolicyCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waa.WaaClient(config, service_endpoint=service_endpoint)
            response = client.change_web_app_acceleration_policy_compartment(
                web_app_acceleration_policy_id=request.pop(util.camelize('webAppAccelerationPolicyId')),
                change_web_app_acceleration_policy_compartment_details=request.pop(util.camelize('ChangeWebAppAccelerationPolicyCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waa',
            'ChangeWebAppAccelerationPolicyCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_web_app_acceleration_policy_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="ociwaa_portal_lt_grp@oracle.com" jiraProject="WAAAPI" opsJiraProject="WAA"
def test_create_web_app_acceleration(testing_service_client):
    if not testing_service_client.is_api_enabled('waa', 'CreateWebAppAcceleration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waa', util.camelize('waa'), 'CreateWebAppAcceleration')
    )

    request_containers = testing_service_client.get_requests(service_name='waa', api_name='CreateWebAppAcceleration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waa.WaaClient(config, service_endpoint=service_endpoint)
            response = client.create_web_app_acceleration(
                create_web_app_acceleration_details=request.pop(util.camelize('CreateWebAppAccelerationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waa',
            'CreateWebAppAcceleration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'webAppAcceleration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="ociwaa_portal_lt_grp@oracle.com" jiraProject="WAAAPI" opsJiraProject="WAA"
def test_create_web_app_acceleration_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('waa', 'CreateWebAppAccelerationPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waa', util.camelize('waa'), 'CreateWebAppAccelerationPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='waa', api_name='CreateWebAppAccelerationPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waa.WaaClient(config, service_endpoint=service_endpoint)
            response = client.create_web_app_acceleration_policy(
                create_web_app_acceleration_policy_details=request.pop(util.camelize('CreateWebAppAccelerationPolicyDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waa',
            'CreateWebAppAccelerationPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'webAppAccelerationPolicy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="ociwaa_portal_lt_grp@oracle.com" jiraProject="WAAAPI" opsJiraProject="WAA"
def test_delete_web_app_acceleration(testing_service_client):
    if not testing_service_client.is_api_enabled('waa', 'DeleteWebAppAcceleration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waa', util.camelize('waa'), 'DeleteWebAppAcceleration')
    )

    request_containers = testing_service_client.get_requests(service_name='waa', api_name='DeleteWebAppAcceleration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waa.WaaClient(config, service_endpoint=service_endpoint)
            response = client.delete_web_app_acceleration(
                web_app_acceleration_id=request.pop(util.camelize('webAppAccelerationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waa',
            'DeleteWebAppAcceleration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_web_app_acceleration',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="ociwaa_portal_lt_grp@oracle.com" jiraProject="WAAAPI" opsJiraProject="WAA"
def test_delete_web_app_acceleration_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('waa', 'DeleteWebAppAccelerationPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waa', util.camelize('waa'), 'DeleteWebAppAccelerationPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='waa', api_name='DeleteWebAppAccelerationPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waa.WaaClient(config, service_endpoint=service_endpoint)
            response = client.delete_web_app_acceleration_policy(
                web_app_acceleration_policy_id=request.pop(util.camelize('webAppAccelerationPolicyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waa',
            'DeleteWebAppAccelerationPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_web_app_acceleration_policy',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="ociwaa_portal_lt_grp@oracle.com" jiraProject="WAAAPI" opsJiraProject="WAA"
def test_get_web_app_acceleration(testing_service_client):
    if not testing_service_client.is_api_enabled('waa', 'GetWebAppAcceleration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waa', util.camelize('waa'), 'GetWebAppAcceleration')
    )

    request_containers = testing_service_client.get_requests(service_name='waa', api_name='GetWebAppAcceleration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waa.WaaClient(config, service_endpoint=service_endpoint)
            response = client.get_web_app_acceleration(
                web_app_acceleration_id=request.pop(util.camelize('webAppAccelerationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waa',
            'GetWebAppAcceleration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'webAppAcceleration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="ociwaa_portal_lt_grp@oracle.com" jiraProject="WAAAPI" opsJiraProject="WAA"
def test_get_web_app_acceleration_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('waa', 'GetWebAppAccelerationPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waa', util.camelize('waa'), 'GetWebAppAccelerationPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='waa', api_name='GetWebAppAccelerationPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waa.WaaClient(config, service_endpoint=service_endpoint)
            response = client.get_web_app_acceleration_policy(
                web_app_acceleration_policy_id=request.pop(util.camelize('webAppAccelerationPolicyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waa',
            'GetWebAppAccelerationPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'webAppAccelerationPolicy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="ociwaa_portal_lt_grp@oracle.com" jiraProject="WAAAPI" opsJiraProject="WAA"
def test_list_web_app_acceleration_policies(testing_service_client):
    if not testing_service_client.is_api_enabled('waa', 'ListWebAppAccelerationPolicies'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waa', util.camelize('waa'), 'ListWebAppAccelerationPolicies')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='waa', api_name='ListWebAppAccelerationPolicies')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waa.WaaClient(config, service_endpoint=service_endpoint)
            response = client.list_web_app_acceleration_policies(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_web_app_acceleration_policies(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_web_app_acceleration_policies(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waa',
            'ListWebAppAccelerationPolicies',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'webAppAccelerationPolicyCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="ociwaa_portal_lt_grp@oracle.com" jiraProject="WAAAPI" opsJiraProject="WAA"
def test_list_web_app_accelerations(testing_service_client):
    if not testing_service_client.is_api_enabled('waa', 'ListWebAppAccelerations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waa', util.camelize('waa'), 'ListWebAppAccelerations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='waa', api_name='ListWebAppAccelerations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waa.WaaClient(config, service_endpoint=service_endpoint)
            response = client.list_web_app_accelerations(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_web_app_accelerations(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_web_app_accelerations(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waa',
            'ListWebAppAccelerations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'webAppAccelerationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="ociwaa_portal_lt_grp@oracle.com" jiraProject="WAAAPI" opsJiraProject="WAA"
def test_purge_web_app_acceleration_cache(testing_service_client):
    if not testing_service_client.is_api_enabled('waa', 'PurgeWebAppAccelerationCache'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waa', util.camelize('waa'), 'PurgeWebAppAccelerationCache')
    )

    request_containers = testing_service_client.get_requests(service_name='waa', api_name='PurgeWebAppAccelerationCache')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waa.WaaClient(config, service_endpoint=service_endpoint)
            response = client.purge_web_app_acceleration_cache(
                web_app_acceleration_id=request.pop(util.camelize('webAppAccelerationId')),
                purge_web_app_acceleration_cache_details=request.pop(util.camelize('PurgeWebAppAccelerationCacheDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waa',
            'PurgeWebAppAccelerationCache',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'purge_web_app_acceleration_cache',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="ociwaa_portal_lt_grp@oracle.com" jiraProject="WAAAPI" opsJiraProject="WAA"
def test_update_web_app_acceleration(testing_service_client):
    if not testing_service_client.is_api_enabled('waa', 'UpdateWebAppAcceleration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waa', util.camelize('waa'), 'UpdateWebAppAcceleration')
    )

    request_containers = testing_service_client.get_requests(service_name='waa', api_name='UpdateWebAppAcceleration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waa.WaaClient(config, service_endpoint=service_endpoint)
            response = client.update_web_app_acceleration(
                web_app_acceleration_id=request.pop(util.camelize('webAppAccelerationId')),
                update_web_app_acceleration_details=request.pop(util.camelize('UpdateWebAppAccelerationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waa',
            'UpdateWebAppAcceleration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_web_app_acceleration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="ociwaa_portal_lt_grp@oracle.com" jiraProject="WAAAPI" opsJiraProject="WAA"
def test_update_web_app_acceleration_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('waa', 'UpdateWebAppAccelerationPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waa', util.camelize('waa'), 'UpdateWebAppAccelerationPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='waa', api_name='UpdateWebAppAccelerationPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waa.WaaClient(config, service_endpoint=service_endpoint)
            response = client.update_web_app_acceleration_policy(
                web_app_acceleration_policy_id=request.pop(util.camelize('webAppAccelerationPolicyId')),
                update_web_app_acceleration_policy_details=request.pop(util.camelize('UpdateWebAppAccelerationPolicyDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waa',
            'UpdateWebAppAccelerationPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_web_app_acceleration_policy',
            False,
            False
        )
