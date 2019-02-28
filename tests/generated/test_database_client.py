# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

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
    # use the default matching logic (link below) with the exception of 'session_agnostic_query_matcher'
    # instead of 'query' matcher (which ignores sessionId in the url)
    # https://vcrpy.readthedocs.io/en/latest/configuration.html#request-matching
    custom_vcr = test_config_container.create_vcr()
    custom_vcr.register_matcher('session_agnostic_query_matcher', session_agnostic_query_matcher)

    cassette_location = os.path.join('generated', 'database_{name}.yml'.format(name=request.function.__name__))
    with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
        yield


def test_complete_external_backup_job(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'CompleteExternalBackupJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='CompleteExternalBackupJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.complete_external_backup_job(
                backup_id=request.pop(util.camelize('backup_id')),
                complete_external_backup_job_details=request.pop(util.camelize('complete_external_backup_job_details')),
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


def test_create_autonomous_data_warehouse(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'CreateAutonomousDataWarehouse'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='CreateAutonomousDataWarehouse')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.create_autonomous_data_warehouse(
                create_autonomous_data_warehouse_details=request.pop(util.camelize('create_autonomous_data_warehouse_details')),
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


def test_create_autonomous_data_warehouse_backup(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'CreateAutonomousDataWarehouseBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='CreateAutonomousDataWarehouseBackup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.create_autonomous_data_warehouse_backup(
                create_autonomous_data_warehouse_backup_details=request.pop(util.camelize('create_autonomous_data_warehouse_backup_details')),
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


def test_create_autonomous_database(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'CreateAutonomousDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='CreateAutonomousDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.create_autonomous_database(
                create_autonomous_database_details=request.pop(util.camelize('create_autonomous_database_details')),
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


def test_create_autonomous_database_backup(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'CreateAutonomousDatabaseBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='CreateAutonomousDatabaseBackup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.create_autonomous_database_backup(
                create_autonomous_database_backup_details=request.pop(util.camelize('create_autonomous_database_backup_details')),
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


def test_create_backup(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'CreateBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='CreateBackup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.create_backup(
                create_backup_details=request.pop(util.camelize('create_backup_details')),
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


def test_create_data_guard_association(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'CreateDataGuardAssociation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='CreateDataGuardAssociation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.create_data_guard_association(
                database_id=request.pop(util.camelize('database_id')),
                create_data_guard_association_details=request.pop(util.camelize('create_data_guard_association_details')),
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


def test_create_db_home(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'CreateDbHome'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='CreateDbHome')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.create_db_home(
                create_db_home_with_db_system_id_details=request.pop(util.camelize('create_db_home_with_db_system_id_details')),
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


def test_create_external_backup_job(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'CreateExternalBackupJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='CreateExternalBackupJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.create_external_backup_job(
                create_external_backup_job_details=request.pop(util.camelize('create_external_backup_job_details')),
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


def test_db_node_action(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'DbNodeAction'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='DbNodeAction')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.db_node_action(
                db_node_id=request.pop(util.camelize('db_node_id')),
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


def test_delete_autonomous_data_warehouse(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'DeleteAutonomousDataWarehouse'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='DeleteAutonomousDataWarehouse')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.delete_autonomous_data_warehouse(
                autonomous_data_warehouse_id=request.pop(util.camelize('autonomous_data_warehouse_id')),
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


def test_delete_autonomous_database(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'DeleteAutonomousDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='DeleteAutonomousDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.delete_autonomous_database(
                autonomous_database_id=request.pop(util.camelize('autonomous_database_id')),
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


def test_delete_backup(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'DeleteBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='DeleteBackup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.delete_backup(
                backup_id=request.pop(util.camelize('backup_id')),
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


def test_delete_db_home(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'DeleteDbHome'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='DeleteDbHome')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.delete_db_home(
                db_home_id=request.pop(util.camelize('db_home_id')),
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


def test_failover_data_guard_association(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'FailoverDataGuardAssociation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='FailoverDataGuardAssociation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.failover_data_guard_association(
                database_id=request.pop(util.camelize('database_id')),
                data_guard_association_id=request.pop(util.camelize('data_guard_association_id')),
                failover_data_guard_association_details=request.pop(util.camelize('failover_data_guard_association_details')),
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


def test_generate_autonomous_data_warehouse_wallet(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'GenerateAutonomousDataWarehouseWallet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GenerateAutonomousDataWarehouseWallet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.generate_autonomous_data_warehouse_wallet(
                autonomous_data_warehouse_id=request.pop(util.camelize('autonomous_data_warehouse_id')),
                generate_autonomous_data_warehouse_wallet_details=request.pop(util.camelize('generate_autonomous_data_warehouse_wallet_details')),
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


def test_generate_autonomous_database_wallet(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'GenerateAutonomousDatabaseWallet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GenerateAutonomousDatabaseWallet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.generate_autonomous_database_wallet(
                autonomous_database_id=request.pop(util.camelize('autonomous_database_id')),
                generate_autonomous_database_wallet_details=request.pop(util.camelize('generate_autonomous_database_wallet_details')),
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


def test_get_autonomous_data_warehouse(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'GetAutonomousDataWarehouse'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetAutonomousDataWarehouse')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.get_autonomous_data_warehouse(
                autonomous_data_warehouse_id=request.pop(util.camelize('autonomous_data_warehouse_id')),
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


def test_get_autonomous_data_warehouse_backup(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'GetAutonomousDataWarehouseBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetAutonomousDataWarehouseBackup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.get_autonomous_data_warehouse_backup(
                autonomous_data_warehouse_backup_id=request.pop(util.camelize('autonomous_data_warehouse_backup_id')),
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


def test_get_autonomous_database(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'GetAutonomousDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetAutonomousDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.get_autonomous_database(
                autonomous_database_id=request.pop(util.camelize('autonomous_database_id')),
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


def test_get_autonomous_database_backup(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'GetAutonomousDatabaseBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetAutonomousDatabaseBackup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.get_autonomous_database_backup(
                autonomous_database_backup_id=request.pop(util.camelize('autonomous_database_backup_id')),
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


def test_get_backup(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'GetBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetBackup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.get_backup(
                backup_id=request.pop(util.camelize('backup_id')),
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


def test_get_data_guard_association(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'GetDataGuardAssociation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetDataGuardAssociation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.get_data_guard_association(
                database_id=request.pop(util.camelize('database_id')),
                data_guard_association_id=request.pop(util.camelize('data_guard_association_id')),
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


def test_get_database(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'GetDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.get_database(
                database_id=request.pop(util.camelize('database_id')),
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


def test_get_db_home(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'GetDbHome'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetDbHome')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.get_db_home(
                db_home_id=request.pop(util.camelize('db_home_id')),
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


def test_get_db_home_patch(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'GetDbHomePatch'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetDbHomePatch')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.get_db_home_patch(
                db_home_id=request.pop(util.camelize('db_home_id')),
                patch_id=request.pop(util.camelize('patch_id')),
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


def test_get_db_home_patch_history_entry(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'GetDbHomePatchHistoryEntry'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetDbHomePatchHistoryEntry')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.get_db_home_patch_history_entry(
                db_home_id=request.pop(util.camelize('db_home_id')),
                patch_history_entry_id=request.pop(util.camelize('patch_history_entry_id')),
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


def test_get_db_node(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'GetDbNode'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetDbNode')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.get_db_node(
                db_node_id=request.pop(util.camelize('db_node_id')),
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


def test_get_db_system(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'GetDbSystem'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetDbSystem')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.get_db_system(
                db_system_id=request.pop(util.camelize('db_system_id')),
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


def test_get_db_system_patch(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'GetDbSystemPatch'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetDbSystemPatch')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.get_db_system_patch(
                db_system_id=request.pop(util.camelize('db_system_id')),
                patch_id=request.pop(util.camelize('patch_id')),
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


def test_get_db_system_patch_history_entry(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'GetDbSystemPatchHistoryEntry'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetDbSystemPatchHistoryEntry')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.get_db_system_patch_history_entry(
                db_system_id=request.pop(util.camelize('db_system_id')),
                patch_history_entry_id=request.pop(util.camelize('patch_history_entry_id')),
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


def test_get_external_backup_job(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'GetExternalBackupJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='GetExternalBackupJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.get_external_backup_job(
                backup_id=request.pop(util.camelize('backup_id')),
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


def test_launch_db_system(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'LaunchDbSystem'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='LaunchDbSystem')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.launch_db_system(
                launch_db_system_details=request.pop(util.camelize('launch_db_system_details')),
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


def test_list_autonomous_data_warehouse_backups(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'ListAutonomousDataWarehouseBackups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListAutonomousDataWarehouseBackups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.list_autonomous_data_warehouse_backups(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
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


def test_list_autonomous_data_warehouses(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'ListAutonomousDataWarehouses'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListAutonomousDataWarehouses')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.list_autonomous_data_warehouses(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_autonomous_data_warehouses(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_autonomous_data_warehouses(
                        compartment_id=request.pop(util.camelize('compartment_id')),
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


def test_list_autonomous_database_backups(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'ListAutonomousDatabaseBackups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListAutonomousDatabaseBackups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.list_autonomous_database_backups(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
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


def test_list_autonomous_databases(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'ListAutonomousDatabases'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListAutonomousDatabases')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.list_autonomous_databases(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_autonomous_databases(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_autonomous_databases(
                        compartment_id=request.pop(util.camelize('compartment_id')),
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


def test_list_backups(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'ListBackups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListBackups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.list_backups(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
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


def test_list_data_guard_associations(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'ListDataGuardAssociations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListDataGuardAssociations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.list_data_guard_associations(
                database_id=request.pop(util.camelize('database_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_data_guard_associations(
                    database_id=request.pop(util.camelize('database_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_data_guard_associations(
                        database_id=request.pop(util.camelize('database_id')),
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


def test_list_databases(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'ListDatabases'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListDatabases')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.list_databases(
                compartment_id=request.pop(util.camelize('compartment_id')),
                db_home_id=request.pop(util.camelize('db_home_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_databases(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    db_home_id=request.pop(util.camelize('db_home_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_databases(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        db_home_id=request.pop(util.camelize('db_home_id')),
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


def test_list_db_home_patch_history_entries(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'ListDbHomePatchHistoryEntries'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListDbHomePatchHistoryEntries')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.list_db_home_patch_history_entries(
                db_home_id=request.pop(util.camelize('db_home_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_db_home_patch_history_entries(
                    db_home_id=request.pop(util.camelize('db_home_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_db_home_patch_history_entries(
                        db_home_id=request.pop(util.camelize('db_home_id')),
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


def test_list_db_home_patches(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'ListDbHomePatches'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListDbHomePatches')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.list_db_home_patches(
                db_home_id=request.pop(util.camelize('db_home_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_db_home_patches(
                    db_home_id=request.pop(util.camelize('db_home_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_db_home_patches(
                        db_home_id=request.pop(util.camelize('db_home_id')),
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


def test_list_db_homes(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'ListDbHomes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListDbHomes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.list_db_homes(
                compartment_id=request.pop(util.camelize('compartment_id')),
                db_system_id=request.pop(util.camelize('db_system_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_db_homes(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    db_system_id=request.pop(util.camelize('db_system_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_db_homes(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        db_system_id=request.pop(util.camelize('db_system_id')),
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


def test_list_db_nodes(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'ListDbNodes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListDbNodes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.list_db_nodes(
                compartment_id=request.pop(util.camelize('compartment_id')),
                db_system_id=request.pop(util.camelize('db_system_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_db_nodes(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    db_system_id=request.pop(util.camelize('db_system_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_db_nodes(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        db_system_id=request.pop(util.camelize('db_system_id')),
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


def test_list_db_system_patch_history_entries(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'ListDbSystemPatchHistoryEntries'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListDbSystemPatchHistoryEntries')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.list_db_system_patch_history_entries(
                db_system_id=request.pop(util.camelize('db_system_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_db_system_patch_history_entries(
                    db_system_id=request.pop(util.camelize('db_system_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_db_system_patch_history_entries(
                        db_system_id=request.pop(util.camelize('db_system_id')),
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


def test_list_db_system_patches(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'ListDbSystemPatches'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListDbSystemPatches')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.list_db_system_patches(
                db_system_id=request.pop(util.camelize('db_system_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_db_system_patches(
                    db_system_id=request.pop(util.camelize('db_system_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_db_system_patches(
                        db_system_id=request.pop(util.camelize('db_system_id')),
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


def test_list_db_system_shapes(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'ListDbSystemShapes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListDbSystemShapes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.list_db_system_shapes(
                availability_domain=request.pop(util.camelize('availability_domain')),
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_db_system_shapes(
                    availability_domain=request.pop(util.camelize('availability_domain')),
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_db_system_shapes(
                        availability_domain=request.pop(util.camelize('availability_domain')),
                        compartment_id=request.pop(util.camelize('compartment_id')),
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


def test_list_db_systems(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'ListDbSystems'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListDbSystems')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.list_db_systems(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_db_systems(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_db_systems(
                        compartment_id=request.pop(util.camelize('compartment_id')),
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


def test_list_db_versions(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'ListDbVersions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ListDbVersions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.list_db_versions(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_db_versions(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_db_versions(
                        compartment_id=request.pop(util.camelize('compartment_id')),
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


def test_reinstate_data_guard_association(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'ReinstateDataGuardAssociation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='ReinstateDataGuardAssociation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.reinstate_data_guard_association(
                database_id=request.pop(util.camelize('database_id')),
                data_guard_association_id=request.pop(util.camelize('data_guard_association_id')),
                reinstate_data_guard_association_details=request.pop(util.camelize('reinstate_data_guard_association_details')),
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


def test_restore_autonomous_data_warehouse(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'RestoreAutonomousDataWarehouse'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='RestoreAutonomousDataWarehouse')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.restore_autonomous_data_warehouse(
                autonomous_data_warehouse_id=request.pop(util.camelize('autonomous_data_warehouse_id')),
                restore_autonomous_data_warehouse_details=request.pop(util.camelize('restore_autonomous_data_warehouse_details')),
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


def test_restore_autonomous_database(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'RestoreAutonomousDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='RestoreAutonomousDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.restore_autonomous_database(
                autonomous_database_id=request.pop(util.camelize('autonomous_database_id')),
                restore_autonomous_database_details=request.pop(util.camelize('restore_autonomous_database_details')),
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


def test_restore_database(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'RestoreDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='RestoreDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.restore_database(
                database_id=request.pop(util.camelize('database_id')),
                restore_database_details=request.pop(util.camelize('restore_database_details')),
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


def test_start_autonomous_data_warehouse(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'StartAutonomousDataWarehouse'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='StartAutonomousDataWarehouse')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.start_autonomous_data_warehouse(
                autonomous_data_warehouse_id=request.pop(util.camelize('autonomous_data_warehouse_id')),
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


def test_start_autonomous_database(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'StartAutonomousDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='StartAutonomousDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.start_autonomous_database(
                autonomous_database_id=request.pop(util.camelize('autonomous_database_id')),
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


def test_stop_autonomous_data_warehouse(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'StopAutonomousDataWarehouse'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='StopAutonomousDataWarehouse')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.stop_autonomous_data_warehouse(
                autonomous_data_warehouse_id=request.pop(util.camelize('autonomous_data_warehouse_id')),
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


def test_stop_autonomous_database(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'StopAutonomousDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='StopAutonomousDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.stop_autonomous_database(
                autonomous_database_id=request.pop(util.camelize('autonomous_database_id')),
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


def test_switchover_data_guard_association(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'SwitchoverDataGuardAssociation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='SwitchoverDataGuardAssociation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.switchover_data_guard_association(
                database_id=request.pop(util.camelize('database_id')),
                data_guard_association_id=request.pop(util.camelize('data_guard_association_id')),
                switchover_data_guard_association_details=request.pop(util.camelize('switchover_data_guard_association_details')),
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


def test_terminate_db_system(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'TerminateDbSystem'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='TerminateDbSystem')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.terminate_db_system(
                db_system_id=request.pop(util.camelize('db_system_id')),
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


def test_update_autonomous_data_warehouse(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'UpdateAutonomousDataWarehouse'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='UpdateAutonomousDataWarehouse')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.update_autonomous_data_warehouse(
                autonomous_data_warehouse_id=request.pop(util.camelize('autonomous_data_warehouse_id')),
                update_autonomous_data_warehouse_details=request.pop(util.camelize('update_autonomous_data_warehouse_details')),
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


def test_update_autonomous_database(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'UpdateAutonomousDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='UpdateAutonomousDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.update_autonomous_database(
                autonomous_database_id=request.pop(util.camelize('autonomous_database_id')),
                update_autonomous_database_details=request.pop(util.camelize('update_autonomous_database_details')),
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


def test_update_database(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'UpdateDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='UpdateDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.update_database(
                database_id=request.pop(util.camelize('database_id')),
                update_database_details=request.pop(util.camelize('update_database_details')),
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


def test_update_db_home(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'UpdateDbHome'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='UpdateDbHome')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.update_db_home(
                db_home_id=request.pop(util.camelize('db_home_id')),
                update_db_home_details=request.pop(util.camelize('update_db_home_details')),
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


def test_update_db_system(testing_service_client, config):
    if not testing_service_client.is_api_enabled('database', 'UpdateDbSystem'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='database', api_name='UpdateDbSystem')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.database.DatabaseClient(config)
            response = client.update_db_system(
                db_system_id=request.pop(util.camelize('db_system_id')),
                update_db_system_details=request.pop(util.camelize('update_db_system_details')),
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