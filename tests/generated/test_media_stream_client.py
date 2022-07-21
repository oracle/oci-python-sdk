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

        cassette_location = os.path.join('generated', 'media_services_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_generate_playlist(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'GeneratePlaylist'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_stream'), 'GeneratePlaylist')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='GeneratePlaylist')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaStreamClient(config, service_endpoint=service_endpoint)
            response = client.generate_playlist(
                stream_packaging_config_id=request.pop(util.camelize('streamPackagingConfigId')),
                media_asset_id=request.pop(util.camelize('mediaAssetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'GeneratePlaylist',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_generate_session_token(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'GenerateSessionToken'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_stream'), 'GenerateSessionToken')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='GenerateSessionToken')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaStreamClient(config, service_endpoint=service_endpoint)
            response = client.generate_session_token(
                generate_session_token_details=request.pop(util.camelize('GenerateSessionTokenDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'GenerateSessionToken',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sessionToken',
            False,
            False
        )
