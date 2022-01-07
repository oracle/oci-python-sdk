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

        cassette_location = os.path.join('generated', 'data_safe_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_activate_target_database(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ActivateTargetDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ActivateTargetDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ActivateTargetDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.activate_target_database(
                activate_target_database_details=request.pop(util.camelize('ActivateTargetDatabaseDetails')),
                target_database_id=request.pop(util.camelize('targetDatabaseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ActivateTargetDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'activate_target_database',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_change_data_safe_private_endpoint_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ChangeDataSafePrivateEndpointCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ChangeDataSafePrivateEndpointCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ChangeDataSafePrivateEndpointCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.change_data_safe_private_endpoint_compartment(
                data_safe_private_endpoint_id=request.pop(util.camelize('dataSafePrivateEndpointId')),
                change_data_safe_private_endpoint_compartment_details=request.pop(util.camelize('ChangeDataSafePrivateEndpointCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ChangeDataSafePrivateEndpointCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_data_safe_private_endpoint_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_change_on_prem_connector_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ChangeOnPremConnectorCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ChangeOnPremConnectorCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ChangeOnPremConnectorCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.change_on_prem_connector_compartment(
                on_prem_connector_id=request.pop(util.camelize('onPremConnectorId')),
                change_on_prem_connector_compartment_details=request.pop(util.camelize('ChangeOnPremConnectorCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ChangeOnPremConnectorCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_on_prem_connector_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_change_security_assessment_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ChangeSecurityAssessmentCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ChangeSecurityAssessmentCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ChangeSecurityAssessmentCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.change_security_assessment_compartment(
                security_assessment_id=request.pop(util.camelize('securityAssessmentId')),
                change_security_assessment_compartment_details=request.pop(util.camelize('ChangeSecurityAssessmentCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ChangeSecurityAssessmentCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_security_assessment_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_change_target_database_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ChangeTargetDatabaseCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ChangeTargetDatabaseCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ChangeTargetDatabaseCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.change_target_database_compartment(
                target_database_id=request.pop(util.camelize('targetDatabaseId')),
                change_target_database_compartment_details=request.pop(util.camelize('ChangeTargetDatabaseCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ChangeTargetDatabaseCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_target_database_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_change_user_assessment_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ChangeUserAssessmentCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ChangeUserAssessmentCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ChangeUserAssessmentCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.change_user_assessment_compartment(
                user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                change_user_assessment_compartment_details=request.pop(util.camelize('ChangeUserAssessmentCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ChangeUserAssessmentCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_user_assessment_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_compare_security_assessment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'CompareSecurityAssessment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'CompareSecurityAssessment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='CompareSecurityAssessment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.compare_security_assessment(
                security_assessment_id=request.pop(util.camelize('securityAssessmentId')),
                compare_security_assessment_details=request.pop(util.camelize('CompareSecurityAssessmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'CompareSecurityAssessment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'compare_security_assessment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_compare_user_assessment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'CompareUserAssessment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'CompareUserAssessment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='CompareUserAssessment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.compare_user_assessment(
                user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                compare_user_assessment_details=request.pop(util.camelize('CompareUserAssessmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'CompareUserAssessment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'compare_user_assessment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_create_data_safe_private_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'CreateDataSafePrivateEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'CreateDataSafePrivateEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='CreateDataSafePrivateEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.create_data_safe_private_endpoint(
                create_data_safe_private_endpoint_details=request.pop(util.camelize('CreateDataSafePrivateEndpointDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'CreateDataSafePrivateEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataSafePrivateEndpoint',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_create_on_prem_connector(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'CreateOnPremConnector'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'CreateOnPremConnector')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='CreateOnPremConnector')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.create_on_prem_connector(
                create_on_prem_connector_details=request.pop(util.camelize('CreateOnPremConnectorDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'CreateOnPremConnector',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'onPremConnector',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_create_security_assessment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'CreateSecurityAssessment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'CreateSecurityAssessment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='CreateSecurityAssessment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.create_security_assessment(
                create_security_assessment_details=request.pop(util.camelize('CreateSecurityAssessmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'CreateSecurityAssessment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'securityAssessment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_create_target_database(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'CreateTargetDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'CreateTargetDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='CreateTargetDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.create_target_database(
                create_target_database_details=request.pop(util.camelize('CreateTargetDatabaseDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'CreateTargetDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'targetDatabase',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_create_user_assessment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'CreateUserAssessment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'CreateUserAssessment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='CreateUserAssessment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.create_user_assessment(
                create_user_assessment_details=request.pop(util.camelize('CreateUserAssessmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'CreateUserAssessment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'userAssessment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_deactivate_target_database(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DeactivateTargetDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DeactivateTargetDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DeactivateTargetDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.deactivate_target_database(
                target_database_id=request.pop(util.camelize('targetDatabaseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DeactivateTargetDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deactivate_target_database',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_delete_data_safe_private_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DeleteDataSafePrivateEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DeleteDataSafePrivateEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DeleteDataSafePrivateEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.delete_data_safe_private_endpoint(
                data_safe_private_endpoint_id=request.pop(util.camelize('dataSafePrivateEndpointId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DeleteDataSafePrivateEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_data_safe_private_endpoint',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_delete_on_prem_connector(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DeleteOnPremConnector'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DeleteOnPremConnector')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DeleteOnPremConnector')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.delete_on_prem_connector(
                on_prem_connector_id=request.pop(util.camelize('onPremConnectorId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DeleteOnPremConnector',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_on_prem_connector',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_delete_security_assessment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DeleteSecurityAssessment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DeleteSecurityAssessment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DeleteSecurityAssessment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.delete_security_assessment(
                security_assessment_id=request.pop(util.camelize('securityAssessmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DeleteSecurityAssessment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_security_assessment',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_delete_target_database(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DeleteTargetDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DeleteTargetDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DeleteTargetDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.delete_target_database(
                target_database_id=request.pop(util.camelize('targetDatabaseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DeleteTargetDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_target_database',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_delete_user_assessment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DeleteUserAssessment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DeleteUserAssessment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DeleteUserAssessment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.delete_user_assessment(
                user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DeleteUserAssessment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_user_assessment',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_download_privilege_script(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DownloadPrivilegeScript'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DownloadPrivilegeScript')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DownloadPrivilegeScript')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.download_privilege_script(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DownloadPrivilegeScript',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_download_security_assessment_report(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DownloadSecurityAssessmentReport'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DownloadSecurityAssessmentReport')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DownloadSecurityAssessmentReport')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.download_security_assessment_report(
                security_assessment_id=request.pop(util.camelize('securityAssessmentId')),
                download_security_assessment_report_details=request.pop(util.camelize('DownloadSecurityAssessmentReportDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DownloadSecurityAssessmentReport',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_download_user_assessment_report(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DownloadUserAssessmentReport'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DownloadUserAssessmentReport')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DownloadUserAssessmentReport')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.download_user_assessment_report(
                user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                download_user_assessment_report_details=request.pop(util.camelize('DownloadUserAssessmentReportDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DownloadUserAssessmentReport',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_enable_data_safe_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'EnableDataSafeConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'EnableDataSafeConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='EnableDataSafeConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.enable_data_safe_configuration(
                enable_data_safe_configuration_details=request.pop(util.camelize('EnableDataSafeConfigurationDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'EnableDataSafeConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'enable_data_safe_configuration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_generate_on_prem_connector_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GenerateOnPremConnectorConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GenerateOnPremConnectorConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GenerateOnPremConnectorConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.generate_on_prem_connector_configuration(
                generate_on_prem_connector_configuration_details=request.pop(util.camelize('GenerateOnPremConnectorConfigurationDetails')),
                on_prem_connector_id=request.pop(util.camelize('onPremConnectorId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GenerateOnPremConnectorConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_generate_security_assessment_report(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GenerateSecurityAssessmentReport'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GenerateSecurityAssessmentReport')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GenerateSecurityAssessmentReport')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.generate_security_assessment_report(
                security_assessment_id=request.pop(util.camelize('securityAssessmentId')),
                generate_security_assessment_report_details=request.pop(util.camelize('GenerateSecurityAssessmentReportDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GenerateSecurityAssessmentReport',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'generate_security_assessment_report',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_generate_user_assessment_report(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GenerateUserAssessmentReport'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GenerateUserAssessmentReport')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GenerateUserAssessmentReport')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.generate_user_assessment_report(
                user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                generate_user_assessment_report_details=request.pop(util.camelize('GenerateUserAssessmentReportDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GenerateUserAssessmentReport',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'generate_user_assessment_report',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_data_safe_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetDataSafeConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetDataSafeConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetDataSafeConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_data_safe_configuration(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetDataSafeConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataSafeConfiguration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_data_safe_private_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetDataSafePrivateEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetDataSafePrivateEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetDataSafePrivateEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_data_safe_private_endpoint(
                data_safe_private_endpoint_id=request.pop(util.camelize('dataSafePrivateEndpointId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetDataSafePrivateEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataSafePrivateEndpoint',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_on_prem_connector(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetOnPremConnector'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetOnPremConnector')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetOnPremConnector')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_on_prem_connector(
                on_prem_connector_id=request.pop(util.camelize('onPremConnectorId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetOnPremConnector',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'onPremConnector',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_security_assessment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetSecurityAssessment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetSecurityAssessment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetSecurityAssessment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_security_assessment(
                security_assessment_id=request.pop(util.camelize('securityAssessmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetSecurityAssessment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'securityAssessment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_security_assessment_comparison(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetSecurityAssessmentComparison'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetSecurityAssessmentComparison')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetSecurityAssessmentComparison')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_security_assessment_comparison(
                security_assessment_id=request.pop(util.camelize('securityAssessmentId')),
                comparison_security_assessment_id=request.pop(util.camelize('comparisonSecurityAssessmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetSecurityAssessmentComparison',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'securityAssessmentComparison',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_target_database(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetTargetDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetTargetDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetTargetDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_target_database(
                target_database_id=request.pop(util.camelize('targetDatabaseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetTargetDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'targetDatabase',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_user_assessment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetUserAssessment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetUserAssessment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetUserAssessment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_user_assessment(
                user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetUserAssessment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'userAssessment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_user_assessment_comparison(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetUserAssessmentComparison'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetUserAssessmentComparison')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetUserAssessmentComparison')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_user_assessment_comparison(
                user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                comparison_user_assessment_id=request.pop(util.camelize('comparisonUserAssessmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetUserAssessmentComparison',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'userAssessmentComparison',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_data_safe_private_endpoints(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListDataSafePrivateEndpoints'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListDataSafePrivateEndpoints')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListDataSafePrivateEndpoints')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_data_safe_private_endpoints(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_data_safe_private_endpoints(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_data_safe_private_endpoints(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListDataSafePrivateEndpoints',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataSafePrivateEndpointSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_findings(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListFindings'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListFindings')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListFindings')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_findings(
                security_assessment_id=request.pop(util.camelize('securityAssessmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_findings(
                    security_assessment_id=request.pop(util.camelize('securityAssessmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_findings(
                        security_assessment_id=request.pop(util.camelize('securityAssessmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListFindings',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'findingSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_grants(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListGrants'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListGrants')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListGrants')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_grants(
                user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                user_key=request.pop(util.camelize('userKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_grants(
                    user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                    user_key=request.pop(util.camelize('userKey')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_grants(
                        user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                        user_key=request.pop(util.camelize('userKey')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListGrants',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'grantSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_on_prem_connectors(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListOnPremConnectors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListOnPremConnectors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListOnPremConnectors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_on_prem_connectors(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_on_prem_connectors(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_on_prem_connectors(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListOnPremConnectors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'onPremConnectorSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_security_assessments(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListSecurityAssessments'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListSecurityAssessments')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListSecurityAssessments')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_security_assessments(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_security_assessments(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_security_assessments(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListSecurityAssessments',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'securityAssessmentSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_target_databases(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListTargetDatabases'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListTargetDatabases')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListTargetDatabases')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_target_databases(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_target_databases(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_target_databases(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListTargetDatabases',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'targetDatabaseSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_user_analytics(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListUserAnalytics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListUserAnalytics')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListUserAnalytics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_user_analytics(
                user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_user_analytics(
                    user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_user_analytics(
                        user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListUserAnalytics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'userAggregation',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_user_assessments(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListUserAssessments'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListUserAssessments')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListUserAssessments')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_user_assessments(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_user_assessments(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_user_assessments(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListUserAssessments',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'userAssessmentSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_users(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListUsers'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListUsers')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListUsers')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_users(
                user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_users(
                    user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_users(
                        user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListUsers',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'userSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
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
            'data_safe',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestError',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
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
            'data_safe',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntry',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
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
            'data_safe',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_refresh_security_assessment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'RefreshSecurityAssessment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'RefreshSecurityAssessment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='RefreshSecurityAssessment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.refresh_security_assessment(
                security_assessment_id=request.pop(util.camelize('securityAssessmentId')),
                run_security_assessment_details=request.pop(util.camelize('RunSecurityAssessmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'RefreshSecurityAssessment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'refresh_security_assessment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_refresh_user_assessment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'RefreshUserAssessment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'RefreshUserAssessment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='RefreshUserAssessment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.refresh_user_assessment(
                user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                run_user_assessment_details=request.pop(util.camelize('RunUserAssessmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'RefreshUserAssessment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'refresh_user_assessment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_set_security_assessment_baseline(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'SetSecurityAssessmentBaseline'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'SetSecurityAssessmentBaseline')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='SetSecurityAssessmentBaseline')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.set_security_assessment_baseline(
                security_assessment_id=request.pop(util.camelize('securityAssessmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'SetSecurityAssessmentBaseline',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'set_security_assessment_baseline',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_set_user_assessment_baseline(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'SetUserAssessmentBaseline'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'SetUserAssessmentBaseline')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='SetUserAssessmentBaseline')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.set_user_assessment_baseline(
                user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'SetUserAssessmentBaseline',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'set_user_assessment_baseline',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_unset_security_assessment_baseline(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'UnsetSecurityAssessmentBaseline'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'UnsetSecurityAssessmentBaseline')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='UnsetSecurityAssessmentBaseline')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.unset_security_assessment_baseline(
                security_assessment_id=request.pop(util.camelize('securityAssessmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'UnsetSecurityAssessmentBaseline',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'unset_security_assessment_baseline',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_unset_user_assessment_baseline(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'UnsetUserAssessmentBaseline'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'UnsetUserAssessmentBaseline')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='UnsetUserAssessmentBaseline')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.unset_user_assessment_baseline(
                user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'UnsetUserAssessmentBaseline',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'unset_user_assessment_baseline',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_update_data_safe_private_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'UpdateDataSafePrivateEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'UpdateDataSafePrivateEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='UpdateDataSafePrivateEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.update_data_safe_private_endpoint(
                data_safe_private_endpoint_id=request.pop(util.camelize('dataSafePrivateEndpointId')),
                update_data_safe_private_endpoint_details=request.pop(util.camelize('UpdateDataSafePrivateEndpointDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'UpdateDataSafePrivateEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_data_safe_private_endpoint',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_update_on_prem_connector(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'UpdateOnPremConnector'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'UpdateOnPremConnector')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='UpdateOnPremConnector')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.update_on_prem_connector(
                on_prem_connector_id=request.pop(util.camelize('onPremConnectorId')),
                update_on_prem_connector_details=request.pop(util.camelize('UpdateOnPremConnectorDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'UpdateOnPremConnector',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_on_prem_connector',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_update_on_prem_connector_wallet(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'UpdateOnPremConnectorWallet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'UpdateOnPremConnectorWallet')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='UpdateOnPremConnectorWallet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.update_on_prem_connector_wallet(
                update_on_prem_connector_wallet_details=request.pop(util.camelize('UpdateOnPremConnectorWalletDetails')),
                on_prem_connector_id=request.pop(util.camelize('onPremConnectorId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'UpdateOnPremConnectorWallet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_on_prem_connector_wallet',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_update_security_assessment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'UpdateSecurityAssessment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'UpdateSecurityAssessment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='UpdateSecurityAssessment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.update_security_assessment(
                security_assessment_id=request.pop(util.camelize('securityAssessmentId')),
                update_security_assessment_details=request.pop(util.camelize('UpdateSecurityAssessmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'UpdateSecurityAssessment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_security_assessment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_update_target_database(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'UpdateTargetDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'UpdateTargetDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='UpdateTargetDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.update_target_database(
                target_database_id=request.pop(util.camelize('targetDatabaseId')),
                update_target_database_details=request.pop(util.camelize('UpdateTargetDatabaseDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'UpdateTargetDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_target_database',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_update_user_assessment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'UpdateUserAssessment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'UpdateUserAssessment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='UpdateUserAssessment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.update_user_assessment(
                user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                update_user_assessment_details=request.pop(util.camelize('UpdateUserAssessmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'UpdateUserAssessment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_user_assessment',
            False,
            False
        )
