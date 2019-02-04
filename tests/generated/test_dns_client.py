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


def test_create_zone(testing_service_client, config):
    if not testing_service_client.is_api_enabled('dns', 'CreateZone'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='CreateZone')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.dns.DnsClient(config)
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


def test_delete_domain_records(testing_service_client, config):
    if not testing_service_client.is_api_enabled('dns', 'DeleteDomainRecords'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='DeleteDomainRecords')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.dns.DnsClient(config)
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


def test_delete_rr_set(testing_service_client, config):
    if not testing_service_client.is_api_enabled('dns', 'DeleteRRSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='DeleteRRSet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.dns.DnsClient(config)
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


def test_delete_zone(testing_service_client, config):
    if not testing_service_client.is_api_enabled('dns', 'DeleteZone'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='DeleteZone')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.dns.DnsClient(config)
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


def test_get_domain_records(testing_service_client, config):
    if not testing_service_client.is_api_enabled('dns', 'GetDomainRecords'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='GetDomainRecords')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.dns.DnsClient(config)
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


def test_get_rr_set(testing_service_client, config):
    if not testing_service_client.is_api_enabled('dns', 'GetRRSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='GetRRSet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.dns.DnsClient(config)
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


def test_get_zone(testing_service_client, config):
    if not testing_service_client.is_api_enabled('dns', 'GetZone'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='GetZone')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.dns.DnsClient(config)
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


def test_get_zone_records(testing_service_client, config):
    if not testing_service_client.is_api_enabled('dns', 'GetZoneRecords'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='GetZoneRecords')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.dns.DnsClient(config)
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


def test_list_zones(testing_service_client, config):
    if not testing_service_client.is_api_enabled('dns', 'ListZones'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='ListZones')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.dns.DnsClient(config)
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


def test_patch_domain_records(testing_service_client, config):
    if not testing_service_client.is_api_enabled('dns', 'PatchDomainRecords'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='PatchDomainRecords')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.dns.DnsClient(config)
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


def test_patch_rr_set(testing_service_client, config):
    if not testing_service_client.is_api_enabled('dns', 'PatchRRSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='PatchRRSet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.dns.DnsClient(config)
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


def test_patch_zone_records(testing_service_client, config):
    if not testing_service_client.is_api_enabled('dns', 'PatchZoneRecords'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='PatchZoneRecords')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.dns.DnsClient(config)
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


def test_update_domain_records(testing_service_client, config):
    if not testing_service_client.is_api_enabled('dns', 'UpdateDomainRecords'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='UpdateDomainRecords')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.dns.DnsClient(config)
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


def test_update_rr_set(testing_service_client, config):
    if not testing_service_client.is_api_enabled('dns', 'UpdateRRSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='UpdateRRSet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.dns.DnsClient(config)
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


def test_update_zone(testing_service_client, config):
    if not testing_service_client.is_api_enabled('dns', 'UpdateZone'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='UpdateZone')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.dns.DnsClient(config)
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


def test_update_zone_records(testing_service_client, config):
    if not testing_service_client.is_api_enabled('dns', 'UpdateZoneRecords'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='dns', api_name='UpdateZoneRecords')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.dns.DnsClient(config)
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


