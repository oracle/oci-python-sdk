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

        cassette_location = os.path.join('generated', 'media_services_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_change_media_asset_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'ChangeMediaAssetCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'ChangeMediaAssetCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='ChangeMediaAssetCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.change_media_asset_compartment(
                media_asset_id=request.pop(util.camelize('mediaAssetId')),
                change_media_asset_compartment_details=request.pop(util.camelize('ChangeMediaAssetCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'ChangeMediaAssetCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_media_asset_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_change_media_workflow_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'ChangeMediaWorkflowCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'ChangeMediaWorkflowCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='ChangeMediaWorkflowCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.change_media_workflow_compartment(
                media_workflow_id=request.pop(util.camelize('mediaWorkflowId')),
                change_media_workflow_compartment_details=request.pop(util.camelize('ChangeMediaWorkflowCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'ChangeMediaWorkflowCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_media_workflow_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_change_media_workflow_configuration_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'ChangeMediaWorkflowConfigurationCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'ChangeMediaWorkflowConfigurationCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='ChangeMediaWorkflowConfigurationCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.change_media_workflow_configuration_compartment(
                media_workflow_configuration_id=request.pop(util.camelize('mediaWorkflowConfigurationId')),
                change_media_workflow_configuration_compartment_details=request.pop(util.camelize('ChangeMediaWorkflowConfigurationCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'ChangeMediaWorkflowConfigurationCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_media_workflow_configuration_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_change_media_workflow_job_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'ChangeMediaWorkflowJobCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'ChangeMediaWorkflowJobCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='ChangeMediaWorkflowJobCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.change_media_workflow_job_compartment(
                media_workflow_job_id=request.pop(util.camelize('mediaWorkflowJobId')),
                change_media_workflow_job_compartment_details=request.pop(util.camelize('ChangeMediaWorkflowJobCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'ChangeMediaWorkflowJobCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_media_workflow_job_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_change_stream_distribution_channel_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'ChangeStreamDistributionChannelCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'ChangeStreamDistributionChannelCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='ChangeStreamDistributionChannelCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.change_stream_distribution_channel_compartment(
                stream_distribution_channel_id=request.pop(util.camelize('streamDistributionChannelId')),
                change_stream_distribution_channel_compartment_details=request.pop(util.camelize('ChangeStreamDistributionChannelCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'ChangeStreamDistributionChannelCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_stream_distribution_channel_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_create_media_asset(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'CreateMediaAsset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'CreateMediaAsset')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='CreateMediaAsset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.create_media_asset(
                create_media_asset_details=request.pop(util.camelize('CreateMediaAssetDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'CreateMediaAsset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mediaAsset',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_create_media_workflow(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'CreateMediaWorkflow'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'CreateMediaWorkflow')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='CreateMediaWorkflow')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.create_media_workflow(
                create_media_workflow_details=request.pop(util.camelize('CreateMediaWorkflowDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'CreateMediaWorkflow',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mediaWorkflow',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_create_media_workflow_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'CreateMediaWorkflowConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'CreateMediaWorkflowConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='CreateMediaWorkflowConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.create_media_workflow_configuration(
                create_media_workflow_configuration_details=request.pop(util.camelize('CreateMediaWorkflowConfigurationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'CreateMediaWorkflowConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mediaWorkflowConfiguration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_create_media_workflow_job(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'CreateMediaWorkflowJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'CreateMediaWorkflowJob')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='CreateMediaWorkflowJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.create_media_workflow_job(
                create_media_workflow_job_details=request.pop(util.camelize('CreateMediaWorkflowJobDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'CreateMediaWorkflowJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mediaWorkflowJob',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_create_stream_cdn_config(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'CreateStreamCdnConfig'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'CreateStreamCdnConfig')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='CreateStreamCdnConfig')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.create_stream_cdn_config(
                create_stream_cdn_config_details=request.pop(util.camelize('CreateStreamCdnConfigDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'CreateStreamCdnConfig',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'streamCdnConfig',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_create_stream_distribution_channel(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'CreateStreamDistributionChannel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'CreateStreamDistributionChannel')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='CreateStreamDistributionChannel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.create_stream_distribution_channel(
                create_stream_distribution_channel_details=request.pop(util.camelize('CreateStreamDistributionChannelDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'CreateStreamDistributionChannel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'streamDistributionChannel',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_create_stream_packaging_config(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'CreateStreamPackagingConfig'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'CreateStreamPackagingConfig')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='CreateStreamPackagingConfig')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.create_stream_packaging_config(
                create_stream_packaging_config_details=request.pop(util.camelize('CreateStreamPackagingConfigDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'CreateStreamPackagingConfig',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'streamPackagingConfig',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_delete_media_asset(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'DeleteMediaAsset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'DeleteMediaAsset')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='DeleteMediaAsset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.delete_media_asset(
                media_asset_id=request.pop(util.camelize('mediaAssetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'DeleteMediaAsset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_media_asset',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_delete_media_asset_distribution_channel_attachment(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'DeleteMediaAssetDistributionChannelAttachment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'DeleteMediaAssetDistributionChannelAttachment')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='DeleteMediaAssetDistributionChannelAttachment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.delete_media_asset_distribution_channel_attachment(
                media_asset_id=request.pop(util.camelize('mediaAssetId')),
                distribution_channel_id=request.pop(util.camelize('distributionChannelId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'DeleteMediaAssetDistributionChannelAttachment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_media_asset_distribution_channel_attachment',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_delete_media_workflow(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'DeleteMediaWorkflow'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'DeleteMediaWorkflow')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='DeleteMediaWorkflow')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.delete_media_workflow(
                media_workflow_id=request.pop(util.camelize('mediaWorkflowId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'DeleteMediaWorkflow',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_media_workflow',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_delete_media_workflow_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'DeleteMediaWorkflowConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'DeleteMediaWorkflowConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='DeleteMediaWorkflowConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.delete_media_workflow_configuration(
                media_workflow_configuration_id=request.pop(util.camelize('mediaWorkflowConfigurationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'DeleteMediaWorkflowConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_media_workflow_configuration',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_delete_media_workflow_job(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'DeleteMediaWorkflowJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'DeleteMediaWorkflowJob')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='DeleteMediaWorkflowJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.delete_media_workflow_job(
                media_workflow_job_id=request.pop(util.camelize('mediaWorkflowJobId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'DeleteMediaWorkflowJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_media_workflow_job',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_delete_stream_cdn_config(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'DeleteStreamCdnConfig'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'DeleteStreamCdnConfig')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='DeleteStreamCdnConfig')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.delete_stream_cdn_config(
                stream_cdn_config_id=request.pop(util.camelize('streamCdnConfigId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'DeleteStreamCdnConfig',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_stream_cdn_config',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_delete_stream_distribution_channel(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'DeleteStreamDistributionChannel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'DeleteStreamDistributionChannel')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='DeleteStreamDistributionChannel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.delete_stream_distribution_channel(
                stream_distribution_channel_id=request.pop(util.camelize('streamDistributionChannelId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'DeleteStreamDistributionChannel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_stream_distribution_channel',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_delete_stream_packaging_config(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'DeleteStreamPackagingConfig'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'DeleteStreamPackagingConfig')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='DeleteStreamPackagingConfig')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.delete_stream_packaging_config(
                stream_packaging_config_id=request.pop(util.camelize('streamPackagingConfigId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'DeleteStreamPackagingConfig',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_stream_packaging_config',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_get_media_asset(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'GetMediaAsset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'GetMediaAsset')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='GetMediaAsset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.get_media_asset(
                media_asset_id=request.pop(util.camelize('mediaAssetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'GetMediaAsset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mediaAsset',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_get_media_asset_distribution_channel_attachment(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'GetMediaAssetDistributionChannelAttachment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'GetMediaAssetDistributionChannelAttachment')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='GetMediaAssetDistributionChannelAttachment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.get_media_asset_distribution_channel_attachment(
                media_asset_id=request.pop(util.camelize('mediaAssetId')),
                distribution_channel_id=request.pop(util.camelize('distributionChannelId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'GetMediaAssetDistributionChannelAttachment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mediaAssetDistributionChannelAttachment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_get_media_workflow(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'GetMediaWorkflow'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'GetMediaWorkflow')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='GetMediaWorkflow')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.get_media_workflow(
                media_workflow_id=request.pop(util.camelize('mediaWorkflowId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'GetMediaWorkflow',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mediaWorkflow',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_get_media_workflow_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'GetMediaWorkflowConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'GetMediaWorkflowConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='GetMediaWorkflowConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.get_media_workflow_configuration(
                media_workflow_configuration_id=request.pop(util.camelize('mediaWorkflowConfigurationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'GetMediaWorkflowConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mediaWorkflowConfiguration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_get_media_workflow_job(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'GetMediaWorkflowJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'GetMediaWorkflowJob')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='GetMediaWorkflowJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.get_media_workflow_job(
                media_workflow_job_id=request.pop(util.camelize('mediaWorkflowJobId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'GetMediaWorkflowJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mediaWorkflowJob',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_get_media_workflow_job_fact(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'GetMediaWorkflowJobFact'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'GetMediaWorkflowJobFact')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='GetMediaWorkflowJobFact')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.get_media_workflow_job_fact(
                media_workflow_job_id=request.pop(util.camelize('mediaWorkflowJobId')),
                key=request.pop(util.camelize('key')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'GetMediaWorkflowJobFact',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mediaWorkflowJobFact',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_get_stream_cdn_config(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'GetStreamCdnConfig'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'GetStreamCdnConfig')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='GetStreamCdnConfig')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.get_stream_cdn_config(
                stream_cdn_config_id=request.pop(util.camelize('streamCdnConfigId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'GetStreamCdnConfig',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'streamCdnConfig',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_get_stream_distribution_channel(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'GetStreamDistributionChannel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'GetStreamDistributionChannel')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='GetStreamDistributionChannel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.get_stream_distribution_channel(
                stream_distribution_channel_id=request.pop(util.camelize('streamDistributionChannelId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'GetStreamDistributionChannel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'streamDistributionChannel',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_get_stream_packaging_config(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'GetStreamPackagingConfig'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'GetStreamPackagingConfig')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='GetStreamPackagingConfig')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.get_stream_packaging_config(
                stream_packaging_config_id=request.pop(util.camelize('streamPackagingConfigId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'GetStreamPackagingConfig',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'streamPackagingConfig',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_ingest_stream_distribution_channel(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'IngestStreamDistributionChannel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'IngestStreamDistributionChannel')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='IngestStreamDistributionChannel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.ingest_stream_distribution_channel(
                stream_distribution_channel_id=request.pop(util.camelize('streamDistributionChannelId')),
                ingest_stream_distribution_channel_details=request.pop(util.camelize('IngestStreamDistributionChannelDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'IngestStreamDistributionChannel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'ingestStreamDistributionChannelResult',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_list_media_asset_distribution_channel_attachments(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'ListMediaAssetDistributionChannelAttachments'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'ListMediaAssetDistributionChannelAttachments')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='ListMediaAssetDistributionChannelAttachments')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.list_media_asset_distribution_channel_attachments(
                media_asset_id=request.pop(util.camelize('mediaAssetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_media_asset_distribution_channel_attachments(
                    media_asset_id=request.pop(util.camelize('mediaAssetId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_media_asset_distribution_channel_attachments(
                        media_asset_id=request.pop(util.camelize('mediaAssetId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'ListMediaAssetDistributionChannelAttachments',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mediaAssetDistributionChannelAttachmentCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_list_media_assets(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'ListMediaAssets'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'ListMediaAssets')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='ListMediaAssets')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.list_media_assets(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_media_assets(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_media_assets(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'ListMediaAssets',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mediaAssetCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_list_media_workflow_configurations(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'ListMediaWorkflowConfigurations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'ListMediaWorkflowConfigurations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='ListMediaWorkflowConfigurations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.list_media_workflow_configurations(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_media_workflow_configurations(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_media_workflow_configurations(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'ListMediaWorkflowConfigurations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mediaWorkflowConfigurationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_list_media_workflow_job_facts(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'ListMediaWorkflowJobFacts'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'ListMediaWorkflowJobFacts')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='ListMediaWorkflowJobFacts')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.list_media_workflow_job_facts(
                media_workflow_job_id=request.pop(util.camelize('mediaWorkflowJobId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_media_workflow_job_facts(
                    media_workflow_job_id=request.pop(util.camelize('mediaWorkflowJobId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_media_workflow_job_facts(
                        media_workflow_job_id=request.pop(util.camelize('mediaWorkflowJobId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'ListMediaWorkflowJobFacts',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mediaWorkflowJobFactCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_list_media_workflow_jobs(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'ListMediaWorkflowJobs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'ListMediaWorkflowJobs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='ListMediaWorkflowJobs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.list_media_workflow_jobs(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_media_workflow_jobs(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_media_workflow_jobs(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'ListMediaWorkflowJobs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mediaWorkflowJobCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_list_media_workflow_task_declarations(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'ListMediaWorkflowTaskDeclarations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'ListMediaWorkflowTaskDeclarations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='ListMediaWorkflowTaskDeclarations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.list_media_workflow_task_declarations(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_media_workflow_task_declarations(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_media_workflow_task_declarations(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'ListMediaWorkflowTaskDeclarations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mediaWorkflowTaskDeclarationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_list_media_workflows(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'ListMediaWorkflows'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'ListMediaWorkflows')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='ListMediaWorkflows')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.list_media_workflows(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_media_workflows(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_media_workflows(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'ListMediaWorkflows',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mediaWorkflowCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_list_stream_cdn_configs(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'ListStreamCdnConfigs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'ListStreamCdnConfigs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='ListStreamCdnConfigs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.list_stream_cdn_configs(
                distribution_channel_id=request.pop(util.camelize('distributionChannelId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_stream_cdn_configs(
                    distribution_channel_id=request.pop(util.camelize('distributionChannelId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_stream_cdn_configs(
                        distribution_channel_id=request.pop(util.camelize('distributionChannelId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'ListStreamCdnConfigs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'streamCdnConfigCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_list_stream_distribution_channels(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'ListStreamDistributionChannels'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'ListStreamDistributionChannels')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='ListStreamDistributionChannels')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.list_stream_distribution_channels(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_stream_distribution_channels(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_stream_distribution_channels(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'ListStreamDistributionChannels',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'streamDistributionChannelCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_list_stream_packaging_configs(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'ListStreamPackagingConfigs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'ListStreamPackagingConfigs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='ListStreamPackagingConfigs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.list_stream_packaging_configs(
                distribution_channel_id=request.pop(util.camelize('distributionChannelId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_stream_packaging_configs(
                    distribution_channel_id=request.pop(util.camelize('distributionChannelId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_stream_packaging_configs(
                        distribution_channel_id=request.pop(util.camelize('distributionChannelId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'ListStreamPackagingConfigs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'streamPackagingConfigCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_list_system_media_workflows(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'ListSystemMediaWorkflows'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'ListSystemMediaWorkflows')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='ListSystemMediaWorkflows')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.list_system_media_workflows(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_system_media_workflows(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_system_media_workflows(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'ListSystemMediaWorkflows',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'systemMediaWorkflowCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_update_media_asset(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'UpdateMediaAsset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'UpdateMediaAsset')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='UpdateMediaAsset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.update_media_asset(
                media_asset_id=request.pop(util.camelize('mediaAssetId')),
                update_media_asset_details=request.pop(util.camelize('UpdateMediaAssetDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'UpdateMediaAsset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mediaAsset',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_update_media_workflow(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'UpdateMediaWorkflow'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'UpdateMediaWorkflow')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='UpdateMediaWorkflow')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.update_media_workflow(
                media_workflow_id=request.pop(util.camelize('mediaWorkflowId')),
                update_media_workflow_details=request.pop(util.camelize('UpdateMediaWorkflowDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'UpdateMediaWorkflow',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mediaWorkflow',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_update_media_workflow_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'UpdateMediaWorkflowConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'UpdateMediaWorkflowConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='UpdateMediaWorkflowConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.update_media_workflow_configuration(
                media_workflow_configuration_id=request.pop(util.camelize('mediaWorkflowConfigurationId')),
                update_media_workflow_configuration_details=request.pop(util.camelize('UpdateMediaWorkflowConfigurationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'UpdateMediaWorkflowConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mediaWorkflowConfiguration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_update_media_workflow_job(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'UpdateMediaWorkflowJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'UpdateMediaWorkflowJob')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='UpdateMediaWorkflowJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.update_media_workflow_job(
                media_workflow_job_id=request.pop(util.camelize('mediaWorkflowJobId')),
                update_media_workflow_job_details=request.pop(util.camelize('UpdateMediaWorkflowJobDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'UpdateMediaWorkflowJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mediaWorkflowJob',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_update_stream_cdn_config(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'UpdateStreamCdnConfig'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'UpdateStreamCdnConfig')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='UpdateStreamCdnConfig')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.update_stream_cdn_config(
                stream_cdn_config_id=request.pop(util.camelize('streamCdnConfigId')),
                update_stream_cdn_config_details=request.pop(util.camelize('UpdateStreamCdnConfigDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'UpdateStreamCdnConfig',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'streamCdnConfig',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_update_stream_distribution_channel(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'UpdateStreamDistributionChannel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'UpdateStreamDistributionChannel')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='UpdateStreamDistributionChannel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.update_stream_distribution_channel(
                stream_distribution_channel_id=request.pop(util.camelize('streamDistributionChannelId')),
                update_stream_distribution_channel_details=request.pop(util.camelize('UpdateStreamDistributionChannelDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'UpdateStreamDistributionChannel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'streamDistributionChannel',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_dig_media_svc_us_grp@oracle.com" jiraProject="DMP" opsJiraProject="DMP"
def test_update_stream_packaging_config(testing_service_client):
    if not testing_service_client.is_api_enabled('media_services', 'UpdateStreamPackagingConfig'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('media_services', util.camelize('media_services'), 'UpdateStreamPackagingConfig')
    )

    request_containers = testing_service_client.get_requests(service_name='media_services', api_name='UpdateStreamPackagingConfig')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.media_services.MediaServicesClient(config, service_endpoint=service_endpoint)
            response = client.update_stream_packaging_config(
                stream_packaging_config_id=request.pop(util.camelize('streamPackagingConfigId')),
                update_stream_packaging_config_details=request.pop(util.camelize('UpdateStreamPackagingConfigDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'media_services',
            'UpdateStreamPackagingConfig',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'streamPackagingConfig',
            False,
            False
        )
