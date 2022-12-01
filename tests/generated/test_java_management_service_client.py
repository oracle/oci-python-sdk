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

        cassette_location = os.path.join('generated', 'jms_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_add_fleet_installation_sites(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'AddFleetInstallationSites'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'AddFleetInstallationSites')
    )

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='AddFleetInstallationSites')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.add_fleet_installation_sites(
                fleet_id=request.pop(util.camelize('fleetId')),
                add_fleet_installation_sites_details=request.pop(util.camelize('AddFleetInstallationSitesDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'AddFleetInstallationSites',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'add_fleet_installation_sites',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_cancel_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'CancelWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'CancelWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='CancelWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.cancel_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'CancelWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cancel_work_request',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_change_fleet_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'ChangeFleetCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'ChangeFleetCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='ChangeFleetCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.change_fleet_compartment(
                fleet_id=request.pop(util.camelize('fleetId')),
                change_fleet_compartment_details=request.pop(util.camelize('ChangeFleetCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'ChangeFleetCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_fleet_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_create_blocklist(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'CreateBlocklist'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'CreateBlocklist')
    )

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='CreateBlocklist')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.create_blocklist(
                fleet_id=request.pop(util.camelize('fleetId')),
                create_blocklist_details=request.pop(util.camelize('CreateBlocklistDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'CreateBlocklist',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'blocklist',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_create_fleet(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'CreateFleet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'CreateFleet')
    )

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='CreateFleet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.create_fleet(
                create_fleet_details=request.pop(util.camelize('CreateFleetDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'CreateFleet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_fleet',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_delete_blocklist(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'DeleteBlocklist'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'DeleteBlocklist')
    )

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='DeleteBlocklist')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.delete_blocklist(
                fleet_id=request.pop(util.camelize('fleetId')),
                blocklist_key=request.pop(util.camelize('blocklistKey')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'DeleteBlocklist',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_blocklist',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_delete_crypto_analysis_result(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'DeleteCryptoAnalysisResult'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'DeleteCryptoAnalysisResult')
    )

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='DeleteCryptoAnalysisResult')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.delete_crypto_analysis_result(
                fleet_id=request.pop(util.camelize('fleetId')),
                crypto_analysis_result_id=request.pop(util.camelize('cryptoAnalysisResultId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'DeleteCryptoAnalysisResult',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_crypto_analysis_result',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_delete_fleet(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'DeleteFleet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'DeleteFleet')
    )

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='DeleteFleet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.delete_fleet(
                fleet_id=request.pop(util.camelize('fleetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'DeleteFleet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_fleet',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_generate_agent_deploy_script(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'GenerateAgentDeployScript'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'GenerateAgentDeployScript')
    )

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='GenerateAgentDeployScript')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.generate_agent_deploy_script(
                fleet_id=request.pop(util.camelize('fleetId')),
                generate_agent_deploy_script_details=request.pop(util.camelize('GenerateAgentDeployScriptDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'GenerateAgentDeployScript',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_get_crypto_analysis_result(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'GetCryptoAnalysisResult'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'GetCryptoAnalysisResult')
    )

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='GetCryptoAnalysisResult')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.get_crypto_analysis_result(
                fleet_id=request.pop(util.camelize('fleetId')),
                crypto_analysis_result_id=request.pop(util.camelize('cryptoAnalysisResultId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'GetCryptoAnalysisResult',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cryptoAnalysisResult',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_get_fleet(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'GetFleet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'GetFleet')
    )

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='GetFleet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.get_fleet(
                fleet_id=request.pop(util.camelize('fleetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'GetFleet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fleet',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_get_fleet_advanced_feature_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'GetFleetAdvancedFeatureConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'GetFleetAdvancedFeatureConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='GetFleetAdvancedFeatureConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.get_fleet_advanced_feature_configuration(
                fleet_id=request.pop(util.camelize('fleetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'GetFleetAdvancedFeatureConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fleetAdvancedFeatureConfiguration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_get_fleet_agent_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'GetFleetAgentConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'GetFleetAgentConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='GetFleetAgentConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.get_fleet_agent_configuration(
                fleet_id=request.pop(util.camelize('fleetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'GetFleetAgentConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fleetAgentConfiguration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_get_java_family(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'GetJavaFamily'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'GetJavaFamily')
    )

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='GetJavaFamily')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.get_java_family(
                family_version=request.pop(util.camelize('familyVersion')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'GetJavaFamily',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'javaFamily',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_get_java_release(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'GetJavaRelease'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'GetJavaRelease')
    )

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='GetJavaRelease')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.get_java_release(
                release_version=request.pop(util.camelize('releaseVersion')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'GetJavaRelease',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'javaRelease',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_list_blocklists(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'ListBlocklists'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'ListBlocklists')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='ListBlocklists')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.list_blocklists(
                fleet_id=request.pop(util.camelize('fleetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_blocklists(
                    fleet_id=request.pop(util.camelize('fleetId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_blocklists(
                        fleet_id=request.pop(util.camelize('fleetId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'ListBlocklists',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'blocklistCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_list_crypto_analysis_results(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'ListCryptoAnalysisResults'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'ListCryptoAnalysisResults')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='ListCryptoAnalysisResults')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.list_crypto_analysis_results(
                fleet_id=request.pop(util.camelize('fleetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_crypto_analysis_results(
                    fleet_id=request.pop(util.camelize('fleetId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_crypto_analysis_results(
                        fleet_id=request.pop(util.camelize('fleetId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'ListCryptoAnalysisResults',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cryptoAnalysisResultCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_list_fleets(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'ListFleets'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'ListFleets')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='ListFleets')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.list_fleets(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_fleets(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_fleets(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'ListFleets',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fleetCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_list_installation_sites(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'ListInstallationSites'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'ListInstallationSites')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='ListInstallationSites')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.list_installation_sites(
                fleet_id=request.pop(util.camelize('fleetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_installation_sites(
                    fleet_id=request.pop(util.camelize('fleetId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_installation_sites(
                        fleet_id=request.pop(util.camelize('fleetId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'ListInstallationSites',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'installationSiteCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_list_java_families(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'ListJavaFamilies'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'ListJavaFamilies')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='ListJavaFamilies')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.list_java_families(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_java_families(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_java_families(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'ListJavaFamilies',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'javaFamilyCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_list_java_releases(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'ListJavaReleases'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'ListJavaReleases')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='ListJavaReleases')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.list_java_releases(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_java_releases(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_java_releases(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'ListJavaReleases',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'javaReleaseCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_list_jre_usage(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'ListJreUsage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'ListJreUsage')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='ListJreUsage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.list_jre_usage(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_jre_usage(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_jre_usage(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'ListJreUsage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'jreUsageCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_list_work_items(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'ListWorkItems'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'ListWorkItems')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='ListWorkItems')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.list_work_items(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_items(
                    work_request_id=request.pop(util.camelize('workRequestId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_items(
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'ListWorkItems',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workItemCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
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
            'jms',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestErrorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
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
            'jms',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.list_work_requests(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_requests(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_requests(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_remove_fleet_installation_sites(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'RemoveFleetInstallationSites'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'RemoveFleetInstallationSites')
    )

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='RemoveFleetInstallationSites')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.remove_fleet_installation_sites(
                fleet_id=request.pop(util.camelize('fleetId')),
                remove_fleet_installation_sites_details=request.pop(util.camelize('RemoveFleetInstallationSitesDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'RemoveFleetInstallationSites',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'remove_fleet_installation_sites',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_request_crypto_analyses(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'RequestCryptoAnalyses'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'RequestCryptoAnalyses')
    )

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='RequestCryptoAnalyses')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.request_crypto_analyses(
                fleet_id=request.pop(util.camelize('fleetId')),
                request_crypto_analyses_details=request.pop(util.camelize('RequestCryptoAnalysesDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'RequestCryptoAnalyses',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'request_crypto_analyses',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_request_jfr_recordings(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'RequestJfrRecordings'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'RequestJfrRecordings')
    )

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='RequestJfrRecordings')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.request_jfr_recordings(
                fleet_id=request.pop(util.camelize('fleetId')),
                request_jfr_recordings_details=request.pop(util.camelize('RequestJfrRecordingsDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'RequestJfrRecordings',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'request_jfr_recordings',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_scan_java_server_usage(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'ScanJavaServerUsage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'ScanJavaServerUsage')
    )

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='ScanJavaServerUsage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.scan_java_server_usage(
                fleet_id=request.pop(util.camelize('fleetId')),
                scan_java_server_usage_details=request.pop(util.camelize('ScanJavaServerUsageDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'ScanJavaServerUsage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'scan_java_server_usage',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_scan_library_usage(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'ScanLibraryUsage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'ScanLibraryUsage')
    )

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='ScanLibraryUsage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.scan_library_usage(
                fleet_id=request.pop(util.camelize('fleetId')),
                scan_library_usage_details=request.pop(util.camelize('ScanLibraryUsageDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'ScanLibraryUsage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'scan_library_usage',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_summarize_application_usage(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'SummarizeApplicationUsage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'SummarizeApplicationUsage')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='SummarizeApplicationUsage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.summarize_application_usage(
                fleet_id=request.pop(util.camelize('fleetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_application_usage(
                    fleet_id=request.pop(util.camelize('fleetId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_application_usage(
                        fleet_id=request.pop(util.camelize('fleetId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'SummarizeApplicationUsage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'applicationUsageCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_summarize_deployed_application_usage(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'SummarizeDeployedApplicationUsage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'SummarizeDeployedApplicationUsage')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='SummarizeDeployedApplicationUsage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.summarize_deployed_application_usage(
                fleet_id=request.pop(util.camelize('fleetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_deployed_application_usage(
                    fleet_id=request.pop(util.camelize('fleetId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_deployed_application_usage(
                        fleet_id=request.pop(util.camelize('fleetId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'SummarizeDeployedApplicationUsage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deployedApplicationUsageCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_summarize_installation_usage(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'SummarizeInstallationUsage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'SummarizeInstallationUsage')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='SummarizeInstallationUsage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.summarize_installation_usage(
                fleet_id=request.pop(util.camelize('fleetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_installation_usage(
                    fleet_id=request.pop(util.camelize('fleetId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_installation_usage(
                        fleet_id=request.pop(util.camelize('fleetId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'SummarizeInstallationUsage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'installationUsageCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_summarize_java_server_instance_usage(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'SummarizeJavaServerInstanceUsage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'SummarizeJavaServerInstanceUsage')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='SummarizeJavaServerInstanceUsage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.summarize_java_server_instance_usage(
                fleet_id=request.pop(util.camelize('fleetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_java_server_instance_usage(
                    fleet_id=request.pop(util.camelize('fleetId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_java_server_instance_usage(
                        fleet_id=request.pop(util.camelize('fleetId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'SummarizeJavaServerInstanceUsage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'javaServerInstanceUsageCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_summarize_java_server_usage(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'SummarizeJavaServerUsage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'SummarizeJavaServerUsage')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='SummarizeJavaServerUsage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.summarize_java_server_usage(
                fleet_id=request.pop(util.camelize('fleetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_java_server_usage(
                    fleet_id=request.pop(util.camelize('fleetId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_java_server_usage(
                        fleet_id=request.pop(util.camelize('fleetId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'SummarizeJavaServerUsage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'javaServerUsageCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_summarize_jre_usage(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'SummarizeJreUsage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'SummarizeJreUsage')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='SummarizeJreUsage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.summarize_jre_usage(
                fleet_id=request.pop(util.camelize('fleetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_jre_usage(
                    fleet_id=request.pop(util.camelize('fleetId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_jre_usage(
                        fleet_id=request.pop(util.camelize('fleetId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'SummarizeJreUsage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'jreUsageCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_summarize_library_usage(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'SummarizeLibraryUsage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'SummarizeLibraryUsage')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='SummarizeLibraryUsage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.summarize_library_usage(
                fleet_id=request.pop(util.camelize('fleetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_library_usage(
                    fleet_id=request.pop(util.camelize('fleetId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_library_usage(
                        fleet_id=request.pop(util.camelize('fleetId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'SummarizeLibraryUsage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'libraryUsageCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_summarize_managed_instance_usage(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'SummarizeManagedInstanceUsage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'SummarizeManagedInstanceUsage')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='SummarizeManagedInstanceUsage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.summarize_managed_instance_usage(
                fleet_id=request.pop(util.camelize('fleetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_managed_instance_usage(
                    fleet_id=request.pop(util.camelize('fleetId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_managed_instance_usage(
                        fleet_id=request.pop(util.camelize('fleetId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'SummarizeManagedInstanceUsage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managedInstanceUsageCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_summarize_resource_inventory(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'SummarizeResourceInventory'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'SummarizeResourceInventory')
    )

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='SummarizeResourceInventory')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.summarize_resource_inventory(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'SummarizeResourceInventory',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'resourceInventory',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_update_fleet(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'UpdateFleet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'UpdateFleet')
    )

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='UpdateFleet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.update_fleet(
                fleet_id=request.pop(util.camelize('fleetId')),
                update_fleet_details=request.pop(util.camelize('UpdateFleetDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'UpdateFleet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_fleet',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_update_fleet_advanced_feature_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'UpdateFleetAdvancedFeatureConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'UpdateFleetAdvancedFeatureConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='UpdateFleetAdvancedFeatureConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.update_fleet_advanced_feature_configuration(
                fleet_id=request.pop(util.camelize('fleetId')),
                update_fleet_advanced_feature_configuration_details=request.pop(util.camelize('UpdateFleetAdvancedFeatureConfigurationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'UpdateFleetAdvancedFeatureConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fleetAdvancedFeatureConfiguration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="autonomous_java-dev_us_grp@oracle.com" jiraProject="AJ" opsJiraProject="AJ"
def test_update_fleet_agent_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('jms', 'UpdateFleetAgentConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('jms', util.camelize('java_management_service'), 'UpdateFleetAgentConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='jms', api_name='UpdateFleetAgentConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.jms.JavaManagementServiceClient(config, service_endpoint=service_endpoint)
            response = client.update_fleet_agent_configuration(
                fleet_id=request.pop(util.camelize('fleetId')),
                update_fleet_agent_configuration_details=request.pop(util.camelize('UpdateFleetAgentConfigurationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'jms',
            'UpdateFleetAgentConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_fleet_agent_configuration',
            False,
            False
        )
