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

        cassette_location = os.path.join('generated', 'marketplace_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_change_publication_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('marketplace', 'ChangePublicationCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('marketplace', util.camelize('marketplace'), 'ChangePublicationCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='marketplace', api_name='ChangePublicationCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.marketplace.MarketplaceClient(config, service_endpoint=service_endpoint)
            response = client.change_publication_compartment(
                publication_id=request.pop(util.camelize('publicationId')),
                change_publication_compartment_details=request.pop(util.camelize('ChangePublicationCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'marketplace',
            'ChangePublicationCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_publication_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_create_accepted_agreement(testing_service_client):
    if not testing_service_client.is_api_enabled('marketplace', 'CreateAcceptedAgreement'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('marketplace', util.camelize('marketplace'), 'CreateAcceptedAgreement')
    )

    request_containers = testing_service_client.get_requests(service_name='marketplace', api_name='CreateAcceptedAgreement')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.marketplace.MarketplaceClient(config, service_endpoint=service_endpoint)
            response = client.create_accepted_agreement(
                create_accepted_agreement_details=request.pop(util.camelize('CreateAcceptedAgreementDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'marketplace',
            'CreateAcceptedAgreement',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'acceptedAgreement',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_create_publication(testing_service_client):
    if not testing_service_client.is_api_enabled('marketplace', 'CreatePublication'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('marketplace', util.camelize('marketplace'), 'CreatePublication')
    )

    request_containers = testing_service_client.get_requests(service_name='marketplace', api_name='CreatePublication')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.marketplace.MarketplaceClient(config, service_endpoint=service_endpoint)
            response = client.create_publication(
                create_publication_details=request.pop(util.camelize('CreatePublicationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'marketplace',
            'CreatePublication',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'publication',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_delete_accepted_agreement(testing_service_client):
    if not testing_service_client.is_api_enabled('marketplace', 'DeleteAcceptedAgreement'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('marketplace', util.camelize('marketplace'), 'DeleteAcceptedAgreement')
    )

    request_containers = testing_service_client.get_requests(service_name='marketplace', api_name='DeleteAcceptedAgreement')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.marketplace.MarketplaceClient(config, service_endpoint=service_endpoint)
            response = client.delete_accepted_agreement(
                accepted_agreement_id=request.pop(util.camelize('acceptedAgreementId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'marketplace',
            'DeleteAcceptedAgreement',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_accepted_agreement',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_delete_publication(testing_service_client):
    if not testing_service_client.is_api_enabled('marketplace', 'DeletePublication'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('marketplace', util.camelize('marketplace'), 'DeletePublication')
    )

    request_containers = testing_service_client.get_requests(service_name='marketplace', api_name='DeletePublication')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.marketplace.MarketplaceClient(config, service_endpoint=service_endpoint)
            response = client.delete_publication(
                publication_id=request.pop(util.camelize('publicationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'marketplace',
            'DeletePublication',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_publication',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_get_accepted_agreement(testing_service_client):
    if not testing_service_client.is_api_enabled('marketplace', 'GetAcceptedAgreement'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('marketplace', util.camelize('marketplace'), 'GetAcceptedAgreement')
    )

    request_containers = testing_service_client.get_requests(service_name='marketplace', api_name='GetAcceptedAgreement')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.marketplace.MarketplaceClient(config, service_endpoint=service_endpoint)
            response = client.get_accepted_agreement(
                accepted_agreement_id=request.pop(util.camelize('acceptedAgreementId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'marketplace',
            'GetAcceptedAgreement',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'acceptedAgreement',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_get_agreement(testing_service_client):
    if not testing_service_client.is_api_enabled('marketplace', 'GetAgreement'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('marketplace', util.camelize('marketplace'), 'GetAgreement')
    )

    request_containers = testing_service_client.get_requests(service_name='marketplace', api_name='GetAgreement')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.marketplace.MarketplaceClient(config, service_endpoint=service_endpoint)
            response = client.get_agreement(
                listing_id=request.pop(util.camelize('listingId')),
                package_version=request.pop(util.camelize('packageVersion')),
                agreement_id=request.pop(util.camelize('agreementId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'marketplace',
            'GetAgreement',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'agreement',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_get_listing(testing_service_client):
    if not testing_service_client.is_api_enabled('marketplace', 'GetListing'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('marketplace', util.camelize('marketplace'), 'GetListing')
    )

    request_containers = testing_service_client.get_requests(service_name='marketplace', api_name='GetListing')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.marketplace.MarketplaceClient(config, service_endpoint=service_endpoint)
            response = client.get_listing(
                listing_id=request.pop(util.camelize('listingId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'marketplace',
            'GetListing',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'listing',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_get_package(testing_service_client):
    if not testing_service_client.is_api_enabled('marketplace', 'GetPackage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('marketplace', util.camelize('marketplace'), 'GetPackage')
    )

    request_containers = testing_service_client.get_requests(service_name='marketplace', api_name='GetPackage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.marketplace.MarketplaceClient(config, service_endpoint=service_endpoint)
            response = client.get_package(
                listing_id=request.pop(util.camelize('listingId')),
                package_version=request.pop(util.camelize('packageVersion')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'marketplace',
            'GetPackage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'listingPackage',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_get_publication(testing_service_client):
    if not testing_service_client.is_api_enabled('marketplace', 'GetPublication'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('marketplace', util.camelize('marketplace'), 'GetPublication')
    )

    request_containers = testing_service_client.get_requests(service_name='marketplace', api_name='GetPublication')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.marketplace.MarketplaceClient(config, service_endpoint=service_endpoint)
            response = client.get_publication(
                publication_id=request.pop(util.camelize('publicationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'marketplace',
            'GetPublication',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'publication',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_get_publication_package(testing_service_client):
    if not testing_service_client.is_api_enabled('marketplace', 'GetPublicationPackage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('marketplace', util.camelize('marketplace'), 'GetPublicationPackage')
    )

    request_containers = testing_service_client.get_requests(service_name='marketplace', api_name='GetPublicationPackage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.marketplace.MarketplaceClient(config, service_endpoint=service_endpoint)
            response = client.get_publication_package(
                publication_id=request.pop(util.camelize('publicationId')),
                package_version=request.pop(util.camelize('packageVersion')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'marketplace',
            'GetPublicationPackage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'publicationPackage',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_list_accepted_agreements(testing_service_client):
    if not testing_service_client.is_api_enabled('marketplace', 'ListAcceptedAgreements'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('marketplace', util.camelize('marketplace'), 'ListAcceptedAgreements')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='marketplace', api_name='ListAcceptedAgreements')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.marketplace.MarketplaceClient(config, service_endpoint=service_endpoint)
            response = client.list_accepted_agreements(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_accepted_agreements(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_accepted_agreements(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'marketplace',
            'ListAcceptedAgreements',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'acceptedAgreementSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_list_agreements(testing_service_client):
    if not testing_service_client.is_api_enabled('marketplace', 'ListAgreements'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('marketplace', util.camelize('marketplace'), 'ListAgreements')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='marketplace', api_name='ListAgreements')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.marketplace.MarketplaceClient(config, service_endpoint=service_endpoint)
            response = client.list_agreements(
                listing_id=request.pop(util.camelize('listingId')),
                package_version=request.pop(util.camelize('packageVersion')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_agreements(
                    listing_id=request.pop(util.camelize('listingId')),
                    package_version=request.pop(util.camelize('packageVersion')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_agreements(
                        listing_id=request.pop(util.camelize('listingId')),
                        package_version=request.pop(util.camelize('packageVersion')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'marketplace',
            'ListAgreements',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'agreementSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_list_categories(testing_service_client):
    if not testing_service_client.is_api_enabled('marketplace', 'ListCategories'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('marketplace', util.camelize('marketplace'), 'ListCategories')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='marketplace', api_name='ListCategories')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.marketplace.MarketplaceClient(config, service_endpoint=service_endpoint)
            response = client.list_categories(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_categories(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_categories(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'marketplace',
            'ListCategories',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'categorySummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_list_listings(testing_service_client):
    if not testing_service_client.is_api_enabled('marketplace', 'ListListings'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('marketplace', util.camelize('marketplace'), 'ListListings')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='marketplace', api_name='ListListings')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.marketplace.MarketplaceClient(config, service_endpoint=service_endpoint)
            response = client.list_listings(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_listings(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_listings(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'marketplace',
            'ListListings',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'listingSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_list_packages(testing_service_client):
    if not testing_service_client.is_api_enabled('marketplace', 'ListPackages'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('marketplace', util.camelize('marketplace'), 'ListPackages')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='marketplace', api_name='ListPackages')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.marketplace.MarketplaceClient(config, service_endpoint=service_endpoint)
            response = client.list_packages(
                listing_id=request.pop(util.camelize('listingId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_packages(
                    listing_id=request.pop(util.camelize('listingId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_packages(
                        listing_id=request.pop(util.camelize('listingId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'marketplace',
            'ListPackages',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'listingPackageSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_list_publication_packages(testing_service_client):
    if not testing_service_client.is_api_enabled('marketplace', 'ListPublicationPackages'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('marketplace', util.camelize('marketplace'), 'ListPublicationPackages')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='marketplace', api_name='ListPublicationPackages')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.marketplace.MarketplaceClient(config, service_endpoint=service_endpoint)
            response = client.list_publication_packages(
                publication_id=request.pop(util.camelize('publicationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_publication_packages(
                    publication_id=request.pop(util.camelize('publicationId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_publication_packages(
                        publication_id=request.pop(util.camelize('publicationId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'marketplace',
            'ListPublicationPackages',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'publicationPackageSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_list_publications(testing_service_client):
    if not testing_service_client.is_api_enabled('marketplace', 'ListPublications'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('marketplace', util.camelize('marketplace'), 'ListPublications')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='marketplace', api_name='ListPublications')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.marketplace.MarketplaceClient(config, service_endpoint=service_endpoint)
            response = client.list_publications(
                compartment_id=request.pop(util.camelize('compartmentId')),
                listing_type=request.pop(util.camelize('listingType')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_publications(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    listing_type=request.pop(util.camelize('listingType')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_publications(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        listing_type=request.pop(util.camelize('listingType')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'marketplace',
            'ListPublications',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'publicationSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_list_publishers(testing_service_client):
    if not testing_service_client.is_api_enabled('marketplace', 'ListPublishers'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('marketplace', util.camelize('marketplace'), 'ListPublishers')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='marketplace', api_name='ListPublishers')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.marketplace.MarketplaceClient(config, service_endpoint=service_endpoint)
            response = client.list_publishers(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_publishers(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_publishers(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'marketplace',
            'ListPublishers',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'publisherSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_list_report_types(testing_service_client):
    if not testing_service_client.is_api_enabled('marketplace', 'ListReportTypes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('marketplace', util.camelize('marketplace'), 'ListReportTypes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='marketplace', api_name='ListReportTypes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.marketplace.MarketplaceClient(config, service_endpoint=service_endpoint)
            response = client.list_report_types(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_report_types(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_report_types(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'marketplace',
            'ListReportTypes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'reportTypeCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_list_reports(testing_service_client):
    if not testing_service_client.is_api_enabled('marketplace', 'ListReports'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('marketplace', util.camelize('marketplace'), 'ListReports')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='marketplace', api_name='ListReports')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.marketplace.MarketplaceClient(config, service_endpoint=service_endpoint)
            response = client.list_reports(
                report_type=request.pop(util.camelize('reportType')),
                date=request.pop(util.camelize('date')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_reports(
                    report_type=request.pop(util.camelize('reportType')),
                    date=request.pop(util.camelize('date')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_reports(
                        report_type=request.pop(util.camelize('reportType')),
                        date=request.pop(util.camelize('date')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'marketplace',
            'ListReports',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'reportCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_list_taxes(testing_service_client):
    if not testing_service_client.is_api_enabled('marketplace', 'ListTaxes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('marketplace', util.camelize('marketplace'), 'ListTaxes')
    )

    request_containers = testing_service_client.get_requests(service_name='marketplace', api_name='ListTaxes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.marketplace.MarketplaceClient(config, service_endpoint=service_endpoint)
            response = client.list_taxes(
                listing_id=request.pop(util.camelize('listingId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'marketplace',
            'ListTaxes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'taxSummary',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_search_listings(testing_service_client):
    if not testing_service_client.is_api_enabled('marketplace', 'SearchListings'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('marketplace', util.camelize('marketplace'), 'SearchListings')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='marketplace', api_name='SearchListings')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.marketplace.MarketplaceClient(config, service_endpoint=service_endpoint)
            response = client.search_listings(
                search_listings_details=request.pop(util.camelize('SearchListingsDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.search_listings(
                    search_listings_details=request.pop(util.camelize('SearchListingsDetails')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.search_listings(
                        search_listings_details=request.pop(util.camelize('SearchListingsDetails')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'marketplace',
            'SearchListings',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'listingSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_update_accepted_agreement(testing_service_client):
    if not testing_service_client.is_api_enabled('marketplace', 'UpdateAcceptedAgreement'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('marketplace', util.camelize('marketplace'), 'UpdateAcceptedAgreement')
    )

    request_containers = testing_service_client.get_requests(service_name='marketplace', api_name='UpdateAcceptedAgreement')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.marketplace.MarketplaceClient(config, service_endpoint=service_endpoint)
            response = client.update_accepted_agreement(
                accepted_agreement_id=request.pop(util.camelize('acceptedAgreementId')),
                update_accepted_agreement_details=request.pop(util.camelize('UpdateAcceptedAgreementDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'marketplace',
            'UpdateAcceptedAgreement',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'acceptedAgreement',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_marketplace_seattle_us_grp@oracle.com" jiraProject="MAR" opsJiraProject="CMP"
def test_update_publication(testing_service_client):
    if not testing_service_client.is_api_enabled('marketplace', 'UpdatePublication'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('marketplace', util.camelize('marketplace'), 'UpdatePublication')
    )

    request_containers = testing_service_client.get_requests(service_name='marketplace', api_name='UpdatePublication')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.marketplace.MarketplaceClient(config, service_endpoint=service_endpoint)
            response = client.update_publication(
                publication_id=request.pop(util.camelize('publicationId')),
                update_publication_details=request.pop(util.camelize('UpdatePublicationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'marketplace',
            'UpdatePublication',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'publication',
            False,
            False
        )
