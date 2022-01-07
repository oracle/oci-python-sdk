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

        cassette_location = os.path.join('generated', 'apm_synthetics_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="rchandok_org_ww@oracle.com" jiraProject="APM" opsJiraProject="APMSDC"
def test_create_monitor(testing_service_client):
    if not testing_service_client.is_api_enabled('apm_synthetics', 'CreateMonitor'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apm_synthetics', util.camelize('apm_synthetic'), 'CreateMonitor')
    )

    request_containers = testing_service_client.get_requests(service_name='apm_synthetics', api_name='CreateMonitor')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apm_synthetics.ApmSyntheticClient(config, service_endpoint=service_endpoint)
            response = client.create_monitor(
                apm_domain_id=request.pop(util.camelize('apmDomainId')),
                create_monitor_details=request.pop(util.camelize('CreateMonitorDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apm_synthetics',
            'CreateMonitor',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'monitor',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="rchandok_org_ww@oracle.com" jiraProject="APM" opsJiraProject="APMSDC"
def test_create_script(testing_service_client):
    if not testing_service_client.is_api_enabled('apm_synthetics', 'CreateScript'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apm_synthetics', util.camelize('apm_synthetic'), 'CreateScript')
    )

    request_containers = testing_service_client.get_requests(service_name='apm_synthetics', api_name='CreateScript')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apm_synthetics.ApmSyntheticClient(config, service_endpoint=service_endpoint)
            response = client.create_script(
                apm_domain_id=request.pop(util.camelize('apmDomainId')),
                create_script_details=request.pop(util.camelize('CreateScriptDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apm_synthetics',
            'CreateScript',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'script',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="rchandok_org_ww@oracle.com" jiraProject="APM" opsJiraProject="APMSDC"
def test_delete_monitor(testing_service_client):
    if not testing_service_client.is_api_enabled('apm_synthetics', 'DeleteMonitor'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apm_synthetics', util.camelize('apm_synthetic'), 'DeleteMonitor')
    )

    request_containers = testing_service_client.get_requests(service_name='apm_synthetics', api_name='DeleteMonitor')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apm_synthetics.ApmSyntheticClient(config, service_endpoint=service_endpoint)
            response = client.delete_monitor(
                apm_domain_id=request.pop(util.camelize('apmDomainId')),
                monitor_id=request.pop(util.camelize('monitorId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apm_synthetics',
            'DeleteMonitor',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_monitor',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="rchandok_org_ww@oracle.com" jiraProject="APM" opsJiraProject="APMSDC"
def test_delete_script(testing_service_client):
    if not testing_service_client.is_api_enabled('apm_synthetics', 'DeleteScript'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apm_synthetics', util.camelize('apm_synthetic'), 'DeleteScript')
    )

    request_containers = testing_service_client.get_requests(service_name='apm_synthetics', api_name='DeleteScript')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apm_synthetics.ApmSyntheticClient(config, service_endpoint=service_endpoint)
            response = client.delete_script(
                apm_domain_id=request.pop(util.camelize('apmDomainId')),
                script_id=request.pop(util.camelize('scriptId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apm_synthetics',
            'DeleteScript',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_script',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="rchandok_org_ww@oracle.com" jiraProject="APM" opsJiraProject="APMSDC"
def test_get_monitor(testing_service_client):
    if not testing_service_client.is_api_enabled('apm_synthetics', 'GetMonitor'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apm_synthetics', util.camelize('apm_synthetic'), 'GetMonitor')
    )

    request_containers = testing_service_client.get_requests(service_name='apm_synthetics', api_name='GetMonitor')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apm_synthetics.ApmSyntheticClient(config, service_endpoint=service_endpoint)
            response = client.get_monitor(
                apm_domain_id=request.pop(util.camelize('apmDomainId')),
                monitor_id=request.pop(util.camelize('monitorId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apm_synthetics',
            'GetMonitor',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'monitor',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="rchandok_org_ww@oracle.com" jiraProject="APM" opsJiraProject="APMSDC"
def test_get_monitor_result(testing_service_client):
    if not testing_service_client.is_api_enabled('apm_synthetics', 'GetMonitorResult'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apm_synthetics', util.camelize('apm_synthetic'), 'GetMonitorResult')
    )

    request_containers = testing_service_client.get_requests(service_name='apm_synthetics', api_name='GetMonitorResult')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apm_synthetics.ApmSyntheticClient(config, service_endpoint=service_endpoint)
            response = client.get_monitor_result(
                apm_domain_id=request.pop(util.camelize('apmDomainId')),
                monitor_id=request.pop(util.camelize('monitorId')),
                vantage_point=request.pop(util.camelize('vantagePoint')),
                result_type=request.pop(util.camelize('resultType')),
                result_content_type=request.pop(util.camelize('resultContentType')),
                execution_time=request.pop(util.camelize('executionTime')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apm_synthetics',
            'GetMonitorResult',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'monitorResult',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="rchandok_org_ww@oracle.com" jiraProject="APM" opsJiraProject="APMSDC"
def test_get_script(testing_service_client):
    if not testing_service_client.is_api_enabled('apm_synthetics', 'GetScript'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apm_synthetics', util.camelize('apm_synthetic'), 'GetScript')
    )

    request_containers = testing_service_client.get_requests(service_name='apm_synthetics', api_name='GetScript')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apm_synthetics.ApmSyntheticClient(config, service_endpoint=service_endpoint)
            response = client.get_script(
                apm_domain_id=request.pop(util.camelize('apmDomainId')),
                script_id=request.pop(util.camelize('scriptId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apm_synthetics',
            'GetScript',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'script',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="rchandok_org_ww@oracle.com" jiraProject="APM" opsJiraProject="APMSDC"
def test_list_monitors(testing_service_client):
    if not testing_service_client.is_api_enabled('apm_synthetics', 'ListMonitors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apm_synthetics', util.camelize('apm_synthetic'), 'ListMonitors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='apm_synthetics', api_name='ListMonitors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apm_synthetics.ApmSyntheticClient(config, service_endpoint=service_endpoint)
            response = client.list_monitors(
                apm_domain_id=request.pop(util.camelize('apmDomainId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_monitors(
                    apm_domain_id=request.pop(util.camelize('apmDomainId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_monitors(
                        apm_domain_id=request.pop(util.camelize('apmDomainId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apm_synthetics',
            'ListMonitors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'monitorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="rchandok_org_ww@oracle.com" jiraProject="APM" opsJiraProject="APMSDC"
def test_list_public_vantage_points(testing_service_client):
    if not testing_service_client.is_api_enabled('apm_synthetics', 'ListPublicVantagePoints'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apm_synthetics', util.camelize('apm_synthetic'), 'ListPublicVantagePoints')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='apm_synthetics', api_name='ListPublicVantagePoints')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apm_synthetics.ApmSyntheticClient(config, service_endpoint=service_endpoint)
            response = client.list_public_vantage_points(
                apm_domain_id=request.pop(util.camelize('apmDomainId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_public_vantage_points(
                    apm_domain_id=request.pop(util.camelize('apmDomainId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_public_vantage_points(
                        apm_domain_id=request.pop(util.camelize('apmDomainId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apm_synthetics',
            'ListPublicVantagePoints',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'publicVantagePointCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="rchandok_org_ww@oracle.com" jiraProject="APM" opsJiraProject="APMSDC"
def test_list_scripts(testing_service_client):
    if not testing_service_client.is_api_enabled('apm_synthetics', 'ListScripts'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apm_synthetics', util.camelize('apm_synthetic'), 'ListScripts')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='apm_synthetics', api_name='ListScripts')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apm_synthetics.ApmSyntheticClient(config, service_endpoint=service_endpoint)
            response = client.list_scripts(
                apm_domain_id=request.pop(util.camelize('apmDomainId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_scripts(
                    apm_domain_id=request.pop(util.camelize('apmDomainId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_scripts(
                        apm_domain_id=request.pop(util.camelize('apmDomainId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apm_synthetics',
            'ListScripts',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'scriptCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="rchandok_org_ww@oracle.com" jiraProject="APM" opsJiraProject="APMSDC"
def test_update_monitor(testing_service_client):
    if not testing_service_client.is_api_enabled('apm_synthetics', 'UpdateMonitor'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apm_synthetics', util.camelize('apm_synthetic'), 'UpdateMonitor')
    )

    request_containers = testing_service_client.get_requests(service_name='apm_synthetics', api_name='UpdateMonitor')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apm_synthetics.ApmSyntheticClient(config, service_endpoint=service_endpoint)
            response = client.update_monitor(
                apm_domain_id=request.pop(util.camelize('apmDomainId')),
                monitor_id=request.pop(util.camelize('monitorId')),
                update_monitor_details=request.pop(util.camelize('UpdateMonitorDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apm_synthetics',
            'UpdateMonitor',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'monitor',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="rchandok_org_ww@oracle.com" jiraProject="APM" opsJiraProject="APMSDC"
def test_update_script(testing_service_client):
    if not testing_service_client.is_api_enabled('apm_synthetics', 'UpdateScript'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apm_synthetics', util.camelize('apm_synthetic'), 'UpdateScript')
    )

    request_containers = testing_service_client.get_requests(service_name='apm_synthetics', api_name='UpdateScript')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apm_synthetics.ApmSyntheticClient(config, service_endpoint=service_endpoint)
            response = client.update_script(
                apm_domain_id=request.pop(util.camelize('apmDomainId')),
                script_id=request.pop(util.camelize('scriptId')),
                update_script_details=request.pop(util.camelize('UpdateScriptDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apm_synthetics',
            'UpdateScript',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'script',
            False,
            False
        )
