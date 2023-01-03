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

        cassette_location = os.path.join('generated', 'stack_monitoring_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="inframondev_us_grp@oracle.com" jiraProject="APPMGMT" opsJiraProject="APPMGMT"
def test_associate_monitored_resources(testing_service_client):
    if not testing_service_client.is_api_enabled('stack_monitoring', 'AssociateMonitoredResources'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('stack_monitoring', util.camelize('stack_monitoring'), 'AssociateMonitoredResources')
    )

    request_containers = testing_service_client.get_requests(service_name='stack_monitoring', api_name='AssociateMonitoredResources')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.stack_monitoring.StackMonitoringClient(config, service_endpoint=service_endpoint)
            response = client.associate_monitored_resources(
                associate_monitored_resources_details=request.pop(util.camelize('AssociateMonitoredResourcesDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'stack_monitoring',
            'AssociateMonitoredResources',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'monitoredResourceAssociation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="inframondev_us_grp@oracle.com" jiraProject="APPMGMT" opsJiraProject="APPMGMT"
def test_change_monitored_resource_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('stack_monitoring', 'ChangeMonitoredResourceCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('stack_monitoring', util.camelize('stack_monitoring'), 'ChangeMonitoredResourceCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='stack_monitoring', api_name='ChangeMonitoredResourceCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.stack_monitoring.StackMonitoringClient(config, service_endpoint=service_endpoint)
            response = client.change_monitored_resource_compartment(
                monitored_resource_id=request.pop(util.camelize('monitoredResourceId')),
                change_monitored_resource_compartment_details=request.pop(util.camelize('ChangeMonitoredResourceCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'stack_monitoring',
            'ChangeMonitoredResourceCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_monitored_resource_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="inframondev_us_grp@oracle.com" jiraProject="APPMGMT" opsJiraProject="APPMGMT"
def test_create_discovery_job(testing_service_client):
    if not testing_service_client.is_api_enabled('stack_monitoring', 'CreateDiscoveryJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('stack_monitoring', util.camelize('stack_monitoring'), 'CreateDiscoveryJob')
    )

    request_containers = testing_service_client.get_requests(service_name='stack_monitoring', api_name='CreateDiscoveryJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.stack_monitoring.StackMonitoringClient(config, service_endpoint=service_endpoint)
            response = client.create_discovery_job(
                create_discovery_job_details=request.pop(util.camelize('CreateDiscoveryJobDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'stack_monitoring',
            'CreateDiscoveryJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'discoveryJob',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="inframondev_us_grp@oracle.com" jiraProject="APPMGMT" opsJiraProject="APPMGMT"
def test_create_monitored_resource(testing_service_client):
    if not testing_service_client.is_api_enabled('stack_monitoring', 'CreateMonitoredResource'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('stack_monitoring', util.camelize('stack_monitoring'), 'CreateMonitoredResource')
    )

    request_containers = testing_service_client.get_requests(service_name='stack_monitoring', api_name='CreateMonitoredResource')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.stack_monitoring.StackMonitoringClient(config, service_endpoint=service_endpoint)
            response = client.create_monitored_resource(
                create_monitored_resource_details=request.pop(util.camelize('CreateMonitoredResourceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'stack_monitoring',
            'CreateMonitoredResource',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'monitoredResource',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="inframondev_us_grp@oracle.com" jiraProject="APPMGMT" opsJiraProject="APPMGMT"
def test_delete_discovery_job(testing_service_client):
    if not testing_service_client.is_api_enabled('stack_monitoring', 'DeleteDiscoveryJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('stack_monitoring', util.camelize('stack_monitoring'), 'DeleteDiscoveryJob')
    )

    request_containers = testing_service_client.get_requests(service_name='stack_monitoring', api_name='DeleteDiscoveryJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.stack_monitoring.StackMonitoringClient(config, service_endpoint=service_endpoint)
            response = client.delete_discovery_job(
                discovery_job_id=request.pop(util.camelize('discoveryJobId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'stack_monitoring',
            'DeleteDiscoveryJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_discovery_job',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="inframondev_us_grp@oracle.com" jiraProject="APPMGMT" opsJiraProject="APPMGMT"
def test_delete_monitored_resource(testing_service_client):
    if not testing_service_client.is_api_enabled('stack_monitoring', 'DeleteMonitoredResource'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('stack_monitoring', util.camelize('stack_monitoring'), 'DeleteMonitoredResource')
    )

    request_containers = testing_service_client.get_requests(service_name='stack_monitoring', api_name='DeleteMonitoredResource')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.stack_monitoring.StackMonitoringClient(config, service_endpoint=service_endpoint)
            response = client.delete_monitored_resource(
                monitored_resource_id=request.pop(util.camelize('monitoredResourceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'stack_monitoring',
            'DeleteMonitoredResource',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_monitored_resource',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="inframondev_us_grp@oracle.com" jiraProject="APPMGMT" opsJiraProject="APPMGMT"
def test_disable_external_database(testing_service_client):
    if not testing_service_client.is_api_enabled('stack_monitoring', 'DisableExternalDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('stack_monitoring', util.camelize('stack_monitoring'), 'DisableExternalDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='stack_monitoring', api_name='DisableExternalDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.stack_monitoring.StackMonitoringClient(config, service_endpoint=service_endpoint)
            response = client.disable_external_database(
                monitored_resource_id=request.pop(util.camelize('monitoredResourceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'stack_monitoring',
            'DisableExternalDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'disable_external_database',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="inframondev_us_grp@oracle.com" jiraProject="APPMGMT" opsJiraProject="APPMGMT"
def test_disassociate_monitored_resources(testing_service_client):
    if not testing_service_client.is_api_enabled('stack_monitoring', 'DisassociateMonitoredResources'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('stack_monitoring', util.camelize('stack_monitoring'), 'DisassociateMonitoredResources')
    )

    request_containers = testing_service_client.get_requests(service_name='stack_monitoring', api_name='DisassociateMonitoredResources')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.stack_monitoring.StackMonitoringClient(config, service_endpoint=service_endpoint)
            response = client.disassociate_monitored_resources(
                disassociate_monitored_resources_details=request.pop(util.camelize('DisassociateMonitoredResourcesDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'stack_monitoring',
            'DisassociateMonitoredResources',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'disassociate_monitored_resources',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="inframondev_us_grp@oracle.com" jiraProject="APPMGMT" opsJiraProject="APPMGMT"
def test_get_discovery_job(testing_service_client):
    if not testing_service_client.is_api_enabled('stack_monitoring', 'GetDiscoveryJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('stack_monitoring', util.camelize('stack_monitoring'), 'GetDiscoveryJob')
    )

    request_containers = testing_service_client.get_requests(service_name='stack_monitoring', api_name='GetDiscoveryJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.stack_monitoring.StackMonitoringClient(config, service_endpoint=service_endpoint)
            response = client.get_discovery_job(
                discovery_job_id=request.pop(util.camelize('discoveryJobId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'stack_monitoring',
            'GetDiscoveryJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'discoveryJob',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="inframondev_us_grp@oracle.com" jiraProject="APPMGMT" opsJiraProject="APPMGMT"
def test_get_monitored_resource(testing_service_client):
    if not testing_service_client.is_api_enabled('stack_monitoring', 'GetMonitoredResource'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('stack_monitoring', util.camelize('stack_monitoring'), 'GetMonitoredResource')
    )

    request_containers = testing_service_client.get_requests(service_name='stack_monitoring', api_name='GetMonitoredResource')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.stack_monitoring.StackMonitoringClient(config, service_endpoint=service_endpoint)
            response = client.get_monitored_resource(
                monitored_resource_id=request.pop(util.camelize('monitoredResourceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'stack_monitoring',
            'GetMonitoredResource',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'monitoredResource',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="inframondev_us_grp@oracle.com" jiraProject="APPMGMT" opsJiraProject="APPMGMT"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('stack_monitoring', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('stack_monitoring', util.camelize('stack_monitoring'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='stack_monitoring', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.stack_monitoring.StackMonitoringClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'stack_monitoring',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="inframondev_us_grp@oracle.com" jiraProject="APPMGMT" opsJiraProject="APPMGMT"
def test_list_discovery_job_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('stack_monitoring', 'ListDiscoveryJobLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('stack_monitoring', util.camelize('stack_monitoring'), 'ListDiscoveryJobLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='stack_monitoring', api_name='ListDiscoveryJobLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.stack_monitoring.StackMonitoringClient(config, service_endpoint=service_endpoint)
            response = client.list_discovery_job_logs(
                discovery_job_id=request.pop(util.camelize('discoveryJobId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_discovery_job_logs(
                    discovery_job_id=request.pop(util.camelize('discoveryJobId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_discovery_job_logs(
                        discovery_job_id=request.pop(util.camelize('discoveryJobId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'stack_monitoring',
            'ListDiscoveryJobLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'discoveryJobLogCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="inframondev_us_grp@oracle.com" jiraProject="APPMGMT" opsJiraProject="APPMGMT"
def test_list_discovery_jobs(testing_service_client):
    if not testing_service_client.is_api_enabled('stack_monitoring', 'ListDiscoveryJobs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('stack_monitoring', util.camelize('stack_monitoring'), 'ListDiscoveryJobs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='stack_monitoring', api_name='ListDiscoveryJobs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.stack_monitoring.StackMonitoringClient(config, service_endpoint=service_endpoint)
            response = client.list_discovery_jobs(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_discovery_jobs(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_discovery_jobs(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'stack_monitoring',
            'ListDiscoveryJobs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'discoveryJobCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="inframondev_us_grp@oracle.com" jiraProject="APPMGMT" opsJiraProject="APPMGMT"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('stack_monitoring', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('stack_monitoring', util.camelize('stack_monitoring'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='stack_monitoring', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.stack_monitoring.StackMonitoringClient(config, service_endpoint=service_endpoint)
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
            'stack_monitoring',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestErrorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="inframondev_us_grp@oracle.com" jiraProject="APPMGMT" opsJiraProject="APPMGMT"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('stack_monitoring', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('stack_monitoring', util.camelize('stack_monitoring'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='stack_monitoring', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.stack_monitoring.StackMonitoringClient(config, service_endpoint=service_endpoint)
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
            'stack_monitoring',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="inframondev_us_grp@oracle.com" jiraProject="APPMGMT" opsJiraProject="APPMGMT"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('stack_monitoring', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('stack_monitoring', util.camelize('stack_monitoring'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='stack_monitoring', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.stack_monitoring.StackMonitoringClient(config, service_endpoint=service_endpoint)
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
            'stack_monitoring',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="inframondev_us_grp@oracle.com" jiraProject="APPMGMT" opsJiraProject="APPMGMT"
def test_search_associated_resources(testing_service_client):
    if not testing_service_client.is_api_enabled('stack_monitoring', 'SearchAssociatedResources'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('stack_monitoring', util.camelize('stack_monitoring'), 'SearchAssociatedResources')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='stack_monitoring', api_name='SearchAssociatedResources')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.stack_monitoring.StackMonitoringClient(config, service_endpoint=service_endpoint)
            response = client.search_associated_resources(
                search_associated_resources_details=request.pop(util.camelize('SearchAssociatedResourcesDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.search_associated_resources(
                    search_associated_resources_details=request.pop(util.camelize('SearchAssociatedResourcesDetails')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.search_associated_resources(
                        search_associated_resources_details=request.pop(util.camelize('SearchAssociatedResourcesDetails')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'stack_monitoring',
            'SearchAssociatedResources',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'associatedResourcesCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="inframondev_us_grp@oracle.com" jiraProject="APPMGMT" opsJiraProject="APPMGMT"
def test_search_monitored_resource_associations(testing_service_client):
    if not testing_service_client.is_api_enabled('stack_monitoring', 'SearchMonitoredResourceAssociations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('stack_monitoring', util.camelize('stack_monitoring'), 'SearchMonitoredResourceAssociations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='stack_monitoring', api_name='SearchMonitoredResourceAssociations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.stack_monitoring.StackMonitoringClient(config, service_endpoint=service_endpoint)
            response = client.search_monitored_resource_associations(
                search_monitored_resource_associations_details=request.pop(util.camelize('SearchMonitoredResourceAssociationsDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.search_monitored_resource_associations(
                    search_monitored_resource_associations_details=request.pop(util.camelize('SearchMonitoredResourceAssociationsDetails')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.search_monitored_resource_associations(
                        search_monitored_resource_associations_details=request.pop(util.camelize('SearchMonitoredResourceAssociationsDetails')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'stack_monitoring',
            'SearchMonitoredResourceAssociations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'monitoredResourceAssociationsCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="inframondev_us_grp@oracle.com" jiraProject="APPMGMT" opsJiraProject="APPMGMT"
def test_search_monitored_resource_members(testing_service_client):
    if not testing_service_client.is_api_enabled('stack_monitoring', 'SearchMonitoredResourceMembers'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('stack_monitoring', util.camelize('stack_monitoring'), 'SearchMonitoredResourceMembers')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='stack_monitoring', api_name='SearchMonitoredResourceMembers')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.stack_monitoring.StackMonitoringClient(config, service_endpoint=service_endpoint)
            response = client.search_monitored_resource_members(
                monitored_resource_id=request.pop(util.camelize('monitoredResourceId')),
                search_monitored_resource_members_details=request.pop(util.camelize('SearchMonitoredResourceMembersDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.search_monitored_resource_members(
                    monitored_resource_id=request.pop(util.camelize('monitoredResourceId')),
                    search_monitored_resource_members_details=request.pop(util.camelize('SearchMonitoredResourceMembersDetails')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.search_monitored_resource_members(
                        monitored_resource_id=request.pop(util.camelize('monitoredResourceId')),
                        search_monitored_resource_members_details=request.pop(util.camelize('SearchMonitoredResourceMembersDetails')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'stack_monitoring',
            'SearchMonitoredResourceMembers',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'monitoredResourceMembersCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="inframondev_us_grp@oracle.com" jiraProject="APPMGMT" opsJiraProject="APPMGMT"
def test_search_monitored_resources(testing_service_client):
    if not testing_service_client.is_api_enabled('stack_monitoring', 'SearchMonitoredResources'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('stack_monitoring', util.camelize('stack_monitoring'), 'SearchMonitoredResources')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='stack_monitoring', api_name='SearchMonitoredResources')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.stack_monitoring.StackMonitoringClient(config, service_endpoint=service_endpoint)
            response = client.search_monitored_resources(
                search_monitored_resources_details=request.pop(util.camelize('SearchMonitoredResourcesDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.search_monitored_resources(
                    search_monitored_resources_details=request.pop(util.camelize('SearchMonitoredResourcesDetails')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.search_monitored_resources(
                        search_monitored_resources_details=request.pop(util.camelize('SearchMonitoredResourcesDetails')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'stack_monitoring',
            'SearchMonitoredResources',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'monitoredResourceCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="inframondev_us_grp@oracle.com" jiraProject="APPMGMT" opsJiraProject="APPMGMT"
def test_update_monitored_resource(testing_service_client):
    if not testing_service_client.is_api_enabled('stack_monitoring', 'UpdateMonitoredResource'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('stack_monitoring', util.camelize('stack_monitoring'), 'UpdateMonitoredResource')
    )

    request_containers = testing_service_client.get_requests(service_name='stack_monitoring', api_name='UpdateMonitoredResource')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.stack_monitoring.StackMonitoringClient(config, service_endpoint=service_endpoint)
            response = client.update_monitored_resource(
                monitored_resource_id=request.pop(util.camelize('monitoredResourceId')),
                update_monitored_resource_details=request.pop(util.camelize('UpdateMonitoredResourceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'stack_monitoring',
            'UpdateMonitoredResource',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_monitored_resource',
            False,
            False
        )
