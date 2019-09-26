# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

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
    # use the default matching logic (link below) with the exception of 'session_agnostic_query_matcher'
    # instead of 'query' matcher (which ignores sessionId in the url)
    # https://vcrpy.readthedocs.io/en/latest/configuration.html#request-matching
    custom_vcr = test_config_container.create_vcr()
    custom_vcr.register_matcher('session_agnostic_query_matcher', session_agnostic_query_matcher)

    cassette_location = os.path.join('generated', 'identity_{name}.yml'.format(name=request.function.__name__))
    with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
        yield


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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.activate_mfa_totp_device(
                user_id=request.pop(util.camelize('user_id')),
                mfa_totp_device_id=request.pop(util.camelize('mfa_totp_device_id')),
                mfa_totp_token=request.pop(util.camelize('mfa_totp_token')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.add_user_to_group(
                add_user_to_group_details=request.pop(util.camelize('add_user_to_group_details')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.assemble_effective_tag_set(
                compartment_id=request.pop(util.camelize('compartment_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.change_tag_namespace_compartment(
                tag_namespace_id=request.pop(util.camelize('tag_namespace_id')),
                change_tag_namespace_compartment_detail=request.pop(util.camelize('change_tag_namespace_compartment_detail')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_auth_token(
                create_auth_token_details=request.pop(util.camelize('create_auth_token_details')),
                user_id=request.pop(util.camelize('user_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_compartment(
                create_compartment_details=request.pop(util.camelize('create_compartment_details')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_customer_secret_key(
                create_customer_secret_key_details=request.pop(util.camelize('create_customer_secret_key_details')),
                user_id=request.pop(util.camelize('user_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_dynamic_group(
                create_dynamic_group_details=request.pop(util.camelize('create_dynamic_group_details')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_group(
                create_group_details=request.pop(util.camelize('create_group_details')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_identity_provider(
                create_identity_provider_details=request.pop(util.camelize('create_identity_provider_details')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_idp_group_mapping(
                create_idp_group_mapping_details=request.pop(util.camelize('create_idp_group_mapping_details')),
                identity_provider_id=request.pop(util.camelize('identity_provider_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_mfa_totp_device(
                user_id=request.pop(util.camelize('user_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_or_reset_ui_password(
                user_id=request.pop(util.camelize('user_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_policy(
                create_policy_details=request.pop(util.camelize('create_policy_details')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_region_subscription(
                create_region_subscription_details=request.pop(util.camelize('create_region_subscription_details')),
                tenancy_id=request.pop(util.camelize('tenancy_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_smtp_credential(
                create_smtp_credential_details=request.pop(util.camelize('create_smtp_credential_details')),
                user_id=request.pop(util.camelize('user_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_swift_password(
                create_swift_password_details=request.pop(util.camelize('create_swift_password_details')),
                user_id=request.pop(util.camelize('user_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_tag(
                tag_namespace_id=request.pop(util.camelize('tag_namespace_id')),
                create_tag_details=request.pop(util.camelize('create_tag_details')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_tag_default(
                create_tag_default_details=request.pop(util.camelize('create_tag_default_details')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_tag_namespace(
                create_tag_namespace_details=request.pop(util.camelize('create_tag_namespace_details')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.create_user(
                create_user_details=request.pop(util.camelize('create_user_details')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.delete_api_key(
                user_id=request.pop(util.camelize('user_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.delete_auth_token(
                user_id=request.pop(util.camelize('user_id')),
                auth_token_id=request.pop(util.camelize('auth_token_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.delete_compartment(
                compartment_id=request.pop(util.camelize('compartment_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.delete_customer_secret_key(
                user_id=request.pop(util.camelize('user_id')),
                customer_secret_key_id=request.pop(util.camelize('customer_secret_key_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.delete_dynamic_group(
                dynamic_group_id=request.pop(util.camelize('dynamic_group_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.delete_group(
                group_id=request.pop(util.camelize('group_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.delete_identity_provider(
                identity_provider_id=request.pop(util.camelize('identity_provider_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.delete_idp_group_mapping(
                identity_provider_id=request.pop(util.camelize('identity_provider_id')),
                mapping_id=request.pop(util.camelize('mapping_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.delete_mfa_totp_device(
                user_id=request.pop(util.camelize('user_id')),
                mfa_totp_device_id=request.pop(util.camelize('mfa_totp_device_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.delete_policy(
                policy_id=request.pop(util.camelize('policy_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.delete_smtp_credential(
                user_id=request.pop(util.camelize('user_id')),
                smtp_credential_id=request.pop(util.camelize('smtp_credential_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.delete_swift_password(
                user_id=request.pop(util.camelize('user_id')),
                swift_password_id=request.pop(util.camelize('swift_password_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.delete_tag(
                tag_namespace_id=request.pop(util.camelize('tag_namespace_id')),
                tag_name=request.pop(util.camelize('tag_name')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.delete_tag_default(
                tag_default_id=request.pop(util.camelize('tag_default_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.delete_tag_namespace(
                tag_namespace_id=request.pop(util.camelize('tag_namespace_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.delete_user(
                user_id=request.pop(util.camelize('user_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.generate_totp_seed(
                user_id=request.pop(util.camelize('user_id')),
                mfa_totp_device_id=request.pop(util.camelize('mfa_totp_device_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_authentication_policy(
                compartment_id=request.pop(util.camelize('compartment_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_compartment(
                compartment_id=request.pop(util.camelize('compartment_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_dynamic_group(
                dynamic_group_id=request.pop(util.camelize('dynamic_group_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_group(
                group_id=request.pop(util.camelize('group_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_identity_provider(
                identity_provider_id=request.pop(util.camelize('identity_provider_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_idp_group_mapping(
                identity_provider_id=request.pop(util.camelize('identity_provider_id')),
                mapping_id=request.pop(util.camelize('mapping_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_mfa_totp_device(
                user_id=request.pop(util.camelize('user_id')),
                mfa_totp_device_id=request.pop(util.camelize('mfa_totp_device_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_policy(
                policy_id=request.pop(util.camelize('policy_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_tag(
                tag_namespace_id=request.pop(util.camelize('tag_namespace_id')),
                tag_name=request.pop(util.camelize('tag_name')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_tag_default(
                tag_default_id=request.pop(util.camelize('tag_default_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_tag_namespace(
                tag_namespace_id=request.pop(util.camelize('tag_namespace_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_tagging_work_request(
                work_request_id=request.pop(util.camelize('work_request_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_tenancy(
                tenancy_id=request.pop(util.camelize('tenancy_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_user(
                user_id=request.pop(util.camelize('user_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_user_group_membership(
                user_group_membership_id=request.pop(util.camelize('user_group_membership_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_user_ui_password_information(
                user_id=request.pop(util.camelize('user_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('work_request_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_api_keys(
                user_id=request.pop(util.camelize('user_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_auth_tokens(
                user_id=request.pop(util.camelize('user_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_availability_domains(
                compartment_id=request.pop(util.camelize('compartment_id')),
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
def test_list_compartments(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListCompartments'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListCompartments')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListCompartments')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_compartments(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_compartments(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_compartments(
                        compartment_id=request.pop(util.camelize('compartment_id')),
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

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListCostTrackingTags')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_cost_tracking_tags(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_cost_tracking_tags(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_cost_tracking_tags(
                        compartment_id=request.pop(util.camelize('compartment_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_customer_secret_keys(
                user_id=request.pop(util.camelize('user_id')),
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
def test_list_dynamic_groups(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListDynamicGroups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListDynamicGroups')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListDynamicGroups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_dynamic_groups(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_dynamic_groups(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_dynamic_groups(
                        compartment_id=request.pop(util.camelize('compartment_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_fault_domains(
                compartment_id=request.pop(util.camelize('compartment_id')),
                availability_domain=request.pop(util.camelize('availability_domain')),
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

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListGroups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_groups(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_groups(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_groups(
                        compartment_id=request.pop(util.camelize('compartment_id')),
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
def test_list_identity_provider_groups(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListIdentityProviderGroups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListIdentityProviderGroups')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListIdentityProviderGroups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_identity_provider_groups(
                identity_provider_id=request.pop(util.camelize('identity_provider_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_identity_provider_groups(
                    identity_provider_id=request.pop(util.camelize('identity_provider_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_identity_provider_groups(
                        identity_provider_id=request.pop(util.camelize('identity_provider_id')),
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

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListIdentityProviders')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_identity_providers(
                protocol=request.pop(util.camelize('protocol')),
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_identity_providers(
                    protocol=request.pop(util.camelize('protocol')),
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_identity_providers(
                        protocol=request.pop(util.camelize('protocol')),
                        compartment_id=request.pop(util.camelize('compartment_id')),
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

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListIdpGroupMappings')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_idp_group_mappings(
                identity_provider_id=request.pop(util.camelize('identity_provider_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_idp_group_mappings(
                    identity_provider_id=request.pop(util.camelize('identity_provider_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_idp_group_mappings(
                        identity_provider_id=request.pop(util.camelize('identity_provider_id')),
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

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListMfaTotpDevices')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_mfa_totp_devices(
                user_id=request.pop(util.camelize('user_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_mfa_totp_devices(
                    user_id=request.pop(util.camelize('user_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_mfa_totp_devices(
                        user_id=request.pop(util.camelize('user_id')),
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
def test_list_policies(testing_service_client):
    if not testing_service_client.is_api_enabled('identity', 'ListPolicies'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity', util.camelize('identity'), 'ListPolicies')
    )

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListPolicies')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_policies(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_policies(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_policies(
                        compartment_id=request.pop(util.camelize('compartment_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_region_subscriptions(
                tenancy_id=request.pop(util.camelize('tenancy_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_smtp_credentials(
                user_id=request.pop(util.camelize('user_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_swift_passwords(
                user_id=request.pop(util.camelize('user_id')),
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

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListTagDefaults')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_tag_defaults(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
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

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListTagNamespaces')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_tag_namespaces(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_tag_namespaces(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_tag_namespaces(
                        compartment_id=request.pop(util.camelize('compartment_id')),
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

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListTaggingWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_tagging_work_request_errors(
                work_request_id=request.pop(util.camelize('work_request_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_tagging_work_request_errors(
                    work_request_id=request.pop(util.camelize('work_request_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_tagging_work_request_errors(
                        work_request_id=request.pop(util.camelize('work_request_id')),
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

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListTaggingWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_tagging_work_request_logs(
                work_request_id=request.pop(util.camelize('work_request_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_tagging_work_request_logs(
                    work_request_id=request.pop(util.camelize('work_request_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_tagging_work_request_logs(
                        work_request_id=request.pop(util.camelize('work_request_id')),
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

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListTaggingWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_tagging_work_requests(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_tagging_work_requests(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_tagging_work_requests(
                        compartment_id=request.pop(util.camelize('compartment_id')),
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

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListTags')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_tags(
                tag_namespace_id=request.pop(util.camelize('tag_namespace_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_tags(
                    tag_namespace_id=request.pop(util.camelize('tag_namespace_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_tags(
                        tag_namespace_id=request.pop(util.camelize('tag_namespace_id')),
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

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListUserGroupMemberships')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_user_group_memberships(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_user_group_memberships(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_user_group_memberships(
                        compartment_id=request.pop(util.camelize('compartment_id')),
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

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListUsers')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_users(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_users(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_users(
                        compartment_id=request.pop(util.camelize('compartment_id')),
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

    request_containers = testing_service_client.get_requests(service_name='identity', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.list_work_requests(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_requests(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_requests(
                        compartment_id=request.pop(util.camelize('compartment_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.move_compartment(
                compartment_id=request.pop(util.camelize('compartment_id')),
                move_compartment_details=request.pop(util.camelize('move_compartment_details')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.remove_user_from_group(
                user_group_membership_id=request.pop(util.camelize('user_group_membership_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.reset_idp_scim_client(
                identity_provider_id=request.pop(util.camelize('identity_provider_id')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.update_auth_token(
                user_id=request.pop(util.camelize('user_id')),
                auth_token_id=request.pop(util.camelize('auth_token_id')),
                update_auth_token_details=request.pop(util.camelize('update_auth_token_details')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.update_authentication_policy(
                compartment_id=request.pop(util.camelize('compartment_id')),
                update_authentication_policy_details=request.pop(util.camelize('update_authentication_policy_details')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.update_compartment(
                compartment_id=request.pop(util.camelize('compartment_id')),
                update_compartment_details=request.pop(util.camelize('update_compartment_details')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.update_customer_secret_key(
                user_id=request.pop(util.camelize('user_id')),
                customer_secret_key_id=request.pop(util.camelize('customer_secret_key_id')),
                update_customer_secret_key_details=request.pop(util.camelize('update_customer_secret_key_details')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.update_dynamic_group(
                dynamic_group_id=request.pop(util.camelize('dynamic_group_id')),
                update_dynamic_group_details=request.pop(util.camelize('update_dynamic_group_details')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.update_group(
                group_id=request.pop(util.camelize('group_id')),
                update_group_details=request.pop(util.camelize('update_group_details')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.update_identity_provider(
                identity_provider_id=request.pop(util.camelize('identity_provider_id')),
                update_identity_provider_details=request.pop(util.camelize('update_identity_provider_details')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.update_idp_group_mapping(
                identity_provider_id=request.pop(util.camelize('identity_provider_id')),
                mapping_id=request.pop(util.camelize('mapping_id')),
                update_idp_group_mapping_details=request.pop(util.camelize('update_idp_group_mapping_details')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.update_policy(
                policy_id=request.pop(util.camelize('policy_id')),
                update_policy_details=request.pop(util.camelize('update_policy_details')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.update_smtp_credential(
                user_id=request.pop(util.camelize('user_id')),
                smtp_credential_id=request.pop(util.camelize('smtp_credential_id')),
                update_smtp_credential_details=request.pop(util.camelize('update_smtp_credential_details')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.update_swift_password(
                user_id=request.pop(util.camelize('user_id')),
                swift_password_id=request.pop(util.camelize('swift_password_id')),
                update_swift_password_details=request.pop(util.camelize('update_swift_password_details')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.update_tag(
                tag_namespace_id=request.pop(util.camelize('tag_namespace_id')),
                tag_name=request.pop(util.camelize('tag_name')),
                update_tag_details=request.pop(util.camelize('update_tag_details')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.update_tag_default(
                tag_default_id=request.pop(util.camelize('tag_default_id')),
                update_tag_default_details=request.pop(util.camelize('update_tag_default_details')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.update_tag_namespace(
                tag_namespace_id=request.pop(util.camelize('tag_namespace_id')),
                update_tag_namespace_details=request.pop(util.camelize('update_tag_namespace_details')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.update_user(
                user_id=request.pop(util.camelize('user_id')),
                update_user_details=request.pop(util.camelize('update_user_details')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.update_user_capabilities(
                user_id=request.pop(util.camelize('user_id')),
                update_user_capabilities_details=request.pop(util.camelize('update_user_capabilities_details')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.update_user_state(
                user_id=request.pop(util.camelize('user_id')),
                update_state_details=request.pop(util.camelize('update_state_details')),
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
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.identity.IdentityClient(config, service_endpoint=service_endpoint)
            response = client.upload_api_key(
                user_id=request.pop(util.camelize('user_id')),
                create_api_key_details=request.pop(util.camelize('create_api_key_details')),
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
