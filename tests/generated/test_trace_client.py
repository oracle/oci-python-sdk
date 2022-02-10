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

        cassette_location = os.path.join('generated', 'apm_traces_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="tstaaden_directs_ww@oracle.com" jiraProject="APM" opsJiraProject="APMSDC"
def test_get_aggregated_snapshot(testing_service_client):
    if not testing_service_client.is_api_enabled('apm_traces', 'GetAggregatedSnapshot'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apm_traces', util.camelize('trace'), 'GetAggregatedSnapshot')
    )

    request_containers = testing_service_client.get_requests(service_name='apm_traces', api_name='GetAggregatedSnapshot')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apm_traces.TraceClient(config, service_endpoint=service_endpoint)
            response = client.get_aggregated_snapshot(
                apm_domain_id=request.pop(util.camelize('apmDomainId')),
                trace_key=request.pop(util.camelize('traceKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apm_traces',
            'GetAggregatedSnapshot',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'aggregatedSnapshot',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="tstaaden_directs_ww@oracle.com" jiraProject="APM" opsJiraProject="APMSDC"
def test_get_span(testing_service_client):
    if not testing_service_client.is_api_enabled('apm_traces', 'GetSpan'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apm_traces', util.camelize('trace'), 'GetSpan')
    )

    request_containers = testing_service_client.get_requests(service_name='apm_traces', api_name='GetSpan')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apm_traces.TraceClient(config, service_endpoint=service_endpoint)
            response = client.get_span(
                apm_domain_id=request.pop(util.camelize('apmDomainId')),
                span_key=request.pop(util.camelize('spanKey')),
                trace_key=request.pop(util.camelize('traceKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apm_traces',
            'GetSpan',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'span',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="tstaaden_directs_ww@oracle.com" jiraProject="APM" opsJiraProject="APMSDC"
def test_get_trace(testing_service_client):
    if not testing_service_client.is_api_enabled('apm_traces', 'GetTrace'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apm_traces', util.camelize('trace'), 'GetTrace')
    )

    request_containers = testing_service_client.get_requests(service_name='apm_traces', api_name='GetTrace')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apm_traces.TraceClient(config, service_endpoint=service_endpoint)
            response = client.get_trace(
                apm_domain_id=request.pop(util.camelize('apmDomainId')),
                trace_key=request.pop(util.camelize('traceKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apm_traces',
            'GetTrace',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'trace',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="tstaaden_directs_ww@oracle.com" jiraProject="APM" opsJiraProject="APMSDC"
def test_get_trace_snapshot(testing_service_client):
    if not testing_service_client.is_api_enabled('apm_traces', 'GetTraceSnapshot'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apm_traces', util.camelize('trace'), 'GetTraceSnapshot')
    )

    request_containers = testing_service_client.get_requests(service_name='apm_traces', api_name='GetTraceSnapshot')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apm_traces.TraceClient(config, service_endpoint=service_endpoint)
            response = client.get_trace_snapshot(
                apm_domain_id=request.pop(util.camelize('apmDomainId')),
                trace_key=request.pop(util.camelize('traceKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apm_traces',
            'GetTraceSnapshot',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'traceSnapshot',
            False,
            False
        )
