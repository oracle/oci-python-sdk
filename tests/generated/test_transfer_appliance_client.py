# Code generated. DO NOT EDIT.
# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
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

        cassette_location = os.path.join('generated', 'dts_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="data_transfer_platform_dev_ww_grp@oracle.com" jiraProject="BDTS" opsJiraProject="DTS"
def test_create_transfer_appliance(testing_service_client):
    if not testing_service_client.is_api_enabled('dts', 'CreateTransferAppliance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dts', util.camelize('transfer_appliance'), 'CreateTransferAppliance')
    )

    request_containers = testing_service_client.get_requests(service_name='dts', api_name='CreateTransferAppliance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dts.TransferApplianceClient(config, service_endpoint=service_endpoint)
            response = client.create_transfer_appliance(
                id=request.pop(util.camelize('id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dts',
            'CreateTransferAppliance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'transferAppliance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="data_transfer_platform_dev_ww_grp@oracle.com" jiraProject="BDTS" opsJiraProject="DTS"
def test_create_transfer_appliance_admin_credentials(testing_service_client):
    if not testing_service_client.is_api_enabled('dts', 'CreateTransferApplianceAdminCredentials'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dts', util.camelize('transfer_appliance'), 'CreateTransferApplianceAdminCredentials')
    )

    request_containers = testing_service_client.get_requests(service_name='dts', api_name='CreateTransferApplianceAdminCredentials')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dts.TransferApplianceClient(config, service_endpoint=service_endpoint)
            response = client.create_transfer_appliance_admin_credentials(
                id=request.pop(util.camelize('id')),
                transfer_appliance_label=request.pop(util.camelize('transferApplianceLabel')),
                admin_public_key=request.pop(util.camelize('adminPublicKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dts',
            'CreateTransferApplianceAdminCredentials',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'transferApplianceCertificate',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="data_transfer_platform_dev_ww_grp@oracle.com" jiraProject="BDTS" opsJiraProject="DTS"
def test_delete_transfer_appliance(testing_service_client):
    if not testing_service_client.is_api_enabled('dts', 'DeleteTransferAppliance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dts', util.camelize('transfer_appliance'), 'DeleteTransferAppliance')
    )

    request_containers = testing_service_client.get_requests(service_name='dts', api_name='DeleteTransferAppliance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dts.TransferApplianceClient(config, service_endpoint=service_endpoint)
            response = client.delete_transfer_appliance(
                id=request.pop(util.camelize('id')),
                transfer_appliance_label=request.pop(util.camelize('transferApplianceLabel')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dts',
            'DeleteTransferAppliance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_transfer_appliance',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="data_transfer_platform_dev_ww_grp@oracle.com" jiraProject="BDTS" opsJiraProject="DTS"
def test_get_transfer_appliance(testing_service_client):
    if not testing_service_client.is_api_enabled('dts', 'GetTransferAppliance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dts', util.camelize('transfer_appliance'), 'GetTransferAppliance')
    )

    request_containers = testing_service_client.get_requests(service_name='dts', api_name='GetTransferAppliance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dts.TransferApplianceClient(config, service_endpoint=service_endpoint)
            response = client.get_transfer_appliance(
                id=request.pop(util.camelize('id')),
                transfer_appliance_label=request.pop(util.camelize('transferApplianceLabel')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dts',
            'GetTransferAppliance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'transferAppliance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="data_transfer_platform_dev_ww_grp@oracle.com" jiraProject="BDTS" opsJiraProject="DTS"
def test_get_transfer_appliance_certificate_authority_certificate(testing_service_client):
    if not testing_service_client.is_api_enabled('dts', 'GetTransferApplianceCertificateAuthorityCertificate'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dts', util.camelize('transfer_appliance'), 'GetTransferApplianceCertificateAuthorityCertificate')
    )

    request_containers = testing_service_client.get_requests(service_name='dts', api_name='GetTransferApplianceCertificateAuthorityCertificate')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dts.TransferApplianceClient(config, service_endpoint=service_endpoint)
            response = client.get_transfer_appliance_certificate_authority_certificate(
                id=request.pop(util.camelize('id')),
                transfer_appliance_label=request.pop(util.camelize('transferApplianceLabel')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dts',
            'GetTransferApplianceCertificateAuthorityCertificate',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'transferApplianceCertificate',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="data_transfer_platform_dev_ww_grp@oracle.com" jiraProject="BDTS" opsJiraProject="DTS"
def test_get_transfer_appliance_encryption_passphrase(testing_service_client):
    if not testing_service_client.is_api_enabled('dts', 'GetTransferApplianceEncryptionPassphrase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dts', util.camelize('transfer_appliance'), 'GetTransferApplianceEncryptionPassphrase')
    )

    request_containers = testing_service_client.get_requests(service_name='dts', api_name='GetTransferApplianceEncryptionPassphrase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dts.TransferApplianceClient(config, service_endpoint=service_endpoint)
            response = client.get_transfer_appliance_encryption_passphrase(
                id=request.pop(util.camelize('id')),
                transfer_appliance_label=request.pop(util.camelize('transferApplianceLabel')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dts',
            'GetTransferApplianceEncryptionPassphrase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'transferApplianceEncryptionPassphrase',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="data_transfer_platform_dev_ww_grp@oracle.com" jiraProject="BDTS" opsJiraProject="DTS"
def test_list_transfer_appliances(testing_service_client):
    if not testing_service_client.is_api_enabled('dts', 'ListTransferAppliances'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dts', util.camelize('transfer_appliance'), 'ListTransferAppliances')
    )

    request_containers = testing_service_client.get_requests(service_name='dts', api_name='ListTransferAppliances')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dts.TransferApplianceClient(config, service_endpoint=service_endpoint)
            response = client.list_transfer_appliances(
                id=request.pop(util.camelize('id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dts',
            'ListTransferAppliances',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'multipleTransferAppliances',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="data_transfer_platform_dev_ww_grp@oracle.com" jiraProject="BDTS" opsJiraProject="DTS"
def test_update_transfer_appliance(testing_service_client):
    if not testing_service_client.is_api_enabled('dts', 'UpdateTransferAppliance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('dts', util.camelize('transfer_appliance'), 'UpdateTransferAppliance')
    )

    request_containers = testing_service_client.get_requests(service_name='dts', api_name='UpdateTransferAppliance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.dts.TransferApplianceClient(config, service_endpoint=service_endpoint)
            response = client.update_transfer_appliance(
                id=request.pop(util.camelize('id')),
                transfer_appliance_label=request.pop(util.camelize('transferApplianceLabel')),
                update_transfer_appliance_details=request.pop(util.camelize('UpdateTransferApplianceDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'dts',
            'UpdateTransferAppliance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'transferAppliance',
            False,
            False
        )
