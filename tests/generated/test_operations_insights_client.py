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

        cassette_location = os.path.join('generated', 'opsi_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_add_exadata_insight_members(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'AddExadataInsightMembers'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'AddExadataInsightMembers')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='AddExadataInsightMembers')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.add_exadata_insight_members(
                add_exadata_insight_members_details=request.pop(util.camelize('AddExadataInsightMembersDetails')),
                exadata_insight_id=request.pop(util.camelize('exadataInsightId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'AddExadataInsightMembers',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'add_exadata_insight_members',
            False,
            False
        )


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
def test_change_exadata_insight_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ChangeExadataInsightCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ChangeExadataInsightCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ChangeExadataInsightCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.change_exadata_insight_compartment(
                exadata_insight_id=request.pop(util.camelize('exadataInsightId')),
                change_exadata_insight_compartment_details=request.pop(util.camelize('ChangeExadataInsightCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ChangeExadataInsightCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_exadata_insight_compartment',
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
def test_change_operations_insights_private_endpoint_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ChangeOperationsInsightsPrivateEndpointCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ChangeOperationsInsightsPrivateEndpointCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ChangeOperationsInsightsPrivateEndpointCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.change_operations_insights_private_endpoint_compartment(
                operations_insights_private_endpoint_id=request.pop(util.camelize('operationsInsightsPrivateEndpointId')),
                change_operations_insights_private_endpoint_compartment_details=request.pop(util.camelize('ChangeOperationsInsightsPrivateEndpointCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ChangeOperationsInsightsPrivateEndpointCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_operations_insights_private_endpoint_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_change_pe_comanaged_database_insight(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ChangePeComanagedDatabaseInsight'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ChangePeComanagedDatabaseInsight')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ChangePeComanagedDatabaseInsight')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.change_pe_comanaged_database_insight(
                database_insight_id=request.pop(util.camelize('databaseInsightId')),
                change_pe_comanaged_database_insight_details=request.pop(util.camelize('ChangePeComanagedDatabaseInsightDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ChangePeComanagedDatabaseInsight',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_pe_comanaged_database_insight',
            False,
            False
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_create_awr_hub(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'CreateAwrHub'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'CreateAwrHub')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='CreateAwrHub')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.create_awr_hub(
                create_awr_hub_details=request.pop(util.camelize('CreateAwrHubDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'CreateAwrHub',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'awrHub',
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
def test_create_exadata_insight(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'CreateExadataInsight'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'CreateExadataInsight')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='CreateExadataInsight')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.create_exadata_insight(
                create_exadata_insight_details=request.pop(util.camelize('CreateExadataInsightDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'CreateExadataInsight',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'exadataInsight',
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
def test_create_operations_insights_private_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'CreateOperationsInsightsPrivateEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'CreateOperationsInsightsPrivateEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='CreateOperationsInsightsPrivateEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.create_operations_insights_private_endpoint(
                create_operations_insights_private_endpoint_details=request.pop(util.camelize('CreateOperationsInsightsPrivateEndpointDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'CreateOperationsInsightsPrivateEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'operationsInsightsPrivateEndpoint',
            False,
            False
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_create_operations_insights_warehouse(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'CreateOperationsInsightsWarehouse'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'CreateOperationsInsightsWarehouse')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='CreateOperationsInsightsWarehouse')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.create_operations_insights_warehouse(
                create_operations_insights_warehouse_details=request.pop(util.camelize('CreateOperationsInsightsWarehouseDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'CreateOperationsInsightsWarehouse',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'operationsInsightsWarehouse',
            False,
            False
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_create_operations_insights_warehouse_user(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'CreateOperationsInsightsWarehouseUser'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'CreateOperationsInsightsWarehouseUser')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='CreateOperationsInsightsWarehouseUser')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.create_operations_insights_warehouse_user(
                create_operations_insights_warehouse_user_details=request.pop(util.camelize('CreateOperationsInsightsWarehouseUserDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'CreateOperationsInsightsWarehouseUser',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'operationsInsightsWarehouseUser',
            False,
            False
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_delete_awr_hub(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'DeleteAwrHub'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'DeleteAwrHub')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='DeleteAwrHub')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.delete_awr_hub(
                awr_hub_id=request.pop(util.camelize('awrHubId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'DeleteAwrHub',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_awr_hub',
            True,
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
def test_delete_exadata_insight(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'DeleteExadataInsight'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'DeleteExadataInsight')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='DeleteExadataInsight')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.delete_exadata_insight(
                exadata_insight_id=request.pop(util.camelize('exadataInsightId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'DeleteExadataInsight',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_exadata_insight',
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
def test_delete_operations_insights_private_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'DeleteOperationsInsightsPrivateEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'DeleteOperationsInsightsPrivateEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='DeleteOperationsInsightsPrivateEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.delete_operations_insights_private_endpoint(
                operations_insights_private_endpoint_id=request.pop(util.camelize('operationsInsightsPrivateEndpointId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'DeleteOperationsInsightsPrivateEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_operations_insights_private_endpoint',
            True,
            False
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_delete_operations_insights_warehouse(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'DeleteOperationsInsightsWarehouse'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'DeleteOperationsInsightsWarehouse')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='DeleteOperationsInsightsWarehouse')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.delete_operations_insights_warehouse(
                operations_insights_warehouse_id=request.pop(util.camelize('operationsInsightsWarehouseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'DeleteOperationsInsightsWarehouse',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_operations_insights_warehouse',
            True,
            False
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_delete_operations_insights_warehouse_user(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'DeleteOperationsInsightsWarehouseUser'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'DeleteOperationsInsightsWarehouseUser')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='DeleteOperationsInsightsWarehouseUser')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.delete_operations_insights_warehouse_user(
                operations_insights_warehouse_user_id=request.pop(util.camelize('operationsInsightsWarehouseUserId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'DeleteOperationsInsightsWarehouseUser',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_operations_insights_warehouse_user',
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
def test_disable_exadata_insight(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'DisableExadataInsight'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'DisableExadataInsight')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='DisableExadataInsight')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.disable_exadata_insight(
                exadata_insight_id=request.pop(util.camelize('exadataInsightId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'DisableExadataInsight',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'disable_exadata_insight',
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
def test_download_operations_insights_warehouse_wallet(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'DownloadOperationsInsightsWarehouseWallet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'DownloadOperationsInsightsWarehouseWallet')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='DownloadOperationsInsightsWarehouseWallet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.download_operations_insights_warehouse_wallet(
                operations_insights_warehouse_id=request.pop(util.camelize('operationsInsightsWarehouseId')),
                download_operations_insights_warehouse_wallet_details=request.pop(util.camelize('DownloadOperationsInsightsWarehouseWalletDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'DownloadOperationsInsightsWarehouseWallet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
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
def test_enable_exadata_insight(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'EnableExadataInsight'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'EnableExadataInsight')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='EnableExadataInsight')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.enable_exadata_insight(
                enable_exadata_insight_details=request.pop(util.camelize('EnableExadataInsightDetails')),
                exadata_insight_id=request.pop(util.camelize('exadataInsightId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'EnableExadataInsight',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'enable_exadata_insight',
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
def test_get_awr_hub(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'GetAwrHub'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'GetAwrHub')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='GetAwrHub')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.get_awr_hub(
                awr_hub_id=request.pop(util.camelize('awrHubId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'GetAwrHub',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'awrHub',
            False,
            False
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_get_awr_report(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'GetAwrReport'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'GetAwrReport')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='GetAwrReport')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.get_awr_report(
                awr_hub_id=request.pop(util.camelize('awrHubId')),
                awr_source_database_identifier=request.pop(util.camelize('awrSourceDatabaseIdentifier')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'GetAwrReport',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'awrReport',
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
def test_get_exadata_insight(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'GetExadataInsight'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'GetExadataInsight')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='GetExadataInsight')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.get_exadata_insight(
                exadata_insight_id=request.pop(util.camelize('exadataInsightId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'GetExadataInsight',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'exadataInsight',
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
def test_get_operations_insights_private_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'GetOperationsInsightsPrivateEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'GetOperationsInsightsPrivateEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='GetOperationsInsightsPrivateEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.get_operations_insights_private_endpoint(
                operations_insights_private_endpoint_id=request.pop(util.camelize('operationsInsightsPrivateEndpointId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'GetOperationsInsightsPrivateEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'operationsInsightsPrivateEndpoint',
            False,
            False
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_get_operations_insights_warehouse(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'GetOperationsInsightsWarehouse'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'GetOperationsInsightsWarehouse')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='GetOperationsInsightsWarehouse')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.get_operations_insights_warehouse(
                operations_insights_warehouse_id=request.pop(util.camelize('operationsInsightsWarehouseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'GetOperationsInsightsWarehouse',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'operationsInsightsWarehouse',
            False,
            False
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_get_operations_insights_warehouse_user(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'GetOperationsInsightsWarehouseUser'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'GetOperationsInsightsWarehouseUser')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='GetOperationsInsightsWarehouseUser')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.get_operations_insights_warehouse_user(
                operations_insights_warehouse_user_id=request.pop(util.camelize('operationsInsightsWarehouseUserId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'GetOperationsInsightsWarehouseUser',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'operationsInsightsWarehouseUser',
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
def test_ingest_sql_stats(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'IngestSqlStats'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'IngestSqlStats')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='IngestSqlStats')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.ingest_sql_stats(
                ingest_sql_stats_details=request.pop(util.camelize('IngestSqlStatsDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'IngestSqlStats',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'ingestSqlStatsResponseDetails',
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


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_list_awr_hubs(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ListAwrHubs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ListAwrHubs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ListAwrHubs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.list_awr_hubs(
                operations_insights_warehouse_id=request.pop(util.camelize('operationsInsightsWarehouseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_awr_hubs(
                    operations_insights_warehouse_id=request.pop(util.camelize('operationsInsightsWarehouseId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_awr_hubs(
                        operations_insights_warehouse_id=request.pop(util.camelize('operationsInsightsWarehouseId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ListAwrHubs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'awrHubSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_list_awr_snapshots(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ListAwrSnapshots'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ListAwrSnapshots')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ListAwrSnapshots')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.list_awr_snapshots(
                awr_hub_id=request.pop(util.camelize('awrHubId')),
                awr_source_database_identifier=request.pop(util.camelize('awrSourceDatabaseIdentifier')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_awr_snapshots(
                    awr_hub_id=request.pop(util.camelize('awrHubId')),
                    awr_source_database_identifier=request.pop(util.camelize('awrSourceDatabaseIdentifier')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_awr_snapshots(
                        awr_hub_id=request.pop(util.camelize('awrHubId')),
                        awr_source_database_identifier=request.pop(util.camelize('awrSourceDatabaseIdentifier')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ListAwrSnapshots',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'awrSnapshotCollection',
            False,
            True
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


# IssueRoutingInfo tag="resourcePlanning" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_list_exadata_configurations(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ListExadataConfigurations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ListExadataConfigurations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ListExadataConfigurations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.list_exadata_configurations(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_exadata_configurations(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_exadata_configurations(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ListExadataConfigurations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'exadataConfigurationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_list_exadata_insights(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ListExadataInsights'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ListExadataInsights')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ListExadataInsights')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.list_exadata_insights(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_exadata_insights(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_exadata_insights(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ListExadataInsights',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'exadataInsightSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="resourcePlanning" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_list_host_configurations(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ListHostConfigurations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ListHostConfigurations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ListHostConfigurations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.list_host_configurations(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_host_configurations(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_host_configurations(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ListHostConfigurations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'hostConfigurationCollection',
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


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_list_operations_insights_private_endpoints(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ListOperationsInsightsPrivateEndpoints'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ListOperationsInsightsPrivateEndpoints')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ListOperationsInsightsPrivateEndpoints')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.list_operations_insights_private_endpoints(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_operations_insights_private_endpoints(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_operations_insights_private_endpoints(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ListOperationsInsightsPrivateEndpoints',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'operationsInsightsPrivateEndpointCollection',
            False,
            True
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_list_operations_insights_warehouse_users(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ListOperationsInsightsWarehouseUsers'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ListOperationsInsightsWarehouseUsers')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ListOperationsInsightsWarehouseUsers')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.list_operations_insights_warehouse_users(
                operations_insights_warehouse_id=request.pop(util.camelize('operationsInsightsWarehouseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_operations_insights_warehouse_users(
                    operations_insights_warehouse_id=request.pop(util.camelize('operationsInsightsWarehouseId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_operations_insights_warehouse_users(
                        operations_insights_warehouse_id=request.pop(util.camelize('operationsInsightsWarehouseId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ListOperationsInsightsWarehouseUsers',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'operationsInsightsWarehouseUserSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_list_operations_insights_warehouses(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ListOperationsInsightsWarehouses'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ListOperationsInsightsWarehouses')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ListOperationsInsightsWarehouses')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.list_operations_insights_warehouses(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_operations_insights_warehouses(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_operations_insights_warehouses(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ListOperationsInsightsWarehouses',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'operationsInsightsWarehouseSummaryCollection',
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
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_requests(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_requests(
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


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_rotate_operations_insights_warehouse_wallet(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'RotateOperationsInsightsWarehouseWallet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'RotateOperationsInsightsWarehouseWallet')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='RotateOperationsInsightsWarehouseWallet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.rotate_operations_insights_warehouse_wallet(
                operations_insights_warehouse_id=request.pop(util.camelize('operationsInsightsWarehouseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'RotateOperationsInsightsWarehouseWallet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'rotate_operations_insights_warehouse_wallet',
            False,
            False
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_awr_sources_summaries(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeAwrSourcesSummaries'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeAwrSourcesSummaries')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeAwrSourcesSummaries')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_awr_sources_summaries(
                awr_hub_id=request.pop(util.camelize('awrHubId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_awr_sources_summaries(
                    awr_hub_id=request.pop(util.camelize('awrHubId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_awr_sources_summaries(
                        awr_hub_id=request.pop(util.camelize('awrHubId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeAwrSourcesSummaries',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'summarizeAwrSourcesSummariesCollection',
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
def test_summarize_exadata_insight_resource_capacity_trend(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeExadataInsightResourceCapacityTrend'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeExadataInsightResourceCapacityTrend')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeExadataInsightResourceCapacityTrend')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_exadata_insight_resource_capacity_trend(
                resource_type=request.pop(util.camelize('resourceType')),
                resource_metric=request.pop(util.camelize('resourceMetric')),
                exadata_insight_id=request.pop(util.camelize('exadataInsightId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_exadata_insight_resource_capacity_trend(
                    resource_type=request.pop(util.camelize('resourceType')),
                    resource_metric=request.pop(util.camelize('resourceMetric')),
                    exadata_insight_id=request.pop(util.camelize('exadataInsightId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_exadata_insight_resource_capacity_trend(
                        resource_type=request.pop(util.camelize('resourceType')),
                        resource_metric=request.pop(util.camelize('resourceMetric')),
                        exadata_insight_id=request.pop(util.camelize('exadataInsightId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeExadataInsightResourceCapacityTrend',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'summarizeExadataInsightResourceCapacityTrendCollection',
            False,
            True
        )


# IssueRoutingInfo tag="resourcePlanning" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_exadata_insight_resource_capacity_trend_aggregated(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeExadataInsightResourceCapacityTrendAggregated'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeExadataInsightResourceCapacityTrendAggregated')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeExadataInsightResourceCapacityTrendAggregated')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_exadata_insight_resource_capacity_trend_aggregated(
                resource_type=request.pop(util.camelize('resourceType')),
                resource_metric=request.pop(util.camelize('resourceMetric')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_exadata_insight_resource_capacity_trend_aggregated(
                    resource_type=request.pop(util.camelize('resourceType')),
                    resource_metric=request.pop(util.camelize('resourceMetric')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_exadata_insight_resource_capacity_trend_aggregated(
                        resource_type=request.pop(util.camelize('resourceType')),
                        resource_metric=request.pop(util.camelize('resourceMetric')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeExadataInsightResourceCapacityTrendAggregated',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'summarizeExadataInsightResourceCapacityTrendAggregation',
            False,
            True
        )


# IssueRoutingInfo tag="resourcePlanning" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_exadata_insight_resource_forecast_trend(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeExadataInsightResourceForecastTrend'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeExadataInsightResourceForecastTrend')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeExadataInsightResourceForecastTrend')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_exadata_insight_resource_forecast_trend(
                resource_type=request.pop(util.camelize('resourceType')),
                resource_metric=request.pop(util.camelize('resourceMetric')),
                exadata_insight_id=request.pop(util.camelize('exadataInsightId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_exadata_insight_resource_forecast_trend(
                    resource_type=request.pop(util.camelize('resourceType')),
                    resource_metric=request.pop(util.camelize('resourceMetric')),
                    exadata_insight_id=request.pop(util.camelize('exadataInsightId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_exadata_insight_resource_forecast_trend(
                        resource_type=request.pop(util.camelize('resourceType')),
                        resource_metric=request.pop(util.camelize('resourceMetric')),
                        exadata_insight_id=request.pop(util.camelize('exadataInsightId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeExadataInsightResourceForecastTrend',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'summarizeExadataInsightResourceForecastTrendCollection',
            False,
            True
        )


# IssueRoutingInfo tag="resourcePlanning" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_exadata_insight_resource_forecast_trend_aggregated(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeExadataInsightResourceForecastTrendAggregated'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeExadataInsightResourceForecastTrendAggregated')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeExadataInsightResourceForecastTrendAggregated')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_exadata_insight_resource_forecast_trend_aggregated(
                resource_type=request.pop(util.camelize('resourceType')),
                resource_metric=request.pop(util.camelize('resourceMetric')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_exadata_insight_resource_forecast_trend_aggregated(
                    resource_type=request.pop(util.camelize('resourceType')),
                    resource_metric=request.pop(util.camelize('resourceMetric')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_exadata_insight_resource_forecast_trend_aggregated(
                        resource_type=request.pop(util.camelize('resourceType')),
                        resource_metric=request.pop(util.camelize('resourceMetric')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeExadataInsightResourceForecastTrendAggregated',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'summarizeExadataInsightResourceForecastTrendAggregation',
            False,
            True
        )


# IssueRoutingInfo tag="resourcePlanning" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_exadata_insight_resource_statistics(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeExadataInsightResourceStatistics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeExadataInsightResourceStatistics')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeExadataInsightResourceStatistics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_exadata_insight_resource_statistics(
                exadata_insight_id=request.pop(util.camelize('exadataInsightId')),
                resource_type=request.pop(util.camelize('resourceType')),
                resource_metric=request.pop(util.camelize('resourceMetric')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_exadata_insight_resource_statistics(
                    exadata_insight_id=request.pop(util.camelize('exadataInsightId')),
                    resource_type=request.pop(util.camelize('resourceType')),
                    resource_metric=request.pop(util.camelize('resourceMetric')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_exadata_insight_resource_statistics(
                        exadata_insight_id=request.pop(util.camelize('exadataInsightId')),
                        resource_type=request.pop(util.camelize('resourceType')),
                        resource_metric=request.pop(util.camelize('resourceMetric')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeExadataInsightResourceStatistics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'summarizeExadataInsightResourceStatisticsAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="resourcePlanning" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_exadata_insight_resource_usage(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeExadataInsightResourceUsage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeExadataInsightResourceUsage')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeExadataInsightResourceUsage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_exadata_insight_resource_usage(
                compartment_id=request.pop(util.camelize('compartmentId')),
                resource_type=request.pop(util.camelize('resourceType')),
                resource_metric=request.pop(util.camelize('resourceMetric')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_exadata_insight_resource_usage(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    resource_type=request.pop(util.camelize('resourceType')),
                    resource_metric=request.pop(util.camelize('resourceMetric')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_exadata_insight_resource_usage(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        resource_type=request.pop(util.camelize('resourceType')),
                        resource_metric=request.pop(util.camelize('resourceMetric')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeExadataInsightResourceUsage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'summarizeExadataInsightResourceUsageCollection',
            False,
            True
        )


# IssueRoutingInfo tag="resourcePlanning" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_exadata_insight_resource_usage_aggregated(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeExadataInsightResourceUsageAggregated'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeExadataInsightResourceUsageAggregated')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeExadataInsightResourceUsageAggregated')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_exadata_insight_resource_usage_aggregated(
                compartment_id=request.pop(util.camelize('compartmentId')),
                resource_type=request.pop(util.camelize('resourceType')),
                resource_metric=request.pop(util.camelize('resourceMetric')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_exadata_insight_resource_usage_aggregated(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    resource_type=request.pop(util.camelize('resourceType')),
                    resource_metric=request.pop(util.camelize('resourceMetric')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_exadata_insight_resource_usage_aggregated(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        resource_type=request.pop(util.camelize('resourceType')),
                        resource_metric=request.pop(util.camelize('resourceMetric')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeExadataInsightResourceUsageAggregated',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'summarizeExadataInsightResourceUsageAggregation',
            False,
            True
        )


# IssueRoutingInfo tag="resourcePlanning" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_exadata_insight_resource_utilization_insight(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeExadataInsightResourceUtilizationInsight'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeExadataInsightResourceUtilizationInsight')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeExadataInsightResourceUtilizationInsight')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_exadata_insight_resource_utilization_insight(
                compartment_id=request.pop(util.camelize('compartmentId')),
                resource_type=request.pop(util.camelize('resourceType')),
                resource_metric=request.pop(util.camelize('resourceMetric')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_exadata_insight_resource_utilization_insight(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    resource_type=request.pop(util.camelize('resourceType')),
                    resource_metric=request.pop(util.camelize('resourceMetric')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_exadata_insight_resource_utilization_insight(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        resource_type=request.pop(util.camelize('resourceType')),
                        resource_metric=request.pop(util.camelize('resourceMetric')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeExadataInsightResourceUtilizationInsight',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'summarizeExadataInsightResourceUtilizationInsightAggregation',
            False,
            True
        )


# IssueRoutingInfo tag="resourcePlanning" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_exadata_members(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeExadataMembers'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeExadataMembers')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeExadataMembers')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_exadata_members(
                exadata_insight_id=request.pop(util.camelize('exadataInsightId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_exadata_members(
                    exadata_insight_id=request.pop(util.camelize('exadataInsightId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_exadata_members(
                        exadata_insight_id=request.pop(util.camelize('exadataInsightId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeExadataMembers',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'exadataMemberCollection',
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


# IssueRoutingInfo tag="resourcePlanning" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_host_insight_top_processes_usage_trend(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeHostInsightTopProcessesUsageTrend'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeHostInsightTopProcessesUsageTrend')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeHostInsightTopProcessesUsageTrend')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_host_insight_top_processes_usage_trend(
                compartment_id=request.pop(util.camelize('compartmentId')),
                id=request.pop(util.camelize('id')),
                resource_metric=request.pop(util.camelize('resourceMetric')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_host_insight_top_processes_usage_trend(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    id=request.pop(util.camelize('id')),
                    resource_metric=request.pop(util.camelize('resourceMetric')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_host_insight_top_processes_usage_trend(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        id=request.pop(util.camelize('id')),
                        resource_metric=request.pop(util.camelize('resourceMetric')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeHostInsightTopProcessesUsageTrend',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'summarizeHostInsightsTopProcessesUsageTrendCollection',
            False,
            True
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_operations_insights_warehouse_resource_usage(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeOperationsInsightsWarehouseResourceUsage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeOperationsInsightsWarehouseResourceUsage')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeOperationsInsightsWarehouseResourceUsage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_operations_insights_warehouse_resource_usage(
                operations_insights_warehouse_id=request.pop(util.camelize('operationsInsightsWarehouseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeOperationsInsightsWarehouseResourceUsage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'summarizeOperationsInsightsWarehouseResourceUsageAggregation',
            False,
            False
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
def test_update_awr_hub(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'UpdateAwrHub'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'UpdateAwrHub')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='UpdateAwrHub')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.update_awr_hub(
                awr_hub_id=request.pop(util.camelize('awrHubId')),
                update_awr_hub_details=request.pop(util.camelize('UpdateAwrHubDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'UpdateAwrHub',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_awr_hub',
            False,
            False
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
def test_update_exadata_insight(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'UpdateExadataInsight'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'UpdateExadataInsight')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='UpdateExadataInsight')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.update_exadata_insight(
                exadata_insight_id=request.pop(util.camelize('exadataInsightId')),
                update_exadata_insight_details=request.pop(util.camelize('UpdateExadataInsightDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'UpdateExadataInsight',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_exadata_insight',
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


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_update_operations_insights_private_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'UpdateOperationsInsightsPrivateEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'UpdateOperationsInsightsPrivateEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='UpdateOperationsInsightsPrivateEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.update_operations_insights_private_endpoint(
                operations_insights_private_endpoint_id=request.pop(util.camelize('operationsInsightsPrivateEndpointId')),
                update_operations_insights_private_endpoint_details=request.pop(util.camelize('UpdateOperationsInsightsPrivateEndpointDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'UpdateOperationsInsightsPrivateEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_operations_insights_private_endpoint',
            False,
            False
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_update_operations_insights_warehouse(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'UpdateOperationsInsightsWarehouse'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'UpdateOperationsInsightsWarehouse')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='UpdateOperationsInsightsWarehouse')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.update_operations_insights_warehouse(
                operations_insights_warehouse_id=request.pop(util.camelize('operationsInsightsWarehouseId')),
                update_operations_insights_warehouse_details=request.pop(util.camelize('UpdateOperationsInsightsWarehouseDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'UpdateOperationsInsightsWarehouse',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_operations_insights_warehouse',
            False,
            False
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_update_operations_insights_warehouse_user(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'UpdateOperationsInsightsWarehouseUser'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'UpdateOperationsInsightsWarehouseUser')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='UpdateOperationsInsightsWarehouseUser')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.update_operations_insights_warehouse_user(
                operations_insights_warehouse_user_id=request.pop(util.camelize('operationsInsightsWarehouseUserId')),
                update_operations_insights_warehouse_user_details=request.pop(util.camelize('UpdateOperationsInsightsWarehouseUserDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'UpdateOperationsInsightsWarehouseUser',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_operations_insights_warehouse_user',
            False,
            False
        )
