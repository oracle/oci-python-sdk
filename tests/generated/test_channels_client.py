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

        cassette_location = os.path.join('generated', 'mysql_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="mysql-cloud-dev_ww_grp@oracle.com" jiraProject="MY" opsJiraProject="MYOPS"
def test_create_channel(testing_service_client):
    if not testing_service_client.is_api_enabled('mysql', 'CreateChannel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('mysql', util.camelize('channels'), 'CreateChannel')
    )

    request_containers = testing_service_client.get_requests(service_name='mysql', api_name='CreateChannel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.mysql.ChannelsClient(config, service_endpoint=service_endpoint)
            response = client.create_channel(
                create_channel_details=request.pop(util.camelize('CreateChannelDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'mysql',
            'CreateChannel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'channel',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="mysql-cloud-dev_ww_grp@oracle.com" jiraProject="MY" opsJiraProject="MYOPS"
def test_delete_channel(testing_service_client):
    if not testing_service_client.is_api_enabled('mysql', 'DeleteChannel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('mysql', util.camelize('channels'), 'DeleteChannel')
    )

    request_containers = testing_service_client.get_requests(service_name='mysql', api_name='DeleteChannel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.mysql.ChannelsClient(config, service_endpoint=service_endpoint)
            response = client.delete_channel(
                channel_id=request.pop(util.camelize('channelId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'mysql',
            'DeleteChannel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_channel',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="mysql-cloud-dev_ww_grp@oracle.com" jiraProject="MY" opsJiraProject="MYOPS"
def test_get_channel(testing_service_client):
    if not testing_service_client.is_api_enabled('mysql', 'GetChannel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('mysql', util.camelize('channels'), 'GetChannel')
    )

    request_containers = testing_service_client.get_requests(service_name='mysql', api_name='GetChannel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.mysql.ChannelsClient(config, service_endpoint=service_endpoint)
            response = client.get_channel(
                channel_id=request.pop(util.camelize('channelId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'mysql',
            'GetChannel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'channel',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="mysql-cloud-dev_ww_grp@oracle.com" jiraProject="MY" opsJiraProject="MYOPS"
def test_list_channels(testing_service_client):
    if not testing_service_client.is_api_enabled('mysql', 'ListChannels'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('mysql', util.camelize('channels'), 'ListChannels')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='mysql', api_name='ListChannels')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.mysql.ChannelsClient(config, service_endpoint=service_endpoint)
            response = client.list_channels(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_channels(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_channels(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'mysql',
            'ListChannels',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'channelSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="mysql-cloud-dev_ww_grp@oracle.com" jiraProject="MY" opsJiraProject="MYOPS"
def test_reset_channel(testing_service_client):
    if not testing_service_client.is_api_enabled('mysql', 'ResetChannel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('mysql', util.camelize('channels'), 'ResetChannel')
    )

    request_containers = testing_service_client.get_requests(service_name='mysql', api_name='ResetChannel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.mysql.ChannelsClient(config, service_endpoint=service_endpoint)
            response = client.reset_channel(
                channel_id=request.pop(util.camelize('channelId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'mysql',
            'ResetChannel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'reset_channel',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="mysql-cloud-dev_ww_grp@oracle.com" jiraProject="MY" opsJiraProject="MYOPS"
def test_resume_channel(testing_service_client):
    if not testing_service_client.is_api_enabled('mysql', 'ResumeChannel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('mysql', util.camelize('channels'), 'ResumeChannel')
    )

    request_containers = testing_service_client.get_requests(service_name='mysql', api_name='ResumeChannel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.mysql.ChannelsClient(config, service_endpoint=service_endpoint)
            response = client.resume_channel(
                channel_id=request.pop(util.camelize('channelId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'mysql',
            'ResumeChannel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'resume_channel',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="mysql-cloud-dev_ww_grp@oracle.com" jiraProject="MY" opsJiraProject="MYOPS"
def test_update_channel(testing_service_client):
    if not testing_service_client.is_api_enabled('mysql', 'UpdateChannel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('mysql', util.camelize('channels'), 'UpdateChannel')
    )

    request_containers = testing_service_client.get_requests(service_name='mysql', api_name='UpdateChannel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.mysql.ChannelsClient(config, service_endpoint=service_endpoint)
            response = client.update_channel(
                channel_id=request.pop(util.camelize('channelId')),
                update_channel_details=request.pop(util.camelize('UpdateChannelDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'mysql',
            'UpdateChannel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_channel',
            False,
            False
        )
