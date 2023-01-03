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

        cassette_location = os.path.join('generated', 'visual_builder_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="vb-oci-dev_grp@oracle.com" jiraProject="VB" opsJiraProject="AVBCS"
def test_change_vb_instance_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('visual_builder', 'ChangeVbInstanceCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('visual_builder', util.camelize('vb_instance'), 'ChangeVbInstanceCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='visual_builder', api_name='ChangeVbInstanceCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.visual_builder.VbInstanceClient(config, service_endpoint=service_endpoint)
            response = client.change_vb_instance_compartment(
                vb_instance_id=request.pop(util.camelize('vbInstanceId')),
                change_vb_instance_compartment_details=request.pop(util.camelize('ChangeVbInstanceCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'visual_builder',
            'ChangeVbInstanceCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_vb_instance_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="vb-oci-dev_grp@oracle.com" jiraProject="VB" opsJiraProject="AVBCS"
def test_create_vb_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('visual_builder', 'CreateVbInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('visual_builder', util.camelize('vb_instance'), 'CreateVbInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='visual_builder', api_name='CreateVbInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.visual_builder.VbInstanceClient(config, service_endpoint=service_endpoint)
            response = client.create_vb_instance(
                create_vb_instance_details=request.pop(util.camelize('CreateVbInstanceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'visual_builder',
            'CreateVbInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_vb_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="vb-oci-dev_grp@oracle.com" jiraProject="VB" opsJiraProject="AVBCS"
def test_delete_vb_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('visual_builder', 'DeleteVbInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('visual_builder', util.camelize('vb_instance'), 'DeleteVbInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='visual_builder', api_name='DeleteVbInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.visual_builder.VbInstanceClient(config, service_endpoint=service_endpoint)
            response = client.delete_vb_instance(
                vb_instance_id=request.pop(util.camelize('vbInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'visual_builder',
            'DeleteVbInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_vb_instance',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="vb-oci-dev_grp@oracle.com" jiraProject="VB" opsJiraProject="AVBCS"
def test_get_vb_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('visual_builder', 'GetVbInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('visual_builder', util.camelize('vb_instance'), 'GetVbInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='visual_builder', api_name='GetVbInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.visual_builder.VbInstanceClient(config, service_endpoint=service_endpoint)
            response = client.get_vb_instance(
                vb_instance_id=request.pop(util.camelize('vbInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'visual_builder',
            'GetVbInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'vbInstance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="vb-oci-dev_grp@oracle.com" jiraProject="VB" opsJiraProject="AVBCS"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('visual_builder', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('visual_builder', util.camelize('vb_instance'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='visual_builder', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.visual_builder.VbInstanceClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'visual_builder',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="vb-oci-dev_grp@oracle.com" jiraProject="VB" opsJiraProject="AVBCS"
def test_list_vb_instances(testing_service_client):
    if not testing_service_client.is_api_enabled('visual_builder', 'ListVbInstances'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('visual_builder', util.camelize('vb_instance'), 'ListVbInstances')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='visual_builder', api_name='ListVbInstances')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.visual_builder.VbInstanceClient(config, service_endpoint=service_endpoint)
            response = client.list_vb_instances(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_vb_instances(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_vb_instances(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'visual_builder',
            'ListVbInstances',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'vbInstanceSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="vb-oci-dev_grp@oracle.com" jiraProject="VB" opsJiraProject="AVBCS"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('visual_builder', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('visual_builder', util.camelize('vb_instance'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='visual_builder', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.visual_builder.VbInstanceClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_errors(
                compartment_id=request.pop(util.camelize('compartmentId')),
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_errors(
                    compartment_id=request.pop(util.camelize('compartmentId')),
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
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'visual_builder',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestErrorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="vb-oci-dev_grp@oracle.com" jiraProject="VB" opsJiraProject="AVBCS"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('visual_builder', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('visual_builder', util.camelize('vb_instance'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='visual_builder', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.visual_builder.VbInstanceClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_logs(
                compartment_id=request.pop(util.camelize('compartmentId')),
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_logs(
                    compartment_id=request.pop(util.camelize('compartmentId')),
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
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'visual_builder',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="vb-oci-dev_grp@oracle.com" jiraProject="VB" opsJiraProject="AVBCS"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('visual_builder', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('visual_builder', util.camelize('vb_instance'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='visual_builder', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.visual_builder.VbInstanceClient(config, service_endpoint=service_endpoint)
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
            'visual_builder',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="vb-oci-dev_grp@oracle.com" jiraProject="VB" opsJiraProject="AVBCS"
def test_request_summarized_applications(testing_service_client):
    if not testing_service_client.is_api_enabled('visual_builder', 'RequestSummarizedApplications'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('visual_builder', util.camelize('vb_instance'), 'RequestSummarizedApplications')
    )

    request_containers = testing_service_client.get_requests(service_name='visual_builder', api_name='RequestSummarizedApplications')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.visual_builder.VbInstanceClient(config, service_endpoint=service_endpoint)
            response = client.request_summarized_applications(
                request_summarized_applications_details=request.pop(util.camelize('RequestSummarizedApplicationsDetails')),
                vb_instance_id=request.pop(util.camelize('vbInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'visual_builder',
            'RequestSummarizedApplications',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'applicationSummaryCollection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="vb-oci-dev_grp@oracle.com" jiraProject="VB" opsJiraProject="AVBCS"
def test_start_vb_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('visual_builder', 'StartVbInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('visual_builder', util.camelize('vb_instance'), 'StartVbInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='visual_builder', api_name='StartVbInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.visual_builder.VbInstanceClient(config, service_endpoint=service_endpoint)
            response = client.start_vb_instance(
                vb_instance_id=request.pop(util.camelize('vbInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'visual_builder',
            'StartVbInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'start_vb_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="vb-oci-dev_grp@oracle.com" jiraProject="VB" opsJiraProject="AVBCS"
def test_stop_vb_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('visual_builder', 'StopVbInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('visual_builder', util.camelize('vb_instance'), 'StopVbInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='visual_builder', api_name='StopVbInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.visual_builder.VbInstanceClient(config, service_endpoint=service_endpoint)
            response = client.stop_vb_instance(
                vb_instance_id=request.pop(util.camelize('vbInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'visual_builder',
            'StopVbInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stop_vb_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="vb-oci-dev_grp@oracle.com" jiraProject="VB" opsJiraProject="AVBCS"
def test_update_vb_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('visual_builder', 'UpdateVbInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('visual_builder', util.camelize('vb_instance'), 'UpdateVbInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='visual_builder', api_name='UpdateVbInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.visual_builder.VbInstanceClient(config, service_endpoint=service_endpoint)
            response = client.update_vb_instance(
                vb_instance_id=request.pop(util.camelize('vbInstanceId')),
                update_vb_instance_details=request.pop(util.camelize('UpdateVbInstanceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'visual_builder',
            'UpdateVbInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_vb_instance',
            False,
            False
        )
