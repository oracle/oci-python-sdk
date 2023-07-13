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

        cassette_location = os.path.join('generated', 'bds_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_activate_bds_metastore_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'ActivateBdsMetastoreConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'ActivateBdsMetastoreConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='ActivateBdsMetastoreConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.activate_bds_metastore_configuration(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                metastore_config_id=request.pop(util.camelize('metastoreConfigId')),
                activate_bds_metastore_configuration_details=request.pop(util.camelize('ActivateBdsMetastoreConfigurationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'ActivateBdsMetastoreConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'activate_bds_metastore_configuration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_add_auto_scaling_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'AddAutoScalingConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'AddAutoScalingConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='AddAutoScalingConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.add_auto_scaling_configuration(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                add_auto_scaling_configuration_details=request.pop(util.camelize('AddAutoScalingConfigurationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'AddAutoScalingConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'add_auto_scaling_configuration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_add_block_storage(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'AddBlockStorage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'AddBlockStorage')
    )

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='AddBlockStorage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.add_block_storage(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                add_block_storage_details=request.pop(util.camelize('AddBlockStorageDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'AddBlockStorage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'add_block_storage',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_add_cloud_sql(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'AddCloudSql'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'AddCloudSql')
    )

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='AddCloudSql')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.add_cloud_sql(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                add_cloud_sql_details=request.pop(util.camelize('AddCloudSqlDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'AddCloudSql',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'add_cloud_sql',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_add_kafka(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'AddKafka'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'AddKafka')
    )

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='AddKafka')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.add_kafka(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                add_kafka_details=request.pop(util.camelize('AddKafkaDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'AddKafka',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'add_kafka',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_add_master_nodes(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'AddMasterNodes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'AddMasterNodes')
    )

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='AddMasterNodes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.add_master_nodes(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                add_master_nodes_details=request.pop(util.camelize('AddMasterNodesDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'AddMasterNodes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'add_master_nodes',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_add_utility_nodes(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'AddUtilityNodes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'AddUtilityNodes')
    )

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='AddUtilityNodes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.add_utility_nodes(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                add_utility_nodes_details=request.pop(util.camelize('AddUtilityNodesDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'AddUtilityNodes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'add_utility_nodes',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_add_worker_nodes(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'AddWorkerNodes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'AddWorkerNodes')
    )

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='AddWorkerNodes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.add_worker_nodes(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                add_worker_nodes_details=request.pop(util.camelize('AddWorkerNodesDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'AddWorkerNodes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'add_worker_nodes',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_change_bds_instance_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'ChangeBdsInstanceCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'ChangeBdsInstanceCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='ChangeBdsInstanceCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.change_bds_instance_compartment(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                change_bds_instance_compartment_details=request.pop(util.camelize('ChangeBdsInstanceCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'ChangeBdsInstanceCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_bds_instance_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_change_shape(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'ChangeShape'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'ChangeShape')
    )

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='ChangeShape')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.change_shape(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                change_shape_details=request.pop(util.camelize('ChangeShapeDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'ChangeShape',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_shape',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_create_bds_api_key(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'CreateBdsApiKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'CreateBdsApiKey')
    )

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='CreateBdsApiKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.create_bds_api_key(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                create_bds_api_key_details=request.pop(util.camelize('CreateBdsApiKeyDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'CreateBdsApiKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_bds_api_key',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_create_bds_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'CreateBdsInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'CreateBdsInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='CreateBdsInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.create_bds_instance(
                create_bds_instance_details=request.pop(util.camelize('CreateBdsInstanceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'CreateBdsInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_bds_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_create_bds_metastore_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'CreateBdsMetastoreConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'CreateBdsMetastoreConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='CreateBdsMetastoreConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.create_bds_metastore_configuration(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                create_bds_metastore_configuration_details=request.pop(util.camelize('CreateBdsMetastoreConfigurationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'CreateBdsMetastoreConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_bds_metastore_configuration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_delete_bds_api_key(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'DeleteBdsApiKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'DeleteBdsApiKey')
    )

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='DeleteBdsApiKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.delete_bds_api_key(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                api_key_id=request.pop(util.camelize('apiKeyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'DeleteBdsApiKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_bds_api_key',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_delete_bds_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'DeleteBdsInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'DeleteBdsInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='DeleteBdsInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.delete_bds_instance(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'DeleteBdsInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_bds_instance',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_delete_bds_metastore_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'DeleteBdsMetastoreConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'DeleteBdsMetastoreConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='DeleteBdsMetastoreConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.delete_bds_metastore_configuration(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                metastore_config_id=request.pop(util.camelize('metastoreConfigId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'DeleteBdsMetastoreConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_bds_metastore_configuration',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_execute_bootstrap_script(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'ExecuteBootstrapScript'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'ExecuteBootstrapScript')
    )

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='ExecuteBootstrapScript')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.execute_bootstrap_script(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                execute_bootstrap_script_details=request.pop(util.camelize('ExecuteBootstrapScriptDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'ExecuteBootstrapScript',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'execute_bootstrap_script',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_get_auto_scaling_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'GetAutoScalingConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'GetAutoScalingConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='GetAutoScalingConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.get_auto_scaling_configuration(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                auto_scaling_configuration_id=request.pop(util.camelize('autoScalingConfigurationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'GetAutoScalingConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autoScalingConfiguration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_get_bds_api_key(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'GetBdsApiKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'GetBdsApiKey')
    )

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='GetBdsApiKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.get_bds_api_key(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                api_key_id=request.pop(util.camelize('apiKeyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'GetBdsApiKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bdsApiKey',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_get_bds_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'GetBdsInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'GetBdsInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='GetBdsInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.get_bds_instance(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'GetBdsInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bdsInstance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_get_bds_metastore_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'GetBdsMetastoreConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'GetBdsMetastoreConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='GetBdsMetastoreConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.get_bds_metastore_configuration(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                metastore_config_id=request.pop(util.camelize('metastoreConfigId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'GetBdsMetastoreConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bdsMetastoreConfiguration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_get_os_patch_details(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'GetOsPatchDetails'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'GetOsPatchDetails')
    )

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='GetOsPatchDetails')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.get_os_patch_details(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                os_patch_version=request.pop(util.camelize('osPatchVersion')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'GetOsPatchDetails',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'osPatchDetails',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_install_os_patch(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'InstallOsPatch'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'InstallOsPatch')
    )

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='InstallOsPatch')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.install_os_patch(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                install_os_patch_details=request.pop(util.camelize('InstallOsPatchDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'InstallOsPatch',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'install_os_patch',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_install_patch(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'InstallPatch'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'InstallPatch')
    )

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='InstallPatch')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.install_patch(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                install_patch_details=request.pop(util.camelize('InstallPatchDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'InstallPatch',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'install_patch',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_list_auto_scaling_configurations(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'ListAutoScalingConfigurations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'ListAutoScalingConfigurations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='ListAutoScalingConfigurations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.list_auto_scaling_configurations(
                compartment_id=request.pop(util.camelize('compartmentId')),
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_auto_scaling_configurations(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_auto_scaling_configurations(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'ListAutoScalingConfigurations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'autoScalingConfigurationSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_list_bds_api_keys(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'ListBdsApiKeys'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'ListBdsApiKeys')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='ListBdsApiKeys')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.list_bds_api_keys(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_bds_api_keys(
                    bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_bds_api_keys(
                        bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'ListBdsApiKeys',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bdsApiKeySummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_list_bds_instances(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'ListBdsInstances'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'ListBdsInstances')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='ListBdsInstances')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.list_bds_instances(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_bds_instances(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_bds_instances(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'ListBdsInstances',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bdsInstanceSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_list_bds_metastore_configurations(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'ListBdsMetastoreConfigurations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'ListBdsMetastoreConfigurations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='ListBdsMetastoreConfigurations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.list_bds_metastore_configurations(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_bds_metastore_configurations(
                    bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_bds_metastore_configurations(
                        bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'ListBdsMetastoreConfigurations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bdsMetastoreConfigurationSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_list_os_patches(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'ListOsPatches'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'ListOsPatches')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='ListOsPatches')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.list_os_patches(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_os_patches(
                    bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_os_patches(
                        bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'ListOsPatches',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'osPatchSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_list_patch_histories(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'ListPatchHistories'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'ListPatchHistories')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='ListPatchHistories')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.list_patch_histories(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_patch_histories(
                    bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_patch_histories(
                        bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'ListPatchHistories',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'patchHistorySummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_list_patches(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'ListPatches'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'ListPatches')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='ListPatches')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.list_patches(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_patches(
                    bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_patches(
                        bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'ListPatches',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'patchSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
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
            'bds',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestError',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
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
            'bds',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntry',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.list_work_requests(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_requests(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_requests(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_remove_auto_scaling_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'RemoveAutoScalingConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'RemoveAutoScalingConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='RemoveAutoScalingConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.remove_auto_scaling_configuration(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                auto_scaling_configuration_id=request.pop(util.camelize('autoScalingConfigurationId')),
                remove_auto_scaling_configuration_details=request.pop(util.camelize('RemoveAutoScalingConfigurationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'RemoveAutoScalingConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'remove_auto_scaling_configuration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_remove_cloud_sql(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'RemoveCloudSql'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'RemoveCloudSql')
    )

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='RemoveCloudSql')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.remove_cloud_sql(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                remove_cloud_sql_details=request.pop(util.camelize('RemoveCloudSqlDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'RemoveCloudSql',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'remove_cloud_sql',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_remove_kafka(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'RemoveKafka'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'RemoveKafka')
    )

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='RemoveKafka')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.remove_kafka(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                remove_kafka_details=request.pop(util.camelize('RemoveKafkaDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'RemoveKafka',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'remove_kafka',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_remove_node(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'RemoveNode'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'RemoveNode')
    )

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='RemoveNode')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.remove_node(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                remove_node_details=request.pop(util.camelize('RemoveNodeDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'RemoveNode',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'remove_node',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_restart_node(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'RestartNode'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'RestartNode')
    )

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='RestartNode')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.restart_node(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                restart_node_details=request.pop(util.camelize('RestartNodeDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'RestartNode',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'restart_node',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_start_bds_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'StartBdsInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'StartBdsInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='StartBdsInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.start_bds_instance(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                start_bds_instance_details=request.pop(util.camelize('StartBdsInstanceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'StartBdsInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'start_bds_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_stop_bds_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'StopBdsInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'StopBdsInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='StopBdsInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.stop_bds_instance(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                stop_bds_instance_details=request.pop(util.camelize('StopBdsInstanceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'StopBdsInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stop_bds_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_test_bds_metastore_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'TestBdsMetastoreConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'TestBdsMetastoreConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='TestBdsMetastoreConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.test_bds_metastore_configuration(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                metastore_config_id=request.pop(util.camelize('metastoreConfigId')),
                test_bds_metastore_configuration_details=request.pop(util.camelize('TestBdsMetastoreConfigurationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'TestBdsMetastoreConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'test_bds_metastore_configuration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_test_bds_object_storage_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'TestBdsObjectStorageConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'TestBdsObjectStorageConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='TestBdsObjectStorageConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.test_bds_object_storage_connection(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                api_key_id=request.pop(util.camelize('apiKeyId')),
                test_bds_object_storage_connection_details=request.pop(util.camelize('TestBdsObjectStorageConnectionDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'TestBdsObjectStorageConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'test_bds_object_storage_connection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_update_auto_scaling_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'UpdateAutoScalingConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'UpdateAutoScalingConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='UpdateAutoScalingConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.update_auto_scaling_configuration(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                auto_scaling_configuration_id=request.pop(util.camelize('autoScalingConfigurationId')),
                update_auto_scaling_configuration_details=request.pop(util.camelize('UpdateAutoScalingConfigurationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'UpdateAutoScalingConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_auto_scaling_configuration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_update_bds_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'UpdateBdsInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'UpdateBdsInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='UpdateBdsInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.update_bds_instance(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                update_bds_instance_details=request.pop(util.camelize('UpdateBdsInstanceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'UpdateBdsInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_bds_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bdcs_dev_ww_grp@oracle.com" jiraProject="BDCS" opsJiraProject="OBDS"
def test_update_bds_metastore_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('bds', 'UpdateBdsMetastoreConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('bds', util.camelize('bds'), 'UpdateBdsMetastoreConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='bds', api_name='UpdateBdsMetastoreConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.bds.BdsClient(config, service_endpoint=service_endpoint)
            response = client.update_bds_metastore_configuration(
                bds_instance_id=request.pop(util.camelize('bdsInstanceId')),
                metastore_config_id=request.pop(util.camelize('metastoreConfigId')),
                update_bds_metastore_configuration_details=request.pop(util.camelize('UpdateBdsMetastoreConfigurationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'bds',
            'UpdateBdsMetastoreConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_bds_metastore_configuration',
            False,
            False
        )
