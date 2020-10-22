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

        cassette_location = os.path.join('generated', 'database_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_activate_exadata_infrastructure(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ActivateExadataInfrastructure'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ActivateExadataInfrastructure')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ActivateExadataInfrastructure')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.activate_exadata_infrastructure(
                exadata_infrastructure_id=request.pop(util.camelize('exadataInfrastructureId')),
                activate_exadata_infrastructure_details=request.pop(util.camelize('ActivateExadataInfrastructureDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ActivateExadataInfrastructure',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'exadataInfrastructure',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-adb" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_autonomous_database_manual_refresh(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'AutonomousDatabaseManualRefresh'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'AutonomousDatabaseManualRefresh')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='AutonomousDatabaseManualRefresh')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.autonomous_database_manual_refresh(
                autonomous_database_id=request.pop(util.camelize('autonomousDatabaseId')),
                autonomous_database_manual_refresh_details=request.pop(util.camelize('AutonomousDatabaseManualRefreshDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'AutonomousDatabaseManualRefresh',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousDatabase',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-atp-d" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_change_autonomous_container_database_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ChangeAutonomousContainerDatabaseCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ChangeAutonomousContainerDatabaseCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ChangeAutonomousContainerDatabaseCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.change_autonomous_container_database_compartment(
                change_compartment_details=request.pop(util.camelize('ChangeCompartmentDetails')),
                autonomous_container_database_id=request.pop(util.camelize('autonomousContainerDatabaseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ChangeAutonomousContainerDatabaseCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_autonomous_container_database_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-adb" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_change_autonomous_database_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ChangeAutonomousDatabaseCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ChangeAutonomousDatabaseCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ChangeAutonomousDatabaseCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.change_autonomous_database_compartment(
                change_compartment_details=request.pop(util.camelize('ChangeCompartmentDetails')),
                autonomous_database_id=request.pop(util.camelize('autonomousDatabaseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ChangeAutonomousDatabaseCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_autonomous_database_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-atp-d" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_change_autonomous_exadata_infrastructure_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ChangeAutonomousExadataInfrastructureCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ChangeAutonomousExadataInfrastructureCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ChangeAutonomousExadataInfrastructureCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.change_autonomous_exadata_infrastructure_compartment(
                change_compartment_details=request.pop(util.camelize('ChangeCompartmentDetails')),
                autonomous_exadata_infrastructure_id=request.pop(util.camelize('autonomousExadataInfrastructureId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ChangeAutonomousExadataInfrastructureCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_autonomous_exadata_infrastructure_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_change_autonomous_vm_cluster_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ChangeAutonomousVmClusterCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ChangeAutonomousVmClusterCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ChangeAutonomousVmClusterCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.change_autonomous_vm_cluster_compartment(
                change_autonomous_vm_cluster_compartment_details=request.pop(util.camelize('ChangeAutonomousVmClusterCompartmentDetails')),
                autonomous_vm_cluster_id=request.pop(util.camelize('autonomousVmClusterId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ChangeAutonomousVmClusterCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_autonomous_vm_cluster_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_change_backup_destination_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ChangeBackupDestinationCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ChangeBackupDestinationCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ChangeBackupDestinationCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.change_backup_destination_compartment(
                change_compartment_details=request.pop(util.camelize('ChangeCompartmentDetails')),
                backup_destination_id=request.pop(util.camelize('backupDestinationId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ChangeBackupDestinationCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_backup_destination_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="ExaCS" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_change_cloud_exadata_infrastructure_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ChangeCloudExadataInfrastructureCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ChangeCloudExadataInfrastructureCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ChangeCloudExadataInfrastructureCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.change_cloud_exadata_infrastructure_compartment(
                change_cloud_exadata_infrastructure_compartment_details=request.pop(util.camelize('ChangeCloudExadataInfrastructureCompartmentDetails')),
                cloud_exadata_infrastructure_id=request.pop(util.camelize('cloudExadataInfrastructureId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ChangeCloudExadataInfrastructureCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_cloud_exadata_infrastructure_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="ExaCS" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_change_cloud_vm_cluster_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ChangeCloudVmClusterCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ChangeCloudVmClusterCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ChangeCloudVmClusterCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.change_cloud_vm_cluster_compartment(
                change_cloud_vm_cluster_compartment_details=request.pop(util.camelize('ChangeCloudVmClusterCompartmentDetails')),
                cloud_vm_cluster_id=request.pop(util.camelize('cloudVmClusterId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ChangeCloudVmClusterCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_cloud_vm_cluster_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_change_database_software_image_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ChangeDatabaseSoftwareImageCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ChangeDatabaseSoftwareImageCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ChangeDatabaseSoftwareImageCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.change_database_software_image_compartment(
                change_compartment_details=request.pop(util.camelize('ChangeCompartmentDetails')),
                database_software_image_id=request.pop(util.camelize('databaseSoftwareImageId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ChangeDatabaseSoftwareImageCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_database_software_image_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_change_db_system_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ChangeDbSystemCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ChangeDbSystemCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ChangeDbSystemCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.change_db_system_compartment(
                change_compartment_details=request.pop(util.camelize('ChangeCompartmentDetails')),
                db_system_id=request.pop(util.camelize('dbSystemId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ChangeDbSystemCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_db_system_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_change_exadata_infrastructure_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ChangeExadataInfrastructureCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ChangeExadataInfrastructureCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ChangeExadataInfrastructureCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.change_exadata_infrastructure_compartment(
                change_exadata_infrastructure_compartment_details=request.pop(util.camelize('ChangeExadataInfrastructureCompartmentDetails')),
                exadata_infrastructure_id=request.pop(util.camelize('exadataInfrastructureId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ChangeExadataInfrastructureCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_exadata_infrastructure_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_change_key_store_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ChangeKeyStoreCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ChangeKeyStoreCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ChangeKeyStoreCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.change_key_store_compartment(
                change_key_store_compartment_details=request.pop(util.camelize('ChangeKeyStoreCompartmentDetails')),
                key_store_id=request.pop(util.camelize('keyStoreId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ChangeKeyStoreCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_key_store_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_change_vm_cluster_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ChangeVmClusterCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ChangeVmClusterCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ChangeVmClusterCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.change_vm_cluster_compartment(
                change_vm_cluster_compartment_details=request.pop(util.camelize('ChangeVmClusterCompartmentDetails')),
                vm_cluster_id=request.pop(util.camelize('vmClusterId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ChangeVmClusterCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_vm_cluster_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_complete_external_backup_job(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'CompleteExternalBackupJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'CompleteExternalBackupJob')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='CompleteExternalBackupJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.complete_external_backup_job(
                backup_id=request.pop(util.camelize('backupId')),
                complete_external_backup_job_details=request.pop(util.camelize('CompleteExternalBackupJobDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'CompleteExternalBackupJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalBackupJob',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-atp-d" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_create_autonomous_container_database(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'CreateAutonomousContainerDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'CreateAutonomousContainerDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='CreateAutonomousContainerDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.create_autonomous_container_database(
                create_autonomous_container_database_details=request.pop(util.camelize('CreateAutonomousContainerDatabaseDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'CreateAutonomousContainerDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousContainerDatabase',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_create_autonomous_data_warehouse(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'CreateAutonomousDataWarehouse'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'CreateAutonomousDataWarehouse')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='CreateAutonomousDataWarehouse')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.create_autonomous_data_warehouse(
                create_autonomous_data_warehouse_details=request.pop(util.camelize('CreateAutonomousDataWarehouseDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'CreateAutonomousDataWarehouse',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousDataWarehouse',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_create_autonomous_data_warehouse_backup(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'CreateAutonomousDataWarehouseBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'CreateAutonomousDataWarehouseBackup')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='CreateAutonomousDataWarehouseBackup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.create_autonomous_data_warehouse_backup(
                create_autonomous_data_warehouse_backup_details=request.pop(util.camelize('CreateAutonomousDataWarehouseBackupDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'CreateAutonomousDataWarehouseBackup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousDataWarehouseBackup',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-adb" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_create_autonomous_database(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'CreateAutonomousDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'CreateAutonomousDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='CreateAutonomousDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.create_autonomous_database(
                create_autonomous_database_details=request.pop(util.camelize('CreateAutonomousDatabaseDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'CreateAutonomousDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousDatabase',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-adb" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_create_autonomous_database_backup(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'CreateAutonomousDatabaseBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'CreateAutonomousDatabaseBackup')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='CreateAutonomousDatabaseBackup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.create_autonomous_database_backup(
                create_autonomous_database_backup_details=request.pop(util.camelize('CreateAutonomousDatabaseBackupDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'CreateAutonomousDatabaseBackup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousDatabaseBackup',
            False,
            False
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_create_autonomous_vm_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'CreateAutonomousVmCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'CreateAutonomousVmCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='CreateAutonomousVmCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.create_autonomous_vm_cluster(
                create_autonomous_vm_cluster_details=request.pop(util.camelize('CreateAutonomousVmClusterDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'CreateAutonomousVmCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousVmCluster',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_create_backup(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'CreateBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'CreateBackup')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='CreateBackup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.create_backup(
                create_backup_details=request.pop(util.camelize('CreateBackupDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'CreateBackup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'backup',
            False,
            False
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_create_backup_destination(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'CreateBackupDestination'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'CreateBackupDestination')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='CreateBackupDestination')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.create_backup_destination(
                create_backup_destination_details=request.pop(util.camelize('CreateBackupDestinationDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'CreateBackupDestination',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'backupDestination',
            False,
            False
        )


# IssueRoutingInfo tag="ExaCS" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_create_cloud_exadata_infrastructure(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'CreateCloudExadataInfrastructure'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'CreateCloudExadataInfrastructure')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='CreateCloudExadataInfrastructure')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.create_cloud_exadata_infrastructure(
                create_cloud_exadata_infrastructure_details=request.pop(util.camelize('CreateCloudExadataInfrastructureDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'CreateCloudExadataInfrastructure',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cloudExadataInfrastructure',
            False,
            False
        )


# IssueRoutingInfo tag="ExaCS" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_create_cloud_vm_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'CreateCloudVmCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'CreateCloudVmCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='CreateCloudVmCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.create_cloud_vm_cluster(
                create_cloud_vm_cluster_details=request.pop(util.camelize('CreateCloudVmClusterDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'CreateCloudVmCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cloudVmCluster',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_create_console_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'CreateConsoleConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'CreateConsoleConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='CreateConsoleConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.create_console_connection(
                create_console_connection_details=request.pop(util.camelize('CreateConsoleConnectionDetails')),
                db_node_id=request.pop(util.camelize('dbNodeId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'CreateConsoleConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'consoleConnection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_create_data_guard_association(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'CreateDataGuardAssociation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'CreateDataGuardAssociation')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='CreateDataGuardAssociation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.create_data_guard_association(
                database_id=request.pop(util.camelize('databaseId')),
                create_data_guard_association_details=request.pop(util.camelize('CreateDataGuardAssociationDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'CreateDataGuardAssociation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataGuardAssociation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_create_database(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'CreateDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'CreateDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='CreateDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.create_database(
                create_new_database_details=request.pop(util.camelize('CreateNewDatabaseDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'CreateDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'database',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_create_database_software_image(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'CreateDatabaseSoftwareImage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'CreateDatabaseSoftwareImage')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='CreateDatabaseSoftwareImage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.create_database_software_image(
                create_database_software_image_details=request.pop(util.camelize('CreateDatabaseSoftwareImageDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'CreateDatabaseSoftwareImage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'databaseSoftwareImage',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_create_db_home(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'CreateDbHome'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'CreateDbHome')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='CreateDbHome')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.create_db_home(
                create_db_home_with_db_system_id_details=request.pop(util.camelize('CreateDbHomeWithDbSystemIdDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'CreateDbHome',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dbHome',
            False,
            False
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_create_exadata_infrastructure(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'CreateExadataInfrastructure'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'CreateExadataInfrastructure')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='CreateExadataInfrastructure')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.create_exadata_infrastructure(
                create_exadata_infrastructure_details=request.pop(util.camelize('CreateExadataInfrastructureDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'CreateExadataInfrastructure',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'exadataInfrastructure',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_create_external_backup_job(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'CreateExternalBackupJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'CreateExternalBackupJob')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='CreateExternalBackupJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.create_external_backup_job(
                create_external_backup_job_details=request.pop(util.camelize('CreateExternalBackupJobDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'CreateExternalBackupJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalBackupJob',
            False,
            False
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_create_key_store(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'CreateKeyStore'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'CreateKeyStore')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='CreateKeyStore')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.create_key_store(
                create_key_store_details=request.pop(util.camelize('CreateKeyStoreDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'CreateKeyStore',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'keyStore',
            False,
            False
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_create_vm_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'CreateVmCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'CreateVmCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='CreateVmCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.create_vm_cluster(
                create_vm_cluster_details=request.pop(util.camelize('CreateVmClusterDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'CreateVmCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'vmCluster',
            False,
            False
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_create_vm_cluster_network(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'CreateVmClusterNetwork'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'CreateVmClusterNetwork')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='CreateVmClusterNetwork')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.create_vm_cluster_network(
                exadata_infrastructure_id=request.pop(util.camelize('exadataInfrastructureId')),
                vm_cluster_network_details=request.pop(util.camelize('VmClusterNetworkDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'CreateVmClusterNetwork',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'vmClusterNetwork',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_db_node_action(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'DbNodeAction'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'DbNodeAction')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='DbNodeAction')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.db_node_action(
                db_node_id=request.pop(util.camelize('dbNodeId')),
                action=request.pop(util.camelize('action')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'DbNodeAction',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dbNode',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_delete_autonomous_data_warehouse(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'DeleteAutonomousDataWarehouse'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'DeleteAutonomousDataWarehouse')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='DeleteAutonomousDataWarehouse')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.delete_autonomous_data_warehouse(
                autonomous_data_warehouse_id=request.pop(util.camelize('autonomousDataWarehouseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'DeleteAutonomousDataWarehouse',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_autonomous_data_warehouse',
            True,
            False
        )


# IssueRoutingInfo tag="dbaas-adb" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_delete_autonomous_database(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'DeleteAutonomousDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'DeleteAutonomousDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='DeleteAutonomousDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.delete_autonomous_database(
                autonomous_database_id=request.pop(util.camelize('autonomousDatabaseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'DeleteAutonomousDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_autonomous_database',
            True,
            False
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_delete_autonomous_vm_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'DeleteAutonomousVmCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'DeleteAutonomousVmCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='DeleteAutonomousVmCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.delete_autonomous_vm_cluster(
                autonomous_vm_cluster_id=request.pop(util.camelize('autonomousVmClusterId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'DeleteAutonomousVmCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_autonomous_vm_cluster',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_delete_backup(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'DeleteBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'DeleteBackup')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='DeleteBackup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.delete_backup(
                backup_id=request.pop(util.camelize('backupId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'DeleteBackup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_backup',
            True,
            False
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_delete_backup_destination(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'DeleteBackupDestination'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'DeleteBackupDestination')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='DeleteBackupDestination')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.delete_backup_destination(
                backup_destination_id=request.pop(util.camelize('backupDestinationId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'DeleteBackupDestination',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_backup_destination',
            True,
            False
        )


# IssueRoutingInfo tag="ExaCS" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_delete_cloud_exadata_infrastructure(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'DeleteCloudExadataInfrastructure'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'DeleteCloudExadataInfrastructure')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='DeleteCloudExadataInfrastructure')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.delete_cloud_exadata_infrastructure(
                cloud_exadata_infrastructure_id=request.pop(util.camelize('cloudExadataInfrastructureId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'DeleteCloudExadataInfrastructure',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_cloud_exadata_infrastructure',
            True,
            False
        )


# IssueRoutingInfo tag="ExaCS" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_delete_cloud_vm_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'DeleteCloudVmCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'DeleteCloudVmCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='DeleteCloudVmCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.delete_cloud_vm_cluster(
                cloud_vm_cluster_id=request.pop(util.camelize('cloudVmClusterId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'DeleteCloudVmCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_cloud_vm_cluster',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_delete_console_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'DeleteConsoleConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'DeleteConsoleConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='DeleteConsoleConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.delete_console_connection(
                db_node_id=request.pop(util.camelize('dbNodeId')),
                console_connection_id=request.pop(util.camelize('consoleConnectionId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'DeleteConsoleConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_console_connection',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_delete_database(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'DeleteDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'DeleteDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='DeleteDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.delete_database(
                database_id=request.pop(util.camelize('databaseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'DeleteDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_database',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_delete_database_software_image(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'DeleteDatabaseSoftwareImage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'DeleteDatabaseSoftwareImage')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='DeleteDatabaseSoftwareImage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.delete_database_software_image(
                database_software_image_id=request.pop(util.camelize('databaseSoftwareImageId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'DeleteDatabaseSoftwareImage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_database_software_image',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_delete_db_home(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'DeleteDbHome'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'DeleteDbHome')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='DeleteDbHome')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.delete_db_home(
                db_home_id=request.pop(util.camelize('dbHomeId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'DeleteDbHome',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_db_home',
            True,
            False
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_delete_exadata_infrastructure(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'DeleteExadataInfrastructure'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'DeleteExadataInfrastructure')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='DeleteExadataInfrastructure')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.delete_exadata_infrastructure(
                exadata_infrastructure_id=request.pop(util.camelize('exadataInfrastructureId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'DeleteExadataInfrastructure',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_exadata_infrastructure',
            True,
            False
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_delete_key_store(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'DeleteKeyStore'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'DeleteKeyStore')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='DeleteKeyStore')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.delete_key_store(
                key_store_id=request.pop(util.camelize('keyStoreId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'DeleteKeyStore',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_key_store',
            True,
            False
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_delete_vm_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'DeleteVmCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'DeleteVmCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='DeleteVmCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.delete_vm_cluster(
                vm_cluster_id=request.pop(util.camelize('vmClusterId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'DeleteVmCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_vm_cluster',
            True,
            False
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_delete_vm_cluster_network(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'DeleteVmClusterNetwork'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'DeleteVmClusterNetwork')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='DeleteVmClusterNetwork')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.delete_vm_cluster_network(
                exadata_infrastructure_id=request.pop(util.camelize('exadataInfrastructureId')),
                vm_cluster_network_id=request.pop(util.camelize('vmClusterNetworkId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'DeleteVmClusterNetwork',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_vm_cluster_network',
            True,
            False
        )


# IssueRoutingInfo tag="dbaas-adb" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_deregister_autonomous_database_data_safe(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'DeregisterAutonomousDatabaseDataSafe'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'DeregisterAutonomousDatabaseDataSafe')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='DeregisterAutonomousDatabaseDataSafe')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.deregister_autonomous_database_data_safe(
                autonomous_database_id=request.pop(util.camelize('autonomousDatabaseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'DeregisterAutonomousDatabaseDataSafe',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deregister_autonomous_database_data_safe',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-adb" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_disable_autonomous_database_operations_insights(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'DisableAutonomousDatabaseOperationsInsights'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'DisableAutonomousDatabaseOperationsInsights')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='DisableAutonomousDatabaseOperationsInsights')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.disable_autonomous_database_operations_insights(
                autonomous_database_id=request.pop(util.camelize('autonomousDatabaseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'DisableAutonomousDatabaseOperationsInsights',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'disable_autonomous_database_operations_insights',
            False,
            False
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_download_exadata_infrastructure_config_file(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'DownloadExadataInfrastructureConfigFile'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'DownloadExadataInfrastructureConfigFile')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='DownloadExadataInfrastructureConfigFile')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.download_exadata_infrastructure_config_file(
                exadata_infrastructure_id=request.pop(util.camelize('exadataInfrastructureId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'DownloadExadataInfrastructureConfigFile',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_download_vm_cluster_network_config_file(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'DownloadVmClusterNetworkConfigFile'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'DownloadVmClusterNetworkConfigFile')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='DownloadVmClusterNetworkConfigFile')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.download_vm_cluster_network_config_file(
                exadata_infrastructure_id=request.pop(util.camelize('exadataInfrastructureId')),
                vm_cluster_network_id=request.pop(util.camelize('vmClusterNetworkId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'DownloadVmClusterNetworkConfigFile',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-adb" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_enable_autonomous_database_operations_insights(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'EnableAutonomousDatabaseOperationsInsights'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'EnableAutonomousDatabaseOperationsInsights')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='EnableAutonomousDatabaseOperationsInsights')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.enable_autonomous_database_operations_insights(
                autonomous_database_id=request.pop(util.camelize('autonomousDatabaseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'EnableAutonomousDatabaseOperationsInsights',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'enable_autonomous_database_operations_insights',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-adb" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_fail_over_autonomous_database(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'FailOverAutonomousDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'FailOverAutonomousDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='FailOverAutonomousDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.fail_over_autonomous_database(
                autonomous_database_id=request.pop(util.camelize('autonomousDatabaseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'FailOverAutonomousDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousDatabase',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-atp-d" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_failover_autonomous_container_database_dataguard_association(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'FailoverAutonomousContainerDatabaseDataguardAssociation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'FailoverAutonomousContainerDatabaseDataguardAssociation')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='FailoverAutonomousContainerDatabaseDataguardAssociation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.failover_autonomous_container_database_dataguard_association(
                autonomous_container_database_id=request.pop(util.camelize('autonomousContainerDatabaseId')),
                autonomous_container_database_dataguard_association_id=request.pop(util.camelize('autonomousContainerDatabaseDataguardAssociationId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'FailoverAutonomousContainerDatabaseDataguardAssociation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousContainerDatabaseDataguardAssociation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_failover_data_guard_association(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'FailoverDataGuardAssociation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'FailoverDataGuardAssociation')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='FailoverDataGuardAssociation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.failover_data_guard_association(
                database_id=request.pop(util.camelize('databaseId')),
                data_guard_association_id=request.pop(util.camelize('dataGuardAssociationId')),
                failover_data_guard_association_details=request.pop(util.camelize('FailoverDataGuardAssociationDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'FailoverDataGuardAssociation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataGuardAssociation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_generate_autonomous_data_warehouse_wallet(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GenerateAutonomousDataWarehouseWallet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GenerateAutonomousDataWarehouseWallet')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GenerateAutonomousDataWarehouseWallet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.generate_autonomous_data_warehouse_wallet(
                autonomous_data_warehouse_id=request.pop(util.camelize('autonomousDataWarehouseId')),
                generate_autonomous_data_warehouse_wallet_details=request.pop(util.camelize('GenerateAutonomousDataWarehouseWalletDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GenerateAutonomousDataWarehouseWallet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-adb" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_generate_autonomous_database_wallet(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GenerateAutonomousDatabaseWallet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GenerateAutonomousDatabaseWallet')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GenerateAutonomousDatabaseWallet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.generate_autonomous_database_wallet(
                autonomous_database_id=request.pop(util.camelize('autonomousDatabaseId')),
                generate_autonomous_database_wallet_details=request.pop(util.camelize('GenerateAutonomousDatabaseWalletDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GenerateAutonomousDatabaseWallet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_generate_recommended_vm_cluster_network(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GenerateRecommendedVmClusterNetwork'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GenerateRecommendedVmClusterNetwork')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GenerateRecommendedVmClusterNetwork')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.generate_recommended_vm_cluster_network(
                exadata_infrastructure_id=request.pop(util.camelize('exadataInfrastructureId')),
                generate_recommended_network_details=request.pop(util.camelize('GenerateRecommendedNetworkDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GenerateRecommendedVmClusterNetwork',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'vmClusterNetworkDetails',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-atp-d" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_autonomous_container_database(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetAutonomousContainerDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetAutonomousContainerDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetAutonomousContainerDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_autonomous_container_database(
                autonomous_container_database_id=request.pop(util.camelize('autonomousContainerDatabaseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetAutonomousContainerDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousContainerDatabase',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-atp-d" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_autonomous_container_database_dataguard_association(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetAutonomousContainerDatabaseDataguardAssociation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetAutonomousContainerDatabaseDataguardAssociation')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetAutonomousContainerDatabaseDataguardAssociation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_autonomous_container_database_dataguard_association(
                autonomous_container_database_id=request.pop(util.camelize('autonomousContainerDatabaseId')),
                autonomous_container_database_dataguard_association_id=request.pop(util.camelize('autonomousContainerDatabaseDataguardAssociationId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetAutonomousContainerDatabaseDataguardAssociation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousContainerDatabaseDataguardAssociation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_autonomous_data_warehouse(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetAutonomousDataWarehouse'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetAutonomousDataWarehouse')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetAutonomousDataWarehouse')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_autonomous_data_warehouse(
                autonomous_data_warehouse_id=request.pop(util.camelize('autonomousDataWarehouseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetAutonomousDataWarehouse',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousDataWarehouse',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_autonomous_data_warehouse_backup(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetAutonomousDataWarehouseBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetAutonomousDataWarehouseBackup')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetAutonomousDataWarehouseBackup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_autonomous_data_warehouse_backup(
                autonomous_data_warehouse_backup_id=request.pop(util.camelize('autonomousDataWarehouseBackupId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetAutonomousDataWarehouseBackup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousDataWarehouseBackup',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-adb" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_autonomous_database(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetAutonomousDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetAutonomousDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetAutonomousDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_autonomous_database(
                autonomous_database_id=request.pop(util.camelize('autonomousDatabaseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetAutonomousDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousDatabase',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-adb" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_autonomous_database_backup(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetAutonomousDatabaseBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetAutonomousDatabaseBackup')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetAutonomousDatabaseBackup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_autonomous_database_backup(
                autonomous_database_backup_id=request.pop(util.camelize('autonomousDatabaseBackupId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetAutonomousDatabaseBackup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousDatabaseBackup',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-atp-d" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_autonomous_database_dataguard_association(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetAutonomousDatabaseDataguardAssociation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetAutonomousDatabaseDataguardAssociation')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetAutonomousDatabaseDataguardAssociation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_autonomous_database_dataguard_association(
                autonomous_database_id=request.pop(util.camelize('autonomousDatabaseId')),
                autonomous_database_dataguard_association_id=request.pop(util.camelize('autonomousDatabaseDataguardAssociationId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetAutonomousDatabaseDataguardAssociation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousDatabaseDataguardAssociation',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-adb" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_autonomous_database_regional_wallet(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetAutonomousDatabaseRegionalWallet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetAutonomousDatabaseRegionalWallet')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetAutonomousDatabaseRegionalWallet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_autonomous_database_regional_wallet(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetAutonomousDatabaseRegionalWallet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousDatabaseWallet',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-adb" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_autonomous_database_wallet(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetAutonomousDatabaseWallet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetAutonomousDatabaseWallet')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetAutonomousDatabaseWallet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_autonomous_database_wallet(
                autonomous_database_id=request.pop(util.camelize('autonomousDatabaseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetAutonomousDatabaseWallet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousDatabaseWallet',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-atp-d" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_autonomous_exadata_infrastructure(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetAutonomousExadataInfrastructure'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetAutonomousExadataInfrastructure')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetAutonomousExadataInfrastructure')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_autonomous_exadata_infrastructure(
                autonomous_exadata_infrastructure_id=request.pop(util.camelize('autonomousExadataInfrastructureId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetAutonomousExadataInfrastructure',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousExadataInfrastructure',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-atp-d" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_autonomous_patch(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetAutonomousPatch'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetAutonomousPatch')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetAutonomousPatch')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_autonomous_patch(
                autonomous_patch_id=request.pop(util.camelize('autonomousPatchId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetAutonomousPatch',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousPatch',
            False,
            False
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_autonomous_vm_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetAutonomousVmCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetAutonomousVmCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetAutonomousVmCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_autonomous_vm_cluster(
                autonomous_vm_cluster_id=request.pop(util.camelize('autonomousVmClusterId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetAutonomousVmCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousVmCluster',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_backup(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetBackup')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetBackup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_backup(
                backup_id=request.pop(util.camelize('backupId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetBackup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'backup',
            False,
            False
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_backup_destination(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetBackupDestination'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetBackupDestination')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetBackupDestination')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_backup_destination(
                backup_destination_id=request.pop(util.camelize('backupDestinationId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetBackupDestination',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'backupDestination',
            False,
            False
        )


# IssueRoutingInfo tag="ExaCS" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_cloud_exadata_infrastructure(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetCloudExadataInfrastructure'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetCloudExadataInfrastructure')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetCloudExadataInfrastructure')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_cloud_exadata_infrastructure(
                cloud_exadata_infrastructure_id=request.pop(util.camelize('cloudExadataInfrastructureId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetCloudExadataInfrastructure',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cloudExadataInfrastructure',
            False,
            False
        )


# IssueRoutingInfo tag="ExaCS" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_cloud_vm_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetCloudVmCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetCloudVmCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetCloudVmCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_cloud_vm_cluster(
                cloud_vm_cluster_id=request.pop(util.camelize('cloudVmClusterId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetCloudVmCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cloudVmCluster',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_cloud_vm_cluster_iorm_config(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetCloudVmClusterIormConfig'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetCloudVmClusterIormConfig')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetCloudVmClusterIormConfig')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_cloud_vm_cluster_iorm_config(
                cloud_vm_cluster_id=request.pop(util.camelize('cloudVmClusterId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetCloudVmClusterIormConfig',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'exadataIormConfig',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_cloud_vm_cluster_update(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetCloudVmClusterUpdate'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetCloudVmClusterUpdate')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetCloudVmClusterUpdate')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_cloud_vm_cluster_update(
                cloud_vm_cluster_id=request.pop(util.camelize('cloudVmClusterId')),
                update_id=request.pop(util.camelize('updateId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetCloudVmClusterUpdate',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_cloud_vm_cluster_update_history_entry(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetCloudVmClusterUpdateHistoryEntry'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetCloudVmClusterUpdateHistoryEntry')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetCloudVmClusterUpdateHistoryEntry')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_cloud_vm_cluster_update_history_entry(
                cloud_vm_cluster_id=request.pop(util.camelize('cloudVmClusterId')),
                update_history_entry_id=request.pop(util.camelize('updateHistoryEntryId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetCloudVmClusterUpdateHistoryEntry',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'updateHistoryEntry',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_console_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetConsoleConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetConsoleConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetConsoleConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_console_connection(
                db_node_id=request.pop(util.camelize('dbNodeId')),
                console_connection_id=request.pop(util.camelize('consoleConnectionId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetConsoleConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'consoleConnection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_data_guard_association(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetDataGuardAssociation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetDataGuardAssociation')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetDataGuardAssociation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_data_guard_association(
                database_id=request.pop(util.camelize('databaseId')),
                data_guard_association_id=request.pop(util.camelize('dataGuardAssociationId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetDataGuardAssociation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataGuardAssociation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_database(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_database(
                database_id=request.pop(util.camelize('databaseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'database',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_database_software_image(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetDatabaseSoftwareImage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetDatabaseSoftwareImage')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetDatabaseSoftwareImage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_database_software_image(
                database_software_image_id=request.pop(util.camelize('databaseSoftwareImageId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetDatabaseSoftwareImage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'databaseSoftwareImage',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_db_home(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetDbHome'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetDbHome')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetDbHome')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_db_home(
                db_home_id=request.pop(util.camelize('dbHomeId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetDbHome',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dbHome',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_db_home_patch(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetDbHomePatch'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetDbHomePatch')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetDbHomePatch')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_db_home_patch(
                db_home_id=request.pop(util.camelize('dbHomeId')),
                patch_id=request.pop(util.camelize('patchId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetDbHomePatch',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'patch',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_db_home_patch_history_entry(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetDbHomePatchHistoryEntry'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetDbHomePatchHistoryEntry')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetDbHomePatchHistoryEntry')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_db_home_patch_history_entry(
                db_home_id=request.pop(util.camelize('dbHomeId')),
                patch_history_entry_id=request.pop(util.camelize('patchHistoryEntryId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetDbHomePatchHistoryEntry',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'patchHistoryEntry',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_db_node(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetDbNode'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetDbNode')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetDbNode')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_db_node(
                db_node_id=request.pop(util.camelize('dbNodeId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetDbNode',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dbNode',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_db_system(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetDbSystem'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetDbSystem')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetDbSystem')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_db_system(
                db_system_id=request.pop(util.camelize('dbSystemId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetDbSystem',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dbSystem',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_db_system_patch(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetDbSystemPatch'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetDbSystemPatch')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetDbSystemPatch')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_db_system_patch(
                db_system_id=request.pop(util.camelize('dbSystemId')),
                patch_id=request.pop(util.camelize('patchId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetDbSystemPatch',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'patch',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_db_system_patch_history_entry(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetDbSystemPatchHistoryEntry'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetDbSystemPatchHistoryEntry')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetDbSystemPatchHistoryEntry')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_db_system_patch_history_entry(
                db_system_id=request.pop(util.camelize('dbSystemId')),
                patch_history_entry_id=request.pop(util.camelize('patchHistoryEntryId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetDbSystemPatchHistoryEntry',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'patchHistoryEntry',
            False,
            False
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_exadata_infrastructure(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetExadataInfrastructure'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetExadataInfrastructure')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetExadataInfrastructure')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_exadata_infrastructure(
                exadata_infrastructure_id=request.pop(util.camelize('exadataInfrastructureId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetExadataInfrastructure',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'exadataInfrastructure',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_exadata_infrastructure_ocpus(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetExadataInfrastructureOcpus'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetExadataInfrastructureOcpus')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetExadataInfrastructureOcpus')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_exadata_infrastructure_ocpus(
                autonomous_exadata_infrastructure_id=request.pop(util.camelize('autonomousExadataInfrastructureId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetExadataInfrastructureOcpus',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'oCPUs',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_exadata_iorm_config(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetExadataIormConfig'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetExadataIormConfig')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetExadataIormConfig')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_exadata_iorm_config(
                db_system_id=request.pop(util.camelize('dbSystemId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetExadataIormConfig',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'exadataIormConfig',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_external_backup_job(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetExternalBackupJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetExternalBackupJob')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetExternalBackupJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_external_backup_job(
                backup_id=request.pop(util.camelize('backupId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetExternalBackupJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalBackupJob',
            False,
            False
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_key_store(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetKeyStore'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetKeyStore')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetKeyStore')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_key_store(
                key_store_id=request.pop(util.camelize('keyStoreId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetKeyStore',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'keyStore',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-atp-d" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_maintenance_run(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetMaintenanceRun'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetMaintenanceRun')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetMaintenanceRun')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_maintenance_run(
                maintenance_run_id=request.pop(util.camelize('maintenanceRunId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetMaintenanceRun',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'maintenanceRun',
            False,
            False
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_vm_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetVmCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetVmCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetVmCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_vm_cluster(
                vm_cluster_id=request.pop(util.camelize('vmClusterId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetVmCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'vmCluster',
            False,
            False
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_vm_cluster_network(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetVmClusterNetwork'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetVmClusterNetwork')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetVmClusterNetwork')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_vm_cluster_network(
                exadata_infrastructure_id=request.pop(util.camelize('exadataInfrastructureId')),
                vm_cluster_network_id=request.pop(util.camelize('vmClusterNetworkId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetVmClusterNetwork',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'vmClusterNetwork',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_vm_cluster_patch(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetVmClusterPatch'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetVmClusterPatch')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetVmClusterPatch')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_vm_cluster_patch(
                vm_cluster_id=request.pop(util.camelize('vmClusterId')),
                patch_id=request.pop(util.camelize('patchId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetVmClusterPatch',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'patch',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_get_vm_cluster_patch_history_entry(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'GetVmClusterPatchHistoryEntry'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'GetVmClusterPatchHistoryEntry')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetVmClusterPatchHistoryEntry')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.get_vm_cluster_patch_history_entry(
                vm_cluster_id=request.pop(util.camelize('vmClusterId')),
                patch_history_entry_id=request.pop(util.camelize('patchHistoryEntryId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'GetVmClusterPatchHistoryEntry',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'patchHistoryEntry',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-atp-d" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_launch_autonomous_exadata_infrastructure(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'LaunchAutonomousExadataInfrastructure'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'LaunchAutonomousExadataInfrastructure')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='LaunchAutonomousExadataInfrastructure')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.launch_autonomous_exadata_infrastructure(
                launch_autonomous_exadata_infrastructure_details=request.pop(util.camelize('LaunchAutonomousExadataInfrastructureDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'LaunchAutonomousExadataInfrastructure',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousExadataInfrastructure',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_launch_db_system(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'LaunchDbSystem'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'LaunchDbSystem')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='LaunchDbSystem')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.launch_db_system(
                launch_db_system_details=request.pop(util.camelize('LaunchDbSystemDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'LaunchDbSystem',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dbSystem',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-atp-d" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_autonomous_container_database_dataguard_associations(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListAutonomousContainerDatabaseDataguardAssociations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListAutonomousContainerDatabaseDataguardAssociations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListAutonomousContainerDatabaseDataguardAssociations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_autonomous_container_database_dataguard_associations(
                autonomous_container_database_id=request.pop(util.camelize('autonomousContainerDatabaseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_autonomous_container_database_dataguard_associations(
                    autonomous_container_database_id=request.pop(util.camelize('autonomousContainerDatabaseId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_autonomous_container_database_dataguard_associations(
                        autonomous_container_database_id=request.pop(util.camelize('autonomousContainerDatabaseId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListAutonomousContainerDatabaseDataguardAssociations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousContainerDatabaseDataguardAssociation',
            False,
            True
        )


# IssueRoutingInfo tag="dbaas-atp-d" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_autonomous_container_databases(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListAutonomousContainerDatabases'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListAutonomousContainerDatabases')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListAutonomousContainerDatabases')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_autonomous_container_databases(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_autonomous_container_databases(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_autonomous_container_databases(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListAutonomousContainerDatabases',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousContainerDatabaseSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_autonomous_data_warehouse_backups(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListAutonomousDataWarehouseBackups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListAutonomousDataWarehouseBackups')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListAutonomousDataWarehouseBackups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_autonomous_data_warehouse_backups(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_autonomous_data_warehouse_backups(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_autonomous_data_warehouse_backups(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListAutonomousDataWarehouseBackups',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousDataWarehouseBackupSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_autonomous_data_warehouses(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListAutonomousDataWarehouses'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListAutonomousDataWarehouses')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListAutonomousDataWarehouses')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_autonomous_data_warehouses(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_autonomous_data_warehouses(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_autonomous_data_warehouses(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListAutonomousDataWarehouses',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousDataWarehouseSummary',
            False,
            True
        )


# IssueRoutingInfo tag="dbaas-adb" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_autonomous_database_backups(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListAutonomousDatabaseBackups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListAutonomousDatabaseBackups')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListAutonomousDatabaseBackups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_autonomous_database_backups(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_autonomous_database_backups(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_autonomous_database_backups(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListAutonomousDatabaseBackups',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousDatabaseBackupSummary',
            False,
            True
        )


# IssueRoutingInfo tag="dbaas-adb" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_autonomous_database_clones(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListAutonomousDatabaseClones'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListAutonomousDatabaseClones')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListAutonomousDatabaseClones')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_autonomous_database_clones(
                compartment_id=request.pop(util.camelize('compartmentId')),
                autonomous_database_id=request.pop(util.camelize('autonomousDatabaseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_autonomous_database_clones(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    autonomous_database_id=request.pop(util.camelize('autonomousDatabaseId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_autonomous_database_clones(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        autonomous_database_id=request.pop(util.camelize('autonomousDatabaseId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListAutonomousDatabaseClones',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousDatabaseSummary',
            False,
            True
        )


# IssueRoutingInfo tag="dbaas-atp-d" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_autonomous_database_dataguard_associations(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListAutonomousDatabaseDataguardAssociations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListAutonomousDatabaseDataguardAssociations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListAutonomousDatabaseDataguardAssociations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_autonomous_database_dataguard_associations(
                autonomous_database_id=request.pop(util.camelize('autonomousDatabaseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_autonomous_database_dataguard_associations(
                    autonomous_database_id=request.pop(util.camelize('autonomousDatabaseId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_autonomous_database_dataguard_associations(
                        autonomous_database_id=request.pop(util.camelize('autonomousDatabaseId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListAutonomousDatabaseDataguardAssociations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousDatabaseDataguardAssociation',
            False,
            True
        )


# IssueRoutingInfo tag="dbaas-adb" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_autonomous_databases(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListAutonomousDatabases'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListAutonomousDatabases')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListAutonomousDatabases')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_autonomous_databases(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_autonomous_databases(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_autonomous_databases(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListAutonomousDatabases',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousDatabaseSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_autonomous_db_preview_versions(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListAutonomousDbPreviewVersions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListAutonomousDbPreviewVersions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListAutonomousDbPreviewVersions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_autonomous_db_preview_versions(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_autonomous_db_preview_versions(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_autonomous_db_preview_versions(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListAutonomousDbPreviewVersions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousDbPreviewVersionSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_autonomous_db_versions(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListAutonomousDbVersions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListAutonomousDbVersions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListAutonomousDbVersions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_autonomous_db_versions(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_autonomous_db_versions(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_autonomous_db_versions(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListAutonomousDbVersions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousDbVersionSummary',
            False,
            True
        )


# IssueRoutingInfo tag="dbaas-atp-d" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_autonomous_exadata_infrastructure_shapes(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListAutonomousExadataInfrastructureShapes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListAutonomousExadataInfrastructureShapes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListAutonomousExadataInfrastructureShapes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_autonomous_exadata_infrastructure_shapes(
                availability_domain=request.pop(util.camelize('availabilityDomain')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_autonomous_exadata_infrastructure_shapes(
                    availability_domain=request.pop(util.camelize('availabilityDomain')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_autonomous_exadata_infrastructure_shapes(
                        availability_domain=request.pop(util.camelize('availabilityDomain')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListAutonomousExadataInfrastructureShapes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousExadataInfrastructureShapeSummary',
            False,
            True
        )


# IssueRoutingInfo tag="dbaas-atp-d" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_autonomous_exadata_infrastructures(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListAutonomousExadataInfrastructures'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListAutonomousExadataInfrastructures')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListAutonomousExadataInfrastructures')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_autonomous_exadata_infrastructures(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_autonomous_exadata_infrastructures(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_autonomous_exadata_infrastructures(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListAutonomousExadataInfrastructures',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousExadataInfrastructureSummary',
            False,
            True
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_autonomous_vm_clusters(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListAutonomousVmClusters'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListAutonomousVmClusters')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListAutonomousVmClusters')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_autonomous_vm_clusters(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_autonomous_vm_clusters(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_autonomous_vm_clusters(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListAutonomousVmClusters',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousVmClusterSummary',
            False,
            True
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_backup_destination(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListBackupDestination'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListBackupDestination')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListBackupDestination')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_backup_destination(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_backup_destination(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_backup_destination(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListBackupDestination',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'backupDestinationSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_backups(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListBackups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListBackups')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListBackups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_backups(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_backups(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_backups(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListBackups',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'backupSummary',
            False,
            True
        )


# IssueRoutingInfo tag="ExaCS" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_cloud_exadata_infrastructures(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListCloudExadataInfrastructures'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListCloudExadataInfrastructures')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListCloudExadataInfrastructures')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_cloud_exadata_infrastructures(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_cloud_exadata_infrastructures(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_cloud_exadata_infrastructures(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListCloudExadataInfrastructures',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cloudExadataInfrastructureSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_cloud_vm_cluster_update_history_entries(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListCloudVmClusterUpdateHistoryEntries'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListCloudVmClusterUpdateHistoryEntries')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListCloudVmClusterUpdateHistoryEntries')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_cloud_vm_cluster_update_history_entries(
                cloud_vm_cluster_id=request.pop(util.camelize('cloudVmClusterId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_cloud_vm_cluster_update_history_entries(
                    cloud_vm_cluster_id=request.pop(util.camelize('cloudVmClusterId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_cloud_vm_cluster_update_history_entries(
                        cloud_vm_cluster_id=request.pop(util.camelize('cloudVmClusterId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListCloudVmClusterUpdateHistoryEntries',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'updateHistoryEntrySummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_cloud_vm_cluster_updates(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListCloudVmClusterUpdates'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListCloudVmClusterUpdates')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListCloudVmClusterUpdates')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_cloud_vm_cluster_updates(
                cloud_vm_cluster_id=request.pop(util.camelize('cloudVmClusterId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_cloud_vm_cluster_updates(
                    cloud_vm_cluster_id=request.pop(util.camelize('cloudVmClusterId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_cloud_vm_cluster_updates(
                        cloud_vm_cluster_id=request.pop(util.camelize('cloudVmClusterId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListCloudVmClusterUpdates',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'updateSummary',
            False,
            True
        )


# IssueRoutingInfo tag="ExaCS" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_cloud_vm_clusters(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListCloudVmClusters'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListCloudVmClusters')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListCloudVmClusters')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_cloud_vm_clusters(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_cloud_vm_clusters(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_cloud_vm_clusters(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListCloudVmClusters',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cloudVmClusterSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_console_connections(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListConsoleConnections'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListConsoleConnections')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListConsoleConnections')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_console_connections(
                db_node_id=request.pop(util.camelize('dbNodeId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListConsoleConnections',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'consoleConnectionSummary',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_container_database_patches(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListContainerDatabasePatches'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListContainerDatabasePatches')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListContainerDatabasePatches')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_container_database_patches(
                autonomous_container_database_id=request.pop(util.camelize('autonomousContainerDatabaseId')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_container_database_patches(
                    autonomous_container_database_id=request.pop(util.camelize('autonomousContainerDatabaseId')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_container_database_patches(
                        autonomous_container_database_id=request.pop(util.camelize('autonomousContainerDatabaseId')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListContainerDatabasePatches',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousPatchSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_data_guard_associations(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListDataGuardAssociations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListDataGuardAssociations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListDataGuardAssociations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_data_guard_associations(
                database_id=request.pop(util.camelize('databaseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_data_guard_associations(
                    database_id=request.pop(util.camelize('databaseId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_data_guard_associations(
                        database_id=request.pop(util.camelize('databaseId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListDataGuardAssociations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataGuardAssociationSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_database_software_images(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListDatabaseSoftwareImages'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListDatabaseSoftwareImages')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListDatabaseSoftwareImages')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_database_software_images(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_database_software_images(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_database_software_images(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListDatabaseSoftwareImages',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'databaseSoftwareImageSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_databases(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListDatabases'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListDatabases')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListDatabases')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_databases(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_databases(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_databases(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListDatabases',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'databaseSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_db_home_patch_history_entries(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListDbHomePatchHistoryEntries'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListDbHomePatchHistoryEntries')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListDbHomePatchHistoryEntries')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_db_home_patch_history_entries(
                db_home_id=request.pop(util.camelize('dbHomeId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_db_home_patch_history_entries(
                    db_home_id=request.pop(util.camelize('dbHomeId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_db_home_patch_history_entries(
                        db_home_id=request.pop(util.camelize('dbHomeId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListDbHomePatchHistoryEntries',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'patchHistoryEntrySummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_db_home_patches(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListDbHomePatches'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListDbHomePatches')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListDbHomePatches')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_db_home_patches(
                db_home_id=request.pop(util.camelize('dbHomeId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_db_home_patches(
                    db_home_id=request.pop(util.camelize('dbHomeId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_db_home_patches(
                        db_home_id=request.pop(util.camelize('dbHomeId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListDbHomePatches',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'patchSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_db_homes(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListDbHomes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListDbHomes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListDbHomes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_db_homes(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_db_homes(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_db_homes(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListDbHomes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dbHomeSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_db_nodes(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListDbNodes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListDbNodes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListDbNodes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_db_nodes(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_db_nodes(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_db_nodes(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListDbNodes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dbNodeSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_db_system_patch_history_entries(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListDbSystemPatchHistoryEntries'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListDbSystemPatchHistoryEntries')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListDbSystemPatchHistoryEntries')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_db_system_patch_history_entries(
                db_system_id=request.pop(util.camelize('dbSystemId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_db_system_patch_history_entries(
                    db_system_id=request.pop(util.camelize('dbSystemId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_db_system_patch_history_entries(
                        db_system_id=request.pop(util.camelize('dbSystemId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListDbSystemPatchHistoryEntries',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'patchHistoryEntrySummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_db_system_patches(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListDbSystemPatches'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListDbSystemPatches')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListDbSystemPatches')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_db_system_patches(
                db_system_id=request.pop(util.camelize('dbSystemId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_db_system_patches(
                    db_system_id=request.pop(util.camelize('dbSystemId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_db_system_patches(
                        db_system_id=request.pop(util.camelize('dbSystemId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListDbSystemPatches',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'patchSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_db_system_shapes(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListDbSystemShapes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListDbSystemShapes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListDbSystemShapes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_db_system_shapes(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_db_system_shapes(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_db_system_shapes(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListDbSystemShapes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dbSystemShapeSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_db_systems(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListDbSystems'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListDbSystems')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListDbSystems')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_db_systems(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_db_systems(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_db_systems(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListDbSystems',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dbSystemSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_db_versions(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListDbVersions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListDbVersions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListDbVersions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_db_versions(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_db_versions(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_db_versions(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListDbVersions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dbVersionSummary',
            False,
            True
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_exadata_infrastructures(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListExadataInfrastructures'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListExadataInfrastructures')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListExadataInfrastructures')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_exadata_infrastructures(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_exadata_infrastructures(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_exadata_infrastructures(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListExadataInfrastructures',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'exadataInfrastructureSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_gi_versions(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListGiVersions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListGiVersions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListGiVersions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_gi_versions(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_gi_versions(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_gi_versions(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListGiVersions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'giVersionSummary',
            False,
            True
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_key_stores(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListKeyStores'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListKeyStores')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListKeyStores')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_key_stores(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_key_stores(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_key_stores(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListKeyStores',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'keyStoreSummary',
            False,
            True
        )


# IssueRoutingInfo tag="dbaas-atp-d" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_maintenance_runs(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListMaintenanceRuns'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListMaintenanceRuns')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListMaintenanceRuns')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_maintenance_runs(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_maintenance_runs(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_maintenance_runs(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListMaintenanceRuns',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'maintenanceRunSummary',
            False,
            True
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_vm_cluster_networks(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListVmClusterNetworks'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListVmClusterNetworks')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListVmClusterNetworks')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_vm_cluster_networks(
                exadata_infrastructure_id=request.pop(util.camelize('exadataInfrastructureId')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_vm_cluster_networks(
                    exadata_infrastructure_id=request.pop(util.camelize('exadataInfrastructureId')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_vm_cluster_networks(
                        exadata_infrastructure_id=request.pop(util.camelize('exadataInfrastructureId')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListVmClusterNetworks',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'vmClusterNetworkSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_vm_cluster_patch_history_entries(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListVmClusterPatchHistoryEntries'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListVmClusterPatchHistoryEntries')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListVmClusterPatchHistoryEntries')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_vm_cluster_patch_history_entries(
                vm_cluster_id=request.pop(util.camelize('vmClusterId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_vm_cluster_patch_history_entries(
                    vm_cluster_id=request.pop(util.camelize('vmClusterId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_vm_cluster_patch_history_entries(
                        vm_cluster_id=request.pop(util.camelize('vmClusterId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListVmClusterPatchHistoryEntries',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'patchHistoryEntrySummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_vm_cluster_patches(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListVmClusterPatches'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListVmClusterPatches')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListVmClusterPatches')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_vm_cluster_patches(
                vm_cluster_id=request.pop(util.camelize('vmClusterId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_vm_cluster_patches(
                    vm_cluster_id=request.pop(util.camelize('vmClusterId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_vm_cluster_patches(
                        vm_cluster_id=request.pop(util.camelize('vmClusterId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListVmClusterPatches',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'patchSummary',
            False,
            True
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_list_vm_clusters(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ListVmClusters'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ListVmClusters')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListVmClusters')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.list_vm_clusters(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_vm_clusters(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_vm_clusters(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ListVmClusters',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'vmClusterSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_migrate_exadata_db_system_resource_model(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'MigrateExadataDbSystemResourceModel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'MigrateExadataDbSystemResourceModel')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='MigrateExadataDbSystemResourceModel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.migrate_exadata_db_system_resource_model(
                db_system_id=request.pop(util.camelize('dbSystemId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'MigrateExadataDbSystemResourceModel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'exadataDbSystemMigration',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-adb" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_register_autonomous_database_data_safe(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'RegisterAutonomousDatabaseDataSafe'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'RegisterAutonomousDatabaseDataSafe')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='RegisterAutonomousDatabaseDataSafe')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.register_autonomous_database_data_safe(
                autonomous_database_id=request.pop(util.camelize('autonomousDatabaseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'RegisterAutonomousDatabaseDataSafe',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'register_autonomous_database_data_safe',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-atp-d" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_reinstate_autonomous_container_database_dataguard_association(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ReinstateAutonomousContainerDatabaseDataguardAssociation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ReinstateAutonomousContainerDatabaseDataguardAssociation')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ReinstateAutonomousContainerDatabaseDataguardAssociation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.reinstate_autonomous_container_database_dataguard_association(
                autonomous_container_database_id=request.pop(util.camelize('autonomousContainerDatabaseId')),
                autonomous_container_database_dataguard_association_id=request.pop(util.camelize('autonomousContainerDatabaseDataguardAssociationId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ReinstateAutonomousContainerDatabaseDataguardAssociation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousContainerDatabaseDataguardAssociation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_reinstate_data_guard_association(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ReinstateDataGuardAssociation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ReinstateDataGuardAssociation')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ReinstateDataGuardAssociation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.reinstate_data_guard_association(
                database_id=request.pop(util.camelize('databaseId')),
                data_guard_association_id=request.pop(util.camelize('dataGuardAssociationId')),
                reinstate_data_guard_association_details=request.pop(util.camelize('ReinstateDataGuardAssociationDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ReinstateDataGuardAssociation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataGuardAssociation',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-atp-d" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_restart_autonomous_container_database(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'RestartAutonomousContainerDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'RestartAutonomousContainerDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='RestartAutonomousContainerDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.restart_autonomous_container_database(
                autonomous_container_database_id=request.pop(util.camelize('autonomousContainerDatabaseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'RestartAutonomousContainerDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousContainerDatabase',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-adb" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_restart_autonomous_database(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'RestartAutonomousDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'RestartAutonomousDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='RestartAutonomousDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.restart_autonomous_database(
                autonomous_database_id=request.pop(util.camelize('autonomousDatabaseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'RestartAutonomousDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousDatabase',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_restore_autonomous_data_warehouse(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'RestoreAutonomousDataWarehouse'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'RestoreAutonomousDataWarehouse')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='RestoreAutonomousDataWarehouse')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.restore_autonomous_data_warehouse(
                autonomous_data_warehouse_id=request.pop(util.camelize('autonomousDataWarehouseId')),
                restore_autonomous_data_warehouse_details=request.pop(util.camelize('RestoreAutonomousDataWarehouseDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'RestoreAutonomousDataWarehouse',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousDataWarehouse',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-adb" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_restore_autonomous_database(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'RestoreAutonomousDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'RestoreAutonomousDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='RestoreAutonomousDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.restore_autonomous_database(
                autonomous_database_id=request.pop(util.camelize('autonomousDatabaseId')),
                restore_autonomous_database_details=request.pop(util.camelize('RestoreAutonomousDatabaseDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'RestoreAutonomousDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousDatabase',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_restore_database(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'RestoreDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'RestoreDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='RestoreDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.restore_database(
                database_id=request.pop(util.camelize('databaseId')),
                restore_database_details=request.pop(util.camelize('RestoreDatabaseDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'RestoreDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'database',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-atp-d" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_rotate_autonomous_container_database_encryption_key(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'RotateAutonomousContainerDatabaseEncryptionKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'RotateAutonomousContainerDatabaseEncryptionKey')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='RotateAutonomousContainerDatabaseEncryptionKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.rotate_autonomous_container_database_encryption_key(
                autonomous_container_database_id=request.pop(util.camelize('autonomousContainerDatabaseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'RotateAutonomousContainerDatabaseEncryptionKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousContainerDatabase',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-adb" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_rotate_autonomous_database_encryption_key(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'RotateAutonomousDatabaseEncryptionKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'RotateAutonomousDatabaseEncryptionKey')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='RotateAutonomousDatabaseEncryptionKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.rotate_autonomous_database_encryption_key(
                autonomous_database_id=request.pop(util.camelize('autonomousDatabaseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'RotateAutonomousDatabaseEncryptionKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousDatabase',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_start_autonomous_data_warehouse(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'StartAutonomousDataWarehouse'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'StartAutonomousDataWarehouse')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='StartAutonomousDataWarehouse')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.start_autonomous_data_warehouse(
                autonomous_data_warehouse_id=request.pop(util.camelize('autonomousDataWarehouseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'StartAutonomousDataWarehouse',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousDataWarehouse',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-adb" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_start_autonomous_database(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'StartAutonomousDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'StartAutonomousDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='StartAutonomousDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.start_autonomous_database(
                autonomous_database_id=request.pop(util.camelize('autonomousDatabaseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'StartAutonomousDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousDatabase',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_stop_autonomous_data_warehouse(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'StopAutonomousDataWarehouse'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'StopAutonomousDataWarehouse')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='StopAutonomousDataWarehouse')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.stop_autonomous_data_warehouse(
                autonomous_data_warehouse_id=request.pop(util.camelize('autonomousDataWarehouseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'StopAutonomousDataWarehouse',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousDataWarehouse',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-adb" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_stop_autonomous_database(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'StopAutonomousDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'StopAutonomousDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='StopAutonomousDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.stop_autonomous_database(
                autonomous_database_id=request.pop(util.camelize('autonomousDatabaseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'StopAutonomousDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousDatabase',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-atp-d" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_switchover_autonomous_container_database_dataguard_association(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'SwitchoverAutonomousContainerDatabaseDataguardAssociation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'SwitchoverAutonomousContainerDatabaseDataguardAssociation')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='SwitchoverAutonomousContainerDatabaseDataguardAssociation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.switchover_autonomous_container_database_dataguard_association(
                autonomous_container_database_id=request.pop(util.camelize('autonomousContainerDatabaseId')),
                autonomous_container_database_dataguard_association_id=request.pop(util.camelize('autonomousContainerDatabaseDataguardAssociationId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'SwitchoverAutonomousContainerDatabaseDataguardAssociation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousContainerDatabaseDataguardAssociation',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-adb" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_switchover_autonomous_database(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'SwitchoverAutonomousDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'SwitchoverAutonomousDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='SwitchoverAutonomousDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.switchover_autonomous_database(
                autonomous_database_id=request.pop(util.camelize('autonomousDatabaseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'SwitchoverAutonomousDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousDatabase',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_switchover_data_guard_association(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'SwitchoverDataGuardAssociation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'SwitchoverDataGuardAssociation')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='SwitchoverDataGuardAssociation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.switchover_data_guard_association(
                database_id=request.pop(util.camelize('databaseId')),
                data_guard_association_id=request.pop(util.camelize('dataGuardAssociationId')),
                switchover_data_guard_association_details=request.pop(util.camelize('SwitchoverDataGuardAssociationDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'SwitchoverDataGuardAssociation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataGuardAssociation',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-atp-d" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_terminate_autonomous_container_database(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'TerminateAutonomousContainerDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'TerminateAutonomousContainerDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='TerminateAutonomousContainerDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.terminate_autonomous_container_database(
                autonomous_container_database_id=request.pop(util.camelize('autonomousContainerDatabaseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'TerminateAutonomousContainerDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'terminate_autonomous_container_database',
            True,
            False
        )


# IssueRoutingInfo tag="dbaas-atp-d" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_terminate_autonomous_exadata_infrastructure(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'TerminateAutonomousExadataInfrastructure'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'TerminateAutonomousExadataInfrastructure')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='TerminateAutonomousExadataInfrastructure')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.terminate_autonomous_exadata_infrastructure(
                autonomous_exadata_infrastructure_id=request.pop(util.camelize('autonomousExadataInfrastructureId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'TerminateAutonomousExadataInfrastructure',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'terminate_autonomous_exadata_infrastructure',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_terminate_db_system(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'TerminateDbSystem'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'TerminateDbSystem')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='TerminateDbSystem')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.terminate_db_system(
                db_system_id=request.pop(util.camelize('dbSystemId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'TerminateDbSystem',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'terminate_db_system',
            True,
            False
        )


# IssueRoutingInfo tag="dbaas-atp-d" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_update_autonomous_container_database(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'UpdateAutonomousContainerDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'UpdateAutonomousContainerDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='UpdateAutonomousContainerDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.update_autonomous_container_database(
                autonomous_container_database_id=request.pop(util.camelize('autonomousContainerDatabaseId')),
                update_autonomous_container_database_details=request.pop(util.camelize('UpdateAutonomousContainerDatabaseDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'UpdateAutonomousContainerDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousContainerDatabase',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_update_autonomous_data_warehouse(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'UpdateAutonomousDataWarehouse'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'UpdateAutonomousDataWarehouse')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='UpdateAutonomousDataWarehouse')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.update_autonomous_data_warehouse(
                autonomous_data_warehouse_id=request.pop(util.camelize('autonomousDataWarehouseId')),
                update_autonomous_data_warehouse_details=request.pop(util.camelize('UpdateAutonomousDataWarehouseDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'UpdateAutonomousDataWarehouse',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousDataWarehouse',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-adb" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_update_autonomous_database(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'UpdateAutonomousDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'UpdateAutonomousDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='UpdateAutonomousDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.update_autonomous_database(
                autonomous_database_id=request.pop(util.camelize('autonomousDatabaseId')),
                update_autonomous_database_details=request.pop(util.camelize('UpdateAutonomousDatabaseDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'UpdateAutonomousDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousDatabase',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-adb" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_update_autonomous_database_regional_wallet(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'UpdateAutonomousDatabaseRegionalWallet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'UpdateAutonomousDatabaseRegionalWallet')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='UpdateAutonomousDatabaseRegionalWallet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.update_autonomous_database_regional_wallet(
                update_autonomous_database_wallet_details=request.pop(util.camelize('UpdateAutonomousDatabaseWalletDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'UpdateAutonomousDatabaseRegionalWallet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_autonomous_database_regional_wallet',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-adb" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_update_autonomous_database_wallet(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'UpdateAutonomousDatabaseWallet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'UpdateAutonomousDatabaseWallet')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='UpdateAutonomousDatabaseWallet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.update_autonomous_database_wallet(
                autonomous_database_id=request.pop(util.camelize('autonomousDatabaseId')),
                update_autonomous_database_wallet_details=request.pop(util.camelize('UpdateAutonomousDatabaseWalletDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'UpdateAutonomousDatabaseWallet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_autonomous_database_wallet',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-atp-d" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_update_autonomous_exadata_infrastructure(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'UpdateAutonomousExadataInfrastructure'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'UpdateAutonomousExadataInfrastructure')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='UpdateAutonomousExadataInfrastructure')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.update_autonomous_exadata_infrastructure(
                autonomous_exadata_infrastructure_id=request.pop(util.camelize('autonomousExadataInfrastructureId')),
                update_autonomous_exadata_infrastructures_details=request.pop(util.camelize('UpdateAutonomousExadataInfrastructuresDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'UpdateAutonomousExadataInfrastructure',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousExadataInfrastructure',
            False,
            False
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_update_autonomous_vm_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'UpdateAutonomousVmCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'UpdateAutonomousVmCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='UpdateAutonomousVmCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.update_autonomous_vm_cluster(
                autonomous_vm_cluster_id=request.pop(util.camelize('autonomousVmClusterId')),
                update_autonomous_vm_cluster_details=request.pop(util.camelize('UpdateAutonomousVmClusterDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'UpdateAutonomousVmCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autonomousVmCluster',
            False,
            False
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_update_backup_destination(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'UpdateBackupDestination'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'UpdateBackupDestination')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='UpdateBackupDestination')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.update_backup_destination(
                backup_destination_id=request.pop(util.camelize('backupDestinationId')),
                update_backup_destination_details=request.pop(util.camelize('UpdateBackupDestinationDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'UpdateBackupDestination',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'backupDestination',
            False,
            False
        )


# IssueRoutingInfo tag="ExaCS" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_update_cloud_exadata_infrastructure(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'UpdateCloudExadataInfrastructure'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'UpdateCloudExadataInfrastructure')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='UpdateCloudExadataInfrastructure')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.update_cloud_exadata_infrastructure(
                cloud_exadata_infrastructure_id=request.pop(util.camelize('cloudExadataInfrastructureId')),
                update_cloud_exadata_infrastructure_details=request.pop(util.camelize('UpdateCloudExadataInfrastructureDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'UpdateCloudExadataInfrastructure',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cloudExadataInfrastructure',
            False,
            False
        )


# IssueRoutingInfo tag="ExaCS" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_update_cloud_vm_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'UpdateCloudVmCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'UpdateCloudVmCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='UpdateCloudVmCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.update_cloud_vm_cluster(
                cloud_vm_cluster_id=request.pop(util.camelize('cloudVmClusterId')),
                update_cloud_vm_cluster_details=request.pop(util.camelize('UpdateCloudVmClusterDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'UpdateCloudVmCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cloudVmCluster',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_update_cloud_vm_cluster_iorm_config(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'UpdateCloudVmClusterIormConfig'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'UpdateCloudVmClusterIormConfig')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='UpdateCloudVmClusterIormConfig')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.update_cloud_vm_cluster_iorm_config(
                cloud_vm_cluster_id=request.pop(util.camelize('cloudVmClusterId')),
                cloud_vm_cluster_iorm_config_update_details=request.pop(util.camelize('CloudVmClusterIormConfigUpdateDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'UpdateCloudVmClusterIormConfig',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'exadataIormConfig',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_update_database(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'UpdateDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'UpdateDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='UpdateDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.update_database(
                database_id=request.pop(util.camelize('databaseId')),
                update_database_details=request.pop(util.camelize('UpdateDatabaseDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'UpdateDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'database',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_update_database_software_image(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'UpdateDatabaseSoftwareImage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'UpdateDatabaseSoftwareImage')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='UpdateDatabaseSoftwareImage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.update_database_software_image(
                database_software_image_id=request.pop(util.camelize('databaseSoftwareImageId')),
                update_database_software_image_details=request.pop(util.camelize('UpdateDatabaseSoftwareImageDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'UpdateDatabaseSoftwareImage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'databaseSoftwareImage',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_update_db_home(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'UpdateDbHome'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'UpdateDbHome')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='UpdateDbHome')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.update_db_home(
                db_home_id=request.pop(util.camelize('dbHomeId')),
                update_db_home_details=request.pop(util.camelize('UpdateDbHomeDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'UpdateDbHome',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dbHome',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_update_db_system(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'UpdateDbSystem'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'UpdateDbSystem')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='UpdateDbSystem')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.update_db_system(
                db_system_id=request.pop(util.camelize('dbSystemId')),
                update_db_system_details=request.pop(util.camelize('UpdateDbSystemDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'UpdateDbSystem',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dbSystem',
            False,
            False
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_update_exadata_infrastructure(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'UpdateExadataInfrastructure'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'UpdateExadataInfrastructure')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='UpdateExadataInfrastructure')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.update_exadata_infrastructure(
                exadata_infrastructure_id=request.pop(util.camelize('exadataInfrastructureId')),
                update_exadata_infrastructure_details=request.pop(util.camelize('UpdateExadataInfrastructureDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'UpdateExadataInfrastructure',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'exadataInfrastructure',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_update_exadata_iorm_config(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'UpdateExadataIormConfig'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'UpdateExadataIormConfig')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='UpdateExadataIormConfig')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.update_exadata_iorm_config(
                db_system_id=request.pop(util.camelize('dbSystemId')),
                exadata_iorm_config_update_details=request.pop(util.camelize('ExadataIormConfigUpdateDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'UpdateExadataIormConfig',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'exadataIormConfig',
            False,
            False
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_update_key_store(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'UpdateKeyStore'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'UpdateKeyStore')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='UpdateKeyStore')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.update_key_store(
                key_store_id=request.pop(util.camelize('keyStoreId')),
                update_key_store_details=request.pop(util.camelize('UpdateKeyStoreDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'UpdateKeyStore',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'keyStore',
            False,
            False
        )


# IssueRoutingInfo tag="dbaas-atp-d" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_update_maintenance_run(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'UpdateMaintenanceRun'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'UpdateMaintenanceRun')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='UpdateMaintenanceRun')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.update_maintenance_run(
                maintenance_run_id=request.pop(util.camelize('maintenanceRunId')),
                update_maintenance_run_details=request.pop(util.camelize('UpdateMaintenanceRunDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'UpdateMaintenanceRun',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'maintenanceRun',
            False,
            False
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_update_vm_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'UpdateVmCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'UpdateVmCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='UpdateVmCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.update_vm_cluster(
                vm_cluster_id=request.pop(util.camelize('vmClusterId')),
                update_vm_cluster_details=request.pop(util.camelize('UpdateVmClusterDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'UpdateVmCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'vmCluster',
            False,
            False
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_update_vm_cluster_network(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'UpdateVmClusterNetwork'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'UpdateVmClusterNetwork')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='UpdateVmClusterNetwork')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.update_vm_cluster_network(
                exadata_infrastructure_id=request.pop(util.camelize('exadataInfrastructureId')),
                vm_cluster_network_id=request.pop(util.camelize('vmClusterNetworkId')),
                update_vm_cluster_network_details=request.pop(util.camelize('UpdateVmClusterNetworkDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'UpdateVmClusterNetwork',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'vmClusterNetwork',
            False,
            False
        )


# IssueRoutingInfo tag="ExaCC" email="sic_dbaas_cp_us_grp@oracle.com" jiraProject="DBAAS" opsJiraProject="DBAASOPS"
def test_validate_vm_cluster_network(testing_service_client):
    if not testing_service_client.is_api_enabled('database', 'ValidateVmClusterNetwork'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database', util.camelize('database'), 'ValidateVmClusterNetwork')
    )

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ValidateVmClusterNetwork')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database.DatabaseClient(config, service_endpoint=service_endpoint)
            response = client.validate_vm_cluster_network(
                exadata_infrastructure_id=request.pop(util.camelize('exadataInfrastructureId')),
                vm_cluster_network_id=request.pop(util.camelize('vmClusterNetworkId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database',
            'ValidateVmClusterNetwork',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'vmClusterNetwork',
            False,
            False
        )
