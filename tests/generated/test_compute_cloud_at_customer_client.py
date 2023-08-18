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

        cassette_location = os.path.join('generated', 'compute_cloud_at_customer_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="compute_cloud_at_customer_dev_grp@oracle.com" jiraProject="CCATC" opsJiraProject="CCATC"
def test_change_ccc_infrastructure_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('compute_cloud_at_customer', 'ChangeCccInfrastructureCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('compute_cloud_at_customer', util.camelize('compute_cloud_at_customer'), 'ChangeCccInfrastructureCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='compute_cloud_at_customer', api_name='ChangeCccInfrastructureCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.compute_cloud_at_customer.ComputeCloudAtCustomerClient(config, service_endpoint=service_endpoint)
            response = client.change_ccc_infrastructure_compartment(
                ccc_infrastructure_id=request.pop(util.camelize('cccInfrastructureId')),
                change_ccc_infrastructure_compartment_details=request.pop(util.camelize('ChangeCccInfrastructureCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'compute_cloud_at_customer',
            'ChangeCccInfrastructureCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_ccc_infrastructure_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="compute_cloud_at_customer_dev_grp@oracle.com" jiraProject="CCATC" opsJiraProject="CCATC"
def test_change_ccc_upgrade_schedule_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('compute_cloud_at_customer', 'ChangeCccUpgradeScheduleCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('compute_cloud_at_customer', util.camelize('compute_cloud_at_customer'), 'ChangeCccUpgradeScheduleCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='compute_cloud_at_customer', api_name='ChangeCccUpgradeScheduleCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.compute_cloud_at_customer.ComputeCloudAtCustomerClient(config, service_endpoint=service_endpoint)
            response = client.change_ccc_upgrade_schedule_compartment(
                ccc_upgrade_schedule_id=request.pop(util.camelize('cccUpgradeScheduleId')),
                change_ccc_upgrade_schedule_compartment_details=request.pop(util.camelize('ChangeCccUpgradeScheduleCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'compute_cloud_at_customer',
            'ChangeCccUpgradeScheduleCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_ccc_upgrade_schedule_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="compute_cloud_at_customer_dev_grp@oracle.com" jiraProject="CCATC" opsJiraProject="CCATC"
def test_create_ccc_infrastructure(testing_service_client):
    if not testing_service_client.is_api_enabled('compute_cloud_at_customer', 'CreateCccInfrastructure'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('compute_cloud_at_customer', util.camelize('compute_cloud_at_customer'), 'CreateCccInfrastructure')
    )

    request_containers = testing_service_client.get_requests(service_name='compute_cloud_at_customer', api_name='CreateCccInfrastructure')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.compute_cloud_at_customer.ComputeCloudAtCustomerClient(config, service_endpoint=service_endpoint)
            response = client.create_ccc_infrastructure(
                create_ccc_infrastructure_details=request.pop(util.camelize('CreateCccInfrastructureDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'compute_cloud_at_customer',
            'CreateCccInfrastructure',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cccInfrastructure',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="compute_cloud_at_customer_dev_grp@oracle.com" jiraProject="CCATC" opsJiraProject="CCATC"
def test_create_ccc_upgrade_schedule(testing_service_client):
    if not testing_service_client.is_api_enabled('compute_cloud_at_customer', 'CreateCccUpgradeSchedule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('compute_cloud_at_customer', util.camelize('compute_cloud_at_customer'), 'CreateCccUpgradeSchedule')
    )

    request_containers = testing_service_client.get_requests(service_name='compute_cloud_at_customer', api_name='CreateCccUpgradeSchedule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.compute_cloud_at_customer.ComputeCloudAtCustomerClient(config, service_endpoint=service_endpoint)
            response = client.create_ccc_upgrade_schedule(
                create_ccc_upgrade_schedule_details=request.pop(util.camelize('CreateCccUpgradeScheduleDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'compute_cloud_at_customer',
            'CreateCccUpgradeSchedule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cccUpgradeSchedule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="compute_cloud_at_customer_dev_grp@oracle.com" jiraProject="CCATC" opsJiraProject="CCATC"
def test_delete_ccc_infrastructure(testing_service_client):
    if not testing_service_client.is_api_enabled('compute_cloud_at_customer', 'DeleteCccInfrastructure'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('compute_cloud_at_customer', util.camelize('compute_cloud_at_customer'), 'DeleteCccInfrastructure')
    )

    request_containers = testing_service_client.get_requests(service_name='compute_cloud_at_customer', api_name='DeleteCccInfrastructure')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.compute_cloud_at_customer.ComputeCloudAtCustomerClient(config, service_endpoint=service_endpoint)
            response = client.delete_ccc_infrastructure(
                ccc_infrastructure_id=request.pop(util.camelize('cccInfrastructureId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'compute_cloud_at_customer',
            'DeleteCccInfrastructure',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_ccc_infrastructure',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="compute_cloud_at_customer_dev_grp@oracle.com" jiraProject="CCATC" opsJiraProject="CCATC"
def test_delete_ccc_upgrade_schedule(testing_service_client):
    if not testing_service_client.is_api_enabled('compute_cloud_at_customer', 'DeleteCccUpgradeSchedule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('compute_cloud_at_customer', util.camelize('compute_cloud_at_customer'), 'DeleteCccUpgradeSchedule')
    )

    request_containers = testing_service_client.get_requests(service_name='compute_cloud_at_customer', api_name='DeleteCccUpgradeSchedule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.compute_cloud_at_customer.ComputeCloudAtCustomerClient(config, service_endpoint=service_endpoint)
            response = client.delete_ccc_upgrade_schedule(
                ccc_upgrade_schedule_id=request.pop(util.camelize('cccUpgradeScheduleId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'compute_cloud_at_customer',
            'DeleteCccUpgradeSchedule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_ccc_upgrade_schedule',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="compute_cloud_at_customer_dev_grp@oracle.com" jiraProject="CCATC" opsJiraProject="CCATC"
def test_get_ccc_infrastructure(testing_service_client):
    if not testing_service_client.is_api_enabled('compute_cloud_at_customer', 'GetCccInfrastructure'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('compute_cloud_at_customer', util.camelize('compute_cloud_at_customer'), 'GetCccInfrastructure')
    )

    request_containers = testing_service_client.get_requests(service_name='compute_cloud_at_customer', api_name='GetCccInfrastructure')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.compute_cloud_at_customer.ComputeCloudAtCustomerClient(config, service_endpoint=service_endpoint)
            response = client.get_ccc_infrastructure(
                ccc_infrastructure_id=request.pop(util.camelize('cccInfrastructureId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'compute_cloud_at_customer',
            'GetCccInfrastructure',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cccInfrastructure',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="compute_cloud_at_customer_dev_grp@oracle.com" jiraProject="CCATC" opsJiraProject="CCATC"
def test_get_ccc_upgrade_schedule(testing_service_client):
    if not testing_service_client.is_api_enabled('compute_cloud_at_customer', 'GetCccUpgradeSchedule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('compute_cloud_at_customer', util.camelize('compute_cloud_at_customer'), 'GetCccUpgradeSchedule')
    )

    request_containers = testing_service_client.get_requests(service_name='compute_cloud_at_customer', api_name='GetCccUpgradeSchedule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.compute_cloud_at_customer.ComputeCloudAtCustomerClient(config, service_endpoint=service_endpoint)
            response = client.get_ccc_upgrade_schedule(
                ccc_upgrade_schedule_id=request.pop(util.camelize('cccUpgradeScheduleId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'compute_cloud_at_customer',
            'GetCccUpgradeSchedule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cccUpgradeSchedule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="compute_cloud_at_customer_dev_grp@oracle.com" jiraProject="CCATC" opsJiraProject="CCATC"
def test_list_ccc_infrastructures(testing_service_client):
    if not testing_service_client.is_api_enabled('compute_cloud_at_customer', 'ListCccInfrastructures'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('compute_cloud_at_customer', util.camelize('compute_cloud_at_customer'), 'ListCccInfrastructures')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='compute_cloud_at_customer', api_name='ListCccInfrastructures')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.compute_cloud_at_customer.ComputeCloudAtCustomerClient(config, service_endpoint=service_endpoint)
            response = client.list_ccc_infrastructures(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_ccc_infrastructures(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_ccc_infrastructures(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'compute_cloud_at_customer',
            'ListCccInfrastructures',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cccInfrastructureCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="compute_cloud_at_customer_dev_grp@oracle.com" jiraProject="CCATC" opsJiraProject="CCATC"
def test_list_ccc_upgrade_schedules(testing_service_client):
    if not testing_service_client.is_api_enabled('compute_cloud_at_customer', 'ListCccUpgradeSchedules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('compute_cloud_at_customer', util.camelize('compute_cloud_at_customer'), 'ListCccUpgradeSchedules')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='compute_cloud_at_customer', api_name='ListCccUpgradeSchedules')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.compute_cloud_at_customer.ComputeCloudAtCustomerClient(config, service_endpoint=service_endpoint)
            response = client.list_ccc_upgrade_schedules(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_ccc_upgrade_schedules(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_ccc_upgrade_schedules(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'compute_cloud_at_customer',
            'ListCccUpgradeSchedules',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cccUpgradeScheduleCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="compute_cloud_at_customer_dev_grp@oracle.com" jiraProject="CCATC" opsJiraProject="CCATC"
def test_update_ccc_infrastructure(testing_service_client):
    if not testing_service_client.is_api_enabled('compute_cloud_at_customer', 'UpdateCccInfrastructure'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('compute_cloud_at_customer', util.camelize('compute_cloud_at_customer'), 'UpdateCccInfrastructure')
    )

    request_containers = testing_service_client.get_requests(service_name='compute_cloud_at_customer', api_name='UpdateCccInfrastructure')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.compute_cloud_at_customer.ComputeCloudAtCustomerClient(config, service_endpoint=service_endpoint)
            response = client.update_ccc_infrastructure(
                ccc_infrastructure_id=request.pop(util.camelize('cccInfrastructureId')),
                update_ccc_infrastructure_details=request.pop(util.camelize('UpdateCccInfrastructureDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'compute_cloud_at_customer',
            'UpdateCccInfrastructure',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cccInfrastructure',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="compute_cloud_at_customer_dev_grp@oracle.com" jiraProject="CCATC" opsJiraProject="CCATC"
def test_update_ccc_upgrade_schedule(testing_service_client):
    if not testing_service_client.is_api_enabled('compute_cloud_at_customer', 'UpdateCccUpgradeSchedule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('compute_cloud_at_customer', util.camelize('compute_cloud_at_customer'), 'UpdateCccUpgradeSchedule')
    )

    request_containers = testing_service_client.get_requests(service_name='compute_cloud_at_customer', api_name='UpdateCccUpgradeSchedule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.compute_cloud_at_customer.ComputeCloudAtCustomerClient(config, service_endpoint=service_endpoint)
            response = client.update_ccc_upgrade_schedule(
                ccc_upgrade_schedule_id=request.pop(util.camelize('cccUpgradeScheduleId')),
                update_ccc_upgrade_schedule_details=request.pop(util.camelize('UpdateCccUpgradeScheduleDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'compute_cloud_at_customer',
            'UpdateCccUpgradeSchedule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cccUpgradeSchedule',
            False,
            False
        )
