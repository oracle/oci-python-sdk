# Code generated. DO NOT EDIT.
# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

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
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_bds_instances(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_bds_instances(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
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
