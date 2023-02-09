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

        cassette_location = os.path.join('generated', 'recovery_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="rcs_dev_ww_grp@oracle.com" jiraProject="RCCS" opsJiraProject="RCCS"
def test_change_protected_database_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('recovery', 'ChangeProtectedDatabaseCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('recovery', util.camelize('database_recovery'), 'ChangeProtectedDatabaseCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='recovery', api_name='ChangeProtectedDatabaseCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.recovery.DatabaseRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.change_protected_database_compartment(
                protected_database_id=request.pop(util.camelize('protectedDatabaseId')),
                change_protected_database_compartment_details=request.pop(util.camelize('ChangeProtectedDatabaseCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'recovery',
            'ChangeProtectedDatabaseCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_protected_database_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="rcs_dev_ww_grp@oracle.com" jiraProject="RCCS" opsJiraProject="RCCS"
def test_change_protection_policy_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('recovery', 'ChangeProtectionPolicyCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('recovery', util.camelize('database_recovery'), 'ChangeProtectionPolicyCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='recovery', api_name='ChangeProtectionPolicyCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.recovery.DatabaseRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.change_protection_policy_compartment(
                protection_policy_id=request.pop(util.camelize('protectionPolicyId')),
                change_protection_policy_compartment_details=request.pop(util.camelize('ChangeProtectionPolicyCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'recovery',
            'ChangeProtectionPolicyCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_protection_policy_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="rcs_dev_ww_grp@oracle.com" jiraProject="RCCS" opsJiraProject="RCCS"
def test_change_recovery_service_subnet_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('recovery', 'ChangeRecoveryServiceSubnetCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('recovery', util.camelize('database_recovery'), 'ChangeRecoveryServiceSubnetCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='recovery', api_name='ChangeRecoveryServiceSubnetCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.recovery.DatabaseRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.change_recovery_service_subnet_compartment(
                recovery_service_subnet_id=request.pop(util.camelize('recoveryServiceSubnetId')),
                change_recovery_service_subnet_compartment_details=request.pop(util.camelize('ChangeRecoveryServiceSubnetCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'recovery',
            'ChangeRecoveryServiceSubnetCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_recovery_service_subnet_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="rcs_dev_ww_grp@oracle.com" jiraProject="RCCS" opsJiraProject="RCCS"
def test_create_protected_database(testing_service_client):
    if not testing_service_client.is_api_enabled('recovery', 'CreateProtectedDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('recovery', util.camelize('database_recovery'), 'CreateProtectedDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='recovery', api_name='CreateProtectedDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.recovery.DatabaseRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.create_protected_database(
                create_protected_database_details=request.pop(util.camelize('CreateProtectedDatabaseDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'recovery',
            'CreateProtectedDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'protectedDatabase',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="rcs_dev_ww_grp@oracle.com" jiraProject="RCCS" opsJiraProject="RCCS"
def test_create_protection_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('recovery', 'CreateProtectionPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('recovery', util.camelize('database_recovery'), 'CreateProtectionPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='recovery', api_name='CreateProtectionPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.recovery.DatabaseRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.create_protection_policy(
                create_protection_policy_details=request.pop(util.camelize('CreateProtectionPolicyDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'recovery',
            'CreateProtectionPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'protectionPolicy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="rcs_dev_ww_grp@oracle.com" jiraProject="RCCS" opsJiraProject="RCCS"
def test_create_recovery_service_subnet(testing_service_client):
    if not testing_service_client.is_api_enabled('recovery', 'CreateRecoveryServiceSubnet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('recovery', util.camelize('database_recovery'), 'CreateRecoveryServiceSubnet')
    )

    request_containers = testing_service_client.get_requests(service_name='recovery', api_name='CreateRecoveryServiceSubnet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.recovery.DatabaseRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.create_recovery_service_subnet(
                create_recovery_service_subnet_details=request.pop(util.camelize('CreateRecoveryServiceSubnetDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'recovery',
            'CreateRecoveryServiceSubnet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'recoveryServiceSubnet',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="rcs_dev_ww_grp@oracle.com" jiraProject="RCCS" opsJiraProject="RCCS"
def test_delete_protected_database(testing_service_client):
    if not testing_service_client.is_api_enabled('recovery', 'DeleteProtectedDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('recovery', util.camelize('database_recovery'), 'DeleteProtectedDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='recovery', api_name='DeleteProtectedDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.recovery.DatabaseRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.delete_protected_database(
                protected_database_id=request.pop(util.camelize('protectedDatabaseId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'recovery',
            'DeleteProtectedDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_protected_database',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="rcs_dev_ww_grp@oracle.com" jiraProject="RCCS" opsJiraProject="RCCS"
def test_delete_protection_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('recovery', 'DeleteProtectionPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('recovery', util.camelize('database_recovery'), 'DeleteProtectionPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='recovery', api_name='DeleteProtectionPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.recovery.DatabaseRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.delete_protection_policy(
                protection_policy_id=request.pop(util.camelize('protectionPolicyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'recovery',
            'DeleteProtectionPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_protection_policy',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="rcs_dev_ww_grp@oracle.com" jiraProject="RCCS" opsJiraProject="RCCS"
def test_delete_recovery_service_subnet(testing_service_client):
    if not testing_service_client.is_api_enabled('recovery', 'DeleteRecoveryServiceSubnet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('recovery', util.camelize('database_recovery'), 'DeleteRecoveryServiceSubnet')
    )

    request_containers = testing_service_client.get_requests(service_name='recovery', api_name='DeleteRecoveryServiceSubnet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.recovery.DatabaseRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.delete_recovery_service_subnet(
                recovery_service_subnet_id=request.pop(util.camelize('recoveryServiceSubnetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'recovery',
            'DeleteRecoveryServiceSubnet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_recovery_service_subnet',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="rcs_dev_ww_grp@oracle.com" jiraProject="RCCS" opsJiraProject="RCCS"
def test_fetch_protected_database_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('recovery', 'FetchProtectedDatabaseConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('recovery', util.camelize('database_recovery'), 'FetchProtectedDatabaseConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='recovery', api_name='FetchProtectedDatabaseConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.recovery.DatabaseRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.fetch_protected_database_configuration(
                protected_database_id=request.pop(util.camelize('protectedDatabaseId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'recovery',
            'FetchProtectedDatabaseConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="rcs_dev_ww_grp@oracle.com" jiraProject="RCCS" opsJiraProject="RCCS"
def test_get_protected_database(testing_service_client):
    if not testing_service_client.is_api_enabled('recovery', 'GetProtectedDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('recovery', util.camelize('database_recovery'), 'GetProtectedDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='recovery', api_name='GetProtectedDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.recovery.DatabaseRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.get_protected_database(
                protected_database_id=request.pop(util.camelize('protectedDatabaseId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'recovery',
            'GetProtectedDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'protectedDatabase',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="rcs_dev_ww_grp@oracle.com" jiraProject="RCCS" opsJiraProject="RCCS"
def test_get_protection_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('recovery', 'GetProtectionPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('recovery', util.camelize('database_recovery'), 'GetProtectionPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='recovery', api_name='GetProtectionPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.recovery.DatabaseRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.get_protection_policy(
                protection_policy_id=request.pop(util.camelize('protectionPolicyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'recovery',
            'GetProtectionPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'protectionPolicy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="rcs_dev_ww_grp@oracle.com" jiraProject="RCCS" opsJiraProject="RCCS"
def test_get_recovery_service_subnet(testing_service_client):
    if not testing_service_client.is_api_enabled('recovery', 'GetRecoveryServiceSubnet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('recovery', util.camelize('database_recovery'), 'GetRecoveryServiceSubnet')
    )

    request_containers = testing_service_client.get_requests(service_name='recovery', api_name='GetRecoveryServiceSubnet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.recovery.DatabaseRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.get_recovery_service_subnet(
                recovery_service_subnet_id=request.pop(util.camelize('recoveryServiceSubnetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'recovery',
            'GetRecoveryServiceSubnet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'recoveryServiceSubnet',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="rcs_dev_ww_grp@oracle.com" jiraProject="RCCS" opsJiraProject="RCCS"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('recovery', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('recovery', util.camelize('database_recovery'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='recovery', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.recovery.DatabaseRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'recovery',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="rcs_dev_ww_grp@oracle.com" jiraProject="RCCS" opsJiraProject="RCCS"
def test_list_protected_databases(testing_service_client):
    if not testing_service_client.is_api_enabled('recovery', 'ListProtectedDatabases'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('recovery', util.camelize('database_recovery'), 'ListProtectedDatabases')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='recovery', api_name='ListProtectedDatabases')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.recovery.DatabaseRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.list_protected_databases(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_protected_databases(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_protected_databases(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'recovery',
            'ListProtectedDatabases',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'protectedDatabaseCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="rcs_dev_ww_grp@oracle.com" jiraProject="RCCS" opsJiraProject="RCCS"
def test_list_protection_policies(testing_service_client):
    if not testing_service_client.is_api_enabled('recovery', 'ListProtectionPolicies'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('recovery', util.camelize('database_recovery'), 'ListProtectionPolicies')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='recovery', api_name='ListProtectionPolicies')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.recovery.DatabaseRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.list_protection_policies(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_protection_policies(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_protection_policies(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'recovery',
            'ListProtectionPolicies',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'protectionPolicyCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="rcs_dev_ww_grp@oracle.com" jiraProject="RCCS" opsJiraProject="RCCS"
def test_list_recovery_service_subnets(testing_service_client):
    if not testing_service_client.is_api_enabled('recovery', 'ListRecoveryServiceSubnets'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('recovery', util.camelize('database_recovery'), 'ListRecoveryServiceSubnets')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='recovery', api_name='ListRecoveryServiceSubnets')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.recovery.DatabaseRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.list_recovery_service_subnets(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_recovery_service_subnets(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_recovery_service_subnets(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'recovery',
            'ListRecoveryServiceSubnets',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'recoveryServiceSubnetCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="rcs_dev_ww_grp@oracle.com" jiraProject="RCCS" opsJiraProject="RCCS"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('recovery', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('recovery', util.camelize('database_recovery'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='recovery', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.recovery.DatabaseRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_errors(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_errors(
                    work_request_id=request.pop(util.camelize('workRequestId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_request_errors(
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'recovery',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestErrorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="rcs_dev_ww_grp@oracle.com" jiraProject="RCCS" opsJiraProject="RCCS"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('recovery', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('recovery', util.camelize('database_recovery'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='recovery', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.recovery.DatabaseRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_logs(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_logs(
                    work_request_id=request.pop(util.camelize('workRequestId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_request_logs(
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'recovery',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="rcs_dev_ww_grp@oracle.com" jiraProject="RCCS" opsJiraProject="RCCS"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('recovery', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('recovery', util.camelize('database_recovery'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='recovery', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.recovery.DatabaseRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.list_work_requests(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_requests(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_requests(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'recovery',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="rcs_dev_ww_grp@oracle.com" jiraProject="RCCS" opsJiraProject="RCCS"
def test_update_protected_database(testing_service_client):
    if not testing_service_client.is_api_enabled('recovery', 'UpdateProtectedDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('recovery', util.camelize('database_recovery'), 'UpdateProtectedDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='recovery', api_name='UpdateProtectedDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.recovery.DatabaseRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.update_protected_database(
                protected_database_id=request.pop(util.camelize('protectedDatabaseId')),
                update_protected_database_details=request.pop(util.camelize('UpdateProtectedDatabaseDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'recovery',
            'UpdateProtectedDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_protected_database',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="rcs_dev_ww_grp@oracle.com" jiraProject="RCCS" opsJiraProject="RCCS"
def test_update_protection_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('recovery', 'UpdateProtectionPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('recovery', util.camelize('database_recovery'), 'UpdateProtectionPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='recovery', api_name='UpdateProtectionPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.recovery.DatabaseRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.update_protection_policy(
                protection_policy_id=request.pop(util.camelize('protectionPolicyId')),
                update_protection_policy_details=request.pop(util.camelize('UpdateProtectionPolicyDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'recovery',
            'UpdateProtectionPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_protection_policy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="rcs_dev_ww_grp@oracle.com" jiraProject="RCCS" opsJiraProject="RCCS"
def test_update_recovery_service_subnet(testing_service_client):
    if not testing_service_client.is_api_enabled('recovery', 'UpdateRecoveryServiceSubnet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('recovery', util.camelize('database_recovery'), 'UpdateRecoveryServiceSubnet')
    )

    request_containers = testing_service_client.get_requests(service_name='recovery', api_name='UpdateRecoveryServiceSubnet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.recovery.DatabaseRecoveryClient(config, service_endpoint=service_endpoint)
            response = client.update_recovery_service_subnet(
                recovery_service_subnet_id=request.pop(util.camelize('recoveryServiceSubnetId')),
                update_recovery_service_subnet_details=request.pop(util.camelize('UpdateRecoveryServiceSubnetDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'recovery',
            'UpdateRecoveryServiceSubnet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_recovery_service_subnet',
            False,
            False
        )
