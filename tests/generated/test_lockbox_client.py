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

        cassette_location = os.path.join('generated', 'lockbox_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="team_oci_lockbox_us_grp@oracle.com" jiraProject="LOCKBOX" opsJiraProject="OMA"
def test_cancel_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('lockbox', 'CancelWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('lockbox', util.camelize('lockbox'), 'CancelWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='lockbox', api_name='CancelWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.lockbox.LockboxClient(config, service_endpoint=service_endpoint)
            response = client.cancel_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'lockbox',
            'CancelWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cancel_work_request',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_lockbox_us_grp@oracle.com" jiraProject="LOCKBOX" opsJiraProject="OMA"
def test_change_approval_template_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('lockbox', 'ChangeApprovalTemplateCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('lockbox', util.camelize('lockbox'), 'ChangeApprovalTemplateCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='lockbox', api_name='ChangeApprovalTemplateCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.lockbox.LockboxClient(config, service_endpoint=service_endpoint)
            response = client.change_approval_template_compartment(
                approval_template_id=request.pop(util.camelize('approvalTemplateId')),
                change_approval_template_compartment_details=request.pop(util.camelize('ChangeApprovalTemplateCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'lockbox',
            'ChangeApprovalTemplateCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_approval_template_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_lockbox_us_grp@oracle.com" jiraProject="LOCKBOX" opsJiraProject="OMA"
def test_change_lockbox_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('lockbox', 'ChangeLockboxCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('lockbox', util.camelize('lockbox'), 'ChangeLockboxCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='lockbox', api_name='ChangeLockboxCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.lockbox.LockboxClient(config, service_endpoint=service_endpoint)
            response = client.change_lockbox_compartment(
                lockbox_id=request.pop(util.camelize('lockboxId')),
                change_lockbox_compartment_details=request.pop(util.camelize('ChangeLockboxCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'lockbox',
            'ChangeLockboxCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_lockbox_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_lockbox_us_grp@oracle.com" jiraProject="LOCKBOX" opsJiraProject="OMA"
def test_create_access_request(testing_service_client):
    if not testing_service_client.is_api_enabled('lockbox', 'CreateAccessRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('lockbox', util.camelize('lockbox'), 'CreateAccessRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='lockbox', api_name='CreateAccessRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.lockbox.LockboxClient(config, service_endpoint=service_endpoint)
            response = client.create_access_request(
                create_access_request_details=request.pop(util.camelize('CreateAccessRequestDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'lockbox',
            'CreateAccessRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'accessRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_lockbox_us_grp@oracle.com" jiraProject="LOCKBOX" opsJiraProject="OMA"
def test_create_approval_template(testing_service_client):
    if not testing_service_client.is_api_enabled('lockbox', 'CreateApprovalTemplate'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('lockbox', util.camelize('lockbox'), 'CreateApprovalTemplate')
    )

    request_containers = testing_service_client.get_requests(service_name='lockbox', api_name='CreateApprovalTemplate')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.lockbox.LockboxClient(config, service_endpoint=service_endpoint)
            response = client.create_approval_template(
                create_approval_template_details=request.pop(util.camelize('CreateApprovalTemplateDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'lockbox',
            'CreateApprovalTemplate',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'approvalTemplate',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_lockbox_us_grp@oracle.com" jiraProject="LOCKBOX" opsJiraProject="OMA"
def test_create_lockbox(testing_service_client):
    if not testing_service_client.is_api_enabled('lockbox', 'CreateLockbox'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('lockbox', util.camelize('lockbox'), 'CreateLockbox')
    )

    request_containers = testing_service_client.get_requests(service_name='lockbox', api_name='CreateLockbox')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.lockbox.LockboxClient(config, service_endpoint=service_endpoint)
            response = client.create_lockbox(
                create_lockbox_details=request.pop(util.camelize('CreateLockboxDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'lockbox',
            'CreateLockbox',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'lockbox',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_lockbox_us_grp@oracle.com" jiraProject="LOCKBOX" opsJiraProject="OMA"
def test_delete_approval_template(testing_service_client):
    if not testing_service_client.is_api_enabled('lockbox', 'DeleteApprovalTemplate'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('lockbox', util.camelize('lockbox'), 'DeleteApprovalTemplate')
    )

    request_containers = testing_service_client.get_requests(service_name='lockbox', api_name='DeleteApprovalTemplate')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.lockbox.LockboxClient(config, service_endpoint=service_endpoint)
            response = client.delete_approval_template(
                approval_template_id=request.pop(util.camelize('approvalTemplateId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'lockbox',
            'DeleteApprovalTemplate',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_approval_template',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_lockbox_us_grp@oracle.com" jiraProject="LOCKBOX" opsJiraProject="OMA"
def test_delete_lockbox(testing_service_client):
    if not testing_service_client.is_api_enabled('lockbox', 'DeleteLockbox'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('lockbox', util.camelize('lockbox'), 'DeleteLockbox')
    )

    request_containers = testing_service_client.get_requests(service_name='lockbox', api_name='DeleteLockbox')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.lockbox.LockboxClient(config, service_endpoint=service_endpoint)
            response = client.delete_lockbox(
                lockbox_id=request.pop(util.camelize('lockboxId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'lockbox',
            'DeleteLockbox',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_lockbox',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_lockbox_us_grp@oracle.com" jiraProject="LOCKBOX" opsJiraProject="OMA"
def test_get_access_materials(testing_service_client):
    if not testing_service_client.is_api_enabled('lockbox', 'GetAccessMaterials'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('lockbox', util.camelize('lockbox'), 'GetAccessMaterials')
    )

    request_containers = testing_service_client.get_requests(service_name='lockbox', api_name='GetAccessMaterials')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.lockbox.LockboxClient(config, service_endpoint=service_endpoint)
            response = client.get_access_materials(
                access_request_id=request.pop(util.camelize('accessRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'lockbox',
            'GetAccessMaterials',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'accessMaterials',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_lockbox_us_grp@oracle.com" jiraProject="LOCKBOX" opsJiraProject="OMA"
def test_get_access_request(testing_service_client):
    if not testing_service_client.is_api_enabled('lockbox', 'GetAccessRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('lockbox', util.camelize('lockbox'), 'GetAccessRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='lockbox', api_name='GetAccessRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.lockbox.LockboxClient(config, service_endpoint=service_endpoint)
            response = client.get_access_request(
                access_request_id=request.pop(util.camelize('accessRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'lockbox',
            'GetAccessRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'accessRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_lockbox_us_grp@oracle.com" jiraProject="LOCKBOX" opsJiraProject="OMA"
def test_get_approval_template(testing_service_client):
    if not testing_service_client.is_api_enabled('lockbox', 'GetApprovalTemplate'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('lockbox', util.camelize('lockbox'), 'GetApprovalTemplate')
    )

    request_containers = testing_service_client.get_requests(service_name='lockbox', api_name='GetApprovalTemplate')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.lockbox.LockboxClient(config, service_endpoint=service_endpoint)
            response = client.get_approval_template(
                approval_template_id=request.pop(util.camelize('approvalTemplateId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'lockbox',
            'GetApprovalTemplate',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'approvalTemplate',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_lockbox_us_grp@oracle.com" jiraProject="LOCKBOX" opsJiraProject="OMA"
def test_get_lockbox(testing_service_client):
    if not testing_service_client.is_api_enabled('lockbox', 'GetLockbox'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('lockbox', util.camelize('lockbox'), 'GetLockbox')
    )

    request_containers = testing_service_client.get_requests(service_name='lockbox', api_name='GetLockbox')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.lockbox.LockboxClient(config, service_endpoint=service_endpoint)
            response = client.get_lockbox(
                lockbox_id=request.pop(util.camelize('lockboxId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'lockbox',
            'GetLockbox',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'lockbox',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_lockbox_us_grp@oracle.com" jiraProject="LOCKBOX" opsJiraProject="OMA"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('lockbox', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('lockbox', util.camelize('lockbox'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='lockbox', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.lockbox.LockboxClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'lockbox',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_lockbox_us_grp@oracle.com" jiraProject="LOCKBOX" opsJiraProject="OMA"
def test_handle_access_request(testing_service_client):
    if not testing_service_client.is_api_enabled('lockbox', 'HandleAccessRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('lockbox', util.camelize('lockbox'), 'HandleAccessRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='lockbox', api_name='HandleAccessRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.lockbox.LockboxClient(config, service_endpoint=service_endpoint)
            response = client.handle_access_request(
                access_request_id=request.pop(util.camelize('accessRequestId')),
                handle_access_request_details=request.pop(util.camelize('HandleAccessRequestDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'lockbox',
            'HandleAccessRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'handle_access_request',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_lockbox_us_grp@oracle.com" jiraProject="LOCKBOX" opsJiraProject="OMA"
def test_list_access_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('lockbox', 'ListAccessRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('lockbox', util.camelize('lockbox'), 'ListAccessRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='lockbox', api_name='ListAccessRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.lockbox.LockboxClient(config, service_endpoint=service_endpoint)
            response = client.list_access_requests(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_access_requests(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_access_requests(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'lockbox',
            'ListAccessRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'accessRequestCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_lockbox_us_grp@oracle.com" jiraProject="LOCKBOX" opsJiraProject="OMA"
def test_list_approval_templates(testing_service_client):
    if not testing_service_client.is_api_enabled('lockbox', 'ListApprovalTemplates'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('lockbox', util.camelize('lockbox'), 'ListApprovalTemplates')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='lockbox', api_name='ListApprovalTemplates')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.lockbox.LockboxClient(config, service_endpoint=service_endpoint)
            response = client.list_approval_templates(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_approval_templates(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_approval_templates(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'lockbox',
            'ListApprovalTemplates',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'approvalTemplateCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_lockbox_us_grp@oracle.com" jiraProject="LOCKBOX" opsJiraProject="OMA"
def test_list_lockboxes(testing_service_client):
    if not testing_service_client.is_api_enabled('lockbox', 'ListLockboxes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('lockbox', util.camelize('lockbox'), 'ListLockboxes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='lockbox', api_name='ListLockboxes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.lockbox.LockboxClient(config, service_endpoint=service_endpoint)
            response = client.list_lockboxes(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_lockboxes(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_lockboxes(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'lockbox',
            'ListLockboxes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'lockboxCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_lockbox_us_grp@oracle.com" jiraProject="LOCKBOX" opsJiraProject="OMA"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('lockbox', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('lockbox', util.camelize('lockbox'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='lockbox', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.lockbox.LockboxClient(config, service_endpoint=service_endpoint)
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
            'lockbox',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestErrorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_lockbox_us_grp@oracle.com" jiraProject="LOCKBOX" opsJiraProject="OMA"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('lockbox', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('lockbox', util.camelize('lockbox'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='lockbox', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.lockbox.LockboxClient(config, service_endpoint=service_endpoint)
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
            'lockbox',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_lockbox_us_grp@oracle.com" jiraProject="LOCKBOX" opsJiraProject="OMA"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('lockbox', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('lockbox', util.camelize('lockbox'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='lockbox', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.lockbox.LockboxClient(config, service_endpoint=service_endpoint)
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
            'lockbox',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_lockbox_us_grp@oracle.com" jiraProject="LOCKBOX" opsJiraProject="OMA"
def test_update_approval_template(testing_service_client):
    if not testing_service_client.is_api_enabled('lockbox', 'UpdateApprovalTemplate'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('lockbox', util.camelize('lockbox'), 'UpdateApprovalTemplate')
    )

    request_containers = testing_service_client.get_requests(service_name='lockbox', api_name='UpdateApprovalTemplate')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.lockbox.LockboxClient(config, service_endpoint=service_endpoint)
            response = client.update_approval_template(
                approval_template_id=request.pop(util.camelize('approvalTemplateId')),
                update_approval_template_details=request.pop(util.camelize('UpdateApprovalTemplateDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'lockbox',
            'UpdateApprovalTemplate',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'approvalTemplate',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_lockbox_us_grp@oracle.com" jiraProject="LOCKBOX" opsJiraProject="OMA"
def test_update_lockbox(testing_service_client):
    if not testing_service_client.is_api_enabled('lockbox', 'UpdateLockbox'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('lockbox', util.camelize('lockbox'), 'UpdateLockbox')
    )

    request_containers = testing_service_client.get_requests(service_name='lockbox', api_name='UpdateLockbox')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.lockbox.LockboxClient(config, service_endpoint=service_endpoint)
            response = client.update_lockbox(
                lockbox_id=request.pop(util.camelize('lockboxId')),
                update_lockbox_details=request.pop(util.camelize('UpdateLockboxDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'lockbox',
            'UpdateLockbox',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'lockbox',
            False,
            False
        )
