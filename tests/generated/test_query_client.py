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

        cassette_location = os.path.join('generated', 'apm_traces_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="tstaaden_directs_ww@oracle.com" jiraProject="APM" opsJiraProject="APMSDC"
def test_list_quick_picks(testing_service_client):
    if not testing_service_client.is_api_enabled('apm_traces', 'ListQuickPicks'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apm_traces', util.camelize('query'), 'ListQuickPicks')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='apm_traces', api_name='ListQuickPicks')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apm_traces.QueryClient(config, service_endpoint=service_endpoint)
            response = client.list_quick_picks(
                apm_domain_id=request.pop(util.camelize('apmDomainId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_quick_picks(
                    apm_domain_id=request.pop(util.camelize('apmDomainId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_quick_picks(
                        apm_domain_id=request.pop(util.camelize('apmDomainId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apm_traces',
            'ListQuickPicks',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'quickPickSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="tstaaden_directs_ww@oracle.com" jiraProject="APM" opsJiraProject="APMSDC"
def test_query(testing_service_client):
    if not testing_service_client.is_api_enabled('apm_traces', 'Query'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apm_traces', util.camelize('query'), 'Query')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='apm_traces', api_name='Query')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apm_traces.QueryClient(config, service_endpoint=service_endpoint)
            response = client.query(
                apm_domain_id=request.pop(util.camelize('apmDomainId')),
                time_span_started_greater_than_or_equal_to=request.pop(util.camelize('timeSpanStartedGreaterThanOrEqualTo')),
                time_span_started_less_than=request.pop(util.camelize('timeSpanStartedLessThan')),
                query_details=request.pop(util.camelize('QueryDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.query(
                    apm_domain_id=request.pop(util.camelize('apmDomainId')),
                    time_span_started_greater_than_or_equal_to=request.pop(util.camelize('timeSpanStartedGreaterThanOrEqualTo')),
                    time_span_started_less_than=request.pop(util.camelize('timeSpanStartedLessThan')),
                    query_details=request.pop(util.camelize('QueryDetails')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.query(
                        apm_domain_id=request.pop(util.camelize('apmDomainId')),
                        time_span_started_greater_than_or_equal_to=request.pop(util.camelize('timeSpanStartedGreaterThanOrEqualTo')),
                        time_span_started_less_than=request.pop(util.camelize('timeSpanStartedLessThan')),
                        query_details=request.pop(util.camelize('QueryDetails')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apm_traces',
            'Query',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'queryResultResponse',
            False,
            True
        )
