# Code generated. DO NOT EDIT.
# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
def test_change_autonomous_database_insight_advanced_features(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ChangeAutonomousDatabaseInsightAdvancedFeatures'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ChangeAutonomousDatabaseInsightAdvancedFeatures')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ChangeAutonomousDatabaseInsightAdvancedFeatures')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.change_autonomous_database_insight_advanced_features(
                change_autonomous_database_insight_advanced_features_details=request.pop(util.camelize('ChangeAutonomousDatabaseInsightAdvancedFeaturesDetails')),
                database_insight_id=request.pop(util.camelize('databaseInsightId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ChangeAutonomousDatabaseInsightAdvancedFeatures',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_autonomous_database_insight_advanced_features',
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
def test_change_opsi_configuration_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ChangeOpsiConfigurationCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ChangeOpsiConfigurationCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ChangeOpsiConfigurationCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.change_opsi_configuration_compartment(
                opsi_configuration_id=request.pop(util.camelize('opsiConfigurationId')),
                change_opsi_configuration_compartment_details=request.pop(util.camelize('ChangeOpsiConfigurationCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ChangeOpsiConfigurationCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_opsi_configuration_compartment',
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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


# IssueRoutingInfo tag="default" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_create_opsi_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'CreateOpsiConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'CreateOpsiConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='CreateOpsiConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.create_opsi_configuration(
                create_opsi_configuration_details=request.pop(util.camelize('CreateOpsiConfigurationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'CreateOpsiConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'opsiConfiguration',
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
def test_delete_opsi_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'DeleteOpsiConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'DeleteOpsiConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='DeleteOpsiConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.delete_opsi_configuration(
                opsi_configuration_id=request.pop(util.camelize('opsiConfigurationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'DeleteOpsiConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_opsi_configuration',
            True,
            False
        )


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_disable_autonomous_database_insight_advanced_features(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'DisableAutonomousDatabaseInsightAdvancedFeatures'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'DisableAutonomousDatabaseInsightAdvancedFeatures')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='DisableAutonomousDatabaseInsightAdvancedFeatures')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.disable_autonomous_database_insight_advanced_features(
                database_insight_id=request.pop(util.camelize('databaseInsightId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'DisableAutonomousDatabaseInsightAdvancedFeatures',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'disable_autonomous_database_insight_advanced_features',
            False,
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
def test_enable_autonomous_database_insight_advanced_features(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'EnableAutonomousDatabaseInsightAdvancedFeatures'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'EnableAutonomousDatabaseInsightAdvancedFeatures')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='EnableAutonomousDatabaseInsightAdvancedFeatures')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.enable_autonomous_database_insight_advanced_features(
                enable_autonomous_database_insight_advanced_features_details=request.pop(util.camelize('EnableAutonomousDatabaseInsightAdvancedFeaturesDetails')),
                database_insight_id=request.pop(util.camelize('databaseInsightId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'EnableAutonomousDatabaseInsightAdvancedFeatures',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'enable_autonomous_database_insight_advanced_features',
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_get_awr_database_report(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'GetAwrDatabaseReport'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'GetAwrDatabaseReport')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='GetAwrDatabaseReport')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.get_awr_database_report(
                awr_hub_id=request.pop(util.camelize('awrHubId')),
                awr_source_database_identifier=request.pop(util.camelize('awrSourceDatabaseIdentifier')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'GetAwrDatabaseReport',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'awrDatabaseReport',
            False,
            False
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_get_awr_database_sql_report(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'GetAwrDatabaseSqlReport'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'GetAwrDatabaseSqlReport')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='GetAwrDatabaseSqlReport')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.get_awr_database_sql_report(
                awr_hub_id=request.pop(util.camelize('awrHubId')),
                awr_source_database_identifier=request.pop(util.camelize('awrSourceDatabaseIdentifier')),
                sql_id=request.pop(util.camelize('sqlId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'GetAwrDatabaseSqlReport',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'awrDatabaseSqlReport',
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
def test_get_opsi_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'GetOpsiConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'GetOpsiConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='GetOpsiConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.get_opsi_configuration(
                opsi_configuration_id=request.pop(util.camelize('opsiConfigurationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'GetOpsiConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'opsiConfiguration',
            False,
            False
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_get_opsi_data_object(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'GetOpsiDataObject'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'GetOpsiDataObject')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='GetOpsiDataObject')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.get_opsi_data_object(
                compartment_id=request.pop(util.camelize('compartmentId')),
                opsi_data_object_identifier=request.pop(util.camelize('opsiDataObjectIdentifier')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'GetOpsiDataObject',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'opsiDataObject',
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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


# IssueRoutingInfo tag="sqlLoader" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_ingest_addm_reports(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'IngestAddmReports'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'IngestAddmReports')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='IngestAddmReports')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.ingest_addm_reports(
                ingest_addm_reports_details=request.pop(util.camelize('IngestAddmReportsDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'IngestAddmReports',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'ingestAddmReportsResponseDetails',
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_list_addm_db_finding_categories(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ListAddmDbFindingCategories'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ListAddmDbFindingCategories')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ListAddmDbFindingCategories')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.list_addm_db_finding_categories(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_addm_db_finding_categories(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_addm_db_finding_categories(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ListAddmDbFindingCategories',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'addmDbFindingCategoryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_list_addm_db_findings_time_series(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ListAddmDbFindingsTimeSeries'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ListAddmDbFindingsTimeSeries')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ListAddmDbFindingsTimeSeries')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.list_addm_db_findings_time_series(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_addm_db_findings_time_series(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_addm_db_findings_time_series(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ListAddmDbFindingsTimeSeries',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'addmDbFindingsTimeSeriesCollection',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_list_addm_db_parameter_categories(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ListAddmDbParameterCategories'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ListAddmDbParameterCategories')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ListAddmDbParameterCategories')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.list_addm_db_parameter_categories(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_addm_db_parameter_categories(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_addm_db_parameter_categories(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ListAddmDbParameterCategories',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'addmDbParameterCategoryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_list_addm_db_recommendation_categories(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ListAddmDbRecommendationCategories'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ListAddmDbRecommendationCategories')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ListAddmDbRecommendationCategories')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.list_addm_db_recommendation_categories(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_addm_db_recommendation_categories(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_addm_db_recommendation_categories(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ListAddmDbRecommendationCategories',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'addmDbRecommendationCategoryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_list_addm_db_recommendations_time_series(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ListAddmDbRecommendationsTimeSeries'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ListAddmDbRecommendationsTimeSeries')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ListAddmDbRecommendationsTimeSeries')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.list_addm_db_recommendations_time_series(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_addm_db_recommendations_time_series(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_addm_db_recommendations_time_series(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ListAddmDbRecommendationsTimeSeries',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'addmDbRecommendationsTimeSeriesCollection',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_list_addm_dbs(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ListAddmDbs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ListAddmDbs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ListAddmDbs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.list_addm_dbs(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_addm_dbs(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_addm_dbs(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ListAddmDbs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'addmDbCollection',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_list_awr_database_snapshots(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ListAwrDatabaseSnapshots'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ListAwrDatabaseSnapshots')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ListAwrDatabaseSnapshots')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.list_awr_database_snapshots(
                awr_hub_id=request.pop(util.camelize('awrHubId')),
                awr_source_database_identifier=request.pop(util.camelize('awrSourceDatabaseIdentifier')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_awr_database_snapshots(
                    awr_hub_id=request.pop(util.camelize('awrHubId')),
                    awr_source_database_identifier=request.pop(util.camelize('awrSourceDatabaseIdentifier')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_awr_database_snapshots(
                        awr_hub_id=request.pop(util.camelize('awrHubId')),
                        awr_source_database_identifier=request.pop(util.camelize('awrSourceDatabaseIdentifier')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ListAwrDatabaseSnapshots',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'awrDatabaseSnapshotCollection',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_list_awr_databases(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ListAwrDatabases'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ListAwrDatabases')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ListAwrDatabases')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.list_awr_databases(
                awr_hub_id=request.pop(util.camelize('awrHubId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_awr_databases(
                    awr_hub_id=request.pop(util.camelize('awrHubId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_awr_databases(
                        awr_hub_id=request.pop(util.camelize('awrHubId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ListAwrDatabases',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'awrDatabaseCollection',
            False,
            True
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_awr_hubs(
                    operations_insights_warehouse_id=request.pop(util.camelize('operationsInsightsWarehouseId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_awr_hubs(
                        operations_insights_warehouse_id=request.pop(util.camelize('operationsInsightsWarehouseId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                    retry_strategy=oci.retry.NoneRetryStrategy(),
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
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_database_configurations(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_database_configurations(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_database_insights(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_database_insights(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_enterprise_manager_bridges(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_enterprise_manager_bridges(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_exadata_configurations(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_exadata_configurations(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_exadata_insights(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_exadata_insights(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_host_configurations(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_host_configurations(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_host_insights(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_host_insights(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                    retry_strategy=oci.retry.NoneRetryStrategy(),
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
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_importable_agent_entities(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_importable_agent_entities(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
def test_list_importable_compute_entities(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ListImportableComputeEntities'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ListImportableComputeEntities')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ListImportableComputeEntities')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.list_importable_compute_entities(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_importable_compute_entities(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_importable_compute_entities(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ListImportableComputeEntities',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'importableComputeEntitySummaryCollection',
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_importable_enterprise_manager_entities(
                    enterprise_manager_bridge_id=request.pop(util.camelize('enterpriseManagerBridgeId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_importable_enterprise_manager_entities(
                        enterprise_manager_bridge_id=request.pop(util.camelize('enterpriseManagerBridgeId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_operations_insights_private_endpoints(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_operations_insights_private_endpoints(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_operations_insights_warehouse_users(
                    operations_insights_warehouse_id=request.pop(util.camelize('operationsInsightsWarehouseId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_operations_insights_warehouse_users(
                        operations_insights_warehouse_id=request.pop(util.camelize('operationsInsightsWarehouseId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_operations_insights_warehouses(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_operations_insights_warehouses(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_list_opsi_configurations(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ListOpsiConfigurations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ListOpsiConfigurations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ListOpsiConfigurations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.list_opsi_configurations(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_opsi_configurations(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_opsi_configurations(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ListOpsiConfigurations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'opsiConfigurationsCollection',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_list_opsi_data_objects(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ListOpsiDataObjects'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ListOpsiDataObjects')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ListOpsiDataObjects')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.list_opsi_data_objects(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_opsi_data_objects(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_opsi_data_objects(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ListOpsiDataObjects',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'opsiDataObjectsCollection',
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                    retry_strategy=oci.retry.NoneRetryStrategy(),
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
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                    retry_strategy=oci.retry.NoneRetryStrategy(),
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
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                    retry_strategy=oci.retry.NoneRetryStrategy(),
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
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_errors(
                    work_request_id=request.pop(util.camelize('workRequestId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_request_errors(
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_logs(
                    work_request_id=request.pop(util.camelize('workRequestId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_request_logs(
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_requests(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_requests(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_query_opsi_data_object_data(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'QueryOpsiDataObjectData'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'QueryOpsiDataObjectData')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='QueryOpsiDataObjectData')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.query_opsi_data_object_data(
                compartment_id=request.pop(util.camelize('compartmentId')),
                query_opsi_data_object_data_details=request.pop(util.camelize('QueryOpsiDataObjectDataDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.query_opsi_data_object_data(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    query_opsi_data_object_data_details=request.pop(util.camelize('QueryOpsiDataObjectDataDetails')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.query_opsi_data_object_data(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        query_opsi_data_object_data_details=request.pop(util.camelize('QueryOpsiDataObjectDataDetails')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'QueryOpsiDataObjectData',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'queryDataObjectResultSetRowsCollection',
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_addm_db_findings(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeAddmDbFindings'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeAddmDbFindings')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeAddmDbFindings')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_addm_db_findings(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_addm_db_findings(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_addm_db_findings(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeAddmDbFindings',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'addmDbFindingAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_addm_db_parameter_changes(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeAddmDbParameterChanges'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeAddmDbParameterChanges')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeAddmDbParameterChanges')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_addm_db_parameter_changes(
                compartment_id=request.pop(util.camelize('compartmentId')),
                name=request.pop(util.camelize('name')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_addm_db_parameter_changes(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    name=request.pop(util.camelize('name')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_addm_db_parameter_changes(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        name=request.pop(util.camelize('name')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeAddmDbParameterChanges',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'addmDbParameterChangeAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_addm_db_parameters(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeAddmDbParameters'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeAddmDbParameters')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeAddmDbParameters')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_addm_db_parameters(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_addm_db_parameters(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_addm_db_parameters(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeAddmDbParameters',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'addmDbParameterAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_addm_db_recommendations(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeAddmDbRecommendations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeAddmDbRecommendations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeAddmDbRecommendations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_addm_db_recommendations(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_addm_db_recommendations(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_addm_db_recommendations(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeAddmDbRecommendations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'addmDbRecommendationAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_addm_db_schema_objects(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeAddmDbSchemaObjects'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeAddmDbSchemaObjects')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeAddmDbSchemaObjects')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_addm_db_schema_objects(
                compartment_id=request.pop(util.camelize('compartmentId')),
                object_identifier=request.pop(util.camelize('objectIdentifier')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_addm_db_schema_objects(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    object_identifier=request.pop(util.camelize('objectIdentifier')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_addm_db_schema_objects(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        object_identifier=request.pop(util.camelize('objectIdentifier')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeAddmDbSchemaObjects',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'addmDbSchemaObjectCollection',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_addm_db_sql_statements(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeAddmDbSqlStatements'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeAddmDbSqlStatements')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeAddmDbSqlStatements')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_addm_db_sql_statements(
                compartment_id=request.pop(util.camelize('compartmentId')),
                sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_addm_db_sql_statements(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_addm_db_sql_statements(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeAddmDbSqlStatements',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'addmDbSqlStatementCollection',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_awr_database_cpu_usages(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeAwrDatabaseCpuUsages'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeAwrDatabaseCpuUsages')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeAwrDatabaseCpuUsages')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_awr_database_cpu_usages(
                awr_hub_id=request.pop(util.camelize('awrHubId')),
                awr_source_database_identifier=request.pop(util.camelize('awrSourceDatabaseIdentifier')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_awr_database_cpu_usages(
                    awr_hub_id=request.pop(util.camelize('awrHubId')),
                    awr_source_database_identifier=request.pop(util.camelize('awrSourceDatabaseIdentifier')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_awr_database_cpu_usages(
                        awr_hub_id=request.pop(util.camelize('awrHubId')),
                        awr_source_database_identifier=request.pop(util.camelize('awrSourceDatabaseIdentifier')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeAwrDatabaseCpuUsages',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'awrDatabaseCpuUsageCollection',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_awr_database_metrics(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeAwrDatabaseMetrics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeAwrDatabaseMetrics')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeAwrDatabaseMetrics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_awr_database_metrics(
                awr_hub_id=request.pop(util.camelize('awrHubId')),
                awr_source_database_identifier=request.pop(util.camelize('awrSourceDatabaseIdentifier')),
                name=request.pop(util.camelize('name')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_awr_database_metrics(
                    awr_hub_id=request.pop(util.camelize('awrHubId')),
                    awr_source_database_identifier=request.pop(util.camelize('awrSourceDatabaseIdentifier')),
                    name=request.pop(util.camelize('name')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_awr_database_metrics(
                        awr_hub_id=request.pop(util.camelize('awrHubId')),
                        awr_source_database_identifier=request.pop(util.camelize('awrSourceDatabaseIdentifier')),
                        name=request.pop(util.camelize('name')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeAwrDatabaseMetrics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'awrDatabaseMetricCollection',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_awr_database_parameter_changes(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeAwrDatabaseParameterChanges'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeAwrDatabaseParameterChanges')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeAwrDatabaseParameterChanges')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_awr_database_parameter_changes(
                awr_hub_id=request.pop(util.camelize('awrHubId')),
                awr_source_database_identifier=request.pop(util.camelize('awrSourceDatabaseIdentifier')),
                name=request.pop(util.camelize('name')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_awr_database_parameter_changes(
                    awr_hub_id=request.pop(util.camelize('awrHubId')),
                    awr_source_database_identifier=request.pop(util.camelize('awrSourceDatabaseIdentifier')),
                    name=request.pop(util.camelize('name')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_awr_database_parameter_changes(
                        awr_hub_id=request.pop(util.camelize('awrHubId')),
                        awr_source_database_identifier=request.pop(util.camelize('awrSourceDatabaseIdentifier')),
                        name=request.pop(util.camelize('name')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeAwrDatabaseParameterChanges',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'awrDatabaseParameterChangeCollection',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_awr_database_parameters(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeAwrDatabaseParameters'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeAwrDatabaseParameters')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeAwrDatabaseParameters')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_awr_database_parameters(
                awr_hub_id=request.pop(util.camelize('awrHubId')),
                awr_source_database_identifier=request.pop(util.camelize('awrSourceDatabaseIdentifier')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_awr_database_parameters(
                    awr_hub_id=request.pop(util.camelize('awrHubId')),
                    awr_source_database_identifier=request.pop(util.camelize('awrSourceDatabaseIdentifier')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_awr_database_parameters(
                        awr_hub_id=request.pop(util.camelize('awrHubId')),
                        awr_source_database_identifier=request.pop(util.camelize('awrSourceDatabaseIdentifier')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeAwrDatabaseParameters',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'awrDatabaseParameterCollection',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_awr_database_snapshot_ranges(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeAwrDatabaseSnapshotRanges'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeAwrDatabaseSnapshotRanges')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeAwrDatabaseSnapshotRanges')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_awr_database_snapshot_ranges(
                awr_hub_id=request.pop(util.camelize('awrHubId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_awr_database_snapshot_ranges(
                    awr_hub_id=request.pop(util.camelize('awrHubId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_awr_database_snapshot_ranges(
                        awr_hub_id=request.pop(util.camelize('awrHubId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeAwrDatabaseSnapshotRanges',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'awrDatabaseSnapshotRangeCollection',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_awr_database_sysstats(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeAwrDatabaseSysstats'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeAwrDatabaseSysstats')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeAwrDatabaseSysstats')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_awr_database_sysstats(
                awr_hub_id=request.pop(util.camelize('awrHubId')),
                awr_source_database_identifier=request.pop(util.camelize('awrSourceDatabaseIdentifier')),
                name=request.pop(util.camelize('name')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_awr_database_sysstats(
                    awr_hub_id=request.pop(util.camelize('awrHubId')),
                    awr_source_database_identifier=request.pop(util.camelize('awrSourceDatabaseIdentifier')),
                    name=request.pop(util.camelize('name')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_awr_database_sysstats(
                        awr_hub_id=request.pop(util.camelize('awrHubId')),
                        awr_source_database_identifier=request.pop(util.camelize('awrSourceDatabaseIdentifier')),
                        name=request.pop(util.camelize('name')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeAwrDatabaseSysstats',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'awrDatabaseSysstatCollection',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_awr_database_top_wait_events(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeAwrDatabaseTopWaitEvents'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeAwrDatabaseTopWaitEvents')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeAwrDatabaseTopWaitEvents')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_awr_database_top_wait_events(
                awr_hub_id=request.pop(util.camelize('awrHubId')),
                awr_source_database_identifier=request.pop(util.camelize('awrSourceDatabaseIdentifier')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeAwrDatabaseTopWaitEvents',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'awrDatabaseTopWaitEventCollection',
            False,
            False
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_awr_database_wait_event_buckets(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeAwrDatabaseWaitEventBuckets'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeAwrDatabaseWaitEventBuckets')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeAwrDatabaseWaitEventBuckets')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_awr_database_wait_event_buckets(
                awr_hub_id=request.pop(util.camelize('awrHubId')),
                awr_source_database_identifier=request.pop(util.camelize('awrSourceDatabaseIdentifier')),
                name=request.pop(util.camelize('name')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_awr_database_wait_event_buckets(
                    awr_hub_id=request.pop(util.camelize('awrHubId')),
                    awr_source_database_identifier=request.pop(util.camelize('awrSourceDatabaseIdentifier')),
                    name=request.pop(util.camelize('name')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_awr_database_wait_event_buckets(
                        awr_hub_id=request.pop(util.camelize('awrHubId')),
                        awr_source_database_identifier=request.pop(util.camelize('awrSourceDatabaseIdentifier')),
                        name=request.pop(util.camelize('name')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeAwrDatabaseWaitEventBuckets',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'awrDatabaseWaitEventBucketCollection',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_awr_database_wait_events(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeAwrDatabaseWaitEvents'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeAwrDatabaseWaitEvents')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeAwrDatabaseWaitEvents')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_awr_database_wait_events(
                awr_hub_id=request.pop(util.camelize('awrHubId')),
                awr_source_database_identifier=request.pop(util.camelize('awrSourceDatabaseIdentifier')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_awr_database_wait_events(
                    awr_hub_id=request.pop(util.camelize('awrHubId')),
                    awr_source_database_identifier=request.pop(util.camelize('awrSourceDatabaseIdentifier')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_awr_database_wait_events(
                        awr_hub_id=request.pop(util.camelize('awrHubId')),
                        awr_source_database_identifier=request.pop(util.camelize('awrSourceDatabaseIdentifier')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeAwrDatabaseWaitEvents',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'awrDatabaseWaitEventCollection',
            False,
            True
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_awr_sources_summaries(
                    awr_hub_id=request.pop(util.camelize('awrHubId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_awr_sources_summaries(
                        awr_hub_id=request.pop(util.camelize('awrHubId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_configuration_items(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeConfigurationItems'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeConfigurationItems')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeConfigurationItems')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_configuration_items(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_configuration_items(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_configuration_items(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeConfigurationItems',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'configurationItemsCollection',
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                    retry_strategy=oci.retry.NoneRetryStrategy(),
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
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                    retry_strategy=oci.retry.NoneRetryStrategy(),
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
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                    retry_strategy=oci.retry.NoneRetryStrategy(),
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
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                    retry_strategy=oci.retry.NoneRetryStrategy(),
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
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                    retry_strategy=oci.retry.NoneRetryStrategy(),
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
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                    retry_strategy=oci.retry.NoneRetryStrategy(),
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
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_database_insight_tablespace_usage_trend(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_database_insight_tablespace_usage_trend(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                    retry_strategy=oci.retry.NoneRetryStrategy(),
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
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                    retry_strategy=oci.retry.NoneRetryStrategy(),
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
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                    retry_strategy=oci.retry.NoneRetryStrategy(),
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
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                    retry_strategy=oci.retry.NoneRetryStrategy(),
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
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                    retry_strategy=oci.retry.NoneRetryStrategy(),
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
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                    retry_strategy=oci.retry.NoneRetryStrategy(),
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
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                    retry_strategy=oci.retry.NoneRetryStrategy(),
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
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                    retry_strategy=oci.retry.NoneRetryStrategy(),
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
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_exadata_members(
                    exadata_insight_id=request.pop(util.camelize('exadataInsightId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_exadata_members(
                        exadata_insight_id=request.pop(util.camelize('exadataInsightId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
def test_summarize_host_insight_network_usage_trend(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeHostInsightNetworkUsageTrend'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeHostInsightNetworkUsageTrend')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeHostInsightNetworkUsageTrend')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_host_insight_network_usage_trend(
                compartment_id=request.pop(util.camelize('compartmentId')),
                id=request.pop(util.camelize('id')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_host_insight_network_usage_trend(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    id=request.pop(util.camelize('id')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_host_insight_network_usage_trend(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        id=request.pop(util.camelize('id')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeHostInsightNetworkUsageTrend',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'summarizeHostInsightNetworkUsageTrendAggregationCollection',
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                    retry_strategy=oci.retry.NoneRetryStrategy(),
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
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                    retry_strategy=oci.retry.NoneRetryStrategy(),
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
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                    retry_strategy=oci.retry.NoneRetryStrategy(),
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
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                    retry_strategy=oci.retry.NoneRetryStrategy(),
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
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                    retry_strategy=oci.retry.NoneRetryStrategy(),
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
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                    retry_strategy=oci.retry.NoneRetryStrategy(),
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
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
def test_summarize_host_insight_storage_usage_trend(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeHostInsightStorageUsageTrend'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeHostInsightStorageUsageTrend')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeHostInsightStorageUsageTrend')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_host_insight_storage_usage_trend(
                compartment_id=request.pop(util.camelize('compartmentId')),
                id=request.pop(util.camelize('id')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_host_insight_storage_usage_trend(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    id=request.pop(util.camelize('id')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_host_insight_storage_usage_trend(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        id=request.pop(util.camelize('id')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeHostInsightStorageUsageTrend',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'summarizeHostInsightStorageUsageTrendAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="resourcePlanning" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_host_insight_top_processes_usage(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeHostInsightTopProcessesUsage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeHostInsightTopProcessesUsage')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeHostInsightTopProcessesUsage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_host_insight_top_processes_usage(
                compartment_id=request.pop(util.camelize('compartmentId')),
                id=request.pop(util.camelize('id')),
                resource_metric=request.pop(util.camelize('resourceMetric')),
                timestamp=request.pop(util.camelize('timestamp')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_host_insight_top_processes_usage(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    id=request.pop(util.camelize('id')),
                    resource_metric=request.pop(util.camelize('resourceMetric')),
                    timestamp=request.pop(util.camelize('timestamp')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_host_insight_top_processes_usage(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        id=request.pop(util.camelize('id')),
                        resource_metric=request.pop(util.camelize('resourceMetric')),
                        timestamp=request.pop(util.camelize('timestamp')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeHostInsightTopProcessesUsage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'summarizeHostInsightsTopProcessesUsageCollection',
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                    retry_strategy=oci.retry.NoneRetryStrategy(),
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
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_sql_insights(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_sql_insights(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                    retry_strategy=oci.retry.NoneRetryStrategy(),
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
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                    retry_strategy=oci.retry.NoneRetryStrategy(),
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
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_sql_statistics(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_sql_statistics(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                    retry_strategy=oci.retry.NoneRetryStrategy(),
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
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                    retry_strategy=oci.retry.NoneRetryStrategy(),
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
                        retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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
                retry_strategy=oci.retry.NoneRetryStrategy(),
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


# IssueRoutingInfo tag="controlPlane" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_update_opsi_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'UpdateOpsiConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'UpdateOpsiConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='UpdateOpsiConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.update_opsi_configuration(
                opsi_configuration_id=request.pop(util.camelize('opsiConfigurationId')),
                update_opsi_configuration_details=request.pop(util.camelize('UpdateOpsiConfigurationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'UpdateOpsiConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_opsi_configuration',
            False,
            False
        )
