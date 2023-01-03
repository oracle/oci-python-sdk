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

        cassette_location = os.path.join('generated', 'load_balancer_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_change_load_balancer_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'ChangeLoadBalancerCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'ChangeLoadBalancerCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='ChangeLoadBalancerCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.change_load_balancer_compartment(
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                change_load_balancer_compartment_details=request.pop(util.camelize('ChangeLoadBalancerCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'ChangeLoadBalancerCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_load_balancer_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_create_backend(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'CreateBackend'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'CreateBackend')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='CreateBackend')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.create_backend(
                create_backend_details=request.pop(util.camelize('CreateBackendDetails')),
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                backend_set_name=request.pop(util.camelize('backendSetName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'CreateBackend',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_backend',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_create_backend_set(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'CreateBackendSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'CreateBackendSet')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='CreateBackendSet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.create_backend_set(
                create_backend_set_details=request.pop(util.camelize('CreateBackendSetDetails')),
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'CreateBackendSet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_backend_set',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_create_certificate(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'CreateCertificate'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'CreateCertificate')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='CreateCertificate')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.create_certificate(
                create_certificate_details=request.pop(util.camelize('CreateCertificateDetails')),
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'CreateCertificate',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_certificate',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_create_hostname(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'CreateHostname'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'CreateHostname')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='CreateHostname')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.create_hostname(
                create_hostname_details=request.pop(util.camelize('CreateHostnameDetails')),
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'CreateHostname',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_hostname',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_create_listener(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'CreateListener'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'CreateListener')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='CreateListener')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.create_listener(
                create_listener_details=request.pop(util.camelize('CreateListenerDetails')),
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'CreateListener',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_listener',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_create_load_balancer(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'CreateLoadBalancer'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'CreateLoadBalancer')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='CreateLoadBalancer')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.create_load_balancer(
                create_load_balancer_details=request.pop(util.camelize('CreateLoadBalancerDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'CreateLoadBalancer',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_load_balancer',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_create_path_route_set(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'CreatePathRouteSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'CreatePathRouteSet')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='CreatePathRouteSet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.create_path_route_set(
                create_path_route_set_details=request.pop(util.camelize('CreatePathRouteSetDetails')),
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'CreatePathRouteSet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_path_route_set',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_create_routing_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'CreateRoutingPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'CreateRoutingPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='CreateRoutingPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.create_routing_policy(
                create_routing_policy_details=request.pop(util.camelize('CreateRoutingPolicyDetails')),
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'CreateRoutingPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_routing_policy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_create_rule_set(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'CreateRuleSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'CreateRuleSet')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='CreateRuleSet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.create_rule_set(
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                create_rule_set_details=request.pop(util.camelize('CreateRuleSetDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'CreateRuleSet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_rule_set',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_create_ssl_cipher_suite(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'CreateSSLCipherSuite'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'CreateSSLCipherSuite')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='CreateSSLCipherSuite')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.create_ssl_cipher_suite(
                create_ssl_cipher_suite_details=request.pop(util.camelize('CreateSSLCipherSuiteDetails')),
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'CreateSSLCipherSuite',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_ssl_cipher_suite',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_delete_backend(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'DeleteBackend'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'DeleteBackend')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='DeleteBackend')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.delete_backend(
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                backend_set_name=request.pop(util.camelize('backendSetName')),
                backend_name=request.pop(util.camelize('backendName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'DeleteBackend',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_backend',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_delete_backend_set(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'DeleteBackendSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'DeleteBackendSet')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='DeleteBackendSet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.delete_backend_set(
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                backend_set_name=request.pop(util.camelize('backendSetName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'DeleteBackendSet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_backend_set',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_delete_certificate(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'DeleteCertificate'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'DeleteCertificate')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='DeleteCertificate')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.delete_certificate(
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                certificate_name=request.pop(util.camelize('certificateName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'DeleteCertificate',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_certificate',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_delete_hostname(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'DeleteHostname'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'DeleteHostname')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='DeleteHostname')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.delete_hostname(
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                name=request.pop(util.camelize('name')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'DeleteHostname',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_hostname',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_delete_listener(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'DeleteListener'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'DeleteListener')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='DeleteListener')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.delete_listener(
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                listener_name=request.pop(util.camelize('listenerName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'DeleteListener',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_listener',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_delete_load_balancer(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'DeleteLoadBalancer'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'DeleteLoadBalancer')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='DeleteLoadBalancer')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.delete_load_balancer(
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'DeleteLoadBalancer',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_load_balancer',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_delete_path_route_set(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'DeletePathRouteSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'DeletePathRouteSet')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='DeletePathRouteSet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.delete_path_route_set(
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                path_route_set_name=request.pop(util.camelize('pathRouteSetName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'DeletePathRouteSet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_path_route_set',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_delete_routing_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'DeleteRoutingPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'DeleteRoutingPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='DeleteRoutingPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.delete_routing_policy(
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                routing_policy_name=request.pop(util.camelize('routingPolicyName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'DeleteRoutingPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_routing_policy',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_delete_rule_set(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'DeleteRuleSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'DeleteRuleSet')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='DeleteRuleSet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.delete_rule_set(
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                rule_set_name=request.pop(util.camelize('ruleSetName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'DeleteRuleSet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_rule_set',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_delete_ssl_cipher_suite(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'DeleteSSLCipherSuite'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'DeleteSSLCipherSuite')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='DeleteSSLCipherSuite')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.delete_ssl_cipher_suite(
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                name=request.pop(util.camelize('name')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'DeleteSSLCipherSuite',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_ssl_cipher_suite',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_get_backend(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'GetBackend'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'GetBackend')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='GetBackend')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.get_backend(
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                backend_set_name=request.pop(util.camelize('backendSetName')),
                backend_name=request.pop(util.camelize('backendName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'GetBackend',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'backend',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_get_backend_health(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'GetBackendHealth'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'GetBackendHealth')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='GetBackendHealth')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.get_backend_health(
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                backend_set_name=request.pop(util.camelize('backendSetName')),
                backend_name=request.pop(util.camelize('backendName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'GetBackendHealth',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'backendHealth',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_get_backend_set(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'GetBackendSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'GetBackendSet')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='GetBackendSet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.get_backend_set(
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                backend_set_name=request.pop(util.camelize('backendSetName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'GetBackendSet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'backendSet',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_get_backend_set_health(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'GetBackendSetHealth'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'GetBackendSetHealth')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='GetBackendSetHealth')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.get_backend_set_health(
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                backend_set_name=request.pop(util.camelize('backendSetName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'GetBackendSetHealth',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'backendSetHealth',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_get_health_checker(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'GetHealthChecker'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'GetHealthChecker')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='GetHealthChecker')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.get_health_checker(
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                backend_set_name=request.pop(util.camelize('backendSetName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'GetHealthChecker',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'healthChecker',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_get_hostname(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'GetHostname'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'GetHostname')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='GetHostname')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.get_hostname(
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                name=request.pop(util.camelize('name')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'GetHostname',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'hostname',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_get_load_balancer(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'GetLoadBalancer'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'GetLoadBalancer')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='GetLoadBalancer')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.get_load_balancer(
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'GetLoadBalancer',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'loadBalancer',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_get_load_balancer_health(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'GetLoadBalancerHealth'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'GetLoadBalancerHealth')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='GetLoadBalancerHealth')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.get_load_balancer_health(
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'GetLoadBalancerHealth',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'loadBalancerHealth',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_get_path_route_set(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'GetPathRouteSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'GetPathRouteSet')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='GetPathRouteSet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.get_path_route_set(
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                path_route_set_name=request.pop(util.camelize('pathRouteSetName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'GetPathRouteSet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'pathRouteSet',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_get_routing_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'GetRoutingPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'GetRoutingPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='GetRoutingPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.get_routing_policy(
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                routing_policy_name=request.pop(util.camelize('routingPolicyName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'GetRoutingPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'routingPolicy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_get_rule_set(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'GetRuleSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'GetRuleSet')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='GetRuleSet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.get_rule_set(
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                rule_set_name=request.pop(util.camelize('ruleSetName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'GetRuleSet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'ruleSet',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_get_ssl_cipher_suite(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'GetSSLCipherSuite'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'GetSSLCipherSuite')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='GetSSLCipherSuite')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.get_ssl_cipher_suite(
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                name=request.pop(util.camelize('name')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'GetSSLCipherSuite',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sSLCipherSuite',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_list_backend_sets(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'ListBackendSets'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'ListBackendSets')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='ListBackendSets')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.list_backend_sets(
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'ListBackendSets',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'backendSet',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_list_backends(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'ListBackends'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'ListBackends')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='ListBackends')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.list_backends(
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                backend_set_name=request.pop(util.camelize('backendSetName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'ListBackends',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'backend',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_list_certificates(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'ListCertificates'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'ListCertificates')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='ListCertificates')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.list_certificates(
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'ListCertificates',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'certificate',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_list_hostnames(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'ListHostnames'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'ListHostnames')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='ListHostnames')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.list_hostnames(
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'ListHostnames',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'hostname',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_list_listener_rules(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'ListListenerRules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'ListListenerRules')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='ListListenerRules')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.list_listener_rules(
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                listener_name=request.pop(util.camelize('listenerName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'ListListenerRules',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'listenerRuleSummary',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_list_load_balancer_healths(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'ListLoadBalancerHealths'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'ListLoadBalancerHealths')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='ListLoadBalancerHealths')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.list_load_balancer_healths(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_load_balancer_healths(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_load_balancer_healths(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'ListLoadBalancerHealths',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'loadBalancerHealthSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_list_load_balancers(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'ListLoadBalancers'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'ListLoadBalancers')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='ListLoadBalancers')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.list_load_balancers(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_load_balancers(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_load_balancers(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'ListLoadBalancers',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'loadBalancer',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_list_path_route_sets(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'ListPathRouteSets'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'ListPathRouteSets')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='ListPathRouteSets')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.list_path_route_sets(
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'ListPathRouteSets',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'pathRouteSet',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_list_policies(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'ListPolicies'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'ListPolicies')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='ListPolicies')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.list_policies(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_policies(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_policies(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'ListPolicies',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'loadBalancerPolicy',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_list_protocols(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'ListProtocols'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'ListProtocols')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='ListProtocols')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.list_protocols(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_protocols(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_protocols(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'ListProtocols',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'loadBalancerProtocol',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_list_routing_policies(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'ListRoutingPolicies'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'ListRoutingPolicies')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='ListRoutingPolicies')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.list_routing_policies(
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_routing_policies(
                    load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_routing_policies(
                        load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'ListRoutingPolicies',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'routingPolicy',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_list_rule_sets(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'ListRuleSets'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'ListRuleSets')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='ListRuleSets')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.list_rule_sets(
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'ListRuleSets',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'ruleSet',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_list_shapes(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'ListShapes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'ListShapes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='ListShapes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.list_shapes(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_shapes(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_shapes(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'ListShapes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'loadBalancerShape',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_list_ssl_cipher_suites(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'ListSSLCipherSuites'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'ListSSLCipherSuites')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='ListSSLCipherSuites')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.list_ssl_cipher_suites(
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'ListSSLCipherSuites',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sSLCipherSuite',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.list_work_requests(
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_requests(
                    load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_requests(
                        load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_update_backend(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'UpdateBackend'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'UpdateBackend')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='UpdateBackend')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.update_backend(
                update_backend_details=request.pop(util.camelize('UpdateBackendDetails')),
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                backend_set_name=request.pop(util.camelize('backendSetName')),
                backend_name=request.pop(util.camelize('backendName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'UpdateBackend',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_backend',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_update_backend_set(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'UpdateBackendSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'UpdateBackendSet')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='UpdateBackendSet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.update_backend_set(
                update_backend_set_details=request.pop(util.camelize('UpdateBackendSetDetails')),
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                backend_set_name=request.pop(util.camelize('backendSetName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'UpdateBackendSet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_backend_set',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_update_health_checker(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'UpdateHealthChecker'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'UpdateHealthChecker')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='UpdateHealthChecker')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.update_health_checker(
                health_checker=request.pop(util.camelize('HealthChecker')),
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                backend_set_name=request.pop(util.camelize('backendSetName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'UpdateHealthChecker',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_health_checker',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_update_hostname(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'UpdateHostname'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'UpdateHostname')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='UpdateHostname')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.update_hostname(
                update_hostname_details=request.pop(util.camelize('UpdateHostnameDetails')),
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                name=request.pop(util.camelize('name')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'UpdateHostname',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_hostname',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_update_listener(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'UpdateListener'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'UpdateListener')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='UpdateListener')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.update_listener(
                update_listener_details=request.pop(util.camelize('UpdateListenerDetails')),
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                listener_name=request.pop(util.camelize('listenerName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'UpdateListener',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_listener',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_update_load_balancer(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'UpdateLoadBalancer'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'UpdateLoadBalancer')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='UpdateLoadBalancer')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.update_load_balancer(
                update_load_balancer_details=request.pop(util.camelize('UpdateLoadBalancerDetails')),
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'UpdateLoadBalancer',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_load_balancer',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_update_load_balancer_shape(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'UpdateLoadBalancerShape'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'UpdateLoadBalancerShape')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='UpdateLoadBalancerShape')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.update_load_balancer_shape(
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                update_load_balancer_shape_details=request.pop(util.camelize('UpdateLoadBalancerShapeDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'UpdateLoadBalancerShape',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_load_balancer_shape',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_update_network_security_groups(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'UpdateNetworkSecurityGroups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'UpdateNetworkSecurityGroups')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='UpdateNetworkSecurityGroups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.update_network_security_groups(
                update_network_security_groups_details=request.pop(util.camelize('UpdateNetworkSecurityGroupsDetails')),
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'UpdateNetworkSecurityGroups',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_network_security_groups',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_update_path_route_set(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'UpdatePathRouteSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'UpdatePathRouteSet')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='UpdatePathRouteSet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.update_path_route_set(
                update_path_route_set_details=request.pop(util.camelize('UpdatePathRouteSetDetails')),
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                path_route_set_name=request.pop(util.camelize('pathRouteSetName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'UpdatePathRouteSet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_path_route_set',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_update_routing_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'UpdateRoutingPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'UpdateRoutingPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='UpdateRoutingPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.update_routing_policy(
                update_routing_policy_details=request.pop(util.camelize('UpdateRoutingPolicyDetails')),
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                routing_policy_name=request.pop(util.camelize('routingPolicyName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'UpdateRoutingPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_routing_policy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_update_rule_set(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'UpdateRuleSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'UpdateRuleSet')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='UpdateRuleSet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.update_rule_set(
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                rule_set_name=request.pop(util.camelize('ruleSetName')),
                update_rule_set_details=request.pop(util.camelize('UpdateRuleSetDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'UpdateRuleSet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_rule_set',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_lbaas_dev_us_grp@oracle.com" jiraProject="LBCP" opsJiraProject="LBCP"
def test_update_ssl_cipher_suite(testing_service_client):
    if not testing_service_client.is_api_enabled('load_balancer', 'UpdateSSLCipherSuite'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('load_balancer', util.camelize('load_balancer'), 'UpdateSSLCipherSuite')
    )

    request_containers = testing_service_client.get_requests(service_name='load_balancer', api_name='UpdateSSLCipherSuite')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.load_balancer.LoadBalancerClient(config, service_endpoint=service_endpoint)
            response = client.update_ssl_cipher_suite(
                update_ssl_cipher_suite_details=request.pop(util.camelize('UpdateSSLCipherSuiteDetails')),
                load_balancer_id=request.pop(util.camelize('loadBalancerId')),
                name=request.pop(util.camelize('name')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'load_balancer',
            'UpdateSSLCipherSuite',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_ssl_cipher_suite',
            False,
            False
        )
