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

        cassette_location = os.path.join('generated', 'service_mesh_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_change_access_policy_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'ChangeAccessPolicyCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'ChangeAccessPolicyCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='ChangeAccessPolicyCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.change_access_policy_compartment(
                access_policy_id=request.pop(util.camelize('accessPolicyId')),
                change_access_policy_compartment_details=request.pop(util.camelize('ChangeAccessPolicyCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'ChangeAccessPolicyCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_access_policy_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_change_ingress_gateway_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'ChangeIngressGatewayCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'ChangeIngressGatewayCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='ChangeIngressGatewayCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.change_ingress_gateway_compartment(
                ingress_gateway_id=request.pop(util.camelize('ingressGatewayId')),
                change_ingress_gateway_compartment_details=request.pop(util.camelize('ChangeIngressGatewayCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'ChangeIngressGatewayCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_ingress_gateway_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_change_ingress_gateway_route_table_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'ChangeIngressGatewayRouteTableCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'ChangeIngressGatewayRouteTableCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='ChangeIngressGatewayRouteTableCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.change_ingress_gateway_route_table_compartment(
                ingress_gateway_route_table_id=request.pop(util.camelize('ingressGatewayRouteTableId')),
                change_ingress_gateway_route_table_compartment_details=request.pop(util.camelize('ChangeIngressGatewayRouteTableCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'ChangeIngressGatewayRouteTableCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_ingress_gateway_route_table_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_change_mesh_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'ChangeMeshCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'ChangeMeshCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='ChangeMeshCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.change_mesh_compartment(
                mesh_id=request.pop(util.camelize('meshId')),
                change_mesh_compartment_details=request.pop(util.camelize('ChangeMeshCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'ChangeMeshCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_mesh_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_change_virtual_deployment_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'ChangeVirtualDeploymentCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'ChangeVirtualDeploymentCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='ChangeVirtualDeploymentCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.change_virtual_deployment_compartment(
                virtual_deployment_id=request.pop(util.camelize('virtualDeploymentId')),
                change_virtual_deployment_compartment_details=request.pop(util.camelize('ChangeVirtualDeploymentCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'ChangeVirtualDeploymentCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_virtual_deployment_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_change_virtual_service_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'ChangeVirtualServiceCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'ChangeVirtualServiceCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='ChangeVirtualServiceCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.change_virtual_service_compartment(
                virtual_service_id=request.pop(util.camelize('virtualServiceId')),
                change_virtual_service_compartment_details=request.pop(util.camelize('ChangeVirtualServiceCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'ChangeVirtualServiceCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_virtual_service_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_change_virtual_service_route_table_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'ChangeVirtualServiceRouteTableCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'ChangeVirtualServiceRouteTableCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='ChangeVirtualServiceRouteTableCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.change_virtual_service_route_table_compartment(
                virtual_service_route_table_id=request.pop(util.camelize('virtualServiceRouteTableId')),
                change_virtual_service_route_table_compartment_details=request.pop(util.camelize('ChangeVirtualServiceRouteTableCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'ChangeVirtualServiceRouteTableCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_virtual_service_route_table_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_create_access_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'CreateAccessPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'CreateAccessPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='CreateAccessPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.create_access_policy(
                create_access_policy_details=request.pop(util.camelize('CreateAccessPolicyDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'CreateAccessPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'accessPolicy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_create_ingress_gateway(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'CreateIngressGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'CreateIngressGateway')
    )

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='CreateIngressGateway')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.create_ingress_gateway(
                create_ingress_gateway_details=request.pop(util.camelize('CreateIngressGatewayDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'CreateIngressGateway',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'ingressGateway',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_create_ingress_gateway_route_table(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'CreateIngressGatewayRouteTable'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'CreateIngressGatewayRouteTable')
    )

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='CreateIngressGatewayRouteTable')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.create_ingress_gateway_route_table(
                create_ingress_gateway_route_table_details=request.pop(util.camelize('CreateIngressGatewayRouteTableDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'CreateIngressGatewayRouteTable',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'ingressGatewayRouteTable',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_create_mesh(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'CreateMesh'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'CreateMesh')
    )

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='CreateMesh')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.create_mesh(
                create_mesh_details=request.pop(util.camelize('CreateMeshDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'CreateMesh',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mesh',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_create_virtual_deployment(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'CreateVirtualDeployment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'CreateVirtualDeployment')
    )

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='CreateVirtualDeployment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.create_virtual_deployment(
                create_virtual_deployment_details=request.pop(util.camelize('CreateVirtualDeploymentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'CreateVirtualDeployment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'virtualDeployment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_create_virtual_service(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'CreateVirtualService'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'CreateVirtualService')
    )

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='CreateVirtualService')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.create_virtual_service(
                create_virtual_service_details=request.pop(util.camelize('CreateVirtualServiceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'CreateVirtualService',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'virtualService',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_create_virtual_service_route_table(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'CreateVirtualServiceRouteTable'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'CreateVirtualServiceRouteTable')
    )

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='CreateVirtualServiceRouteTable')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.create_virtual_service_route_table(
                create_virtual_service_route_table_details=request.pop(util.camelize('CreateVirtualServiceRouteTableDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'CreateVirtualServiceRouteTable',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'virtualServiceRouteTable',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_delete_access_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'DeleteAccessPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'DeleteAccessPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='DeleteAccessPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.delete_access_policy(
                access_policy_id=request.pop(util.camelize('accessPolicyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'DeleteAccessPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_access_policy',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_delete_ingress_gateway(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'DeleteIngressGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'DeleteIngressGateway')
    )

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='DeleteIngressGateway')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.delete_ingress_gateway(
                ingress_gateway_id=request.pop(util.camelize('ingressGatewayId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'DeleteIngressGateway',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_ingress_gateway',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_delete_ingress_gateway_route_table(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'DeleteIngressGatewayRouteTable'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'DeleteIngressGatewayRouteTable')
    )

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='DeleteIngressGatewayRouteTable')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.delete_ingress_gateway_route_table(
                ingress_gateway_route_table_id=request.pop(util.camelize('ingressGatewayRouteTableId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'DeleteIngressGatewayRouteTable',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_ingress_gateway_route_table',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_delete_mesh(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'DeleteMesh'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'DeleteMesh')
    )

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='DeleteMesh')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.delete_mesh(
                mesh_id=request.pop(util.camelize('meshId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'DeleteMesh',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_mesh',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_delete_virtual_deployment(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'DeleteVirtualDeployment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'DeleteVirtualDeployment')
    )

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='DeleteVirtualDeployment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.delete_virtual_deployment(
                virtual_deployment_id=request.pop(util.camelize('virtualDeploymentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'DeleteVirtualDeployment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_virtual_deployment',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_delete_virtual_service(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'DeleteVirtualService'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'DeleteVirtualService')
    )

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='DeleteVirtualService')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.delete_virtual_service(
                virtual_service_id=request.pop(util.camelize('virtualServiceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'DeleteVirtualService',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_virtual_service',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_delete_virtual_service_route_table(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'DeleteVirtualServiceRouteTable'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'DeleteVirtualServiceRouteTable')
    )

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='DeleteVirtualServiceRouteTable')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.delete_virtual_service_route_table(
                virtual_service_route_table_id=request.pop(util.camelize('virtualServiceRouteTableId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'DeleteVirtualServiceRouteTable',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_virtual_service_route_table',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_get_access_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'GetAccessPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'GetAccessPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='GetAccessPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.get_access_policy(
                access_policy_id=request.pop(util.camelize('accessPolicyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'GetAccessPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'accessPolicy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_get_ingress_gateway(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'GetIngressGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'GetIngressGateway')
    )

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='GetIngressGateway')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.get_ingress_gateway(
                ingress_gateway_id=request.pop(util.camelize('ingressGatewayId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'GetIngressGateway',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'ingressGateway',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_get_ingress_gateway_route_table(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'GetIngressGatewayRouteTable'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'GetIngressGatewayRouteTable')
    )

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='GetIngressGatewayRouteTable')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.get_ingress_gateway_route_table(
                ingress_gateway_route_table_id=request.pop(util.camelize('ingressGatewayRouteTableId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'GetIngressGatewayRouteTable',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'ingressGatewayRouteTable',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_get_mesh(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'GetMesh'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'GetMesh')
    )

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='GetMesh')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.get_mesh(
                mesh_id=request.pop(util.camelize('meshId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'GetMesh',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mesh',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_get_proxy_details(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'GetProxyDetails'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'GetProxyDetails')
    )

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='GetProxyDetails')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.get_proxy_details(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'GetProxyDetails',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'proxyDetails',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_get_virtual_deployment(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'GetVirtualDeployment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'GetVirtualDeployment')
    )

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='GetVirtualDeployment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.get_virtual_deployment(
                virtual_deployment_id=request.pop(util.camelize('virtualDeploymentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'GetVirtualDeployment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'virtualDeployment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_get_virtual_service(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'GetVirtualService'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'GetVirtualService')
    )

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='GetVirtualService')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.get_virtual_service(
                virtual_service_id=request.pop(util.camelize('virtualServiceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'GetVirtualService',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'virtualService',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_get_virtual_service_route_table(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'GetVirtualServiceRouteTable'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'GetVirtualServiceRouteTable')
    )

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='GetVirtualServiceRouteTable')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.get_virtual_service_route_table(
                virtual_service_route_table_id=request.pop(util.camelize('virtualServiceRouteTableId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'GetVirtualServiceRouteTable',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'virtualServiceRouteTable',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_list_access_policies(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'ListAccessPolicies'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'ListAccessPolicies')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='ListAccessPolicies')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.list_access_policies(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_access_policies(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_access_policies(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'ListAccessPolicies',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'accessPolicyCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_list_ingress_gateway_route_tables(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'ListIngressGatewayRouteTables'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'ListIngressGatewayRouteTables')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='ListIngressGatewayRouteTables')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.list_ingress_gateway_route_tables(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_ingress_gateway_route_tables(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_ingress_gateway_route_tables(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'ListIngressGatewayRouteTables',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'ingressGatewayRouteTableCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_list_ingress_gateways(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'ListIngressGateways'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'ListIngressGateways')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='ListIngressGateways')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.list_ingress_gateways(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_ingress_gateways(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_ingress_gateways(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'ListIngressGateways',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'ingressGatewayCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_list_meshes(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'ListMeshes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'ListMeshes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='ListMeshes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.list_meshes(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_meshes(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_meshes(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'ListMeshes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'meshCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_list_virtual_deployments(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'ListVirtualDeployments'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'ListVirtualDeployments')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='ListVirtualDeployments')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.list_virtual_deployments(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_virtual_deployments(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_virtual_deployments(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'ListVirtualDeployments',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'virtualDeploymentCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_list_virtual_service_route_tables(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'ListVirtualServiceRouteTables'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'ListVirtualServiceRouteTables')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='ListVirtualServiceRouteTables')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.list_virtual_service_route_tables(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_virtual_service_route_tables(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_virtual_service_route_tables(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'ListVirtualServiceRouteTables',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'virtualServiceRouteTableCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_list_virtual_services(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'ListVirtualServices'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'ListVirtualServices')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='ListVirtualServices')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.list_virtual_services(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_virtual_services(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_virtual_services(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'ListVirtualServices',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'virtualServiceCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
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
            'service_mesh',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestErrorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
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
            'service_mesh',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
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
            'service_mesh',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_update_access_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'UpdateAccessPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'UpdateAccessPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='UpdateAccessPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.update_access_policy(
                access_policy_id=request.pop(util.camelize('accessPolicyId')),
                update_access_policy_details=request.pop(util.camelize('UpdateAccessPolicyDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'UpdateAccessPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_access_policy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_update_ingress_gateway(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'UpdateIngressGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'UpdateIngressGateway')
    )

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='UpdateIngressGateway')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.update_ingress_gateway(
                ingress_gateway_id=request.pop(util.camelize('ingressGatewayId')),
                update_ingress_gateway_details=request.pop(util.camelize('UpdateIngressGatewayDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'UpdateIngressGateway',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_ingress_gateway',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_update_ingress_gateway_route_table(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'UpdateIngressGatewayRouteTable'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'UpdateIngressGatewayRouteTable')
    )

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='UpdateIngressGatewayRouteTable')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.update_ingress_gateway_route_table(
                ingress_gateway_route_table_id=request.pop(util.camelize('ingressGatewayRouteTableId')),
                update_ingress_gateway_route_table_details=request.pop(util.camelize('UpdateIngressGatewayRouteTableDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'UpdateIngressGatewayRouteTable',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_ingress_gateway_route_table',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_update_mesh(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'UpdateMesh'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'UpdateMesh')
    )

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='UpdateMesh')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.update_mesh(
                mesh_id=request.pop(util.camelize('meshId')),
                update_mesh_details=request.pop(util.camelize('UpdateMeshDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'UpdateMesh',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_mesh',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_update_virtual_deployment(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'UpdateVirtualDeployment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'UpdateVirtualDeployment')
    )

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='UpdateVirtualDeployment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.update_virtual_deployment(
                virtual_deployment_id=request.pop(util.camelize('virtualDeploymentId')),
                update_virtual_deployment_details=request.pop(util.camelize('UpdateVirtualDeploymentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'UpdateVirtualDeployment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_virtual_deployment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_update_virtual_service(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'UpdateVirtualService'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'UpdateVirtualService')
    )

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='UpdateVirtualService')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.update_virtual_service(
                virtual_service_id=request.pop(util.camelize('virtualServiceId')),
                update_virtual_service_details=request.pop(util.camelize('UpdateVirtualServiceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'UpdateVirtualService',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_virtual_service',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_servicemesh_ww_grp@oracle.com" jiraProject="MESH" opsJiraProject="MESH"
def test_update_virtual_service_route_table(testing_service_client):
    if not testing_service_client.is_api_enabled('service_mesh', 'UpdateVirtualServiceRouteTable'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_mesh', util.camelize('service_mesh'), 'UpdateVirtualServiceRouteTable')
    )

    request_containers = testing_service_client.get_requests(service_name='service_mesh', api_name='UpdateVirtualServiceRouteTable')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_mesh.ServiceMeshClient(config, service_endpoint=service_endpoint)
            response = client.update_virtual_service_route_table(
                virtual_service_route_table_id=request.pop(util.camelize('virtualServiceRouteTableId')),
                update_virtual_service_route_table_details=request.pop(util.camelize('UpdateVirtualServiceRouteTableDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_mesh',
            'UpdateVirtualServiceRouteTable',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_virtual_service_route_table',
            False,
            False
        )
