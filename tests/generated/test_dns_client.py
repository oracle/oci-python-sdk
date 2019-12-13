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

    cassette_location = os.path.join('generated', 'dns_{name}.yml'.format(name=request.function.__name__))
    with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
        yield


# IssueRoutingInfo tag="default" email="oci_pubdns_dev_us_grp@oracle.com" jiraProject="PD" opsJiraProject="PUBDNS"
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.change_steering_policy_compartment(
                steering_policy_id=request.pop(util.camelize('steering_policy_id')),
                change_steering_policy_compartment_details=request.pop(util.camelize('change_steering_policy_compartment_details')),
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


# IssueRoutingInfo tag="default" email="oci_pubdns_dev_us_grp@oracle.com" jiraProject="PD" opsJiraProject="PUBDNS"
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.change_tsig_key_compartment(
                tsig_key_id=request.pop(util.camelize('tsig_key_id')),
                change_tsig_key_compartment_details=request.pop(util.camelize('change_tsig_key_compartment_details')),
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


# IssueRoutingInfo tag="default" email="oci_pubdns_dev_us_grp@oracle.com" jiraProject="PD" opsJiraProject="PUBDNS"
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.change_zone_compartment(
                zone_id=request.pop(util.camelize('zone_id')),
                change_zone_compartment_details=request.pop(util.camelize('change_zone_compartment_details')),
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


# IssueRoutingInfo tag="default" email="oci_pubdns_dev_us_grp@oracle.com" jiraProject="PD" opsJiraProject="PUBDNS"
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.create_steering_policy(
                create_steering_policy_details=request.pop(util.camelize('create_steering_policy_details')),
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


# IssueRoutingInfo tag="default" email="oci_pubdns_dev_us_grp@oracle.com" jiraProject="PD" opsJiraProject="PUBDNS"
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.create_steering_policy_attachment(
                create_steering_policy_attachment_details=request.pop(util.camelize('create_steering_policy_attachment_details')),
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


# IssueRoutingInfo tag="default" email="oci_pubdns_dev_us_grp@oracle.com" jiraProject="PD" opsJiraProject="PUBDNS"
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.create_tsig_key(
                create_tsig_key_details=request.pop(util.camelize('create_tsig_key_details')),
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


# IssueRoutingInfo tag="default" email="oci_pubdns_dev_us_grp@oracle.com" jiraProject="PD" opsJiraProject="PUBDNS"
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.create_zone(
                create_zone_details=request.pop(util.camelize('create_zone_details')),
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


# IssueRoutingInfo tag="default" email="oci_pubdns_dev_us_grp@oracle.com" jiraProject="PD" opsJiraProject="PUBDNS"
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.delete_domain_records(
                zone_name_or_id=request.pop(util.camelize('zone_name_or_id')),
                domain=request.pop(util.camelize('domain')),
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


# IssueRoutingInfo tag="default" email="oci_pubdns_dev_us_grp@oracle.com" jiraProject="PD" opsJiraProject="PUBDNS"
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.delete_rr_set(
                zone_name_or_id=request.pop(util.camelize('zone_name_or_id')),
                domain=request.pop(util.camelize('domain')),
                rtype=request.pop(util.camelize('rtype')),
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


# IssueRoutingInfo tag="default" email="oci_pubdns_dev_us_grp@oracle.com" jiraProject="PD" opsJiraProject="PUBDNS"
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.delete_steering_policy(
                steering_policy_id=request.pop(util.camelize('steering_policy_id')),
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


# IssueRoutingInfo tag="default" email="oci_pubdns_dev_us_grp@oracle.com" jiraProject="PD" opsJiraProject="PUBDNS"
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.delete_steering_policy_attachment(
                steering_policy_attachment_id=request.pop(util.camelize('steering_policy_attachment_id')),
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


# IssueRoutingInfo tag="default" email="oci_pubdns_dev_us_grp@oracle.com" jiraProject="PD" opsJiraProject="PUBDNS"
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.delete_tsig_key(
                tsig_key_id=request.pop(util.camelize('tsig_key_id')),
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


# IssueRoutingInfo tag="default" email="oci_pubdns_dev_us_grp@oracle.com" jiraProject="PD" opsJiraProject="PUBDNS"
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.delete_zone(
                zone_name_or_id=request.pop(util.camelize('zone_name_or_id')),
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


# IssueRoutingInfo tag="default" email="oci_pubdns_dev_us_grp@oracle.com" jiraProject="PD" opsJiraProject="PUBDNS"
def test_get_domain_records(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'GetDomainRecords'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'GetDomainRecords')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='GetDomainRecords')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.get_domain_records(
                zone_name_or_id=request.pop(util.camelize('zone_name_or_id')),
                domain=request.pop(util.camelize('domain')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.get_domain_records(
                    zone_name_or_id=request.pop(util.camelize('zone_name_or_id')),
                    domain=request.pop(util.camelize('domain')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.get_domain_records(
                        zone_name_or_id=request.pop(util.camelize('zone_name_or_id')),
                        domain=request.pop(util.camelize('domain')),
                        page=next_response.headers[prev_page],
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


# IssueRoutingInfo tag="default" email="oci_pubdns_dev_us_grp@oracle.com" jiraProject="PD" opsJiraProject="PUBDNS"
def test_get_rr_set(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'GetRRSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'GetRRSet')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='GetRRSet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.get_rr_set(
                zone_name_or_id=request.pop(util.camelize('zone_name_or_id')),
                domain=request.pop(util.camelize('domain')),
                rtype=request.pop(util.camelize('rtype')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.get_rr_set(
                    zone_name_or_id=request.pop(util.camelize('zone_name_or_id')),
                    domain=request.pop(util.camelize('domain')),
                    rtype=request.pop(util.camelize('rtype')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.get_rr_set(
                        zone_name_or_id=request.pop(util.camelize('zone_name_or_id')),
                        domain=request.pop(util.camelize('domain')),
                        rtype=request.pop(util.camelize('rtype')),
                        page=next_response.headers[prev_page],
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


# IssueRoutingInfo tag="default" email="oci_pubdns_dev_us_grp@oracle.com" jiraProject="PD" opsJiraProject="PUBDNS"
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.get_steering_policy(
                steering_policy_id=request.pop(util.camelize('steering_policy_id')),
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


# IssueRoutingInfo tag="default" email="oci_pubdns_dev_us_grp@oracle.com" jiraProject="PD" opsJiraProject="PUBDNS"
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.get_steering_policy_attachment(
                steering_policy_attachment_id=request.pop(util.camelize('steering_policy_attachment_id')),
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


# IssueRoutingInfo tag="default" email="oci_pubdns_dev_us_grp@oracle.com" jiraProject="PD" opsJiraProject="PUBDNS"
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.get_tsig_key(
                tsig_key_id=request.pop(util.camelize('tsig_key_id')),
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


# IssueRoutingInfo tag="default" email="oci_pubdns_dev_us_grp@oracle.com" jiraProject="PD" opsJiraProject="PUBDNS"
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.get_zone(
                zone_name_or_id=request.pop(util.camelize('zone_name_or_id')),
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


# IssueRoutingInfo tag="default" email="oci_pubdns_dev_us_grp@oracle.com" jiraProject="PD" opsJiraProject="PUBDNS"
def test_get_zone_records(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'GetZoneRecords'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'GetZoneRecords')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='GetZoneRecords')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.get_zone_records(
                zone_name_or_id=request.pop(util.camelize('zone_name_or_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.get_zone_records(
                    zone_name_or_id=request.pop(util.camelize('zone_name_or_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.get_zone_records(
                        zone_name_or_id=request.pop(util.camelize('zone_name_or_id')),
                        page=next_response.headers[prev_page],
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


# IssueRoutingInfo tag="default" email="oci_pubdns_dev_us_grp@oracle.com" jiraProject="PD" opsJiraProject="PUBDNS"
def test_list_steering_policies(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'ListSteeringPolicies'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'ListSteeringPolicies')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='ListSteeringPolicies')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.list_steering_policies(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_steering_policies(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_steering_policies(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
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


# IssueRoutingInfo tag="default" email="oci_pubdns_dev_us_grp@oracle.com" jiraProject="PD" opsJiraProject="PUBDNS"
def test_list_steering_policy_attachments(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'ListSteeringPolicyAttachments'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'ListSteeringPolicyAttachments')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='ListSteeringPolicyAttachments')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.list_steering_policy_attachments(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_steering_policy_attachments(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_steering_policy_attachments(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
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


# IssueRoutingInfo tag="default" email="oci_pubdns_dev_us_grp@oracle.com" jiraProject="PD" opsJiraProject="PUBDNS"
def test_list_tsig_keys(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'ListTsigKeys'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'ListTsigKeys')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='ListTsigKeys')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.list_tsig_keys(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_tsig_keys(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_tsig_keys(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
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


# IssueRoutingInfo tag="default" email="oci_pubdns_dev_us_grp@oracle.com" jiraProject="PD" opsJiraProject="PUBDNS"
def test_list_zones(testing_service_client):
    if not testing_service_client.is_api_enabled('dns', 'ListZones'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dns', util.camelize('dns'), 'ListZones')
    )

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='ListZones')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.list_zones(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_zones(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_zones(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
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


# IssueRoutingInfo tag="default" email="oci_pubdns_dev_us_grp@oracle.com" jiraProject="PD" opsJiraProject="PUBDNS"
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.patch_domain_records(
                zone_name_or_id=request.pop(util.camelize('zone_name_or_id')),
                domain=request.pop(util.camelize('domain')),
                patch_domain_records_details=request.pop(util.camelize('patch_domain_records_details')),
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


# IssueRoutingInfo tag="default" email="oci_pubdns_dev_us_grp@oracle.com" jiraProject="PD" opsJiraProject="PUBDNS"
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.patch_rr_set(
                zone_name_or_id=request.pop(util.camelize('zone_name_or_id')),
                domain=request.pop(util.camelize('domain')),
                rtype=request.pop(util.camelize('rtype')),
                patch_rr_set_details=request.pop(util.camelize('patch_rr_set_details')),
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


# IssueRoutingInfo tag="default" email="oci_pubdns_dev_us_grp@oracle.com" jiraProject="PD" opsJiraProject="PUBDNS"
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.patch_zone_records(
                zone_name_or_id=request.pop(util.camelize('zone_name_or_id')),
                patch_zone_records_details=request.pop(util.camelize('patch_zone_records_details')),
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


# IssueRoutingInfo tag="default" email="oci_pubdns_dev_us_grp@oracle.com" jiraProject="PD" opsJiraProject="PUBDNS"
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.update_domain_records(
                zone_name_or_id=request.pop(util.camelize('zone_name_or_id')),
                domain=request.pop(util.camelize('domain')),
                update_domain_records_details=request.pop(util.camelize('update_domain_records_details')),
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


# IssueRoutingInfo tag="default" email="oci_pubdns_dev_us_grp@oracle.com" jiraProject="PD" opsJiraProject="PUBDNS"
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.update_rr_set(
                zone_name_or_id=request.pop(util.camelize('zone_name_or_id')),
                domain=request.pop(util.camelize('domain')),
                rtype=request.pop(util.camelize('rtype')),
                update_rr_set_details=request.pop(util.camelize('update_rr_set_details')),
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


# IssueRoutingInfo tag="default" email="oci_pubdns_dev_us_grp@oracle.com" jiraProject="PD" opsJiraProject="PUBDNS"
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.update_steering_policy(
                steering_policy_id=request.pop(util.camelize('steering_policy_id')),
                update_steering_policy_details=request.pop(util.camelize('update_steering_policy_details')),
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


# IssueRoutingInfo tag="default" email="oci_pubdns_dev_us_grp@oracle.com" jiraProject="PD" opsJiraProject="PUBDNS"
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.update_steering_policy_attachment(
                steering_policy_attachment_id=request.pop(util.camelize('steering_policy_attachment_id')),
                update_steering_policy_attachment_details=request.pop(util.camelize('update_steering_policy_attachment_details')),
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


# IssueRoutingInfo tag="default" email="oci_pubdns_dev_us_grp@oracle.com" jiraProject="PD" opsJiraProject="PUBDNS"
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.update_tsig_key(
                tsig_key_id=request.pop(util.camelize('tsig_key_id')),
                update_tsig_key_details=request.pop(util.camelize('update_tsig_key_details')),
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


# IssueRoutingInfo tag="default" email="oci_pubdns_dev_us_grp@oracle.com" jiraProject="PD" opsJiraProject="PUBDNS"
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.update_zone(
                zone_name_or_id=request.pop(util.camelize('zone_name_or_id')),
                update_zone_details=request.pop(util.camelize('update_zone_details')),
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


# IssueRoutingInfo tag="default" email="oci_pubdns_dev_us_grp@oracle.com" jiraProject="PD" opsJiraProject="PUBDNS"
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.dns.DnsClient(config, service_endpoint=service_endpoint)
            response = client.update_zone_records(
                zone_name_or_id=request.pop(util.camelize('zone_name_or_id')),
                update_zone_records_details=request.pop(util.camelize('update_zone_records_details')),
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
