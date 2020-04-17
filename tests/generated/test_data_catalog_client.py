# Code generated. DO NOT EDIT.
# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
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

        cassette_location = os.path.join('generated', 'data_catalog_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_change_catalog_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'ChangeCatalogCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'ChangeCatalogCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='ChangeCatalogCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.change_catalog_compartment(
                change_catalog_compartment_details=request.pop(util.camelize('ChangeCatalogCompartmentDetails')),
                catalog_id=request.pop(util.camelize('catalogId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'ChangeCatalogCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_catalog_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_create_attribute(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'CreateAttribute'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'CreateAttribute')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='CreateAttribute')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.create_attribute(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                entity_key=request.pop(util.camelize('entityKey')),
                create_attribute_details=request.pop(util.camelize('CreateAttributeDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'CreateAttribute',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'attribute',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_create_attribute_tag(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'CreateAttributeTag'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'CreateAttributeTag')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='CreateAttributeTag')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.create_attribute_tag(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                entity_key=request.pop(util.camelize('entityKey')),
                attribute_key=request.pop(util.camelize('attributeKey')),
                create_attribute_tag_details=request.pop(util.camelize('CreateAttributeTagDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'CreateAttributeTag',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'attributeTag',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_create_catalog(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'CreateCatalog'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'CreateCatalog')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='CreateCatalog')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.create_catalog(
                create_catalog_details=request.pop(util.camelize('CreateCatalogDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'CreateCatalog',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_catalog',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_create_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'CreateConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'CreateConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='CreateConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.create_connection(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                create_connection_details=request.pop(util.camelize('CreateConnectionDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'CreateConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'connection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_create_data_asset(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'CreateDataAsset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'CreateDataAsset')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='CreateDataAsset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.create_data_asset(
                catalog_id=request.pop(util.camelize('catalogId')),
                create_data_asset_details=request.pop(util.camelize('CreateDataAssetDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'CreateDataAsset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataAsset',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_create_data_asset_tag(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'CreateDataAssetTag'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'CreateDataAssetTag')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='CreateDataAssetTag')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.create_data_asset_tag(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                create_data_asset_tag_details=request.pop(util.camelize('CreateDataAssetTagDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'CreateDataAssetTag',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataAssetTag',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_create_entity(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'CreateEntity'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'CreateEntity')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='CreateEntity')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.create_entity(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                create_entity_details=request.pop(util.camelize('CreateEntityDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'CreateEntity',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'entity',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_create_entity_tag(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'CreateEntityTag'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'CreateEntityTag')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='CreateEntityTag')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.create_entity_tag(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                entity_key=request.pop(util.camelize('entityKey')),
                create_entity_tag_details=request.pop(util.camelize('CreateEntityTagDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'CreateEntityTag',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'entityTag',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_create_folder(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'CreateFolder'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'CreateFolder')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='CreateFolder')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.create_folder(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                create_folder_details=request.pop(util.camelize('CreateFolderDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'CreateFolder',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'folder',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_create_folder_tag(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'CreateFolderTag'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'CreateFolderTag')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='CreateFolderTag')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.create_folder_tag(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                folder_key=request.pop(util.camelize('folderKey')),
                create_folder_tag_details=request.pop(util.camelize('CreateFolderTagDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'CreateFolderTag',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'folderTag',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_create_glossary(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'CreateGlossary'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'CreateGlossary')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='CreateGlossary')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.create_glossary(
                catalog_id=request.pop(util.camelize('catalogId')),
                create_glossary_details=request.pop(util.camelize('CreateGlossaryDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'CreateGlossary',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'glossary',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_create_job(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'CreateJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'CreateJob')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='CreateJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.create_job(
                catalog_id=request.pop(util.camelize('catalogId')),
                create_job_details=request.pop(util.camelize('CreateJobDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'CreateJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'job',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_create_job_definition(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'CreateJobDefinition'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'CreateJobDefinition')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='CreateJobDefinition')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.create_job_definition(
                catalog_id=request.pop(util.camelize('catalogId')),
                create_job_definition_details=request.pop(util.camelize('CreateJobDefinitionDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'CreateJobDefinition',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'jobDefinition',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_create_job_execution(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'CreateJobExecution'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'CreateJobExecution')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='CreateJobExecution')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.create_job_execution(
                catalog_id=request.pop(util.camelize('catalogId')),
                job_key=request.pop(util.camelize('jobKey')),
                create_job_execution_details=request.pop(util.camelize('CreateJobExecutionDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'CreateJobExecution',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'jobExecution',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_create_term(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'CreateTerm'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'CreateTerm')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='CreateTerm')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.create_term(
                catalog_id=request.pop(util.camelize('catalogId')),
                glossary_key=request.pop(util.camelize('glossaryKey')),
                create_term_details=request.pop(util.camelize('CreateTermDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'CreateTerm',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'term',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_create_term_relationship(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'CreateTermRelationship'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'CreateTermRelationship')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='CreateTermRelationship')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.create_term_relationship(
                catalog_id=request.pop(util.camelize('catalogId')),
                glossary_key=request.pop(util.camelize('glossaryKey')),
                term_key=request.pop(util.camelize('termKey')),
                create_term_relationship_details=request.pop(util.camelize('CreateTermRelationshipDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'CreateTermRelationship',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'termRelationship',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_delete_attribute(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'DeleteAttribute'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'DeleteAttribute')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='DeleteAttribute')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.delete_attribute(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                entity_key=request.pop(util.camelize('entityKey')),
                attribute_key=request.pop(util.camelize('attributeKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'DeleteAttribute',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_attribute',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_delete_attribute_tag(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'DeleteAttributeTag'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'DeleteAttributeTag')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='DeleteAttributeTag')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.delete_attribute_tag(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                entity_key=request.pop(util.camelize('entityKey')),
                attribute_key=request.pop(util.camelize('attributeKey')),
                tag_key=request.pop(util.camelize('tagKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'DeleteAttributeTag',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_attribute_tag',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_delete_catalog(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'DeleteCatalog'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'DeleteCatalog')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='DeleteCatalog')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.delete_catalog(
                catalog_id=request.pop(util.camelize('catalogId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'DeleteCatalog',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_catalog',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_delete_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'DeleteConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'DeleteConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='DeleteConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.delete_connection(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                connection_key=request.pop(util.camelize('connectionKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'DeleteConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_connection',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_delete_data_asset(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'DeleteDataAsset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'DeleteDataAsset')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='DeleteDataAsset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.delete_data_asset(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'DeleteDataAsset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_data_asset',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_delete_data_asset_tag(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'DeleteDataAssetTag'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'DeleteDataAssetTag')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='DeleteDataAssetTag')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.delete_data_asset_tag(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                tag_key=request.pop(util.camelize('tagKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'DeleteDataAssetTag',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_data_asset_tag',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_delete_entity(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'DeleteEntity'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'DeleteEntity')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='DeleteEntity')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.delete_entity(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                entity_key=request.pop(util.camelize('entityKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'DeleteEntity',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_entity',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_delete_entity_tag(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'DeleteEntityTag'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'DeleteEntityTag')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='DeleteEntityTag')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.delete_entity_tag(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                entity_key=request.pop(util.camelize('entityKey')),
                tag_key=request.pop(util.camelize('tagKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'DeleteEntityTag',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_entity_tag',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_delete_folder(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'DeleteFolder'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'DeleteFolder')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='DeleteFolder')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.delete_folder(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                folder_key=request.pop(util.camelize('folderKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'DeleteFolder',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_folder',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_delete_folder_tag(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'DeleteFolderTag'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'DeleteFolderTag')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='DeleteFolderTag')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.delete_folder_tag(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                folder_key=request.pop(util.camelize('folderKey')),
                tag_key=request.pop(util.camelize('tagKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'DeleteFolderTag',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_folder_tag',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_delete_glossary(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'DeleteGlossary'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'DeleteGlossary')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='DeleteGlossary')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.delete_glossary(
                catalog_id=request.pop(util.camelize('catalogId')),
                glossary_key=request.pop(util.camelize('glossaryKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'DeleteGlossary',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_glossary',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_delete_job(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'DeleteJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'DeleteJob')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='DeleteJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.delete_job(
                catalog_id=request.pop(util.camelize('catalogId')),
                job_key=request.pop(util.camelize('jobKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'DeleteJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_job',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_delete_job_definition(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'DeleteJobDefinition'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'DeleteJobDefinition')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='DeleteJobDefinition')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.delete_job_definition(
                catalog_id=request.pop(util.camelize('catalogId')),
                job_definition_key=request.pop(util.camelize('jobDefinitionKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'DeleteJobDefinition',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_job_definition',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_delete_term(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'DeleteTerm'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'DeleteTerm')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='DeleteTerm')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.delete_term(
                catalog_id=request.pop(util.camelize('catalogId')),
                glossary_key=request.pop(util.camelize('glossaryKey')),
                term_key=request.pop(util.camelize('termKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'DeleteTerm',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_term',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_delete_term_relationship(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'DeleteTermRelationship'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'DeleteTermRelationship')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='DeleteTermRelationship')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.delete_term_relationship(
                catalog_id=request.pop(util.camelize('catalogId')),
                glossary_key=request.pop(util.camelize('glossaryKey')),
                term_key=request.pop(util.camelize('termKey')),
                term_relationship_key=request.pop(util.camelize('termRelationshipKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'DeleteTermRelationship',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_term_relationship',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_expand_tree_for_glossary(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'ExpandTreeForGlossary'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'ExpandTreeForGlossary')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='ExpandTreeForGlossary')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.expand_tree_for_glossary(
                catalog_id=request.pop(util.camelize('catalogId')),
                glossary_key=request.pop(util.camelize('glossaryKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'ExpandTreeForGlossary',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'glossaryTreeElement',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_export_glossary(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'ExportGlossary'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'ExportGlossary')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='ExportGlossary')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.export_glossary(
                catalog_id=request.pop(util.camelize('catalogId')),
                glossary_key=request.pop(util.camelize('glossaryKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'ExportGlossary',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'str',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_get_attribute(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'GetAttribute'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'GetAttribute')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='GetAttribute')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.get_attribute(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                entity_key=request.pop(util.camelize('entityKey')),
                attribute_key=request.pop(util.camelize('attributeKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'GetAttribute',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'attribute',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_get_attribute_tag(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'GetAttributeTag'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'GetAttributeTag')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='GetAttributeTag')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.get_attribute_tag(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                entity_key=request.pop(util.camelize('entityKey')),
                attribute_key=request.pop(util.camelize('attributeKey')),
                tag_key=request.pop(util.camelize('tagKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'GetAttributeTag',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'attributeTag',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_get_catalog(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'GetCatalog'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'GetCatalog')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='GetCatalog')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.get_catalog(
                catalog_id=request.pop(util.camelize('catalogId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'GetCatalog',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'catalog',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_get_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'GetConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'GetConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='GetConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.get_connection(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                connection_key=request.pop(util.camelize('connectionKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'GetConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'connection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_get_data_asset(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'GetDataAsset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'GetDataAsset')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='GetDataAsset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.get_data_asset(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'GetDataAsset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataAsset',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_get_data_asset_tag(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'GetDataAssetTag'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'GetDataAssetTag')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='GetDataAssetTag')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.get_data_asset_tag(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                tag_key=request.pop(util.camelize('tagKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'GetDataAssetTag',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataAssetTag',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_get_entity(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'GetEntity'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'GetEntity')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='GetEntity')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.get_entity(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                entity_key=request.pop(util.camelize('entityKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'GetEntity',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'entity',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_get_entity_tag(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'GetEntityTag'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'GetEntityTag')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='GetEntityTag')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.get_entity_tag(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                entity_key=request.pop(util.camelize('entityKey')),
                tag_key=request.pop(util.camelize('tagKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'GetEntityTag',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'entityTag',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_get_folder(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'GetFolder'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'GetFolder')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='GetFolder')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.get_folder(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                folder_key=request.pop(util.camelize('folderKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'GetFolder',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'folder',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_get_folder_tag(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'GetFolderTag'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'GetFolderTag')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='GetFolderTag')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.get_folder_tag(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                folder_key=request.pop(util.camelize('folderKey')),
                tag_key=request.pop(util.camelize('tagKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'GetFolderTag',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'folderTag',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_get_glossary(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'GetGlossary'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'GetGlossary')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='GetGlossary')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.get_glossary(
                catalog_id=request.pop(util.camelize('catalogId')),
                glossary_key=request.pop(util.camelize('glossaryKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'GetGlossary',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'glossary',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_get_job(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'GetJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'GetJob')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='GetJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.get_job(
                catalog_id=request.pop(util.camelize('catalogId')),
                job_key=request.pop(util.camelize('jobKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'GetJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'job',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_get_job_definition(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'GetJobDefinition'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'GetJobDefinition')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='GetJobDefinition')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.get_job_definition(
                catalog_id=request.pop(util.camelize('catalogId')),
                job_definition_key=request.pop(util.camelize('jobDefinitionKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'GetJobDefinition',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'jobDefinition',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_get_job_execution(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'GetJobExecution'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'GetJobExecution')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='GetJobExecution')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.get_job_execution(
                catalog_id=request.pop(util.camelize('catalogId')),
                job_key=request.pop(util.camelize('jobKey')),
                job_execution_key=request.pop(util.camelize('jobExecutionKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'GetJobExecution',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'jobExecution',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_get_job_log(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'GetJobLog'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'GetJobLog')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='GetJobLog')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.get_job_log(
                catalog_id=request.pop(util.camelize('catalogId')),
                job_key=request.pop(util.camelize('jobKey')),
                job_execution_key=request.pop(util.camelize('jobExecutionKey')),
                job_log_key=request.pop(util.camelize('jobLogKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'GetJobLog',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'jobLog',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_get_job_metrics(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'GetJobMetrics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'GetJobMetrics')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='GetJobMetrics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.get_job_metrics(
                catalog_id=request.pop(util.camelize('catalogId')),
                job_key=request.pop(util.camelize('jobKey')),
                job_execution_key=request.pop(util.camelize('jobExecutionKey')),
                job_metrics_key=request.pop(util.camelize('jobMetricsKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'GetJobMetrics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'jobMetric',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_get_term(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'GetTerm'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'GetTerm')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='GetTerm')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.get_term(
                catalog_id=request.pop(util.camelize('catalogId')),
                glossary_key=request.pop(util.camelize('glossaryKey')),
                term_key=request.pop(util.camelize('termKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'GetTerm',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'term',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_get_term_relationship(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'GetTermRelationship'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'GetTermRelationship')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='GetTermRelationship')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.get_term_relationship(
                catalog_id=request.pop(util.camelize('catalogId')),
                glossary_key=request.pop(util.camelize('glossaryKey')),
                term_key=request.pop(util.camelize('termKey')),
                term_relationship_key=request.pop(util.camelize('termRelationshipKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'GetTermRelationship',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'termRelationship',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_get_type(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'GetType'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'GetType')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='GetType')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.get_type(
                catalog_id=request.pop(util.camelize('catalogId')),
                type_key=request.pop(util.camelize('typeKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'GetType',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'type',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_import_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'ImportConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'ImportConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='ImportConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.import_connection(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                import_connection_details=request.pop(util.camelize('ImportConnectionDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'ImportConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'connection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_import_glossary(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'ImportGlossary'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'ImportGlossary')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='ImportGlossary')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.import_glossary(
                catalog_id=request.pop(util.camelize('catalogId')),
                glossary_key=request.pop(util.camelize('glossaryKey')),
                import_glossary_details=request.pop(util.camelize('ImportGlossaryDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'ImportGlossary',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'import_glossary',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_list_attribute_tags(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'ListAttributeTags'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'ListAttributeTags')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='ListAttributeTags')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.list_attribute_tags(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                entity_key=request.pop(util.camelize('entityKey')),
                attribute_key=request.pop(util.camelize('attributeKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_attribute_tags(
                    catalog_id=request.pop(util.camelize('catalogId')),
                    data_asset_key=request.pop(util.camelize('dataAssetKey')),
                    entity_key=request.pop(util.camelize('entityKey')),
                    attribute_key=request.pop(util.camelize('attributeKey')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_attribute_tags(
                        catalog_id=request.pop(util.camelize('catalogId')),
                        data_asset_key=request.pop(util.camelize('dataAssetKey')),
                        entity_key=request.pop(util.camelize('entityKey')),
                        attribute_key=request.pop(util.camelize('attributeKey')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'ListAttributeTags',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'attributeTagCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_list_attributes(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'ListAttributes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'ListAttributes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='ListAttributes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.list_attributes(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                entity_key=request.pop(util.camelize('entityKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_attributes(
                    catalog_id=request.pop(util.camelize('catalogId')),
                    data_asset_key=request.pop(util.camelize('dataAssetKey')),
                    entity_key=request.pop(util.camelize('entityKey')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_attributes(
                        catalog_id=request.pop(util.camelize('catalogId')),
                        data_asset_key=request.pop(util.camelize('dataAssetKey')),
                        entity_key=request.pop(util.camelize('entityKey')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'ListAttributes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'attributeCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_list_catalogs(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'ListCatalogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'ListCatalogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='ListCatalogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.list_catalogs(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_catalogs(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_catalogs(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'ListCatalogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'catalogSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_list_connections(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'ListConnections'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'ListConnections')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='ListConnections')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.list_connections(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_connections(
                    catalog_id=request.pop(util.camelize('catalogId')),
                    data_asset_key=request.pop(util.camelize('dataAssetKey')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_connections(
                        catalog_id=request.pop(util.camelize('catalogId')),
                        data_asset_key=request.pop(util.camelize('dataAssetKey')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'ListConnections',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'connectionCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_list_data_asset_tags(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'ListDataAssetTags'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'ListDataAssetTags')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='ListDataAssetTags')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.list_data_asset_tags(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_data_asset_tags(
                    catalog_id=request.pop(util.camelize('catalogId')),
                    data_asset_key=request.pop(util.camelize('dataAssetKey')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_data_asset_tags(
                        catalog_id=request.pop(util.camelize('catalogId')),
                        data_asset_key=request.pop(util.camelize('dataAssetKey')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'ListDataAssetTags',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataAssetTagCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_list_data_assets(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'ListDataAssets'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'ListDataAssets')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='ListDataAssets')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.list_data_assets(
                catalog_id=request.pop(util.camelize('catalogId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_data_assets(
                    catalog_id=request.pop(util.camelize('catalogId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_data_assets(
                        catalog_id=request.pop(util.camelize('catalogId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'ListDataAssets',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataAssetCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_list_entities(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'ListEntities'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'ListEntities')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='ListEntities')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.list_entities(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_entities(
                    catalog_id=request.pop(util.camelize('catalogId')),
                    data_asset_key=request.pop(util.camelize('dataAssetKey')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_entities(
                        catalog_id=request.pop(util.camelize('catalogId')),
                        data_asset_key=request.pop(util.camelize('dataAssetKey')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'ListEntities',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'entityCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_list_entity_tags(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'ListEntityTags'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'ListEntityTags')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='ListEntityTags')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.list_entity_tags(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                entity_key=request.pop(util.camelize('entityKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_entity_tags(
                    catalog_id=request.pop(util.camelize('catalogId')),
                    data_asset_key=request.pop(util.camelize('dataAssetKey')),
                    entity_key=request.pop(util.camelize('entityKey')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_entity_tags(
                        catalog_id=request.pop(util.camelize('catalogId')),
                        data_asset_key=request.pop(util.camelize('dataAssetKey')),
                        entity_key=request.pop(util.camelize('entityKey')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'ListEntityTags',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'entityTagCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_list_folder_tags(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'ListFolderTags'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'ListFolderTags')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='ListFolderTags')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.list_folder_tags(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                folder_key=request.pop(util.camelize('folderKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_folder_tags(
                    catalog_id=request.pop(util.camelize('catalogId')),
                    data_asset_key=request.pop(util.camelize('dataAssetKey')),
                    folder_key=request.pop(util.camelize('folderKey')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_folder_tags(
                        catalog_id=request.pop(util.camelize('catalogId')),
                        data_asset_key=request.pop(util.camelize('dataAssetKey')),
                        folder_key=request.pop(util.camelize('folderKey')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'ListFolderTags',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'folderTagCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_list_folders(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'ListFolders'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'ListFolders')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='ListFolders')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.list_folders(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_folders(
                    catalog_id=request.pop(util.camelize('catalogId')),
                    data_asset_key=request.pop(util.camelize('dataAssetKey')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_folders(
                        catalog_id=request.pop(util.camelize('catalogId')),
                        data_asset_key=request.pop(util.camelize('dataAssetKey')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'ListFolders',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'folderCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_list_glossaries(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'ListGlossaries'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'ListGlossaries')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='ListGlossaries')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.list_glossaries(
                catalog_id=request.pop(util.camelize('catalogId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_glossaries(
                    catalog_id=request.pop(util.camelize('catalogId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_glossaries(
                        catalog_id=request.pop(util.camelize('catalogId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'ListGlossaries',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'glossaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_list_job_definitions(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'ListJobDefinitions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'ListJobDefinitions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='ListJobDefinitions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.list_job_definitions(
                catalog_id=request.pop(util.camelize('catalogId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_job_definitions(
                    catalog_id=request.pop(util.camelize('catalogId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_job_definitions(
                        catalog_id=request.pop(util.camelize('catalogId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'ListJobDefinitions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'jobDefinitionCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_list_job_executions(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'ListJobExecutions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'ListJobExecutions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='ListJobExecutions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.list_job_executions(
                catalog_id=request.pop(util.camelize('catalogId')),
                job_key=request.pop(util.camelize('jobKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_job_executions(
                    catalog_id=request.pop(util.camelize('catalogId')),
                    job_key=request.pop(util.camelize('jobKey')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_job_executions(
                        catalog_id=request.pop(util.camelize('catalogId')),
                        job_key=request.pop(util.camelize('jobKey')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'ListJobExecutions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'jobExecutionCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_list_job_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'ListJobLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'ListJobLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='ListJobLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.list_job_logs(
                catalog_id=request.pop(util.camelize('catalogId')),
                job_key=request.pop(util.camelize('jobKey')),
                job_execution_key=request.pop(util.camelize('jobExecutionKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_job_logs(
                    catalog_id=request.pop(util.camelize('catalogId')),
                    job_key=request.pop(util.camelize('jobKey')),
                    job_execution_key=request.pop(util.camelize('jobExecutionKey')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_job_logs(
                        catalog_id=request.pop(util.camelize('catalogId')),
                        job_key=request.pop(util.camelize('jobKey')),
                        job_execution_key=request.pop(util.camelize('jobExecutionKey')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'ListJobLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'jobLogCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_list_job_metrics(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'ListJobMetrics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'ListJobMetrics')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='ListJobMetrics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.list_job_metrics(
                catalog_id=request.pop(util.camelize('catalogId')),
                job_key=request.pop(util.camelize('jobKey')),
                job_execution_key=request.pop(util.camelize('jobExecutionKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_job_metrics(
                    catalog_id=request.pop(util.camelize('catalogId')),
                    job_key=request.pop(util.camelize('jobKey')),
                    job_execution_key=request.pop(util.camelize('jobExecutionKey')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_job_metrics(
                        catalog_id=request.pop(util.camelize('catalogId')),
                        job_key=request.pop(util.camelize('jobKey')),
                        job_execution_key=request.pop(util.camelize('jobExecutionKey')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'ListJobMetrics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'jobMetricCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_list_jobs(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'ListJobs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'ListJobs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='ListJobs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.list_jobs(
                catalog_id=request.pop(util.camelize('catalogId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_jobs(
                    catalog_id=request.pop(util.camelize('catalogId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_jobs(
                        catalog_id=request.pop(util.camelize('catalogId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'ListJobs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'jobCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_list_tags(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'ListTags'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'ListTags')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='ListTags')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.list_tags(
                catalog_id=request.pop(util.camelize('catalogId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_tags(
                    catalog_id=request.pop(util.camelize('catalogId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_tags(
                        catalog_id=request.pop(util.camelize('catalogId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'ListTags',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'termCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_list_term_relationships(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'ListTermRelationships'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'ListTermRelationships')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='ListTermRelationships')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.list_term_relationships(
                catalog_id=request.pop(util.camelize('catalogId')),
                glossary_key=request.pop(util.camelize('glossaryKey')),
                term_key=request.pop(util.camelize('termKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_term_relationships(
                    catalog_id=request.pop(util.camelize('catalogId')),
                    glossary_key=request.pop(util.camelize('glossaryKey')),
                    term_key=request.pop(util.camelize('termKey')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_term_relationships(
                        catalog_id=request.pop(util.camelize('catalogId')),
                        glossary_key=request.pop(util.camelize('glossaryKey')),
                        term_key=request.pop(util.camelize('termKey')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'ListTermRelationships',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'termRelationshipCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_list_terms(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'ListTerms'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'ListTerms')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='ListTerms')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.list_terms(
                catalog_id=request.pop(util.camelize('catalogId')),
                glossary_key=request.pop(util.camelize('glossaryKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_terms(
                    catalog_id=request.pop(util.camelize('catalogId')),
                    glossary_key=request.pop(util.camelize('glossaryKey')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_terms(
                        catalog_id=request.pop(util.camelize('catalogId')),
                        glossary_key=request.pop(util.camelize('glossaryKey')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'ListTerms',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'termCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_list_types(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'ListTypes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'ListTypes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='ListTypes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.list_types(
                catalog_id=request.pop(util.camelize('catalogId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_types(
                    catalog_id=request.pop(util.camelize('catalogId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_types(
                        catalog_id=request.pop(util.camelize('catalogId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'ListTypes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'typeCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_errors(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_errors(
                    work_request_id=request.pop(util.camelize('workRequestId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_request_errors(
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestError',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_logs(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_logs(
                    work_request_id=request.pop(util.camelize('workRequestId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_request_logs(
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLog',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
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
            'data_catalog',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_object_stats(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'ObjectStats'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'ObjectStats')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='ObjectStats')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.object_stats(
                catalog_id=request.pop(util.camelize('catalogId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.object_stats(
                    catalog_id=request.pop(util.camelize('catalogId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.object_stats(
                        catalog_id=request.pop(util.camelize('catalogId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'ObjectStats',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'str',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_parse_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'ParseConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'ParseConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='ParseConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.parse_connection(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                parse_connection_details=request.pop(util.camelize('ParseConnectionDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'ParseConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'connectionAliasSummary',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_search_criteria(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'SearchCriteria'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'SearchCriteria')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='SearchCriteria')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.search_criteria(
                catalog_id=request.pop(util.camelize('catalogId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.search_criteria(
                    catalog_id=request.pop(util.camelize('catalogId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.search_criteria(
                        catalog_id=request.pop(util.camelize('catalogId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'SearchCriteria',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'searchResultCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_test_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'TestConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'TestConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='TestConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.test_connection(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                connection_key=request.pop(util.camelize('connectionKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'TestConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'validateConnectionResult',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_update_attribute(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'UpdateAttribute'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'UpdateAttribute')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='UpdateAttribute')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.update_attribute(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                entity_key=request.pop(util.camelize('entityKey')),
                attribute_key=request.pop(util.camelize('attributeKey')),
                update_attribute_details=request.pop(util.camelize('UpdateAttributeDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'UpdateAttribute',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'attribute',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_update_catalog(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'UpdateCatalog'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'UpdateCatalog')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='UpdateCatalog')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.update_catalog(
                catalog_id=request.pop(util.camelize('catalogId')),
                update_catalog_details=request.pop(util.camelize('UpdateCatalogDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'UpdateCatalog',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'catalog',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_update_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'UpdateConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'UpdateConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='UpdateConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.update_connection(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                connection_key=request.pop(util.camelize('connectionKey')),
                update_connection_details=request.pop(util.camelize('UpdateConnectionDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'UpdateConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'connection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_update_data_asset(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'UpdateDataAsset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'UpdateDataAsset')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='UpdateDataAsset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.update_data_asset(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                update_data_asset_details=request.pop(util.camelize('UpdateDataAssetDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'UpdateDataAsset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataAsset',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_update_entity(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'UpdateEntity'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'UpdateEntity')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='UpdateEntity')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.update_entity(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                entity_key=request.pop(util.camelize('entityKey')),
                update_entity_details=request.pop(util.camelize('UpdateEntityDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'UpdateEntity',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'entity',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_update_folder(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'UpdateFolder'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'UpdateFolder')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='UpdateFolder')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.update_folder(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                folder_key=request.pop(util.camelize('folderKey')),
                update_folder_details=request.pop(util.camelize('UpdateFolderDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'UpdateFolder',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'folder',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_update_glossary(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'UpdateGlossary'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'UpdateGlossary')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='UpdateGlossary')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.update_glossary(
                catalog_id=request.pop(util.camelize('catalogId')),
                glossary_key=request.pop(util.camelize('glossaryKey')),
                update_glossary_details=request.pop(util.camelize('UpdateGlossaryDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'UpdateGlossary',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'glossary',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_update_job(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'UpdateJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'UpdateJob')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='UpdateJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.update_job(
                catalog_id=request.pop(util.camelize('catalogId')),
                job_key=request.pop(util.camelize('jobKey')),
                update_job_details=request.pop(util.camelize('UpdateJobDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'UpdateJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'job',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_update_job_definition(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'UpdateJobDefinition'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'UpdateJobDefinition')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='UpdateJobDefinition')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.update_job_definition(
                catalog_id=request.pop(util.camelize('catalogId')),
                job_definition_key=request.pop(util.camelize('jobDefinitionKey')),
                update_job_definition_details=request.pop(util.camelize('UpdateJobDefinitionDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'UpdateJobDefinition',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'jobDefinition',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_update_term(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'UpdateTerm'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'UpdateTerm')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='UpdateTerm')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.update_term(
                catalog_id=request.pop(util.camelize('catalogId')),
                glossary_key=request.pop(util.camelize('glossaryKey')),
                term_key=request.pop(util.camelize('termKey')),
                update_term_details=request.pop(util.camelize('UpdateTermDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'UpdateTerm',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'term',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_update_term_relationship(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'UpdateTermRelationship'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'UpdateTermRelationship')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='UpdateTermRelationship')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.update_term_relationship(
                catalog_id=request.pop(util.camelize('catalogId')),
                glossary_key=request.pop(util.camelize('glossaryKey')),
                term_key=request.pop(util.camelize('termKey')),
                term_relationship_key=request.pop(util.camelize('termRelationshipKey')),
                update_term_relationship_details=request.pop(util.camelize('UpdateTermRelationshipDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'UpdateTermRelationship',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'termRelationship',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_upload_credentials(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'UploadCredentials'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'UploadCredentials')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='UploadCredentials')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.upload_credentials(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                connection_key=request.pop(util.camelize('connectionKey')),
                upload_credentials_details=request.pop(util.camelize('UploadCredentialsDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'UploadCredentials',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'connection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_users(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'Users'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'Users')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='Users')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.users(
                catalog_id=request.pop(util.camelize('catalogId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.users(
                    catalog_id=request.pop(util.camelize('catalogId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.users(
                        catalog_id=request.pop(util.camelize('catalogId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'Users',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'str',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datacatalog_ww_grp@oracle.com" jiraProject="DCAT" opsJiraProject="ADCS"
def test_validate_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('data_catalog', 'ValidateConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_catalog', util.camelize('data_catalog'), 'ValidateConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='data_catalog', api_name='ValidateConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_catalog.DataCatalogClient(config, service_endpoint=service_endpoint)
            response = client.validate_connection(
                catalog_id=request.pop(util.camelize('catalogId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                validate_connection_details=request.pop(util.camelize('ValidateConnectionDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_catalog',
            'ValidateConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'validateConnectionResult',
            False,
            False
        )
