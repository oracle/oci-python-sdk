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


# IssueRoutingInfo tag="serviceGateway" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="SG" opsJiraProject="SGW"
def test_attach_service_id(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'AttachServiceId'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'AttachServiceId')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='AttachServiceId')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.attach_service_id(
                service_gateway_id=request.pop(util.camelize('service_gateway_id')),
                attach_service_details=request.pop(util.camelize('attach_service_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'AttachServiceId',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'serviceGateway',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_bulk_add_virtual_circuit_public_prefixes(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'BulkAddVirtualCircuitPublicPrefixes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'BulkAddVirtualCircuitPublicPrefixes')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='BulkAddVirtualCircuitPublicPrefixes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.bulk_add_virtual_circuit_public_prefixes(
                virtual_circuit_id=request.pop(util.camelize('virtual_circuit_id')),
                bulk_add_virtual_circuit_public_prefixes_details=request.pop(util.camelize('bulk_add_virtual_circuit_public_prefixes_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'BulkAddVirtualCircuitPublicPrefixes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bulk_add_virtual_circuit_public_prefixes',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_bulk_delete_virtual_circuit_public_prefixes(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'BulkDeleteVirtualCircuitPublicPrefixes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'BulkDeleteVirtualCircuitPublicPrefixes')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='BulkDeleteVirtualCircuitPublicPrefixes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.bulk_delete_virtual_circuit_public_prefixes(
                virtual_circuit_id=request.pop(util.camelize('virtual_circuit_id')),
                bulk_delete_virtual_circuit_public_prefixes_details=request.pop(util.camelize('bulk_delete_virtual_circuit_public_prefixes_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'BulkDeleteVirtualCircuitPublicPrefixes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bulk_delete_virtual_circuit_public_prefixes',
            False,
            False
        )


# IssueRoutingInfo tag="pnp" email="elpaso_ops_us_grp@oracle.com" jiraProject="NAT" opsJiraProject="PNP"
def test_change_nat_gateway_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ChangeNatGatewayCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ChangeNatGatewayCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ChangeNatGatewayCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.change_nat_gateway_compartment(
                nat_gateway_id=request.pop(util.camelize('nat_gateway_id')),
                change_nat_gateway_compartment_details=request.pop(util.camelize('change_nat_gateway_compartment_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ChangeNatGatewayCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_nat_gateway_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="serviceGateway" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="SG" opsJiraProject="SGW"
def test_change_service_gateway_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ChangeServiceGatewayCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ChangeServiceGatewayCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ChangeServiceGatewayCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.change_service_gateway_compartment(
                service_gateway_id=request.pop(util.camelize('service_gateway_id')),
                change_service_gateway_compartment_details=request.pop(util.camelize('change_service_gateway_compartment_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ChangeServiceGatewayCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_service_gateway_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_connect_local_peering_gateways(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ConnectLocalPeeringGateways'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ConnectLocalPeeringGateways')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ConnectLocalPeeringGateways')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.connect_local_peering_gateways(
                local_peering_gateway_id=request.pop(util.camelize('local_peering_gateway_id')),
                connect_local_peering_gateways_details=request.pop(util.camelize('connect_local_peering_gateways_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ConnectLocalPeeringGateways',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'connect_local_peering_gateways',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_connect_remote_peering_connections(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ConnectRemotePeeringConnections'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ConnectRemotePeeringConnections')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ConnectRemotePeeringConnections')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.connect_remote_peering_connections(
                remote_peering_connection_id=request.pop(util.camelize('remote_peering_connection_id')),
                connect_remote_peering_connections_details=request.pop(util.camelize('connect_remote_peering_connections_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ConnectRemotePeeringConnections',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'connect_remote_peering_connections',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_create_cpe(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CreateCpe'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'CreateCpe')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CreateCpe')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_cpe(
                create_cpe_details=request.pop(util.camelize('create_cpe_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CreateCpe',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cpe',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_create_cross_connect(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CreateCrossConnect'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'CreateCrossConnect')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CreateCrossConnect')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_cross_connect(
                create_cross_connect_details=request.pop(util.camelize('create_cross_connect_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CreateCrossConnect',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'crossConnect',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_create_cross_connect_group(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CreateCrossConnectGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'CreateCrossConnectGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CreateCrossConnectGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_cross_connect_group(
                create_cross_connect_group_details=request.pop(util.camelize('create_cross_connect_group_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CreateCrossConnectGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'crossConnectGroup',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_create_dhcp_options(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CreateDhcpOptions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'CreateDhcpOptions')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CreateDhcpOptions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_dhcp_options(
                create_dhcp_details=request.pop(util.camelize('create_dhcp_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CreateDhcpOptions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dhcpOptions',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_create_drg(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CreateDrg'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'CreateDrg')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CreateDrg')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_drg(
                create_drg_details=request.pop(util.camelize('create_drg_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CreateDrg',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'drg',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_create_drg_attachment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CreateDrgAttachment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'CreateDrgAttachment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CreateDrgAttachment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_drg_attachment(
                create_drg_attachment_details=request.pop(util.camelize('create_drg_attachment_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CreateDrgAttachment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'drgAttachment',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_create_internet_gateway(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CreateInternetGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'CreateInternetGateway')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CreateInternetGateway')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_internet_gateway(
                create_internet_gateway_details=request.pop(util.camelize('create_internet_gateway_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CreateInternetGateway',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'internetGateway',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_create_ip_sec_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CreateIPSecConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'CreateIPSecConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CreateIPSecConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_ip_sec_connection(
                create_ip_sec_connection_details=request.pop(util.camelize('create_ip_sec_connection_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CreateIPSecConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'iPSecConnection',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_create_local_peering_gateway(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CreateLocalPeeringGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'CreateLocalPeeringGateway')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CreateLocalPeeringGateway')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_local_peering_gateway(
                create_local_peering_gateway_details=request.pop(util.camelize('create_local_peering_gateway_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CreateLocalPeeringGateway',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'localPeeringGateway',
            False,
            False
        )


# IssueRoutingInfo tag="pnp" email="elpaso_ops_us_grp@oracle.com" jiraProject="NAT" opsJiraProject="PNP"
def test_create_nat_gateway(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CreateNatGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'CreateNatGateway')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CreateNatGateway')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_nat_gateway(
                create_nat_gateway_details=request.pop(util.camelize('create_nat_gateway_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CreateNatGateway',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'natGateway',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_create_private_ip(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CreatePrivateIp'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'CreatePrivateIp')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CreatePrivateIp')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_private_ip(
                create_private_ip_details=request.pop(util.camelize('create_private_ip_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CreatePrivateIp',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'privateIp',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_create_public_ip(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CreatePublicIp'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'CreatePublicIp')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CreatePublicIp')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_public_ip(
                create_public_ip_details=request.pop(util.camelize('create_public_ip_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CreatePublicIp',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'publicIp',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_create_remote_peering_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CreateRemotePeeringConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'CreateRemotePeeringConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CreateRemotePeeringConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_remote_peering_connection(
                create_remote_peering_connection_details=request.pop(util.camelize('create_remote_peering_connection_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CreateRemotePeeringConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'remotePeeringConnection',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_create_route_table(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CreateRouteTable'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'CreateRouteTable')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CreateRouteTable')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_route_table(
                create_route_table_details=request.pop(util.camelize('create_route_table_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CreateRouteTable',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'routeTable',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_create_security_list(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CreateSecurityList'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'CreateSecurityList')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CreateSecurityList')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_security_list(
                create_security_list_details=request.pop(util.camelize('create_security_list_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CreateSecurityList',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'securityList',
            False,
            False
        )


# IssueRoutingInfo tag="serviceGateway" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="SG" opsJiraProject="SGW"
def test_create_service_gateway(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CreateServiceGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'CreateServiceGateway')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CreateServiceGateway')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_service_gateway(
                create_service_gateway_details=request.pop(util.camelize('create_service_gateway_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CreateServiceGateway',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'serviceGateway',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_create_subnet(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CreateSubnet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'CreateSubnet')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CreateSubnet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_subnet(
                create_subnet_details=request.pop(util.camelize('create_subnet_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CreateSubnet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'subnet',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_create_vcn(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CreateVcn'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'CreateVcn')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CreateVcn')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_vcn(
                create_vcn_details=request.pop(util.camelize('create_vcn_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CreateVcn',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'vcn',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_create_virtual_circuit(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CreateVirtualCircuit'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'CreateVirtualCircuit')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CreateVirtualCircuit')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_virtual_circuit(
                create_virtual_circuit_details=request.pop(util.camelize('create_virtual_circuit_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CreateVirtualCircuit',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'virtualCircuit',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_delete_cpe(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeleteCpe'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'DeleteCpe')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeleteCpe')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_cpe(
                cpe_id=request.pop(util.camelize('cpe_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeleteCpe',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_cpe',
            True,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_delete_cross_connect(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeleteCrossConnect'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'DeleteCrossConnect')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeleteCrossConnect')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_cross_connect(
                cross_connect_id=request.pop(util.camelize('cross_connect_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeleteCrossConnect',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_cross_connect',
            True,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_delete_cross_connect_group(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeleteCrossConnectGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'DeleteCrossConnectGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeleteCrossConnectGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_cross_connect_group(
                cross_connect_group_id=request.pop(util.camelize('cross_connect_group_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeleteCrossConnectGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_cross_connect_group',
            True,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_delete_dhcp_options(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeleteDhcpOptions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'DeleteDhcpOptions')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeleteDhcpOptions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_dhcp_options(
                dhcp_id=request.pop(util.camelize('dhcp_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeleteDhcpOptions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_dhcp_options',
            True,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_delete_drg(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeleteDrg'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'DeleteDrg')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeleteDrg')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_drg(
                drg_id=request.pop(util.camelize('drg_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeleteDrg',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_drg',
            True,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_delete_drg_attachment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeleteDrgAttachment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'DeleteDrgAttachment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeleteDrgAttachment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_drg_attachment(
                drg_attachment_id=request.pop(util.camelize('drg_attachment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeleteDrgAttachment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_drg_attachment',
            True,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_delete_internet_gateway(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeleteInternetGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'DeleteInternetGateway')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeleteInternetGateway')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_internet_gateway(
                ig_id=request.pop(util.camelize('ig_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeleteInternetGateway',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_internet_gateway',
            True,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_delete_ip_sec_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeleteIPSecConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'DeleteIPSecConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeleteIPSecConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_ip_sec_connection(
                ipsc_id=request.pop(util.camelize('ipsc_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeleteIPSecConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_ip_sec_connection',
            True,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_delete_local_peering_gateway(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeleteLocalPeeringGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'DeleteLocalPeeringGateway')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeleteLocalPeeringGateway')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_local_peering_gateway(
                local_peering_gateway_id=request.pop(util.camelize('local_peering_gateway_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeleteLocalPeeringGateway',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_local_peering_gateway',
            True,
            False
        )


# IssueRoutingInfo tag="pnp" email="elpaso_ops_us_grp@oracle.com" jiraProject="NAT" opsJiraProject="PNP"
def test_delete_nat_gateway(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeleteNatGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'DeleteNatGateway')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeleteNatGateway')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_nat_gateway(
                nat_gateway_id=request.pop(util.camelize('nat_gateway_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeleteNatGateway',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_nat_gateway',
            True,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_delete_private_ip(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeletePrivateIp'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'DeletePrivateIp')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeletePrivateIp')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_private_ip(
                private_ip_id=request.pop(util.camelize('private_ip_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeletePrivateIp',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_private_ip',
            True,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_delete_public_ip(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeletePublicIp'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'DeletePublicIp')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeletePublicIp')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_public_ip(
                public_ip_id=request.pop(util.camelize('public_ip_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeletePublicIp',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_public_ip',
            True,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_delete_remote_peering_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeleteRemotePeeringConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'DeleteRemotePeeringConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeleteRemotePeeringConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_remote_peering_connection(
                remote_peering_connection_id=request.pop(util.camelize('remote_peering_connection_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeleteRemotePeeringConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_remote_peering_connection',
            True,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_delete_route_table(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeleteRouteTable'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'DeleteRouteTable')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeleteRouteTable')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_route_table(
                rt_id=request.pop(util.camelize('rt_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeleteRouteTable',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_route_table',
            True,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_delete_security_list(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeleteSecurityList'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'DeleteSecurityList')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeleteSecurityList')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_security_list(
                security_list_id=request.pop(util.camelize('security_list_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeleteSecurityList',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_security_list',
            True,
            False
        )


# IssueRoutingInfo tag="serviceGateway" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="SG" opsJiraProject="SGW"
def test_delete_service_gateway(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeleteServiceGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'DeleteServiceGateway')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeleteServiceGateway')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_service_gateway(
                service_gateway_id=request.pop(util.camelize('service_gateway_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeleteServiceGateway',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_service_gateway',
            True,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_delete_subnet(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeleteSubnet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'DeleteSubnet')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeleteSubnet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_subnet(
                subnet_id=request.pop(util.camelize('subnet_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeleteSubnet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_subnet',
            True,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_delete_vcn(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeleteVcn'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'DeleteVcn')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeleteVcn')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_vcn(
                vcn_id=request.pop(util.camelize('vcn_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeleteVcn',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_vcn',
            True,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_delete_virtual_circuit(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeleteVirtualCircuit'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'DeleteVirtualCircuit')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeleteVirtualCircuit')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_virtual_circuit(
                virtual_circuit_id=request.pop(util.camelize('virtual_circuit_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeleteVirtualCircuit',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_virtual_circuit',
            True,
            False
        )


# IssueRoutingInfo tag="serviceGateway" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="SG" opsJiraProject="SGW"
def test_detach_service_id(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DetachServiceId'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'DetachServiceId')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DetachServiceId')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.detach_service_id(
                service_gateway_id=request.pop(util.camelize('service_gateway_id')),
                detach_service_details=request.pop(util.camelize('detach_service_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DetachServiceId',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'serviceGateway',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_get_cpe(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetCpe'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'GetCpe')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetCpe')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_cpe(
                cpe_id=request.pop(util.camelize('cpe_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetCpe',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cpe',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_get_cross_connect(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetCrossConnect'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'GetCrossConnect')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetCrossConnect')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_cross_connect(
                cross_connect_id=request.pop(util.camelize('cross_connect_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetCrossConnect',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'crossConnect',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_get_cross_connect_group(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetCrossConnectGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'GetCrossConnectGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetCrossConnectGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_cross_connect_group(
                cross_connect_group_id=request.pop(util.camelize('cross_connect_group_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetCrossConnectGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'crossConnectGroup',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_get_cross_connect_letter_of_authority(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetCrossConnectLetterOfAuthority'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'GetCrossConnectLetterOfAuthority')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetCrossConnectLetterOfAuthority')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_cross_connect_letter_of_authority(
                cross_connect_id=request.pop(util.camelize('cross_connect_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetCrossConnectLetterOfAuthority',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'letterOfAuthority',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_get_cross_connect_status(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetCrossConnectStatus'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'GetCrossConnectStatus')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetCrossConnectStatus')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_cross_connect_status(
                cross_connect_id=request.pop(util.camelize('cross_connect_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetCrossConnectStatus',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'crossConnectStatus',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_get_dhcp_options(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetDhcpOptions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'GetDhcpOptions')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetDhcpOptions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_dhcp_options(
                dhcp_id=request.pop(util.camelize('dhcp_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetDhcpOptions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dhcpOptions',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_get_drg(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetDrg'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'GetDrg')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetDrg')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_drg(
                drg_id=request.pop(util.camelize('drg_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetDrg',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'drg',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_get_drg_attachment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetDrgAttachment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'GetDrgAttachment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetDrgAttachment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_drg_attachment(
                drg_attachment_id=request.pop(util.camelize('drg_attachment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetDrgAttachment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'drgAttachment',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_get_fast_connect_provider_service(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetFastConnectProviderService'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'GetFastConnectProviderService')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetFastConnectProviderService')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_fast_connect_provider_service(
                provider_service_id=request.pop(util.camelize('provider_service_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetFastConnectProviderService',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fastConnectProviderService',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_get_fast_connect_provider_service_key(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetFastConnectProviderServiceKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'GetFastConnectProviderServiceKey')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetFastConnectProviderServiceKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_fast_connect_provider_service_key(
                provider_service_id=request.pop(util.camelize('provider_service_id')),
                provider_service_key_name=request.pop(util.camelize('provider_service_key_name')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetFastConnectProviderServiceKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fastConnectProviderServiceKey',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_get_internet_gateway(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetInternetGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'GetInternetGateway')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetInternetGateway')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_internet_gateway(
                ig_id=request.pop(util.camelize('ig_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetInternetGateway',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'internetGateway',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_get_ip_sec_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetIPSecConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'GetIPSecConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetIPSecConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_ip_sec_connection(
                ipsc_id=request.pop(util.camelize('ipsc_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetIPSecConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'iPSecConnection',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_get_ip_sec_connection_device_config(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetIPSecConnectionDeviceConfig'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'GetIPSecConnectionDeviceConfig')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetIPSecConnectionDeviceConfig')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_ip_sec_connection_device_config(
                ipsc_id=request.pop(util.camelize('ipsc_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetIPSecConnectionDeviceConfig',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'iPSecConnectionDeviceConfig',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_get_ip_sec_connection_device_status(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetIPSecConnectionDeviceStatus'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'GetIPSecConnectionDeviceStatus')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetIPSecConnectionDeviceStatus')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_ip_sec_connection_device_status(
                ipsc_id=request.pop(util.camelize('ipsc_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetIPSecConnectionDeviceStatus',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'iPSecConnectionDeviceStatus',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_get_ip_sec_connection_tunnel(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetIPSecConnectionTunnel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'GetIPSecConnectionTunnel')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetIPSecConnectionTunnel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_ip_sec_connection_tunnel(
                ipsc_id=request.pop(util.camelize('ipsc_id')),
                tunnel_id=request.pop(util.camelize('tunnel_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetIPSecConnectionTunnel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'iPSecConnectionTunnel',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_get_ip_sec_connection_tunnel_shared_secret(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetIPSecConnectionTunnelSharedSecret'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'GetIPSecConnectionTunnelSharedSecret')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetIPSecConnectionTunnelSharedSecret')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_ip_sec_connection_tunnel_shared_secret(
                ipsc_id=request.pop(util.camelize('ipsc_id')),
                tunnel_id=request.pop(util.camelize('tunnel_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetIPSecConnectionTunnelSharedSecret',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'iPSecConnectionTunnelSharedSecret',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_get_local_peering_gateway(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetLocalPeeringGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'GetLocalPeeringGateway')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetLocalPeeringGateway')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_local_peering_gateway(
                local_peering_gateway_id=request.pop(util.camelize('local_peering_gateway_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetLocalPeeringGateway',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'localPeeringGateway',
            False,
            False
        )


# IssueRoutingInfo tag="pnp" email="elpaso_ops_us_grp@oracle.com" jiraProject="NAT" opsJiraProject="PNP"
def test_get_nat_gateway(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetNatGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'GetNatGateway')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetNatGateway')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_nat_gateway(
                nat_gateway_id=request.pop(util.camelize('nat_gateway_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetNatGateway',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'natGateway',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_get_private_ip(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetPrivateIp'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'GetPrivateIp')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetPrivateIp')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_private_ip(
                private_ip_id=request.pop(util.camelize('private_ip_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetPrivateIp',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'privateIp',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_get_public_ip(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetPublicIp'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'GetPublicIp')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetPublicIp')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_public_ip(
                public_ip_id=request.pop(util.camelize('public_ip_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetPublicIp',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'publicIp',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_get_public_ip_by_ip_address(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetPublicIpByIpAddress'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'GetPublicIpByIpAddress')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetPublicIpByIpAddress')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_public_ip_by_ip_address(
                get_public_ip_by_ip_address_details=request.pop(util.camelize('get_public_ip_by_ip_address_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetPublicIpByIpAddress',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'publicIp',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_get_public_ip_by_private_ip_id(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetPublicIpByPrivateIpId'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'GetPublicIpByPrivateIpId')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetPublicIpByPrivateIpId')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_public_ip_by_private_ip_id(
                get_public_ip_by_private_ip_id_details=request.pop(util.camelize('get_public_ip_by_private_ip_id_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetPublicIpByPrivateIpId',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'publicIp',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_get_remote_peering_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetRemotePeeringConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'GetRemotePeeringConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetRemotePeeringConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_remote_peering_connection(
                remote_peering_connection_id=request.pop(util.camelize('remote_peering_connection_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetRemotePeeringConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'remotePeeringConnection',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_get_route_table(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetRouteTable'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'GetRouteTable')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetRouteTable')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_route_table(
                rt_id=request.pop(util.camelize('rt_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetRouteTable',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'routeTable',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_get_security_list(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetSecurityList'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'GetSecurityList')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetSecurityList')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_security_list(
                security_list_id=request.pop(util.camelize('security_list_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetSecurityList',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'securityList',
            False,
            False
        )


# IssueRoutingInfo tag="serviceGateway" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="SG" opsJiraProject="SGW"
def test_get_service(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetService'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'GetService')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetService')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_service(
                service_id=request.pop(util.camelize('service_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetService',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'service',
            False,
            False
        )


# IssueRoutingInfo tag="serviceGateway" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="SG" opsJiraProject="SGW"
def test_get_service_gateway(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetServiceGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'GetServiceGateway')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetServiceGateway')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_service_gateway(
                service_gateway_id=request.pop(util.camelize('service_gateway_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetServiceGateway',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'serviceGateway',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_get_subnet(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetSubnet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'GetSubnet')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetSubnet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_subnet(
                subnet_id=request.pop(util.camelize('subnet_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetSubnet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'subnet',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_get_vcn(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetVcn'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'GetVcn')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetVcn')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_vcn(
                vcn_id=request.pop(util.camelize('vcn_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetVcn',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'vcn',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_get_virtual_circuit(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetVirtualCircuit'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'GetVirtualCircuit')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetVirtualCircuit')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_virtual_circuit(
                virtual_circuit_id=request.pop(util.camelize('virtual_circuit_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetVirtualCircuit',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'virtualCircuit',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_get_vnic(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetVnic'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'GetVnic')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetVnic')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_vnic(
                vnic_id=request.pop(util.camelize('vnic_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetVnic',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'vnic',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_list_allowed_peer_regions_for_remote_peering(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListAllowedPeerRegionsForRemotePeering'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ListAllowedPeerRegionsForRemotePeering')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListAllowedPeerRegionsForRemotePeering')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_allowed_peer_regions_for_remote_peering(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListAllowedPeerRegionsForRemotePeering',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'peerRegionForRemotePeering',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_list_cpes(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListCpes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ListCpes')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListCpes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_cpes(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_cpes(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_cpes(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListCpes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cpe',
            False,
            True
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_list_cross_connect_groups(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListCrossConnectGroups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ListCrossConnectGroups')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListCrossConnectGroups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_cross_connect_groups(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_cross_connect_groups(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_cross_connect_groups(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListCrossConnectGroups',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'crossConnectGroup',
            False,
            True
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_list_cross_connect_locations(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListCrossConnectLocations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ListCrossConnectLocations')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListCrossConnectLocations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_cross_connect_locations(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_cross_connect_locations(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_cross_connect_locations(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListCrossConnectLocations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'crossConnectLocation',
            False,
            True
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_list_cross_connects(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListCrossConnects'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ListCrossConnects')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListCrossConnects')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_cross_connects(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_cross_connects(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_cross_connects(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListCrossConnects',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'crossConnect',
            False,
            True
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_list_crossconnect_port_speed_shapes(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListCrossconnectPortSpeedShapes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ListCrossconnectPortSpeedShapes')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListCrossconnectPortSpeedShapes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_crossconnect_port_speed_shapes(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_crossconnect_port_speed_shapes(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_crossconnect_port_speed_shapes(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListCrossconnectPortSpeedShapes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'crossConnectPortSpeedShape',
            False,
            True
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_list_dhcp_options(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListDhcpOptions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ListDhcpOptions')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListDhcpOptions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_dhcp_options(
                compartment_id=request.pop(util.camelize('compartment_id')),
                vcn_id=request.pop(util.camelize('vcn_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_dhcp_options(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    vcn_id=request.pop(util.camelize('vcn_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_dhcp_options(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        vcn_id=request.pop(util.camelize('vcn_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListDhcpOptions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dhcpOptions',
            False,
            True
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_list_drg_attachments(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListDrgAttachments'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ListDrgAttachments')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListDrgAttachments')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_drg_attachments(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_drg_attachments(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_drg_attachments(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListDrgAttachments',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'drgAttachment',
            False,
            True
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_list_drgs(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListDrgs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ListDrgs')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListDrgs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_drgs(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_drgs(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_drgs(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListDrgs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'drg',
            False,
            True
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_list_fast_connect_provider_services(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListFastConnectProviderServices'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ListFastConnectProviderServices')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListFastConnectProviderServices')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_fast_connect_provider_services(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_fast_connect_provider_services(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_fast_connect_provider_services(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListFastConnectProviderServices',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fastConnectProviderService',
            False,
            True
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_list_fast_connect_provider_virtual_circuit_bandwidth_shapes(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListFastConnectProviderVirtualCircuitBandwidthShapes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ListFastConnectProviderVirtualCircuitBandwidthShapes')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListFastConnectProviderVirtualCircuitBandwidthShapes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_fast_connect_provider_virtual_circuit_bandwidth_shapes(
                provider_service_id=request.pop(util.camelize('provider_service_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_fast_connect_provider_virtual_circuit_bandwidth_shapes(
                    provider_service_id=request.pop(util.camelize('provider_service_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_fast_connect_provider_virtual_circuit_bandwidth_shapes(
                        provider_service_id=request.pop(util.camelize('provider_service_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListFastConnectProviderVirtualCircuitBandwidthShapes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'virtualCircuitBandwidthShape',
            False,
            True
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_list_internet_gateways(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListInternetGateways'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ListInternetGateways')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListInternetGateways')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_internet_gateways(
                compartment_id=request.pop(util.camelize('compartment_id')),
                vcn_id=request.pop(util.camelize('vcn_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_internet_gateways(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    vcn_id=request.pop(util.camelize('vcn_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_internet_gateways(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        vcn_id=request.pop(util.camelize('vcn_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListInternetGateways',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'internetGateway',
            False,
            True
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_list_ip_sec_connection_tunnels(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListIPSecConnectionTunnels'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ListIPSecConnectionTunnels')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListIPSecConnectionTunnels')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_ip_sec_connection_tunnels(
                ipsc_id=request.pop(util.camelize('ipsc_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_ip_sec_connection_tunnels(
                    ipsc_id=request.pop(util.camelize('ipsc_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_ip_sec_connection_tunnels(
                        ipsc_id=request.pop(util.camelize('ipsc_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListIPSecConnectionTunnels',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'iPSecConnectionTunnel',
            False,
            True
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_list_ip_sec_connections(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListIPSecConnections'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ListIPSecConnections')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListIPSecConnections')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_ip_sec_connections(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_ip_sec_connections(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_ip_sec_connections(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListIPSecConnections',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'iPSecConnection',
            False,
            True
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_list_local_peering_gateways(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListLocalPeeringGateways'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ListLocalPeeringGateways')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListLocalPeeringGateways')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_local_peering_gateways(
                compartment_id=request.pop(util.camelize('compartment_id')),
                vcn_id=request.pop(util.camelize('vcn_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_local_peering_gateways(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    vcn_id=request.pop(util.camelize('vcn_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_local_peering_gateways(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        vcn_id=request.pop(util.camelize('vcn_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListLocalPeeringGateways',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'localPeeringGateway',
            False,
            True
        )


# IssueRoutingInfo tag="pnp" email="elpaso_ops_us_grp@oracle.com" jiraProject="NAT" opsJiraProject="PNP"
def test_list_nat_gateways(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListNatGateways'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ListNatGateways')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListNatGateways')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_nat_gateways(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_nat_gateways(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_nat_gateways(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListNatGateways',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'natGateway',
            False,
            True
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_list_private_ips(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListPrivateIps'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ListPrivateIps')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListPrivateIps')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_private_ips(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_private_ips(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_private_ips(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListPrivateIps',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'privateIp',
            False,
            True
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_list_public_ips(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListPublicIps'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ListPublicIps')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListPublicIps')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_public_ips(
                scope=request.pop(util.camelize('scope')),
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_public_ips(
                    scope=request.pop(util.camelize('scope')),
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_public_ips(
                        scope=request.pop(util.camelize('scope')),
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListPublicIps',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'publicIp',
            False,
            True
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_list_remote_peering_connections(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListRemotePeeringConnections'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ListRemotePeeringConnections')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListRemotePeeringConnections')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_remote_peering_connections(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_remote_peering_connections(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_remote_peering_connections(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListRemotePeeringConnections',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'remotePeeringConnection',
            False,
            True
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_list_route_tables(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListRouteTables'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ListRouteTables')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListRouteTables')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_route_tables(
                compartment_id=request.pop(util.camelize('compartment_id')),
                vcn_id=request.pop(util.camelize('vcn_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_route_tables(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    vcn_id=request.pop(util.camelize('vcn_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_route_tables(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        vcn_id=request.pop(util.camelize('vcn_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListRouteTables',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'routeTable',
            False,
            True
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_list_security_lists(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListSecurityLists'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ListSecurityLists')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListSecurityLists')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_security_lists(
                compartment_id=request.pop(util.camelize('compartment_id')),
                vcn_id=request.pop(util.camelize('vcn_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_security_lists(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    vcn_id=request.pop(util.camelize('vcn_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_security_lists(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        vcn_id=request.pop(util.camelize('vcn_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListSecurityLists',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'securityList',
            False,
            True
        )


# IssueRoutingInfo tag="serviceGateway" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="SG" opsJiraProject="SGW"
def test_list_service_gateways(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListServiceGateways'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ListServiceGateways')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListServiceGateways')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_service_gateways(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_service_gateways(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_service_gateways(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListServiceGateways',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'serviceGateway',
            False,
            True
        )


# IssueRoutingInfo tag="serviceGateway" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="SG" opsJiraProject="SGW"
def test_list_services(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListServices'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ListServices')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListServices')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_services(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_services(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_services(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListServices',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'service',
            False,
            True
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_list_subnets(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListSubnets'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ListSubnets')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListSubnets')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_subnets(
                compartment_id=request.pop(util.camelize('compartment_id')),
                vcn_id=request.pop(util.camelize('vcn_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_subnets(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    vcn_id=request.pop(util.camelize('vcn_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_subnets(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        vcn_id=request.pop(util.camelize('vcn_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListSubnets',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'subnet',
            False,
            True
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_list_vcns(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListVcns'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ListVcns')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListVcns')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_vcns(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_vcns(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_vcns(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListVcns',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'vcn',
            False,
            True
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_list_virtual_circuit_bandwidth_shapes(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListVirtualCircuitBandwidthShapes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ListVirtualCircuitBandwidthShapes')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListVirtualCircuitBandwidthShapes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_virtual_circuit_bandwidth_shapes(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_virtual_circuit_bandwidth_shapes(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_virtual_circuit_bandwidth_shapes(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListVirtualCircuitBandwidthShapes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'virtualCircuitBandwidthShape',
            False,
            True
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_list_virtual_circuit_public_prefixes(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListVirtualCircuitPublicPrefixes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ListVirtualCircuitPublicPrefixes')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListVirtualCircuitPublicPrefixes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_virtual_circuit_public_prefixes(
                virtual_circuit_id=request.pop(util.camelize('virtual_circuit_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListVirtualCircuitPublicPrefixes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'virtualCircuitPublicPrefix',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_list_virtual_circuits(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListVirtualCircuits'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ListVirtualCircuits')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListVirtualCircuits')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_virtual_circuits(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_virtual_circuits(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_virtual_circuits(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListVirtualCircuits',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'virtualCircuit',
            False,
            True
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_update_cpe(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateCpe'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'UpdateCpe')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateCpe')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_cpe(
                cpe_id=request.pop(util.camelize('cpe_id')),
                update_cpe_details=request.pop(util.camelize('update_cpe_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateCpe',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cpe',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_update_cross_connect(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateCrossConnect'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'UpdateCrossConnect')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateCrossConnect')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_cross_connect(
                cross_connect_id=request.pop(util.camelize('cross_connect_id')),
                update_cross_connect_details=request.pop(util.camelize('update_cross_connect_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateCrossConnect',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'crossConnect',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_update_cross_connect_group(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateCrossConnectGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'UpdateCrossConnectGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateCrossConnectGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_cross_connect_group(
                cross_connect_group_id=request.pop(util.camelize('cross_connect_group_id')),
                update_cross_connect_group_details=request.pop(util.camelize('update_cross_connect_group_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateCrossConnectGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'crossConnectGroup',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_update_dhcp_options(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateDhcpOptions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'UpdateDhcpOptions')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateDhcpOptions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_dhcp_options(
                dhcp_id=request.pop(util.camelize('dhcp_id')),
                update_dhcp_details=request.pop(util.camelize('update_dhcp_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateDhcpOptions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dhcpOptions',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_update_drg(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateDrg'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'UpdateDrg')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateDrg')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_drg(
                drg_id=request.pop(util.camelize('drg_id')),
                update_drg_details=request.pop(util.camelize('update_drg_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateDrg',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'drg',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_update_drg_attachment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateDrgAttachment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'UpdateDrgAttachment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateDrgAttachment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_drg_attachment(
                drg_attachment_id=request.pop(util.camelize('drg_attachment_id')),
                update_drg_attachment_details=request.pop(util.camelize('update_drg_attachment_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateDrgAttachment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'drgAttachment',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_update_internet_gateway(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateInternetGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'UpdateInternetGateway')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateInternetGateway')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_internet_gateway(
                ig_id=request.pop(util.camelize('ig_id')),
                update_internet_gateway_details=request.pop(util.camelize('update_internet_gateway_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateInternetGateway',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'internetGateway',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_update_ip_sec_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateIPSecConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'UpdateIPSecConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateIPSecConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_ip_sec_connection(
                ipsc_id=request.pop(util.camelize('ipsc_id')),
                update_ip_sec_connection_details=request.pop(util.camelize('update_ip_sec_connection_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateIPSecConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'iPSecConnection',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_update_ip_sec_connection_tunnel(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateIPSecConnectionTunnel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'UpdateIPSecConnectionTunnel')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateIPSecConnectionTunnel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_ip_sec_connection_tunnel(
                ipsc_id=request.pop(util.camelize('ipsc_id')),
                tunnel_id=request.pop(util.camelize('tunnel_id')),
                update_ip_sec_connection_tunnel_details=request.pop(util.camelize('update_ip_sec_connection_tunnel_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateIPSecConnectionTunnel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'iPSecConnectionTunnel',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_update_ip_sec_connection_tunnel_shared_secret(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateIPSecConnectionTunnelSharedSecret'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'UpdateIPSecConnectionTunnelSharedSecret')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateIPSecConnectionTunnelSharedSecret')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_ip_sec_connection_tunnel_shared_secret(
                ipsc_id=request.pop(util.camelize('ipsc_id')),
                tunnel_id=request.pop(util.camelize('tunnel_id')),
                update_ip_sec_connection_tunnel_shared_secret_details=request.pop(util.camelize('update_ip_sec_connection_tunnel_shared_secret_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateIPSecConnectionTunnelSharedSecret',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'iPSecConnectionTunnelSharedSecret',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_update_local_peering_gateway(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateLocalPeeringGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'UpdateLocalPeeringGateway')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateLocalPeeringGateway')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_local_peering_gateway(
                local_peering_gateway_id=request.pop(util.camelize('local_peering_gateway_id')),
                update_local_peering_gateway_details=request.pop(util.camelize('update_local_peering_gateway_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateLocalPeeringGateway',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'localPeeringGateway',
            False,
            False
        )


# IssueRoutingInfo tag="pnp" email="elpaso_ops_us_grp@oracle.com" jiraProject="NAT" opsJiraProject="PNP"
def test_update_nat_gateway(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateNatGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'UpdateNatGateway')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateNatGateway')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_nat_gateway(
                nat_gateway_id=request.pop(util.camelize('nat_gateway_id')),
                update_nat_gateway_details=request.pop(util.camelize('update_nat_gateway_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateNatGateway',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'natGateway',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_update_private_ip(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdatePrivateIp'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'UpdatePrivateIp')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdatePrivateIp')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_private_ip(
                private_ip_id=request.pop(util.camelize('private_ip_id')),
                update_private_ip_details=request.pop(util.camelize('update_private_ip_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdatePrivateIp',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'privateIp',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_update_public_ip(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdatePublicIp'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'UpdatePublicIp')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdatePublicIp')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_public_ip(
                public_ip_id=request.pop(util.camelize('public_ip_id')),
                update_public_ip_details=request.pop(util.camelize('update_public_ip_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdatePublicIp',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'publicIp',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_update_remote_peering_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateRemotePeeringConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'UpdateRemotePeeringConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateRemotePeeringConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_remote_peering_connection(
                remote_peering_connection_id=request.pop(util.camelize('remote_peering_connection_id')),
                update_remote_peering_connection_details=request.pop(util.camelize('update_remote_peering_connection_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateRemotePeeringConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'remotePeeringConnection',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_update_route_table(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateRouteTable'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'UpdateRouteTable')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateRouteTable')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_route_table(
                rt_id=request.pop(util.camelize('rt_id')),
                update_route_table_details=request.pop(util.camelize('update_route_table_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateRouteTable',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'routeTable',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_update_security_list(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateSecurityList'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'UpdateSecurityList')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateSecurityList')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_security_list(
                security_list_id=request.pop(util.camelize('security_list_id')),
                update_security_list_details=request.pop(util.camelize('update_security_list_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateSecurityList',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'securityList',
            False,
            False
        )


# IssueRoutingInfo tag="serviceGateway" email="oci_sgw_ops_us_grp@oracle.com" jiraProject="SG" opsJiraProject="SGW"
def test_update_service_gateway(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateServiceGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'UpdateServiceGateway')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateServiceGateway')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_service_gateway(
                service_gateway_id=request.pop(util.camelize('service_gateway_id')),
                update_service_gateway_details=request.pop(util.camelize('update_service_gateway_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateServiceGateway',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'serviceGateway',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_update_subnet(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateSubnet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'UpdateSubnet')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateSubnet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_subnet(
                subnet_id=request.pop(util.camelize('subnet_id')),
                update_subnet_details=request.pop(util.camelize('update_subnet_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateSubnet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'subnet',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_update_vcn(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateVcn'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'UpdateVcn')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateVcn')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_vcn(
                vcn_id=request.pop(util.camelize('vcn_id')),
                update_vcn_details=request.pop(util.camelize('update_vcn_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateVcn',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'vcn',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_update_virtual_circuit(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateVirtualCircuit'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'UpdateVirtualCircuit')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateVirtualCircuit')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_virtual_circuit(
                virtual_circuit_id=request.pop(util.camelize('virtual_circuit_id')),
                update_virtual_circuit_details=request.pop(util.camelize('update_virtual_circuit_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateVirtualCircuit',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'virtualCircuit',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_update_vnic(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateVnic'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'UpdateVnic')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateVnic')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_vnic(
                vnic_id=request.pop(util.camelize('vnic_id')),
                update_vnic_details=request.pop(util.camelize('update_vnic_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateVnic',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'vnic',
            False,
            False
        )
