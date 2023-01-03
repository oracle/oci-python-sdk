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

        cassette_location = os.path.join('generated', 'service_catalog_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_bulk_replace_service_catalog_associations(testing_service_client):
    if not testing_service_client.is_api_enabled('service_catalog', 'BulkReplaceServiceCatalogAssociations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_catalog', util.camelize('service_catalog'), 'BulkReplaceServiceCatalogAssociations')
    )

    request_containers = testing_service_client.get_requests(service_name='service_catalog', api_name='BulkReplaceServiceCatalogAssociations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_catalog.ServiceCatalogClient(config, service_endpoint=service_endpoint)
            response = client.bulk_replace_service_catalog_associations(
                service_catalog_id=request.pop(util.camelize('serviceCatalogId')),
                bulk_replace_service_catalog_associations_details=request.pop(util.camelize('BulkReplaceServiceCatalogAssociationsDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_catalog',
            'BulkReplaceServiceCatalogAssociations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bulk_replace_service_catalog_associations',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_change_private_application_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('service_catalog', 'ChangePrivateApplicationCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_catalog', util.camelize('service_catalog'), 'ChangePrivateApplicationCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='service_catalog', api_name='ChangePrivateApplicationCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_catalog.ServiceCatalogClient(config, service_endpoint=service_endpoint)
            response = client.change_private_application_compartment(
                private_application_id=request.pop(util.camelize('privateApplicationId')),
                change_private_application_compartment_details=request.pop(util.camelize('ChangePrivateApplicationCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_catalog',
            'ChangePrivateApplicationCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_private_application_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_change_service_catalog_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('service_catalog', 'ChangeServiceCatalogCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_catalog', util.camelize('service_catalog'), 'ChangeServiceCatalogCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='service_catalog', api_name='ChangeServiceCatalogCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_catalog.ServiceCatalogClient(config, service_endpoint=service_endpoint)
            response = client.change_service_catalog_compartment(
                service_catalog_id=request.pop(util.camelize('serviceCatalogId')),
                change_service_catalog_compartment_details=request.pop(util.camelize('ChangeServiceCatalogCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_catalog',
            'ChangeServiceCatalogCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_service_catalog_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_create_private_application(testing_service_client):
    if not testing_service_client.is_api_enabled('service_catalog', 'CreatePrivateApplication'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_catalog', util.camelize('service_catalog'), 'CreatePrivateApplication')
    )

    request_containers = testing_service_client.get_requests(service_name='service_catalog', api_name='CreatePrivateApplication')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_catalog.ServiceCatalogClient(config, service_endpoint=service_endpoint)
            response = client.create_private_application(
                create_private_application_details=request.pop(util.camelize('CreatePrivateApplicationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_catalog',
            'CreatePrivateApplication',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'privateApplication',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_create_service_catalog(testing_service_client):
    if not testing_service_client.is_api_enabled('service_catalog', 'CreateServiceCatalog'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_catalog', util.camelize('service_catalog'), 'CreateServiceCatalog')
    )

    request_containers = testing_service_client.get_requests(service_name='service_catalog', api_name='CreateServiceCatalog')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_catalog.ServiceCatalogClient(config, service_endpoint=service_endpoint)
            response = client.create_service_catalog(
                create_service_catalog_details=request.pop(util.camelize('CreateServiceCatalogDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_catalog',
            'CreateServiceCatalog',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'serviceCatalog',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_create_service_catalog_association(testing_service_client):
    if not testing_service_client.is_api_enabled('service_catalog', 'CreateServiceCatalogAssociation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_catalog', util.camelize('service_catalog'), 'CreateServiceCatalogAssociation')
    )

    request_containers = testing_service_client.get_requests(service_name='service_catalog', api_name='CreateServiceCatalogAssociation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_catalog.ServiceCatalogClient(config, service_endpoint=service_endpoint)
            response = client.create_service_catalog_association(
                create_service_catalog_association_details=request.pop(util.camelize('CreateServiceCatalogAssociationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_catalog',
            'CreateServiceCatalogAssociation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'serviceCatalogAssociation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_delete_private_application(testing_service_client):
    if not testing_service_client.is_api_enabled('service_catalog', 'DeletePrivateApplication'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_catalog', util.camelize('service_catalog'), 'DeletePrivateApplication')
    )

    request_containers = testing_service_client.get_requests(service_name='service_catalog', api_name='DeletePrivateApplication')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_catalog.ServiceCatalogClient(config, service_endpoint=service_endpoint)
            response = client.delete_private_application(
                private_application_id=request.pop(util.camelize('privateApplicationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_catalog',
            'DeletePrivateApplication',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_private_application',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_delete_service_catalog(testing_service_client):
    if not testing_service_client.is_api_enabled('service_catalog', 'DeleteServiceCatalog'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_catalog', util.camelize('service_catalog'), 'DeleteServiceCatalog')
    )

    request_containers = testing_service_client.get_requests(service_name='service_catalog', api_name='DeleteServiceCatalog')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_catalog.ServiceCatalogClient(config, service_endpoint=service_endpoint)
            response = client.delete_service_catalog(
                service_catalog_id=request.pop(util.camelize('serviceCatalogId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_catalog',
            'DeleteServiceCatalog',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_service_catalog',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_delete_service_catalog_association(testing_service_client):
    if not testing_service_client.is_api_enabled('service_catalog', 'DeleteServiceCatalogAssociation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_catalog', util.camelize('service_catalog'), 'DeleteServiceCatalogAssociation')
    )

    request_containers = testing_service_client.get_requests(service_name='service_catalog', api_name='DeleteServiceCatalogAssociation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_catalog.ServiceCatalogClient(config, service_endpoint=service_endpoint)
            response = client.delete_service_catalog_association(
                service_catalog_association_id=request.pop(util.camelize('serviceCatalogAssociationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_catalog',
            'DeleteServiceCatalogAssociation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_service_catalog_association',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_get_private_application(testing_service_client):
    if not testing_service_client.is_api_enabled('service_catalog', 'GetPrivateApplication'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_catalog', util.camelize('service_catalog'), 'GetPrivateApplication')
    )

    request_containers = testing_service_client.get_requests(service_name='service_catalog', api_name='GetPrivateApplication')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_catalog.ServiceCatalogClient(config, service_endpoint=service_endpoint)
            response = client.get_private_application(
                private_application_id=request.pop(util.camelize('privateApplicationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_catalog',
            'GetPrivateApplication',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'privateApplication',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_get_private_application_action_download_logo(testing_service_client):
    if not testing_service_client.is_api_enabled('service_catalog', 'GetPrivateApplicationActionDownloadLogo'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_catalog', util.camelize('service_catalog'), 'GetPrivateApplicationActionDownloadLogo')
    )

    request_containers = testing_service_client.get_requests(service_name='service_catalog', api_name='GetPrivateApplicationActionDownloadLogo')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_catalog.ServiceCatalogClient(config, service_endpoint=service_endpoint)
            response = client.get_private_application_action_download_logo(
                private_application_id=request.pop(util.camelize('privateApplicationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_catalog',
            'GetPrivateApplicationActionDownloadLogo',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_get_private_application_package(testing_service_client):
    if not testing_service_client.is_api_enabled('service_catalog', 'GetPrivateApplicationPackage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_catalog', util.camelize('service_catalog'), 'GetPrivateApplicationPackage')
    )

    request_containers = testing_service_client.get_requests(service_name='service_catalog', api_name='GetPrivateApplicationPackage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_catalog.ServiceCatalogClient(config, service_endpoint=service_endpoint)
            response = client.get_private_application_package(
                private_application_package_id=request.pop(util.camelize('privateApplicationPackageId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_catalog',
            'GetPrivateApplicationPackage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'privateApplicationPackage',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_get_private_application_package_action_download_config(testing_service_client):
    if not testing_service_client.is_api_enabled('service_catalog', 'GetPrivateApplicationPackageActionDownloadConfig'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_catalog', util.camelize('service_catalog'), 'GetPrivateApplicationPackageActionDownloadConfig')
    )

    request_containers = testing_service_client.get_requests(service_name='service_catalog', api_name='GetPrivateApplicationPackageActionDownloadConfig')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_catalog.ServiceCatalogClient(config, service_endpoint=service_endpoint)
            response = client.get_private_application_package_action_download_config(
                private_application_package_id=request.pop(util.camelize('privateApplicationPackageId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_catalog',
            'GetPrivateApplicationPackageActionDownloadConfig',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_get_service_catalog(testing_service_client):
    if not testing_service_client.is_api_enabled('service_catalog', 'GetServiceCatalog'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_catalog', util.camelize('service_catalog'), 'GetServiceCatalog')
    )

    request_containers = testing_service_client.get_requests(service_name='service_catalog', api_name='GetServiceCatalog')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_catalog.ServiceCatalogClient(config, service_endpoint=service_endpoint)
            response = client.get_service_catalog(
                service_catalog_id=request.pop(util.camelize('serviceCatalogId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_catalog',
            'GetServiceCatalog',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'serviceCatalog',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_get_service_catalog_association(testing_service_client):
    if not testing_service_client.is_api_enabled('service_catalog', 'GetServiceCatalogAssociation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_catalog', util.camelize('service_catalog'), 'GetServiceCatalogAssociation')
    )

    request_containers = testing_service_client.get_requests(service_name='service_catalog', api_name='GetServiceCatalogAssociation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_catalog.ServiceCatalogClient(config, service_endpoint=service_endpoint)
            response = client.get_service_catalog_association(
                service_catalog_association_id=request.pop(util.camelize('serviceCatalogAssociationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_catalog',
            'GetServiceCatalogAssociation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'serviceCatalogAssociation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('service_catalog', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_catalog', util.camelize('service_catalog'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='service_catalog', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_catalog.ServiceCatalogClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_catalog',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_list_applications(testing_service_client):
    if not testing_service_client.is_api_enabled('service_catalog', 'ListApplications'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_catalog', util.camelize('service_catalog'), 'ListApplications')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='service_catalog', api_name='ListApplications')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_catalog.ServiceCatalogClient(config, service_endpoint=service_endpoint)
            response = client.list_applications(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_applications(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_applications(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_catalog',
            'ListApplications',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'applicationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_list_private_application_packages(testing_service_client):
    if not testing_service_client.is_api_enabled('service_catalog', 'ListPrivateApplicationPackages'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_catalog', util.camelize('service_catalog'), 'ListPrivateApplicationPackages')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='service_catalog', api_name='ListPrivateApplicationPackages')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_catalog.ServiceCatalogClient(config, service_endpoint=service_endpoint)
            response = client.list_private_application_packages(
                private_application_id=request.pop(util.camelize('privateApplicationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_private_application_packages(
                    private_application_id=request.pop(util.camelize('privateApplicationId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_private_application_packages(
                        private_application_id=request.pop(util.camelize('privateApplicationId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_catalog',
            'ListPrivateApplicationPackages',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'privateApplicationPackageCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_list_private_applications(testing_service_client):
    if not testing_service_client.is_api_enabled('service_catalog', 'ListPrivateApplications'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_catalog', util.camelize('service_catalog'), 'ListPrivateApplications')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='service_catalog', api_name='ListPrivateApplications')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_catalog.ServiceCatalogClient(config, service_endpoint=service_endpoint)
            response = client.list_private_applications(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_private_applications(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_private_applications(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_catalog',
            'ListPrivateApplications',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'privateApplicationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_list_service_catalog_associations(testing_service_client):
    if not testing_service_client.is_api_enabled('service_catalog', 'ListServiceCatalogAssociations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_catalog', util.camelize('service_catalog'), 'ListServiceCatalogAssociations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='service_catalog', api_name='ListServiceCatalogAssociations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_catalog.ServiceCatalogClient(config, service_endpoint=service_endpoint)
            response = client.list_service_catalog_associations(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_service_catalog_associations(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_service_catalog_associations(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_catalog',
            'ListServiceCatalogAssociations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'serviceCatalogAssociationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_list_service_catalogs(testing_service_client):
    if not testing_service_client.is_api_enabled('service_catalog', 'ListServiceCatalogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_catalog', util.camelize('service_catalog'), 'ListServiceCatalogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='service_catalog', api_name='ListServiceCatalogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_catalog.ServiceCatalogClient(config, service_endpoint=service_endpoint)
            response = client.list_service_catalogs(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_service_catalogs(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_service_catalogs(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_catalog',
            'ListServiceCatalogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'serviceCatalogCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('service_catalog', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_catalog', util.camelize('service_catalog'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='service_catalog', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_catalog.ServiceCatalogClient(config, service_endpoint=service_endpoint)
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
            'service_catalog',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestErrorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('service_catalog', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_catalog', util.camelize('service_catalog'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='service_catalog', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_catalog.ServiceCatalogClient(config, service_endpoint=service_endpoint)
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
            'service_catalog',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('service_catalog', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_catalog', util.camelize('service_catalog'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='service_catalog', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_catalog.ServiceCatalogClient(config, service_endpoint=service_endpoint)
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
            'service_catalog',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_update_private_application(testing_service_client):
    if not testing_service_client.is_api_enabled('service_catalog', 'UpdatePrivateApplication'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_catalog', util.camelize('service_catalog'), 'UpdatePrivateApplication')
    )

    request_containers = testing_service_client.get_requests(service_name='service_catalog', api_name='UpdatePrivateApplication')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_catalog.ServiceCatalogClient(config, service_endpoint=service_endpoint)
            response = client.update_private_application(
                private_application_id=request.pop(util.camelize('privateApplicationId')),
                update_private_application_details=request.pop(util.camelize('UpdatePrivateApplicationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_catalog',
            'UpdatePrivateApplication',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'privateApplication',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_update_service_catalog(testing_service_client):
    if not testing_service_client.is_api_enabled('service_catalog', 'UpdateServiceCatalog'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('service_catalog', util.camelize('service_catalog'), 'UpdateServiceCatalog')
    )

    request_containers = testing_service_client.get_requests(service_name='service_catalog', api_name='UpdateServiceCatalog')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.service_catalog.ServiceCatalogClient(config, service_endpoint=service_endpoint)
            response = client.update_service_catalog(
                service_catalog_id=request.pop(util.camelize('serviceCatalogId')),
                update_service_catalog_details=request.pop(util.camelize('UpdateServiceCatalogDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'service_catalog',
            'UpdateServiceCatalog',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'serviceCatalog',
            False,
            False
        )
