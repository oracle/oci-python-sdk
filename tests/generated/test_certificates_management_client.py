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

        cassette_location = os.path.join('generated', 'certificates_management_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="team_oci_certificates_us_grp@oracle.com" jiraProject="OCICERT" opsJiraProject="OCICERT"
def test_cancel_certificate_authority_deletion(testing_service_client):
    if not testing_service_client.is_api_enabled('certificates_management', 'CancelCertificateAuthorityDeletion'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('certificates_management', util.camelize('certificates_management'), 'CancelCertificateAuthorityDeletion')
    )

    request_containers = testing_service_client.get_requests(service_name='certificates_management', api_name='CancelCertificateAuthorityDeletion')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.certificates_management.CertificatesManagementClient(config, service_endpoint=service_endpoint)
            response = client.cancel_certificate_authority_deletion(
                certificate_authority_id=request.pop(util.camelize('certificateAuthorityId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'certificates_management',
            'CancelCertificateAuthorityDeletion',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cancel_certificate_authority_deletion',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_certificates_us_grp@oracle.com" jiraProject="OCICERT" opsJiraProject="OCICERT"
def test_cancel_certificate_authority_version_deletion(testing_service_client):
    if not testing_service_client.is_api_enabled('certificates_management', 'CancelCertificateAuthorityVersionDeletion'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('certificates_management', util.camelize('certificates_management'), 'CancelCertificateAuthorityVersionDeletion')
    )

    request_containers = testing_service_client.get_requests(service_name='certificates_management', api_name='CancelCertificateAuthorityVersionDeletion')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.certificates_management.CertificatesManagementClient(config, service_endpoint=service_endpoint)
            response = client.cancel_certificate_authority_version_deletion(
                certificate_authority_id=request.pop(util.camelize('certificateAuthorityId')),
                certificate_authority_version_number=request.pop(util.camelize('certificateAuthorityVersionNumber')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'certificates_management',
            'CancelCertificateAuthorityVersionDeletion',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cancel_certificate_authority_version_deletion',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_certificates_us_grp@oracle.com" jiraProject="OCICERT" opsJiraProject="OCICERT"
def test_cancel_certificate_deletion(testing_service_client):
    if not testing_service_client.is_api_enabled('certificates_management', 'CancelCertificateDeletion'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('certificates_management', util.camelize('certificates_management'), 'CancelCertificateDeletion')
    )

    request_containers = testing_service_client.get_requests(service_name='certificates_management', api_name='CancelCertificateDeletion')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.certificates_management.CertificatesManagementClient(config, service_endpoint=service_endpoint)
            response = client.cancel_certificate_deletion(
                certificate_id=request.pop(util.camelize('certificateId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'certificates_management',
            'CancelCertificateDeletion',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cancel_certificate_deletion',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_certificates_us_grp@oracle.com" jiraProject="OCICERT" opsJiraProject="OCICERT"
def test_cancel_certificate_version_deletion(testing_service_client):
    if not testing_service_client.is_api_enabled('certificates_management', 'CancelCertificateVersionDeletion'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('certificates_management', util.camelize('certificates_management'), 'CancelCertificateVersionDeletion')
    )

    request_containers = testing_service_client.get_requests(service_name='certificates_management', api_name='CancelCertificateVersionDeletion')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.certificates_management.CertificatesManagementClient(config, service_endpoint=service_endpoint)
            response = client.cancel_certificate_version_deletion(
                certificate_id=request.pop(util.camelize('certificateId')),
                certificate_version_number=request.pop(util.camelize('certificateVersionNumber')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'certificates_management',
            'CancelCertificateVersionDeletion',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cancel_certificate_version_deletion',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_certificates_us_grp@oracle.com" jiraProject="OCICERT" opsJiraProject="OCICERT"
def test_change_ca_bundle_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('certificates_management', 'ChangeCaBundleCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('certificates_management', util.camelize('certificates_management'), 'ChangeCaBundleCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='certificates_management', api_name='ChangeCaBundleCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.certificates_management.CertificatesManagementClient(config, service_endpoint=service_endpoint)
            response = client.change_ca_bundle_compartment(
                ca_bundle_id=request.pop(util.camelize('caBundleId')),
                change_ca_bundle_compartment_details=request.pop(util.camelize('ChangeCaBundleCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'certificates_management',
            'ChangeCaBundleCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_ca_bundle_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_certificates_us_grp@oracle.com" jiraProject="OCICERT" opsJiraProject="OCICERT"
def test_change_certificate_authority_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('certificates_management', 'ChangeCertificateAuthorityCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('certificates_management', util.camelize('certificates_management'), 'ChangeCertificateAuthorityCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='certificates_management', api_name='ChangeCertificateAuthorityCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.certificates_management.CertificatesManagementClient(config, service_endpoint=service_endpoint)
            response = client.change_certificate_authority_compartment(
                certificate_authority_id=request.pop(util.camelize('certificateAuthorityId')),
                change_certificate_authority_compartment_details=request.pop(util.camelize('ChangeCertificateAuthorityCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'certificates_management',
            'ChangeCertificateAuthorityCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_certificate_authority_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_certificates_us_grp@oracle.com" jiraProject="OCICERT" opsJiraProject="OCICERT"
def test_change_certificate_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('certificates_management', 'ChangeCertificateCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('certificates_management', util.camelize('certificates_management'), 'ChangeCertificateCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='certificates_management', api_name='ChangeCertificateCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.certificates_management.CertificatesManagementClient(config, service_endpoint=service_endpoint)
            response = client.change_certificate_compartment(
                certificate_id=request.pop(util.camelize('certificateId')),
                change_certificate_compartment_details=request.pop(util.camelize('ChangeCertificateCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'certificates_management',
            'ChangeCertificateCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_certificate_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_certificates_us_grp@oracle.com" jiraProject="OCICERT" opsJiraProject="OCICERT"
def test_create_ca_bundle(testing_service_client):
    if not testing_service_client.is_api_enabled('certificates_management', 'CreateCaBundle'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('certificates_management', util.camelize('certificates_management'), 'CreateCaBundle')
    )

    request_containers = testing_service_client.get_requests(service_name='certificates_management', api_name='CreateCaBundle')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.certificates_management.CertificatesManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_ca_bundle(
                create_ca_bundle_details=request.pop(util.camelize('CreateCaBundleDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'certificates_management',
            'CreateCaBundle',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'caBundle',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_certificates_us_grp@oracle.com" jiraProject="OCICERT" opsJiraProject="OCICERT"
def test_create_certificate(testing_service_client):
    if not testing_service_client.is_api_enabled('certificates_management', 'CreateCertificate'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('certificates_management', util.camelize('certificates_management'), 'CreateCertificate')
    )

    request_containers = testing_service_client.get_requests(service_name='certificates_management', api_name='CreateCertificate')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.certificates_management.CertificatesManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_certificate(
                create_certificate_details=request.pop(util.camelize('CreateCertificateDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'certificates_management',
            'CreateCertificate',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'certificate',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_certificates_us_grp@oracle.com" jiraProject="OCICERT" opsJiraProject="OCICERT"
def test_create_certificate_authority(testing_service_client):
    if not testing_service_client.is_api_enabled('certificates_management', 'CreateCertificateAuthority'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('certificates_management', util.camelize('certificates_management'), 'CreateCertificateAuthority')
    )

    request_containers = testing_service_client.get_requests(service_name='certificates_management', api_name='CreateCertificateAuthority')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.certificates_management.CertificatesManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_certificate_authority(
                create_certificate_authority_details=request.pop(util.camelize('CreateCertificateAuthorityDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'certificates_management',
            'CreateCertificateAuthority',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'certificateAuthority',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_certificates_us_grp@oracle.com" jiraProject="OCICERT" opsJiraProject="OCICERT"
def test_delete_ca_bundle(testing_service_client):
    if not testing_service_client.is_api_enabled('certificates_management', 'DeleteCaBundle'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('certificates_management', util.camelize('certificates_management'), 'DeleteCaBundle')
    )

    request_containers = testing_service_client.get_requests(service_name='certificates_management', api_name='DeleteCaBundle')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.certificates_management.CertificatesManagementClient(config, service_endpoint=service_endpoint)
            response = client.delete_ca_bundle(
                ca_bundle_id=request.pop(util.camelize('caBundleId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'certificates_management',
            'DeleteCaBundle',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_ca_bundle',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_certificates_us_grp@oracle.com" jiraProject="OCICERT" opsJiraProject="OCICERT"
def test_get_association(testing_service_client):
    if not testing_service_client.is_api_enabled('certificates_management', 'GetAssociation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('certificates_management', util.camelize('certificates_management'), 'GetAssociation')
    )

    request_containers = testing_service_client.get_requests(service_name='certificates_management', api_name='GetAssociation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.certificates_management.CertificatesManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_association(
                association_id=request.pop(util.camelize('associationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'certificates_management',
            'GetAssociation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'association',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_certificates_us_grp@oracle.com" jiraProject="OCICERT" opsJiraProject="OCICERT"
def test_get_ca_bundle(testing_service_client):
    if not testing_service_client.is_api_enabled('certificates_management', 'GetCaBundle'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('certificates_management', util.camelize('certificates_management'), 'GetCaBundle')
    )

    request_containers = testing_service_client.get_requests(service_name='certificates_management', api_name='GetCaBundle')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.certificates_management.CertificatesManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_ca_bundle(
                ca_bundle_id=request.pop(util.camelize('caBundleId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'certificates_management',
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
def test_get_certificate(testing_service_client):
    if not testing_service_client.is_api_enabled('certificates_management', 'GetCertificate'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('certificates_management', util.camelize('certificates_management'), 'GetCertificate')
    )

    request_containers = testing_service_client.get_requests(service_name='certificates_management', api_name='GetCertificate')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.certificates_management.CertificatesManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_certificate(
                certificate_id=request.pop(util.camelize('certificateId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'certificates_management',
            'GetCertificate',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'certificate',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_certificates_us_grp@oracle.com" jiraProject="OCICERT" opsJiraProject="OCICERT"
def test_get_certificate_authority(testing_service_client):
    if not testing_service_client.is_api_enabled('certificates_management', 'GetCertificateAuthority'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('certificates_management', util.camelize('certificates_management'), 'GetCertificateAuthority')
    )

    request_containers = testing_service_client.get_requests(service_name='certificates_management', api_name='GetCertificateAuthority')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.certificates_management.CertificatesManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_certificate_authority(
                certificate_authority_id=request.pop(util.camelize('certificateAuthorityId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'certificates_management',
            'GetCertificateAuthority',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'certificateAuthority',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_certificates_us_grp@oracle.com" jiraProject="OCICERT" opsJiraProject="OCICERT"
def test_get_certificate_authority_version(testing_service_client):
    if not testing_service_client.is_api_enabled('certificates_management', 'GetCertificateAuthorityVersion'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('certificates_management', util.camelize('certificates_management'), 'GetCertificateAuthorityVersion')
    )

    request_containers = testing_service_client.get_requests(service_name='certificates_management', api_name='GetCertificateAuthorityVersion')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.certificates_management.CertificatesManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_certificate_authority_version(
                certificate_authority_id=request.pop(util.camelize('certificateAuthorityId')),
                certificate_authority_version_number=request.pop(util.camelize('certificateAuthorityVersionNumber')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'certificates_management',
            'GetCertificateAuthorityVersion',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'certificateAuthorityVersion',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_certificates_us_grp@oracle.com" jiraProject="OCICERT" opsJiraProject="OCICERT"
def test_get_certificate_version(testing_service_client):
    if not testing_service_client.is_api_enabled('certificates_management', 'GetCertificateVersion'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('certificates_management', util.camelize('certificates_management'), 'GetCertificateVersion')
    )

    request_containers = testing_service_client.get_requests(service_name='certificates_management', api_name='GetCertificateVersion')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.certificates_management.CertificatesManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_certificate_version(
                certificate_id=request.pop(util.camelize('certificateId')),
                certificate_version_number=request.pop(util.camelize('certificateVersionNumber')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'certificates_management',
            'GetCertificateVersion',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'certificateVersion',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_certificates_us_grp@oracle.com" jiraProject="OCICERT" opsJiraProject="OCICERT"
def test_list_associations(testing_service_client):
    if not testing_service_client.is_api_enabled('certificates_management', 'ListAssociations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('certificates_management', util.camelize('certificates_management'), 'ListAssociations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='certificates_management', api_name='ListAssociations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.certificates_management.CertificatesManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_associations(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_associations(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_associations(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'certificates_management',
            'ListAssociations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'associationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_certificates_us_grp@oracle.com" jiraProject="OCICERT" opsJiraProject="OCICERT"
def test_list_ca_bundles(testing_service_client):
    if not testing_service_client.is_api_enabled('certificates_management', 'ListCaBundles'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('certificates_management', util.camelize('certificates_management'), 'ListCaBundles')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='certificates_management', api_name='ListCaBundles')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.certificates_management.CertificatesManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_ca_bundles(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_ca_bundles(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_ca_bundles(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'certificates_management',
            'ListCaBundles',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'caBundleCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_certificates_us_grp@oracle.com" jiraProject="OCICERT" opsJiraProject="OCICERT"
def test_list_certificate_authorities(testing_service_client):
    if not testing_service_client.is_api_enabled('certificates_management', 'ListCertificateAuthorities'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('certificates_management', util.camelize('certificates_management'), 'ListCertificateAuthorities')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='certificates_management', api_name='ListCertificateAuthorities')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.certificates_management.CertificatesManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_certificate_authorities(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_certificate_authorities(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_certificate_authorities(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'certificates_management',
            'ListCertificateAuthorities',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'certificateAuthorityCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_certificates_us_grp@oracle.com" jiraProject="OCICERT" opsJiraProject="OCICERT"
def test_list_certificate_authority_versions(testing_service_client):
    if not testing_service_client.is_api_enabled('certificates_management', 'ListCertificateAuthorityVersions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('certificates_management', util.camelize('certificates_management'), 'ListCertificateAuthorityVersions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='certificates_management', api_name='ListCertificateAuthorityVersions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.certificates_management.CertificatesManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_certificate_authority_versions(
                certificate_authority_id=request.pop(util.camelize('certificateAuthorityId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_certificate_authority_versions(
                    certificate_authority_id=request.pop(util.camelize('certificateAuthorityId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_certificate_authority_versions(
                        certificate_authority_id=request.pop(util.camelize('certificateAuthorityId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'certificates_management',
            'ListCertificateAuthorityVersions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'certificateAuthorityVersionCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_certificates_us_grp@oracle.com" jiraProject="OCICERT" opsJiraProject="OCICERT"
def test_list_certificate_versions(testing_service_client):
    if not testing_service_client.is_api_enabled('certificates_management', 'ListCertificateVersions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('certificates_management', util.camelize('certificates_management'), 'ListCertificateVersions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='certificates_management', api_name='ListCertificateVersions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.certificates_management.CertificatesManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_certificate_versions(
                certificate_id=request.pop(util.camelize('certificateId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_certificate_versions(
                    certificate_id=request.pop(util.camelize('certificateId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_certificate_versions(
                        certificate_id=request.pop(util.camelize('certificateId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'certificates_management',
            'ListCertificateVersions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'certificateVersionCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_certificates_us_grp@oracle.com" jiraProject="OCICERT" opsJiraProject="OCICERT"
def test_list_certificates(testing_service_client):
    if not testing_service_client.is_api_enabled('certificates_management', 'ListCertificates'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('certificates_management', util.camelize('certificates_management'), 'ListCertificates')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='certificates_management', api_name='ListCertificates')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.certificates_management.CertificatesManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_certificates(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_certificates(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_certificates(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'certificates_management',
            'ListCertificates',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'certificateCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_certificates_us_grp@oracle.com" jiraProject="OCICERT" opsJiraProject="OCICERT"
def test_revoke_certificate_authority_version(testing_service_client):
    if not testing_service_client.is_api_enabled('certificates_management', 'RevokeCertificateAuthorityVersion'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('certificates_management', util.camelize('certificates_management'), 'RevokeCertificateAuthorityVersion')
    )

    request_containers = testing_service_client.get_requests(service_name='certificates_management', api_name='RevokeCertificateAuthorityVersion')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.certificates_management.CertificatesManagementClient(config, service_endpoint=service_endpoint)
            response = client.revoke_certificate_authority_version(
                certificate_authority_id=request.pop(util.camelize('certificateAuthorityId')),
                certificate_authority_version_number=request.pop(util.camelize('certificateAuthorityVersionNumber')),
                revoke_certificate_authority_version_details=request.pop(util.camelize('RevokeCertificateAuthorityVersionDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'certificates_management',
            'RevokeCertificateAuthorityVersion',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'revoke_certificate_authority_version',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_certificates_us_grp@oracle.com" jiraProject="OCICERT" opsJiraProject="OCICERT"
def test_revoke_certificate_version(testing_service_client):
    if not testing_service_client.is_api_enabled('certificates_management', 'RevokeCertificateVersion'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('certificates_management', util.camelize('certificates_management'), 'RevokeCertificateVersion')
    )

    request_containers = testing_service_client.get_requests(service_name='certificates_management', api_name='RevokeCertificateVersion')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.certificates_management.CertificatesManagementClient(config, service_endpoint=service_endpoint)
            response = client.revoke_certificate_version(
                certificate_id=request.pop(util.camelize('certificateId')),
                certificate_version_number=request.pop(util.camelize('certificateVersionNumber')),
                revoke_certificate_version_details=request.pop(util.camelize('RevokeCertificateVersionDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'certificates_management',
            'RevokeCertificateVersion',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'revoke_certificate_version',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_certificates_us_grp@oracle.com" jiraProject="OCICERT" opsJiraProject="OCICERT"
def test_schedule_certificate_authority_deletion(testing_service_client):
    if not testing_service_client.is_api_enabled('certificates_management', 'ScheduleCertificateAuthorityDeletion'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('certificates_management', util.camelize('certificates_management'), 'ScheduleCertificateAuthorityDeletion')
    )

    request_containers = testing_service_client.get_requests(service_name='certificates_management', api_name='ScheduleCertificateAuthorityDeletion')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.certificates_management.CertificatesManagementClient(config, service_endpoint=service_endpoint)
            response = client.schedule_certificate_authority_deletion(
                certificate_authority_id=request.pop(util.camelize('certificateAuthorityId')),
                schedule_certificate_authority_deletion_details=request.pop(util.camelize('ScheduleCertificateAuthorityDeletionDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'certificates_management',
            'ScheduleCertificateAuthorityDeletion',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'schedule_certificate_authority_deletion',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_certificates_us_grp@oracle.com" jiraProject="OCICERT" opsJiraProject="OCICERT"
def test_schedule_certificate_authority_version_deletion(testing_service_client):
    if not testing_service_client.is_api_enabled('certificates_management', 'ScheduleCertificateAuthorityVersionDeletion'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('certificates_management', util.camelize('certificates_management'), 'ScheduleCertificateAuthorityVersionDeletion')
    )

    request_containers = testing_service_client.get_requests(service_name='certificates_management', api_name='ScheduleCertificateAuthorityVersionDeletion')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.certificates_management.CertificatesManagementClient(config, service_endpoint=service_endpoint)
            response = client.schedule_certificate_authority_version_deletion(
                certificate_authority_id=request.pop(util.camelize('certificateAuthorityId')),
                certificate_authority_version_number=request.pop(util.camelize('certificateAuthorityVersionNumber')),
                schedule_certificate_authority_version_deletion_details=request.pop(util.camelize('ScheduleCertificateAuthorityVersionDeletionDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'certificates_management',
            'ScheduleCertificateAuthorityVersionDeletion',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'schedule_certificate_authority_version_deletion',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_certificates_us_grp@oracle.com" jiraProject="OCICERT" opsJiraProject="OCICERT"
def test_schedule_certificate_deletion(testing_service_client):
    if not testing_service_client.is_api_enabled('certificates_management', 'ScheduleCertificateDeletion'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('certificates_management', util.camelize('certificates_management'), 'ScheduleCertificateDeletion')
    )

    request_containers = testing_service_client.get_requests(service_name='certificates_management', api_name='ScheduleCertificateDeletion')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.certificates_management.CertificatesManagementClient(config, service_endpoint=service_endpoint)
            response = client.schedule_certificate_deletion(
                certificate_id=request.pop(util.camelize('certificateId')),
                schedule_certificate_deletion_details=request.pop(util.camelize('ScheduleCertificateDeletionDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'certificates_management',
            'ScheduleCertificateDeletion',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'schedule_certificate_deletion',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_certificates_us_grp@oracle.com" jiraProject="OCICERT" opsJiraProject="OCICERT"
def test_schedule_certificate_version_deletion(testing_service_client):
    if not testing_service_client.is_api_enabled('certificates_management', 'ScheduleCertificateVersionDeletion'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('certificates_management', util.camelize('certificates_management'), 'ScheduleCertificateVersionDeletion')
    )

    request_containers = testing_service_client.get_requests(service_name='certificates_management', api_name='ScheduleCertificateVersionDeletion')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.certificates_management.CertificatesManagementClient(config, service_endpoint=service_endpoint)
            response = client.schedule_certificate_version_deletion(
                certificate_id=request.pop(util.camelize('certificateId')),
                certificate_version_number=request.pop(util.camelize('certificateVersionNumber')),
                schedule_certificate_version_deletion_details=request.pop(util.camelize('ScheduleCertificateVersionDeletionDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'certificates_management',
            'ScheduleCertificateVersionDeletion',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'schedule_certificate_version_deletion',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_certificates_us_grp@oracle.com" jiraProject="OCICERT" opsJiraProject="OCICERT"
def test_update_ca_bundle(testing_service_client):
    if not testing_service_client.is_api_enabled('certificates_management', 'UpdateCaBundle'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('certificates_management', util.camelize('certificates_management'), 'UpdateCaBundle')
    )

    request_containers = testing_service_client.get_requests(service_name='certificates_management', api_name='UpdateCaBundle')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.certificates_management.CertificatesManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_ca_bundle(
                ca_bundle_id=request.pop(util.camelize('caBundleId')),
                update_ca_bundle_details=request.pop(util.camelize('UpdateCaBundleDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'certificates_management',
            'UpdateCaBundle',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'caBundle',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_certificates_us_grp@oracle.com" jiraProject="OCICERT" opsJiraProject="OCICERT"
def test_update_certificate(testing_service_client):
    if not testing_service_client.is_api_enabled('certificates_management', 'UpdateCertificate'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('certificates_management', util.camelize('certificates_management'), 'UpdateCertificate')
    )

    request_containers = testing_service_client.get_requests(service_name='certificates_management', api_name='UpdateCertificate')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.certificates_management.CertificatesManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_certificate(
                certificate_id=request.pop(util.camelize('certificateId')),
                update_certificate_details=request.pop(util.camelize('UpdateCertificateDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'certificates_management',
            'UpdateCertificate',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'certificate',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_certificates_us_grp@oracle.com" jiraProject="OCICERT" opsJiraProject="OCICERT"
def test_update_certificate_authority(testing_service_client):
    if not testing_service_client.is_api_enabled('certificates_management', 'UpdateCertificateAuthority'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('certificates_management', util.camelize('certificates_management'), 'UpdateCertificateAuthority')
    )

    request_containers = testing_service_client.get_requests(service_name='certificates_management', api_name='UpdateCertificateAuthority')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.certificates_management.CertificatesManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_certificate_authority(
                certificate_authority_id=request.pop(util.camelize('certificateAuthorityId')),
                update_certificate_authority_details=request.pop(util.camelize('UpdateCertificateAuthorityDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'certificates_management',
            'UpdateCertificateAuthority',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'certificateAuthority',
            False,
            False
        )
