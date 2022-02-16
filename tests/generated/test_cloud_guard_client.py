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

        cassette_location = os.path.join('generated', 'cloud_guard_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_change_detector_recipe_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'ChangeDetectorRecipeCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'ChangeDetectorRecipeCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='ChangeDetectorRecipeCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.change_detector_recipe_compartment(
                detector_recipe_id=request.pop(util.camelize('detectorRecipeId')),
                change_detector_recipe_compartment_details=request.pop(util.camelize('ChangeDetectorRecipeCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'ChangeDetectorRecipeCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_detector_recipe_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_change_managed_list_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'ChangeManagedListCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'ChangeManagedListCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='ChangeManagedListCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.change_managed_list_compartment(
                managed_list_id=request.pop(util.camelize('managedListId')),
                change_managed_list_compartment_details=request.pop(util.camelize('ChangeManagedListCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'ChangeManagedListCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_managed_list_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_change_responder_recipe_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'ChangeResponderRecipeCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'ChangeResponderRecipeCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='ChangeResponderRecipeCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.change_responder_recipe_compartment(
                responder_recipe_id=request.pop(util.camelize('responderRecipeId')),
                change_responder_recipe_compartment_details=request.pop(util.camelize('ChangeResponderRecipeCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'ChangeResponderRecipeCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_responder_recipe_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_create_data_mask_rule(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'CreateDataMaskRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'CreateDataMaskRule')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='CreateDataMaskRule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.create_data_mask_rule(
                create_data_mask_rule_details=request.pop(util.camelize('CreateDataMaskRuleDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'CreateDataMaskRule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataMaskRule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_create_detector_recipe(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'CreateDetectorRecipe'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'CreateDetectorRecipe')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='CreateDetectorRecipe')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.create_detector_recipe(
                create_detector_recipe_details=request.pop(util.camelize('CreateDetectorRecipeDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'CreateDetectorRecipe',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'detectorRecipe',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_create_managed_list(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'CreateManagedList'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'CreateManagedList')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='CreateManagedList')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.create_managed_list(
                create_managed_list_details=request.pop(util.camelize('CreateManagedListDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'CreateManagedList',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managedList',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_create_responder_recipe(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'CreateResponderRecipe'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'CreateResponderRecipe')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='CreateResponderRecipe')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.create_responder_recipe(
                create_responder_recipe_details=request.pop(util.camelize('CreateResponderRecipeDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'CreateResponderRecipe',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'responderRecipe',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_create_target(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'CreateTarget'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'CreateTarget')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='CreateTarget')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.create_target(
                create_target_details=request.pop(util.camelize('CreateTargetDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'CreateTarget',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'target',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_create_target_detector_recipe(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'CreateTargetDetectorRecipe'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'CreateTargetDetectorRecipe')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='CreateTargetDetectorRecipe')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.create_target_detector_recipe(
                target_id=request.pop(util.camelize('targetId')),
                attach_target_detector_recipe_details=request.pop(util.camelize('AttachTargetDetectorRecipeDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'CreateTargetDetectorRecipe',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'targetDetectorRecipe',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_create_target_responder_recipe(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'CreateTargetResponderRecipe'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'CreateTargetResponderRecipe')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='CreateTargetResponderRecipe')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.create_target_responder_recipe(
                target_id=request.pop(util.camelize('targetId')),
                attach_target_responder_recipe_details=request.pop(util.camelize('AttachTargetResponderRecipeDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'CreateTargetResponderRecipe',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'targetResponderRecipe',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_delete_data_mask_rule(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'DeleteDataMaskRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'DeleteDataMaskRule')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='DeleteDataMaskRule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.delete_data_mask_rule(
                data_mask_rule_id=request.pop(util.camelize('dataMaskRuleId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'DeleteDataMaskRule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_data_mask_rule',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_delete_detector_recipe(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'DeleteDetectorRecipe'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'DeleteDetectorRecipe')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='DeleteDetectorRecipe')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.delete_detector_recipe(
                detector_recipe_id=request.pop(util.camelize('detectorRecipeId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'DeleteDetectorRecipe',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_detector_recipe',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_delete_managed_list(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'DeleteManagedList'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'DeleteManagedList')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='DeleteManagedList')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.delete_managed_list(
                managed_list_id=request.pop(util.camelize('managedListId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'DeleteManagedList',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_managed_list',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_delete_responder_recipe(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'DeleteResponderRecipe'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'DeleteResponderRecipe')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='DeleteResponderRecipe')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.delete_responder_recipe(
                responder_recipe_id=request.pop(util.camelize('responderRecipeId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'DeleteResponderRecipe',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_responder_recipe',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_delete_target(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'DeleteTarget'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'DeleteTarget')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='DeleteTarget')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.delete_target(
                target_id=request.pop(util.camelize('targetId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'DeleteTarget',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_target',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_delete_target_detector_recipe(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'DeleteTargetDetectorRecipe'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'DeleteTargetDetectorRecipe')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='DeleteTargetDetectorRecipe')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.delete_target_detector_recipe(
                target_id=request.pop(util.camelize('targetId')),
                target_detector_recipe_id=request.pop(util.camelize('targetDetectorRecipeId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'DeleteTargetDetectorRecipe',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_target_detector_recipe',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_delete_target_responder_recipe(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'DeleteTargetResponderRecipe'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'DeleteTargetResponderRecipe')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='DeleteTargetResponderRecipe')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.delete_target_responder_recipe(
                target_id=request.pop(util.camelize('targetId')),
                target_responder_recipe_id=request.pop(util.camelize('targetResponderRecipeId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'DeleteTargetResponderRecipe',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_target_responder_recipe',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_execute_responder_execution(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'ExecuteResponderExecution'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'ExecuteResponderExecution')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='ExecuteResponderExecution')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.execute_responder_execution(
                responder_execution_id=request.pop(util.camelize('responderExecutionId')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'ExecuteResponderExecution',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'execute_responder_execution',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_get_condition_metadata_type(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'GetConditionMetadataType'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'GetConditionMetadataType')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='GetConditionMetadataType')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.get_condition_metadata_type(
                condition_metadata_type_id=request.pop(util.camelize('conditionMetadataTypeId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'GetConditionMetadataType',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'conditionMetadataType',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_get_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'GetConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'GetConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='GetConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.get_configuration(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'GetConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'configuration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_get_data_mask_rule(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'GetDataMaskRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'GetDataMaskRule')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='GetDataMaskRule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.get_data_mask_rule(
                data_mask_rule_id=request.pop(util.camelize('dataMaskRuleId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'GetDataMaskRule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataMaskRule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_get_detector(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'GetDetector'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'GetDetector')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='GetDetector')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.get_detector(
                detector_id=request.pop(util.camelize('detectorId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'GetDetector',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'detector',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_get_detector_recipe(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'GetDetectorRecipe'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'GetDetectorRecipe')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='GetDetectorRecipe')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.get_detector_recipe(
                detector_recipe_id=request.pop(util.camelize('detectorRecipeId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'GetDetectorRecipe',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'detectorRecipe',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_get_detector_recipe_detector_rule(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'GetDetectorRecipeDetectorRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'GetDetectorRecipeDetectorRule')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='GetDetectorRecipeDetectorRule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.get_detector_recipe_detector_rule(
                detector_recipe_id=request.pop(util.camelize('detectorRecipeId')),
                detector_rule_id=request.pop(util.camelize('detectorRuleId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'GetDetectorRecipeDetectorRule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'detectorRecipeDetectorRule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_get_detector_rule(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'GetDetectorRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'GetDetectorRule')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='GetDetectorRule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.get_detector_rule(
                detector_id=request.pop(util.camelize('detectorId')),
                detector_rule_id=request.pop(util.camelize('detectorRuleId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'GetDetectorRule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'detectorRule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_get_managed_list(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'GetManagedList'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'GetManagedList')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='GetManagedList')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.get_managed_list(
                managed_list_id=request.pop(util.camelize('managedListId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'GetManagedList',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managedList',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_get_problem(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'GetProblem'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'GetProblem')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='GetProblem')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.get_problem(
                problem_id=request.pop(util.camelize('problemId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'GetProblem',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'problem',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_get_resource_profile(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'GetResourceProfile'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'GetResourceProfile')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='GetResourceProfile')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.get_resource_profile(
                resource_profile_id=request.pop(util.camelize('resourceProfileId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'GetResourceProfile',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'resourceProfile',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_get_responder_execution(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'GetResponderExecution'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'GetResponderExecution')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='GetResponderExecution')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.get_responder_execution(
                responder_execution_id=request.pop(util.camelize('responderExecutionId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'GetResponderExecution',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'responderExecution',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_get_responder_recipe(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'GetResponderRecipe'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'GetResponderRecipe')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='GetResponderRecipe')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.get_responder_recipe(
                responder_recipe_id=request.pop(util.camelize('responderRecipeId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'GetResponderRecipe',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'responderRecipe',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_get_responder_recipe_responder_rule(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'GetResponderRecipeResponderRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'GetResponderRecipeResponderRule')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='GetResponderRecipeResponderRule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.get_responder_recipe_responder_rule(
                responder_recipe_id=request.pop(util.camelize('responderRecipeId')),
                responder_rule_id=request.pop(util.camelize('responderRuleId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'GetResponderRecipeResponderRule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'responderRecipeResponderRule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_get_responder_rule(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'GetResponderRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'GetResponderRule')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='GetResponderRule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.get_responder_rule(
                responder_rule_id=request.pop(util.camelize('responderRuleId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'GetResponderRule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'responderRule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_get_sighting(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'GetSighting'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'GetSighting')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='GetSighting')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.get_sighting(
                sighting_id=request.pop(util.camelize('sightingId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'GetSighting',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sighting',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_get_target(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'GetTarget'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'GetTarget')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='GetTarget')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.get_target(
                target_id=request.pop(util.camelize('targetId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'GetTarget',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'target',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_get_target_detector_recipe(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'GetTargetDetectorRecipe'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'GetTargetDetectorRecipe')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='GetTargetDetectorRecipe')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.get_target_detector_recipe(
                target_id=request.pop(util.camelize('targetId')),
                target_detector_recipe_id=request.pop(util.camelize('targetDetectorRecipeId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'GetTargetDetectorRecipe',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'targetDetectorRecipe',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_get_target_detector_recipe_detector_rule(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'GetTargetDetectorRecipeDetectorRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'GetTargetDetectorRecipeDetectorRule')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='GetTargetDetectorRecipeDetectorRule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.get_target_detector_recipe_detector_rule(
                target_id=request.pop(util.camelize('targetId')),
                target_detector_recipe_id=request.pop(util.camelize('targetDetectorRecipeId')),
                detector_rule_id=request.pop(util.camelize('detectorRuleId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'GetTargetDetectorRecipeDetectorRule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'targetDetectorRecipeDetectorRule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_get_target_responder_recipe(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'GetTargetResponderRecipe'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'GetTargetResponderRecipe')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='GetTargetResponderRecipe')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.get_target_responder_recipe(
                target_id=request.pop(util.camelize('targetId')),
                target_responder_recipe_id=request.pop(util.camelize('targetResponderRecipeId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'GetTargetResponderRecipe',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'targetResponderRecipe',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_get_target_responder_recipe_responder_rule(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'GetTargetResponderRecipeResponderRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'GetTargetResponderRecipeResponderRule')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='GetTargetResponderRecipeResponderRule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.get_target_responder_recipe_responder_rule(
                target_id=request.pop(util.camelize('targetId')),
                target_responder_recipe_id=request.pop(util.camelize('targetResponderRecipeId')),
                responder_rule_id=request.pop(util.camelize('responderRuleId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'GetTargetResponderRecipeResponderRule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'targetResponderRecipeResponderRule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_list_condition_metadata_types(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'ListConditionMetadataTypes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'ListConditionMetadataTypes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='ListConditionMetadataTypes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.list_condition_metadata_types(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_condition_metadata_types(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_condition_metadata_types(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'ListConditionMetadataTypes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'conditionMetadataTypeCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_list_data_mask_rules(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'ListDataMaskRules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'ListDataMaskRules')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='ListDataMaskRules')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.list_data_mask_rules(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_data_mask_rules(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_data_mask_rules(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'ListDataMaskRules',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataMaskRuleCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_list_detector_recipe_detector_rules(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'ListDetectorRecipeDetectorRules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'ListDetectorRecipeDetectorRules')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='ListDetectorRecipeDetectorRules')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.list_detector_recipe_detector_rules(
                detector_recipe_id=request.pop(util.camelize('detectorRecipeId')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_detector_recipe_detector_rules(
                    detector_recipe_id=request.pop(util.camelize('detectorRecipeId')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_detector_recipe_detector_rules(
                        detector_recipe_id=request.pop(util.camelize('detectorRecipeId')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'ListDetectorRecipeDetectorRules',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'detectorRecipeDetectorRuleCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_list_detector_recipes(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'ListDetectorRecipes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'ListDetectorRecipes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='ListDetectorRecipes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.list_detector_recipes(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_detector_recipes(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_detector_recipes(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'ListDetectorRecipes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'detectorRecipeCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_list_detector_rules(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'ListDetectorRules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'ListDetectorRules')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='ListDetectorRules')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.list_detector_rules(
                detector_id=request.pop(util.camelize('detectorId')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_detector_rules(
                    detector_id=request.pop(util.camelize('detectorId')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_detector_rules(
                        detector_id=request.pop(util.camelize('detectorId')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'ListDetectorRules',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'detectorRuleCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_list_detectors(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'ListDetectors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'ListDetectors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='ListDetectors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.list_detectors(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_detectors(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_detectors(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'ListDetectors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'detectorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_list_impacted_resources(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'ListImpactedResources'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'ListImpactedResources')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='ListImpactedResources')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.list_impacted_resources(
                problem_id=request.pop(util.camelize('problemId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_impacted_resources(
                    problem_id=request.pop(util.camelize('problemId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_impacted_resources(
                        problem_id=request.pop(util.camelize('problemId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'ListImpactedResources',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'impactedResourceCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_list_managed_list_types(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'ListManagedListTypes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'ListManagedListTypes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='ListManagedListTypes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.list_managed_list_types(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_managed_list_types(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_managed_list_types(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'ListManagedListTypes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managedListTypeCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_list_managed_lists(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'ListManagedLists'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'ListManagedLists')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='ListManagedLists')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.list_managed_lists(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_managed_lists(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_managed_lists(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'ListManagedLists',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managedListCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_list_policies(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'ListPolicies'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'ListPolicies')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='ListPolicies')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.list_policies(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_policies(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_policies(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'ListPolicies',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'policyCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_list_problem_endpoints(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'ListProblemEndpoints'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'ListProblemEndpoints')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='ListProblemEndpoints')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.list_problem_endpoints(
                problem_id=request.pop(util.camelize('problemId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_problem_endpoints(
                    problem_id=request.pop(util.camelize('problemId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_problem_endpoints(
                        problem_id=request.pop(util.camelize('problemId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'ListProblemEndpoints',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'problemEndpointCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_list_problem_histories(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'ListProblemHistories'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'ListProblemHistories')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='ListProblemHistories')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.list_problem_histories(
                compartment_id=request.pop(util.camelize('compartmentId')),
                problem_id=request.pop(util.camelize('problemId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_problem_histories(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    problem_id=request.pop(util.camelize('problemId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_problem_histories(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        problem_id=request.pop(util.camelize('problemId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'ListProblemHistories',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'problemHistoryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_list_problems(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'ListProblems'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'ListProblems')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='ListProblems')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.list_problems(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_problems(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_problems(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'ListProblems',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'problemCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_list_recommendations(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'ListRecommendations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'ListRecommendations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='ListRecommendations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.list_recommendations(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_recommendations(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_recommendations(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'ListRecommendations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'recommendationSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_list_resource_profile_endpoints(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'ListResourceProfileEndpoints'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'ListResourceProfileEndpoints')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='ListResourceProfileEndpoints')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.list_resource_profile_endpoints(
                resource_profile_id=request.pop(util.camelize('resourceProfileId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_resource_profile_endpoints(
                    resource_profile_id=request.pop(util.camelize('resourceProfileId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_resource_profile_endpoints(
                        resource_profile_id=request.pop(util.camelize('resourceProfileId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'ListResourceProfileEndpoints',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'resourceProfileEndpointCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_list_resource_profile_impacted_resources(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'ListResourceProfileImpactedResources'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'ListResourceProfileImpactedResources')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='ListResourceProfileImpactedResources')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.list_resource_profile_impacted_resources(
                resource_profile_id=request.pop(util.camelize('resourceProfileId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_resource_profile_impacted_resources(
                    resource_profile_id=request.pop(util.camelize('resourceProfileId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_resource_profile_impacted_resources(
                        resource_profile_id=request.pop(util.camelize('resourceProfileId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'ListResourceProfileImpactedResources',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'resourceProfileImpactedResourceCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_list_resource_profiles(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'ListResourceProfiles'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'ListResourceProfiles')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='ListResourceProfiles')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.list_resource_profiles(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_resource_profiles(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_resource_profiles(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'ListResourceProfiles',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'resourceProfileCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_list_resource_types(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'ListResourceTypes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'ListResourceTypes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='ListResourceTypes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.list_resource_types(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_resource_types(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_resource_types(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'ListResourceTypes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'resourceTypeCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_list_responder_activities(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'ListResponderActivities'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'ListResponderActivities')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='ListResponderActivities')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.list_responder_activities(
                problem_id=request.pop(util.camelize('problemId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_responder_activities(
                    problem_id=request.pop(util.camelize('problemId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_responder_activities(
                        problem_id=request.pop(util.camelize('problemId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'ListResponderActivities',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'responderActivityCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_list_responder_executions(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'ListResponderExecutions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'ListResponderExecutions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='ListResponderExecutions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.list_responder_executions(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_responder_executions(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_responder_executions(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'ListResponderExecutions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'responderExecutionCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_list_responder_recipe_responder_rules(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'ListResponderRecipeResponderRules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'ListResponderRecipeResponderRules')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='ListResponderRecipeResponderRules')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.list_responder_recipe_responder_rules(
                responder_recipe_id=request.pop(util.camelize('responderRecipeId')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_responder_recipe_responder_rules(
                    responder_recipe_id=request.pop(util.camelize('responderRecipeId')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_responder_recipe_responder_rules(
                        responder_recipe_id=request.pop(util.camelize('responderRecipeId')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'ListResponderRecipeResponderRules',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'responderRecipeResponderRuleCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_list_responder_recipes(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'ListResponderRecipes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'ListResponderRecipes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='ListResponderRecipes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.list_responder_recipes(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_responder_recipes(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_responder_recipes(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'ListResponderRecipes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'responderRecipeCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_list_responder_rules(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'ListResponderRules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'ListResponderRules')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='ListResponderRules')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.list_responder_rules(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_responder_rules(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_responder_rules(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'ListResponderRules',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'responderRuleCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_list_sighting_endpoints(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'ListSightingEndpoints'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'ListSightingEndpoints')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='ListSightingEndpoints')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.list_sighting_endpoints(
                sighting_id=request.pop(util.camelize('sightingId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_sighting_endpoints(
                    sighting_id=request.pop(util.camelize('sightingId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_sighting_endpoints(
                        sighting_id=request.pop(util.camelize('sightingId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'ListSightingEndpoints',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sightingEndpointCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_list_sighting_impacted_resources(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'ListSightingImpactedResources'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'ListSightingImpactedResources')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='ListSightingImpactedResources')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.list_sighting_impacted_resources(
                sighting_id=request.pop(util.camelize('sightingId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_sighting_impacted_resources(
                    sighting_id=request.pop(util.camelize('sightingId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_sighting_impacted_resources(
                        sighting_id=request.pop(util.camelize('sightingId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'ListSightingImpactedResources',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sightingImpactedResourceCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_list_sightings(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'ListSightings'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'ListSightings')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='ListSightings')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.list_sightings(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_sightings(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_sightings(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'ListSightings',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sightingCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_list_tactics(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'ListTactics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'ListTactics')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='ListTactics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.list_tactics(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_tactics(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_tactics(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'ListTactics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'tacticCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_list_target_detector_recipe_detector_rules(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'ListTargetDetectorRecipeDetectorRules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'ListTargetDetectorRecipeDetectorRules')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='ListTargetDetectorRecipeDetectorRules')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.list_target_detector_recipe_detector_rules(
                target_id=request.pop(util.camelize('targetId')),
                target_detector_recipe_id=request.pop(util.camelize('targetDetectorRecipeId')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_target_detector_recipe_detector_rules(
                    target_id=request.pop(util.camelize('targetId')),
                    target_detector_recipe_id=request.pop(util.camelize('targetDetectorRecipeId')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_target_detector_recipe_detector_rules(
                        target_id=request.pop(util.camelize('targetId')),
                        target_detector_recipe_id=request.pop(util.camelize('targetDetectorRecipeId')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'ListTargetDetectorRecipeDetectorRules',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'targetDetectorRecipeDetectorRuleCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_list_target_detector_recipes(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'ListTargetDetectorRecipes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'ListTargetDetectorRecipes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='ListTargetDetectorRecipes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.list_target_detector_recipes(
                target_id=request.pop(util.camelize('targetId')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_target_detector_recipes(
                    target_id=request.pop(util.camelize('targetId')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_target_detector_recipes(
                        target_id=request.pop(util.camelize('targetId')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'ListTargetDetectorRecipes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'targetDetectorRecipeCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_list_target_responder_recipe_responder_rules(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'ListTargetResponderRecipeResponderRules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'ListTargetResponderRecipeResponderRules')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='ListTargetResponderRecipeResponderRules')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.list_target_responder_recipe_responder_rules(
                target_id=request.pop(util.camelize('targetId')),
                target_responder_recipe_id=request.pop(util.camelize('targetResponderRecipeId')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_target_responder_recipe_responder_rules(
                    target_id=request.pop(util.camelize('targetId')),
                    target_responder_recipe_id=request.pop(util.camelize('targetResponderRecipeId')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_target_responder_recipe_responder_rules(
                        target_id=request.pop(util.camelize('targetId')),
                        target_responder_recipe_id=request.pop(util.camelize('targetResponderRecipeId')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'ListTargetResponderRecipeResponderRules',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'targetResponderRecipeResponderRuleCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_list_target_responder_recipes(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'ListTargetResponderRecipes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'ListTargetResponderRecipes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='ListTargetResponderRecipes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.list_target_responder_recipes(
                target_id=request.pop(util.camelize('targetId')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_target_responder_recipes(
                    target_id=request.pop(util.camelize('targetId')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_target_responder_recipes(
                        target_id=request.pop(util.camelize('targetId')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'ListTargetResponderRecipes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'targetResponderRecipeCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_list_targets(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'ListTargets'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'ListTargets')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='ListTargets')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.list_targets(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_targets(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_targets(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'ListTargets',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'targetCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_list_techniques(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'ListTechniques'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'ListTechniques')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='ListTechniques')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.list_techniques(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_techniques(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_techniques(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'ListTechniques',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'techniqueCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_request_risk_scores(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'RequestRiskScores'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'RequestRiskScores')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='RequestRiskScores')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.request_risk_scores(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.request_risk_scores(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.request_risk_scores(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'RequestRiskScores',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'riskScoreAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_request_security_score_summarized_trend(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'RequestSecurityScoreSummarizedTrend'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'RequestSecurityScoreSummarizedTrend')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='RequestSecurityScoreSummarizedTrend')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.request_security_score_summarized_trend(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.request_security_score_summarized_trend(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.request_security_score_summarized_trend(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'RequestSecurityScoreSummarizedTrend',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'securityScoreTrendAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_request_security_scores(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'RequestSecurityScores'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'RequestSecurityScores')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='RequestSecurityScores')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.request_security_scores(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.request_security_scores(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.request_security_scores(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'RequestSecurityScores',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'securityScoreAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_request_summarized_activity_problems(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'RequestSummarizedActivityProblems'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'RequestSummarizedActivityProblems')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='RequestSummarizedActivityProblems')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.request_summarized_activity_problems(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.request_summarized_activity_problems(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.request_summarized_activity_problems(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'RequestSummarizedActivityProblems',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'activityProblemAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_request_summarized_problems(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'RequestSummarizedProblems'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'RequestSummarizedProblems')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='RequestSummarizedProblems')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.request_summarized_problems(
                list_dimensions=request.pop(util.camelize('listDimensions')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.request_summarized_problems(
                    list_dimensions=request.pop(util.camelize('listDimensions')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.request_summarized_problems(
                        list_dimensions=request.pop(util.camelize('listDimensions')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'RequestSummarizedProblems',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'problemAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_request_summarized_responder_executions(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'RequestSummarizedResponderExecutions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'RequestSummarizedResponderExecutions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='RequestSummarizedResponderExecutions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.request_summarized_responder_executions(
                responder_executions_dimensions=request.pop(util.camelize('responderExecutionsDimensions')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.request_summarized_responder_executions(
                    responder_executions_dimensions=request.pop(util.camelize('responderExecutionsDimensions')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.request_summarized_responder_executions(
                        responder_executions_dimensions=request.pop(util.camelize('responderExecutionsDimensions')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'RequestSummarizedResponderExecutions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'responderExecutionAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_request_summarized_risk_scores(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'RequestSummarizedRiskScores'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'RequestSummarizedRiskScores')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='RequestSummarizedRiskScores')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.request_summarized_risk_scores(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.request_summarized_risk_scores(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.request_summarized_risk_scores(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'RequestSummarizedRiskScores',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'riskScoreAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_request_summarized_security_scores(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'RequestSummarizedSecurityScores'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'RequestSummarizedSecurityScores')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='RequestSummarizedSecurityScores')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.request_summarized_security_scores(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.request_summarized_security_scores(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.request_summarized_security_scores(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'RequestSummarizedSecurityScores',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'securityScoreAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_request_summarized_top_trend_resource_profile_risk_scores(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'RequestSummarizedTopTrendResourceProfileRiskScores'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'RequestSummarizedTopTrendResourceProfileRiskScores')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='RequestSummarizedTopTrendResourceProfileRiskScores')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.request_summarized_top_trend_resource_profile_risk_scores(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.request_summarized_top_trend_resource_profile_risk_scores(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.request_summarized_top_trend_resource_profile_risk_scores(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'RequestSummarizedTopTrendResourceProfileRiskScores',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'resourceProfileRiskScoreAggregationSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_request_summarized_trend_problems(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'RequestSummarizedTrendProblems'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'RequestSummarizedTrendProblems')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='RequestSummarizedTrendProblems')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.request_summarized_trend_problems(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.request_summarized_trend_problems(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.request_summarized_trend_problems(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'RequestSummarizedTrendProblems',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'problemTrendAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_request_summarized_trend_resource_risk_scores(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'RequestSummarizedTrendResourceRiskScores'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'RequestSummarizedTrendResourceRiskScores')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='RequestSummarizedTrendResourceRiskScores')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.request_summarized_trend_resource_risk_scores(
                request_summarized_trend_resource_risk_scores_details=request.pop(util.camelize('RequestSummarizedTrendResourceRiskScoresDetails')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.request_summarized_trend_resource_risk_scores(
                    request_summarized_trend_resource_risk_scores_details=request.pop(util.camelize('RequestSummarizedTrendResourceRiskScoresDetails')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.request_summarized_trend_resource_risk_scores(
                        request_summarized_trend_resource_risk_scores_details=request.pop(util.camelize('RequestSummarizedTrendResourceRiskScoresDetails')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'RequestSummarizedTrendResourceRiskScores',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'resourceRiskScoreAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_request_summarized_trend_responder_executions(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'RequestSummarizedTrendResponderExecutions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'RequestSummarizedTrendResponderExecutions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='RequestSummarizedTrendResponderExecutions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.request_summarized_trend_responder_executions(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.request_summarized_trend_responder_executions(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.request_summarized_trend_responder_executions(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'RequestSummarizedTrendResponderExecutions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'responderExecutionTrendAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_request_summarized_trend_security_scores(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'RequestSummarizedTrendSecurityScores'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'RequestSummarizedTrendSecurityScores')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='RequestSummarizedTrendSecurityScores')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.request_summarized_trend_security_scores(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.request_summarized_trend_security_scores(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.request_summarized_trend_security_scores(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'RequestSummarizedTrendSecurityScores',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'securityScoreTrendAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_skip_bulk_responder_execution(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'SkipBulkResponderExecution'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'SkipBulkResponderExecution')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='SkipBulkResponderExecution')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.skip_bulk_responder_execution(
                skip_bulk_responder_execution_details=request.pop(util.camelize('SkipBulkResponderExecutionDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'SkipBulkResponderExecution',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'skip_bulk_responder_execution',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_skip_responder_execution(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'SkipResponderExecution'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'SkipResponderExecution')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='SkipResponderExecution')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.skip_responder_execution(
                responder_execution_id=request.pop(util.camelize('responderExecutionId')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'SkipResponderExecution',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'skip_responder_execution',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_trigger_responder(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'TriggerResponder'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'TriggerResponder')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='TriggerResponder')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.trigger_responder(
                problem_id=request.pop(util.camelize('problemId')),
                trigger_responder_details=request.pop(util.camelize('TriggerResponderDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'TriggerResponder',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'trigger_responder',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_update_bulk_problem_status(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'UpdateBulkProblemStatus'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'UpdateBulkProblemStatus')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='UpdateBulkProblemStatus')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.update_bulk_problem_status(
                update_bulk_problem_status_details=request.pop(util.camelize('UpdateBulkProblemStatusDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'UpdateBulkProblemStatus',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_bulk_problem_status',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_update_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'UpdateConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'UpdateConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='UpdateConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.update_configuration(
                update_configuration_details=request.pop(util.camelize('UpdateConfigurationDetails')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'UpdateConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'configuration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_update_data_mask_rule(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'UpdateDataMaskRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'UpdateDataMaskRule')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='UpdateDataMaskRule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.update_data_mask_rule(
                data_mask_rule_id=request.pop(util.camelize('dataMaskRuleId')),
                update_data_mask_rule_details=request.pop(util.camelize('UpdateDataMaskRuleDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'UpdateDataMaskRule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataMaskRule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_update_detector_recipe(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'UpdateDetectorRecipe'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'UpdateDetectorRecipe')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='UpdateDetectorRecipe')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.update_detector_recipe(
                detector_recipe_id=request.pop(util.camelize('detectorRecipeId')),
                update_detector_recipe_details=request.pop(util.camelize('UpdateDetectorRecipeDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'UpdateDetectorRecipe',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'detectorRecipe',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_update_detector_recipe_detector_rule(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'UpdateDetectorRecipeDetectorRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'UpdateDetectorRecipeDetectorRule')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='UpdateDetectorRecipeDetectorRule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.update_detector_recipe_detector_rule(
                detector_recipe_id=request.pop(util.camelize('detectorRecipeId')),
                detector_rule_id=request.pop(util.camelize('detectorRuleId')),
                update_detector_recipe_detector_rule_details=request.pop(util.camelize('UpdateDetectorRecipeDetectorRuleDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'UpdateDetectorRecipeDetectorRule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'detectorRecipeDetectorRule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_update_managed_list(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'UpdateManagedList'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'UpdateManagedList')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='UpdateManagedList')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.update_managed_list(
                managed_list_id=request.pop(util.camelize('managedListId')),
                update_managed_list_details=request.pop(util.camelize('UpdateManagedListDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'UpdateManagedList',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managedList',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_update_problem_status(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'UpdateProblemStatus'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'UpdateProblemStatus')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='UpdateProblemStatus')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.update_problem_status(
                problem_id=request.pop(util.camelize('problemId')),
                update_problem_status_details=request.pop(util.camelize('UpdateProblemStatusDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'UpdateProblemStatus',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'problem',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_update_responder_recipe(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'UpdateResponderRecipe'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'UpdateResponderRecipe')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='UpdateResponderRecipe')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.update_responder_recipe(
                responder_recipe_id=request.pop(util.camelize('responderRecipeId')),
                update_responder_recipe_details=request.pop(util.camelize('UpdateResponderRecipeDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'UpdateResponderRecipe',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'responderRecipe',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_update_responder_recipe_responder_rule(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'UpdateResponderRecipeResponderRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'UpdateResponderRecipeResponderRule')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='UpdateResponderRecipeResponderRule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.update_responder_recipe_responder_rule(
                responder_recipe_id=request.pop(util.camelize('responderRecipeId')),
                responder_rule_id=request.pop(util.camelize('responderRuleId')),
                update_responder_recipe_responder_rule_details=request.pop(util.camelize('UpdateResponderRecipeResponderRuleDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'UpdateResponderRecipeResponderRule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'responderRecipeResponderRule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_update_target(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'UpdateTarget'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'UpdateTarget')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='UpdateTarget')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.update_target(
                target_id=request.pop(util.camelize('targetId')),
                update_target_details=request.pop(util.camelize('UpdateTargetDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'UpdateTarget',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'target',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_update_target_detector_recipe(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'UpdateTargetDetectorRecipe'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'UpdateTargetDetectorRecipe')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='UpdateTargetDetectorRecipe')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.update_target_detector_recipe(
                target_id=request.pop(util.camelize('targetId')),
                target_detector_recipe_id=request.pop(util.camelize('targetDetectorRecipeId')),
                update_target_detector_recipe_details=request.pop(util.camelize('UpdateTargetDetectorRecipeDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'UpdateTargetDetectorRecipe',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'targetDetectorRecipe',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_update_target_detector_recipe_detector_rule(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'UpdateTargetDetectorRecipeDetectorRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'UpdateTargetDetectorRecipeDetectorRule')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='UpdateTargetDetectorRecipeDetectorRule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.update_target_detector_recipe_detector_rule(
                target_id=request.pop(util.camelize('targetId')),
                target_detector_recipe_id=request.pop(util.camelize('targetDetectorRecipeId')),
                detector_rule_id=request.pop(util.camelize('detectorRuleId')),
                update_target_detector_recipe_detector_rule_details=request.pop(util.camelize('UpdateTargetDetectorRecipeDetectorRuleDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'UpdateTargetDetectorRecipeDetectorRule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'targetDetectorRecipeDetectorRule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_update_target_responder_recipe(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'UpdateTargetResponderRecipe'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'UpdateTargetResponderRecipe')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='UpdateTargetResponderRecipe')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.update_target_responder_recipe(
                target_id=request.pop(util.camelize('targetId')),
                target_responder_recipe_id=request.pop(util.camelize('targetResponderRecipeId')),
                update_target_responder_recipe_details=request.pop(util.camelize('UpdateTargetResponderRecipeDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'UpdateTargetResponderRecipe',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'targetResponderRecipe',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="seccen-engg_ww_grp@oracle.com" jiraProject="SECCEN" opsJiraProject="SECCENOPS"
def test_update_target_responder_recipe_responder_rule(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_guard', 'UpdateTargetResponderRecipeResponderRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_guard', util.camelize('cloud_guard'), 'UpdateTargetResponderRecipeResponderRule')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_guard', api_name='UpdateTargetResponderRecipeResponderRule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_guard.CloudGuardClient(config, service_endpoint=service_endpoint)
            response = client.update_target_responder_recipe_responder_rule(
                target_id=request.pop(util.camelize('targetId')),
                target_responder_recipe_id=request.pop(util.camelize('targetResponderRecipeId')),
                responder_rule_id=request.pop(util.camelize('responderRuleId')),
                update_target_responder_recipe_responder_rule_details=request.pop(util.camelize('UpdateTargetResponderRecipeResponderRuleDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_guard',
            'UpdateTargetResponderRecipeResponderRule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'targetResponderRecipeResponderRule',
            False,
            False
        )
