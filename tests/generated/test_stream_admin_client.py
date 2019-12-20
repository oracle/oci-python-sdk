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

        cassette_location = os.path.join('generated', 'streaming_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="opc_streaming_us_grp@oracle.com" jiraProject="STREAMSTR" opsJiraProject="STREAMOSS"
def test_change_connect_harness_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('streaming', 'ChangeConnectHarnessCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('streaming', util.camelize('stream_admin'), 'ChangeConnectHarnessCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='ChangeConnectHarnessCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.streaming.StreamAdminClient(config, service_endpoint=service_endpoint)
            response = client.change_connect_harness_compartment(
                connect_harness_id=request.pop(util.camelize('connectHarnessId')),
                change_connect_harness_compartment_details=request.pop(util.camelize('ChangeConnectHarnessCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'streaming',
            'ChangeConnectHarnessCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_connect_harness_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_streaming_us_grp@oracle.com" jiraProject="STREAMSTR" opsJiraProject="STREAMOSS"
def test_change_stream_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('streaming', 'ChangeStreamCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('streaming', util.camelize('stream_admin'), 'ChangeStreamCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='ChangeStreamCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.streaming.StreamAdminClient(config, service_endpoint=service_endpoint)
            response = client.change_stream_compartment(
                stream_id=request.pop(util.camelize('streamId')),
                change_stream_compartment_details=request.pop(util.camelize('ChangeStreamCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'streaming',
            'ChangeStreamCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_stream_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_streaming_us_grp@oracle.com" jiraProject="STREAMSTR" opsJiraProject="STREAMOSS"
def test_change_stream_pool_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('streaming', 'ChangeStreamPoolCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('streaming', util.camelize('stream_admin'), 'ChangeStreamPoolCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='ChangeStreamPoolCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.streaming.StreamAdminClient(config, service_endpoint=service_endpoint)
            response = client.change_stream_pool_compartment(
                stream_pool_id=request.pop(util.camelize('streamPoolId')),
                change_stream_pool_compartment_details=request.pop(util.camelize('ChangeStreamPoolCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'streaming',
            'ChangeStreamPoolCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_stream_pool_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_streaming_us_grp@oracle.com" jiraProject="STREAMSTR" opsJiraProject="STREAMOSS"
def test_create_archiver(testing_service_client):
    if not testing_service_client.is_api_enabled('streaming', 'CreateArchiver'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('streaming', util.camelize('stream_admin'), 'CreateArchiver')
    )

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='CreateArchiver')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.streaming.StreamAdminClient(config, service_endpoint=service_endpoint)
            response = client.create_archiver(
                stream_id=request.pop(util.camelize('streamId')),
                create_archiver_details=request.pop(util.camelize('CreateArchiverDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'streaming',
            'CreateArchiver',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'archiver',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_streaming_us_grp@oracle.com" jiraProject="STREAMSTR" opsJiraProject="STREAMOSS"
def test_create_connect_harness(testing_service_client):
    if not testing_service_client.is_api_enabled('streaming', 'CreateConnectHarness'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('streaming', util.camelize('stream_admin'), 'CreateConnectHarness')
    )

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='CreateConnectHarness')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.streaming.StreamAdminClient(config, service_endpoint=service_endpoint)
            response = client.create_connect_harness(
                create_connect_harness_details=request.pop(util.camelize('CreateConnectHarnessDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'streaming',
            'CreateConnectHarness',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'connectHarness',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_streaming_us_grp@oracle.com" jiraProject="STREAMSTR" opsJiraProject="STREAMOSS"
def test_create_stream(testing_service_client):
    if not testing_service_client.is_api_enabled('streaming', 'CreateStream'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('streaming', util.camelize('stream_admin'), 'CreateStream')
    )

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='CreateStream')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.streaming.StreamAdminClient(config, service_endpoint=service_endpoint)
            response = client.create_stream(
                create_stream_details=request.pop(util.camelize('CreateStreamDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'streaming',
            'CreateStream',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_streaming_us_grp@oracle.com" jiraProject="STREAMSTR" opsJiraProject="STREAMOSS"
def test_create_stream_pool(testing_service_client):
    if not testing_service_client.is_api_enabled('streaming', 'CreateStreamPool'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('streaming', util.camelize('stream_admin'), 'CreateStreamPool')
    )

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='CreateStreamPool')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.streaming.StreamAdminClient(config, service_endpoint=service_endpoint)
            response = client.create_stream_pool(
                create_stream_pool_details=request.pop(util.camelize('CreateStreamPoolDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'streaming',
            'CreateStreamPool',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'streamPool',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_streaming_us_grp@oracle.com" jiraProject="STREAMSTR" opsJiraProject="STREAMOSS"
def test_delete_connect_harness(testing_service_client):
    if not testing_service_client.is_api_enabled('streaming', 'DeleteConnectHarness'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('streaming', util.camelize('stream_admin'), 'DeleteConnectHarness')
    )

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='DeleteConnectHarness')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.streaming.StreamAdminClient(config, service_endpoint=service_endpoint)
            response = client.delete_connect_harness(
                connect_harness_id=request.pop(util.camelize('connectHarnessId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'streaming',
            'DeleteConnectHarness',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_connect_harness',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="opc_streaming_us_grp@oracle.com" jiraProject="STREAMSTR" opsJiraProject="STREAMOSS"
def test_delete_stream(testing_service_client):
    if not testing_service_client.is_api_enabled('streaming', 'DeleteStream'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('streaming', util.camelize('stream_admin'), 'DeleteStream')
    )

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='DeleteStream')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.streaming.StreamAdminClient(config, service_endpoint=service_endpoint)
            response = client.delete_stream(
                stream_id=request.pop(util.camelize('streamId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'streaming',
            'DeleteStream',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_stream',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="opc_streaming_us_grp@oracle.com" jiraProject="STREAMSTR" opsJiraProject="STREAMOSS"
def test_delete_stream_pool(testing_service_client):
    if not testing_service_client.is_api_enabled('streaming', 'DeleteStreamPool'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('streaming', util.camelize('stream_admin'), 'DeleteStreamPool')
    )

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='DeleteStreamPool')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.streaming.StreamAdminClient(config, service_endpoint=service_endpoint)
            response = client.delete_stream_pool(
                stream_pool_id=request.pop(util.camelize('streamPoolId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'streaming',
            'DeleteStreamPool',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_stream_pool',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="opc_streaming_us_grp@oracle.com" jiraProject="STREAMSTR" opsJiraProject="STREAMOSS"
def test_get_archiver(testing_service_client):
    if not testing_service_client.is_api_enabled('streaming', 'GetArchiver'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('streaming', util.camelize('stream_admin'), 'GetArchiver')
    )

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='GetArchiver')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.streaming.StreamAdminClient(config, service_endpoint=service_endpoint)
            response = client.get_archiver(
                stream_id=request.pop(util.camelize('streamId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'streaming',
            'GetArchiver',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'archiver',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_streaming_us_grp@oracle.com" jiraProject="STREAMSTR" opsJiraProject="STREAMOSS"
def test_get_connect_harness(testing_service_client):
    if not testing_service_client.is_api_enabled('streaming', 'GetConnectHarness'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('streaming', util.camelize('stream_admin'), 'GetConnectHarness')
    )

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='GetConnectHarness')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.streaming.StreamAdminClient(config, service_endpoint=service_endpoint)
            response = client.get_connect_harness(
                connect_harness_id=request.pop(util.camelize('connectHarnessId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'streaming',
            'GetConnectHarness',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'connectHarness',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_streaming_us_grp@oracle.com" jiraProject="STREAMSTR" opsJiraProject="STREAMOSS"
def test_get_stream(testing_service_client):
    if not testing_service_client.is_api_enabled('streaming', 'GetStream'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('streaming', util.camelize('stream_admin'), 'GetStream')
    )

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='GetStream')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.streaming.StreamAdminClient(config, service_endpoint=service_endpoint)
            response = client.get_stream(
                stream_id=request.pop(util.camelize('streamId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'streaming',
            'GetStream',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_streaming_us_grp@oracle.com" jiraProject="STREAMSTR" opsJiraProject="STREAMOSS"
def test_get_stream_pool(testing_service_client):
    if not testing_service_client.is_api_enabled('streaming', 'GetStreamPool'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('streaming', util.camelize('stream_admin'), 'GetStreamPool')
    )

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='GetStreamPool')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.streaming.StreamAdminClient(config, service_endpoint=service_endpoint)
            response = client.get_stream_pool(
                stream_pool_id=request.pop(util.camelize('streamPoolId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'streaming',
            'GetStreamPool',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'streamPool',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_streaming_us_grp@oracle.com" jiraProject="STREAMSTR" opsJiraProject="STREAMOSS"
def test_list_connect_harnesses(testing_service_client):
    if not testing_service_client.is_api_enabled('streaming', 'ListConnectHarnesses'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('streaming', util.camelize('stream_admin'), 'ListConnectHarnesses')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='ListConnectHarnesses')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.streaming.StreamAdminClient(config, service_endpoint=service_endpoint)
            response = client.list_connect_harnesses(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_connect_harnesses(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_connect_harnesses(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'streaming',
            'ListConnectHarnesses',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'connectHarnessSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="opc_streaming_us_grp@oracle.com" jiraProject="STREAMSTR" opsJiraProject="STREAMOSS"
def test_list_stream_pools(testing_service_client):
    if not testing_service_client.is_api_enabled('streaming', 'ListStreamPools'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('streaming', util.camelize('stream_admin'), 'ListStreamPools')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='ListStreamPools')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.streaming.StreamAdminClient(config, service_endpoint=service_endpoint)
            response = client.list_stream_pools(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_stream_pools(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_stream_pools(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'streaming',
            'ListStreamPools',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'streamPoolSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="opc_streaming_us_grp@oracle.com" jiraProject="STREAMSTR" opsJiraProject="STREAMOSS"
def test_list_streams(testing_service_client):
    if not testing_service_client.is_api_enabled('streaming', 'ListStreams'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('streaming', util.camelize('stream_admin'), 'ListStreams')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='ListStreams')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.streaming.StreamAdminClient(config, service_endpoint=service_endpoint)
            response = client.list_streams(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_streams(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_streams(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'streaming',
            'ListStreams',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'streamSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="opc_streaming_us_grp@oracle.com" jiraProject="STREAMSTR" opsJiraProject="STREAMOSS"
def test_start_archiver(testing_service_client):
    if not testing_service_client.is_api_enabled('streaming', 'StartArchiver'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('streaming', util.camelize('stream_admin'), 'StartArchiver')
    )

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='StartArchiver')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.streaming.StreamAdminClient(config, service_endpoint=service_endpoint)
            response = client.start_archiver(
                stream_id=request.pop(util.camelize('streamId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'streaming',
            'StartArchiver',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'archiver',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_streaming_us_grp@oracle.com" jiraProject="STREAMSTR" opsJiraProject="STREAMOSS"
def test_stop_archiver(testing_service_client):
    if not testing_service_client.is_api_enabled('streaming', 'StopArchiver'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('streaming', util.camelize('stream_admin'), 'StopArchiver')
    )

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='StopArchiver')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.streaming.StreamAdminClient(config, service_endpoint=service_endpoint)
            response = client.stop_archiver(
                stream_id=request.pop(util.camelize('streamId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'streaming',
            'StopArchiver',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'archiver',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_streaming_us_grp@oracle.com" jiraProject="STREAMSTR" opsJiraProject="STREAMOSS"
def test_update_archiver(testing_service_client):
    if not testing_service_client.is_api_enabled('streaming', 'UpdateArchiver'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('streaming', util.camelize('stream_admin'), 'UpdateArchiver')
    )

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='UpdateArchiver')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.streaming.StreamAdminClient(config, service_endpoint=service_endpoint)
            response = client.update_archiver(
                stream_id=request.pop(util.camelize('streamId')),
                update_archiver_details=request.pop(util.camelize('UpdateArchiverDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'streaming',
            'UpdateArchiver',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'archiver',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_streaming_us_grp@oracle.com" jiraProject="STREAMSTR" opsJiraProject="STREAMOSS"
def test_update_connect_harness(testing_service_client):
    if not testing_service_client.is_api_enabled('streaming', 'UpdateConnectHarness'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('streaming', util.camelize('stream_admin'), 'UpdateConnectHarness')
    )

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='UpdateConnectHarness')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.streaming.StreamAdminClient(config, service_endpoint=service_endpoint)
            response = client.update_connect_harness(
                connect_harness_id=request.pop(util.camelize('connectHarnessId')),
                update_connect_harness_details=request.pop(util.camelize('UpdateConnectHarnessDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'streaming',
            'UpdateConnectHarness',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'connectHarness',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_streaming_us_grp@oracle.com" jiraProject="STREAMSTR" opsJiraProject="STREAMOSS"
def test_update_stream(testing_service_client):
    if not testing_service_client.is_api_enabled('streaming', 'UpdateStream'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('streaming', util.camelize('stream_admin'), 'UpdateStream')
    )

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='UpdateStream')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.streaming.StreamAdminClient(config, service_endpoint=service_endpoint)
            response = client.update_stream(
                stream_id=request.pop(util.camelize('streamId')),
                update_stream_details=request.pop(util.camelize('UpdateStreamDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'streaming',
            'UpdateStream',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_streaming_us_grp@oracle.com" jiraProject="STREAMSTR" opsJiraProject="STREAMOSS"
def test_update_stream_pool(testing_service_client):
    if not testing_service_client.is_api_enabled('streaming', 'UpdateStreamPool'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('streaming', util.camelize('stream_admin'), 'UpdateStreamPool')
    )

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='UpdateStreamPool')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.streaming.StreamAdminClient(config, service_endpoint=service_endpoint)
            response = client.update_stream_pool(
                stream_pool_id=request.pop(util.camelize('streamPoolId')),
                update_stream_pool_details=request.pop(util.camelize('UpdateStreamPoolDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'streaming',
            'UpdateStreamPool',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'streamPool',
            False,
            False
        )
