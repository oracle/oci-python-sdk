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

        cassette_location = os.path.join('generated', 'core_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_add_network_security_group_security_rules(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'AddNetworkSecurityGroupSecurityRules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'AddNetworkSecurityGroupSecurityRules')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='AddNetworkSecurityGroupSecurityRules')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.add_network_security_group_security_rules(
                network_security_group_id=request.pop(util.camelize('networkSecurityGroupId')),
                add_network_security_group_security_rules_details=request.pop(util.camelize('AddNetworkSecurityGroupSecurityRulesDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'AddNetworkSecurityGroupSecurityRules',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'addedNetworkSecurityGroupSecurityRules',
            False,
            False
        )


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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.attach_service_id(
                service_gateway_id=request.pop(util.camelize('serviceGatewayId')),
                attach_service_details=request.pop(util.camelize('AttachServiceDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.bulk_add_virtual_circuit_public_prefixes(
                virtual_circuit_id=request.pop(util.camelize('virtualCircuitId')),
                bulk_add_virtual_circuit_public_prefixes_details=request.pop(util.camelize('BulkAddVirtualCircuitPublicPrefixesDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.bulk_delete_virtual_circuit_public_prefixes(
                virtual_circuit_id=request.pop(util.camelize('virtualCircuitId')),
                bulk_delete_virtual_circuit_public_prefixes_details=request.pop(util.camelize('BulkDeleteVirtualCircuitPublicPrefixesDetails')),
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


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_change_cpe_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ChangeCpeCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ChangeCpeCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ChangeCpeCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.change_cpe_compartment(
                cpe_id=request.pop(util.camelize('cpeId')),
                change_cpe_compartment_details=request.pop(util.camelize('ChangeCpeCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ChangeCpeCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_cpe_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_change_cross_connect_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ChangeCrossConnectCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ChangeCrossConnectCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ChangeCrossConnectCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.change_cross_connect_compartment(
                cross_connect_id=request.pop(util.camelize('crossConnectId')),
                change_cross_connect_compartment_details=request.pop(util.camelize('ChangeCrossConnectCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ChangeCrossConnectCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_cross_connect_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_change_cross_connect_group_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ChangeCrossConnectGroupCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ChangeCrossConnectGroupCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ChangeCrossConnectGroupCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.change_cross_connect_group_compartment(
                cross_connect_group_id=request.pop(util.camelize('crossConnectGroupId')),
                change_cross_connect_group_compartment_details=request.pop(util.camelize('ChangeCrossConnectGroupCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ChangeCrossConnectGroupCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_cross_connect_group_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_change_dhcp_options_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ChangeDhcpOptionsCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ChangeDhcpOptionsCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ChangeDhcpOptionsCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.change_dhcp_options_compartment(
                dhcp_id=request.pop(util.camelize('dhcpId')),
                change_dhcp_options_compartment_details=request.pop(util.camelize('ChangeDhcpOptionsCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ChangeDhcpOptionsCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_dhcp_options_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_change_drg_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ChangeDrgCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ChangeDrgCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ChangeDrgCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.change_drg_compartment(
                drg_id=request.pop(util.camelize('drgId')),
                change_drg_compartment_details=request.pop(util.camelize('ChangeDrgCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ChangeDrgCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_drg_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_change_internet_gateway_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ChangeInternetGatewayCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ChangeInternetGatewayCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ChangeInternetGatewayCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.change_internet_gateway_compartment(
                ig_id=request.pop(util.camelize('igId')),
                change_internet_gateway_compartment_details=request.pop(util.camelize('ChangeInternetGatewayCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ChangeInternetGatewayCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_internet_gateway_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_change_ip_sec_connection_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ChangeIPSecConnectionCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ChangeIPSecConnectionCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ChangeIPSecConnectionCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.change_ip_sec_connection_compartment(
                ipsc_id=request.pop(util.camelize('ipscId')),
                change_ip_sec_connection_compartment_details=request.pop(util.camelize('ChangeIPSecConnectionCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ChangeIPSecConnectionCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_ip_sec_connection_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_change_local_peering_gateway_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ChangeLocalPeeringGatewayCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ChangeLocalPeeringGatewayCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ChangeLocalPeeringGatewayCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.change_local_peering_gateway_compartment(
                local_peering_gateway_id=request.pop(util.camelize('localPeeringGatewayId')),
                change_local_peering_gateway_compartment_details=request.pop(util.camelize('ChangeLocalPeeringGatewayCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ChangeLocalPeeringGatewayCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_local_peering_gateway_compartment',
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.change_nat_gateway_compartment(
                nat_gateway_id=request.pop(util.camelize('natGatewayId')),
                change_nat_gateway_compartment_details=request.pop(util.camelize('ChangeNatGatewayCompartmentDetails')),
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


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_change_network_security_group_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ChangeNetworkSecurityGroupCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ChangeNetworkSecurityGroupCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ChangeNetworkSecurityGroupCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.change_network_security_group_compartment(
                network_security_group_id=request.pop(util.camelize('networkSecurityGroupId')),
                change_network_security_group_compartment_details=request.pop(util.camelize('ChangeNetworkSecurityGroupCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ChangeNetworkSecurityGroupCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_network_security_group_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_change_public_ip_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ChangePublicIpCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ChangePublicIpCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ChangePublicIpCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.change_public_ip_compartment(
                public_ip_id=request.pop(util.camelize('publicIpId')),
                change_public_ip_compartment_details=request.pop(util.camelize('ChangePublicIpCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ChangePublicIpCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_public_ip_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_change_remote_peering_connection_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ChangeRemotePeeringConnectionCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ChangeRemotePeeringConnectionCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ChangeRemotePeeringConnectionCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.change_remote_peering_connection_compartment(
                remote_peering_connection_id=request.pop(util.camelize('remotePeeringConnectionId')),
                change_remote_peering_connection_compartment_details=request.pop(util.camelize('ChangeRemotePeeringConnectionCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ChangeRemotePeeringConnectionCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_remote_peering_connection_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_change_route_table_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ChangeRouteTableCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ChangeRouteTableCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ChangeRouteTableCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.change_route_table_compartment(
                rt_id=request.pop(util.camelize('rtId')),
                change_route_table_compartment_details=request.pop(util.camelize('ChangeRouteTableCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ChangeRouteTableCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_route_table_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_change_security_list_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ChangeSecurityListCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ChangeSecurityListCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ChangeSecurityListCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.change_security_list_compartment(
                security_list_id=request.pop(util.camelize('securityListId')),
                change_security_list_compartment_details=request.pop(util.camelize('ChangeSecurityListCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ChangeSecurityListCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_security_list_compartment',
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.change_service_gateway_compartment(
                service_gateway_id=request.pop(util.camelize('serviceGatewayId')),
                change_service_gateway_compartment_details=request.pop(util.camelize('ChangeServiceGatewayCompartmentDetails')),
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
def test_change_subnet_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ChangeSubnetCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ChangeSubnetCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ChangeSubnetCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.change_subnet_compartment(
                subnet_id=request.pop(util.camelize('subnetId')),
                change_subnet_compartment_details=request.pop(util.camelize('ChangeSubnetCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ChangeSubnetCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_subnet_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_change_vcn_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ChangeVcnCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ChangeVcnCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ChangeVcnCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.change_vcn_compartment(
                vcn_id=request.pop(util.camelize('vcnId')),
                change_vcn_compartment_details=request.pop(util.camelize('ChangeVcnCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ChangeVcnCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_vcn_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="c3" email="c3_scrum_team_us_grp@oracle.com" jiraProject="RSC" opsJiraProject="RSC"
def test_change_virtual_circuit_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ChangeVirtualCircuitCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ChangeVirtualCircuitCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ChangeVirtualCircuitCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.change_virtual_circuit_compartment(
                virtual_circuit_id=request.pop(util.camelize('virtualCircuitId')),
                change_virtual_circuit_compartment_details=request.pop(util.camelize('ChangeVirtualCircuitCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ChangeVirtualCircuitCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_virtual_circuit_compartment',
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.connect_local_peering_gateways(
                local_peering_gateway_id=request.pop(util.camelize('localPeeringGatewayId')),
                connect_local_peering_gateways_details=request.pop(util.camelize('ConnectLocalPeeringGatewaysDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.connect_remote_peering_connections(
                remote_peering_connection_id=request.pop(util.camelize('remotePeeringConnectionId')),
                connect_remote_peering_connections_details=request.pop(util.camelize('ConnectRemotePeeringConnectionsDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_cpe(
                create_cpe_details=request.pop(util.camelize('CreateCpeDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_cross_connect(
                create_cross_connect_details=request.pop(util.camelize('CreateCrossConnectDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_cross_connect_group(
                create_cross_connect_group_details=request.pop(util.camelize('CreateCrossConnectGroupDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_dhcp_options(
                create_dhcp_details=request.pop(util.camelize('CreateDhcpDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_drg(
                create_drg_details=request.pop(util.camelize('CreateDrgDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_drg_attachment(
                create_drg_attachment_details=request.pop(util.camelize('CreateDrgAttachmentDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_internet_gateway(
                create_internet_gateway_details=request.pop(util.camelize('CreateInternetGatewayDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_ip_sec_connection(
                create_ip_sec_connection_details=request.pop(util.camelize('CreateIPSecConnectionDetails')),
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
def test_create_ipv6(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CreateIpv6'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'CreateIpv6')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CreateIpv6')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_ipv6(
                create_ipv6_details=request.pop(util.camelize('CreateIpv6Details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CreateIpv6',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'ipv6',
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_local_peering_gateway(
                create_local_peering_gateway_details=request.pop(util.camelize('CreateLocalPeeringGatewayDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_nat_gateway(
                create_nat_gateway_details=request.pop(util.camelize('CreateNatGatewayDetails')),
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
def test_create_network_security_group(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CreateNetworkSecurityGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'CreateNetworkSecurityGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CreateNetworkSecurityGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_network_security_group(
                create_network_security_group_details=request.pop(util.camelize('CreateNetworkSecurityGroupDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CreateNetworkSecurityGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'networkSecurityGroup',
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_private_ip(
                create_private_ip_details=request.pop(util.camelize('CreatePrivateIpDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_public_ip(
                create_public_ip_details=request.pop(util.camelize('CreatePublicIpDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_remote_peering_connection(
                create_remote_peering_connection_details=request.pop(util.camelize('CreateRemotePeeringConnectionDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_route_table(
                create_route_table_details=request.pop(util.camelize('CreateRouteTableDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_security_list(
                create_security_list_details=request.pop(util.camelize('CreateSecurityListDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_service_gateway(
                create_service_gateway_details=request.pop(util.camelize('CreateServiceGatewayDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_subnet(
                create_subnet_details=request.pop(util.camelize('CreateSubnetDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_vcn(
                create_vcn_details=request.pop(util.camelize('CreateVcnDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.create_virtual_circuit(
                create_virtual_circuit_details=request.pop(util.camelize('CreateVirtualCircuitDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_cpe(
                cpe_id=request.pop(util.camelize('cpeId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_cross_connect(
                cross_connect_id=request.pop(util.camelize('crossConnectId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_cross_connect_group(
                cross_connect_group_id=request.pop(util.camelize('crossConnectGroupId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_dhcp_options(
                dhcp_id=request.pop(util.camelize('dhcpId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_drg(
                drg_id=request.pop(util.camelize('drgId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_drg_attachment(
                drg_attachment_id=request.pop(util.camelize('drgAttachmentId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_internet_gateway(
                ig_id=request.pop(util.camelize('igId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_ip_sec_connection(
                ipsc_id=request.pop(util.camelize('ipscId')),
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
def test_delete_ipv6(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeleteIpv6'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'DeleteIpv6')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeleteIpv6')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_ipv6(
                ipv6_id=request.pop(util.camelize('ipv6Id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeleteIpv6',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_ipv6',
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_local_peering_gateway(
                local_peering_gateway_id=request.pop(util.camelize('localPeeringGatewayId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_nat_gateway(
                nat_gateway_id=request.pop(util.camelize('natGatewayId')),
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
def test_delete_network_security_group(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeleteNetworkSecurityGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'DeleteNetworkSecurityGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeleteNetworkSecurityGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_network_security_group(
                network_security_group_id=request.pop(util.camelize('networkSecurityGroupId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeleteNetworkSecurityGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_network_security_group',
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_private_ip(
                private_ip_id=request.pop(util.camelize('privateIpId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_public_ip(
                public_ip_id=request.pop(util.camelize('publicIpId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_remote_peering_connection(
                remote_peering_connection_id=request.pop(util.camelize('remotePeeringConnectionId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_route_table(
                rt_id=request.pop(util.camelize('rtId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_security_list(
                security_list_id=request.pop(util.camelize('securityListId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_service_gateway(
                service_gateway_id=request.pop(util.camelize('serviceGatewayId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_subnet(
                subnet_id=request.pop(util.camelize('subnetId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_vcn(
                vcn_id=request.pop(util.camelize('vcnId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.delete_virtual_circuit(
                virtual_circuit_id=request.pop(util.camelize('virtualCircuitId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.detach_service_id(
                service_gateway_id=request.pop(util.camelize('serviceGatewayId')),
                detach_service_details=request.pop(util.camelize('DetachServiceDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_cpe(
                cpe_id=request.pop(util.camelize('cpeId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_cross_connect(
                cross_connect_id=request.pop(util.camelize('crossConnectId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_cross_connect_group(
                cross_connect_group_id=request.pop(util.camelize('crossConnectGroupId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_cross_connect_letter_of_authority(
                cross_connect_id=request.pop(util.camelize('crossConnectId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_cross_connect_status(
                cross_connect_id=request.pop(util.camelize('crossConnectId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_dhcp_options(
                dhcp_id=request.pop(util.camelize('dhcpId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_drg(
                drg_id=request.pop(util.camelize('drgId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_drg_attachment(
                drg_attachment_id=request.pop(util.camelize('drgAttachmentId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_fast_connect_provider_service(
                provider_service_id=request.pop(util.camelize('providerServiceId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_fast_connect_provider_service_key(
                provider_service_id=request.pop(util.camelize('providerServiceId')),
                provider_service_key_name=request.pop(util.camelize('providerServiceKeyName')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_internet_gateway(
                ig_id=request.pop(util.camelize('igId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_ip_sec_connection(
                ipsc_id=request.pop(util.camelize('ipscId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_ip_sec_connection_device_config(
                ipsc_id=request.pop(util.camelize('ipscId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_ip_sec_connection_device_status(
                ipsc_id=request.pop(util.camelize('ipscId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_ip_sec_connection_tunnel(
                ipsc_id=request.pop(util.camelize('ipscId')),
                tunnel_id=request.pop(util.camelize('tunnelId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_ip_sec_connection_tunnel_shared_secret(
                ipsc_id=request.pop(util.camelize('ipscId')),
                tunnel_id=request.pop(util.camelize('tunnelId')),
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
def test_get_ipv6(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetIpv6'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'GetIpv6')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetIpv6')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_ipv6(
                ipv6_id=request.pop(util.camelize('ipv6Id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetIpv6',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'ipv6',
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_local_peering_gateway(
                local_peering_gateway_id=request.pop(util.camelize('localPeeringGatewayId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_nat_gateway(
                nat_gateway_id=request.pop(util.camelize('natGatewayId')),
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
def test_get_network_security_group(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetNetworkSecurityGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'GetNetworkSecurityGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetNetworkSecurityGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_network_security_group(
                network_security_group_id=request.pop(util.camelize('networkSecurityGroupId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetNetworkSecurityGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'networkSecurityGroup',
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_private_ip(
                private_ip_id=request.pop(util.camelize('privateIpId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_public_ip(
                public_ip_id=request.pop(util.camelize('publicIpId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_public_ip_by_ip_address(
                get_public_ip_by_ip_address_details=request.pop(util.camelize('GetPublicIpByIpAddressDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_public_ip_by_private_ip_id(
                get_public_ip_by_private_ip_id_details=request.pop(util.camelize('GetPublicIpByPrivateIpIdDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_remote_peering_connection(
                remote_peering_connection_id=request.pop(util.camelize('remotePeeringConnectionId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_route_table(
                rt_id=request.pop(util.camelize('rtId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_security_list(
                security_list_id=request.pop(util.camelize('securityListId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_service(
                service_id=request.pop(util.camelize('serviceId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_service_gateway(
                service_gateway_id=request.pop(util.camelize('serviceGatewayId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_subnet(
                subnet_id=request.pop(util.camelize('subnetId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_vcn(
                vcn_id=request.pop(util.camelize('vcnId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_virtual_circuit(
                virtual_circuit_id=request.pop(util.camelize('virtualCircuitId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.get_vnic(
                vnic_id=request.pop(util.camelize('vnicId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
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
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListCpes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_cpes(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_cpes(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_cpes(
                        compartment_id=request.pop(util.camelize('compartmentId')),
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
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListCrossConnectGroups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_cross_connect_groups(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_cross_connect_groups(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_cross_connect_groups(
                        compartment_id=request.pop(util.camelize('compartmentId')),
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
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListCrossConnectLocations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_cross_connect_locations(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_cross_connect_locations(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_cross_connect_locations(
                        compartment_id=request.pop(util.camelize('compartmentId')),
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
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListCrossConnects')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_cross_connects(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_cross_connects(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_cross_connects(
                        compartment_id=request.pop(util.camelize('compartmentId')),
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
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListCrossconnectPortSpeedShapes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_crossconnect_port_speed_shapes(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_crossconnect_port_speed_shapes(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_crossconnect_port_speed_shapes(
                        compartment_id=request.pop(util.camelize('compartmentId')),
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
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListDhcpOptions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_dhcp_options(
                compartment_id=request.pop(util.camelize('compartmentId')),
                vcn_id=request.pop(util.camelize('vcnId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_dhcp_options(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    vcn_id=request.pop(util.camelize('vcnId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_dhcp_options(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        vcn_id=request.pop(util.camelize('vcnId')),
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
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListDrgAttachments')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_drg_attachments(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_drg_attachments(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_drg_attachments(
                        compartment_id=request.pop(util.camelize('compartmentId')),
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
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListDrgs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_drgs(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_drgs(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_drgs(
                        compartment_id=request.pop(util.camelize('compartmentId')),
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
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListFastConnectProviderServices')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_fast_connect_provider_services(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_fast_connect_provider_services(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_fast_connect_provider_services(
                        compartment_id=request.pop(util.camelize('compartmentId')),
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
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListFastConnectProviderVirtualCircuitBandwidthShapes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_fast_connect_provider_virtual_circuit_bandwidth_shapes(
                provider_service_id=request.pop(util.camelize('providerServiceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_fast_connect_provider_virtual_circuit_bandwidth_shapes(
                    provider_service_id=request.pop(util.camelize('providerServiceId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_fast_connect_provider_virtual_circuit_bandwidth_shapes(
                        provider_service_id=request.pop(util.camelize('providerServiceId')),
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
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListInternetGateways')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_internet_gateways(
                compartment_id=request.pop(util.camelize('compartmentId')),
                vcn_id=request.pop(util.camelize('vcnId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_internet_gateways(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    vcn_id=request.pop(util.camelize('vcnId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_internet_gateways(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        vcn_id=request.pop(util.camelize('vcnId')),
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
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListIPSecConnectionTunnels')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_ip_sec_connection_tunnels(
                ipsc_id=request.pop(util.camelize('ipscId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_ip_sec_connection_tunnels(
                    ipsc_id=request.pop(util.camelize('ipscId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_ip_sec_connection_tunnels(
                        ipsc_id=request.pop(util.camelize('ipscId')),
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
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListIPSecConnections')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_ip_sec_connections(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_ip_sec_connections(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_ip_sec_connections(
                        compartment_id=request.pop(util.camelize('compartmentId')),
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
def test_list_ipv6s(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListIpv6s'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ListIpv6s')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListIpv6s')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_ipv6s(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_ipv6s(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_ipv6s(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListIpv6s',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'ipv6',
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
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListLocalPeeringGateways')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_local_peering_gateways(
                compartment_id=request.pop(util.camelize('compartmentId')),
                vcn_id=request.pop(util.camelize('vcnId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_local_peering_gateways(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    vcn_id=request.pop(util.camelize('vcnId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_local_peering_gateways(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        vcn_id=request.pop(util.camelize('vcnId')),
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
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListNatGateways')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_nat_gateways(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_nat_gateways(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_nat_gateways(
                        compartment_id=request.pop(util.camelize('compartmentId')),
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
def test_list_network_security_group_security_rules(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListNetworkSecurityGroupSecurityRules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ListNetworkSecurityGroupSecurityRules')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListNetworkSecurityGroupSecurityRules')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_network_security_group_security_rules(
                network_security_group_id=request.pop(util.camelize('networkSecurityGroupId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_network_security_group_security_rules(
                    network_security_group_id=request.pop(util.camelize('networkSecurityGroupId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_network_security_group_security_rules(
                        network_security_group_id=request.pop(util.camelize('networkSecurityGroupId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListNetworkSecurityGroupSecurityRules',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'securityRule',
            False,
            True
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_list_network_security_group_vnics(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListNetworkSecurityGroupVnics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ListNetworkSecurityGroupVnics')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListNetworkSecurityGroupVnics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_network_security_group_vnics(
                network_security_group_id=request.pop(util.camelize('networkSecurityGroupId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_network_security_group_vnics(
                    network_security_group_id=request.pop(util.camelize('networkSecurityGroupId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_network_security_group_vnics(
                        network_security_group_id=request.pop(util.camelize('networkSecurityGroupId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListNetworkSecurityGroupVnics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'networkSecurityGroupVnic',
            False,
            True
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_list_network_security_groups(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListNetworkSecurityGroups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'ListNetworkSecurityGroups')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListNetworkSecurityGroups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_network_security_groups(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_network_security_groups(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_network_security_groups(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListNetworkSecurityGroups',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'networkSecurityGroup',
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
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListPrivateIps')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_private_ips(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
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
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListPublicIps')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_public_ips(
                scope=request.pop(util.camelize('scope')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_public_ips(
                    scope=request.pop(util.camelize('scope')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_public_ips(
                        scope=request.pop(util.camelize('scope')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
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
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListRemotePeeringConnections')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_remote_peering_connections(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_remote_peering_connections(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_remote_peering_connections(
                        compartment_id=request.pop(util.camelize('compartmentId')),
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
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListRouteTables')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_route_tables(
                compartment_id=request.pop(util.camelize('compartmentId')),
                vcn_id=request.pop(util.camelize('vcnId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_route_tables(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    vcn_id=request.pop(util.camelize('vcnId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_route_tables(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        vcn_id=request.pop(util.camelize('vcnId')),
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
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListSecurityLists')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_security_lists(
                compartment_id=request.pop(util.camelize('compartmentId')),
                vcn_id=request.pop(util.camelize('vcnId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_security_lists(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    vcn_id=request.pop(util.camelize('vcnId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_security_lists(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        vcn_id=request.pop(util.camelize('vcnId')),
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
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListServiceGateways')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_service_gateways(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_service_gateways(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_service_gateways(
                        compartment_id=request.pop(util.camelize('compartmentId')),
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
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListServices')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_services(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
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
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListSubnets')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_subnets(
                compartment_id=request.pop(util.camelize('compartmentId')),
                vcn_id=request.pop(util.camelize('vcnId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_subnets(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    vcn_id=request.pop(util.camelize('vcnId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_subnets(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        vcn_id=request.pop(util.camelize('vcnId')),
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
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListVcns')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_vcns(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_vcns(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_vcns(
                        compartment_id=request.pop(util.camelize('compartmentId')),
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
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListVirtualCircuitBandwidthShapes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_virtual_circuit_bandwidth_shapes(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_virtual_circuit_bandwidth_shapes(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_virtual_circuit_bandwidth_shapes(
                        compartment_id=request.pop(util.camelize('compartmentId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_virtual_circuit_public_prefixes(
                virtual_circuit_id=request.pop(util.camelize('virtualCircuitId')),
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
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListVirtualCircuits')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.list_virtual_circuits(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_virtual_circuits(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_virtual_circuits(
                        compartment_id=request.pop(util.camelize('compartmentId')),
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


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_remove_network_security_group_security_rules(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'RemoveNetworkSecurityGroupSecurityRules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'RemoveNetworkSecurityGroupSecurityRules')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='RemoveNetworkSecurityGroupSecurityRules')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.remove_network_security_group_security_rules(
                network_security_group_id=request.pop(util.camelize('networkSecurityGroupId')),
                remove_network_security_group_security_rules_details=request.pop(util.camelize('RemoveNetworkSecurityGroupSecurityRulesDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'RemoveNetworkSecurityGroupSecurityRules',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'remove_network_security_group_security_rules',
            False,
            False
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_cpe(
                cpe_id=request.pop(util.camelize('cpeId')),
                update_cpe_details=request.pop(util.camelize('UpdateCpeDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_cross_connect(
                cross_connect_id=request.pop(util.camelize('crossConnectId')),
                update_cross_connect_details=request.pop(util.camelize('UpdateCrossConnectDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_cross_connect_group(
                cross_connect_group_id=request.pop(util.camelize('crossConnectGroupId')),
                update_cross_connect_group_details=request.pop(util.camelize('UpdateCrossConnectGroupDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_dhcp_options(
                dhcp_id=request.pop(util.camelize('dhcpId')),
                update_dhcp_details=request.pop(util.camelize('UpdateDhcpDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_drg(
                drg_id=request.pop(util.camelize('drgId')),
                update_drg_details=request.pop(util.camelize('UpdateDrgDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_drg_attachment(
                drg_attachment_id=request.pop(util.camelize('drgAttachmentId')),
                update_drg_attachment_details=request.pop(util.camelize('UpdateDrgAttachmentDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_internet_gateway(
                ig_id=request.pop(util.camelize('igId')),
                update_internet_gateway_details=request.pop(util.camelize('UpdateInternetGatewayDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_ip_sec_connection(
                ipsc_id=request.pop(util.camelize('ipscId')),
                update_ip_sec_connection_details=request.pop(util.camelize('UpdateIPSecConnectionDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_ip_sec_connection_tunnel(
                ipsc_id=request.pop(util.camelize('ipscId')),
                tunnel_id=request.pop(util.camelize('tunnelId')),
                update_ip_sec_connection_tunnel_details=request.pop(util.camelize('UpdateIPSecConnectionTunnelDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_ip_sec_connection_tunnel_shared_secret(
                ipsc_id=request.pop(util.camelize('ipscId')),
                tunnel_id=request.pop(util.camelize('tunnelId')),
                update_ip_sec_connection_tunnel_shared_secret_details=request.pop(util.camelize('UpdateIPSecConnectionTunnelSharedSecretDetails')),
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
def test_update_ipv6(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateIpv6'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'UpdateIpv6')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateIpv6')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_ipv6(
                ipv6_id=request.pop(util.camelize('ipv6Id')),
                update_ipv6_details=request.pop(util.camelize('UpdateIpv6Details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateIpv6',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'ipv6',
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_local_peering_gateway(
                local_peering_gateway_id=request.pop(util.camelize('localPeeringGatewayId')),
                update_local_peering_gateway_details=request.pop(util.camelize('UpdateLocalPeeringGatewayDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_nat_gateway(
                nat_gateway_id=request.pop(util.camelize('natGatewayId')),
                update_nat_gateway_details=request.pop(util.camelize('UpdateNatGatewayDetails')),
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
def test_update_network_security_group(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateNetworkSecurityGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'UpdateNetworkSecurityGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateNetworkSecurityGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_network_security_group(
                network_security_group_id=request.pop(util.camelize('networkSecurityGroupId')),
                update_network_security_group_details=request.pop(util.camelize('UpdateNetworkSecurityGroupDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateNetworkSecurityGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'networkSecurityGroup',
            False,
            False
        )


# IssueRoutingInfo tag="virtualNetwork" email="bmc_vcn_cp_us_grp@oracle.com" jiraProject="VCN" opsJiraProject="VN"
def test_update_network_security_group_security_rules(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateNetworkSecurityGroupSecurityRules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('virtual_network'), 'UpdateNetworkSecurityGroupSecurityRules')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateNetworkSecurityGroupSecurityRules')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_network_security_group_security_rules(
                network_security_group_id=request.pop(util.camelize('networkSecurityGroupId')),
                update_network_security_group_security_rules_details=request.pop(util.camelize('UpdateNetworkSecurityGroupSecurityRulesDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateNetworkSecurityGroupSecurityRules',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'updatedNetworkSecurityGroupSecurityRules',
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_private_ip(
                private_ip_id=request.pop(util.camelize('privateIpId')),
                update_private_ip_details=request.pop(util.camelize('UpdatePrivateIpDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_public_ip(
                public_ip_id=request.pop(util.camelize('publicIpId')),
                update_public_ip_details=request.pop(util.camelize('UpdatePublicIpDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_remote_peering_connection(
                remote_peering_connection_id=request.pop(util.camelize('remotePeeringConnectionId')),
                update_remote_peering_connection_details=request.pop(util.camelize('UpdateRemotePeeringConnectionDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_route_table(
                rt_id=request.pop(util.camelize('rtId')),
                update_route_table_details=request.pop(util.camelize('UpdateRouteTableDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_security_list(
                security_list_id=request.pop(util.camelize('securityListId')),
                update_security_list_details=request.pop(util.camelize('UpdateSecurityListDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_service_gateway(
                service_gateway_id=request.pop(util.camelize('serviceGatewayId')),
                update_service_gateway_details=request.pop(util.camelize('UpdateServiceGatewayDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_subnet(
                subnet_id=request.pop(util.camelize('subnetId')),
                update_subnet_details=request.pop(util.camelize('UpdateSubnetDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_vcn(
                vcn_id=request.pop(util.camelize('vcnId')),
                update_vcn_details=request.pop(util.camelize('UpdateVcnDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_virtual_circuit(
                virtual_circuit_id=request.pop(util.camelize('virtualCircuitId')),
                update_virtual_circuit_details=request.pop(util.camelize('UpdateVirtualCircuitDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.VirtualNetworkClient(config, service_endpoint=service_endpoint)
            response = client.update_vnic(
                vnic_id=request.pop(util.camelize('vnicId')),
                update_vnic_details=request.pop(util.camelize('UpdateVnicDetails')),
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
