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

        cassette_location = os.path.join('generated', 'blockchain_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="bcs_devops_ww_grp@oracle.com" jiraProject="OBP" opsJiraProject="OBP"
def test_change_blockchain_platform_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('blockchain', 'ChangeBlockchainPlatformCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('blockchain', util.camelize('blockchain_platform'), 'ChangeBlockchainPlatformCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='blockchain', api_name='ChangeBlockchainPlatformCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.blockchain.BlockchainPlatformClient(config, service_endpoint=service_endpoint)
            response = client.change_blockchain_platform_compartment(
                blockchain_platform_id=request.pop(util.camelize('blockchainPlatformId')),
                change_blockchain_platform_compartment_details=request.pop(util.camelize('ChangeBlockchainPlatformCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'blockchain',
            'ChangeBlockchainPlatformCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_blockchain_platform_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bcs_devops_ww_grp@oracle.com" jiraProject="OBP" opsJiraProject="OBP"
def test_create_blockchain_platform(testing_service_client):
    if not testing_service_client.is_api_enabled('blockchain', 'CreateBlockchainPlatform'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('blockchain', util.camelize('blockchain_platform'), 'CreateBlockchainPlatform')
    )

    request_containers = testing_service_client.get_requests(service_name='blockchain', api_name='CreateBlockchainPlatform')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.blockchain.BlockchainPlatformClient(config, service_endpoint=service_endpoint)
            response = client.create_blockchain_platform(
                create_blockchain_platform_details=request.pop(util.camelize('CreateBlockchainPlatformDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'blockchain',
            'CreateBlockchainPlatform',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_blockchain_platform',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bcs_devops_ww_grp@oracle.com" jiraProject="OBP" opsJiraProject="OBP"
def test_create_osn(testing_service_client):
    if not testing_service_client.is_api_enabled('blockchain', 'CreateOsn'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('blockchain', util.camelize('blockchain_platform'), 'CreateOsn')
    )

    request_containers = testing_service_client.get_requests(service_name='blockchain', api_name='CreateOsn')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.blockchain.BlockchainPlatformClient(config, service_endpoint=service_endpoint)
            response = client.create_osn(
                blockchain_platform_id=request.pop(util.camelize('blockchainPlatformId')),
                create_osn_details=request.pop(util.camelize('CreateOsnDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'blockchain',
            'CreateOsn',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_osn',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bcs_devops_ww_grp@oracle.com" jiraProject="OBP" opsJiraProject="OBP"
def test_create_peer(testing_service_client):
    if not testing_service_client.is_api_enabled('blockchain', 'CreatePeer'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('blockchain', util.camelize('blockchain_platform'), 'CreatePeer')
    )

    request_containers = testing_service_client.get_requests(service_name='blockchain', api_name='CreatePeer')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.blockchain.BlockchainPlatformClient(config, service_endpoint=service_endpoint)
            response = client.create_peer(
                blockchain_platform_id=request.pop(util.camelize('blockchainPlatformId')),
                create_peer_details=request.pop(util.camelize('CreatePeerDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'blockchain',
            'CreatePeer',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_peer',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bcs_devops_ww_grp@oracle.com" jiraProject="OBP" opsJiraProject="OBP"
def test_delete_blockchain_platform(testing_service_client):
    if not testing_service_client.is_api_enabled('blockchain', 'DeleteBlockchainPlatform'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('blockchain', util.camelize('blockchain_platform'), 'DeleteBlockchainPlatform')
    )

    request_containers = testing_service_client.get_requests(service_name='blockchain', api_name='DeleteBlockchainPlatform')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.blockchain.BlockchainPlatformClient(config, service_endpoint=service_endpoint)
            response = client.delete_blockchain_platform(
                blockchain_platform_id=request.pop(util.camelize('blockchainPlatformId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'blockchain',
            'DeleteBlockchainPlatform',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_blockchain_platform',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="bcs_devops_ww_grp@oracle.com" jiraProject="OBP" opsJiraProject="OBP"
def test_delete_osn(testing_service_client):
    if not testing_service_client.is_api_enabled('blockchain', 'DeleteOsn'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('blockchain', util.camelize('blockchain_platform'), 'DeleteOsn')
    )

    request_containers = testing_service_client.get_requests(service_name='blockchain', api_name='DeleteOsn')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.blockchain.BlockchainPlatformClient(config, service_endpoint=service_endpoint)
            response = client.delete_osn(
                blockchain_platform_id=request.pop(util.camelize('blockchainPlatformId')),
                osn_id=request.pop(util.camelize('osnId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'blockchain',
            'DeleteOsn',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_osn',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="bcs_devops_ww_grp@oracle.com" jiraProject="OBP" opsJiraProject="OBP"
def test_delete_peer(testing_service_client):
    if not testing_service_client.is_api_enabled('blockchain', 'DeletePeer'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('blockchain', util.camelize('blockchain_platform'), 'DeletePeer')
    )

    request_containers = testing_service_client.get_requests(service_name='blockchain', api_name='DeletePeer')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.blockchain.BlockchainPlatformClient(config, service_endpoint=service_endpoint)
            response = client.delete_peer(
                blockchain_platform_id=request.pop(util.camelize('blockchainPlatformId')),
                peer_id=request.pop(util.camelize('peerId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'blockchain',
            'DeletePeer',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_peer',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="bcs_devops_ww_grp@oracle.com" jiraProject="OBP" opsJiraProject="OBP"
def test_delete_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('blockchain', 'DeleteWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('blockchain', util.camelize('blockchain_platform'), 'DeleteWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='blockchain', api_name='DeleteWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.blockchain.BlockchainPlatformClient(config, service_endpoint=service_endpoint)
            response = client.delete_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'blockchain',
            'DeleteWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_work_request',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="bcs_devops_ww_grp@oracle.com" jiraProject="OBP" opsJiraProject="OBP"
def test_get_blockchain_platform(testing_service_client):
    if not testing_service_client.is_api_enabled('blockchain', 'GetBlockchainPlatform'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('blockchain', util.camelize('blockchain_platform'), 'GetBlockchainPlatform')
    )

    request_containers = testing_service_client.get_requests(service_name='blockchain', api_name='GetBlockchainPlatform')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.blockchain.BlockchainPlatformClient(config, service_endpoint=service_endpoint)
            response = client.get_blockchain_platform(
                blockchain_platform_id=request.pop(util.camelize('blockchainPlatformId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'blockchain',
            'GetBlockchainPlatform',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'blockchainPlatform',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bcs_devops_ww_grp@oracle.com" jiraProject="OBP" opsJiraProject="OBP"
def test_get_osn(testing_service_client):
    if not testing_service_client.is_api_enabled('blockchain', 'GetOsn'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('blockchain', util.camelize('blockchain_platform'), 'GetOsn')
    )

    request_containers = testing_service_client.get_requests(service_name='blockchain', api_name='GetOsn')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.blockchain.BlockchainPlatformClient(config, service_endpoint=service_endpoint)
            response = client.get_osn(
                blockchain_platform_id=request.pop(util.camelize('blockchainPlatformId')),
                osn_id=request.pop(util.camelize('osnId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'blockchain',
            'GetOsn',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'osn',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bcs_devops_ww_grp@oracle.com" jiraProject="OBP" opsJiraProject="OBP"
def test_get_peer(testing_service_client):
    if not testing_service_client.is_api_enabled('blockchain', 'GetPeer'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('blockchain', util.camelize('blockchain_platform'), 'GetPeer')
    )

    request_containers = testing_service_client.get_requests(service_name='blockchain', api_name='GetPeer')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.blockchain.BlockchainPlatformClient(config, service_endpoint=service_endpoint)
            response = client.get_peer(
                blockchain_platform_id=request.pop(util.camelize('blockchainPlatformId')),
                peer_id=request.pop(util.camelize('peerId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'blockchain',
            'GetPeer',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'peer',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bcs_devops_ww_grp@oracle.com" jiraProject="OBP" opsJiraProject="OBP"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('blockchain', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('blockchain', util.camelize('blockchain_platform'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='blockchain', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.blockchain.BlockchainPlatformClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'blockchain',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bcs_devops_ww_grp@oracle.com" jiraProject="OBP" opsJiraProject="OBP"
def test_list_blockchain_platform_patches(testing_service_client):
    if not testing_service_client.is_api_enabled('blockchain', 'ListBlockchainPlatformPatches'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('blockchain', util.camelize('blockchain_platform'), 'ListBlockchainPlatformPatches')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='blockchain', api_name='ListBlockchainPlatformPatches')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.blockchain.BlockchainPlatformClient(config, service_endpoint=service_endpoint)
            response = client.list_blockchain_platform_patches(
                blockchain_platform_id=request.pop(util.camelize('blockchainPlatformId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_blockchain_platform_patches(
                    blockchain_platform_id=request.pop(util.camelize('blockchainPlatformId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_blockchain_platform_patches(
                        blockchain_platform_id=request.pop(util.camelize('blockchainPlatformId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'blockchain',
            'ListBlockchainPlatformPatches',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'blockchainPlatformPatchCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="bcs_devops_ww_grp@oracle.com" jiraProject="OBP" opsJiraProject="OBP"
def test_list_blockchain_platforms(testing_service_client):
    if not testing_service_client.is_api_enabled('blockchain', 'ListBlockchainPlatforms'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('blockchain', util.camelize('blockchain_platform'), 'ListBlockchainPlatforms')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='blockchain', api_name='ListBlockchainPlatforms')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.blockchain.BlockchainPlatformClient(config, service_endpoint=service_endpoint)
            response = client.list_blockchain_platforms(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_blockchain_platforms(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_blockchain_platforms(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'blockchain',
            'ListBlockchainPlatforms',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'blockchainPlatformCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="bcs_devops_ww_grp@oracle.com" jiraProject="OBP" opsJiraProject="OBP"
def test_list_osns(testing_service_client):
    if not testing_service_client.is_api_enabled('blockchain', 'ListOsns'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('blockchain', util.camelize('blockchain_platform'), 'ListOsns')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='blockchain', api_name='ListOsns')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.blockchain.BlockchainPlatformClient(config, service_endpoint=service_endpoint)
            response = client.list_osns(
                blockchain_platform_id=request.pop(util.camelize('blockchainPlatformId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_osns(
                    blockchain_platform_id=request.pop(util.camelize('blockchainPlatformId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_osns(
                        blockchain_platform_id=request.pop(util.camelize('blockchainPlatformId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'blockchain',
            'ListOsns',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'osnCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="bcs_devops_ww_grp@oracle.com" jiraProject="OBP" opsJiraProject="OBP"
def test_list_peers(testing_service_client):
    if not testing_service_client.is_api_enabled('blockchain', 'ListPeers'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('blockchain', util.camelize('blockchain_platform'), 'ListPeers')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='blockchain', api_name='ListPeers')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.blockchain.BlockchainPlatformClient(config, service_endpoint=service_endpoint)
            response = client.list_peers(
                blockchain_platform_id=request.pop(util.camelize('blockchainPlatformId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_peers(
                    blockchain_platform_id=request.pop(util.camelize('blockchainPlatformId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_peers(
                        blockchain_platform_id=request.pop(util.camelize('blockchainPlatformId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'blockchain',
            'ListPeers',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'peerCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="bcs_devops_ww_grp@oracle.com" jiraProject="OBP" opsJiraProject="OBP"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('blockchain', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('blockchain', util.camelize('blockchain_platform'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='blockchain', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.blockchain.BlockchainPlatformClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_errors(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_errors(
                    work_request_id=request.pop(util.camelize('workRequestId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_request_errors(
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'blockchain',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestErrorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="bcs_devops_ww_grp@oracle.com" jiraProject="OBP" opsJiraProject="OBP"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('blockchain', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('blockchain', util.camelize('blockchain_platform'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='blockchain', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.blockchain.BlockchainPlatformClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_logs(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_logs(
                    work_request_id=request.pop(util.camelize('workRequestId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_request_logs(
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'blockchain',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="bcs_devops_ww_grp@oracle.com" jiraProject="OBP" opsJiraProject="OBP"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('blockchain', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('blockchain', util.camelize('blockchain_platform'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='blockchain', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.blockchain.BlockchainPlatformClient(config, service_endpoint=service_endpoint)
            response = client.list_work_requests(
                compartment_id=request.pop(util.camelize('compartmentId')),
                blockchain_platform_id=request.pop(util.camelize('blockchainPlatformId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_requests(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    blockchain_platform_id=request.pop(util.camelize('blockchainPlatformId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_requests(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        blockchain_platform_id=request.pop(util.camelize('blockchainPlatformId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'blockchain',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="bcs_devops_ww_grp@oracle.com" jiraProject="OBP" opsJiraProject="OBP"
def test_preview_scale_blockchain_platform(testing_service_client):
    if not testing_service_client.is_api_enabled('blockchain', 'PreviewScaleBlockchainPlatform'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('blockchain', util.camelize('blockchain_platform'), 'PreviewScaleBlockchainPlatform')
    )

    request_containers = testing_service_client.get_requests(service_name='blockchain', api_name='PreviewScaleBlockchainPlatform')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.blockchain.BlockchainPlatformClient(config, service_endpoint=service_endpoint)
            response = client.preview_scale_blockchain_platform(
                blockchain_platform_id=request.pop(util.camelize('blockchainPlatformId')),
                scale_blockchain_platform_details=request.pop(util.camelize('ScaleBlockchainPlatformDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'blockchain',
            'PreviewScaleBlockchainPlatform',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'scaledBlockchainPlatformPreview',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bcs_devops_ww_grp@oracle.com" jiraProject="OBP" opsJiraProject="OBP"
def test_scale_blockchain_platform(testing_service_client):
    if not testing_service_client.is_api_enabled('blockchain', 'ScaleBlockchainPlatform'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('blockchain', util.camelize('blockchain_platform'), 'ScaleBlockchainPlatform')
    )

    request_containers = testing_service_client.get_requests(service_name='blockchain', api_name='ScaleBlockchainPlatform')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.blockchain.BlockchainPlatformClient(config, service_endpoint=service_endpoint)
            response = client.scale_blockchain_platform(
                blockchain_platform_id=request.pop(util.camelize('blockchainPlatformId')),
                scale_blockchain_platform_details=request.pop(util.camelize('ScaleBlockchainPlatformDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'blockchain',
            'ScaleBlockchainPlatform',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'scale_blockchain_platform',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bcs_devops_ww_grp@oracle.com" jiraProject="OBP" opsJiraProject="OBP"
def test_start_blockchain_platform(testing_service_client):
    if not testing_service_client.is_api_enabled('blockchain', 'StartBlockchainPlatform'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('blockchain', util.camelize('blockchain_platform'), 'StartBlockchainPlatform')
    )

    request_containers = testing_service_client.get_requests(service_name='blockchain', api_name='StartBlockchainPlatform')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.blockchain.BlockchainPlatformClient(config, service_endpoint=service_endpoint)
            response = client.start_blockchain_platform(
                blockchain_platform_id=request.pop(util.camelize('blockchainPlatformId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'blockchain',
            'StartBlockchainPlatform',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'start_blockchain_platform',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bcs_devops_ww_grp@oracle.com" jiraProject="OBP" opsJiraProject="OBP"
def test_stop_blockchain_platform(testing_service_client):
    if not testing_service_client.is_api_enabled('blockchain', 'StopBlockchainPlatform'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('blockchain', util.camelize('blockchain_platform'), 'StopBlockchainPlatform')
    )

    request_containers = testing_service_client.get_requests(service_name='blockchain', api_name='StopBlockchainPlatform')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.blockchain.BlockchainPlatformClient(config, service_endpoint=service_endpoint)
            response = client.stop_blockchain_platform(
                blockchain_platform_id=request.pop(util.camelize('blockchainPlatformId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'blockchain',
            'StopBlockchainPlatform',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stop_blockchain_platform',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bcs_devops_ww_grp@oracle.com" jiraProject="OBP" opsJiraProject="OBP"
def test_update_blockchain_platform(testing_service_client):
    if not testing_service_client.is_api_enabled('blockchain', 'UpdateBlockchainPlatform'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('blockchain', util.camelize('blockchain_platform'), 'UpdateBlockchainPlatform')
    )

    request_containers = testing_service_client.get_requests(service_name='blockchain', api_name='UpdateBlockchainPlatform')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.blockchain.BlockchainPlatformClient(config, service_endpoint=service_endpoint)
            response = client.update_blockchain_platform(
                update_blockchain_platform_details=request.pop(util.camelize('UpdateBlockchainPlatformDetails')),
                blockchain_platform_id=request.pop(util.camelize('blockchainPlatformId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'blockchain',
            'UpdateBlockchainPlatform',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_blockchain_platform',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bcs_devops_ww_grp@oracle.com" jiraProject="OBP" opsJiraProject="OBP"
def test_update_osn(testing_service_client):
    if not testing_service_client.is_api_enabled('blockchain', 'UpdateOsn'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('blockchain', util.camelize('blockchain_platform'), 'UpdateOsn')
    )

    request_containers = testing_service_client.get_requests(service_name='blockchain', api_name='UpdateOsn')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.blockchain.BlockchainPlatformClient(config, service_endpoint=service_endpoint)
            response = client.update_osn(
                blockchain_platform_id=request.pop(util.camelize('blockchainPlatformId')),
                osn_id=request.pop(util.camelize('osnId')),
                update_osn_details=request.pop(util.camelize('UpdateOsnDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'blockchain',
            'UpdateOsn',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_osn',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bcs_devops_ww_grp@oracle.com" jiraProject="OBP" opsJiraProject="OBP"
def test_update_peer(testing_service_client):
    if not testing_service_client.is_api_enabled('blockchain', 'UpdatePeer'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('blockchain', util.camelize('blockchain_platform'), 'UpdatePeer')
    )

    request_containers = testing_service_client.get_requests(service_name='blockchain', api_name='UpdatePeer')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.blockchain.BlockchainPlatformClient(config, service_endpoint=service_endpoint)
            response = client.update_peer(
                blockchain_platform_id=request.pop(util.camelize('blockchainPlatformId')),
                peer_id=request.pop(util.camelize('peerId')),
                update_peer_details=request.pop(util.camelize('UpdatePeerDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'blockchain',
            'UpdatePeer',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_peer',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="bcs_devops_ww_grp@oracle.com" jiraProject="OBP" opsJiraProject="OBP"
def test_upgrade_blockchain_platform(testing_service_client):
    if not testing_service_client.is_api_enabled('blockchain', 'UpgradeBlockchainPlatform'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('blockchain', util.camelize('blockchain_platform'), 'UpgradeBlockchainPlatform')
    )

    request_containers = testing_service_client.get_requests(service_name='blockchain', api_name='UpgradeBlockchainPlatform')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.blockchain.BlockchainPlatformClient(config, service_endpoint=service_endpoint)
            response = client.upgrade_blockchain_platform(
                upgrade_blockchain_platform_details=request.pop(util.camelize('UpgradeBlockchainPlatformDetails')),
                blockchain_platform_id=request.pop(util.camelize('blockchainPlatformId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'blockchain',
            'UpgradeBlockchainPlatform',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'upgrade_blockchain_platform',
            False,
            False
        )
