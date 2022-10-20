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

        cassette_location = os.path.join('generated', 'disaster_recovery_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="psampath_org_ww@oracle.com" jiraProject="Site Guard as a Service (SGAS)" opsJiraProject="SGAS-OPS"
def test_associate_dr_protection_group(testing_service_client):
    if not testing_service_client.is_api_enabled('disaster_recovery', 'AssociateDrProtectionGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('disaster_recovery', util.camelize('disaster_recovery'), 'AssociateDrProtectionGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='disaster_recovery', api_name='AssociateDrProtectionGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.disaster_recovery.DisasterRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.associate_dr_protection_group(
                associate_dr_protection_group_details=request.pop(util.camelize('AssociateDrProtectionGroupDetails')),
                dr_protection_group_id=request.pop(util.camelize('drProtectionGroupId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'disaster_recovery',
            'AssociateDrProtectionGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'associate_dr_protection_group',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="psampath_org_ww@oracle.com" jiraProject="Site Guard as a Service (SGAS)" opsJiraProject="SGAS-OPS"
def test_cancel_dr_plan_execution(testing_service_client):
    if not testing_service_client.is_api_enabled('disaster_recovery', 'CancelDrPlanExecution'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('disaster_recovery', util.camelize('disaster_recovery'), 'CancelDrPlanExecution')
    )

    request_containers = testing_service_client.get_requests(service_name='disaster_recovery', api_name='CancelDrPlanExecution')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.disaster_recovery.DisasterRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.cancel_dr_plan_execution(
                cancel_dr_plan_execution_details=request.pop(util.camelize('CancelDrPlanExecutionDetails')),
                dr_plan_execution_id=request.pop(util.camelize('drPlanExecutionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'disaster_recovery',
            'CancelDrPlanExecution',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cancel_dr_plan_execution',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="psampath_org_ww@oracle.com" jiraProject="Site Guard as a Service (SGAS)" opsJiraProject="SGAS-OPS"
def test_cancel_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('disaster_recovery', 'CancelWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('disaster_recovery', util.camelize('disaster_recovery'), 'CancelWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='disaster_recovery', api_name='CancelWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.disaster_recovery.DisasterRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.cancel_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'disaster_recovery',
            'CancelWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cancel_work_request',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="psampath_org_ww@oracle.com" jiraProject="Site Guard as a Service (SGAS)" opsJiraProject="SGAS-OPS"
def test_change_dr_protection_group_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('disaster_recovery', 'ChangeDrProtectionGroupCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('disaster_recovery', util.camelize('disaster_recovery'), 'ChangeDrProtectionGroupCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='disaster_recovery', api_name='ChangeDrProtectionGroupCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.disaster_recovery.DisasterRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.change_dr_protection_group_compartment(
                change_dr_protection_group_compartment_details=request.pop(util.camelize('ChangeDrProtectionGroupCompartmentDetails')),
                dr_protection_group_id=request.pop(util.camelize('drProtectionGroupId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'disaster_recovery',
            'ChangeDrProtectionGroupCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_dr_protection_group_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="psampath_org_ww@oracle.com" jiraProject="Site Guard as a Service (SGAS)" opsJiraProject="SGAS-OPS"
def test_create_dr_plan(testing_service_client):
    if not testing_service_client.is_api_enabled('disaster_recovery', 'CreateDrPlan'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('disaster_recovery', util.camelize('disaster_recovery'), 'CreateDrPlan')
    )

    request_containers = testing_service_client.get_requests(service_name='disaster_recovery', api_name='CreateDrPlan')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.disaster_recovery.DisasterRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.create_dr_plan(
                create_dr_plan_details=request.pop(util.camelize('CreateDrPlanDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'disaster_recovery',
            'CreateDrPlan',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'drPlan',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="psampath_org_ww@oracle.com" jiraProject="Site Guard as a Service (SGAS)" opsJiraProject="SGAS-OPS"
def test_create_dr_plan_execution(testing_service_client):
    if not testing_service_client.is_api_enabled('disaster_recovery', 'CreateDrPlanExecution'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('disaster_recovery', util.camelize('disaster_recovery'), 'CreateDrPlanExecution')
    )

    request_containers = testing_service_client.get_requests(service_name='disaster_recovery', api_name='CreateDrPlanExecution')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.disaster_recovery.DisasterRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.create_dr_plan_execution(
                create_dr_plan_execution_details=request.pop(util.camelize('CreateDrPlanExecutionDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'disaster_recovery',
            'CreateDrPlanExecution',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'drPlanExecution',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="psampath_org_ww@oracle.com" jiraProject="Site Guard as a Service (SGAS)" opsJiraProject="SGAS-OPS"
def test_create_dr_protection_group(testing_service_client):
    if not testing_service_client.is_api_enabled('disaster_recovery', 'CreateDrProtectionGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('disaster_recovery', util.camelize('disaster_recovery'), 'CreateDrProtectionGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='disaster_recovery', api_name='CreateDrProtectionGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.disaster_recovery.DisasterRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.create_dr_protection_group(
                create_dr_protection_group_details=request.pop(util.camelize('CreateDrProtectionGroupDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'disaster_recovery',
            'CreateDrProtectionGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'drProtectionGroup',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="psampath_org_ww@oracle.com" jiraProject="Site Guard as a Service (SGAS)" opsJiraProject="SGAS-OPS"
def test_delete_dr_plan(testing_service_client):
    if not testing_service_client.is_api_enabled('disaster_recovery', 'DeleteDrPlan'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('disaster_recovery', util.camelize('disaster_recovery'), 'DeleteDrPlan')
    )

    request_containers = testing_service_client.get_requests(service_name='disaster_recovery', api_name='DeleteDrPlan')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.disaster_recovery.DisasterRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.delete_dr_plan(
                dr_plan_id=request.pop(util.camelize('drPlanId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'disaster_recovery',
            'DeleteDrPlan',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_dr_plan',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="psampath_org_ww@oracle.com" jiraProject="Site Guard as a Service (SGAS)" opsJiraProject="SGAS-OPS"
def test_delete_dr_plan_execution(testing_service_client):
    if not testing_service_client.is_api_enabled('disaster_recovery', 'DeleteDrPlanExecution'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('disaster_recovery', util.camelize('disaster_recovery'), 'DeleteDrPlanExecution')
    )

    request_containers = testing_service_client.get_requests(service_name='disaster_recovery', api_name='DeleteDrPlanExecution')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.disaster_recovery.DisasterRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.delete_dr_plan_execution(
                dr_plan_execution_id=request.pop(util.camelize('drPlanExecutionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'disaster_recovery',
            'DeleteDrPlanExecution',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_dr_plan_execution',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="psampath_org_ww@oracle.com" jiraProject="Site Guard as a Service (SGAS)" opsJiraProject="SGAS-OPS"
def test_delete_dr_protection_group(testing_service_client):
    if not testing_service_client.is_api_enabled('disaster_recovery', 'DeleteDrProtectionGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('disaster_recovery', util.camelize('disaster_recovery'), 'DeleteDrProtectionGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='disaster_recovery', api_name='DeleteDrProtectionGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.disaster_recovery.DisasterRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.delete_dr_protection_group(
                dr_protection_group_id=request.pop(util.camelize('drProtectionGroupId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'disaster_recovery',
            'DeleteDrProtectionGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_dr_protection_group',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="psampath_org_ww@oracle.com" jiraProject="Site Guard as a Service (SGAS)" opsJiraProject="SGAS-OPS"
def test_disassociate_dr_protection_group(testing_service_client):
    if not testing_service_client.is_api_enabled('disaster_recovery', 'DisassociateDrProtectionGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('disaster_recovery', util.camelize('disaster_recovery'), 'DisassociateDrProtectionGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='disaster_recovery', api_name='DisassociateDrProtectionGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.disaster_recovery.DisasterRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.disassociate_dr_protection_group(
                disassociate_dr_protection_group_details=request.pop(util.camelize('DisassociateDrProtectionGroupDetails')),
                dr_protection_group_id=request.pop(util.camelize('drProtectionGroupId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'disaster_recovery',
            'DisassociateDrProtectionGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'disassociate_dr_protection_group',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="psampath_org_ww@oracle.com" jiraProject="Site Guard as a Service (SGAS)" opsJiraProject="SGAS-OPS"
def test_get_dr_plan(testing_service_client):
    if not testing_service_client.is_api_enabled('disaster_recovery', 'GetDrPlan'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('disaster_recovery', util.camelize('disaster_recovery'), 'GetDrPlan')
    )

    request_containers = testing_service_client.get_requests(service_name='disaster_recovery', api_name='GetDrPlan')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.disaster_recovery.DisasterRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.get_dr_plan(
                dr_plan_id=request.pop(util.camelize('drPlanId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'disaster_recovery',
            'GetDrPlan',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'drPlan',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="psampath_org_ww@oracle.com" jiraProject="Site Guard as a Service (SGAS)" opsJiraProject="SGAS-OPS"
def test_get_dr_plan_execution(testing_service_client):
    if not testing_service_client.is_api_enabled('disaster_recovery', 'GetDrPlanExecution'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('disaster_recovery', util.camelize('disaster_recovery'), 'GetDrPlanExecution')
    )

    request_containers = testing_service_client.get_requests(service_name='disaster_recovery', api_name='GetDrPlanExecution')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.disaster_recovery.DisasterRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.get_dr_plan_execution(
                dr_plan_execution_id=request.pop(util.camelize('drPlanExecutionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'disaster_recovery',
            'GetDrPlanExecution',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'drPlanExecution',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="psampath_org_ww@oracle.com" jiraProject="Site Guard as a Service (SGAS)" opsJiraProject="SGAS-OPS"
def test_get_dr_protection_group(testing_service_client):
    if not testing_service_client.is_api_enabled('disaster_recovery', 'GetDrProtectionGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('disaster_recovery', util.camelize('disaster_recovery'), 'GetDrProtectionGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='disaster_recovery', api_name='GetDrProtectionGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.disaster_recovery.DisasterRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.get_dr_protection_group(
                dr_protection_group_id=request.pop(util.camelize('drProtectionGroupId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'disaster_recovery',
            'GetDrProtectionGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'drProtectionGroup',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="psampath_org_ww@oracle.com" jiraProject="Site Guard as a Service (SGAS)" opsJiraProject="SGAS-OPS"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('disaster_recovery', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('disaster_recovery', util.camelize('disaster_recovery'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='disaster_recovery', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.disaster_recovery.DisasterRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'disaster_recovery',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="psampath_org_ww@oracle.com" jiraProject="Site Guard as a Service (SGAS)" opsJiraProject="SGAS-OPS"
def test_ignore_dr_plan_execution(testing_service_client):
    if not testing_service_client.is_api_enabled('disaster_recovery', 'IgnoreDrPlanExecution'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('disaster_recovery', util.camelize('disaster_recovery'), 'IgnoreDrPlanExecution')
    )

    request_containers = testing_service_client.get_requests(service_name='disaster_recovery', api_name='IgnoreDrPlanExecution')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.disaster_recovery.DisasterRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.ignore_dr_plan_execution(
                ignore_dr_plan_execution_details=request.pop(util.camelize('IgnoreDrPlanExecutionDetails')),
                dr_plan_execution_id=request.pop(util.camelize('drPlanExecutionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'disaster_recovery',
            'IgnoreDrPlanExecution',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'ignore_dr_plan_execution',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="psampath_org_ww@oracle.com" jiraProject="Site Guard as a Service (SGAS)" opsJiraProject="SGAS-OPS"
def test_list_dr_plan_executions(testing_service_client):
    if not testing_service_client.is_api_enabled('disaster_recovery', 'ListDrPlanExecutions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('disaster_recovery', util.camelize('disaster_recovery'), 'ListDrPlanExecutions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='disaster_recovery', api_name='ListDrPlanExecutions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.disaster_recovery.DisasterRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.list_dr_plan_executions(
                dr_protection_group_id=request.pop(util.camelize('drProtectionGroupId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_dr_plan_executions(
                    dr_protection_group_id=request.pop(util.camelize('drProtectionGroupId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_dr_plan_executions(
                        dr_protection_group_id=request.pop(util.camelize('drProtectionGroupId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'disaster_recovery',
            'ListDrPlanExecutions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'drPlanExecutionCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="psampath_org_ww@oracle.com" jiraProject="Site Guard as a Service (SGAS)" opsJiraProject="SGAS-OPS"
def test_list_dr_plans(testing_service_client):
    if not testing_service_client.is_api_enabled('disaster_recovery', 'ListDrPlans'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('disaster_recovery', util.camelize('disaster_recovery'), 'ListDrPlans')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='disaster_recovery', api_name='ListDrPlans')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.disaster_recovery.DisasterRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.list_dr_plans(
                dr_protection_group_id=request.pop(util.camelize('drProtectionGroupId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_dr_plans(
                    dr_protection_group_id=request.pop(util.camelize('drProtectionGroupId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_dr_plans(
                        dr_protection_group_id=request.pop(util.camelize('drProtectionGroupId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'disaster_recovery',
            'ListDrPlans',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'drPlanCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="psampath_org_ww@oracle.com" jiraProject="Site Guard as a Service (SGAS)" opsJiraProject="SGAS-OPS"
def test_list_dr_protection_groups(testing_service_client):
    if not testing_service_client.is_api_enabled('disaster_recovery', 'ListDrProtectionGroups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('disaster_recovery', util.camelize('disaster_recovery'), 'ListDrProtectionGroups')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='disaster_recovery', api_name='ListDrProtectionGroups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.disaster_recovery.DisasterRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.list_dr_protection_groups(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_dr_protection_groups(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_dr_protection_groups(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'disaster_recovery',
            'ListDrProtectionGroups',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'drProtectionGroupCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="psampath_org_ww@oracle.com" jiraProject="Site Guard as a Service (SGAS)" opsJiraProject="SGAS-OPS"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('disaster_recovery', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('disaster_recovery', util.camelize('disaster_recovery'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='disaster_recovery', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.disaster_recovery.DisasterRecoveryClient(config, service_endpoint=service_endpoint)
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
            'disaster_recovery',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestErrorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="psampath_org_ww@oracle.com" jiraProject="Site Guard as a Service (SGAS)" opsJiraProject="SGAS-OPS"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('disaster_recovery', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('disaster_recovery', util.camelize('disaster_recovery'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='disaster_recovery', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.disaster_recovery.DisasterRecoveryClient(config, service_endpoint=service_endpoint)
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
            'disaster_recovery',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="psampath_org_ww@oracle.com" jiraProject="Site Guard as a Service (SGAS)" opsJiraProject="SGAS-OPS"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('disaster_recovery', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('disaster_recovery', util.camelize('disaster_recovery'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='disaster_recovery', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.disaster_recovery.DisasterRecoveryClient(config, service_endpoint=service_endpoint)
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
            'disaster_recovery',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="psampath_org_ww@oracle.com" jiraProject="Site Guard as a Service (SGAS)" opsJiraProject="SGAS-OPS"
def test_pause_dr_plan_execution(testing_service_client):
    if not testing_service_client.is_api_enabled('disaster_recovery', 'PauseDrPlanExecution'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('disaster_recovery', util.camelize('disaster_recovery'), 'PauseDrPlanExecution')
    )

    request_containers = testing_service_client.get_requests(service_name='disaster_recovery', api_name='PauseDrPlanExecution')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.disaster_recovery.DisasterRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.pause_dr_plan_execution(
                pause_dr_plan_execution_details=request.pop(util.camelize('PauseDrPlanExecutionDetails')),
                dr_plan_execution_id=request.pop(util.camelize('drPlanExecutionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'disaster_recovery',
            'PauseDrPlanExecution',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'pause_dr_plan_execution',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="psampath_org_ww@oracle.com" jiraProject="Site Guard as a Service (SGAS)" opsJiraProject="SGAS-OPS"
def test_resume_dr_plan_execution(testing_service_client):
    if not testing_service_client.is_api_enabled('disaster_recovery', 'ResumeDrPlanExecution'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('disaster_recovery', util.camelize('disaster_recovery'), 'ResumeDrPlanExecution')
    )

    request_containers = testing_service_client.get_requests(service_name='disaster_recovery', api_name='ResumeDrPlanExecution')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.disaster_recovery.DisasterRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.resume_dr_plan_execution(
                resume_dr_plan_execution_details=request.pop(util.camelize('ResumeDrPlanExecutionDetails')),
                dr_plan_execution_id=request.pop(util.camelize('drPlanExecutionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'disaster_recovery',
            'ResumeDrPlanExecution',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'resume_dr_plan_execution',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="psampath_org_ww@oracle.com" jiraProject="Site Guard as a Service (SGAS)" opsJiraProject="SGAS-OPS"
def test_retry_dr_plan_execution(testing_service_client):
    if not testing_service_client.is_api_enabled('disaster_recovery', 'RetryDrPlanExecution'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('disaster_recovery', util.camelize('disaster_recovery'), 'RetryDrPlanExecution')
    )

    request_containers = testing_service_client.get_requests(service_name='disaster_recovery', api_name='RetryDrPlanExecution')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.disaster_recovery.DisasterRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.retry_dr_plan_execution(
                retry_dr_plan_execution_details=request.pop(util.camelize('RetryDrPlanExecutionDetails')),
                dr_plan_execution_id=request.pop(util.camelize('drPlanExecutionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'disaster_recovery',
            'RetryDrPlanExecution',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'retry_dr_plan_execution',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="psampath_org_ww@oracle.com" jiraProject="Site Guard as a Service (SGAS)" opsJiraProject="SGAS-OPS"
def test_update_dr_plan(testing_service_client):
    if not testing_service_client.is_api_enabled('disaster_recovery', 'UpdateDrPlan'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('disaster_recovery', util.camelize('disaster_recovery'), 'UpdateDrPlan')
    )

    request_containers = testing_service_client.get_requests(service_name='disaster_recovery', api_name='UpdateDrPlan')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.disaster_recovery.DisasterRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.update_dr_plan(
                update_dr_plan_details=request.pop(util.camelize('UpdateDrPlanDetails')),
                dr_plan_id=request.pop(util.camelize('drPlanId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'disaster_recovery',
            'UpdateDrPlan',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_dr_plan',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="psampath_org_ww@oracle.com" jiraProject="Site Guard as a Service (SGAS)" opsJiraProject="SGAS-OPS"
def test_update_dr_plan_execution(testing_service_client):
    if not testing_service_client.is_api_enabled('disaster_recovery', 'UpdateDrPlanExecution'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('disaster_recovery', util.camelize('disaster_recovery'), 'UpdateDrPlanExecution')
    )

    request_containers = testing_service_client.get_requests(service_name='disaster_recovery', api_name='UpdateDrPlanExecution')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.disaster_recovery.DisasterRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.update_dr_plan_execution(
                update_dr_plan_execution_details=request.pop(util.camelize('UpdateDrPlanExecutionDetails')),
                dr_plan_execution_id=request.pop(util.camelize('drPlanExecutionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'disaster_recovery',
            'UpdateDrPlanExecution',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_dr_plan_execution',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="psampath_org_ww@oracle.com" jiraProject="Site Guard as a Service (SGAS)" opsJiraProject="SGAS-OPS"
def test_update_dr_protection_group(testing_service_client):
    if not testing_service_client.is_api_enabled('disaster_recovery', 'UpdateDrProtectionGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('disaster_recovery', util.camelize('disaster_recovery'), 'UpdateDrProtectionGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='disaster_recovery', api_name='UpdateDrProtectionGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.disaster_recovery.DisasterRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.update_dr_protection_group(
                update_dr_protection_group_details=request.pop(util.camelize('UpdateDrProtectionGroupDetails')),
                dr_protection_group_id=request.pop(util.camelize('drProtectionGroupId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'disaster_recovery',
            'UpdateDrProtectionGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_dr_protection_group',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="psampath_org_ww@oracle.com" jiraProject="Site Guard as a Service (SGAS)" opsJiraProject="SGAS-OPS"
def test_update_dr_protection_group_role(testing_service_client):
    if not testing_service_client.is_api_enabled('disaster_recovery', 'UpdateDrProtectionGroupRole'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('disaster_recovery', util.camelize('disaster_recovery'), 'UpdateDrProtectionGroupRole')
    )

    request_containers = testing_service_client.get_requests(service_name='disaster_recovery', api_name='UpdateDrProtectionGroupRole')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.disaster_recovery.DisasterRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.update_dr_protection_group_role(
                update_dr_protection_group_role_details=request.pop(util.camelize('UpdateDrProtectionGroupRoleDetails')),
                dr_protection_group_id=request.pop(util.camelize('drProtectionGroupId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'disaster_recovery',
            'UpdateDrProtectionGroupRole',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_dr_protection_group_role',
            False,
            False
        )
