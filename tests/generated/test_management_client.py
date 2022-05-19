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

        cassette_location = os.path.join('generated', 'oda_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_configure_digital_assistant_parameters(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'ConfigureDigitalAssistantParameters'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'ConfigureDigitalAssistantParameters')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='ConfigureDigitalAssistantParameters')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.configure_digital_assistant_parameters(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                configure_digital_assistant_parameters_details=request.pop(util.camelize('ConfigureDigitalAssistantParametersDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'ConfigureDigitalAssistantParameters',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'configure_digital_assistant_parameters',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_create_authentication_provider(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'CreateAuthenticationProvider'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'CreateAuthenticationProvider')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='CreateAuthenticationProvider')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_authentication_provider(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                create_authentication_provider_details=request.pop(util.camelize('CreateAuthenticationProviderDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'CreateAuthenticationProvider',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'authenticationProvider',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_create_channel(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'CreateChannel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'CreateChannel')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='CreateChannel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_channel(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                create_channel_details=request.pop(util.camelize('CreateChannelDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'CreateChannel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'createChannelResult',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_create_digital_assistant(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'CreateDigitalAssistant'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'CreateDigitalAssistant')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='CreateDigitalAssistant')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_digital_assistant(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                create_digital_assistant_details=request.pop(util.camelize('CreateDigitalAssistantDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'CreateDigitalAssistant',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_digital_assistant',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_create_skill(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'CreateSkill'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'CreateSkill')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='CreateSkill')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_skill(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                create_skill_details=request.pop(util.camelize('CreateSkillDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'CreateSkill',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_skill',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_create_skill_parameter(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'CreateSkillParameter'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'CreateSkillParameter')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='CreateSkillParameter')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_skill_parameter(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                skill_id=request.pop(util.camelize('skillId')),
                create_skill_parameter_details=request.pop(util.camelize('CreateSkillParameterDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'CreateSkillParameter',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'skillParameter',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_create_translator(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'CreateTranslator'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'CreateTranslator')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='CreateTranslator')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_translator(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                create_translator_details=request.pop(util.camelize('CreateTranslatorDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'CreateTranslator',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'translator',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_delete_authentication_provider(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'DeleteAuthenticationProvider'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'DeleteAuthenticationProvider')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='DeleteAuthenticationProvider')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.delete_authentication_provider(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                authentication_provider_id=request.pop(util.camelize('authenticationProviderId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'DeleteAuthenticationProvider',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_authentication_provider',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_delete_channel(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'DeleteChannel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'DeleteChannel')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='DeleteChannel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.delete_channel(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                channel_id=request.pop(util.camelize('channelId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'DeleteChannel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_channel',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_delete_digital_assistant(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'DeleteDigitalAssistant'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'DeleteDigitalAssistant')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='DeleteDigitalAssistant')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.delete_digital_assistant(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                digital_assistant_id=request.pop(util.camelize('digitalAssistantId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'DeleteDigitalAssistant',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_digital_assistant',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_delete_skill(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'DeleteSkill'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'DeleteSkill')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='DeleteSkill')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.delete_skill(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                skill_id=request.pop(util.camelize('skillId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'DeleteSkill',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_skill',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_delete_skill_parameter(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'DeleteSkillParameter'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'DeleteSkillParameter')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='DeleteSkillParameter')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.delete_skill_parameter(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                skill_id=request.pop(util.camelize('skillId')),
                parameter_name=request.pop(util.camelize('parameterName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'DeleteSkillParameter',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_skill_parameter',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_delete_translator(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'DeleteTranslator'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'DeleteTranslator')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='DeleteTranslator')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.delete_translator(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                translator_id=request.pop(util.camelize('translatorId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'DeleteTranslator',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_translator',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_export_digital_assistant(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'ExportDigitalAssistant'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'ExportDigitalAssistant')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='ExportDigitalAssistant')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.export_digital_assistant(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                digital_assistant_id=request.pop(util.camelize('digitalAssistantId')),
                export_digital_assistant_details=request.pop(util.camelize('ExportDigitalAssistantDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'ExportDigitalAssistant',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'export_digital_assistant',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_export_skill(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'ExportSkill'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'ExportSkill')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='ExportSkill')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.export_skill(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                skill_id=request.pop(util.camelize('skillId')),
                export_skill_details=request.pop(util.camelize('ExportSkillDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'ExportSkill',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'export_skill',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_get_authentication_provider(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'GetAuthenticationProvider'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'GetAuthenticationProvider')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='GetAuthenticationProvider')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_authentication_provider(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                authentication_provider_id=request.pop(util.camelize('authenticationProviderId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'GetAuthenticationProvider',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'authenticationProvider',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_get_channel(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'GetChannel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'GetChannel')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='GetChannel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_channel(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                channel_id=request.pop(util.camelize('channelId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'GetChannel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'channel',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_get_digital_assistant(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'GetDigitalAssistant'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'GetDigitalAssistant')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='GetDigitalAssistant')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_digital_assistant(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                digital_assistant_id=request.pop(util.camelize('digitalAssistantId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'GetDigitalAssistant',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'digitalAssistant',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_get_digital_assistant_parameter(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'GetDigitalAssistantParameter'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'GetDigitalAssistantParameter')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='GetDigitalAssistantParameter')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_digital_assistant_parameter(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                digital_assistant_id=request.pop(util.camelize('digitalAssistantId')),
                parameter_name=request.pop(util.camelize('parameterName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'GetDigitalAssistantParameter',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'digitalAssistantParameter',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_get_skill(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'GetSkill'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'GetSkill')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='GetSkill')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_skill(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                skill_id=request.pop(util.camelize('skillId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'GetSkill',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'skill',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_get_skill_parameter(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'GetSkillParameter'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'GetSkillParameter')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='GetSkillParameter')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_skill_parameter(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                skill_id=request.pop(util.camelize('skillId')),
                parameter_name=request.pop(util.camelize('parameterName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'GetSkillParameter',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'skillParameter',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_get_translator(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'GetTranslator'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'GetTranslator')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='GetTranslator')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_translator(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                translator_id=request.pop(util.camelize('translatorId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'GetTranslator',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'translator',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_import_bot(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'ImportBot'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'ImportBot')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='ImportBot')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.import_bot(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                import_bot_details=request.pop(util.camelize('ImportBotDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'ImportBot',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'import_bot',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_list_authentication_providers(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'ListAuthenticationProviders'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'ListAuthenticationProviders')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='ListAuthenticationProviders')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_authentication_providers(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_authentication_providers(
                    oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_authentication_providers(
                        oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'ListAuthenticationProviders',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'authenticationProviderCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_list_channels(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'ListChannels'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'ListChannels')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='ListChannels')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_channels(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_channels(
                    oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_channels(
                        oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'ListChannels',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'channelCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_list_digital_assistant_parameters(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'ListDigitalAssistantParameters'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'ListDigitalAssistantParameters')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='ListDigitalAssistantParameters')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_digital_assistant_parameters(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                digital_assistant_id=request.pop(util.camelize('digitalAssistantId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_digital_assistant_parameters(
                    oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                    digital_assistant_id=request.pop(util.camelize('digitalAssistantId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_digital_assistant_parameters(
                        oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                        digital_assistant_id=request.pop(util.camelize('digitalAssistantId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'ListDigitalAssistantParameters',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'digitalAssistantParameterCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_list_digital_assistants(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'ListDigitalAssistants'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'ListDigitalAssistants')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='ListDigitalAssistants')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_digital_assistants(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_digital_assistants(
                    oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_digital_assistants(
                        oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'ListDigitalAssistants',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'digitalAssistantCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_list_skill_parameters(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'ListSkillParameters'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'ListSkillParameters')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='ListSkillParameters')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_skill_parameters(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                skill_id=request.pop(util.camelize('skillId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_skill_parameters(
                    oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                    skill_id=request.pop(util.camelize('skillId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_skill_parameters(
                        oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                        skill_id=request.pop(util.camelize('skillId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'ListSkillParameters',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'skillParameterCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_list_skills(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'ListSkills'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'ListSkills')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='ListSkills')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_skills(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_skills(
                    oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_skills(
                        oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'ListSkills',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'skillCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_list_translators(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'ListTranslators'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'ListTranslators')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='ListTranslators')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_translators(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_translators(
                    oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_translators(
                        oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'ListTranslators',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'translatorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_publish_digital_assistant(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'PublishDigitalAssistant'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'PublishDigitalAssistant')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='PublishDigitalAssistant')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.publish_digital_assistant(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                digital_assistant_id=request.pop(util.camelize('digitalAssistantId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'PublishDigitalAssistant',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'digitalAssistant',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_publish_skill(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'PublishSkill'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'PublishSkill')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='PublishSkill')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.publish_skill(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                skill_id=request.pop(util.camelize('skillId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'PublishSkill',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'skill',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_rotate_channel_keys(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'RotateChannelKeys'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'RotateChannelKeys')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='RotateChannelKeys')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.rotate_channel_keys(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                channel_id=request.pop(util.camelize('channelId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'RotateChannelKeys',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'createChannelResult',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_start_channel(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'StartChannel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'StartChannel')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='StartChannel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.start_channel(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                channel_id=request.pop(util.camelize('channelId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'StartChannel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'channel',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_stop_channel(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'StopChannel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'StopChannel')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='StopChannel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.stop_channel(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                channel_id=request.pop(util.camelize('channelId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'StopChannel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'channel',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_update_authentication_provider(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'UpdateAuthenticationProvider'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'UpdateAuthenticationProvider')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='UpdateAuthenticationProvider')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_authentication_provider(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                authentication_provider_id=request.pop(util.camelize('authenticationProviderId')),
                update_authentication_provider_details=request.pop(util.camelize('UpdateAuthenticationProviderDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'UpdateAuthenticationProvider',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'authenticationProvider',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_update_channel(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'UpdateChannel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'UpdateChannel')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='UpdateChannel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_channel(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                channel_id=request.pop(util.camelize('channelId')),
                update_channel_details=request.pop(util.camelize('UpdateChannelDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'UpdateChannel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'channel',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_update_digital_assistant(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'UpdateDigitalAssistant'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'UpdateDigitalAssistant')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='UpdateDigitalAssistant')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_digital_assistant(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                digital_assistant_id=request.pop(util.camelize('digitalAssistantId')),
                update_digital_assistant_details=request.pop(util.camelize('UpdateDigitalAssistantDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'UpdateDigitalAssistant',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'digitalAssistant',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_update_digital_assistant_parameter(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'UpdateDigitalAssistantParameter'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'UpdateDigitalAssistantParameter')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='UpdateDigitalAssistantParameter')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_digital_assistant_parameter(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                digital_assistant_id=request.pop(util.camelize('digitalAssistantId')),
                parameter_name=request.pop(util.camelize('parameterName')),
                update_digital_assistant_parameter_details=request.pop(util.camelize('UpdateDigitalAssistantParameterDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'UpdateDigitalAssistantParameter',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'digitalAssistantParameter',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_update_skill(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'UpdateSkill'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'UpdateSkill')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='UpdateSkill')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_skill(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                skill_id=request.pop(util.camelize('skillId')),
                update_skill_details=request.pop(util.camelize('UpdateSkillDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'UpdateSkill',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'skill',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_update_skill_parameter(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'UpdateSkillParameter'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'UpdateSkillParameter')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='UpdateSkillParameter')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_skill_parameter(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                skill_id=request.pop(util.camelize('skillId')),
                parameter_name=request.pop(util.camelize('parameterName')),
                update_skill_parameter_details=request.pop(util.camelize('UpdateSkillParameterDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'UpdateSkillParameter',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'skillParameter',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_update_translator(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'UpdateTranslator'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('management'), 'UpdateTranslator')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='UpdateTranslator')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.ManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_translator(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                translator_id=request.pop(util.camelize('translatorId')),
                update_translator_details=request.pop(util.camelize('UpdateTranslatorDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'UpdateTranslator',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'translator',
            False,
            False
        )
