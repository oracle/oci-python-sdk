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

        cassette_location = os.path.join('generated', 'marketplace_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_get_launch_eligibility(testing_service_client):
    if not testing_service_client.is_api_enabled('marketplace', 'GetLaunchEligibility'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('marketplace', util.camelize('account'), 'GetLaunchEligibility')
    )

    request_containers = testing_service_client.get_requests(service_name='marketplace', api_name='GetLaunchEligibility')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.marketplace.AccountClient(config, service_endpoint=service_endpoint)
            response = client.get_launch_eligibility(
                compartment_id=request.pop(util.camelize('compartmentId')),
                image_id=request.pop(util.camelize('imageId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'marketplace',
            'GetLaunchEligibility',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'launchEligibility',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_get_third_party_paid_listing_eligibility(testing_service_client):
    if not testing_service_client.is_api_enabled('marketplace', 'GetThirdPartyPaidListingEligibility'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('marketplace', util.camelize('account'), 'GetThirdPartyPaidListingEligibility')
    )

    request_containers = testing_service_client.get_requests(service_name='marketplace', api_name='GetThirdPartyPaidListingEligibility')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.marketplace.AccountClient(config, service_endpoint=service_endpoint)
            response = client.get_third_party_paid_listing_eligibility(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'marketplace',
            'GetThirdPartyPaidListingEligibility',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'thirdPartyPaidListingEligibility',
            False,
            False
        )
