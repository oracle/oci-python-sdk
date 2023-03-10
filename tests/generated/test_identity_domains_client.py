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

        cassette_location = os.path.join('generated', 'identity_domains_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_api_key(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'CreateApiKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'CreateApiKey')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='CreateApiKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "CreateApiKey")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.create_api_key(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'CreateApiKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'apiKey',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_auth_token(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'CreateAuthToken'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'CreateAuthToken')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='CreateAuthToken')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "CreateAuthToken")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.create_auth_token(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
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
def test_create_authentication_factors_remover(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'CreateAuthenticationFactorsRemover'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'CreateAuthenticationFactorsRemover')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='CreateAuthenticationFactorsRemover')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "CreateAuthenticationFactorsRemover")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.create_authentication_factors_remover(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'CreateAuthenticationFactorsRemover',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'authenticationFactorsRemover',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_customer_secret_key(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'CreateCustomerSecretKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'CreateCustomerSecretKey')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='CreateCustomerSecretKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "CreateCustomerSecretKey")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.create_customer_secret_key(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
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
def test_create_dynamic_resource_group(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'CreateDynamicResourceGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'CreateDynamicResourceGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='CreateDynamicResourceGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "CreateDynamicResourceGroup")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.create_dynamic_resource_group(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'CreateDynamicResourceGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dynamicResourceGroup',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_group(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'CreateGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'CreateGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='CreateGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "CreateGroup")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.create_group(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
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
    if not testing_service_client.is_api_enabled('identity_domains', 'CreateIdentityProvider'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'CreateIdentityProvider')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='CreateIdentityProvider')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "CreateIdentityProvider")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.create_identity_provider(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
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
def test_create_me(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'CreateMe'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'CreateMe')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='CreateMe')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "CreateMe")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.create_me(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'CreateMe',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'me',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_my_api_key(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'CreateMyApiKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'CreateMyApiKey')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='CreateMyApiKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "CreateMyApiKey")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.create_my_api_key(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'CreateMyApiKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'myApiKey',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_my_auth_token(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'CreateMyAuthToken'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'CreateMyAuthToken')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='CreateMyAuthToken')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "CreateMyAuthToken")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.create_my_auth_token(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'CreateMyAuthToken',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'myAuthToken',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_my_authentication_factor_initiator(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'CreateMyAuthenticationFactorInitiator'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'CreateMyAuthenticationFactorInitiator')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='CreateMyAuthenticationFactorInitiator')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "CreateMyAuthenticationFactorInitiator")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.create_my_authentication_factor_initiator(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'CreateMyAuthenticationFactorInitiator',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'myAuthenticationFactorInitiator',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_my_authentication_factor_validator(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'CreateMyAuthenticationFactorValidator'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'CreateMyAuthenticationFactorValidator')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='CreateMyAuthenticationFactorValidator')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "CreateMyAuthenticationFactorValidator")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.create_my_authentication_factor_validator(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'CreateMyAuthenticationFactorValidator',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'myAuthenticationFactorValidator',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_my_authentication_factors_remover(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'CreateMyAuthenticationFactorsRemover'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'CreateMyAuthenticationFactorsRemover')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='CreateMyAuthenticationFactorsRemover')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "CreateMyAuthenticationFactorsRemover")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.create_my_authentication_factors_remover(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'CreateMyAuthenticationFactorsRemover',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'myAuthenticationFactorsRemover',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_my_customer_secret_key(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'CreateMyCustomerSecretKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'CreateMyCustomerSecretKey')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='CreateMyCustomerSecretKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "CreateMyCustomerSecretKey")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.create_my_customer_secret_key(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'CreateMyCustomerSecretKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'myCustomerSecretKey',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_my_o_auth2_client_credential(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'CreateMyOAuth2ClientCredential'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'CreateMyOAuth2ClientCredential')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='CreateMyOAuth2ClientCredential')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "CreateMyOAuth2ClientCredential")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.create_my_o_auth2_client_credential(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'CreateMyOAuth2ClientCredential',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'myOAuth2ClientCredential',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_my_smtp_credential(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'CreateMySmtpCredential'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'CreateMySmtpCredential')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='CreateMySmtpCredential')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "CreateMySmtpCredential")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.create_my_smtp_credential(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'CreateMySmtpCredential',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mySmtpCredential',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_my_support_account(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'CreateMySupportAccount'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'CreateMySupportAccount')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='CreateMySupportAccount')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "CreateMySupportAccount")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.create_my_support_account(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'CreateMySupportAccount',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mySupportAccount',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_my_user_db_credential(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'CreateMyUserDbCredential'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'CreateMyUserDbCredential')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='CreateMyUserDbCredential')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "CreateMyUserDbCredential")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.create_my_user_db_credential(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'CreateMyUserDbCredential',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'myUserDbCredential',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_o_auth2_client_credential(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'CreateOAuth2ClientCredential'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'CreateOAuth2ClientCredential')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='CreateOAuth2ClientCredential')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "CreateOAuth2ClientCredential")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.create_o_auth2_client_credential(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'CreateOAuth2ClientCredential',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'oAuth2ClientCredential',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_password_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'CreatePasswordPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'CreatePasswordPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='CreatePasswordPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "CreatePasswordPolicy")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.create_password_policy(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'CreatePasswordPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'passwordPolicy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_create_smtp_credential(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'CreateSmtpCredential'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'CreateSmtpCredential')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='CreateSmtpCredential')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "CreateSmtpCredential")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.create_smtp_credential(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
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
def test_create_user(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'CreateUser'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'CreateUser')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='CreateUser')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "CreateUser")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.create_user(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
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
def test_create_user_db_credential(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'CreateUserDbCredential'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'CreateUserDbCredential')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='CreateUserDbCredential')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "CreateUserDbCredential")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.create_user_db_credential(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'CreateUserDbCredential',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'userDbCredential',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_delete_api_key(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'DeleteApiKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'DeleteApiKey')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='DeleteApiKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "DeleteApiKey")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.delete_api_key(
                api_key_id=request.pop(util.camelize('apiKeyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
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
    if not testing_service_client.is_api_enabled('identity_domains', 'DeleteAuthToken'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'DeleteAuthToken')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='DeleteAuthToken')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "DeleteAuthToken")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.delete_auth_token(
                auth_token_id=request.pop(util.camelize('authTokenId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
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
def test_delete_customer_secret_key(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'DeleteCustomerSecretKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'DeleteCustomerSecretKey')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='DeleteCustomerSecretKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "DeleteCustomerSecretKey")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.delete_customer_secret_key(
                customer_secret_key_id=request.pop(util.camelize('customerSecretKeyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
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
def test_delete_dynamic_resource_group(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'DeleteDynamicResourceGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'DeleteDynamicResourceGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='DeleteDynamicResourceGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "DeleteDynamicResourceGroup")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.delete_dynamic_resource_group(
                dynamic_resource_group_id=request.pop(util.camelize('dynamicResourceGroupId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'DeleteDynamicResourceGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_dynamic_resource_group',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_delete_group(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'DeleteGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'DeleteGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='DeleteGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "DeleteGroup")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.delete_group(
                group_id=request.pop(util.camelize('groupId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
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
    if not testing_service_client.is_api_enabled('identity_domains', 'DeleteIdentityProvider'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'DeleteIdentityProvider')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='DeleteIdentityProvider')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "DeleteIdentityProvider")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.delete_identity_provider(
                identity_provider_id=request.pop(util.camelize('identityProviderId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
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
def test_delete_my_api_key(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'DeleteMyApiKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'DeleteMyApiKey')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='DeleteMyApiKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "DeleteMyApiKey")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.delete_my_api_key(
                my_api_key_id=request.pop(util.camelize('myApiKeyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'DeleteMyApiKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_my_api_key',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_delete_my_auth_token(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'DeleteMyAuthToken'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'DeleteMyAuthToken')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='DeleteMyAuthToken')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "DeleteMyAuthToken")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.delete_my_auth_token(
                my_auth_token_id=request.pop(util.camelize('myAuthTokenId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'DeleteMyAuthToken',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_my_auth_token',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_delete_my_customer_secret_key(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'DeleteMyCustomerSecretKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'DeleteMyCustomerSecretKey')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='DeleteMyCustomerSecretKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "DeleteMyCustomerSecretKey")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.delete_my_customer_secret_key(
                my_customer_secret_key_id=request.pop(util.camelize('myCustomerSecretKeyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'DeleteMyCustomerSecretKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_my_customer_secret_key',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_delete_my_device(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'DeleteMyDevice'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'DeleteMyDevice')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='DeleteMyDevice')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "DeleteMyDevice")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.delete_my_device(
                my_device_id=request.pop(util.camelize('myDeviceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'DeleteMyDevice',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_my_device',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_delete_my_o_auth2_client_credential(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'DeleteMyOAuth2ClientCredential'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'DeleteMyOAuth2ClientCredential')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='DeleteMyOAuth2ClientCredential')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "DeleteMyOAuth2ClientCredential")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.delete_my_o_auth2_client_credential(
                my_o_auth2_client_credential_id=request.pop(util.camelize('myOAuth2ClientCredentialId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'DeleteMyOAuth2ClientCredential',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_my_o_auth2_client_credential',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_delete_my_smtp_credential(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'DeleteMySmtpCredential'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'DeleteMySmtpCredential')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='DeleteMySmtpCredential')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "DeleteMySmtpCredential")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.delete_my_smtp_credential(
                my_smtp_credential_id=request.pop(util.camelize('mySmtpCredentialId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'DeleteMySmtpCredential',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_my_smtp_credential',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_delete_my_support_account(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'DeleteMySupportAccount'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'DeleteMySupportAccount')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='DeleteMySupportAccount')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "DeleteMySupportAccount")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.delete_my_support_account(
                my_support_account_id=request.pop(util.camelize('mySupportAccountId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'DeleteMySupportAccount',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_my_support_account',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_delete_my_trusted_user_agent(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'DeleteMyTrustedUserAgent'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'DeleteMyTrustedUserAgent')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='DeleteMyTrustedUserAgent')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "DeleteMyTrustedUserAgent")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.delete_my_trusted_user_agent(
                my_trusted_user_agent_id=request.pop(util.camelize('myTrustedUserAgentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'DeleteMyTrustedUserAgent',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_my_trusted_user_agent',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_delete_my_user_db_credential(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'DeleteMyUserDbCredential'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'DeleteMyUserDbCredential')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='DeleteMyUserDbCredential')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "DeleteMyUserDbCredential")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.delete_my_user_db_credential(
                my_user_db_credential_id=request.pop(util.camelize('myUserDbCredentialId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'DeleteMyUserDbCredential',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_my_user_db_credential',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_delete_o_auth2_client_credential(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'DeleteOAuth2ClientCredential'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'DeleteOAuth2ClientCredential')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='DeleteOAuth2ClientCredential')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "DeleteOAuth2ClientCredential")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.delete_o_auth2_client_credential(
                o_auth2_client_credential_id=request.pop(util.camelize('oAuth2ClientCredentialId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'DeleteOAuth2ClientCredential',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_o_auth2_client_credential',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_delete_password_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'DeletePasswordPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'DeletePasswordPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='DeletePasswordPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "DeletePasswordPolicy")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.delete_password_policy(
                password_policy_id=request.pop(util.camelize('passwordPolicyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'DeletePasswordPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_password_policy',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_delete_smtp_credential(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'DeleteSmtpCredential'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'DeleteSmtpCredential')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='DeleteSmtpCredential')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "DeleteSmtpCredential")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.delete_smtp_credential(
                smtp_credential_id=request.pop(util.camelize('smtpCredentialId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
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
def test_delete_user(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'DeleteUser'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'DeleteUser')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='DeleteUser')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "DeleteUser")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.delete_user(
                user_id=request.pop(util.camelize('userId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
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
def test_delete_user_db_credential(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'DeleteUserDbCredential'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'DeleteUserDbCredential')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='DeleteUserDbCredential')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "DeleteUserDbCredential")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.delete_user_db_credential(
                user_db_credential_id=request.pop(util.camelize('userDbCredentialId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'DeleteUserDbCredential',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_user_db_credential',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_api_key(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'GetApiKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'GetApiKey')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='GetApiKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "GetApiKey")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.get_api_key(
                api_key_id=request.pop(util.camelize('apiKeyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'GetApiKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'apiKey',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_auth_token(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'GetAuthToken'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'GetAuthToken')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='GetAuthToken')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "GetAuthToken")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.get_auth_token(
                auth_token_id=request.pop(util.camelize('authTokenId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'GetAuthToken',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'authToken',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_authentication_factor_setting(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'GetAuthenticationFactorSetting'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'GetAuthenticationFactorSetting')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='GetAuthenticationFactorSetting')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "GetAuthenticationFactorSetting")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.get_authentication_factor_setting(
                authentication_factor_setting_id=request.pop(util.camelize('authenticationFactorSettingId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'GetAuthenticationFactorSetting',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'authenticationFactorSetting',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_customer_secret_key(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'GetCustomerSecretKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'GetCustomerSecretKey')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='GetCustomerSecretKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "GetCustomerSecretKey")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.get_customer_secret_key(
                customer_secret_key_id=request.pop(util.camelize('customerSecretKeyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'GetCustomerSecretKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'customerSecretKey',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_dynamic_resource_group(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'GetDynamicResourceGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'GetDynamicResourceGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='GetDynamicResourceGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "GetDynamicResourceGroup")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.get_dynamic_resource_group(
                dynamic_resource_group_id=request.pop(util.camelize('dynamicResourceGroupId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'GetDynamicResourceGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dynamicResourceGroup',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_group(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'GetGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'GetGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='GetGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "GetGroup")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.get_group(
                group_id=request.pop(util.camelize('groupId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
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
    if not testing_service_client.is_api_enabled('identity_domains', 'GetIdentityProvider'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'GetIdentityProvider')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='GetIdentityProvider')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "GetIdentityProvider")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.get_identity_provider(
                identity_provider_id=request.pop(util.camelize('identityProviderId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
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
def test_get_kmsi_setting(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'GetKmsiSetting'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'GetKmsiSetting')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='GetKmsiSetting')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "GetKmsiSetting")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.get_kmsi_setting(
                kmsi_setting_id=request.pop(util.camelize('kmsiSettingId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'GetKmsiSetting',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'kmsiSetting',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_me(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'GetMe'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'GetMe')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='GetMe')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "GetMe")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.get_me(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'GetMe',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'me',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_my_api_key(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'GetMyApiKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'GetMyApiKey')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='GetMyApiKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "GetMyApiKey")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.get_my_api_key(
                my_api_key_id=request.pop(util.camelize('myApiKeyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'GetMyApiKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'myApiKey',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_my_auth_token(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'GetMyAuthToken'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'GetMyAuthToken')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='GetMyAuthToken')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "GetMyAuthToken")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.get_my_auth_token(
                my_auth_token_id=request.pop(util.camelize('myAuthTokenId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'GetMyAuthToken',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'myAuthToken',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_my_customer_secret_key(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'GetMyCustomerSecretKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'GetMyCustomerSecretKey')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='GetMyCustomerSecretKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "GetMyCustomerSecretKey")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.get_my_customer_secret_key(
                my_customer_secret_key_id=request.pop(util.camelize('myCustomerSecretKeyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'GetMyCustomerSecretKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'myCustomerSecretKey',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_my_device(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'GetMyDevice'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'GetMyDevice')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='GetMyDevice')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "GetMyDevice")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.get_my_device(
                my_device_id=request.pop(util.camelize('myDeviceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'GetMyDevice',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'myDevice',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_my_o_auth2_client_credential(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'GetMyOAuth2ClientCredential'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'GetMyOAuth2ClientCredential')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='GetMyOAuth2ClientCredential')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "GetMyOAuth2ClientCredential")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.get_my_o_auth2_client_credential(
                my_o_auth2_client_credential_id=request.pop(util.camelize('myOAuth2ClientCredentialId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'GetMyOAuth2ClientCredential',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'myOAuth2ClientCredential',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_my_smtp_credential(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'GetMySmtpCredential'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'GetMySmtpCredential')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='GetMySmtpCredential')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "GetMySmtpCredential")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.get_my_smtp_credential(
                my_smtp_credential_id=request.pop(util.camelize('mySmtpCredentialId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'GetMySmtpCredential',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mySmtpCredential',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_my_support_account(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'GetMySupportAccount'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'GetMySupportAccount')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='GetMySupportAccount')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "GetMySupportAccount")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.get_my_support_account(
                my_support_account_id=request.pop(util.camelize('mySupportAccountId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'GetMySupportAccount',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mySupportAccount',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_my_trusted_user_agent(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'GetMyTrustedUserAgent'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'GetMyTrustedUserAgent')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='GetMyTrustedUserAgent')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "GetMyTrustedUserAgent")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.get_my_trusted_user_agent(
                my_trusted_user_agent_id=request.pop(util.camelize('myTrustedUserAgentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'GetMyTrustedUserAgent',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'myTrustedUserAgent',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_my_user_db_credential(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'GetMyUserDbCredential'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'GetMyUserDbCredential')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='GetMyUserDbCredential')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "GetMyUserDbCredential")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.get_my_user_db_credential(
                my_user_db_credential_id=request.pop(util.camelize('myUserDbCredentialId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'GetMyUserDbCredential',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'myUserDbCredential',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_o_auth2_client_credential(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'GetOAuth2ClientCredential'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'GetOAuth2ClientCredential')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='GetOAuth2ClientCredential')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "GetOAuth2ClientCredential")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.get_o_auth2_client_credential(
                o_auth2_client_credential_id=request.pop(util.camelize('oAuth2ClientCredentialId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'GetOAuth2ClientCredential',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'oAuth2ClientCredential',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_password_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'GetPasswordPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'GetPasswordPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='GetPasswordPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "GetPasswordPolicy")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.get_password_policy(
                password_policy_id=request.pop(util.camelize('passwordPolicyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'GetPasswordPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'passwordPolicy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_smtp_credential(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'GetSmtpCredential'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'GetSmtpCredential')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='GetSmtpCredential')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "GetSmtpCredential")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.get_smtp_credential(
                smtp_credential_id=request.pop(util.camelize('smtpCredentialId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'GetSmtpCredential',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'smtpCredential',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_get_user(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'GetUser'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'GetUser')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='GetUser')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "GetUser")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.get_user(
                user_id=request.pop(util.camelize('userId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
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
def test_get_user_db_credential(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'GetUserDbCredential'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'GetUserDbCredential')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='GetUserDbCredential')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "GetUserDbCredential")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.get_user_db_credential(
                user_db_credential_id=request.pop(util.camelize('userDbCredentialId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'GetUserDbCredential',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'userDbCredential',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_api_keys(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'ListApiKeys'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'ListApiKeys')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='ListApiKeys')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "ListApiKeys")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.list_api_keys(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_api_keys(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_api_keys(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'ListApiKeys',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'apiKeys',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_auth_tokens(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'ListAuthTokens'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'ListAuthTokens')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='ListAuthTokens')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "ListAuthTokens")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.list_auth_tokens(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_auth_tokens(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_auth_tokens(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'ListAuthTokens',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'authTokens',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_authentication_factor_settings(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'ListAuthenticationFactorSettings'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'ListAuthenticationFactorSettings')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='ListAuthenticationFactorSettings')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "ListAuthenticationFactorSettings")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.list_authentication_factor_settings(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_authentication_factor_settings(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_authentication_factor_settings(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'ListAuthenticationFactorSettings',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'authenticationFactorSettings',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_customer_secret_keys(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'ListCustomerSecretKeys'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'ListCustomerSecretKeys')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='ListCustomerSecretKeys')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "ListCustomerSecretKeys")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.list_customer_secret_keys(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_customer_secret_keys(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_customer_secret_keys(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'ListCustomerSecretKeys',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'customerSecretKeys',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_dynamic_resource_groups(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'ListDynamicResourceGroups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'ListDynamicResourceGroups')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='ListDynamicResourceGroups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "ListDynamicResourceGroups")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.list_dynamic_resource_groups(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_dynamic_resource_groups(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_dynamic_resource_groups(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'ListDynamicResourceGroups',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dynamicResourceGroups',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_groups(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'ListGroups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'ListGroups')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='ListGroups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "ListGroups")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.list_groups(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_groups(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_groups(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'ListGroups',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'groups',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_identity_providers(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'ListIdentityProviders'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'ListIdentityProviders')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='ListIdentityProviders')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "ListIdentityProviders")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.list_identity_providers(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_identity_providers(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_identity_providers(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'ListIdentityProviders',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'identityProviders',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_kmsi_settings(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'ListKmsiSettings'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'ListKmsiSettings')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='ListKmsiSettings')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "ListKmsiSettings")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.list_kmsi_settings(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_kmsi_settings(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_kmsi_settings(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'ListKmsiSettings',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'kmsiSettings',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_my_api_keys(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'ListMyApiKeys'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'ListMyApiKeys')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='ListMyApiKeys')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "ListMyApiKeys")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.list_my_api_keys(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_my_api_keys(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_my_api_keys(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'ListMyApiKeys',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'myApiKeys',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_my_auth_tokens(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'ListMyAuthTokens'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'ListMyAuthTokens')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='ListMyAuthTokens')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "ListMyAuthTokens")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.list_my_auth_tokens(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_my_auth_tokens(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_my_auth_tokens(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'ListMyAuthTokens',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'myAuthTokens',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_my_customer_secret_keys(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'ListMyCustomerSecretKeys'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'ListMyCustomerSecretKeys')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='ListMyCustomerSecretKeys')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "ListMyCustomerSecretKeys")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.list_my_customer_secret_keys(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_my_customer_secret_keys(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_my_customer_secret_keys(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'ListMyCustomerSecretKeys',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'myCustomerSecretKeys',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_my_devices(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'ListMyDevices'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'ListMyDevices')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='ListMyDevices')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "ListMyDevices")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.list_my_devices(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_my_devices(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_my_devices(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'ListMyDevices',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'myDevices',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_my_groups(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'ListMyGroups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'ListMyGroups')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='ListMyGroups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "ListMyGroups")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.list_my_groups(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_my_groups(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_my_groups(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'ListMyGroups',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'myGroups',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_my_o_auth2_client_credentials(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'ListMyOAuth2ClientCredentials'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'ListMyOAuth2ClientCredentials')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='ListMyOAuth2ClientCredentials')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "ListMyOAuth2ClientCredentials")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.list_my_o_auth2_client_credentials(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_my_o_auth2_client_credentials(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_my_o_auth2_client_credentials(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'ListMyOAuth2ClientCredentials',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'myOAuth2ClientCredentials',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_my_smtp_credentials(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'ListMySmtpCredentials'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'ListMySmtpCredentials')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='ListMySmtpCredentials')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "ListMySmtpCredentials")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.list_my_smtp_credentials(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_my_smtp_credentials(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_my_smtp_credentials(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'ListMySmtpCredentials',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mySmtpCredentials',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_my_support_accounts(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'ListMySupportAccounts'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'ListMySupportAccounts')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='ListMySupportAccounts')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "ListMySupportAccounts")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.list_my_support_accounts(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_my_support_accounts(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_my_support_accounts(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'ListMySupportAccounts',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mySupportAccounts',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_my_trusted_user_agents(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'ListMyTrustedUserAgents'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'ListMyTrustedUserAgents')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='ListMyTrustedUserAgents')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "ListMyTrustedUserAgents")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.list_my_trusted_user_agents(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_my_trusted_user_agents(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_my_trusted_user_agents(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'ListMyTrustedUserAgents',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'myTrustedUserAgents',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_my_user_db_credentials(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'ListMyUserDbCredentials'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'ListMyUserDbCredentials')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='ListMyUserDbCredentials')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "ListMyUserDbCredentials")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.list_my_user_db_credentials(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_my_user_db_credentials(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_my_user_db_credentials(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'ListMyUserDbCredentials',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'myUserDbCredentials',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_o_auth2_client_credentials(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'ListOAuth2ClientCredentials'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'ListOAuth2ClientCredentials')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='ListOAuth2ClientCredentials')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "ListOAuth2ClientCredentials")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.list_o_auth2_client_credentials(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_o_auth2_client_credentials(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_o_auth2_client_credentials(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'ListOAuth2ClientCredentials',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'oAuth2ClientCredentials',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_password_policies(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'ListPasswordPolicies'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'ListPasswordPolicies')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='ListPasswordPolicies')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "ListPasswordPolicies")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.list_password_policies(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_password_policies(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_password_policies(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'ListPasswordPolicies',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'passwordPolicies',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_smtp_credentials(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'ListSmtpCredentials'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'ListSmtpCredentials')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='ListSmtpCredentials')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "ListSmtpCredentials")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.list_smtp_credentials(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_smtp_credentials(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_smtp_credentials(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'ListSmtpCredentials',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'smtpCredentials',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_user_db_credentials(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'ListUserDbCredentials'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'ListUserDbCredentials')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='ListUserDbCredentials')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "ListUserDbCredentials")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.list_user_db_credentials(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_user_db_credentials(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_user_db_credentials(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'ListUserDbCredentials',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'userDbCredentials',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_list_users(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'ListUsers'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'ListUsers')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='ListUsers')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "ListUsers")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.list_users(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_users(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_users(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'ListUsers',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'users',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_patch_api_key(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'PatchApiKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'PatchApiKey')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='PatchApiKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "PatchApiKey")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.patch_api_key(
                api_key_id=request.pop(util.camelize('apiKeyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'PatchApiKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'apiKey',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_patch_auth_token(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'PatchAuthToken'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'PatchAuthToken')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='PatchAuthToken')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "PatchAuthToken")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.patch_auth_token(
                auth_token_id=request.pop(util.camelize('authTokenId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'PatchAuthToken',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'authToken',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_patch_customer_secret_key(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'PatchCustomerSecretKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'PatchCustomerSecretKey')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='PatchCustomerSecretKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "PatchCustomerSecretKey")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.patch_customer_secret_key(
                customer_secret_key_id=request.pop(util.camelize('customerSecretKeyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'PatchCustomerSecretKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'customerSecretKey',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_patch_dynamic_resource_group(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'PatchDynamicResourceGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'PatchDynamicResourceGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='PatchDynamicResourceGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "PatchDynamicResourceGroup")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.patch_dynamic_resource_group(
                dynamic_resource_group_id=request.pop(util.camelize('dynamicResourceGroupId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'PatchDynamicResourceGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dynamicResourceGroup',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_patch_group(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'PatchGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'PatchGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='PatchGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "PatchGroup")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.patch_group(
                group_id=request.pop(util.camelize('groupId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'PatchGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'group',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_patch_identity_provider(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'PatchIdentityProvider'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'PatchIdentityProvider')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='PatchIdentityProvider')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "PatchIdentityProvider")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.patch_identity_provider(
                identity_provider_id=request.pop(util.camelize('identityProviderId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'PatchIdentityProvider',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'identityProvider',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_patch_kmsi_setting(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'PatchKmsiSetting'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'PatchKmsiSetting')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='PatchKmsiSetting')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "PatchKmsiSetting")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.patch_kmsi_setting(
                kmsi_setting_id=request.pop(util.camelize('kmsiSettingId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'PatchKmsiSetting',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'kmsiSetting',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_patch_me(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'PatchMe'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'PatchMe')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='PatchMe')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "PatchMe")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.patch_me(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'PatchMe',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'me',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_patch_my_api_key(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'PatchMyApiKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'PatchMyApiKey')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='PatchMyApiKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "PatchMyApiKey")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.patch_my_api_key(
                my_api_key_id=request.pop(util.camelize('myApiKeyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'PatchMyApiKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'myApiKey',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_patch_my_auth_token(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'PatchMyAuthToken'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'PatchMyAuthToken')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='PatchMyAuthToken')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "PatchMyAuthToken")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.patch_my_auth_token(
                my_auth_token_id=request.pop(util.camelize('myAuthTokenId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'PatchMyAuthToken',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'myAuthToken',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_patch_my_customer_secret_key(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'PatchMyCustomerSecretKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'PatchMyCustomerSecretKey')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='PatchMyCustomerSecretKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "PatchMyCustomerSecretKey")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.patch_my_customer_secret_key(
                my_customer_secret_key_id=request.pop(util.camelize('myCustomerSecretKeyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'PatchMyCustomerSecretKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'myCustomerSecretKey',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_patch_my_device(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'PatchMyDevice'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'PatchMyDevice')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='PatchMyDevice')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "PatchMyDevice")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.patch_my_device(
                my_device_id=request.pop(util.camelize('myDeviceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'PatchMyDevice',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'myDevice',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_patch_my_o_auth2_client_credential(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'PatchMyOAuth2ClientCredential'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'PatchMyOAuth2ClientCredential')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='PatchMyOAuth2ClientCredential')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "PatchMyOAuth2ClientCredential")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.patch_my_o_auth2_client_credential(
                my_o_auth2_client_credential_id=request.pop(util.camelize('myOAuth2ClientCredentialId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'PatchMyOAuth2ClientCredential',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'myOAuth2ClientCredential',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_patch_my_smtp_credential(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'PatchMySmtpCredential'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'PatchMySmtpCredential')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='PatchMySmtpCredential')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "PatchMySmtpCredential")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.patch_my_smtp_credential(
                my_smtp_credential_id=request.pop(util.camelize('mySmtpCredentialId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'PatchMySmtpCredential',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mySmtpCredential',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_patch_o_auth2_client_credential(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'PatchOAuth2ClientCredential'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'PatchOAuth2ClientCredential')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='PatchOAuth2ClientCredential')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "PatchOAuth2ClientCredential")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.patch_o_auth2_client_credential(
                o_auth2_client_credential_id=request.pop(util.camelize('oAuth2ClientCredentialId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'PatchOAuth2ClientCredential',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'oAuth2ClientCredential',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_patch_password_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'PatchPasswordPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'PatchPasswordPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='PatchPasswordPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "PatchPasswordPolicy")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.patch_password_policy(
                password_policy_id=request.pop(util.camelize('passwordPolicyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'PatchPasswordPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'passwordPolicy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_patch_smtp_credential(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'PatchSmtpCredential'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'PatchSmtpCredential')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='PatchSmtpCredential')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "PatchSmtpCredential")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.patch_smtp_credential(
                smtp_credential_id=request.pop(util.camelize('smtpCredentialId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'PatchSmtpCredential',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'smtpCredential',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_patch_user(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'PatchUser'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'PatchUser')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='PatchUser')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "PatchUser")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.patch_user(
                user_id=request.pop(util.camelize('userId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'PatchUser',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'user',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_put_authentication_factor_setting(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'PutAuthenticationFactorSetting'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'PutAuthenticationFactorSetting')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='PutAuthenticationFactorSetting')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "PutAuthenticationFactorSetting")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.put_authentication_factor_setting(
                authentication_factor_setting_id=request.pop(util.camelize('authenticationFactorSettingId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'PutAuthenticationFactorSetting',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'authenticationFactorSetting',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_put_dynamic_resource_group(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'PutDynamicResourceGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'PutDynamicResourceGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='PutDynamicResourceGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "PutDynamicResourceGroup")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.put_dynamic_resource_group(
                dynamic_resource_group_id=request.pop(util.camelize('dynamicResourceGroupId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'PutDynamicResourceGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dynamicResourceGroup',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_put_group(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'PutGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'PutGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='PutGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "PutGroup")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.put_group(
                group_id=request.pop(util.camelize('groupId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'PutGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'group',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_put_identity_provider(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'PutIdentityProvider'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'PutIdentityProvider')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='PutIdentityProvider')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "PutIdentityProvider")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.put_identity_provider(
                identity_provider_id=request.pop(util.camelize('identityProviderId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'PutIdentityProvider',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'identityProvider',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_put_kmsi_setting(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'PutKmsiSetting'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'PutKmsiSetting')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='PutKmsiSetting')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "PutKmsiSetting")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.put_kmsi_setting(
                kmsi_setting_id=request.pop(util.camelize('kmsiSettingId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'PutKmsiSetting',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'kmsiSetting',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_put_me(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'PutMe'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'PutMe')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='PutMe')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "PutMe")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.put_me(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'PutMe',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'me',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_put_me_password_changer(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'PutMePasswordChanger'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'PutMePasswordChanger')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='PutMePasswordChanger')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "PutMePasswordChanger")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.put_me_password_changer(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'PutMePasswordChanger',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mePasswordChanger',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_put_password_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'PutPasswordPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'PutPasswordPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='PutPasswordPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "PutPasswordPolicy")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.put_password_policy(
                password_policy_id=request.pop(util.camelize('passwordPolicyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'PutPasswordPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'passwordPolicy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_put_user(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'PutUser'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'PutUser')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='PutUser')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "PutUser")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.put_user(
                user_id=request.pop(util.camelize('userId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'PutUser',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'user',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_put_user_capabilities_changer(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'PutUserCapabilitiesChanger'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'PutUserCapabilitiesChanger')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='PutUserCapabilitiesChanger')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "PutUserCapabilitiesChanger")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.put_user_capabilities_changer(
                user_capabilities_changer_id=request.pop(util.camelize('userCapabilitiesChangerId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'PutUserCapabilitiesChanger',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'userCapabilitiesChanger',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_put_user_password_changer(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'PutUserPasswordChanger'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'PutUserPasswordChanger')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='PutUserPasswordChanger')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "PutUserPasswordChanger")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.put_user_password_changer(
                user_password_changer_id=request.pop(util.camelize('userPasswordChangerId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'PutUserPasswordChanger',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'userPasswordChanger',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_put_user_password_resetter(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'PutUserPasswordResetter'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'PutUserPasswordResetter')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='PutUserPasswordResetter')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "PutUserPasswordResetter")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.put_user_password_resetter(
                user_password_resetter_id=request.pop(util.camelize('userPasswordResetterId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'PutUserPasswordResetter',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'userPasswordResetter',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_put_user_status_changer(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'PutUserStatusChanger'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'PutUserStatusChanger')
    )

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='PutUserStatusChanger')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "PutUserStatusChanger")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.put_user_status_changer(
                user_status_changer_id=request.pop(util.camelize('userStatusChangerId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'PutUserStatusChanger',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'userStatusChanger',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_search_api_keys(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'SearchApiKeys'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'SearchApiKeys')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='SearchApiKeys')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "SearchApiKeys")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.search_api_keys(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.search_api_keys(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.search_api_keys(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'SearchApiKeys',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'apiKeys',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_search_auth_tokens(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'SearchAuthTokens'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'SearchAuthTokens')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='SearchAuthTokens')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "SearchAuthTokens")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.search_auth_tokens(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.search_auth_tokens(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.search_auth_tokens(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'SearchAuthTokens',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'authTokens',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_search_authentication_factor_settings(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'SearchAuthenticationFactorSettings'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'SearchAuthenticationFactorSettings')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='SearchAuthenticationFactorSettings')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "SearchAuthenticationFactorSettings")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.search_authentication_factor_settings(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.search_authentication_factor_settings(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.search_authentication_factor_settings(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'SearchAuthenticationFactorSettings',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'authenticationFactorSettings',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_search_customer_secret_keys(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'SearchCustomerSecretKeys'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'SearchCustomerSecretKeys')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='SearchCustomerSecretKeys')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "SearchCustomerSecretKeys")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.search_customer_secret_keys(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.search_customer_secret_keys(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.search_customer_secret_keys(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'SearchCustomerSecretKeys',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'customerSecretKeys',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_search_dynamic_resource_groups(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'SearchDynamicResourceGroups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'SearchDynamicResourceGroups')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='SearchDynamicResourceGroups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "SearchDynamicResourceGroups")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.search_dynamic_resource_groups(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.search_dynamic_resource_groups(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.search_dynamic_resource_groups(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'SearchDynamicResourceGroups',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dynamicResourceGroups',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_search_groups(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'SearchGroups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'SearchGroups')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='SearchGroups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "SearchGroups")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.search_groups(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.search_groups(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.search_groups(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'SearchGroups',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'groups',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_search_identity_providers(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'SearchIdentityProviders'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'SearchIdentityProviders')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='SearchIdentityProviders')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "SearchIdentityProviders")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.search_identity_providers(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.search_identity_providers(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.search_identity_providers(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'SearchIdentityProviders',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'identityProviders',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_search_kmsi_settings(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'SearchKmsiSettings'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'SearchKmsiSettings')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='SearchKmsiSettings')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "SearchKmsiSettings")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.search_kmsi_settings(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.search_kmsi_settings(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.search_kmsi_settings(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'SearchKmsiSettings',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'kmsiSettings',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_search_my_groups(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'SearchMyGroups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'SearchMyGroups')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='SearchMyGroups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "SearchMyGroups")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.search_my_groups(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.search_my_groups(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.search_my_groups(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'SearchMyGroups',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'myGroups',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_search_o_auth2_client_credentials(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'SearchOAuth2ClientCredentials'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'SearchOAuth2ClientCredentials')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='SearchOAuth2ClientCredentials')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "SearchOAuth2ClientCredentials")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.search_o_auth2_client_credentials(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.search_o_auth2_client_credentials(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.search_o_auth2_client_credentials(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'SearchOAuth2ClientCredentials',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'oAuth2ClientCredentials',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_search_password_policies(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'SearchPasswordPolicies'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'SearchPasswordPolicies')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='SearchPasswordPolicies')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "SearchPasswordPolicies")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.search_password_policies(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.search_password_policies(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.search_password_policies(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'SearchPasswordPolicies',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'passwordPolicies',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_search_smtp_credentials(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'SearchSmtpCredentials'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'SearchSmtpCredentials')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='SearchSmtpCredentials')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "SearchSmtpCredentials")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.search_smtp_credentials(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.search_smtp_credentials(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.search_smtp_credentials(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'SearchSmtpCredentials',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'smtpCredentials',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_search_user_db_credentials(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'SearchUserDbCredentials'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'SearchUserDbCredentials')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='SearchUserDbCredentials')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "SearchUserDbCredentials")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.search_user_db_credentials(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.search_user_db_credentials(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.search_user_db_credentials(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'SearchUserDbCredentials',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'userDbCredentials',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_identity_team_us_grp@oracle.com" jiraProject="ID" opsJiraProject="ID"
def test_search_users(testing_service_client):
    if not testing_service_client.is_api_enabled('identity_domains', 'SearchUsers'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('identity_domains', util.camelize('identity_domains'), 'SearchUsers')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='identity_domains', api_name='SearchUsers')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("identity_domains", "IdentityDomainsClient", "SearchUsers")
            client = oci.identity_domains.IdentityDomainsClient(config, service_endpoint=service_endpoint)
            response = client.search_users(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.search_users(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.search_users(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'identity_domains',
            'SearchUsers',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'users',
            False,
            True
        )
