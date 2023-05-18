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

        cassette_location = os.path.join('generated', 'dns_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_change_resolver_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'ChangeResolverCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'ChangeResolverCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='ChangeResolverCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.change_resolver_compartment(
                resolver_id=request.pop(util.camelize('resolverId')),
                change_resolver_compartment_details=request.pop(util.camelize('ChangeResolverCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'ChangeResolverCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_resolver_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_change_steering_policy_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'ChangeSteeringPolicyCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'ChangeSteeringPolicyCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='ChangeSteeringPolicyCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.change_steering_policy_compartment(
                steering_policy_id=request.pop(util.camelize('steeringPolicyId')),
                change_steering_policy_compartment_details=request.pop(util.camelize('ChangeSteeringPolicyCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'ChangeSteeringPolicyCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_steering_policy_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_change_tsig_key_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'ChangeTsigKeyCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'ChangeTsigKeyCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='ChangeTsigKeyCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.change_tsig_key_compartment(
                tsig_key_id=request.pop(util.camelize('tsigKeyId')),
                change_tsig_key_compartment_details=request.pop(util.camelize('ChangeTsigKeyCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'ChangeTsigKeyCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_tsig_key_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_change_view_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'ChangeViewCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'ChangeViewCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='ChangeViewCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.change_view_compartment(
                view_id=request.pop(util.camelize('viewId')),
                change_view_compartment_details=request.pop(util.camelize('ChangeViewCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'ChangeViewCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_view_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_change_zone_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'ChangeZoneCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'ChangeZoneCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='ChangeZoneCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.change_zone_compartment(
                zone_id=request.pop(util.camelize('zoneId')),
                change_zone_compartment_details=request.pop(util.camelize('ChangeZoneCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'ChangeZoneCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_zone_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_create_resolver_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'CreateResolverEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'CreateResolverEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='CreateResolverEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.create_resolver_endpoint(
                resolver_id=request.pop(util.camelize('resolverId')),
                create_resolver_endpoint_details=request.pop(util.camelize('CreateResolverEndpointDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'CreateResolverEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'resolverEndpoint',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_create_steering_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'CreateSteeringPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'CreateSteeringPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='CreateSteeringPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.create_steering_policy(
                create_steering_policy_details=request.pop(util.camelize('CreateSteeringPolicyDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'CreateSteeringPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'steeringPolicy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_create_steering_policy_attachment(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'CreateSteeringPolicyAttachment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'CreateSteeringPolicyAttachment')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='CreateSteeringPolicyAttachment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.create_steering_policy_attachment(
                create_steering_policy_attachment_details=request.pop(util.camelize('CreateSteeringPolicyAttachmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'CreateSteeringPolicyAttachment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'steeringPolicyAttachment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_create_tsig_key(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'CreateTsigKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'CreateTsigKey')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='CreateTsigKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.create_tsig_key(
                create_tsig_key_details=request.pop(util.camelize('CreateTsigKeyDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'CreateTsigKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'tsigKey',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_create_view(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'CreateView'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'CreateView')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='CreateView')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.create_view(
                create_view_details=request.pop(util.camelize('CreateViewDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'CreateView',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'view',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_create_zone(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'CreateZone'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'CreateZone')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='CreateZone')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.create_zone(
                create_zone_details=request.pop(util.camelize('CreateZoneDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'CreateZone',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'zone',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_create_zone_from_zone_file(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'CreateZoneFromZoneFile'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'CreateZoneFromZoneFile')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='CreateZoneFromZoneFile')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.create_zone_from_zone_file(
                compartment_id=request.pop(util.camelize('compartmentId')),
                create_zone_from_zone_file_details=request.pop(util.camelize('CreateZoneFromZoneFileDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'CreateZoneFromZoneFile',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'zone',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_delete_domain_records(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'DeleteDomainRecords'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'DeleteDomainRecords')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='DeleteDomainRecords')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.delete_domain_records(
                zone_name_or_id=request.pop(util.camelize('zoneNameOrId')),
                domain=request.pop(util.camelize('domain')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'DeleteDomainRecords',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_domain_records',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_delete_resolver_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'DeleteResolverEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'DeleteResolverEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='DeleteResolverEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.delete_resolver_endpoint(
                resolver_id=request.pop(util.camelize('resolverId')),
                resolver_endpoint_name=request.pop(util.camelize('resolverEndpointName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'DeleteResolverEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_resolver_endpoint',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_delete_rr_set(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'DeleteRRSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'DeleteRRSet')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='DeleteRRSet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.delete_rr_set(
                zone_name_or_id=request.pop(util.camelize('zoneNameOrId')),
                domain=request.pop(util.camelize('domain')),
                rtype=request.pop(util.camelize('rtype')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'DeleteRRSet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_rr_set',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_delete_steering_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'DeleteSteeringPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'DeleteSteeringPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='DeleteSteeringPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.delete_steering_policy(
                steering_policy_id=request.pop(util.camelize('steeringPolicyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'DeleteSteeringPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_steering_policy',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_delete_steering_policy_attachment(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'DeleteSteeringPolicyAttachment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'DeleteSteeringPolicyAttachment')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='DeleteSteeringPolicyAttachment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.delete_steering_policy_attachment(
                steering_policy_attachment_id=request.pop(util.camelize('steeringPolicyAttachmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'DeleteSteeringPolicyAttachment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_steering_policy_attachment',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_delete_tsig_key(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'DeleteTsigKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'DeleteTsigKey')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='DeleteTsigKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.delete_tsig_key(
                tsig_key_id=request.pop(util.camelize('tsigKeyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'DeleteTsigKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_tsig_key',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_delete_view(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'DeleteView'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'DeleteView')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='DeleteView')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.delete_view(
                view_id=request.pop(util.camelize('viewId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'DeleteView',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_view',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_delete_zone(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'DeleteZone'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'DeleteZone')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='DeleteZone')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.delete_zone(
                zone_name_or_id=request.pop(util.camelize('zoneNameOrId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'DeleteZone',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_zone',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_get_domain_records(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'GetDomainRecords'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'GetDomainRecords')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='GetDomainRecords')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.get_domain_records(
                zone_name_or_id=request.pop(util.camelize('zoneNameOrId')),
                domain=request.pop(util.camelize('domain')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.get_domain_records(
                    zone_name_or_id=request.pop(util.camelize('zoneNameOrId')),
                    domain=request.pop(util.camelize('domain')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.get_domain_records(
                        zone_name_or_id=request.pop(util.camelize('zoneNameOrId')),
                        domain=request.pop(util.camelize('domain')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'GetDomainRecords',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'recordCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_get_resolver(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'GetResolver'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'GetResolver')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='GetResolver')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.get_resolver(
                resolver_id=request.pop(util.camelize('resolverId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'GetResolver',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'resolver',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_get_resolver_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'GetResolverEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'GetResolverEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='GetResolverEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.get_resolver_endpoint(
                resolver_id=request.pop(util.camelize('resolverId')),
                resolver_endpoint_name=request.pop(util.camelize('resolverEndpointName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'GetResolverEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'resolverEndpoint',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_get_rr_set(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'GetRRSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'GetRRSet')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='GetRRSet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.get_rr_set(
                zone_name_or_id=request.pop(util.camelize('zoneNameOrId')),
                domain=request.pop(util.camelize('domain')),
                rtype=request.pop(util.camelize('rtype')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.get_rr_set(
                    zone_name_or_id=request.pop(util.camelize('zoneNameOrId')),
                    domain=request.pop(util.camelize('domain')),
                    rtype=request.pop(util.camelize('rtype')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.get_rr_set(
                        zone_name_or_id=request.pop(util.camelize('zoneNameOrId')),
                        domain=request.pop(util.camelize('domain')),
                        rtype=request.pop(util.camelize('rtype')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'GetRRSet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'rRSet',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_get_steering_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'GetSteeringPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'GetSteeringPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='GetSteeringPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.get_steering_policy(
                steering_policy_id=request.pop(util.camelize('steeringPolicyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'GetSteeringPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'steeringPolicy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_get_steering_policy_attachment(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'GetSteeringPolicyAttachment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'GetSteeringPolicyAttachment')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='GetSteeringPolicyAttachment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.get_steering_policy_attachment(
                steering_policy_attachment_id=request.pop(util.camelize('steeringPolicyAttachmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'GetSteeringPolicyAttachment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'steeringPolicyAttachment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_get_tsig_key(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'GetTsigKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'GetTsigKey')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='GetTsigKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.get_tsig_key(
                tsig_key_id=request.pop(util.camelize('tsigKeyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'GetTsigKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'tsigKey',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_get_view(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'GetView'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'GetView')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='GetView')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.get_view(
                view_id=request.pop(util.camelize('viewId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'GetView',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'view',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_get_zone(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'GetZone'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'GetZone')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='GetZone')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.get_zone(
                zone_name_or_id=request.pop(util.camelize('zoneNameOrId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'GetZone',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'zone',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_get_zone_content(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'GetZoneContent'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'GetZoneContent')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='GetZoneContent')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.get_zone_content(
                zone_name_or_id=request.pop(util.camelize('zoneNameOrId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'GetZoneContent',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_get_zone_records(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'GetZoneRecords'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'GetZoneRecords')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='GetZoneRecords')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.get_zone_records(
                zone_name_or_id=request.pop(util.camelize('zoneNameOrId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.get_zone_records(
                    zone_name_or_id=request.pop(util.camelize('zoneNameOrId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.get_zone_records(
                        zone_name_or_id=request.pop(util.camelize('zoneNameOrId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'GetZoneRecords',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'recordCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_list_resolver_endpoints(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'ListResolverEndpoints'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'ListResolverEndpoints')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='ListResolverEndpoints')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.list_resolver_endpoints(
                resolver_id=request.pop(util.camelize('resolverId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_resolver_endpoints(
                    resolver_id=request.pop(util.camelize('resolverId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_resolver_endpoints(
                        resolver_id=request.pop(util.camelize('resolverId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'ListResolverEndpoints',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'resolverEndpointSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_list_resolvers(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'ListResolvers'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'ListResolvers')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='ListResolvers')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.list_resolvers(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_resolvers(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_resolvers(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'ListResolvers',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'resolverSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_list_steering_policies(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'ListSteeringPolicies'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'ListSteeringPolicies')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='ListSteeringPolicies')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.list_steering_policies(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_steering_policies(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_steering_policies(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'ListSteeringPolicies',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'steeringPolicySummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_list_steering_policy_attachments(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'ListSteeringPolicyAttachments'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'ListSteeringPolicyAttachments')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='ListSteeringPolicyAttachments')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.list_steering_policy_attachments(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_steering_policy_attachments(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_steering_policy_attachments(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'ListSteeringPolicyAttachments',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'steeringPolicyAttachmentSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_list_tsig_keys(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'ListTsigKeys'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'ListTsigKeys')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='ListTsigKeys')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.list_tsig_keys(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_tsig_keys(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_tsig_keys(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'ListTsigKeys',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'tsigKeySummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_list_views(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'ListViews'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'ListViews')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='ListViews')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.list_views(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_views(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_views(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'ListViews',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'viewSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_list_zone_transfer_servers(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'ListZoneTransferServers'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'ListZoneTransferServers')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='ListZoneTransferServers')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.list_zone_transfer_servers(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_zone_transfer_servers(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_zone_transfer_servers(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'ListZoneTransferServers',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'zoneTransferServer',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_list_zones(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'ListZones'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'ListZones')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='ListZones')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.list_zones(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_zones(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_zones(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'ListZones',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'zoneSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_patch_domain_records(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'PatchDomainRecords'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'PatchDomainRecords')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='PatchDomainRecords')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.patch_domain_records(
                zone_name_or_id=request.pop(util.camelize('zoneNameOrId')),
                domain=request.pop(util.camelize('domain')),
                patch_domain_records_details=request.pop(util.camelize('PatchDomainRecordsDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'PatchDomainRecords',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'recordCollection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_patch_rr_set(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'PatchRRSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'PatchRRSet')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='PatchRRSet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.patch_rr_set(
                zone_name_or_id=request.pop(util.camelize('zoneNameOrId')),
                domain=request.pop(util.camelize('domain')),
                rtype=request.pop(util.camelize('rtype')),
                patch_rr_set_details=request.pop(util.camelize('PatchRRSetDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'PatchRRSet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'recordCollection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_patch_zone_records(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'PatchZoneRecords'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'PatchZoneRecords')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='PatchZoneRecords')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.patch_zone_records(
                zone_name_or_id=request.pop(util.camelize('zoneNameOrId')),
                patch_zone_records_details=request.pop(util.camelize('PatchZoneRecordsDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'PatchZoneRecords',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'recordCollection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_update_domain_records(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'UpdateDomainRecords'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'UpdateDomainRecords')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='UpdateDomainRecords')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.update_domain_records(
                zone_name_or_id=request.pop(util.camelize('zoneNameOrId')),
                domain=request.pop(util.camelize('domain')),
                update_domain_records_details=request.pop(util.camelize('UpdateDomainRecordsDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'UpdateDomainRecords',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'recordCollection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_update_resolver(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'UpdateResolver'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'UpdateResolver')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='UpdateResolver')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.update_resolver(
                resolver_id=request.pop(util.camelize('resolverId')),
                update_resolver_details=request.pop(util.camelize('UpdateResolverDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'UpdateResolver',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'resolver',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_update_resolver_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'UpdateResolverEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'UpdateResolverEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='UpdateResolverEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.update_resolver_endpoint(
                resolver_id=request.pop(util.camelize('resolverId')),
                resolver_endpoint_name=request.pop(util.camelize('resolverEndpointName')),
                update_resolver_endpoint_details=request.pop(util.camelize('UpdateResolverEndpointDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'UpdateResolverEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'resolverEndpoint',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_update_rr_set(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'UpdateRRSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'UpdateRRSet')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='UpdateRRSet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.update_rr_set(
                zone_name_or_id=request.pop(util.camelize('zoneNameOrId')),
                domain=request.pop(util.camelize('domain')),
                rtype=request.pop(util.camelize('rtype')),
                update_rr_set_details=request.pop(util.camelize('UpdateRRSetDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'UpdateRRSet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'recordCollection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_update_steering_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'UpdateSteeringPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'UpdateSteeringPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='UpdateSteeringPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.update_steering_policy(
                steering_policy_id=request.pop(util.camelize('steeringPolicyId')),
                update_steering_policy_details=request.pop(util.camelize('UpdateSteeringPolicyDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'UpdateSteeringPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'steeringPolicy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_update_steering_policy_attachment(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'UpdateSteeringPolicyAttachment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'UpdateSteeringPolicyAttachment')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='UpdateSteeringPolicyAttachment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.update_steering_policy_attachment(
                steering_policy_attachment_id=request.pop(util.camelize('steeringPolicyAttachmentId')),
                update_steering_policy_attachment_details=request.pop(util.camelize('UpdateSteeringPolicyAttachmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'UpdateSteeringPolicyAttachment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'steeringPolicyAttachment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_update_tsig_key(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'UpdateTsigKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'UpdateTsigKey')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='UpdateTsigKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.update_tsig_key(
                tsig_key_id=request.pop(util.camelize('tsigKeyId')),
                update_tsig_key_details=request.pop(util.camelize('UpdateTsigKeyDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'UpdateTsigKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'tsigKey',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_update_view(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'UpdateView'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'UpdateView')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='UpdateView')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.update_view(
                view_id=request.pop(util.camelize('viewId')),
                update_view_details=request.pop(util.camelize('UpdateViewDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'UpdateView',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'view',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_update_zone(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'UpdateZone'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'UpdateZone')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='UpdateZone')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.update_zone(
                zone_name_or_id=request.pop(util.camelize('zoneNameOrId')),
                update_zone_details=request.pop(util.camelize('UpdateZoneDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'UpdateZone',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'zone',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_dns_control_plane_ww_grp@oracle.com" jiraProject="DNSCP" opsJiraProject="DNS"
def test_update_zone_records(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'UpdateZoneRecords'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'UpdateZoneRecords')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='UpdateZoneRecords')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.update_zone_records(
                zone_name_or_id=request.pop(util.camelize('zoneNameOrId')),
                update_zone_records_details=request.pop(util.camelize('UpdateZoneRecordsDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dns',
            'UpdateZoneRecords',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'recordCollection',
            False,
            False
        )
