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

        cassette_location = os.path.join('generated', 'tenant_manager_control_plane_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="acc_customer_tools_us_grp@oracle.com" jiraProject="ACCMGMT" opsJiraProject="ACCMGMT"
def test_approve_organization_tenancy_for_transfer(testing_service_client):
    if not testing_service_client.is_api_enabled('tenant_manager_control_plane', 'ApproveOrganizationTenancyForTransfer'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('tenant_manager_control_plane', util.camelize('organization'), 'ApproveOrganizationTenancyForTransfer')
    )

    request_containers = testing_service_client.get_requests(service_name='tenant_manager_control_plane', api_name='ApproveOrganizationTenancyForTransfer')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.tenant_manager_control_plane.OrganizationClient(config, service_endpoint=service_endpoint)
            response = client.approve_organization_tenancy_for_transfer(
                compartment_id=request.pop(util.camelize('compartmentId')),
                organization_tenancy_id=request.pop(util.camelize('organizationTenancyId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'tenant_manager_control_plane',
            'ApproveOrganizationTenancyForTransfer',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'organizationTenancy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="acc_customer_tools_us_grp@oracle.com" jiraProject="ACCMGMT" opsJiraProject="ACCMGMT"
def test_create_child_tenancy(testing_service_client):
    if not testing_service_client.is_api_enabled('tenant_manager_control_plane', 'CreateChildTenancy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('tenant_manager_control_plane', util.camelize('organization'), 'CreateChildTenancy')
    )

    request_containers = testing_service_client.get_requests(service_name='tenant_manager_control_plane', api_name='CreateChildTenancy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.tenant_manager_control_plane.OrganizationClient(config, service_endpoint=service_endpoint)
            response = client.create_child_tenancy(
                create_child_tenancy_details=request.pop(util.camelize('CreateChildTenancyDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'tenant_manager_control_plane',
            'CreateChildTenancy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_child_tenancy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="acc_customer_tools_us_grp@oracle.com" jiraProject="ACCMGMT" opsJiraProject="ACCMGMT"
def test_delete_organization_tenancy(testing_service_client):
    if not testing_service_client.is_api_enabled('tenant_manager_control_plane', 'DeleteOrganizationTenancy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('tenant_manager_control_plane', util.camelize('organization'), 'DeleteOrganizationTenancy')
    )

    request_containers = testing_service_client.get_requests(service_name='tenant_manager_control_plane', api_name='DeleteOrganizationTenancy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.tenant_manager_control_plane.OrganizationClient(config, service_endpoint=service_endpoint)
            response = client.delete_organization_tenancy(
                organization_tenancy_id=request.pop(util.camelize('organizationTenancyId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'tenant_manager_control_plane',
            'DeleteOrganizationTenancy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_organization_tenancy',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="acc_customer_tools_us_grp@oracle.com" jiraProject="ACCMGMT" opsJiraProject="ACCMGMT"
def test_get_organization(testing_service_client):
    if not testing_service_client.is_api_enabled('tenant_manager_control_plane', 'GetOrganization'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('tenant_manager_control_plane', util.camelize('organization'), 'GetOrganization')
    )

    request_containers = testing_service_client.get_requests(service_name='tenant_manager_control_plane', api_name='GetOrganization')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.tenant_manager_control_plane.OrganizationClient(config, service_endpoint=service_endpoint)
            response = client.get_organization(
                organization_id=request.pop(util.camelize('organizationId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'tenant_manager_control_plane',
            'GetOrganization',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'organization',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="acc_customer_tools_us_grp@oracle.com" jiraProject="ACCMGMT" opsJiraProject="ACCMGMT"
def test_get_organization_tenancy(testing_service_client):
    if not testing_service_client.is_api_enabled('tenant_manager_control_plane', 'GetOrganizationTenancy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('tenant_manager_control_plane', util.camelize('organization'), 'GetOrganizationTenancy')
    )

    request_containers = testing_service_client.get_requests(service_name='tenant_manager_control_plane', api_name='GetOrganizationTenancy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.tenant_manager_control_plane.OrganizationClient(config, service_endpoint=service_endpoint)
            response = client.get_organization_tenancy(
                organization_id=request.pop(util.camelize('organizationId')),
                tenancy_id=request.pop(util.camelize('tenancyId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'tenant_manager_control_plane',
            'GetOrganizationTenancy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'organizationTenancy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="acc_customer_tools_us_grp@oracle.com" jiraProject="ACCMGMT" opsJiraProject="ACCMGMT"
def test_list_organization_tenancies(testing_service_client):
    if not testing_service_client.is_api_enabled('tenant_manager_control_plane', 'ListOrganizationTenancies'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('tenant_manager_control_plane', util.camelize('organization'), 'ListOrganizationTenancies')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='tenant_manager_control_plane', api_name='ListOrganizationTenancies')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.tenant_manager_control_plane.OrganizationClient(config, service_endpoint=service_endpoint)
            response = client.list_organization_tenancies(
                organization_id=request.pop(util.camelize('organizationId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_organization_tenancies(
                    organization_id=request.pop(util.camelize('organizationId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_organization_tenancies(
                        organization_id=request.pop(util.camelize('organizationId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'tenant_manager_control_plane',
            'ListOrganizationTenancies',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'organizationTenancyCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="acc_customer_tools_us_grp@oracle.com" jiraProject="ACCMGMT" opsJiraProject="ACCMGMT"
def test_list_organizations(testing_service_client):
    if not testing_service_client.is_api_enabled('tenant_manager_control_plane', 'ListOrganizations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('tenant_manager_control_plane', util.camelize('organization'), 'ListOrganizations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='tenant_manager_control_plane', api_name='ListOrganizations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.tenant_manager_control_plane.OrganizationClient(config, service_endpoint=service_endpoint)
            response = client.list_organizations(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_organizations(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_organizations(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'tenant_manager_control_plane',
            'ListOrganizations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'organizationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="acc_customer_tools_us_grp@oracle.com" jiraProject="ACCMGMT" opsJiraProject="ACCMGMT"
def test_unapprove_organization_tenancy_for_transfer(testing_service_client):
    if not testing_service_client.is_api_enabled('tenant_manager_control_plane', 'UnapproveOrganizationTenancyForTransfer'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('tenant_manager_control_plane', util.camelize('organization'), 'UnapproveOrganizationTenancyForTransfer')
    )

    request_containers = testing_service_client.get_requests(service_name='tenant_manager_control_plane', api_name='UnapproveOrganizationTenancyForTransfer')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.tenant_manager_control_plane.OrganizationClient(config, service_endpoint=service_endpoint)
            response = client.unapprove_organization_tenancy_for_transfer(
                compartment_id=request.pop(util.camelize('compartmentId')),
                organization_tenancy_id=request.pop(util.camelize('organizationTenancyId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'tenant_manager_control_plane',
            'UnapproveOrganizationTenancyForTransfer',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'organizationTenancy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="acc_customer_tools_us_grp@oracle.com" jiraProject="ACCMGMT" opsJiraProject="ACCMGMT"
def test_update_organization(testing_service_client):
    if not testing_service_client.is_api_enabled('tenant_manager_control_plane', 'UpdateOrganization'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('tenant_manager_control_plane', util.camelize('organization'), 'UpdateOrganization')
    )

    request_containers = testing_service_client.get_requests(service_name='tenant_manager_control_plane', api_name='UpdateOrganization')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.tenant_manager_control_plane.OrganizationClient(config, service_endpoint=service_endpoint)
            response = client.update_organization(
                organization_id=request.pop(util.camelize('organizationId')),
                update_organization_details=request.pop(util.camelize('UpdateOrganizationDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'tenant_manager_control_plane',
            'UpdateOrganization',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_organization',
            False,
            False
        )
