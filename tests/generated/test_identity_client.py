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

        cassette_location = os.path.join('generated', 'identity_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_activate_domain(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ActivateDomain'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ActivateDomain')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ActivateDomain')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.activate_domain(
                domain_id=request.pop(util.camelize('domainId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ActivateDomain',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'activate_domain',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_activate_mfa_totp_device(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ActivateMfaTotpDevice'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ActivateMfaTotpDevice')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ActivateMfaTotpDevice')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.activate_mfa_totp_device(
                user_id=request.pop(util.camelize('userId')),
                mfa_totp_device_id=request.pop(util.camelize('mfaTotpDeviceId')),
                mfa_totp_token=request.pop(util.camelize('MfaTotpToken')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ActivateMfaTotpDevice',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mfaTotpDeviceSummary',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_add_user_to_group(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'AddUserToGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'AddUserToGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='AddUserToGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.add_user_to_group(
                add_user_to_group_details=request.pop(util.camelize('addUserToGroupDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'AddUserToGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'userGroupMembership',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_assemble_effective_tag_set(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'AssembleEffectiveTagSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'AssembleEffectiveTagSet')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='AssembleEffectiveTagSet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.assemble_effective_tag_set(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'AssembleEffectiveTagSet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'tagDefaultSummary',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_bulk_delete_resources(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'BulkDeleteResources'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'BulkDeleteResources')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='BulkDeleteResources')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.bulk_delete_resources(
                compartment_id=request.pop(util.camelize('compartmentId')),
                bulk_delete_resources_details=request.pop(util.camelize('BulkDeleteResourcesDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'BulkDeleteResources',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bulk_delete_resources',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_bulk_delete_tags(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'BulkDeleteTags'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'BulkDeleteTags')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='BulkDeleteTags')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.bulk_delete_tags(
                bulk_delete_tags_details=request.pop(util.camelize('BulkDeleteTagsDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'BulkDeleteTags',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bulk_delete_tags',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_bulk_edit_tags(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'BulkEditTags'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'BulkEditTags')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='BulkEditTags')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.bulk_edit_tags(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'BulkEditTags',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bulk_edit_tags',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_bulk_move_resources(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'BulkMoveResources'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'BulkMoveResources')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='BulkMoveResources')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.bulk_move_resources(
                compartment_id=request.pop(util.camelize('compartmentId')),
                bulk_move_resources_details=request.pop(util.camelize('BulkMoveResourcesDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'BulkMoveResources',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bulk_move_resources',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_cascade_delete_tag_namespace(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'CascadeDeleteTagNamespace'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'CascadeDeleteTagNamespace')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='CascadeDeleteTagNamespace')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.cascade_delete_tag_namespace(
                tag_namespace_id=request.pop(util.camelize('tagNamespaceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'CascadeDeleteTagNamespace',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cascade_delete_tag_namespace',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_change_domain_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ChangeDomainCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ChangeDomainCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ChangeDomainCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.change_domain_compartment(
                domain_id=request.pop(util.camelize('domainId')),
                change_domain_compartment_details=request.pop(util.camelize('ChangeDomainCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ChangeDomainCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_domain_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_change_domain_license_type(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ChangeDomainLicenseType'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ChangeDomainLicenseType')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ChangeDomainLicenseType')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.change_domain_license_type(
                domain_id=request.pop(util.camelize('domainId')),
                change_domain_license_type_details=request.pop(util.camelize('ChangeDomainLicenseTypeDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ChangeDomainLicenseType',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_domain_license_type',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_change_tag_namespace_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ChangeTagNamespaceCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ChangeTagNamespaceCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ChangeTagNamespaceCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.change_tag_namespace_compartment(
                tag_namespace_id=request.pop(util.camelize('tagNamespaceId')),
                change_tag_namespace_compartment_detail=request.pop(util.camelize('ChangeTagNamespaceCompartmentDetail')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ChangeTagNamespaceCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_tag_namespace_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_auth_token(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'CreateAuthToken'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'CreateAuthToken')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='CreateAuthToken')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_auth_token(
                create_auth_token_details=request.pop(util.camelize('createAuthTokenDetails')),
                user_id=request.pop(util.camelize('userId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'CreateAuthToken',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'authToken',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'CreateCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'CreateCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='CreateCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_compartment(
                create_compartment_details=request.pop(util.camelize('createCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'CreateCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_customer_secret_key(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'CreateCustomerSecretKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'CreateCustomerSecretKey')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='CreateCustomerSecretKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_customer_secret_key(
                create_customer_secret_key_details=request.pop(util.camelize('createCustomerSecretKeyDetails')),
                user_id=request.pop(util.camelize('userId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'CreateCustomerSecretKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'customerSecretKey',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_db_credential(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'CreateDbCredential'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'CreateDbCredential')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='CreateDbCredential')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_db_credential(
                create_db_credential_details=request.pop(util.camelize('CreateDbCredentialDetails')),
                user_id=request.pop(util.camelize('userId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'CreateDbCredential',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dbCredential',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_domain(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'CreateDomain'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'CreateDomain')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='CreateDomain')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_domain(
                create_domain_details=request.pop(util.camelize('CreateDomainDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'CreateDomain',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_domain',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_dynamic_group(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'CreateDynamicGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'CreateDynamicGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='CreateDynamicGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_dynamic_group(
                create_dynamic_group_details=request.pop(util.camelize('CreateDynamicGroupDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'CreateDynamicGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dynamicGroup',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_group(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'CreateGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'CreateGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='CreateGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_group(
                create_group_details=request.pop(util.camelize('createGroupDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'CreateGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'group',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_identity_provider(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'CreateIdentityProvider'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'CreateIdentityProvider')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='CreateIdentityProvider')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_identity_provider(
                create_identity_provider_details=request.pop(util.camelize('createIdentityProviderDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'CreateIdentityProvider',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'identityProvider',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_idp_group_mapping(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'CreateIdpGroupMapping'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'CreateIdpGroupMapping')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='CreateIdpGroupMapping')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_idp_group_mapping(
                create_idp_group_mapping_details=request.pop(util.camelize('createIdpGroupMappingDetails')),
                identity_provider_id=request.pop(util.camelize('identityProviderId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'CreateIdpGroupMapping',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'idpGroupMapping',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_mfa_totp_device(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'CreateMfaTotpDevice'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'CreateMfaTotpDevice')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='CreateMfaTotpDevice')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_mfa_totp_device(
                user_id=request.pop(util.camelize('userId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'CreateMfaTotpDevice',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mfaTotpDevice',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_network_source(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'CreateNetworkSource'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'CreateNetworkSource')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='CreateNetworkSource')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_network_source(
                create_network_source_details=request.pop(util.camelize('CreateNetworkSourceDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'CreateNetworkSource',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'networkSources',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_o_auth_client_credential(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'CreateOAuthClientCredential'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'CreateOAuthClientCredential')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='CreateOAuthClientCredential')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_o_auth_client_credential(
                user_id=request.pop(util.camelize('userId')),
                create_o_auth2_client_credential_details=request.pop(util.camelize('CreateOAuth2ClientCredentialDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'CreateOAuthClientCredential',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'oAuth2ClientCredential',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_or_reset_ui_password(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'CreateOrResetUIPassword'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'CreateOrResetUIPassword')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='CreateOrResetUIPassword')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_or_reset_ui_password(
                user_id=request.pop(util.camelize('userId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'CreateOrResetUIPassword',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'uIPassword',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'CreatePolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'CreatePolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='CreatePolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_policy(
                create_policy_details=request.pop(util.camelize('createPolicyDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'CreatePolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'policy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_region_subscription(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'CreateRegionSubscription'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'CreateRegionSubscription')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='CreateRegionSubscription')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_region_subscription(
                create_region_subscription_details=request.pop(util.camelize('CreateRegionSubscriptionDetails')),
                tenancy_id=request.pop(util.camelize('tenancyId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'CreateRegionSubscription',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'regionSubscription',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_smtp_credential(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'CreateSmtpCredential'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'CreateSmtpCredential')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='CreateSmtpCredential')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_smtp_credential(
                create_smtp_credential_details=request.pop(util.camelize('createSmtpCredentialDetails')),
                user_id=request.pop(util.camelize('userId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'CreateSmtpCredential',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'smtpCredential',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_swift_password(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'CreateSwiftPassword'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'CreateSwiftPassword')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='CreateSwiftPassword')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_swift_password(
                create_swift_password_details=request.pop(util.camelize('createSwiftPasswordDetails')),
                user_id=request.pop(util.camelize('userId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'CreateSwiftPassword',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'swiftPassword',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_tag(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'CreateTag'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'CreateTag')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='CreateTag')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_tag(
                tag_namespace_id=request.pop(util.camelize('tagNamespaceId')),
                create_tag_details=request.pop(util.camelize('CreateTagDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'CreateTag',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'tag',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_tag_default(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'CreateTagDefault'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'CreateTagDefault')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='CreateTagDefault')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_tag_default(
                create_tag_default_details=request.pop(util.camelize('CreateTagDefaultDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'CreateTagDefault',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'tagDefault',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_tag_namespace(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'CreateTagNamespace'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'CreateTagNamespace')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='CreateTagNamespace')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_tag_namespace(
                create_tag_namespace_details=request.pop(util.camelize('CreateTagNamespaceDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'CreateTagNamespace',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'tagNamespace',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_user(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'CreateUser'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'CreateUser')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='CreateUser')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_user(
                create_user_details=request.pop(util.camelize('createUserDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'CreateUser',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'user',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_deactivate_domain(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'DeactivateDomain'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'DeactivateDomain')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='DeactivateDomain')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.deactivate_domain(
                domain_id=request.pop(util.camelize('domainId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'DeactivateDomain',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deactivate_domain',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_delete_api_key(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'DeleteApiKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'DeleteApiKey')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='DeleteApiKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.delete_api_key(
                user_id=request.pop(util.camelize('userId')),
                fingerprint=request.pop(util.camelize('fingerprint')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'DeleteApiKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_api_key',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_delete_auth_token(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'DeleteAuthToken'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'DeleteAuthToken')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='DeleteAuthToken')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.delete_auth_token(
                user_id=request.pop(util.camelize('userId')),
                auth_token_id=request.pop(util.camelize('authTokenId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'DeleteAuthToken',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_auth_token',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_delete_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'DeleteCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'DeleteCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='DeleteCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.delete_compartment(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'DeleteCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_compartment',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_delete_customer_secret_key(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'DeleteCustomerSecretKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'DeleteCustomerSecretKey')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='DeleteCustomerSecretKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.delete_customer_secret_key(
                user_id=request.pop(util.camelize('userId')),
                customer_secret_key_id=request.pop(util.camelize('customerSecretKeyId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'DeleteCustomerSecretKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_customer_secret_key',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_delete_db_credential(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'DeleteDbCredential'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'DeleteDbCredential')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='DeleteDbCredential')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.delete_db_credential(
                user_id=request.pop(util.camelize('userId')),
                db_credential_id=request.pop(util.camelize('dbCredentialId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'DeleteDbCredential',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_db_credential',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_delete_domain(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'DeleteDomain'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'DeleteDomain')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='DeleteDomain')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.delete_domain(
                domain_id=request.pop(util.camelize('domainId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'DeleteDomain',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_domain',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_delete_dynamic_group(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'DeleteDynamicGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'DeleteDynamicGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='DeleteDynamicGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.delete_dynamic_group(
                dynamic_group_id=request.pop(util.camelize('dynamicGroupId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'DeleteDynamicGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_dynamic_group',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_delete_group(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'DeleteGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'DeleteGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='DeleteGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.delete_group(
                group_id=request.pop(util.camelize('groupId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'DeleteGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_group',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_delete_identity_provider(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'DeleteIdentityProvider'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'DeleteIdentityProvider')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='DeleteIdentityProvider')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.delete_identity_provider(
                identity_provider_id=request.pop(util.camelize('identityProviderId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'DeleteIdentityProvider',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_identity_provider',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_delete_idp_group_mapping(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'DeleteIdpGroupMapping'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'DeleteIdpGroupMapping')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='DeleteIdpGroupMapping')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.delete_idp_group_mapping(
                identity_provider_id=request.pop(util.camelize('identityProviderId')),
                mapping_id=request.pop(util.camelize('mappingId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'DeleteIdpGroupMapping',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_idp_group_mapping',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_delete_mfa_totp_device(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'DeleteMfaTotpDevice'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'DeleteMfaTotpDevice')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='DeleteMfaTotpDevice')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.delete_mfa_totp_device(
                user_id=request.pop(util.camelize('userId')),
                mfa_totp_device_id=request.pop(util.camelize('mfaTotpDeviceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'DeleteMfaTotpDevice',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_mfa_totp_device',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_delete_network_source(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'DeleteNetworkSource'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'DeleteNetworkSource')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='DeleteNetworkSource')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.delete_network_source(
                network_source_id=request.pop(util.camelize('networkSourceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'DeleteNetworkSource',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_network_source',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_delete_o_auth_client_credential(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'DeleteOAuthClientCredential'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'DeleteOAuthClientCredential')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='DeleteOAuthClientCredential')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.delete_o_auth_client_credential(
                user_id=request.pop(util.camelize('userId')),
                oauth2_client_credential_id=request.pop(util.camelize('oauth2ClientCredentialId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'DeleteOAuthClientCredential',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_o_auth_client_credential',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_delete_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'DeletePolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'DeletePolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='DeletePolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.delete_policy(
                policy_id=request.pop(util.camelize('policyId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'DeletePolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_policy',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_delete_smtp_credential(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'DeleteSmtpCredential'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'DeleteSmtpCredential')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='DeleteSmtpCredential')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.delete_smtp_credential(
                user_id=request.pop(util.camelize('userId')),
                smtp_credential_id=request.pop(util.camelize('smtpCredentialId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'DeleteSmtpCredential',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_smtp_credential',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_delete_swift_password(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'DeleteSwiftPassword'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'DeleteSwiftPassword')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='DeleteSwiftPassword')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.delete_swift_password(
                user_id=request.pop(util.camelize('userId')),
                swift_password_id=request.pop(util.camelize('swiftPasswordId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'DeleteSwiftPassword',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_swift_password',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_delete_tag(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'DeleteTag'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'DeleteTag')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='DeleteTag')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.delete_tag(
                tag_namespace_id=request.pop(util.camelize('tagNamespaceId')),
                tag_name=request.pop(util.camelize('tagName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'DeleteTag',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_tag',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_delete_tag_default(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'DeleteTagDefault'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'DeleteTagDefault')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='DeleteTagDefault')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.delete_tag_default(
                tag_default_id=request.pop(util.camelize('tagDefaultId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'DeleteTagDefault',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_tag_default',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_delete_tag_namespace(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'DeleteTagNamespace'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'DeleteTagNamespace')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='DeleteTagNamespace')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.delete_tag_namespace(
                tag_namespace_id=request.pop(util.camelize('tagNamespaceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'DeleteTagNamespace',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_tag_namespace',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_delete_user(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'DeleteUser'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'DeleteUser')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='DeleteUser')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.delete_user(
                user_id=request.pop(util.camelize('userId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'DeleteUser',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_user',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_enable_replication_to_region(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'EnableReplicationToRegion'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'EnableReplicationToRegion')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='EnableReplicationToRegion')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.enable_replication_to_region(
                domain_id=request.pop(util.camelize('domainId')),
                enable_replication_to_region_details=request.pop(util.camelize('EnableReplicationToRegionDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'EnableReplicationToRegion',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'enable_replication_to_region',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_generate_totp_seed(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'GenerateTotpSeed'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'GenerateTotpSeed')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='GenerateTotpSeed')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.generate_totp_seed(
                user_id=request.pop(util.camelize('userId')),
                mfa_totp_device_id=request.pop(util.camelize('mfaTotpDeviceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'GenerateTotpSeed',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mfaTotpDevice',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_authentication_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'GetAuthenticationPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'GetAuthenticationPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='GetAuthenticationPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_authentication_policy(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'GetAuthenticationPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'authenticationPolicy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'GetCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'GetCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='GetCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_compartment(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'GetCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_domain(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'GetDomain'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'GetDomain')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='GetDomain')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_domain(
                domain_id=request.pop(util.camelize('domainId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'GetDomain',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'domain',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_dynamic_group(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'GetDynamicGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'GetDynamicGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='GetDynamicGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_dynamic_group(
                dynamic_group_id=request.pop(util.camelize('dynamicGroupId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'GetDynamicGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dynamicGroup',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_group(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'GetGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'GetGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='GetGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_group(
                group_id=request.pop(util.camelize('groupId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'GetGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'group',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_iam_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'GetIamWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'GetIamWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='GetIamWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_iam_work_request(
                iam_work_request_id=request.pop(util.camelize('iamWorkRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'GetIamWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'iamWorkRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_identity_provider(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'GetIdentityProvider'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'GetIdentityProvider')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='GetIdentityProvider')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_identity_provider(
                identity_provider_id=request.pop(util.camelize('identityProviderId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'GetIdentityProvider',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'identityProvider',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_idp_group_mapping(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'GetIdpGroupMapping'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'GetIdpGroupMapping')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='GetIdpGroupMapping')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_idp_group_mapping(
                identity_provider_id=request.pop(util.camelize('identityProviderId')),
                mapping_id=request.pop(util.camelize('mappingId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'GetIdpGroupMapping',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'idpGroupMapping',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_mfa_totp_device(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'GetMfaTotpDevice'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'GetMfaTotpDevice')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='GetMfaTotpDevice')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_mfa_totp_device(
                user_id=request.pop(util.camelize('userId')),
                mfa_totp_device_id=request.pop(util.camelize('mfaTotpDeviceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'GetMfaTotpDevice',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mfaTotpDeviceSummary',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_network_source(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'GetNetworkSource'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'GetNetworkSource')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='GetNetworkSource')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_network_source(
                network_source_id=request.pop(util.camelize('networkSourceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'GetNetworkSource',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'networkSources',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'GetPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'GetPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='GetPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_policy(
                policy_id=request.pop(util.camelize('policyId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'GetPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'policy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_standard_tag_template(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'GetStandardTagTemplate'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'GetStandardTagTemplate')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='GetStandardTagTemplate')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_standard_tag_template(
                compartment_id=request.pop(util.camelize('compartmentId')),
                standard_tag_namespace_name=request.pop(util.camelize('standardTagNamespaceName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'GetStandardTagTemplate',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'standardTagNamespaceTemplate',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_tag(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'GetTag'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'GetTag')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='GetTag')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_tag(
                tag_namespace_id=request.pop(util.camelize('tagNamespaceId')),
                tag_name=request.pop(util.camelize('tagName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'GetTag',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'tag',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_tag_default(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'GetTagDefault'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'GetTagDefault')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='GetTagDefault')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_tag_default(
                tag_default_id=request.pop(util.camelize('tagDefaultId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'GetTagDefault',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'tagDefault',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_tag_namespace(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'GetTagNamespace'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'GetTagNamespace')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='GetTagNamespace')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_tag_namespace(
                tag_namespace_id=request.pop(util.camelize('tagNamespaceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'GetTagNamespace',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'tagNamespace',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_tagging_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'GetTaggingWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'GetTaggingWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='GetTaggingWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_tagging_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'GetTaggingWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'taggingWorkRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_tenancy(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'GetTenancy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'GetTenancy')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='GetTenancy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_tenancy(
                tenancy_id=request.pop(util.camelize('tenancyId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'GetTenancy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'tenancy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_user(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'GetUser'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'GetUser')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='GetUser')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_user(
                user_id=request.pop(util.camelize('userId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'GetUser',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'user',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_user_group_membership(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'GetUserGroupMembership'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'GetUserGroupMembership')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='GetUserGroupMembership')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_user_group_membership(
                user_group_membership_id=request.pop(util.camelize('userGroupMembershipId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'GetUserGroupMembership',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'userGroupMembership',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_user_ui_password_information(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'GetUserUIPasswordInformation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'GetUserUIPasswordInformation')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='GetUserUIPasswordInformation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_user_ui_password_information(
                user_id=request.pop(util.camelize('userId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'GetUserUIPasswordInformation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'uIPasswordInformation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_import_standard_tags(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ImportStandardTags'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ImportStandardTags')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ImportStandardTags')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.import_standard_tags(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ImportStandardTags',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'import_standard_tags',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_allowed_domain_license_types(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListAllowedDomainLicenseTypes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListAllowedDomainLicenseTypes')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListAllowedDomainLicenseTypes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_allowed_domain_license_types(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListAllowedDomainLicenseTypes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'allowedDomainLicenseTypeSummary',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_api_keys(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListApiKeys'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListApiKeys')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListApiKeys')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_api_keys(
                user_id=request.pop(util.camelize('userId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListApiKeys',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'apiKey',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_auth_tokens(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListAuthTokens'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListAuthTokens')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListAuthTokens')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_auth_tokens(
                user_id=request.pop(util.camelize('userId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListAuthTokens',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'authToken',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_availability_domains(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListAvailabilityDomains'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListAvailabilityDomains')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListAvailabilityDomains')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_availability_domains(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListAvailabilityDomains',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'availabilityDomain',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_bulk_action_resource_types(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListBulkActionResourceTypes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListBulkActionResourceTypes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListBulkActionResourceTypes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_bulk_action_resource_types(
                bulk_action_type=request.pop(util.camelize('bulkActionType')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_bulk_action_resource_types(
                    bulk_action_type=request.pop(util.camelize('bulkActionType')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_bulk_action_resource_types(
                        bulk_action_type=request.pop(util.camelize('bulkActionType')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListBulkActionResourceTypes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bulkActionResourceTypeCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_bulk_edit_tags_resource_types(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListBulkEditTagsResourceTypes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListBulkEditTagsResourceTypes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListBulkEditTagsResourceTypes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_bulk_edit_tags_resource_types(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_bulk_edit_tags_resource_types(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_bulk_edit_tags_resource_types(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListBulkEditTagsResourceTypes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bulkEditTagsResourceTypeCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_compartments(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListCompartments'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListCompartments')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListCompartments')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_compartments(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_compartments(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_compartments(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListCompartments',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'compartment',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_cost_tracking_tags(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListCostTrackingTags'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListCostTrackingTags')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListCostTrackingTags')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_cost_tracking_tags(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_cost_tracking_tags(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_cost_tracking_tags(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListCostTrackingTags',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'tag',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_customer_secret_keys(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListCustomerSecretKeys'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListCustomerSecretKeys')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListCustomerSecretKeys')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_customer_secret_keys(
                user_id=request.pop(util.camelize('userId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListCustomerSecretKeys',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'customerSecretKeySummary',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_db_credentials(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListDbCredentials'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListDbCredentials')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListDbCredentials')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_db_credentials(
                user_id=request.pop(util.camelize('userId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_db_credentials(
                    user_id=request.pop(util.camelize('userId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_db_credentials(
                        user_id=request.pop(util.camelize('userId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListDbCredentials',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dbCredentialSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_domains(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListDomains'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListDomains')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListDomains')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_domains(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_domains(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_domains(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListDomains',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'domainSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_dynamic_groups(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListDynamicGroups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListDynamicGroups')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListDynamicGroups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_dynamic_groups(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_dynamic_groups(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_dynamic_groups(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListDynamicGroups',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dynamicGroup',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_fault_domains(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListFaultDomains'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListFaultDomains')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListFaultDomains')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_fault_domains(
                compartment_id=request.pop(util.camelize('compartmentId')),
                availability_domain=request.pop(util.camelize('availabilityDomain')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListFaultDomains',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'faultDomain',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_groups(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListGroups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListGroups')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListGroups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_groups(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_groups(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_groups(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListGroups',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'group',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_iam_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListIamWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListIamWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListIamWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_iam_work_request_errors(
                iam_work_request_id=request.pop(util.camelize('iamWorkRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_iam_work_request_errors(
                    iam_work_request_id=request.pop(util.camelize('iamWorkRequestId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_iam_work_request_errors(
                        iam_work_request_id=request.pop(util.camelize('iamWorkRequestId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListIamWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'iamWorkRequestErrorSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_iam_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListIamWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListIamWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListIamWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_iam_work_request_logs(
                iam_work_request_id=request.pop(util.camelize('iamWorkRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_iam_work_request_logs(
                    iam_work_request_id=request.pop(util.camelize('iamWorkRequestId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_iam_work_request_logs(
                        iam_work_request_id=request.pop(util.camelize('iamWorkRequestId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListIamWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'iamWorkRequestLogSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_iam_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListIamWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListIamWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListIamWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_iam_work_requests(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_iam_work_requests(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_iam_work_requests(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListIamWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'iamWorkRequestSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_identity_provider_groups(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListIdentityProviderGroups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListIdentityProviderGroups')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListIdentityProviderGroups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_identity_provider_groups(
                identity_provider_id=request.pop(util.camelize('identityProviderId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_identity_provider_groups(
                    identity_provider_id=request.pop(util.camelize('identityProviderId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_identity_provider_groups(
                        identity_provider_id=request.pop(util.camelize('identityProviderId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListIdentityProviderGroups',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'identityProviderGroupSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_identity_providers(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListIdentityProviders'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListIdentityProviders')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListIdentityProviders')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_identity_providers(
                protocol=request.pop(util.camelize('protocol')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_identity_providers(
                    protocol=request.pop(util.camelize('protocol')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_identity_providers(
                        protocol=request.pop(util.camelize('protocol')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListIdentityProviders',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'identityProvider',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_idp_group_mappings(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListIdpGroupMappings'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListIdpGroupMappings')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListIdpGroupMappings')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_idp_group_mappings(
                identity_provider_id=request.pop(util.camelize('identityProviderId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_idp_group_mappings(
                    identity_provider_id=request.pop(util.camelize('identityProviderId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_idp_group_mappings(
                        identity_provider_id=request.pop(util.camelize('identityProviderId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListIdpGroupMappings',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'idpGroupMapping',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_mfa_totp_devices(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListMfaTotpDevices'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListMfaTotpDevices')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListMfaTotpDevices')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_mfa_totp_devices(
                user_id=request.pop(util.camelize('userId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_mfa_totp_devices(
                    user_id=request.pop(util.camelize('userId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_mfa_totp_devices(
                        user_id=request.pop(util.camelize('userId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListMfaTotpDevices',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mfaTotpDeviceSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_network_sources(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListNetworkSources'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListNetworkSources')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListNetworkSources')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_network_sources(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_network_sources(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_network_sources(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListNetworkSources',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'networkSourcesSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_o_auth_client_credentials(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListOAuthClientCredentials'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListOAuthClientCredentials')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListOAuthClientCredentials')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_o_auth_client_credentials(
                user_id=request.pop(util.camelize('userId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_o_auth_client_credentials(
                    user_id=request.pop(util.camelize('userId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_o_auth_client_credentials(
                        user_id=request.pop(util.camelize('userId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListOAuthClientCredentials',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'oAuth2ClientCredentialSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_policies(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListPolicies'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListPolicies')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListPolicies')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_policies(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_policies(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_policies(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListPolicies',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'policy',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_region_subscriptions(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListRegionSubscriptions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListRegionSubscriptions')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListRegionSubscriptions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_region_subscriptions(
                tenancy_id=request.pop(util.camelize('tenancyId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListRegionSubscriptions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'regionSubscription',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_regions(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListRegions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListRegions')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListRegions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_regions(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListRegions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'region',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_smtp_credentials(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListSmtpCredentials'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListSmtpCredentials')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListSmtpCredentials')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_smtp_credentials(
                user_id=request.pop(util.camelize('userId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListSmtpCredentials',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'smtpCredentialSummary',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_standard_tag_namespaces(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListStandardTagNamespaces'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListStandardTagNamespaces')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListStandardTagNamespaces')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_standard_tag_namespaces(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_standard_tag_namespaces(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_standard_tag_namespaces(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListStandardTagNamespaces',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'standardTagNamespaceTemplateSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_swift_passwords(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListSwiftPasswords'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListSwiftPasswords')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListSwiftPasswords')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_swift_passwords(
                user_id=request.pop(util.camelize('userId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListSwiftPasswords',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'swiftPassword',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_tag_defaults(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListTagDefaults'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListTagDefaults')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListTagDefaults')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_tag_defaults(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_tag_defaults(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_tag_defaults(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListTagDefaults',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'tagDefaultSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_tag_namespaces(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListTagNamespaces'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListTagNamespaces')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListTagNamespaces')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_tag_namespaces(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_tag_namespaces(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_tag_namespaces(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListTagNamespaces',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'tagNamespaceSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_tagging_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListTaggingWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListTaggingWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListTaggingWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_tagging_work_request_errors(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_tagging_work_request_errors(
                    work_request_id=request.pop(util.camelize('workRequestId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_tagging_work_request_errors(
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListTaggingWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'taggingWorkRequestErrorSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_tagging_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListTaggingWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListTaggingWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListTaggingWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_tagging_work_request_logs(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_tagging_work_request_logs(
                    work_request_id=request.pop(util.camelize('workRequestId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_tagging_work_request_logs(
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListTaggingWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'taggingWorkRequestLogSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_tagging_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListTaggingWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListTaggingWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListTaggingWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_tagging_work_requests(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_tagging_work_requests(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_tagging_work_requests(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListTaggingWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'taggingWorkRequestSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_tags(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListTags'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListTags')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListTags')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_tags(
                tag_namespace_id=request.pop(util.camelize('tagNamespaceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_tags(
                    tag_namespace_id=request.pop(util.camelize('tagNamespaceId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_tags(
                        tag_namespace_id=request.pop(util.camelize('tagNamespaceId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListTags',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'tagSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_user_group_memberships(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListUserGroupMemberships'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListUserGroupMemberships')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListUserGroupMemberships')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_user_group_memberships(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_user_group_memberships(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_user_group_memberships(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListUserGroupMemberships',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'userGroupMembership',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_users(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListUsers'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListUsers')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListUsers')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_users(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_users(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_users(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListUsers',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'user',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_work_requests(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_requests(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_requests(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_move_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'MoveCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'MoveCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='MoveCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.move_compartment(
                compartment_id=request.pop(util.camelize('compartmentId')),
                move_compartment_details=request.pop(util.camelize('MoveCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'MoveCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'move_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_recover_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'RecoverCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'RecoverCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='RecoverCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.recover_compartment(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'RecoverCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_remove_user_from_group(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'RemoveUserFromGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'RemoveUserFromGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='RemoveUserFromGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.remove_user_from_group(
                user_group_membership_id=request.pop(util.camelize('userGroupMembershipId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'RemoveUserFromGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'remove_user_from_group',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_reset_idp_scim_client(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ResetIdpScimClient'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ResetIdpScimClient')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ResetIdpScimClient')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.reset_idp_scim_client(
                identity_provider_id=request.pop(util.camelize('identityProviderId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'ResetIdpScimClient',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'scimClientCredentials',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_update_auth_token(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'UpdateAuthToken'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'UpdateAuthToken')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='UpdateAuthToken')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.update_auth_token(
                user_id=request.pop(util.camelize('userId')),
                auth_token_id=request.pop(util.camelize('authTokenId')),
                update_auth_token_details=request.pop(util.camelize('updateAuthTokenDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'UpdateAuthToken',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'authToken',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_update_authentication_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'UpdateAuthenticationPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'UpdateAuthenticationPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='UpdateAuthenticationPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.update_authentication_policy(
                compartment_id=request.pop(util.camelize('compartmentId')),
                update_authentication_policy_details=request.pop(util.camelize('UpdateAuthenticationPolicyDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'UpdateAuthenticationPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'authenticationPolicy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_update_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'UpdateCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'UpdateCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='UpdateCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.update_compartment(
                compartment_id=request.pop(util.camelize('compartmentId')),
                update_compartment_details=request.pop(util.camelize('updateCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'UpdateCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_update_customer_secret_key(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'UpdateCustomerSecretKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'UpdateCustomerSecretKey')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='UpdateCustomerSecretKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.update_customer_secret_key(
                user_id=request.pop(util.camelize('userId')),
                customer_secret_key_id=request.pop(util.camelize('customerSecretKeyId')),
                update_customer_secret_key_details=request.pop(util.camelize('updateCustomerSecretKeyDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'UpdateCustomerSecretKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'customerSecretKeySummary',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_update_domain(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'UpdateDomain'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'UpdateDomain')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='UpdateDomain')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.update_domain(
                domain_id=request.pop(util.camelize('domainId')),
                update_domain_details=request.pop(util.camelize('UpdateDomainDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'UpdateDomain',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_domain',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_update_dynamic_group(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'UpdateDynamicGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'UpdateDynamicGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='UpdateDynamicGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.update_dynamic_group(
                dynamic_group_id=request.pop(util.camelize('dynamicGroupId')),
                update_dynamic_group_details=request.pop(util.camelize('UpdateDynamicGroupDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'UpdateDynamicGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dynamicGroup',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_update_group(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'UpdateGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'UpdateGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='UpdateGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.update_group(
                group_id=request.pop(util.camelize('groupId')),
                update_group_details=request.pop(util.camelize('updateGroupDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'UpdateGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'group',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_update_identity_provider(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'UpdateIdentityProvider'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'UpdateIdentityProvider')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='UpdateIdentityProvider')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.update_identity_provider(
                identity_provider_id=request.pop(util.camelize('identityProviderId')),
                update_identity_provider_details=request.pop(util.camelize('updateIdentityProviderDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'UpdateIdentityProvider',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'identityProvider',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_update_idp_group_mapping(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'UpdateIdpGroupMapping'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'UpdateIdpGroupMapping')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='UpdateIdpGroupMapping')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.update_idp_group_mapping(
                identity_provider_id=request.pop(util.camelize('identityProviderId')),
                mapping_id=request.pop(util.camelize('mappingId')),
                update_idp_group_mapping_details=request.pop(util.camelize('updateIdpGroupMappingDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'UpdateIdpGroupMapping',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'idpGroupMapping',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_update_network_source(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'UpdateNetworkSource'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'UpdateNetworkSource')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='UpdateNetworkSource')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.update_network_source(
                network_source_id=request.pop(util.camelize('networkSourceId')),
                update_network_source_details=request.pop(util.camelize('UpdateNetworkSourceDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'UpdateNetworkSource',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'networkSources',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_update_o_auth_client_credential(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'UpdateOAuthClientCredential'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'UpdateOAuthClientCredential')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='UpdateOAuthClientCredential')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.update_o_auth_client_credential(
                user_id=request.pop(util.camelize('userId')),
                oauth2_client_credential_id=request.pop(util.camelize('oauth2ClientCredentialId')),
                update_o_auth2_client_credential_details=request.pop(util.camelize('UpdateOAuth2ClientCredentialDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'UpdateOAuthClientCredential',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'oAuth2ClientCredential',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_update_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'UpdatePolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'UpdatePolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='UpdatePolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.update_policy(
                policy_id=request.pop(util.camelize('policyId')),
                update_policy_details=request.pop(util.camelize('updatePolicyDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'UpdatePolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'policy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_update_smtp_credential(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'UpdateSmtpCredential'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'UpdateSmtpCredential')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='UpdateSmtpCredential')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.update_smtp_credential(
                user_id=request.pop(util.camelize('userId')),
                smtp_credential_id=request.pop(util.camelize('smtpCredentialId')),
                update_smtp_credential_details=request.pop(util.camelize('updateSmtpCredentialDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'UpdateSmtpCredential',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'smtpCredentialSummary',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_update_swift_password(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'UpdateSwiftPassword'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'UpdateSwiftPassword')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='UpdateSwiftPassword')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.update_swift_password(
                user_id=request.pop(util.camelize('userId')),
                swift_password_id=request.pop(util.camelize('swiftPasswordId')),
                update_swift_password_details=request.pop(util.camelize('updateSwiftPasswordDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'UpdateSwiftPassword',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'swiftPassword',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_update_tag(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'UpdateTag'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'UpdateTag')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='UpdateTag')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.update_tag(
                tag_namespace_id=request.pop(util.camelize('tagNamespaceId')),
                tag_name=request.pop(util.camelize('tagName')),
                update_tag_details=request.pop(util.camelize('UpdateTagDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'UpdateTag',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'tag',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_update_tag_default(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'UpdateTagDefault'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'UpdateTagDefault')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='UpdateTagDefault')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.update_tag_default(
                tag_default_id=request.pop(util.camelize('tagDefaultId')),
                update_tag_default_details=request.pop(util.camelize('UpdateTagDefaultDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'UpdateTagDefault',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'tagDefault',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_update_tag_namespace(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'UpdateTagNamespace'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'UpdateTagNamespace')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='UpdateTagNamespace')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.update_tag_namespace(
                tag_namespace_id=request.pop(util.camelize('tagNamespaceId')),
                update_tag_namespace_details=request.pop(util.camelize('UpdateTagNamespaceDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'UpdateTagNamespace',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'tagNamespace',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_update_user(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'UpdateUser'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'UpdateUser')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='UpdateUser')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.update_user(
                user_id=request.pop(util.camelize('userId')),
                update_user_details=request.pop(util.camelize('updateUserDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'UpdateUser',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'user',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_update_user_capabilities(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'UpdateUserCapabilities'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'UpdateUserCapabilities')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='UpdateUserCapabilities')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.update_user_capabilities(
                user_id=request.pop(util.camelize('userId')),
                update_user_capabilities_details=request.pop(util.camelize('UpdateUserCapabilitiesDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'UpdateUserCapabilities',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'user',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_update_user_state(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'UpdateUserState'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'UpdateUserState')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='UpdateUserState')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.update_user_state(
                user_id=request.pop(util.camelize('userId')),
                update_state_details=request.pop(util.camelize('updateStateDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'UpdateUserState',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'user',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_upload_api_key(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'UploadApiKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'UploadApiKey')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='UploadApiKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.upload_api_key(
                user_id=request.pop(util.camelize('userId')),
                create_api_key_details=request.pop(util.camelize('createApiKeyDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity',
            'UploadApiKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'apiKey',
            False,
            False
        )
