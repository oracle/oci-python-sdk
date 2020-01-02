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
    # use the default matching logic (link below) with the exception of 'session_agnostic_query_matcher'
    # instead of 'query' matcher (which ignores sessionId in the url)
    # https://vcrpy.readthedocs.io/en/latest/configuration.html#request-matching
    custom_vcr = test_config_container.create_vcr()
    custom_vcr.register_matcher('session_agnostic_query_matcher', session_agnostic_query_matcher)

    cassette_location = os.path.join('generated', 'resource_manager_{name}.yml'.format(name=request.function.__name__))
    with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
        yield


# IssueRoutingInfo tag="default" email="team_oci_orm_us_grp@oracle.com" jiraProject="ORCH" opsJiraProject="OS"
def test_cancel_job(testing_service_client):
    if not testing_service_client.is_api_enabled('resource_manager', 'CancelJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('resource_manager', util.camelize('resource_manager'), 'CancelJob')
    )

    request_containers = testing_service_client.get_requests(service_name='resource_manager', api_name='CancelJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.resource_manager.ResourceManagerClient(config, service_endpoint=service_endpoint)
            response = client.cancel_job(
                job_id=request.pop(util.camelize('job_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'resource_manager',
            'CancelJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cancel_job',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_orm_us_grp@oracle.com" jiraProject="ORCH" opsJiraProject="OS"
def test_change_stack_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('resource_manager', 'ChangeStackCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('resource_manager', util.camelize('resource_manager'), 'ChangeStackCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='resource_manager', api_name='ChangeStackCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.resource_manager.ResourceManagerClient(config, service_endpoint=service_endpoint)
            response = client.change_stack_compartment(
                stack_id=request.pop(util.camelize('stack_id')),
                change_stack_compartment_details=request.pop(util.camelize('change_stack_compartment_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'resource_manager',
            'ChangeStackCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_stack_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_orm_us_grp@oracle.com" jiraProject="ORCH" opsJiraProject="OS"
def test_create_job(testing_service_client):
    if not testing_service_client.is_api_enabled('resource_manager', 'CreateJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('resource_manager', util.camelize('resource_manager'), 'CreateJob')
    )

    request_containers = testing_service_client.get_requests(service_name='resource_manager', api_name='CreateJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.resource_manager.ResourceManagerClient(config, service_endpoint=service_endpoint)
            response = client.create_job(
                create_job_details=request.pop(util.camelize('create_job_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'resource_manager',
            'CreateJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'job',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_orm_us_grp@oracle.com" jiraProject="ORCH" opsJiraProject="OS"
def test_create_stack(testing_service_client):
    if not testing_service_client.is_api_enabled('resource_manager', 'CreateStack'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('resource_manager', util.camelize('resource_manager'), 'CreateStack')
    )

    request_containers = testing_service_client.get_requests(service_name='resource_manager', api_name='CreateStack')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.resource_manager.ResourceManagerClient(config, service_endpoint=service_endpoint)
            response = client.create_stack(
                create_stack_details=request.pop(util.camelize('create_stack_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'resource_manager',
            'CreateStack',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stack',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_orm_us_grp@oracle.com" jiraProject="ORCH" opsJiraProject="OS"
def test_delete_stack(testing_service_client):
    if not testing_service_client.is_api_enabled('resource_manager', 'DeleteStack'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('resource_manager', util.camelize('resource_manager'), 'DeleteStack')
    )

    request_containers = testing_service_client.get_requests(service_name='resource_manager', api_name='DeleteStack')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.resource_manager.ResourceManagerClient(config, service_endpoint=service_endpoint)
            response = client.delete_stack(
                stack_id=request.pop(util.camelize('stack_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'resource_manager',
            'DeleteStack',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_stack',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_orm_us_grp@oracle.com" jiraProject="ORCH" opsJiraProject="OS"
def test_get_job(testing_service_client):
    if not testing_service_client.is_api_enabled('resource_manager', 'GetJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('resource_manager', util.camelize('resource_manager'), 'GetJob')
    )

    request_containers = testing_service_client.get_requests(service_name='resource_manager', api_name='GetJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.resource_manager.ResourceManagerClient(config, service_endpoint=service_endpoint)
            response = client.get_job(
                job_id=request.pop(util.camelize('job_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'resource_manager',
            'GetJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'job',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_orm_us_grp@oracle.com" jiraProject="ORCH" opsJiraProject="OS"
def test_get_job_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('resource_manager', 'GetJobLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('resource_manager', util.camelize('resource_manager'), 'GetJobLogs')
    )

    request_containers = testing_service_client.get_requests(service_name='resource_manager', api_name='GetJobLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.resource_manager.ResourceManagerClient(config, service_endpoint=service_endpoint)
            response = client.get_job_logs(
                job_id=request.pop(util.camelize('job_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.get_job_logs(
                    job_id=request.pop(util.camelize('job_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.get_job_logs(
                        job_id=request.pop(util.camelize('job_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'resource_manager',
            'GetJobLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logEntry',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_orm_us_grp@oracle.com" jiraProject="ORCH" opsJiraProject="OS"
def test_get_job_logs_content(testing_service_client):
    if not testing_service_client.is_api_enabled('resource_manager', 'GetJobLogsContent'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('resource_manager', util.camelize('resource_manager'), 'GetJobLogsContent')
    )

    request_containers = testing_service_client.get_requests(service_name='resource_manager', api_name='GetJobLogsContent')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.resource_manager.ResourceManagerClient(config, service_endpoint=service_endpoint)
            response = client.get_job_logs_content(
                job_id=request.pop(util.camelize('job_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'resource_manager',
            'GetJobLogsContent',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'str',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_orm_us_grp@oracle.com" jiraProject="ORCH" opsJiraProject="OS"
def test_get_job_tf_config(testing_service_client):
    if not testing_service_client.is_api_enabled('resource_manager', 'GetJobTfConfig'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('resource_manager', util.camelize('resource_manager'), 'GetJobTfConfig')
    )

    request_containers = testing_service_client.get_requests(service_name='resource_manager', api_name='GetJobTfConfig')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.resource_manager.ResourceManagerClient(config, service_endpoint=service_endpoint)
            response = client.get_job_tf_config(
                job_id=request.pop(util.camelize('job_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'resource_manager',
            'GetJobTfConfig',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_orm_us_grp@oracle.com" jiraProject="ORCH" opsJiraProject="OS"
def test_get_job_tf_state(testing_service_client):
    if not testing_service_client.is_api_enabled('resource_manager', 'GetJobTfState'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('resource_manager', util.camelize('resource_manager'), 'GetJobTfState')
    )

    request_containers = testing_service_client.get_requests(service_name='resource_manager', api_name='GetJobTfState')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.resource_manager.ResourceManagerClient(config, service_endpoint=service_endpoint)
            response = client.get_job_tf_state(
                job_id=request.pop(util.camelize('job_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'resource_manager',
            'GetJobTfState',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_orm_us_grp@oracle.com" jiraProject="ORCH" opsJiraProject="OS"
def test_get_stack(testing_service_client):
    if not testing_service_client.is_api_enabled('resource_manager', 'GetStack'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('resource_manager', util.camelize('resource_manager'), 'GetStack')
    )

    request_containers = testing_service_client.get_requests(service_name='resource_manager', api_name='GetStack')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.resource_manager.ResourceManagerClient(config, service_endpoint=service_endpoint)
            response = client.get_stack(
                stack_id=request.pop(util.camelize('stack_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'resource_manager',
            'GetStack',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stack',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_orm_us_grp@oracle.com" jiraProject="ORCH" opsJiraProject="OS"
def test_get_stack_tf_config(testing_service_client):
    if not testing_service_client.is_api_enabled('resource_manager', 'GetStackTfConfig'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('resource_manager', util.camelize('resource_manager'), 'GetStackTfConfig')
    )

    request_containers = testing_service_client.get_requests(service_name='resource_manager', api_name='GetStackTfConfig')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.resource_manager.ResourceManagerClient(config, service_endpoint=service_endpoint)
            response = client.get_stack_tf_config(
                stack_id=request.pop(util.camelize('stack_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'resource_manager',
            'GetStackTfConfig',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_orm_us_grp@oracle.com" jiraProject="ORCH" opsJiraProject="OS"
def test_get_stack_tf_state(testing_service_client):
    if not testing_service_client.is_api_enabled('resource_manager', 'GetStackTfState'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('resource_manager', util.camelize('resource_manager'), 'GetStackTfState')
    )

    request_containers = testing_service_client.get_requests(service_name='resource_manager', api_name='GetStackTfState')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.resource_manager.ResourceManagerClient(config, service_endpoint=service_endpoint)
            response = client.get_stack_tf_state(
                stack_id=request.pop(util.camelize('stack_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'resource_manager',
            'GetStackTfState',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_orm_us_grp@oracle.com" jiraProject="ORCH" opsJiraProject="OS"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('resource_manager', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('resource_manager', util.camelize('resource_manager'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='resource_manager', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.resource_manager.ResourceManagerClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('work_request_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'resource_manager',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_orm_us_grp@oracle.com" jiraProject="ORCH" opsJiraProject="OS"
def test_list_jobs(testing_service_client):
    if not testing_service_client.is_api_enabled('resource_manager', 'ListJobs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('resource_manager', util.camelize('resource_manager'), 'ListJobs')
    )

    request_containers = testing_service_client.get_requests(service_name='resource_manager', api_name='ListJobs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.resource_manager.ResourceManagerClient(config, service_endpoint=service_endpoint)
            response = client.list_jobs(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_jobs(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_jobs(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'resource_manager',
            'ListJobs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'jobSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_orm_us_grp@oracle.com" jiraProject="ORCH" opsJiraProject="OS"
def test_list_stacks(testing_service_client):
    if not testing_service_client.is_api_enabled('resource_manager', 'ListStacks'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('resource_manager', util.camelize('resource_manager'), 'ListStacks')
    )

    request_containers = testing_service_client.get_requests(service_name='resource_manager', api_name='ListStacks')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.resource_manager.ResourceManagerClient(config, service_endpoint=service_endpoint)
            response = client.list_stacks(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_stacks(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_stacks(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'resource_manager',
            'ListStacks',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stackSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_orm_us_grp@oracle.com" jiraProject="ORCH" opsJiraProject="OS"
def test_list_terraform_versions(testing_service_client):
    if not testing_service_client.is_api_enabled('resource_manager', 'ListTerraformVersions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('resource_manager', util.camelize('resource_manager'), 'ListTerraformVersions')
    )

    request_containers = testing_service_client.get_requests(service_name='resource_manager', api_name='ListTerraformVersions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.resource_manager.ResourceManagerClient(config, service_endpoint=service_endpoint)
            response = client.list_terraform_versions(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'resource_manager',
            'ListTerraformVersions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'terraformVersionCollection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_orm_us_grp@oracle.com" jiraProject="ORCH" opsJiraProject="OS"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('resource_manager', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('resource_manager', util.camelize('resource_manager'), 'ListWorkRequestErrors')
    )

    request_containers = testing_service_client.get_requests(service_name='resource_manager', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.resource_manager.ResourceManagerClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_errors(
                work_request_id=request.pop(util.camelize('work_request_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_errors(
                    work_request_id=request.pop(util.camelize('work_request_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_request_errors(
                        work_request_id=request.pop(util.camelize('work_request_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'resource_manager',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestError',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_orm_us_grp@oracle.com" jiraProject="ORCH" opsJiraProject="OS"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('resource_manager', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('resource_manager', util.camelize('resource_manager'), 'ListWorkRequestLogs')
    )

    request_containers = testing_service_client.get_requests(service_name='resource_manager', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.resource_manager.ResourceManagerClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_logs(
                work_request_id=request.pop(util.camelize('work_request_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_logs(
                    work_request_id=request.pop(util.camelize('work_request_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_request_logs(
                        work_request_id=request.pop(util.camelize('work_request_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'resource_manager',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntry',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_orm_us_grp@oracle.com" jiraProject="ORCH" opsJiraProject="OS"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('resource_manager', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('resource_manager', util.camelize('resource_manager'), 'ListWorkRequests')
    )

    request_containers = testing_service_client.get_requests(service_name='resource_manager', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.resource_manager.ResourceManagerClient(config, service_endpoint=service_endpoint)
            response = client.list_work_requests(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_requests(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_requests(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'resource_manager',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_orm_us_grp@oracle.com" jiraProject="ORCH" opsJiraProject="OS"
def test_update_job(testing_service_client):
    if not testing_service_client.is_api_enabled('resource_manager', 'UpdateJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('resource_manager', util.camelize('resource_manager'), 'UpdateJob')
    )

    request_containers = testing_service_client.get_requests(service_name='resource_manager', api_name='UpdateJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.resource_manager.ResourceManagerClient(config, service_endpoint=service_endpoint)
            response = client.update_job(
                job_id=request.pop(util.camelize('job_id')),
                update_job_details=request.pop(util.camelize('update_job_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'resource_manager',
            'UpdateJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'job',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_orm_us_grp@oracle.com" jiraProject="ORCH" opsJiraProject="OS"
def test_update_stack(testing_service_client):
    if not testing_service_client.is_api_enabled('resource_manager', 'UpdateStack'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('resource_manager', util.camelize('resource_manager'), 'UpdateStack')
    )

    request_containers = testing_service_client.get_requests(service_name='resource_manager', api_name='UpdateStack')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.resource_manager.ResourceManagerClient(config, service_endpoint=service_endpoint)
            response = client.update_stack(
                stack_id=request.pop(util.camelize('stack_id')),
                update_stack_details=request.pop(util.camelize('update_stack_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'resource_manager',
            'UpdateStack',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stack',
            False,
            False
        )
