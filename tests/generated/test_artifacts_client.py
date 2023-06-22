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

        cassette_location = os.path.join('generated', 'artifacts_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="odx_registry_grp@oracle.com" jiraProject="OCIR" opsJiraProject="OCIR"
def test_change_container_repository_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('artifacts', 'ChangeContainerRepositoryCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('artifacts', util.camelize('artifacts'), 'ChangeContainerRepositoryCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='artifacts', api_name='ChangeContainerRepositoryCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.artifacts.ArtifactsClient(config, service_endpoint=service_endpoint)
            response = client.change_container_repository_compartment(
                repository_id=request.pop(util.camelize('repositoryId')),
                change_container_repository_compartment_details=request.pop(util.camelize('ChangeContainerRepositoryCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'artifacts',
            'ChangeContainerRepositoryCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_container_repository_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="odx_registry_grp@oracle.com" jiraProject="OCIR" opsJiraProject="OCIR"
def test_change_repository_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('artifacts', 'ChangeRepositoryCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('artifacts', util.camelize('artifacts'), 'ChangeRepositoryCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='artifacts', api_name='ChangeRepositoryCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.artifacts.ArtifactsClient(config, service_endpoint=service_endpoint)
            response = client.change_repository_compartment(
                repository_id=request.pop(util.camelize('repositoryId')),
                change_repository_compartment_details=request.pop(util.camelize('ChangeRepositoryCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'artifacts',
            'ChangeRepositoryCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_repository_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="odx_registry_grp@oracle.com" jiraProject="OCIR" opsJiraProject="OCIR"
def test_create_container_image_signature(testing_service_client):
    if not testing_service_client.is_api_enabled('artifacts', 'CreateContainerImageSignature'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('artifacts', util.camelize('artifacts'), 'CreateContainerImageSignature')
    )

    request_containers = testing_service_client.get_requests(service_name='artifacts', api_name='CreateContainerImageSignature')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.artifacts.ArtifactsClient(config, service_endpoint=service_endpoint)
            response = client.create_container_image_signature(
                create_container_image_signature_details=request.pop(util.camelize('CreateContainerImageSignatureDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'artifacts',
            'CreateContainerImageSignature',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'containerImageSignature',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="odx_registry_grp@oracle.com" jiraProject="OCIR" opsJiraProject="OCIR"
def test_create_container_repository(testing_service_client):
    if not testing_service_client.is_api_enabled('artifacts', 'CreateContainerRepository'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('artifacts', util.camelize('artifacts'), 'CreateContainerRepository')
    )

    request_containers = testing_service_client.get_requests(service_name='artifacts', api_name='CreateContainerRepository')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.artifacts.ArtifactsClient(config, service_endpoint=service_endpoint)
            response = client.create_container_repository(
                create_container_repository_details=request.pop(util.camelize('CreateContainerRepositoryDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'artifacts',
            'CreateContainerRepository',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'containerRepository',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="odx_registry_grp@oracle.com" jiraProject="OCIR" opsJiraProject="OCIR"
def test_create_repository(testing_service_client):
    if not testing_service_client.is_api_enabled('artifacts', 'CreateRepository'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('artifacts', util.camelize('artifacts'), 'CreateRepository')
    )

    request_containers = testing_service_client.get_requests(service_name='artifacts', api_name='CreateRepository')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.artifacts.ArtifactsClient(config, service_endpoint=service_endpoint)
            response = client.create_repository(
                create_repository_details=request.pop(util.camelize('CreateRepositoryDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'artifacts',
            'CreateRepository',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'repository',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="odx_registry_grp@oracle.com" jiraProject="OCIR" opsJiraProject="OCIR"
def test_delete_container_image(testing_service_client):
    if not testing_service_client.is_api_enabled('artifacts', 'DeleteContainerImage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('artifacts', util.camelize('artifacts'), 'DeleteContainerImage')
    )

    request_containers = testing_service_client.get_requests(service_name='artifacts', api_name='DeleteContainerImage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.artifacts.ArtifactsClient(config, service_endpoint=service_endpoint)
            response = client.delete_container_image(
                image_id=request.pop(util.camelize('imageId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'artifacts',
            'DeleteContainerImage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_container_image',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="odx_registry_grp@oracle.com" jiraProject="OCIR" opsJiraProject="OCIR"
def test_delete_container_image_signature(testing_service_client):
    if not testing_service_client.is_api_enabled('artifacts', 'DeleteContainerImageSignature'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('artifacts', util.camelize('artifacts'), 'DeleteContainerImageSignature')
    )

    request_containers = testing_service_client.get_requests(service_name='artifacts', api_name='DeleteContainerImageSignature')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.artifacts.ArtifactsClient(config, service_endpoint=service_endpoint)
            response = client.delete_container_image_signature(
                image_signature_id=request.pop(util.camelize('imageSignatureId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'artifacts',
            'DeleteContainerImageSignature',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_container_image_signature',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="odx_registry_grp@oracle.com" jiraProject="OCIR" opsJiraProject="OCIR"
def test_delete_container_repository(testing_service_client):
    if not testing_service_client.is_api_enabled('artifacts', 'DeleteContainerRepository'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('artifacts', util.camelize('artifacts'), 'DeleteContainerRepository')
    )

    request_containers = testing_service_client.get_requests(service_name='artifacts', api_name='DeleteContainerRepository')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.artifacts.ArtifactsClient(config, service_endpoint=service_endpoint)
            response = client.delete_container_repository(
                repository_id=request.pop(util.camelize('repositoryId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'artifacts',
            'DeleteContainerRepository',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_container_repository',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="odx_registry_grp@oracle.com" jiraProject="OCIR" opsJiraProject="OCIR"
def test_delete_generic_artifact(testing_service_client):
    if not testing_service_client.is_api_enabled('artifacts', 'DeleteGenericArtifact'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('artifacts', util.camelize('artifacts'), 'DeleteGenericArtifact')
    )

    request_containers = testing_service_client.get_requests(service_name='artifacts', api_name='DeleteGenericArtifact')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.artifacts.ArtifactsClient(config, service_endpoint=service_endpoint)
            response = client.delete_generic_artifact(
                artifact_id=request.pop(util.camelize('artifactId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'artifacts',
            'DeleteGenericArtifact',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_generic_artifact',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="odx_registry_grp@oracle.com" jiraProject="OCIR" opsJiraProject="OCIR"
def test_delete_generic_artifact_by_path(testing_service_client):
    if not testing_service_client.is_api_enabled('artifacts', 'DeleteGenericArtifactByPath'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('artifacts', util.camelize('artifacts'), 'DeleteGenericArtifactByPath')
    )

    request_containers = testing_service_client.get_requests(service_name='artifacts', api_name='DeleteGenericArtifactByPath')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.artifacts.ArtifactsClient(config, service_endpoint=service_endpoint)
            response = client.delete_generic_artifact_by_path(
                repository_id=request.pop(util.camelize('repositoryId')),
                artifact_path=request.pop(util.camelize('artifactPath')),
                version=request.pop(util.camelize('version')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'artifacts',
            'DeleteGenericArtifactByPath',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_generic_artifact_by_path',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="odx_registry_grp@oracle.com" jiraProject="OCIR" opsJiraProject="OCIR"
def test_delete_repository(testing_service_client):
    if not testing_service_client.is_api_enabled('artifacts', 'DeleteRepository'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('artifacts', util.camelize('artifacts'), 'DeleteRepository')
    )

    request_containers = testing_service_client.get_requests(service_name='artifacts', api_name='DeleteRepository')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.artifacts.ArtifactsClient(config, service_endpoint=service_endpoint)
            response = client.delete_repository(
                repository_id=request.pop(util.camelize('repositoryId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'artifacts',
            'DeleteRepository',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_repository',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="odx_registry_grp@oracle.com" jiraProject="OCIR" opsJiraProject="OCIR"
def test_get_container_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('artifacts', 'GetContainerConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('artifacts', util.camelize('artifacts'), 'GetContainerConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='artifacts', api_name='GetContainerConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.artifacts.ArtifactsClient(config, service_endpoint=service_endpoint)
            response = client.get_container_configuration(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'artifacts',
            'GetContainerConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'containerConfiguration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="odx_registry_grp@oracle.com" jiraProject="OCIR" opsJiraProject="OCIR"
def test_get_container_image(testing_service_client):
    if not testing_service_client.is_api_enabled('artifacts', 'GetContainerImage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('artifacts', util.camelize('artifacts'), 'GetContainerImage')
    )

    request_containers = testing_service_client.get_requests(service_name='artifacts', api_name='GetContainerImage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.artifacts.ArtifactsClient(config, service_endpoint=service_endpoint)
            response = client.get_container_image(
                image_id=request.pop(util.camelize('imageId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'artifacts',
            'GetContainerImage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'containerImage',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="odx_registry_grp@oracle.com" jiraProject="OCIR" opsJiraProject="OCIR"
def test_get_container_image_signature(testing_service_client):
    if not testing_service_client.is_api_enabled('artifacts', 'GetContainerImageSignature'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('artifacts', util.camelize('artifacts'), 'GetContainerImageSignature')
    )

    request_containers = testing_service_client.get_requests(service_name='artifacts', api_name='GetContainerImageSignature')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.artifacts.ArtifactsClient(config, service_endpoint=service_endpoint)
            response = client.get_container_image_signature(
                image_signature_id=request.pop(util.camelize('imageSignatureId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'artifacts',
            'GetContainerImageSignature',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'containerImageSignature',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="odx_registry_grp@oracle.com" jiraProject="OCIR" opsJiraProject="OCIR"
def test_get_container_repository(testing_service_client):
    if not testing_service_client.is_api_enabled('artifacts', 'GetContainerRepository'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('artifacts', util.camelize('artifacts'), 'GetContainerRepository')
    )

    request_containers = testing_service_client.get_requests(service_name='artifacts', api_name='GetContainerRepository')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.artifacts.ArtifactsClient(config, service_endpoint=service_endpoint)
            response = client.get_container_repository(
                repository_id=request.pop(util.camelize('repositoryId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'artifacts',
            'GetContainerRepository',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'containerRepository',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="odx_registry_grp@oracle.com" jiraProject="OCIR" opsJiraProject="OCIR"
def test_get_generic_artifact(testing_service_client):
    if not testing_service_client.is_api_enabled('artifacts', 'GetGenericArtifact'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('artifacts', util.camelize('artifacts'), 'GetGenericArtifact')
    )

    request_containers = testing_service_client.get_requests(service_name='artifacts', api_name='GetGenericArtifact')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.artifacts.ArtifactsClient(config, service_endpoint=service_endpoint)
            response = client.get_generic_artifact(
                artifact_id=request.pop(util.camelize('artifactId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'artifacts',
            'GetGenericArtifact',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'genericArtifact',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="odx_registry_grp@oracle.com" jiraProject="OCIR" opsJiraProject="OCIR"
def test_get_generic_artifact_by_path(testing_service_client):
    if not testing_service_client.is_api_enabled('artifacts', 'GetGenericArtifactByPath'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('artifacts', util.camelize('artifacts'), 'GetGenericArtifactByPath')
    )

    request_containers = testing_service_client.get_requests(service_name='artifacts', api_name='GetGenericArtifactByPath')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.artifacts.ArtifactsClient(config, service_endpoint=service_endpoint)
            response = client.get_generic_artifact_by_path(
                repository_id=request.pop(util.camelize('repositoryId')),
                artifact_path=request.pop(util.camelize('artifactPath')),
                version=request.pop(util.camelize('version')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'artifacts',
            'GetGenericArtifactByPath',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'genericArtifact',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="odx_registry_grp@oracle.com" jiraProject="OCIR" opsJiraProject="OCIR"
def test_get_repository(testing_service_client):
    if not testing_service_client.is_api_enabled('artifacts', 'GetRepository'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('artifacts', util.camelize('artifacts'), 'GetRepository')
    )

    request_containers = testing_service_client.get_requests(service_name='artifacts', api_name='GetRepository')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.artifacts.ArtifactsClient(config, service_endpoint=service_endpoint)
            response = client.get_repository(
                repository_id=request.pop(util.camelize('repositoryId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'artifacts',
            'GetRepository',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'repository',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="odx_registry_grp@oracle.com" jiraProject="OCIR" opsJiraProject="OCIR"
def test_list_container_image_signatures(testing_service_client):
    if not testing_service_client.is_api_enabled('artifacts', 'ListContainerImageSignatures'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('artifacts', util.camelize('artifacts'), 'ListContainerImageSignatures')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='artifacts', api_name='ListContainerImageSignatures')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.artifacts.ArtifactsClient(config, service_endpoint=service_endpoint)
            response = client.list_container_image_signatures(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_container_image_signatures(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_container_image_signatures(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'artifacts',
            'ListContainerImageSignatures',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'containerImageSignatureCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="odx_registry_grp@oracle.com" jiraProject="OCIR" opsJiraProject="OCIR"
def test_list_container_images(testing_service_client):
    if not testing_service_client.is_api_enabled('artifacts', 'ListContainerImages'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('artifacts', util.camelize('artifacts'), 'ListContainerImages')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='artifacts', api_name='ListContainerImages')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.artifacts.ArtifactsClient(config, service_endpoint=service_endpoint)
            response = client.list_container_images(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_container_images(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_container_images(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'artifacts',
            'ListContainerImages',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'containerImageCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="odx_registry_grp@oracle.com" jiraProject="OCIR" opsJiraProject="OCIR"
def test_list_container_repositories(testing_service_client):
    if not testing_service_client.is_api_enabled('artifacts', 'ListContainerRepositories'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('artifacts', util.camelize('artifacts'), 'ListContainerRepositories')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='artifacts', api_name='ListContainerRepositories')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.artifacts.ArtifactsClient(config, service_endpoint=service_endpoint)
            response = client.list_container_repositories(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_container_repositories(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_container_repositories(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'artifacts',
            'ListContainerRepositories',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'containerRepositoryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="odx_registry_grp@oracle.com" jiraProject="OCIR" opsJiraProject="OCIR"
def test_list_generic_artifacts(testing_service_client):
    if not testing_service_client.is_api_enabled('artifacts', 'ListGenericArtifacts'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('artifacts', util.camelize('artifacts'), 'ListGenericArtifacts')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='artifacts', api_name='ListGenericArtifacts')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.artifacts.ArtifactsClient(config, service_endpoint=service_endpoint)
            response = client.list_generic_artifacts(
                compartment_id=request.pop(util.camelize('compartmentId')),
                repository_id=request.pop(util.camelize('repositoryId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_generic_artifacts(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    repository_id=request.pop(util.camelize('repositoryId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_generic_artifacts(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        repository_id=request.pop(util.camelize('repositoryId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'artifacts',
            'ListGenericArtifacts',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'genericArtifactCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="odx_registry_grp@oracle.com" jiraProject="OCIR" opsJiraProject="OCIR"
def test_list_repositories(testing_service_client):
    if not testing_service_client.is_api_enabled('artifacts', 'ListRepositories'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('artifacts', util.camelize('artifacts'), 'ListRepositories')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='artifacts', api_name='ListRepositories')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.artifacts.ArtifactsClient(config, service_endpoint=service_endpoint)
            response = client.list_repositories(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_repositories(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_repositories(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'artifacts',
            'ListRepositories',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'repositoryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="odx_registry_grp@oracle.com" jiraProject="OCIR" opsJiraProject="OCIR"
def test_remove_container_version(testing_service_client):
    if not testing_service_client.is_api_enabled('artifacts', 'RemoveContainerVersion'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('artifacts', util.camelize('artifacts'), 'RemoveContainerVersion')
    )

    request_containers = testing_service_client.get_requests(service_name='artifacts', api_name='RemoveContainerVersion')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.artifacts.ArtifactsClient(config, service_endpoint=service_endpoint)
            response = client.remove_container_version(
                image_id=request.pop(util.camelize('imageId')),
                remove_container_version_details=request.pop(util.camelize('RemoveContainerVersionDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'artifacts',
            'RemoveContainerVersion',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'containerImage',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="odx_registry_grp@oracle.com" jiraProject="OCIR" opsJiraProject="OCIR"
def test_restore_container_image(testing_service_client):
    if not testing_service_client.is_api_enabled('artifacts', 'RestoreContainerImage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('artifacts', util.camelize('artifacts'), 'RestoreContainerImage')
    )

    request_containers = testing_service_client.get_requests(service_name='artifacts', api_name='RestoreContainerImage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.artifacts.ArtifactsClient(config, service_endpoint=service_endpoint)
            response = client.restore_container_image(
                image_id=request.pop(util.camelize('imageId')),
                restore_container_image_details=request.pop(util.camelize('RestoreContainerImageDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'artifacts',
            'RestoreContainerImage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'containerImage',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="odx_registry_grp@oracle.com" jiraProject="OCIR" opsJiraProject="OCIR"
def test_update_container_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('artifacts', 'UpdateContainerConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('artifacts', util.camelize('artifacts'), 'UpdateContainerConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='artifacts', api_name='UpdateContainerConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.artifacts.ArtifactsClient(config, service_endpoint=service_endpoint)
            response = client.update_container_configuration(
                compartment_id=request.pop(util.camelize('compartmentId')),
                update_container_configuration_details=request.pop(util.camelize('UpdateContainerConfigurationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'artifacts',
            'UpdateContainerConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'containerConfiguration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="odx_registry_grp@oracle.com" jiraProject="OCIR" opsJiraProject="OCIR"
def test_update_container_image(testing_service_client):
    if not testing_service_client.is_api_enabled('artifacts', 'UpdateContainerImage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('artifacts', util.camelize('artifacts'), 'UpdateContainerImage')
    )

    request_containers = testing_service_client.get_requests(service_name='artifacts', api_name='UpdateContainerImage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.artifacts.ArtifactsClient(config, service_endpoint=service_endpoint)
            response = client.update_container_image(
                image_id=request.pop(util.camelize('imageId')),
                update_container_image_details=request.pop(util.camelize('UpdateContainerImageDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'artifacts',
            'UpdateContainerImage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'containerImage',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="odx_registry_grp@oracle.com" jiraProject="OCIR" opsJiraProject="OCIR"
def test_update_container_image_signature(testing_service_client):
    if not testing_service_client.is_api_enabled('artifacts', 'UpdateContainerImageSignature'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('artifacts', util.camelize('artifacts'), 'UpdateContainerImageSignature')
    )

    request_containers = testing_service_client.get_requests(service_name='artifacts', api_name='UpdateContainerImageSignature')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.artifacts.ArtifactsClient(config, service_endpoint=service_endpoint)
            response = client.update_container_image_signature(
                image_signature_id=request.pop(util.camelize('imageSignatureId')),
                update_container_image_signature_details=request.pop(util.camelize('UpdateContainerImageSignatureDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'artifacts',
            'UpdateContainerImageSignature',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'containerImageSignature',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="odx_registry_grp@oracle.com" jiraProject="OCIR" opsJiraProject="OCIR"
def test_update_container_repository(testing_service_client):
    if not testing_service_client.is_api_enabled('artifacts', 'UpdateContainerRepository'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('artifacts', util.camelize('artifacts'), 'UpdateContainerRepository')
    )

    request_containers = testing_service_client.get_requests(service_name='artifacts', api_name='UpdateContainerRepository')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.artifacts.ArtifactsClient(config, service_endpoint=service_endpoint)
            response = client.update_container_repository(
                repository_id=request.pop(util.camelize('repositoryId')),
                update_container_repository_details=request.pop(util.camelize('UpdateContainerRepositoryDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'artifacts',
            'UpdateContainerRepository',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'containerRepository',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="odx_registry_grp@oracle.com" jiraProject="OCIR" opsJiraProject="OCIR"
def test_update_generic_artifact(testing_service_client):
    if not testing_service_client.is_api_enabled('artifacts', 'UpdateGenericArtifact'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('artifacts', util.camelize('artifacts'), 'UpdateGenericArtifact')
    )

    request_containers = testing_service_client.get_requests(service_name='artifacts', api_name='UpdateGenericArtifact')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.artifacts.ArtifactsClient(config, service_endpoint=service_endpoint)
            response = client.update_generic_artifact(
                artifact_id=request.pop(util.camelize('artifactId')),
                update_generic_artifact_details=request.pop(util.camelize('UpdateGenericArtifactDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'artifacts',
            'UpdateGenericArtifact',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'genericArtifact',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="odx_registry_grp@oracle.com" jiraProject="OCIR" opsJiraProject="OCIR"
def test_update_generic_artifact_by_path(testing_service_client):
    if not testing_service_client.is_api_enabled('artifacts', 'UpdateGenericArtifactByPath'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('artifacts', util.camelize('artifacts'), 'UpdateGenericArtifactByPath')
    )

    request_containers = testing_service_client.get_requests(service_name='artifacts', api_name='UpdateGenericArtifactByPath')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.artifacts.ArtifactsClient(config, service_endpoint=service_endpoint)
            response = client.update_generic_artifact_by_path(
                repository_id=request.pop(util.camelize('repositoryId')),
                artifact_path=request.pop(util.camelize('artifactPath')),
                version=request.pop(util.camelize('version')),
                update_generic_artifact_by_path_details=request.pop(util.camelize('UpdateGenericArtifactByPathDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'artifacts',
            'UpdateGenericArtifactByPath',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'genericArtifact',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="odx_registry_grp@oracle.com" jiraProject="OCIR" opsJiraProject="OCIR"
def test_update_repository(testing_service_client):
    if not testing_service_client.is_api_enabled('artifacts', 'UpdateRepository'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('artifacts', util.camelize('artifacts'), 'UpdateRepository')
    )

    request_containers = testing_service_client.get_requests(service_name='artifacts', api_name='UpdateRepository')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.artifacts.ArtifactsClient(config, service_endpoint=service_endpoint)
            response = client.update_repository(
                repository_id=request.pop(util.camelize('repositoryId')),
                update_repository_details=request.pop(util.camelize('UpdateRepositoryDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'artifacts',
            'UpdateRepository',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'repository',
            False,
            False
        )
