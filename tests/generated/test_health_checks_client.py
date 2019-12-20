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

        cassette_location = os.path.join('generated', 'healthchecks_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="groan-chomskies_us_grp@oracle.com" jiraProject="OHC" opsJiraProject="HC"
def test_change_http_monitor_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('healthchecks', 'ChangeHttpMonitorCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('healthchecks', util.camelize('health_checks'), 'ChangeHttpMonitorCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='healthchecks', api_name='ChangeHttpMonitorCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.healthchecks.HealthChecksClient(config, service_endpoint=service_endpoint)
            response = client.change_http_monitor_compartment(
                monitor_id=request.pop(util.camelize('monitorId')),
                change_http_monitor_compartment_details=request.pop(util.camelize('ChangeHttpMonitorCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'healthchecks',
            'ChangeHttpMonitorCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_http_monitor_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="groan-chomskies_us_grp@oracle.com" jiraProject="OHC" opsJiraProject="HC"
def test_change_ping_monitor_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('healthchecks', 'ChangePingMonitorCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('healthchecks', util.camelize('health_checks'), 'ChangePingMonitorCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='healthchecks', api_name='ChangePingMonitorCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.healthchecks.HealthChecksClient(config, service_endpoint=service_endpoint)
            response = client.change_ping_monitor_compartment(
                monitor_id=request.pop(util.camelize('monitorId')),
                change_ping_monitor_compartment_details=request.pop(util.camelize('ChangePingMonitorCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'healthchecks',
            'ChangePingMonitorCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_ping_monitor_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="groan-chomskies_us_grp@oracle.com" jiraProject="OHC" opsJiraProject="HC"
def test_create_http_monitor(testing_service_client):
    if not testing_service_client.is_api_enabled('healthchecks', 'CreateHttpMonitor'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('healthchecks', util.camelize('health_checks'), 'CreateHttpMonitor')
    )

    request_containers = testing_service_client.get_requests(service_name='healthchecks', api_name='CreateHttpMonitor')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.healthchecks.HealthChecksClient(config, service_endpoint=service_endpoint)
            response = client.create_http_monitor(
                create_http_monitor_details=request.pop(util.camelize('CreateHttpMonitorDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'healthchecks',
            'CreateHttpMonitor',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'httpMonitor',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="groan-chomskies_us_grp@oracle.com" jiraProject="OHC" opsJiraProject="HC"
def test_create_on_demand_http_probe(testing_service_client):
    if not testing_service_client.is_api_enabled('healthchecks', 'CreateOnDemandHttpProbe'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('healthchecks', util.camelize('health_checks'), 'CreateOnDemandHttpProbe')
    )

    request_containers = testing_service_client.get_requests(service_name='healthchecks', api_name='CreateOnDemandHttpProbe')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.healthchecks.HealthChecksClient(config, service_endpoint=service_endpoint)
            response = client.create_on_demand_http_probe(
                create_on_demand_http_probe_details=request.pop(util.camelize('CreateOnDemandHttpProbeDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'healthchecks',
            'CreateOnDemandHttpProbe',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'httpProbe',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="groan-chomskies_us_grp@oracle.com" jiraProject="OHC" opsJiraProject="HC"
def test_create_on_demand_ping_probe(testing_service_client):
    if not testing_service_client.is_api_enabled('healthchecks', 'CreateOnDemandPingProbe'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('healthchecks', util.camelize('health_checks'), 'CreateOnDemandPingProbe')
    )

    request_containers = testing_service_client.get_requests(service_name='healthchecks', api_name='CreateOnDemandPingProbe')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.healthchecks.HealthChecksClient(config, service_endpoint=service_endpoint)
            response = client.create_on_demand_ping_probe(
                create_on_demand_ping_probe_details=request.pop(util.camelize('CreateOnDemandPingProbeDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'healthchecks',
            'CreateOnDemandPingProbe',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'pingProbe',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="groan-chomskies_us_grp@oracle.com" jiraProject="OHC" opsJiraProject="HC"
def test_create_ping_monitor(testing_service_client):
    if not testing_service_client.is_api_enabled('healthchecks', 'CreatePingMonitor'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('healthchecks', util.camelize('health_checks'), 'CreatePingMonitor')
    )

    request_containers = testing_service_client.get_requests(service_name='healthchecks', api_name='CreatePingMonitor')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.healthchecks.HealthChecksClient(config, service_endpoint=service_endpoint)
            response = client.create_ping_monitor(
                create_ping_monitor_details=request.pop(util.camelize('CreatePingMonitorDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'healthchecks',
            'CreatePingMonitor',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'pingMonitor',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="groan-chomskies_us_grp@oracle.com" jiraProject="OHC" opsJiraProject="HC"
def test_delete_http_monitor(testing_service_client):
    if not testing_service_client.is_api_enabled('healthchecks', 'DeleteHttpMonitor'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('healthchecks', util.camelize('health_checks'), 'DeleteHttpMonitor')
    )

    request_containers = testing_service_client.get_requests(service_name='healthchecks', api_name='DeleteHttpMonitor')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.healthchecks.HealthChecksClient(config, service_endpoint=service_endpoint)
            response = client.delete_http_monitor(
                monitor_id=request.pop(util.camelize('monitorId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'healthchecks',
            'DeleteHttpMonitor',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_http_monitor',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="groan-chomskies_us_grp@oracle.com" jiraProject="OHC" opsJiraProject="HC"
def test_delete_ping_monitor(testing_service_client):
    if not testing_service_client.is_api_enabled('healthchecks', 'DeletePingMonitor'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('healthchecks', util.camelize('health_checks'), 'DeletePingMonitor')
    )

    request_containers = testing_service_client.get_requests(service_name='healthchecks', api_name='DeletePingMonitor')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.healthchecks.HealthChecksClient(config, service_endpoint=service_endpoint)
            response = client.delete_ping_monitor(
                monitor_id=request.pop(util.camelize('monitorId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'healthchecks',
            'DeletePingMonitor',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_ping_monitor',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="groan-chomskies_us_grp@oracle.com" jiraProject="OHC" opsJiraProject="HC"
def test_get_http_monitor(testing_service_client):
    if not testing_service_client.is_api_enabled('healthchecks', 'GetHttpMonitor'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('healthchecks', util.camelize('health_checks'), 'GetHttpMonitor')
    )

    request_containers = testing_service_client.get_requests(service_name='healthchecks', api_name='GetHttpMonitor')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.healthchecks.HealthChecksClient(config, service_endpoint=service_endpoint)
            response = client.get_http_monitor(
                monitor_id=request.pop(util.camelize('monitorId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'healthchecks',
            'GetHttpMonitor',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'httpMonitor',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="groan-chomskies_us_grp@oracle.com" jiraProject="OHC" opsJiraProject="HC"
def test_get_ping_monitor(testing_service_client):
    if not testing_service_client.is_api_enabled('healthchecks', 'GetPingMonitor'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('healthchecks', util.camelize('health_checks'), 'GetPingMonitor')
    )

    request_containers = testing_service_client.get_requests(service_name='healthchecks', api_name='GetPingMonitor')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.healthchecks.HealthChecksClient(config, service_endpoint=service_endpoint)
            response = client.get_ping_monitor(
                monitor_id=request.pop(util.camelize('monitorId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'healthchecks',
            'GetPingMonitor',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'pingMonitor',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="groan-chomskies_us_grp@oracle.com" jiraProject="OHC" opsJiraProject="HC"
def test_list_health_checks_vantage_points(testing_service_client):
    if not testing_service_client.is_api_enabled('healthchecks', 'ListHealthChecksVantagePoints'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('healthchecks', util.camelize('health_checks'), 'ListHealthChecksVantagePoints')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='healthchecks', api_name='ListHealthChecksVantagePoints')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.healthchecks.HealthChecksClient(config, service_endpoint=service_endpoint)
            response = client.list_health_checks_vantage_points(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_health_checks_vantage_points(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_health_checks_vantage_points(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'healthchecks',
            'ListHealthChecksVantagePoints',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'healthChecksVantagePointSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="groan-chomskies_us_grp@oracle.com" jiraProject="OHC" opsJiraProject="HC"
def test_list_http_monitors(testing_service_client):
    if not testing_service_client.is_api_enabled('healthchecks', 'ListHttpMonitors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('healthchecks', util.camelize('health_checks'), 'ListHttpMonitors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='healthchecks', api_name='ListHttpMonitors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.healthchecks.HealthChecksClient(config, service_endpoint=service_endpoint)
            response = client.list_http_monitors(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_http_monitors(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_http_monitors(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'healthchecks',
            'ListHttpMonitors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'httpMonitorSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="groan-chomskies_us_grp@oracle.com" jiraProject="OHC" opsJiraProject="HC"
def test_list_http_probe_results(testing_service_client):
    if not testing_service_client.is_api_enabled('healthchecks', 'ListHttpProbeResults'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('healthchecks', util.camelize('health_checks'), 'ListHttpProbeResults')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='healthchecks', api_name='ListHttpProbeResults')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.healthchecks.HealthChecksClient(config, service_endpoint=service_endpoint)
            response = client.list_http_probe_results(
                probe_configuration_id=request.pop(util.camelize('probeConfigurationId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_http_probe_results(
                    probe_configuration_id=request.pop(util.camelize('probeConfigurationId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_http_probe_results(
                        probe_configuration_id=request.pop(util.camelize('probeConfigurationId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'healthchecks',
            'ListHttpProbeResults',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'httpProbeResultSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="groan-chomskies_us_grp@oracle.com" jiraProject="OHC" opsJiraProject="HC"
def test_list_ping_monitors(testing_service_client):
    if not testing_service_client.is_api_enabled('healthchecks', 'ListPingMonitors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('healthchecks', util.camelize('health_checks'), 'ListPingMonitors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='healthchecks', api_name='ListPingMonitors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.healthchecks.HealthChecksClient(config, service_endpoint=service_endpoint)
            response = client.list_ping_monitors(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_ping_monitors(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_ping_monitors(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'healthchecks',
            'ListPingMonitors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'pingMonitorSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="groan-chomskies_us_grp@oracle.com" jiraProject="OHC" opsJiraProject="HC"
def test_list_ping_probe_results(testing_service_client):
    if not testing_service_client.is_api_enabled('healthchecks', 'ListPingProbeResults'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('healthchecks', util.camelize('health_checks'), 'ListPingProbeResults')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='healthchecks', api_name='ListPingProbeResults')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.healthchecks.HealthChecksClient(config, service_endpoint=service_endpoint)
            response = client.list_ping_probe_results(
                probe_configuration_id=request.pop(util.camelize('probeConfigurationId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_ping_probe_results(
                    probe_configuration_id=request.pop(util.camelize('probeConfigurationId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_ping_probe_results(
                        probe_configuration_id=request.pop(util.camelize('probeConfigurationId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'healthchecks',
            'ListPingProbeResults',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'pingProbeResultSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="groan-chomskies_us_grp@oracle.com" jiraProject="OHC" opsJiraProject="HC"
def test_update_http_monitor(testing_service_client):
    if not testing_service_client.is_api_enabled('healthchecks', 'UpdateHttpMonitor'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('healthchecks', util.camelize('health_checks'), 'UpdateHttpMonitor')
    )

    request_containers = testing_service_client.get_requests(service_name='healthchecks', api_name='UpdateHttpMonitor')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.healthchecks.HealthChecksClient(config, service_endpoint=service_endpoint)
            response = client.update_http_monitor(
                monitor_id=request.pop(util.camelize('monitorId')),
                update_http_monitor_details=request.pop(util.camelize('UpdateHttpMonitorDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'healthchecks',
            'UpdateHttpMonitor',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'httpMonitor',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="groan-chomskies_us_grp@oracle.com" jiraProject="OHC" opsJiraProject="HC"
def test_update_ping_monitor(testing_service_client):
    if not testing_service_client.is_api_enabled('healthchecks', 'UpdatePingMonitor'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('healthchecks', util.camelize('health_checks'), 'UpdatePingMonitor')
    )

    request_containers = testing_service_client.get_requests(service_name='healthchecks', api_name='UpdatePingMonitor')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.healthchecks.HealthChecksClient(config, service_endpoint=service_endpoint)
            response = client.update_ping_monitor(
                monitor_id=request.pop(util.camelize('monitorId')),
                update_ping_monitor_details=request.pop(util.camelize('UpdatePingMonitorDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'healthchecks',
            'UpdatePingMonitor',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'pingMonitor',
            False,
            False
        )
