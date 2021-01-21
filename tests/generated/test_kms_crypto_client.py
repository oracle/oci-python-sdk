# Code generated. DO NOT EDIT.
# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
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

        cassette_location = os.path.join('generated', 'key_management_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="sparta_kms_us_grp@oracle.com" jiraProject="KMS" opsJiraProject="KMS"
def test_decrypt(testing_service_client):
    if not testing_service_client.is_api_enabled('key_management', 'Decrypt'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('key_management', util.camelize('kms_crypto'), 'Decrypt')
    )

    request_containers = testing_service_client.get_requests(service_name='key_management', api_name='Decrypt')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("key_management", "KmsCryptoClient", "Decrypt")
            client = oci.key_management.KmsCryptoClient(config, service_endpoint=service_endpoint)
            response = client.decrypt(
                decrypt_data_details=request.pop(util.camelize('DecryptDataDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'key_management',
            'Decrypt',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'decryptedData',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sparta_kms_us_grp@oracle.com" jiraProject="KMS" opsJiraProject="KMS"
def test_encrypt(testing_service_client):
    if not testing_service_client.is_api_enabled('key_management', 'Encrypt'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('key_management', util.camelize('kms_crypto'), 'Encrypt')
    )

    request_containers = testing_service_client.get_requests(service_name='key_management', api_name='Encrypt')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("key_management", "KmsCryptoClient", "Encrypt")
            client = oci.key_management.KmsCryptoClient(config, service_endpoint=service_endpoint)
            response = client.encrypt(
                encrypt_data_details=request.pop(util.camelize('EncryptDataDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'key_management',
            'Encrypt',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'encryptedData',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sparta_kms_us_grp@oracle.com" jiraProject="KMS" opsJiraProject="KMS"
def test_export_key(testing_service_client):
    if not testing_service_client.is_api_enabled('key_management', 'ExportKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('key_management', util.camelize('kms_crypto'), 'ExportKey')
    )

    request_containers = testing_service_client.get_requests(service_name='key_management', api_name='ExportKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("key_management", "KmsCryptoClient", "ExportKey")
            client = oci.key_management.KmsCryptoClient(config, service_endpoint=service_endpoint)
            response = client.export_key(
                export_key_details=request.pop(util.camelize('ExportKeyDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'key_management',
            'ExportKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'exportedKeyData',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sparta_kms_us_grp@oracle.com" jiraProject="KMS" opsJiraProject="KMS"
def test_generate_data_encryption_key(testing_service_client):
    if not testing_service_client.is_api_enabled('key_management', 'GenerateDataEncryptionKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('key_management', util.camelize('kms_crypto'), 'GenerateDataEncryptionKey')
    )

    request_containers = testing_service_client.get_requests(service_name='key_management', api_name='GenerateDataEncryptionKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("key_management", "KmsCryptoClient", "GenerateDataEncryptionKey")
            client = oci.key_management.KmsCryptoClient(config, service_endpoint=service_endpoint)
            response = client.generate_data_encryption_key(
                generate_key_details=request.pop(util.camelize('GenerateKeyDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'key_management',
            'GenerateDataEncryptionKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'generatedKey',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sparta_kms_us_grp@oracle.com" jiraProject="KMS" opsJiraProject="KMS"
def test_sign(testing_service_client):
    if not testing_service_client.is_api_enabled('key_management', 'Sign'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('key_management', util.camelize('kms_crypto'), 'Sign')
    )

    request_containers = testing_service_client.get_requests(service_name='key_management', api_name='Sign')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("key_management", "KmsCryptoClient", "Sign")
            client = oci.key_management.KmsCryptoClient(config, service_endpoint=service_endpoint)
            response = client.sign(
                sign_data_details=request.pop(util.camelize('SignDataDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'key_management',
            'Sign',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'signedData',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sparta_kms_us_grp@oracle.com" jiraProject="KMS" opsJiraProject="KMS"
def test_verify(testing_service_client):
    if not testing_service_client.is_api_enabled('key_management', 'Verify'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('key_management', util.camelize('kms_crypto'), 'Verify')
    )

    request_containers = testing_service_client.get_requests(service_name='key_management', api_name='Verify')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("key_management", "KmsCryptoClient", "Verify")
            client = oci.key_management.KmsCryptoClient(config, service_endpoint=service_endpoint)
            response = client.verify(
                verify_data_details=request.pop(util.camelize('VerifyDataDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'key_management',
            'Verify',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'verifiedData',
            False,
            False
        )
