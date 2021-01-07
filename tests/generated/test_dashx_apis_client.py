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

        cassette_location = os.path.join('generated', 'management_dashboard_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="em_target_analytics_grp@oracle.com" jiraProject="MGMTUI" opsJiraProject="LOGAN"
def test_change_management_dashboards_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('management_dashboard', 'ChangeManagementDashboardsCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('management_dashboard', util.camelize('dashx_apis'), 'ChangeManagementDashboardsCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='management_dashboard', api_name='ChangeManagementDashboardsCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.management_dashboard.DashxApisClient(config, service_endpoint=service_endpoint)
            response = client.change_management_dashboards_compartment(
                management_dashboard_id=request.pop(util.camelize('managementDashboardId')),
                change_management_dashboards_compartment_details=request.pop(util.camelize('ChangeManagementDashboardsCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'management_dashboard',
            'ChangeManagementDashboardsCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_management_dashboards_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="em_target_analytics_grp@oracle.com" jiraProject="MGMTUI" opsJiraProject="LOGAN"
def test_change_management_saved_searches_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('management_dashboard', 'ChangeManagementSavedSearchesCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('management_dashboard', util.camelize('dashx_apis'), 'ChangeManagementSavedSearchesCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='management_dashboard', api_name='ChangeManagementSavedSearchesCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.management_dashboard.DashxApisClient(config, service_endpoint=service_endpoint)
            response = client.change_management_saved_searches_compartment(
                management_saved_search_id=request.pop(util.camelize('managementSavedSearchId')),
                change_management_saved_searches_compartment_details=request.pop(util.camelize('ChangeManagementSavedSearchesCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'management_dashboard',
            'ChangeManagementSavedSearchesCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_management_saved_searches_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="em_target_analytics_grp@oracle.com" jiraProject="MGMTUI" opsJiraProject="LOGAN"
def test_create_management_dashboard(testing_service_client):
    if not testing_service_client.is_api_enabled('management_dashboard', 'CreateManagementDashboard'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('management_dashboard', util.camelize('dashx_apis'), 'CreateManagementDashboard')
    )

    request_containers = testing_service_client.get_requests(service_name='management_dashboard', api_name='CreateManagementDashboard')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.management_dashboard.DashxApisClient(config, service_endpoint=service_endpoint)
            response = client.create_management_dashboard(
                create_management_dashboard_details=request.pop(util.camelize('CreateManagementDashboardDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'management_dashboard',
            'CreateManagementDashboard',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managementDashboard',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="em_target_analytics_grp@oracle.com" jiraProject="MGMTUI" opsJiraProject="LOGAN"
def test_create_management_saved_search(testing_service_client):
    if not testing_service_client.is_api_enabled('management_dashboard', 'CreateManagementSavedSearch'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('management_dashboard', util.camelize('dashx_apis'), 'CreateManagementSavedSearch')
    )

    request_containers = testing_service_client.get_requests(service_name='management_dashboard', api_name='CreateManagementSavedSearch')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.management_dashboard.DashxApisClient(config, service_endpoint=service_endpoint)
            response = client.create_management_saved_search(
                create_management_saved_search_details=request.pop(util.camelize('CreateManagementSavedSearchDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'management_dashboard',
            'CreateManagementSavedSearch',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managementSavedSearch',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="em_target_analytics_grp@oracle.com" jiraProject="MGMTUI" opsJiraProject="LOGAN"
def test_delete_management_dashboard(testing_service_client):
    if not testing_service_client.is_api_enabled('management_dashboard', 'DeleteManagementDashboard'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('management_dashboard', util.camelize('dashx_apis'), 'DeleteManagementDashboard')
    )

    request_containers = testing_service_client.get_requests(service_name='management_dashboard', api_name='DeleteManagementDashboard')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.management_dashboard.DashxApisClient(config, service_endpoint=service_endpoint)
            response = client.delete_management_dashboard(
                management_dashboard_id=request.pop(util.camelize('managementDashboardId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'management_dashboard',
            'DeleteManagementDashboard',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_management_dashboard',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="em_target_analytics_grp@oracle.com" jiraProject="MGMTUI" opsJiraProject="LOGAN"
def test_delete_management_saved_search(testing_service_client):
    if not testing_service_client.is_api_enabled('management_dashboard', 'DeleteManagementSavedSearch'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('management_dashboard', util.camelize('dashx_apis'), 'DeleteManagementSavedSearch')
    )

    request_containers = testing_service_client.get_requests(service_name='management_dashboard', api_name='DeleteManagementSavedSearch')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.management_dashboard.DashxApisClient(config, service_endpoint=service_endpoint)
            response = client.delete_management_saved_search(
                management_saved_search_id=request.pop(util.camelize('managementSavedSearchId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'management_dashboard',
            'DeleteManagementSavedSearch',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_management_saved_search',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="em_target_analytics_grp@oracle.com" jiraProject="MGMTUI" opsJiraProject="LOGAN"
def test_export_dashboard(testing_service_client):
    if not testing_service_client.is_api_enabled('management_dashboard', 'ExportDashboard'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('management_dashboard', util.camelize('dashx_apis'), 'ExportDashboard')
    )

    request_containers = testing_service_client.get_requests(service_name='management_dashboard', api_name='ExportDashboard')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.management_dashboard.DashxApisClient(config, service_endpoint=service_endpoint)
            response = client.export_dashboard(
                export_dashboard_id=request.pop(util.camelize('exportDashboardId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'management_dashboard',
            'ExportDashboard',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managementDashboardExportDetails',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="em_target_analytics_grp@oracle.com" jiraProject="MGMTUI" opsJiraProject="LOGAN"
def test_get_management_dashboard(testing_service_client):
    if not testing_service_client.is_api_enabled('management_dashboard', 'GetManagementDashboard'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('management_dashboard', util.camelize('dashx_apis'), 'GetManagementDashboard')
    )

    request_containers = testing_service_client.get_requests(service_name='management_dashboard', api_name='GetManagementDashboard')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.management_dashboard.DashxApisClient(config, service_endpoint=service_endpoint)
            response = client.get_management_dashboard(
                management_dashboard_id=request.pop(util.camelize('managementDashboardId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'management_dashboard',
            'GetManagementDashboard',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managementDashboard',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="em_target_analytics_grp@oracle.com" jiraProject="MGMTUI" opsJiraProject="LOGAN"
def test_get_management_saved_search(testing_service_client):
    if not testing_service_client.is_api_enabled('management_dashboard', 'GetManagementSavedSearch'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('management_dashboard', util.camelize('dashx_apis'), 'GetManagementSavedSearch')
    )

    request_containers = testing_service_client.get_requests(service_name='management_dashboard', api_name='GetManagementSavedSearch')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.management_dashboard.DashxApisClient(config, service_endpoint=service_endpoint)
            response = client.get_management_saved_search(
                management_saved_search_id=request.pop(util.camelize('managementSavedSearchId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'management_dashboard',
            'GetManagementSavedSearch',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managementSavedSearch',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="em_target_analytics_grp@oracle.com" jiraProject="MGMTUI" opsJiraProject="LOGAN"
def test_import_dashboard(testing_service_client):
    if not testing_service_client.is_api_enabled('management_dashboard', 'ImportDashboard'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('management_dashboard', util.camelize('dashx_apis'), 'ImportDashboard')
    )

    request_containers = testing_service_client.get_requests(service_name='management_dashboard', api_name='ImportDashboard')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.management_dashboard.DashxApisClient(config, service_endpoint=service_endpoint)
            response = client.import_dashboard(
                management_dashboard_import_details=request.pop(util.camelize('ManagementDashboardImportDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'management_dashboard',
            'ImportDashboard',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'import_dashboard',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="em_target_analytics_grp@oracle.com" jiraProject="MGMTUI" opsJiraProject="LOGAN"
def test_list_management_dashboards(testing_service_client):
    if not testing_service_client.is_api_enabled('management_dashboard', 'ListManagementDashboards'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('management_dashboard', util.camelize('dashx_apis'), 'ListManagementDashboards')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='management_dashboard', api_name='ListManagementDashboards')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.management_dashboard.DashxApisClient(config, service_endpoint=service_endpoint)
            response = client.list_management_dashboards(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_management_dashboards(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_management_dashboards(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'management_dashboard',
            'ListManagementDashboards',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managementDashboardCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="em_target_analytics_grp@oracle.com" jiraProject="MGMTUI" opsJiraProject="LOGAN"
def test_list_management_saved_searches(testing_service_client):
    if not testing_service_client.is_api_enabled('management_dashboard', 'ListManagementSavedSearches'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('management_dashboard', util.camelize('dashx_apis'), 'ListManagementSavedSearches')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='management_dashboard', api_name='ListManagementSavedSearches')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.management_dashboard.DashxApisClient(config, service_endpoint=service_endpoint)
            response = client.list_management_saved_searches(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_management_saved_searches(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_management_saved_searches(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'management_dashboard',
            'ListManagementSavedSearches',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managementSavedSearchCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="em_target_analytics_grp@oracle.com" jiraProject="MGMTUI" opsJiraProject="LOGAN"
def test_update_management_dashboard(testing_service_client):
    if not testing_service_client.is_api_enabled('management_dashboard', 'UpdateManagementDashboard'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('management_dashboard', util.camelize('dashx_apis'), 'UpdateManagementDashboard')
    )

    request_containers = testing_service_client.get_requests(service_name='management_dashboard', api_name='UpdateManagementDashboard')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.management_dashboard.DashxApisClient(config, service_endpoint=service_endpoint)
            response = client.update_management_dashboard(
                management_dashboard_id=request.pop(util.camelize('managementDashboardId')),
                update_management_dashboard_details=request.pop(util.camelize('UpdateManagementDashboardDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'management_dashboard',
            'UpdateManagementDashboard',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managementDashboard',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="em_target_analytics_grp@oracle.com" jiraProject="MGMTUI" opsJiraProject="LOGAN"
def test_update_management_saved_search(testing_service_client):
    if not testing_service_client.is_api_enabled('management_dashboard', 'UpdateManagementSavedSearch'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('management_dashboard', util.camelize('dashx_apis'), 'UpdateManagementSavedSearch')
    )

    request_containers = testing_service_client.get_requests(service_name='management_dashboard', api_name='UpdateManagementSavedSearch')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.management_dashboard.DashxApisClient(config, service_endpoint=service_endpoint)
            response = client.update_management_saved_search(
                management_saved_search_id=request.pop(util.camelize('managementSavedSearchId')),
                update_management_saved_search_details=request.pop(util.camelize('UpdateManagementSavedSearchDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'management_dashboard',
            'UpdateManagementSavedSearch',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managementSavedSearch',
            False,
            False
        )
