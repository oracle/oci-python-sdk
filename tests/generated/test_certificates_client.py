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

        cassette_location = os.path.join('generated', 'certificates_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="team_oci_certificates_us_grp@oracle.com" jiraProject="OCICERT" opsJiraProject="OCICERT"
def test_get_ca_bundle(testing_service_client):
    if not testing_service_client.is_api_enabled('certificates', 'GetCaBundle'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('certificates', util.camelize('certificates'), 'GetCaBundle')
    )

    request_containers = testing_service_client.get_requests(service_name='certificates', api_name='GetCaBundle')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.certificates.CertificatesClient(config, service_endpoint=service_endpoint)
            response = client.get_ca_bundle(
                ca_bundle_id=request.pop(util.camelize('caBundleId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'certificates',
            'GetCaBundle',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'caBundle',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_certificates_us_grp@oracle.com" jiraProject="OCICERT" opsJiraProject="OCICERT"
def test_get_certificate_authority_bundle(testing_service_client):
    if not testing_service_client.is_api_enabled('certificates', 'GetCertificateAuthorityBundle'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('certificates', util.camelize('certificates'), 'GetCertificateAuthorityBundle')
    )

    request_containers = testing_service_client.get_requests(service_name='certificates', api_name='GetCertificateAuthorityBundle')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.certificates.CertificatesClient(config, service_endpoint=service_endpoint)
            response = client.get_certificate_authority_bundle(
                certificate_authority_id=request.pop(util.camelize('certificateAuthorityId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'certificates',
            'GetCertificateAuthorityBundle',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'certificateAuthorityBundle',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_certificates_us_grp@oracle.com" jiraProject="OCICERT" opsJiraProject="OCICERT"
def test_get_certificate_bundle(testing_service_client):
    if not testing_service_client.is_api_enabled('certificates', 'GetCertificateBundle'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('certificates', util.camelize('certificates'), 'GetCertificateBundle')
    )

    request_containers = testing_service_client.get_requests(service_name='certificates', api_name='GetCertificateBundle')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.certificates.CertificatesClient(config, service_endpoint=service_endpoint)
            response = client.get_certificate_bundle(
                certificate_id=request.pop(util.camelize('certificateId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'certificates',
            'GetCertificateBundle',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'certificateBundle',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_certificates_us_grp@oracle.com" jiraProject="OCICERT" opsJiraProject="OCICERT"
def test_list_certificate_authority_bundle_versions(testing_service_client):
    if not testing_service_client.is_api_enabled('certificates', 'ListCertificateAuthorityBundleVersions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('certificates', util.camelize('certificates'), 'ListCertificateAuthorityBundleVersions')
    )

    request_containers = testing_service_client.get_requests(service_name='certificates', api_name='ListCertificateAuthorityBundleVersions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.certificates.CertificatesClient(config, service_endpoint=service_endpoint)
            response = client.list_certificate_authority_bundle_versions(
                certificate_authority_id=request.pop(util.camelize('certificateAuthorityId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'certificates',
            'ListCertificateAuthorityBundleVersions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'certificateAuthorityBundleVersionCollection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_certificates_us_grp@oracle.com" jiraProject="OCICERT" opsJiraProject="OCICERT"
def test_list_certificate_bundle_versions(testing_service_client):
    if not testing_service_client.is_api_enabled('certificates', 'ListCertificateBundleVersions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('certificates', util.camelize('certificates'), 'ListCertificateBundleVersions')
    )

    request_containers = testing_service_client.get_requests(service_name='certificates', api_name='ListCertificateBundleVersions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.certificates.CertificatesClient(config, service_endpoint=service_endpoint)
            response = client.list_certificate_bundle_versions(
                certificate_id=request.pop(util.camelize('certificateId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'certificates',
            'ListCertificateBundleVersions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'certificateBundleVersionCollection',
            False,
            False
        )
