# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

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

    cassette_location = os.path.join('generated', 'core_{name}.yml'.format(name=request.function.__name__))
    with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
        yield


# IssueRoutingInfo tag="computeManagement" email="instance_dev_us_grp@oracle.com" jiraProject="CIM" opsJiraProject="IPA"
def test_attach_load_balancer(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'AttachLoadBalancer'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute_management'), 'AttachLoadBalancer')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='AttachLoadBalancer')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.ComputeManagementClient(config, service_endpoint=service_endpoint)
            response = client.attach_load_balancer(
                instance_pool_id=request.pop(util.camelize('instance_pool_id')),
                attach_load_balancer_details=request.pop(util.camelize('attach_load_balancer_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'AttachLoadBalancer',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'instancePool',
            False,
            False
        )


# IssueRoutingInfo tag="computeManagement" email="instance_dev_us_grp@oracle.com" jiraProject="CIM" opsJiraProject="IPA"
def test_change_instance_configuration_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ChangeInstanceConfigurationCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute_management'), 'ChangeInstanceConfigurationCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ChangeInstanceConfigurationCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.ComputeManagementClient(config, service_endpoint=service_endpoint)
            response = client.change_instance_configuration_compartment(
                instance_configuration_id=request.pop(util.camelize('instance_configuration_id')),
                change_instance_configuration_compartment_details=request.pop(util.camelize('change_instance_configuration_compartment_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ChangeInstanceConfigurationCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_instance_configuration_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="computeManagement" email="instance_dev_us_grp@oracle.com" jiraProject="CIM" opsJiraProject="IPA"
def test_change_instance_pool_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ChangeInstancePoolCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute_management'), 'ChangeInstancePoolCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ChangeInstancePoolCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.ComputeManagementClient(config, service_endpoint=service_endpoint)
            response = client.change_instance_pool_compartment(
                instance_pool_id=request.pop(util.camelize('instance_pool_id')),
                change_instance_pool_compartment_details=request.pop(util.camelize('change_instance_pool_compartment_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ChangeInstancePoolCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_instance_pool_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="computeManagement" email="instance_dev_us_grp@oracle.com" jiraProject="CIM" opsJiraProject="IPA"
def test_create_instance_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CreateInstanceConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute_management'), 'CreateInstanceConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CreateInstanceConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.ComputeManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_instance_configuration(
                create_instance_configuration=request.pop(util.camelize('create_instance_configuration')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CreateInstanceConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'instanceConfiguration',
            False,
            False
        )


# IssueRoutingInfo tag="computeManagement" email="instance_dev_us_grp@oracle.com" jiraProject="CIM" opsJiraProject="IPA"
def test_create_instance_pool(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CreateInstancePool'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute_management'), 'CreateInstancePool')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CreateInstancePool')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.ComputeManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_instance_pool(
                create_instance_pool_details=request.pop(util.camelize('create_instance_pool_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CreateInstancePool',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'instancePool',
            False,
            False
        )


# IssueRoutingInfo tag="computeManagement" email="instance_dev_us_grp@oracle.com" jiraProject="CIM" opsJiraProject="IPA"
def test_delete_instance_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeleteInstanceConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute_management'), 'DeleteInstanceConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeleteInstanceConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.ComputeManagementClient(config, service_endpoint=service_endpoint)
            response = client.delete_instance_configuration(
                instance_configuration_id=request.pop(util.camelize('instance_configuration_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeleteInstanceConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_instance_configuration',
            True,
            False
        )


# IssueRoutingInfo tag="computeManagement" email="instance_dev_us_grp@oracle.com" jiraProject="CIM" opsJiraProject="IPA"
def test_detach_load_balancer(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DetachLoadBalancer'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute_management'), 'DetachLoadBalancer')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DetachLoadBalancer')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.ComputeManagementClient(config, service_endpoint=service_endpoint)
            response = client.detach_load_balancer(
                instance_pool_id=request.pop(util.camelize('instance_pool_id')),
                detach_load_balancer_details=request.pop(util.camelize('detach_load_balancer_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DetachLoadBalancer',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'instancePool',
            False,
            False
        )


# IssueRoutingInfo tag="computeManagement" email="instance_dev_us_grp@oracle.com" jiraProject="CIM" opsJiraProject="IPA"
def test_get_instance_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetInstanceConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute_management'), 'GetInstanceConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetInstanceConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.ComputeManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_instance_configuration(
                instance_configuration_id=request.pop(util.camelize('instance_configuration_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetInstanceConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'instanceConfiguration',
            False,
            False
        )


# IssueRoutingInfo tag="computeManagement" email="instance_dev_us_grp@oracle.com" jiraProject="CIM" opsJiraProject="IPA"
def test_get_instance_pool(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetInstancePool'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute_management'), 'GetInstancePool')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetInstancePool')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.ComputeManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_instance_pool(
                instance_pool_id=request.pop(util.camelize('instance_pool_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetInstancePool',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'instancePool',
            False,
            False
        )


# IssueRoutingInfo tag="computeManagement" email="instance_dev_us_grp@oracle.com" jiraProject="CIM" opsJiraProject="IPA"
def test_launch_instance_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'LaunchInstanceConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute_management'), 'LaunchInstanceConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='LaunchInstanceConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.ComputeManagementClient(config, service_endpoint=service_endpoint)
            response = client.launch_instance_configuration(
                instance_configuration_id=request.pop(util.camelize('instance_configuration_id')),
                instance_configuration=request.pop(util.camelize('instance_configuration')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'LaunchInstanceConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'instance',
            False,
            False
        )


# IssueRoutingInfo tag="computeManagement" email="instance_dev_us_grp@oracle.com" jiraProject="CIM" opsJiraProject="IPA"
def test_list_instance_configurations(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListInstanceConfigurations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute_management'), 'ListInstanceConfigurations')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListInstanceConfigurations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.ComputeManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_instance_configurations(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_instance_configurations(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_instance_configurations(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListInstanceConfigurations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'instanceConfigurationSummary',
            False,
            True
        )


# IssueRoutingInfo tag="computeManagement" email="instance_dev_us_grp@oracle.com" jiraProject="CIM" opsJiraProject="IPA"
def test_list_instance_pool_instances(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListInstancePoolInstances'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute_management'), 'ListInstancePoolInstances')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListInstancePoolInstances')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.ComputeManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_instance_pool_instances(
                compartment_id=request.pop(util.camelize('compartment_id')),
                instance_pool_id=request.pop(util.camelize('instance_pool_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_instance_pool_instances(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    instance_pool_id=request.pop(util.camelize('instance_pool_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_instance_pool_instances(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        instance_pool_id=request.pop(util.camelize('instance_pool_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListInstancePoolInstances',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'instanceSummary',
            False,
            True
        )


# IssueRoutingInfo tag="computeManagement" email="instance_dev_us_grp@oracle.com" jiraProject="CIM" opsJiraProject="IPA"
def test_list_instance_pools(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListInstancePools'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute_management'), 'ListInstancePools')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListInstancePools')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.ComputeManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_instance_pools(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_instance_pools(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_instance_pools(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListInstancePools',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'instancePoolSummary',
            False,
            True
        )


# IssueRoutingInfo tag="computeManagement" email="instance_dev_us_grp@oracle.com" jiraProject="CIM" opsJiraProject="IPA"
def test_reset_instance_pool(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ResetInstancePool'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute_management'), 'ResetInstancePool')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ResetInstancePool')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.ComputeManagementClient(config, service_endpoint=service_endpoint)
            response = client.reset_instance_pool(
                instance_pool_id=request.pop(util.camelize('instance_pool_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ResetInstancePool',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'instancePool',
            False,
            False
        )


# IssueRoutingInfo tag="computeManagement" email="instance_dev_us_grp@oracle.com" jiraProject="CIM" opsJiraProject="IPA"
def test_softreset_instance_pool(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'SoftresetInstancePool'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute_management'), 'SoftresetInstancePool')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='SoftresetInstancePool')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.ComputeManagementClient(config, service_endpoint=service_endpoint)
            response = client.softreset_instance_pool(
                instance_pool_id=request.pop(util.camelize('instance_pool_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'SoftresetInstancePool',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'instancePool',
            False,
            False
        )


# IssueRoutingInfo tag="computeManagement" email="instance_dev_us_grp@oracle.com" jiraProject="CIM" opsJiraProject="IPA"
def test_start_instance_pool(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'StartInstancePool'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute_management'), 'StartInstancePool')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='StartInstancePool')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.ComputeManagementClient(config, service_endpoint=service_endpoint)
            response = client.start_instance_pool(
                instance_pool_id=request.pop(util.camelize('instance_pool_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'StartInstancePool',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'instancePool',
            False,
            False
        )


# IssueRoutingInfo tag="computeManagement" email="instance_dev_us_grp@oracle.com" jiraProject="CIM" opsJiraProject="IPA"
def test_stop_instance_pool(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'StopInstancePool'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute_management'), 'StopInstancePool')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='StopInstancePool')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.ComputeManagementClient(config, service_endpoint=service_endpoint)
            response = client.stop_instance_pool(
                instance_pool_id=request.pop(util.camelize('instance_pool_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'StopInstancePool',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'instancePool',
            False,
            False
        )


# IssueRoutingInfo tag="computeManagement" email="instance_dev_us_grp@oracle.com" jiraProject="CIM" opsJiraProject="IPA"
def test_terminate_instance_pool(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'TerminateInstancePool'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute_management'), 'TerminateInstancePool')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='TerminateInstancePool')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.ComputeManagementClient(config, service_endpoint=service_endpoint)
            response = client.terminate_instance_pool(
                instance_pool_id=request.pop(util.camelize('instance_pool_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'TerminateInstancePool',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'terminate_instance_pool',
            True,
            False
        )


# IssueRoutingInfo tag="computeManagement" email="instance_dev_us_grp@oracle.com" jiraProject="CIM" opsJiraProject="IPA"
def test_update_instance_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateInstanceConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute_management'), 'UpdateInstanceConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateInstanceConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.ComputeManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_instance_configuration(
                instance_configuration_id=request.pop(util.camelize('instance_configuration_id')),
                update_instance_configuration_details=request.pop(util.camelize('update_instance_configuration_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateInstanceConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'instanceConfiguration',
            False,
            False
        )


# IssueRoutingInfo tag="computeManagement" email="instance_dev_us_grp@oracle.com" jiraProject="CIM" opsJiraProject="IPA"
def test_update_instance_pool(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateInstancePool'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute_management'), 'UpdateInstancePool')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateInstancePool')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.ComputeManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_instance_pool(
                instance_pool_id=request.pop(util.camelize('instance_pool_id')),
                update_instance_pool_details=request.pop(util.camelize('update_instance_pool_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateInstancePool',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'instancePool',
            False,
            False
        )
