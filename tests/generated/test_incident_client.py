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

        cassette_location = os.path.join('generated', 'cims_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="oci_ops_cims_dev_us_grp@oracle.com" jiraProject="CIMS" opsJiraProject="CIMS"
def test_create_incident(testing_service_client):
    if not testing_service_client.is_api_enabled('cims', 'CreateIncident'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cims', util.camelize('incident'), 'CreateIncident')
    )

    request_containers = testing_service_client.get_requests(service_name='cims', api_name='CreateIncident')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cims.IncidentClient(config, service_endpoint=service_endpoint)
            response = client.create_incident(
                create_incident_details=request.pop(util.camelize('CreateIncidentDetails')),
                ocid=request.pop(util.camelize('ocid')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cims',
            'CreateIncident',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'incident',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ops_cims_dev_us_grp@oracle.com" jiraProject="CIMS" opsJiraProject="CIMS"
def test_get_incident(testing_service_client):
    if not testing_service_client.is_api_enabled('cims', 'GetIncident'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cims', util.camelize('incident'), 'GetIncident')
    )

    request_containers = testing_service_client.get_requests(service_name='cims', api_name='GetIncident')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cims.IncidentClient(config, service_endpoint=service_endpoint)
            response = client.get_incident(
                incident_key=request.pop(util.camelize('incidentKey')),
                csi=request.pop(util.camelize('csi')),
                ocid=request.pop(util.camelize('ocid')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cims',
            'GetIncident',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'incident',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ops_cims_dev_us_grp@oracle.com" jiraProject="CIMS" opsJiraProject="CIMS"
def test_get_status(testing_service_client):
    if not testing_service_client.is_api_enabled('cims', 'GetStatus'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cims', util.camelize('incident'), 'GetStatus')
    )

    request_containers = testing_service_client.get_requests(service_name='cims', api_name='GetStatus')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cims.IncidentClient(config, service_endpoint=service_endpoint)
            response = client.get_status(
                source=request.pop(util.camelize('source')),
                ocid=request.pop(util.camelize('ocid')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cims',
            'GetStatus',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'status',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ops_cims_dev_us_grp@oracle.com" jiraProject="CIMS" opsJiraProject="CIMS"
def test_list_incident_resource_types(testing_service_client):
    if not testing_service_client.is_api_enabled('cims', 'ListIncidentResourceTypes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cims', util.camelize('incident'), 'ListIncidentResourceTypes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cims', api_name='ListIncidentResourceTypes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cims.IncidentClient(config, service_endpoint=service_endpoint)
            response = client.list_incident_resource_types(
                problem_type=request.pop(util.camelize('problemType')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                csi=request.pop(util.camelize('csi')),
                ocid=request.pop(util.camelize('ocid')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_incident_resource_types(
                    problem_type=request.pop(util.camelize('problemType')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    csi=request.pop(util.camelize('csi')),
                    ocid=request.pop(util.camelize('ocid')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_incident_resource_types(
                        problem_type=request.pop(util.camelize('problemType')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        csi=request.pop(util.camelize('csi')),
                        ocid=request.pop(util.camelize('ocid')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cims',
            'ListIncidentResourceTypes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'incidentResourceType',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_ops_cims_dev_us_grp@oracle.com" jiraProject="CIMS" opsJiraProject="CIMS"
def test_list_incidents(testing_service_client):
    if not testing_service_client.is_api_enabled('cims', 'ListIncidents'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cims', util.camelize('incident'), 'ListIncidents')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cims', api_name='ListIncidents')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cims.IncidentClient(config, service_endpoint=service_endpoint)
            response = client.list_incidents(
                csi=request.pop(util.camelize('csi')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                ocid=request.pop(util.camelize('ocid')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_incidents(
                    csi=request.pop(util.camelize('csi')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    ocid=request.pop(util.camelize('ocid')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_incidents(
                        csi=request.pop(util.camelize('csi')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        ocid=request.pop(util.camelize('ocid')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cims',
            'ListIncidents',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'incidentSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_ops_cims_dev_us_grp@oracle.com" jiraProject="CIMS" opsJiraProject="CIMS"
def test_update_incident(testing_service_client):
    if not testing_service_client.is_api_enabled('cims', 'UpdateIncident'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cims', util.camelize('incident'), 'UpdateIncident')
    )

    request_containers = testing_service_client.get_requests(service_name='cims', api_name='UpdateIncident')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cims.IncidentClient(config, service_endpoint=service_endpoint)
            response = client.update_incident(
                incident_key=request.pop(util.camelize('incidentKey')),
                csi=request.pop(util.camelize('csi')),
                update_incident_details=request.pop(util.camelize('UpdateIncidentDetails')),
                ocid=request.pop(util.camelize('ocid')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cims',
            'UpdateIncident',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'incident',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ops_cims_dev_us_grp@oracle.com" jiraProject="CIMS" opsJiraProject="CIMS"
def test_validate_user(testing_service_client):
    if not testing_service_client.is_api_enabled('cims', 'ValidateUser'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cims', util.camelize('incident'), 'ValidateUser')
    )

    request_containers = testing_service_client.get_requests(service_name='cims', api_name='ValidateUser')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cims.IncidentClient(config, service_endpoint=service_endpoint)
            response = client.validate_user(
                csi=request.pop(util.camelize('csi')),
                ocid=request.pop(util.camelize('ocid')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cims',
            'ValidateUser',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'validationResponse',
            False,
            False
        )
