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

        cassette_location = os.path.join('generated', 'opsi_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_change_database_insight_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ChangeDatabaseInsightCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ChangeDatabaseInsightCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ChangeDatabaseInsightCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.change_database_insight_compartment(
                database_insight_id=request.pop(util.camelize('databaseInsightId')),
                change_database_insight_compartment_details=request.pop(util.camelize('ChangeDatabaseInsightCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ChangeDatabaseInsightCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_database_insight_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_change_enterprise_manager_bridge_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ChangeEnterpriseManagerBridgeCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ChangeEnterpriseManagerBridgeCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ChangeEnterpriseManagerBridgeCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.change_enterprise_manager_bridge_compartment(
                enterprise_manager_bridge_id=request.pop(util.camelize('enterpriseManagerBridgeId')),
                change_enterprise_manager_bridge_compartment_details=request.pop(util.camelize('ChangeEnterpriseManagerBridgeCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ChangeEnterpriseManagerBridgeCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_enterprise_manager_bridge_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_change_host_insight_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ChangeHostInsightCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ChangeHostInsightCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ChangeHostInsightCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.change_host_insight_compartment(
                host_insight_id=request.pop(util.camelize('hostInsightId')),
                change_host_insight_compartment_details=request.pop(util.camelize('ChangeHostInsightCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ChangeHostInsightCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_host_insight_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_create_database_insight(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'CreateDatabaseInsight'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'CreateDatabaseInsight')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='CreateDatabaseInsight')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.create_database_insight(
                create_database_insight_details=request.pop(util.camelize('CreateDatabaseInsightDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'CreateDatabaseInsight',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'databaseInsight',
            False,
            False
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_create_enterprise_manager_bridge(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'CreateEnterpriseManagerBridge'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'CreateEnterpriseManagerBridge')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='CreateEnterpriseManagerBridge')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.create_enterprise_manager_bridge(
                create_enterprise_manager_bridge_details=request.pop(util.camelize('CreateEnterpriseManagerBridgeDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'CreateEnterpriseManagerBridge',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'enterpriseManagerBridge',
            False,
            False
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_create_host_insight(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'CreateHostInsight'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'CreateHostInsight')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='CreateHostInsight')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.create_host_insight(
                create_host_insight_details=request.pop(util.camelize('CreateHostInsightDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'CreateHostInsight',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'hostInsight',
            False,
            False
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_delete_database_insight(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'DeleteDatabaseInsight'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'DeleteDatabaseInsight')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='DeleteDatabaseInsight')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.delete_database_insight(
                database_insight_id=request.pop(util.camelize('databaseInsightId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'DeleteDatabaseInsight',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_database_insight',
            True,
            False
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_delete_enterprise_manager_bridge(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'DeleteEnterpriseManagerBridge'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'DeleteEnterpriseManagerBridge')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='DeleteEnterpriseManagerBridge')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.delete_enterprise_manager_bridge(
                enterprise_manager_bridge_id=request.pop(util.camelize('enterpriseManagerBridgeId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'DeleteEnterpriseManagerBridge',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_enterprise_manager_bridge',
            True,
            False
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_delete_host_insight(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'DeleteHostInsight'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'DeleteHostInsight')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='DeleteHostInsight')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.delete_host_insight(
                host_insight_id=request.pop(util.camelize('hostInsightId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'DeleteHostInsight',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_host_insight',
            True,
            False
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_disable_database_insight(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'DisableDatabaseInsight'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'DisableDatabaseInsight')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='DisableDatabaseInsight')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.disable_database_insight(
                database_insight_id=request.pop(util.camelize('databaseInsightId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'DisableDatabaseInsight',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'disable_database_insight',
            False,
            False
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_disable_host_insight(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'DisableHostInsight'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'DisableHostInsight')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='DisableHostInsight')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.disable_host_insight(
                host_insight_id=request.pop(util.camelize('hostInsightId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'DisableHostInsight',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'disable_host_insight',
            False,
            False
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_enable_database_insight(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'EnableDatabaseInsight'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'EnableDatabaseInsight')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='EnableDatabaseInsight')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.enable_database_insight(
                enable_database_insight_details=request.pop(util.camelize('EnableDatabaseInsightDetails')),
                database_insight_id=request.pop(util.camelize('databaseInsightId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'EnableDatabaseInsight',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'enable_database_insight',
            False,
            False
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_enable_host_insight(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'EnableHostInsight'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'EnableHostInsight')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='EnableHostInsight')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.enable_host_insight(
                enable_host_insight_details=request.pop(util.camelize('EnableHostInsightDetails')),
                host_insight_id=request.pop(util.camelize('hostInsightId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'EnableHostInsight',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'enable_host_insight',
            False,
            False
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_get_database_insight(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'GetDatabaseInsight'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'GetDatabaseInsight')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='GetDatabaseInsight')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.get_database_insight(
                database_insight_id=request.pop(util.camelize('databaseInsightId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'GetDatabaseInsight',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'databaseInsight',
            False,
            False
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_get_enterprise_manager_bridge(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'GetEnterpriseManagerBridge'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'GetEnterpriseManagerBridge')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='GetEnterpriseManagerBridge')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.get_enterprise_manager_bridge(
                enterprise_manager_bridge_id=request.pop(util.camelize('enterpriseManagerBridgeId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'GetEnterpriseManagerBridge',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'enterpriseManagerBridge',
            False,
            False
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_get_host_insight(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'GetHostInsight'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'GetHostInsight')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='GetHostInsight')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.get_host_insight(
                host_insight_id=request.pop(util.camelize('hostInsightId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'GetHostInsight',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'hostInsight',
            False,
            False
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="resourcePlanning" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_ingest_database_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'IngestDatabaseConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'IngestDatabaseConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='IngestDatabaseConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.ingest_database_configuration(
                ingest_database_configuration_details=request.pop(util.camelize('IngestDatabaseConfigurationDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'IngestDatabaseConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'ingestDatabaseConfigurationResponseDetails',
            False,
            False
        )


# IssueRoutingInfo tag="sqlLoader" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_ingest_host_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'IngestHostConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'IngestHostConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='IngestHostConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.ingest_host_configuration(
                id=request.pop(util.camelize('id')),
                ingest_host_configuration_details=request.pop(util.camelize('IngestHostConfigurationDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'IngestHostConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'ingestHostConfigurationResponseDetails',
            False,
            False
        )


# IssueRoutingInfo tag="sqlLoader" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_ingest_host_metrics(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'IngestHostMetrics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'IngestHostMetrics')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='IngestHostMetrics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.ingest_host_metrics(
                id=request.pop(util.camelize('id')),
                ingest_host_metrics_details=request.pop(util.camelize('IngestHostMetricsDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'IngestHostMetrics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'ingestHostMetricsResponseDetails',
            False,
            False
        )


# IssueRoutingInfo tag="sqlLoader" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_ingest_sql_bucket(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'IngestSqlBucket'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'IngestSqlBucket')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='IngestSqlBucket')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.ingest_sql_bucket(
                ingest_sql_bucket_details=request.pop(util.camelize('IngestSqlBucketDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'IngestSqlBucket',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'ingestSqlBucketResponseDetails',
            False,
            False
        )


# IssueRoutingInfo tag="sqlLoader" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_ingest_sql_plan_lines(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'IngestSqlPlanLines'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'IngestSqlPlanLines')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='IngestSqlPlanLines')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.ingest_sql_plan_lines(
                ingest_sql_plan_lines_details=request.pop(util.camelize('IngestSqlPlanLinesDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'IngestSqlPlanLines',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'ingestSqlPlanLinesResponseDetails',
            False,
            False
        )


# IssueRoutingInfo tag="sqlLoader" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_ingest_sql_text(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'IngestSqlText'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'IngestSqlText')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='IngestSqlText')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.ingest_sql_text(
                ingest_sql_text_details=request.pop(util.camelize('IngestSqlTextDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'IngestSqlText',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'ingestSqlTextResponseDetails',
            False,
            False
        )


# IssueRoutingInfo tag="resourcePlanning" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_list_database_configurations(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ListDatabaseConfigurations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ListDatabaseConfigurations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ListDatabaseConfigurations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.list_database_configurations(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_database_configurations(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_database_configurations(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ListDatabaseConfigurations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'databaseConfigurationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_list_database_insights(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ListDatabaseInsights'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ListDatabaseInsights')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ListDatabaseInsights')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.list_database_insights(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_database_insights(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_database_insights(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ListDatabaseInsights',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'databaseInsightsCollection',
            False,
            True
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_list_enterprise_manager_bridges(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ListEnterpriseManagerBridges'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ListEnterpriseManagerBridges')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ListEnterpriseManagerBridges')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.list_enterprise_manager_bridges(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_enterprise_manager_bridges(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_enterprise_manager_bridges(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ListEnterpriseManagerBridges',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'enterpriseManagerBridgeCollection',
            False,
            True
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_list_host_insights(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ListHostInsights'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ListHostInsights')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ListHostInsights')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.list_host_insights(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_host_insights(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_host_insights(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ListHostInsights',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'hostInsightSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="resourcePlanning" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_list_hosted_entities(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ListHostedEntities'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ListHostedEntities')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ListHostedEntities')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.list_hosted_entities(
                compartment_id=request.pop(util.camelize('compartmentId')),
                id=request.pop(util.camelize('id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_hosted_entities(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    id=request.pop(util.camelize('id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_hosted_entities(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        id=request.pop(util.camelize('id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ListHostedEntities',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'hostedEntityCollection',
            False,
            True
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_list_importable_agent_entities(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ListImportableAgentEntities'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ListImportableAgentEntities')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ListImportableAgentEntities')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.list_importable_agent_entities(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_importable_agent_entities(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_importable_agent_entities(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ListImportableAgentEntities',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'importableAgentEntitySummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_list_importable_enterprise_manager_entities(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ListImportableEnterpriseManagerEntities'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ListImportableEnterpriseManagerEntities')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ListImportableEnterpriseManagerEntities')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.list_importable_enterprise_manager_entities(
                enterprise_manager_bridge_id=request.pop(util.camelize('enterpriseManagerBridgeId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_importable_enterprise_manager_entities(
                    enterprise_manager_bridge_id=request.pop(util.camelize('enterpriseManagerBridgeId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_importable_enterprise_manager_entities(
                        enterprise_manager_bridge_id=request.pop(util.camelize('enterpriseManagerBridgeId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ListImportableEnterpriseManagerEntities',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'importableEnterpriseManagerEntityCollection',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_list_sql_plans(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ListSqlPlans'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ListSqlPlans')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ListSqlPlans')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.list_sql_plans(
                compartment_id=request.pop(util.camelize('compartmentId')),
                sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                plan_hash=request.pop(util.camelize('planHash')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_sql_plans(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                    plan_hash=request.pop(util.camelize('planHash')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_sql_plans(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                        plan_hash=request.pop(util.camelize('planHash')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ListSqlPlans',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sqlPlanCollection',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_list_sql_searches(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ListSqlSearches'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ListSqlSearches')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ListSqlSearches')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.list_sql_searches(
                compartment_id=request.pop(util.camelize('compartmentId')),
                sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_sql_searches(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_sql_searches(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ListSqlSearches',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sqlSearchCollection',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_list_sql_texts(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ListSqlTexts'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ListSqlTexts')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ListSqlTexts')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.list_sql_texts(
                compartment_id=request.pop(util.camelize('compartmentId')),
                sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_sql_texts(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_sql_texts(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ListSqlTexts',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sqlTextCollection',
            False,
            True
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
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
            'opsi',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestErrorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
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
            'opsi',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
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
            'opsi',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestCollection',
            False,
            True
        )


# IssueRoutingInfo tag="resourcePlanning" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_database_insight_resource_capacity_trend(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeDatabaseInsightResourceCapacityTrend'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeDatabaseInsightResourceCapacityTrend')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeDatabaseInsightResourceCapacityTrend')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_database_insight_resource_capacity_trend(
                compartment_id=request.pop(util.camelize('compartmentId')),
                resource_metric=request.pop(util.camelize('resourceMetric')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_database_insight_resource_capacity_trend(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    resource_metric=request.pop(util.camelize('resourceMetric')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_database_insight_resource_capacity_trend(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        resource_metric=request.pop(util.camelize('resourceMetric')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeDatabaseInsightResourceCapacityTrend',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'summarizeDatabaseInsightResourceCapacityTrendAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="resourcePlanning" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_database_insight_resource_forecast_trend(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeDatabaseInsightResourceForecastTrend'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeDatabaseInsightResourceForecastTrend')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeDatabaseInsightResourceForecastTrend')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_database_insight_resource_forecast_trend(
                compartment_id=request.pop(util.camelize('compartmentId')),
                resource_metric=request.pop(util.camelize('resourceMetric')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_database_insight_resource_forecast_trend(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    resource_metric=request.pop(util.camelize('resourceMetric')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_database_insight_resource_forecast_trend(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        resource_metric=request.pop(util.camelize('resourceMetric')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeDatabaseInsightResourceForecastTrend',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'summarizeDatabaseInsightResourceForecastTrendAggregation',
            False,
            True
        )


# IssueRoutingInfo tag="resourcePlanning" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_database_insight_resource_statistics(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeDatabaseInsightResourceStatistics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeDatabaseInsightResourceStatistics')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeDatabaseInsightResourceStatistics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_database_insight_resource_statistics(
                compartment_id=request.pop(util.camelize('compartmentId')),
                resource_metric=request.pop(util.camelize('resourceMetric')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_database_insight_resource_statistics(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    resource_metric=request.pop(util.camelize('resourceMetric')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_database_insight_resource_statistics(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        resource_metric=request.pop(util.camelize('resourceMetric')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeDatabaseInsightResourceStatistics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'summarizeDatabaseInsightResourceStatisticsAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="resourcePlanning" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_database_insight_resource_usage(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeDatabaseInsightResourceUsage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeDatabaseInsightResourceUsage')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeDatabaseInsightResourceUsage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_database_insight_resource_usage(
                compartment_id=request.pop(util.camelize('compartmentId')),
                resource_metric=request.pop(util.camelize('resourceMetric')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_database_insight_resource_usage(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    resource_metric=request.pop(util.camelize('resourceMetric')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_database_insight_resource_usage(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        resource_metric=request.pop(util.camelize('resourceMetric')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeDatabaseInsightResourceUsage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'summarizeDatabaseInsightResourceUsageAggregation',
            False,
            True
        )


# IssueRoutingInfo tag="resourcePlanning" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_database_insight_resource_usage_trend(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeDatabaseInsightResourceUsageTrend'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeDatabaseInsightResourceUsageTrend')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeDatabaseInsightResourceUsageTrend')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_database_insight_resource_usage_trend(
                compartment_id=request.pop(util.camelize('compartmentId')),
                resource_metric=request.pop(util.camelize('resourceMetric')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_database_insight_resource_usage_trend(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    resource_metric=request.pop(util.camelize('resourceMetric')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_database_insight_resource_usage_trend(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        resource_metric=request.pop(util.camelize('resourceMetric')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeDatabaseInsightResourceUsageTrend',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'summarizeDatabaseInsightResourceUsageTrendAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="resourcePlanning" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_database_insight_resource_utilization_insight(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeDatabaseInsightResourceUtilizationInsight'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeDatabaseInsightResourceUtilizationInsight')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeDatabaseInsightResourceUtilizationInsight')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_database_insight_resource_utilization_insight(
                compartment_id=request.pop(util.camelize('compartmentId')),
                resource_metric=request.pop(util.camelize('resourceMetric')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_database_insight_resource_utilization_insight(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    resource_metric=request.pop(util.camelize('resourceMetric')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_database_insight_resource_utilization_insight(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        resource_metric=request.pop(util.camelize('resourceMetric')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeDatabaseInsightResourceUtilizationInsight',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'summarizeDatabaseInsightResourceUtilizationInsightAggregation',
            False,
            True
        )


# IssueRoutingInfo tag="resourcePlanning" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_database_insight_tablespace_usage_trend(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeDatabaseInsightTablespaceUsageTrend'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeDatabaseInsightTablespaceUsageTrend')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeDatabaseInsightTablespaceUsageTrend')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_database_insight_tablespace_usage_trend(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_database_insight_tablespace_usage_trend(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_database_insight_tablespace_usage_trend(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeDatabaseInsightTablespaceUsageTrend',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'summarizeDatabaseInsightTablespaceUsageTrendAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="resourcePlanning" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_host_insight_resource_capacity_trend(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeHostInsightResourceCapacityTrend'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeHostInsightResourceCapacityTrend')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeHostInsightResourceCapacityTrend')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_host_insight_resource_capacity_trend(
                compartment_id=request.pop(util.camelize('compartmentId')),
                resource_metric=request.pop(util.camelize('resourceMetric')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_host_insight_resource_capacity_trend(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    resource_metric=request.pop(util.camelize('resourceMetric')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_host_insight_resource_capacity_trend(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        resource_metric=request.pop(util.camelize('resourceMetric')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeHostInsightResourceCapacityTrend',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'summarizeHostInsightResourceCapacityTrendAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="resourcePlanning" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_host_insight_resource_forecast_trend(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeHostInsightResourceForecastTrend'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeHostInsightResourceForecastTrend')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeHostInsightResourceForecastTrend')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_host_insight_resource_forecast_trend(
                compartment_id=request.pop(util.camelize('compartmentId')),
                resource_metric=request.pop(util.camelize('resourceMetric')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_host_insight_resource_forecast_trend(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    resource_metric=request.pop(util.camelize('resourceMetric')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_host_insight_resource_forecast_trend(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        resource_metric=request.pop(util.camelize('resourceMetric')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeHostInsightResourceForecastTrend',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'summarizeHostInsightResourceForecastTrendAggregation',
            False,
            True
        )


# IssueRoutingInfo tag="resourcePlanning" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_host_insight_resource_statistics(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeHostInsightResourceStatistics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeHostInsightResourceStatistics')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeHostInsightResourceStatistics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_host_insight_resource_statistics(
                compartment_id=request.pop(util.camelize('compartmentId')),
                resource_metric=request.pop(util.camelize('resourceMetric')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_host_insight_resource_statistics(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    resource_metric=request.pop(util.camelize('resourceMetric')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_host_insight_resource_statistics(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        resource_metric=request.pop(util.camelize('resourceMetric')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeHostInsightResourceStatistics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'summarizeHostInsightResourceStatisticsAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="resourcePlanning" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_host_insight_resource_usage(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeHostInsightResourceUsage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeHostInsightResourceUsage')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeHostInsightResourceUsage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_host_insight_resource_usage(
                compartment_id=request.pop(util.camelize('compartmentId')),
                resource_metric=request.pop(util.camelize('resourceMetric')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_host_insight_resource_usage(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    resource_metric=request.pop(util.camelize('resourceMetric')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_host_insight_resource_usage(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        resource_metric=request.pop(util.camelize('resourceMetric')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeHostInsightResourceUsage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'summarizeHostInsightResourceUsageAggregation',
            False,
            True
        )


# IssueRoutingInfo tag="resourcePlanning" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_host_insight_resource_usage_trend(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeHostInsightResourceUsageTrend'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeHostInsightResourceUsageTrend')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeHostInsightResourceUsageTrend')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_host_insight_resource_usage_trend(
                compartment_id=request.pop(util.camelize('compartmentId')),
                resource_metric=request.pop(util.camelize('resourceMetric')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_host_insight_resource_usage_trend(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    resource_metric=request.pop(util.camelize('resourceMetric')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_host_insight_resource_usage_trend(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        resource_metric=request.pop(util.camelize('resourceMetric')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeHostInsightResourceUsageTrend',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'summarizeHostInsightResourceUsageTrendAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="resourcePlanning" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_host_insight_resource_utilization_insight(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeHostInsightResourceUtilizationInsight'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeHostInsightResourceUtilizationInsight')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeHostInsightResourceUtilizationInsight')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_host_insight_resource_utilization_insight(
                compartment_id=request.pop(util.camelize('compartmentId')),
                resource_metric=request.pop(util.camelize('resourceMetric')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_host_insight_resource_utilization_insight(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    resource_metric=request.pop(util.camelize('resourceMetric')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_host_insight_resource_utilization_insight(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        resource_metric=request.pop(util.camelize('resourceMetric')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeHostInsightResourceUtilizationInsight',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'summarizeHostInsightResourceUtilizationInsightAggregation',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_sql_insights(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeSqlInsights'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeSqlInsights')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeSqlInsights')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_sql_insights(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_sql_insights(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_sql_insights(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeSqlInsights',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sqlInsightAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_sql_plan_insights(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeSqlPlanInsights'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeSqlPlanInsights')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeSqlPlanInsights')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_sql_plan_insights(
                compartment_id=request.pop(util.camelize('compartmentId')),
                sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_sql_plan_insights(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_sql_plan_insights(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeSqlPlanInsights',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sqlPlanInsightAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_sql_response_time_distributions(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeSqlResponseTimeDistributions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeSqlResponseTimeDistributions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeSqlResponseTimeDistributions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_sql_response_time_distributions(
                compartment_id=request.pop(util.camelize('compartmentId')),
                sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_sql_response_time_distributions(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_sql_response_time_distributions(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeSqlResponseTimeDistributions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sqlResponseTimeDistributionAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_sql_statistics(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeSqlStatistics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeSqlStatistics')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeSqlStatistics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_sql_statistics(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_sql_statistics(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_sql_statistics(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeSqlStatistics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sqlStatisticAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_sql_statistics_time_series(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeSqlStatisticsTimeSeries'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeSqlStatisticsTimeSeries')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeSqlStatisticsTimeSeries')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_sql_statistics_time_series(
                compartment_id=request.pop(util.camelize('compartmentId')),
                sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_sql_statistics_time_series(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_sql_statistics_time_series(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeSqlStatisticsTimeSeries',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sqlStatisticsTimeSeriesAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_sql_statistics_time_series_by_plan(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeSqlStatisticsTimeSeriesByPlan'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeSqlStatisticsTimeSeriesByPlan')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeSqlStatisticsTimeSeriesByPlan')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_sql_statistics_time_series_by_plan(
                compartment_id=request.pop(util.camelize('compartmentId')),
                sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_sql_statistics_time_series_by_plan(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_sql_statistics_time_series_by_plan(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeSqlStatisticsTimeSeriesByPlan',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sqlStatisticsTimeSeriesByPlanAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_update_database_insight(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'UpdateDatabaseInsight'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'UpdateDatabaseInsight')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='UpdateDatabaseInsight')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.update_database_insight(
                database_insight_id=request.pop(util.camelize('databaseInsightId')),
                update_database_insight_details=request.pop(util.camelize('UpdateDatabaseInsightDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'UpdateDatabaseInsight',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_database_insight',
            False,
            False
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_update_enterprise_manager_bridge(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'UpdateEnterpriseManagerBridge'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'UpdateEnterpriseManagerBridge')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='UpdateEnterpriseManagerBridge')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.update_enterprise_manager_bridge(
                enterprise_manager_bridge_id=request.pop(util.camelize('enterpriseManagerBridgeId')),
                update_enterprise_manager_bridge_details=request.pop(util.camelize('UpdateEnterpriseManagerBridgeDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'UpdateEnterpriseManagerBridge',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_enterprise_manager_bridge',
            False,
            False
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_update_host_insight(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'UpdateHostInsight'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'UpdateHostInsight')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='UpdateHostInsight')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.update_host_insight(
                host_insight_id=request.pop(util.camelize('hostInsightId')),
                update_host_insight_details=request.pop(util.camelize('UpdateHostInsightDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'UpdateHostInsight',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_host_insight',
            False,
            False
        )
