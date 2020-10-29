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

        cassette_location = os.path.join('generated', 'optimizer_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="oracle_cloud_optimizer_us_grp@oracle.com" jiraProject="OPTIMIZER" opsJiraProject="OPTIMIZER"
def test_bulk_apply_recommendations(testing_service_client):
    if not testing_service_client.is_api_enabled('optimizer', 'BulkApplyRecommendations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('optimizer', util.camelize('optimizer'), 'BulkApplyRecommendations')
    )

    request_containers = testing_service_client.get_requests(service_name='optimizer', api_name='BulkApplyRecommendations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.optimizer.OptimizerClient(config, service_endpoint=service_endpoint)
            response = client.bulk_apply_recommendations(
                recommendation_id=request.pop(util.camelize('recommendationId')),
                bulk_apply_recommendations_details=request.pop(util.camelize('BulkApplyRecommendationsDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'optimizer',
            'BulkApplyRecommendations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bulk_apply_recommendations',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oracle_cloud_optimizer_us_grp@oracle.com" jiraProject="OPTIMIZER" opsJiraProject="OPTIMIZER"
def test_create_profile(testing_service_client):
    if not testing_service_client.is_api_enabled('optimizer', 'CreateProfile'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('optimizer', util.camelize('optimizer'), 'CreateProfile')
    )

    request_containers = testing_service_client.get_requests(service_name='optimizer', api_name='CreateProfile')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.optimizer.OptimizerClient(config, service_endpoint=service_endpoint)
            response = client.create_profile(
                create_profile_details=request.pop(util.camelize('CreateProfileDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'optimizer',
            'CreateProfile',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'profile',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oracle_cloud_optimizer_us_grp@oracle.com" jiraProject="OPTIMIZER" opsJiraProject="OPTIMIZER"
def test_delete_profile(testing_service_client):
    if not testing_service_client.is_api_enabled('optimizer', 'DeleteProfile'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('optimizer', util.camelize('optimizer'), 'DeleteProfile')
    )

    request_containers = testing_service_client.get_requests(service_name='optimizer', api_name='DeleteProfile')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.optimizer.OptimizerClient(config, service_endpoint=service_endpoint)
            response = client.delete_profile(
                profile_id=request.pop(util.camelize('profileId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'optimizer',
            'DeleteProfile',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_profile',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oracle_cloud_optimizer_us_grp@oracle.com" jiraProject="OPTIMIZER" opsJiraProject="OPTIMIZER"
def test_get_category(testing_service_client):
    if not testing_service_client.is_api_enabled('optimizer', 'GetCategory'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('optimizer', util.camelize('optimizer'), 'GetCategory')
    )

    request_containers = testing_service_client.get_requests(service_name='optimizer', api_name='GetCategory')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.optimizer.OptimizerClient(config, service_endpoint=service_endpoint)
            response = client.get_category(
                category_id=request.pop(util.camelize('categoryId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'optimizer',
            'GetCategory',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'category',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oracle_cloud_optimizer_us_grp@oracle.com" jiraProject="OPTIMIZER" opsJiraProject="OPTIMIZER"
def test_get_enrollment_status(testing_service_client):
    if not testing_service_client.is_api_enabled('optimizer', 'GetEnrollmentStatus'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('optimizer', util.camelize('optimizer'), 'GetEnrollmentStatus')
    )

    request_containers = testing_service_client.get_requests(service_name='optimizer', api_name='GetEnrollmentStatus')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.optimizer.OptimizerClient(config, service_endpoint=service_endpoint)
            response = client.get_enrollment_status(
                enrollment_status_id=request.pop(util.camelize('enrollmentStatusId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'optimizer',
            'GetEnrollmentStatus',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'enrollmentStatus',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oracle_cloud_optimizer_us_grp@oracle.com" jiraProject="OPTIMIZER" opsJiraProject="OPTIMIZER"
def test_get_profile(testing_service_client):
    if not testing_service_client.is_api_enabled('optimizer', 'GetProfile'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('optimizer', util.camelize('optimizer'), 'GetProfile')
    )

    request_containers = testing_service_client.get_requests(service_name='optimizer', api_name='GetProfile')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.optimizer.OptimizerClient(config, service_endpoint=service_endpoint)
            response = client.get_profile(
                profile_id=request.pop(util.camelize('profileId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'optimizer',
            'GetProfile',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'profile',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oracle_cloud_optimizer_us_grp@oracle.com" jiraProject="OPTIMIZER" opsJiraProject="OPTIMIZER"
def test_get_recommendation(testing_service_client):
    if not testing_service_client.is_api_enabled('optimizer', 'GetRecommendation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('optimizer', util.camelize('optimizer'), 'GetRecommendation')
    )

    request_containers = testing_service_client.get_requests(service_name='optimizer', api_name='GetRecommendation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.optimizer.OptimizerClient(config, service_endpoint=service_endpoint)
            response = client.get_recommendation(
                recommendation_id=request.pop(util.camelize('recommendationId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'optimizer',
            'GetRecommendation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'recommendation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oracle_cloud_optimizer_us_grp@oracle.com" jiraProject="OPTIMIZER" opsJiraProject="OPTIMIZER"
def test_get_resource_action(testing_service_client):
    if not testing_service_client.is_api_enabled('optimizer', 'GetResourceAction'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('optimizer', util.camelize('optimizer'), 'GetResourceAction')
    )

    request_containers = testing_service_client.get_requests(service_name='optimizer', api_name='GetResourceAction')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.optimizer.OptimizerClient(config, service_endpoint=service_endpoint)
            response = client.get_resource_action(
                resource_action_id=request.pop(util.camelize('resourceActionId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'optimizer',
            'GetResourceAction',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'resourceAction',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oracle_cloud_optimizer_us_grp@oracle.com" jiraProject="OPTIMIZER" opsJiraProject="OPTIMIZER"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('optimizer', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('optimizer', util.camelize('optimizer'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='optimizer', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.optimizer.OptimizerClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'optimizer',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oracle_cloud_optimizer_us_grp@oracle.com" jiraProject="OPTIMIZER" opsJiraProject="OPTIMIZER"
def test_list_categories(testing_service_client):
    if not testing_service_client.is_api_enabled('optimizer', 'ListCategories'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('optimizer', util.camelize('optimizer'), 'ListCategories')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='optimizer', api_name='ListCategories')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.optimizer.OptimizerClient(config, service_endpoint=service_endpoint)
            response = client.list_categories(
                compartment_id=request.pop(util.camelize('compartmentId')),
                compartment_id_in_subtree=request.pop(util.camelize('compartmentIdInSubtree')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_categories(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    compartment_id_in_subtree=request.pop(util.camelize('compartmentIdInSubtree')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_categories(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        compartment_id_in_subtree=request.pop(util.camelize('compartmentIdInSubtree')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'optimizer',
            'ListCategories',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'categoryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oracle_cloud_optimizer_us_grp@oracle.com" jiraProject="OPTIMIZER" opsJiraProject="OPTIMIZER"
def test_list_enrollment_statuses(testing_service_client):
    if not testing_service_client.is_api_enabled('optimizer', 'ListEnrollmentStatuses'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('optimizer', util.camelize('optimizer'), 'ListEnrollmentStatuses')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='optimizer', api_name='ListEnrollmentStatuses')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.optimizer.OptimizerClient(config, service_endpoint=service_endpoint)
            response = client.list_enrollment_statuses(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_enrollment_statuses(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_enrollment_statuses(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'optimizer',
            'ListEnrollmentStatuses',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'enrollmentStatusCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oracle_cloud_optimizer_us_grp@oracle.com" jiraProject="OPTIMIZER" opsJiraProject="OPTIMIZER"
def test_list_histories(testing_service_client):
    if not testing_service_client.is_api_enabled('optimizer', 'ListHistories'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('optimizer', util.camelize('optimizer'), 'ListHistories')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='optimizer', api_name='ListHistories')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.optimizer.OptimizerClient(config, service_endpoint=service_endpoint)
            response = client.list_histories(
                compartment_id=request.pop(util.camelize('compartmentId')),
                compartment_id_in_subtree=request.pop(util.camelize('compartmentIdInSubtree')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_histories(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    compartment_id_in_subtree=request.pop(util.camelize('compartmentIdInSubtree')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_histories(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        compartment_id_in_subtree=request.pop(util.camelize('compartmentIdInSubtree')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'optimizer',
            'ListHistories',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'historyCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oracle_cloud_optimizer_us_grp@oracle.com" jiraProject="OPTIMIZER" opsJiraProject="OPTIMIZER"
def test_list_profiles(testing_service_client):
    if not testing_service_client.is_api_enabled('optimizer', 'ListProfiles'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('optimizer', util.camelize('optimizer'), 'ListProfiles')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='optimizer', api_name='ListProfiles')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.optimizer.OptimizerClient(config, service_endpoint=service_endpoint)
            response = client.list_profiles(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_profiles(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_profiles(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'optimizer',
            'ListProfiles',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'profileCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oracle_cloud_optimizer_us_grp@oracle.com" jiraProject="OPTIMIZER" opsJiraProject="OPTIMIZER"
def test_list_recommendations(testing_service_client):
    if not testing_service_client.is_api_enabled('optimizer', 'ListRecommendations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('optimizer', util.camelize('optimizer'), 'ListRecommendations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='optimizer', api_name='ListRecommendations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.optimizer.OptimizerClient(config, service_endpoint=service_endpoint)
            response = client.list_recommendations(
                compartment_id=request.pop(util.camelize('compartmentId')),
                compartment_id_in_subtree=request.pop(util.camelize('compartmentIdInSubtree')),
                category_id=request.pop(util.camelize('categoryId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_recommendations(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    compartment_id_in_subtree=request.pop(util.camelize('compartmentIdInSubtree')),
                    category_id=request.pop(util.camelize('categoryId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_recommendations(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        compartment_id_in_subtree=request.pop(util.camelize('compartmentIdInSubtree')),
                        category_id=request.pop(util.camelize('categoryId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'optimizer',
            'ListRecommendations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'recommendationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oracle_cloud_optimizer_us_grp@oracle.com" jiraProject="OPTIMIZER" opsJiraProject="OPTIMIZER"
def test_list_resource_actions(testing_service_client):
    if not testing_service_client.is_api_enabled('optimizer', 'ListResourceActions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('optimizer', util.camelize('optimizer'), 'ListResourceActions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='optimizer', api_name='ListResourceActions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.optimizer.OptimizerClient(config, service_endpoint=service_endpoint)
            response = client.list_resource_actions(
                compartment_id=request.pop(util.camelize('compartmentId')),
                compartment_id_in_subtree=request.pop(util.camelize('compartmentIdInSubtree')),
                recommendation_id=request.pop(util.camelize('recommendationId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_resource_actions(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    compartment_id_in_subtree=request.pop(util.camelize('compartmentIdInSubtree')),
                    recommendation_id=request.pop(util.camelize('recommendationId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_resource_actions(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        compartment_id_in_subtree=request.pop(util.camelize('compartmentIdInSubtree')),
                        recommendation_id=request.pop(util.camelize('recommendationId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'optimizer',
            'ListResourceActions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'resourceActionCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oracle_cloud_optimizer_us_grp@oracle.com" jiraProject="OPTIMIZER" opsJiraProject="OPTIMIZER"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('optimizer', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('optimizer', util.camelize('optimizer'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='optimizer', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.optimizer.OptimizerClient(config, service_endpoint=service_endpoint)
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
            'optimizer',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestErrorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oracle_cloud_optimizer_us_grp@oracle.com" jiraProject="OPTIMIZER" opsJiraProject="OPTIMIZER"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('optimizer', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('optimizer', util.camelize('optimizer'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='optimizer', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.optimizer.OptimizerClient(config, service_endpoint=service_endpoint)
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
            'optimizer',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oracle_cloud_optimizer_us_grp@oracle.com" jiraProject="OPTIMIZER" opsJiraProject="OPTIMIZER"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('optimizer', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('optimizer', util.camelize('optimizer'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='optimizer', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.optimizer.OptimizerClient(config, service_endpoint=service_endpoint)
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
            'optimizer',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oracle_cloud_optimizer_us_grp@oracle.com" jiraProject="OPTIMIZER" opsJiraProject="OPTIMIZER"
def test_update_enrollment_status(testing_service_client):
    if not testing_service_client.is_api_enabled('optimizer', 'UpdateEnrollmentStatus'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('optimizer', util.camelize('optimizer'), 'UpdateEnrollmentStatus')
    )

    request_containers = testing_service_client.get_requests(service_name='optimizer', api_name='UpdateEnrollmentStatus')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.optimizer.OptimizerClient(config, service_endpoint=service_endpoint)
            response = client.update_enrollment_status(
                enrollment_status_id=request.pop(util.camelize('enrollmentStatusId')),
                update_enrollment_status_details=request.pop(util.camelize('UpdateEnrollmentStatusDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'optimizer',
            'UpdateEnrollmentStatus',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'enrollmentStatus',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oracle_cloud_optimizer_us_grp@oracle.com" jiraProject="OPTIMIZER" opsJiraProject="OPTIMIZER"
def test_update_profile(testing_service_client):
    if not testing_service_client.is_api_enabled('optimizer', 'UpdateProfile'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('optimizer', util.camelize('optimizer'), 'UpdateProfile')
    )

    request_containers = testing_service_client.get_requests(service_name='optimizer', api_name='UpdateProfile')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.optimizer.OptimizerClient(config, service_endpoint=service_endpoint)
            response = client.update_profile(
                profile_id=request.pop(util.camelize('profileId')),
                update_profile_details=request.pop(util.camelize('UpdateProfileDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'optimizer',
            'UpdateProfile',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'profile',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oracle_cloud_optimizer_us_grp@oracle.com" jiraProject="OPTIMIZER" opsJiraProject="OPTIMIZER"
def test_update_recommendation(testing_service_client):
    if not testing_service_client.is_api_enabled('optimizer', 'UpdateRecommendation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('optimizer', util.camelize('optimizer'), 'UpdateRecommendation')
    )

    request_containers = testing_service_client.get_requests(service_name='optimizer', api_name='UpdateRecommendation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.optimizer.OptimizerClient(config, service_endpoint=service_endpoint)
            response = client.update_recommendation(
                recommendation_id=request.pop(util.camelize('recommendationId')),
                update_recommendation_details=request.pop(util.camelize('UpdateRecommendationDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'optimizer',
            'UpdateRecommendation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'recommendation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oracle_cloud_optimizer_us_grp@oracle.com" jiraProject="OPTIMIZER" opsJiraProject="OPTIMIZER"
def test_update_resource_action(testing_service_client):
    if not testing_service_client.is_api_enabled('optimizer', 'UpdateResourceAction'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('optimizer', util.camelize('optimizer'), 'UpdateResourceAction')
    )

    request_containers = testing_service_client.get_requests(service_name='optimizer', api_name='UpdateResourceAction')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.optimizer.OptimizerClient(config, service_endpoint=service_endpoint)
            response = client.update_resource_action(
                resource_action_id=request.pop(util.camelize('resourceActionId')),
                update_resource_action_details=request.pop(util.camelize('UpdateResourceActionDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'optimizer',
            'UpdateResourceAction',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'resourceAction',
            False,
            False
        )
