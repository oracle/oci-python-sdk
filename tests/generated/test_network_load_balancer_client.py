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

        cassette_location = os.path.join('generated', 'network_load_balancer_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="NLB" opsJiraProject="NLB"
def test_change_network_load_balancer_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('network_load_balancer', 'ChangeNetworkLoadBalancerCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_load_balancer', util.camelize('network_load_balancer'), 'ChangeNetworkLoadBalancerCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='network_load_balancer', api_name='ChangeNetworkLoadBalancerCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_load_balancer.NetworkLoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.change_network_load_balancer_compartment(
                network_load_balancer_id=request.pop(util.camelize('networkLoadBalancerId')),
                change_network_load_balancer_compartment_details=request.pop(util.camelize('ChangeNetworkLoadBalancerCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_load_balancer',
            'ChangeNetworkLoadBalancerCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_network_load_balancer_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="NLB" opsJiraProject="NLB"
def test_create_backend(testing_service_client):
    if not testing_service_client.is_api_enabled('network_load_balancer', 'CreateBackend'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_load_balancer', util.camelize('network_load_balancer'), 'CreateBackend')
    )

    request_containers = testing_service_client.get_requests(service_name='network_load_balancer', api_name='CreateBackend')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_load_balancer.NetworkLoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.create_backend(
                network_load_balancer_id=request.pop(util.camelize('networkLoadBalancerId')),
                create_backend_details=request.pop(util.camelize('CreateBackendDetails')),
                backend_set_name=request.pop(util.camelize('backendSetName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_load_balancer',
            'CreateBackend',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_backend',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="NLB" opsJiraProject="NLB"
def test_create_backend_set(testing_service_client):
    if not testing_service_client.is_api_enabled('network_load_balancer', 'CreateBackendSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_load_balancer', util.camelize('network_load_balancer'), 'CreateBackendSet')
    )

    request_containers = testing_service_client.get_requests(service_name='network_load_balancer', api_name='CreateBackendSet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_load_balancer.NetworkLoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.create_backend_set(
                network_load_balancer_id=request.pop(util.camelize('networkLoadBalancerId')),
                create_backend_set_details=request.pop(util.camelize('CreateBackendSetDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_load_balancer',
            'CreateBackendSet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_backend_set',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="NLB" opsJiraProject="NLB"
def test_create_listener(testing_service_client):
    if not testing_service_client.is_api_enabled('network_load_balancer', 'CreateListener'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_load_balancer', util.camelize('network_load_balancer'), 'CreateListener')
    )

    request_containers = testing_service_client.get_requests(service_name='network_load_balancer', api_name='CreateListener')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_load_balancer.NetworkLoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.create_listener(
                network_load_balancer_id=request.pop(util.camelize('networkLoadBalancerId')),
                create_listener_details=request.pop(util.camelize('CreateListenerDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_load_balancer',
            'CreateListener',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_listener',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="NLB" opsJiraProject="NLB"
def test_create_network_load_balancer(testing_service_client):
    if not testing_service_client.is_api_enabled('network_load_balancer', 'CreateNetworkLoadBalancer'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_load_balancer', util.camelize('network_load_balancer'), 'CreateNetworkLoadBalancer')
    )

    request_containers = testing_service_client.get_requests(service_name='network_load_balancer', api_name='CreateNetworkLoadBalancer')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_load_balancer.NetworkLoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.create_network_load_balancer(
                create_network_load_balancer_details=request.pop(util.camelize('CreateNetworkLoadBalancerDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_load_balancer',
            'CreateNetworkLoadBalancer',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'networkLoadBalancer',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="NLB" opsJiraProject="NLB"
def test_delete_backend(testing_service_client):
    if not testing_service_client.is_api_enabled('network_load_balancer', 'DeleteBackend'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_load_balancer', util.camelize('network_load_balancer'), 'DeleteBackend')
    )

    request_containers = testing_service_client.get_requests(service_name='network_load_balancer', api_name='DeleteBackend')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_load_balancer.NetworkLoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.delete_backend(
                network_load_balancer_id=request.pop(util.camelize('networkLoadBalancerId')),
                backend_set_name=request.pop(util.camelize('backendSetName')),
                backend_name=request.pop(util.camelize('backendName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_load_balancer',
            'DeleteBackend',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_backend',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="NLB" opsJiraProject="NLB"
def test_delete_backend_set(testing_service_client):
    if not testing_service_client.is_api_enabled('network_load_balancer', 'DeleteBackendSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_load_balancer', util.camelize('network_load_balancer'), 'DeleteBackendSet')
    )

    request_containers = testing_service_client.get_requests(service_name='network_load_balancer', api_name='DeleteBackendSet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_load_balancer.NetworkLoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.delete_backend_set(
                network_load_balancer_id=request.pop(util.camelize('networkLoadBalancerId')),
                backend_set_name=request.pop(util.camelize('backendSetName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_load_balancer',
            'DeleteBackendSet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_backend_set',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="NLB" opsJiraProject="NLB"
def test_delete_listener(testing_service_client):
    if not testing_service_client.is_api_enabled('network_load_balancer', 'DeleteListener'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_load_balancer', util.camelize('network_load_balancer'), 'DeleteListener')
    )

    request_containers = testing_service_client.get_requests(service_name='network_load_balancer', api_name='DeleteListener')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_load_balancer.NetworkLoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.delete_listener(
                network_load_balancer_id=request.pop(util.camelize('networkLoadBalancerId')),
                listener_name=request.pop(util.camelize('listenerName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_load_balancer',
            'DeleteListener',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_listener',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="NLB" opsJiraProject="NLB"
def test_delete_network_load_balancer(testing_service_client):
    if not testing_service_client.is_api_enabled('network_load_balancer', 'DeleteNetworkLoadBalancer'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_load_balancer', util.camelize('network_load_balancer'), 'DeleteNetworkLoadBalancer')
    )

    request_containers = testing_service_client.get_requests(service_name='network_load_balancer', api_name='DeleteNetworkLoadBalancer')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_load_balancer.NetworkLoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.delete_network_load_balancer(
                network_load_balancer_id=request.pop(util.camelize('networkLoadBalancerId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_load_balancer',
            'DeleteNetworkLoadBalancer',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_network_load_balancer',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="NLB" opsJiraProject="NLB"
def test_get_backend(testing_service_client):
    if not testing_service_client.is_api_enabled('network_load_balancer', 'GetBackend'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_load_balancer', util.camelize('network_load_balancer'), 'GetBackend')
    )

    request_containers = testing_service_client.get_requests(service_name='network_load_balancer', api_name='GetBackend')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_load_balancer.NetworkLoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.get_backend(
                network_load_balancer_id=request.pop(util.camelize('networkLoadBalancerId')),
                backend_set_name=request.pop(util.camelize('backendSetName')),
                backend_name=request.pop(util.camelize('backendName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_load_balancer',
            'GetBackend',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'backend',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="NLB" opsJiraProject="NLB"
def test_get_backend_health(testing_service_client):
    if not testing_service_client.is_api_enabled('network_load_balancer', 'GetBackendHealth'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_load_balancer', util.camelize('network_load_balancer'), 'GetBackendHealth')
    )

    request_containers = testing_service_client.get_requests(service_name='network_load_balancer', api_name='GetBackendHealth')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_load_balancer.NetworkLoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.get_backend_health(
                network_load_balancer_id=request.pop(util.camelize('networkLoadBalancerId')),
                backend_set_name=request.pop(util.camelize('backendSetName')),
                backend_name=request.pop(util.camelize('backendName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_load_balancer',
            'GetBackendHealth',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'backendHealth',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="NLB" opsJiraProject="NLB"
def test_get_backend_set(testing_service_client):
    if not testing_service_client.is_api_enabled('network_load_balancer', 'GetBackendSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_load_balancer', util.camelize('network_load_balancer'), 'GetBackendSet')
    )

    request_containers = testing_service_client.get_requests(service_name='network_load_balancer', api_name='GetBackendSet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_load_balancer.NetworkLoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.get_backend_set(
                network_load_balancer_id=request.pop(util.camelize('networkLoadBalancerId')),
                backend_set_name=request.pop(util.camelize('backendSetName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_load_balancer',
            'GetBackendSet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'backendSet',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="NLB" opsJiraProject="NLB"
def test_get_backend_set_health(testing_service_client):
    if not testing_service_client.is_api_enabled('network_load_balancer', 'GetBackendSetHealth'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_load_balancer', util.camelize('network_load_balancer'), 'GetBackendSetHealth')
    )

    request_containers = testing_service_client.get_requests(service_name='network_load_balancer', api_name='GetBackendSetHealth')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_load_balancer.NetworkLoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.get_backend_set_health(
                network_load_balancer_id=request.pop(util.camelize('networkLoadBalancerId')),
                backend_set_name=request.pop(util.camelize('backendSetName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_load_balancer',
            'GetBackendSetHealth',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'backendSetHealth',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="NLB" opsJiraProject="NLB"
def test_get_health_checker(testing_service_client):
    if not testing_service_client.is_api_enabled('network_load_balancer', 'GetHealthChecker'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_load_balancer', util.camelize('network_load_balancer'), 'GetHealthChecker')
    )

    request_containers = testing_service_client.get_requests(service_name='network_load_balancer', api_name='GetHealthChecker')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_load_balancer.NetworkLoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.get_health_checker(
                network_load_balancer_id=request.pop(util.camelize('networkLoadBalancerId')),
                backend_set_name=request.pop(util.camelize('backendSetName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_load_balancer',
            'GetHealthChecker',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'healthChecker',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="NLB" opsJiraProject="NLB"
def test_get_listener(testing_service_client):
    if not testing_service_client.is_api_enabled('network_load_balancer', 'GetListener'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_load_balancer', util.camelize('network_load_balancer'), 'GetListener')
    )

    request_containers = testing_service_client.get_requests(service_name='network_load_balancer', api_name='GetListener')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_load_balancer.NetworkLoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.get_listener(
                network_load_balancer_id=request.pop(util.camelize('networkLoadBalancerId')),
                listener_name=request.pop(util.camelize('listenerName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_load_balancer',
            'GetListener',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'listener',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="NLB" opsJiraProject="NLB"
def test_get_network_load_balancer(testing_service_client):
    if not testing_service_client.is_api_enabled('network_load_balancer', 'GetNetworkLoadBalancer'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_load_balancer', util.camelize('network_load_balancer'), 'GetNetworkLoadBalancer')
    )

    request_containers = testing_service_client.get_requests(service_name='network_load_balancer', api_name='GetNetworkLoadBalancer')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_load_balancer.NetworkLoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.get_network_load_balancer(
                network_load_balancer_id=request.pop(util.camelize('networkLoadBalancerId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_load_balancer',
            'GetNetworkLoadBalancer',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'networkLoadBalancer',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="NLB" opsJiraProject="NLB"
def test_get_network_load_balancer_health(testing_service_client):
    if not testing_service_client.is_api_enabled('network_load_balancer', 'GetNetworkLoadBalancerHealth'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_load_balancer', util.camelize('network_load_balancer'), 'GetNetworkLoadBalancerHealth')
    )

    request_containers = testing_service_client.get_requests(service_name='network_load_balancer', api_name='GetNetworkLoadBalancerHealth')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_load_balancer.NetworkLoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.get_network_load_balancer_health(
                network_load_balancer_id=request.pop(util.camelize('networkLoadBalancerId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_load_balancer',
            'GetNetworkLoadBalancerHealth',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'networkLoadBalancerHealth',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="NLB" opsJiraProject="NLB"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('network_load_balancer', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_load_balancer', util.camelize('network_load_balancer'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='network_load_balancer', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_load_balancer.NetworkLoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_load_balancer',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="NLB" opsJiraProject="NLB"
def test_list_backend_sets(testing_service_client):
    if not testing_service_client.is_api_enabled('network_load_balancer', 'ListBackendSets'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_load_balancer', util.camelize('network_load_balancer'), 'ListBackendSets')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='network_load_balancer', api_name='ListBackendSets')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_load_balancer.NetworkLoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.list_backend_sets(
                network_load_balancer_id=request.pop(util.camelize('networkLoadBalancerId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_backend_sets(
                    network_load_balancer_id=request.pop(util.camelize('networkLoadBalancerId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_backend_sets(
                        network_load_balancer_id=request.pop(util.camelize('networkLoadBalancerId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_load_balancer',
            'ListBackendSets',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'backendSetCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="NLB" opsJiraProject="NLB"
def test_list_backends(testing_service_client):
    if not testing_service_client.is_api_enabled('network_load_balancer', 'ListBackends'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_load_balancer', util.camelize('network_load_balancer'), 'ListBackends')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='network_load_balancer', api_name='ListBackends')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_load_balancer.NetworkLoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.list_backends(
                network_load_balancer_id=request.pop(util.camelize('networkLoadBalancerId')),
                backend_set_name=request.pop(util.camelize('backendSetName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_backends(
                    network_load_balancer_id=request.pop(util.camelize('networkLoadBalancerId')),
                    backend_set_name=request.pop(util.camelize('backendSetName')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_backends(
                        network_load_balancer_id=request.pop(util.camelize('networkLoadBalancerId')),
                        backend_set_name=request.pop(util.camelize('backendSetName')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_load_balancer',
            'ListBackends',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'backendCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="NLB" opsJiraProject="NLB"
def test_list_listeners(testing_service_client):
    if not testing_service_client.is_api_enabled('network_load_balancer', 'ListListeners'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_load_balancer', util.camelize('network_load_balancer'), 'ListListeners')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='network_load_balancer', api_name='ListListeners')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_load_balancer.NetworkLoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.list_listeners(
                network_load_balancer_id=request.pop(util.camelize('networkLoadBalancerId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_listeners(
                    network_load_balancer_id=request.pop(util.camelize('networkLoadBalancerId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_listeners(
                        network_load_balancer_id=request.pop(util.camelize('networkLoadBalancerId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_load_balancer',
            'ListListeners',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'listenerCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="NLB" opsJiraProject="NLB"
def test_list_network_load_balancer_healths(testing_service_client):
    if not testing_service_client.is_api_enabled('network_load_balancer', 'ListNetworkLoadBalancerHealths'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_load_balancer', util.camelize('network_load_balancer'), 'ListNetworkLoadBalancerHealths')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='network_load_balancer', api_name='ListNetworkLoadBalancerHealths')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_load_balancer.NetworkLoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.list_network_load_balancer_healths(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_network_load_balancer_healths(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_network_load_balancer_healths(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_load_balancer',
            'ListNetworkLoadBalancerHealths',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'networkLoadBalancerHealthCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="NLB" opsJiraProject="NLB"
def test_list_network_load_balancers(testing_service_client):
    if not testing_service_client.is_api_enabled('network_load_balancer', 'ListNetworkLoadBalancers'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_load_balancer', util.camelize('network_load_balancer'), 'ListNetworkLoadBalancers')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='network_load_balancer', api_name='ListNetworkLoadBalancers')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_load_balancer.NetworkLoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.list_network_load_balancers(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_network_load_balancers(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_network_load_balancers(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_load_balancer',
            'ListNetworkLoadBalancers',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'networkLoadBalancerCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="NLB" opsJiraProject="NLB"
def test_list_network_load_balancers_policies(testing_service_client):
    if not testing_service_client.is_api_enabled('network_load_balancer', 'ListNetworkLoadBalancersPolicies'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_load_balancer', util.camelize('network_load_balancer'), 'ListNetworkLoadBalancersPolicies')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='network_load_balancer', api_name='ListNetworkLoadBalancersPolicies')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_load_balancer.NetworkLoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.list_network_load_balancers_policies(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_network_load_balancers_policies(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_network_load_balancers_policies(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_load_balancer',
            'ListNetworkLoadBalancersPolicies',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'networkLoadBalancersPolicyCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="NLB" opsJiraProject="NLB"
def test_list_network_load_balancers_protocols(testing_service_client):
    if not testing_service_client.is_api_enabled('network_load_balancer', 'ListNetworkLoadBalancersProtocols'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_load_balancer', util.camelize('network_load_balancer'), 'ListNetworkLoadBalancersProtocols')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='network_load_balancer', api_name='ListNetworkLoadBalancersProtocols')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_load_balancer.NetworkLoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.list_network_load_balancers_protocols(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_network_load_balancers_protocols(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_network_load_balancers_protocols(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_load_balancer',
            'ListNetworkLoadBalancersProtocols',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'networkLoadBalancersProtocolCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="NLB" opsJiraProject="NLB"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('network_load_balancer', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_load_balancer', util.camelize('network_load_balancer'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='network_load_balancer', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_load_balancer.NetworkLoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_errors(
                work_request_id=request.pop(util.camelize('workRequestId')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_errors(
                    work_request_id=request.pop(util.camelize('workRequestId')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_request_errors(
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_load_balancer',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestErrorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="NLB" opsJiraProject="NLB"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('network_load_balancer', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_load_balancer', util.camelize('network_load_balancer'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='network_load_balancer', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_load_balancer.NetworkLoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_logs(
                work_request_id=request.pop(util.camelize('workRequestId')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_logs(
                    work_request_id=request.pop(util.camelize('workRequestId')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_request_logs(
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_load_balancer',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="NLB" opsJiraProject="NLB"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('network_load_balancer', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_load_balancer', util.camelize('network_load_balancer'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='network_load_balancer', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_load_balancer.NetworkLoadBalancerClient(config, service_endpoint=service_endpoint)
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
            'network_load_balancer',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="NLB" opsJiraProject="NLB"
def test_update_backend(testing_service_client):
    if not testing_service_client.is_api_enabled('network_load_balancer', 'UpdateBackend'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_load_balancer', util.camelize('network_load_balancer'), 'UpdateBackend')
    )

    request_containers = testing_service_client.get_requests(service_name='network_load_balancer', api_name='UpdateBackend')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_load_balancer.NetworkLoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.update_backend(
                network_load_balancer_id=request.pop(util.camelize('networkLoadBalancerId')),
                update_backend_details=request.pop(util.camelize('UpdateBackendDetails')),
                backend_set_name=request.pop(util.camelize('backendSetName')),
                backend_name=request.pop(util.camelize('backendName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_load_balancer',
            'UpdateBackend',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_backend',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="NLB" opsJiraProject="NLB"
def test_update_backend_set(testing_service_client):
    if not testing_service_client.is_api_enabled('network_load_balancer', 'UpdateBackendSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_load_balancer', util.camelize('network_load_balancer'), 'UpdateBackendSet')
    )

    request_containers = testing_service_client.get_requests(service_name='network_load_balancer', api_name='UpdateBackendSet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_load_balancer.NetworkLoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.update_backend_set(
                network_load_balancer_id=request.pop(util.camelize('networkLoadBalancerId')),
                update_backend_set_details=request.pop(util.camelize('UpdateBackendSetDetails')),
                backend_set_name=request.pop(util.camelize('backendSetName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_load_balancer',
            'UpdateBackendSet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_backend_set',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="NLB" opsJiraProject="NLB"
def test_update_health_checker(testing_service_client):
    if not testing_service_client.is_api_enabled('network_load_balancer', 'UpdateHealthChecker'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_load_balancer', util.camelize('network_load_balancer'), 'UpdateHealthChecker')
    )

    request_containers = testing_service_client.get_requests(service_name='network_load_balancer', api_name='UpdateHealthChecker')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_load_balancer.NetworkLoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.update_health_checker(
                network_load_balancer_id=request.pop(util.camelize('networkLoadBalancerId')),
                update_health_checker_details=request.pop(util.camelize('UpdateHealthCheckerDetails')),
                backend_set_name=request.pop(util.camelize('backendSetName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_load_balancer',
            'UpdateHealthChecker',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_health_checker',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="NLB" opsJiraProject="NLB"
def test_update_listener(testing_service_client):
    if not testing_service_client.is_api_enabled('network_load_balancer', 'UpdateListener'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_load_balancer', util.camelize('network_load_balancer'), 'UpdateListener')
    )

    request_containers = testing_service_client.get_requests(service_name='network_load_balancer', api_name='UpdateListener')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_load_balancer.NetworkLoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.update_listener(
                network_load_balancer_id=request.pop(util.camelize('networkLoadBalancerId')),
                update_listener_details=request.pop(util.camelize('UpdateListenerDetails')),
                listener_name=request.pop(util.camelize('listenerName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_load_balancer',
            'UpdateListener',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_listener',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="NLB" opsJiraProject="NLB"
def test_update_network_load_balancer(testing_service_client):
    if not testing_service_client.is_api_enabled('network_load_balancer', 'UpdateNetworkLoadBalancer'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_load_balancer', util.camelize('network_load_balancer'), 'UpdateNetworkLoadBalancer')
    )

    request_containers = testing_service_client.get_requests(service_name='network_load_balancer', api_name='UpdateNetworkLoadBalancer')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_load_balancer.NetworkLoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.update_network_load_balancer(
                network_load_balancer_id=request.pop(util.camelize('networkLoadBalancerId')),
                update_network_load_balancer_details=request.pop(util.camelize('UpdateNetworkLoadBalancerDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_load_balancer',
            'UpdateNetworkLoadBalancer',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_network_load_balancer',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="NLB" opsJiraProject="NLB"
def test_update_network_security_groups(testing_service_client):
    if not testing_service_client.is_api_enabled('network_load_balancer', 'UpdateNetworkSecurityGroups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('network_load_balancer', util.camelize('network_load_balancer'), 'UpdateNetworkSecurityGroups')
    )

    request_containers = testing_service_client.get_requests(service_name='network_load_balancer', api_name='UpdateNetworkSecurityGroups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.network_load_balancer.NetworkLoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.update_network_security_groups(
                network_load_balancer_id=request.pop(util.camelize('networkLoadBalancerId')),
                update_network_security_groups_details=request.pop(util.camelize('UpdateNetworkSecurityGroupsDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'network_load_balancer',
            'UpdateNetworkSecurityGroups',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_network_security_groups',
            False,
            False
        )
