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

        cassette_location = os.path.join('generated', 'fusion_apps_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="fa-control-plane_us_grp@oracle.com" jiraProject="FACP" opsJiraProject="FACP"
def test_change_fusion_environment_family_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('fusion_apps', 'ChangeFusionEnvironmentFamilyCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fusion_apps', util.camelize('fusion_environment_family'), 'ChangeFusionEnvironmentFamilyCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='fusion_apps', api_name='ChangeFusionEnvironmentFamilyCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fusion_apps.FusionEnvironmentFamilyClient(config, service_endpoint=service_endpoint)
            response = client.change_fusion_environment_family_compartment(
                fusion_environment_family_id=request.pop(util.camelize('fusionEnvironmentFamilyId')),
                change_fusion_environment_family_compartment_details=request.pop(util.camelize('ChangeFusionEnvironmentFamilyCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fusion_apps',
            'ChangeFusionEnvironmentFamilyCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_fusion_environment_family_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fa-control-plane_us_grp@oracle.com" jiraProject="FACP" opsJiraProject="FACP"
def test_create_fusion_environment_family(testing_service_client):
    if not testing_service_client.is_api_enabled('fusion_apps', 'CreateFusionEnvironmentFamily'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fusion_apps', util.camelize('fusion_environment_family'), 'CreateFusionEnvironmentFamily')
    )

    request_containers = testing_service_client.get_requests(service_name='fusion_apps', api_name='CreateFusionEnvironmentFamily')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fusion_apps.FusionEnvironmentFamilyClient(config, service_endpoint=service_endpoint)
            response = client.create_fusion_environment_family(
                create_fusion_environment_family_details=request.pop(util.camelize('CreateFusionEnvironmentFamilyDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fusion_apps',
            'CreateFusionEnvironmentFamily',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_fusion_environment_family',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fa-control-plane_us_grp@oracle.com" jiraProject="FACP" opsJiraProject="FACP"
def test_delete_fusion_environment_family(testing_service_client):
    if not testing_service_client.is_api_enabled('fusion_apps', 'DeleteFusionEnvironmentFamily'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fusion_apps', util.camelize('fusion_environment_family'), 'DeleteFusionEnvironmentFamily')
    )

    request_containers = testing_service_client.get_requests(service_name='fusion_apps', api_name='DeleteFusionEnvironmentFamily')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fusion_apps.FusionEnvironmentFamilyClient(config, service_endpoint=service_endpoint)
            response = client.delete_fusion_environment_family(
                fusion_environment_family_id=request.pop(util.camelize('fusionEnvironmentFamilyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fusion_apps',
            'DeleteFusionEnvironmentFamily',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_fusion_environment_family',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="fa-control-plane_us_grp@oracle.com" jiraProject="FACP" opsJiraProject="FACP"
def test_get_fusion_environment_family(testing_service_client):
    if not testing_service_client.is_api_enabled('fusion_apps', 'GetFusionEnvironmentFamily'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fusion_apps', util.camelize('fusion_environment_family'), 'GetFusionEnvironmentFamily')
    )

    request_containers = testing_service_client.get_requests(service_name='fusion_apps', api_name='GetFusionEnvironmentFamily')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fusion_apps.FusionEnvironmentFamilyClient(config, service_endpoint=service_endpoint)
            response = client.get_fusion_environment_family(
                fusion_environment_family_id=request.pop(util.camelize('fusionEnvironmentFamilyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fusion_apps',
            'GetFusionEnvironmentFamily',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fusionEnvironmentFamily',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fa-control-plane_us_grp@oracle.com" jiraProject="FACP" opsJiraProject="FACP"
def test_get_fusion_environment_family_limits_and_usage(testing_service_client):
    if not testing_service_client.is_api_enabled('fusion_apps', 'GetFusionEnvironmentFamilyLimitsAndUsage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fusion_apps', util.camelize('fusion_environment_family'), 'GetFusionEnvironmentFamilyLimitsAndUsage')
    )

    request_containers = testing_service_client.get_requests(service_name='fusion_apps', api_name='GetFusionEnvironmentFamilyLimitsAndUsage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fusion_apps.FusionEnvironmentFamilyClient(config, service_endpoint=service_endpoint)
            response = client.get_fusion_environment_family_limits_and_usage(
                fusion_environment_family_id=request.pop(util.camelize('fusionEnvironmentFamilyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fusion_apps',
            'GetFusionEnvironmentFamilyLimitsAndUsage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fusionEnvironmentFamilyLimitsAndUsage',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fa-control-plane_us_grp@oracle.com" jiraProject="FACP" opsJiraProject="FACP"
def test_get_fusion_environment_family_subscription_detail(testing_service_client):
    if not testing_service_client.is_api_enabled('fusion_apps', 'GetFusionEnvironmentFamilySubscriptionDetail'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fusion_apps', util.camelize('fusion_environment_family'), 'GetFusionEnvironmentFamilySubscriptionDetail')
    )

    request_containers = testing_service_client.get_requests(service_name='fusion_apps', api_name='GetFusionEnvironmentFamilySubscriptionDetail')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fusion_apps.FusionEnvironmentFamilyClient(config, service_endpoint=service_endpoint)
            response = client.get_fusion_environment_family_subscription_detail(
                fusion_environment_family_id=request.pop(util.camelize('fusionEnvironmentFamilyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fusion_apps',
            'GetFusionEnvironmentFamilySubscriptionDetail',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'subscriptionDetail',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fa-control-plane_us_grp@oracle.com" jiraProject="FACP" opsJiraProject="FACP"
def test_list_fusion_environment_families(testing_service_client):
    if not testing_service_client.is_api_enabled('fusion_apps', 'ListFusionEnvironmentFamilies'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fusion_apps', util.camelize('fusion_environment_family'), 'ListFusionEnvironmentFamilies')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='fusion_apps', api_name='ListFusionEnvironmentFamilies')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fusion_apps.FusionEnvironmentFamilyClient(config, service_endpoint=service_endpoint)
            response = client.list_fusion_environment_families(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_fusion_environment_families(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_fusion_environment_families(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fusion_apps',
            'ListFusionEnvironmentFamilies',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fusionEnvironmentFamilyCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="fa-control-plane_us_grp@oracle.com" jiraProject="FACP" opsJiraProject="FACP"
def test_update_fusion_environment_family(testing_service_client):
    if not testing_service_client.is_api_enabled('fusion_apps', 'UpdateFusionEnvironmentFamily'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fusion_apps', util.camelize('fusion_environment_family'), 'UpdateFusionEnvironmentFamily')
    )

    request_containers = testing_service_client.get_requests(service_name='fusion_apps', api_name='UpdateFusionEnvironmentFamily')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fusion_apps.FusionEnvironmentFamilyClient(config, service_endpoint=service_endpoint)
            response = client.update_fusion_environment_family(
                fusion_environment_family_id=request.pop(util.camelize('fusionEnvironmentFamilyId')),
                update_fusion_environment_family_details=request.pop(util.camelize('UpdateFusionEnvironmentFamilyDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fusion_apps',
            'UpdateFusionEnvironmentFamily',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_fusion_environment_family',
            False,
            False
        )
