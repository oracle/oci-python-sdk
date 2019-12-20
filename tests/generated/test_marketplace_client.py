# Code generated. DO NOT EDIT.
# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

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
                signature=request.pop(util.camelize('signature')),
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
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_accepted_agreements(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_accepted_agreements(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
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
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_categories(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_categories(
                        page=next_response.headers[prev_page],
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
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_listings(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_listings(
                        page=next_response.headers[prev_page],
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
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_packages(
                    listing_id=request.pop(util.camelize('listingId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_packages(
                        listing_id=request.pop(util.camelize('listingId')),
                        page=next_response.headers[prev_page],
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
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_publishers(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_publishers(
                        page=next_response.headers[prev_page],
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
