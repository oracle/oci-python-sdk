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

        cassette_location = os.path.join('generated', 'license_manager_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="oci_license_manager_ww_grp@oracle.com" jiraProject="LM" opsJiraProject="LM"
def test_bulk_upload_license_records(testing_service_client):
    if not testing_service_client.is_api_enabled('license_manager', 'BulkUploadLicenseRecords'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('license_manager', util.camelize('license_manager'), 'BulkUploadLicenseRecords')
    )

    request_containers = testing_service_client.get_requests(service_name='license_manager', api_name='BulkUploadLicenseRecords')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.license_manager.LicenseManagerClient(config, service_endpoint=service_endpoint)
            response = client.bulk_upload_license_records(
                bulk_upload_license_records_details=request.pop(util.camelize('BulkUploadLicenseRecordsDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'license_manager',
            'BulkUploadLicenseRecords',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bulkUploadResponse',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_license_manager_ww_grp@oracle.com" jiraProject="LM" opsJiraProject="LM"
def test_create_license_record(testing_service_client):
    if not testing_service_client.is_api_enabled('license_manager', 'CreateLicenseRecord'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('license_manager', util.camelize('license_manager'), 'CreateLicenseRecord')
    )

    request_containers = testing_service_client.get_requests(service_name='license_manager', api_name='CreateLicenseRecord')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.license_manager.LicenseManagerClient(config, service_endpoint=service_endpoint)
            response = client.create_license_record(
                create_license_record_details=request.pop(util.camelize('CreateLicenseRecordDetails')),
                product_license_id=request.pop(util.camelize('productLicenseId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'license_manager',
            'CreateLicenseRecord',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'licenseRecord',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_license_manager_ww_grp@oracle.com" jiraProject="LM" opsJiraProject="LM"
def test_create_product_license(testing_service_client):
    if not testing_service_client.is_api_enabled('license_manager', 'CreateProductLicense'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('license_manager', util.camelize('license_manager'), 'CreateProductLicense')
    )

    request_containers = testing_service_client.get_requests(service_name='license_manager', api_name='CreateProductLicense')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.license_manager.LicenseManagerClient(config, service_endpoint=service_endpoint)
            response = client.create_product_license(
                create_product_license_details=request.pop(util.camelize('CreateProductLicenseDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'license_manager',
            'CreateProductLicense',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'productLicense',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_license_manager_ww_grp@oracle.com" jiraProject="LM" opsJiraProject="LM"
def test_delete_license_record(testing_service_client):
    if not testing_service_client.is_api_enabled('license_manager', 'DeleteLicenseRecord'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('license_manager', util.camelize('license_manager'), 'DeleteLicenseRecord')
    )

    request_containers = testing_service_client.get_requests(service_name='license_manager', api_name='DeleteLicenseRecord')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.license_manager.LicenseManagerClient(config, service_endpoint=service_endpoint)
            response = client.delete_license_record(
                license_record_id=request.pop(util.camelize('licenseRecordId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'license_manager',
            'DeleteLicenseRecord',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_license_record',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_license_manager_ww_grp@oracle.com" jiraProject="LM" opsJiraProject="LM"
def test_delete_product_license(testing_service_client):
    if not testing_service_client.is_api_enabled('license_manager', 'DeleteProductLicense'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('license_manager', util.camelize('license_manager'), 'DeleteProductLicense')
    )

    request_containers = testing_service_client.get_requests(service_name='license_manager', api_name='DeleteProductLicense')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.license_manager.LicenseManagerClient(config, service_endpoint=service_endpoint)
            response = client.delete_product_license(
                product_license_id=request.pop(util.camelize('productLicenseId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'license_manager',
            'DeleteProductLicense',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_product_license',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_license_manager_ww_grp@oracle.com" jiraProject="LM" opsJiraProject="LM"
def test_get_bulk_upload_template(testing_service_client):
    if not testing_service_client.is_api_enabled('license_manager', 'GetBulkUploadTemplate'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('license_manager', util.camelize('license_manager'), 'GetBulkUploadTemplate')
    )

    request_containers = testing_service_client.get_requests(service_name='license_manager', api_name='GetBulkUploadTemplate')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.license_manager.LicenseManagerClient(config, service_endpoint=service_endpoint)
            response = client.get_bulk_upload_template(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'license_manager',
            'GetBulkUploadTemplate',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bulkUploadTemplate',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_license_manager_ww_grp@oracle.com" jiraProject="LM" opsJiraProject="LM"
def test_get_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('license_manager', 'GetConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('license_manager', util.camelize('license_manager'), 'GetConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='license_manager', api_name='GetConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.license_manager.LicenseManagerClient(config, service_endpoint=service_endpoint)
            response = client.get_configuration(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'license_manager',
            'GetConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'configuration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_license_manager_ww_grp@oracle.com" jiraProject="LM" opsJiraProject="LM"
def test_get_license_metric(testing_service_client):
    if not testing_service_client.is_api_enabled('license_manager', 'GetLicenseMetric'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('license_manager', util.camelize('license_manager'), 'GetLicenseMetric')
    )

    request_containers = testing_service_client.get_requests(service_name='license_manager', api_name='GetLicenseMetric')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.license_manager.LicenseManagerClient(config, service_endpoint=service_endpoint)
            response = client.get_license_metric(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'license_manager',
            'GetLicenseMetric',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'licenseMetric',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_license_manager_ww_grp@oracle.com" jiraProject="LM" opsJiraProject="LM"
def test_get_license_record(testing_service_client):
    if not testing_service_client.is_api_enabled('license_manager', 'GetLicenseRecord'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('license_manager', util.camelize('license_manager'), 'GetLicenseRecord')
    )

    request_containers = testing_service_client.get_requests(service_name='license_manager', api_name='GetLicenseRecord')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.license_manager.LicenseManagerClient(config, service_endpoint=service_endpoint)
            response = client.get_license_record(
                license_record_id=request.pop(util.camelize('licenseRecordId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'license_manager',
            'GetLicenseRecord',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'licenseRecord',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_license_manager_ww_grp@oracle.com" jiraProject="LM" opsJiraProject="LM"
def test_get_product_license(testing_service_client):
    if not testing_service_client.is_api_enabled('license_manager', 'GetProductLicense'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('license_manager', util.camelize('license_manager'), 'GetProductLicense')
    )

    request_containers = testing_service_client.get_requests(service_name='license_manager', api_name='GetProductLicense')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.license_manager.LicenseManagerClient(config, service_endpoint=service_endpoint)
            response = client.get_product_license(
                product_license_id=request.pop(util.camelize('productLicenseId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'license_manager',
            'GetProductLicense',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'productLicense',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_license_manager_ww_grp@oracle.com" jiraProject="LM" opsJiraProject="LM"
def test_list_license_records(testing_service_client):
    if not testing_service_client.is_api_enabled('license_manager', 'ListLicenseRecords'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('license_manager', util.camelize('license_manager'), 'ListLicenseRecords')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='license_manager', api_name='ListLicenseRecords')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.license_manager.LicenseManagerClient(config, service_endpoint=service_endpoint)
            response = client.list_license_records(
                product_license_id=request.pop(util.camelize('productLicenseId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_license_records(
                    product_license_id=request.pop(util.camelize('productLicenseId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_license_records(
                        product_license_id=request.pop(util.camelize('productLicenseId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'license_manager',
            'ListLicenseRecords',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'licenseRecordCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_license_manager_ww_grp@oracle.com" jiraProject="LM" opsJiraProject="LM"
def test_list_product_license_consumers(testing_service_client):
    if not testing_service_client.is_api_enabled('license_manager', 'ListProductLicenseConsumers'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('license_manager', util.camelize('license_manager'), 'ListProductLicenseConsumers')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='license_manager', api_name='ListProductLicenseConsumers')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.license_manager.LicenseManagerClient(config, service_endpoint=service_endpoint)
            response = client.list_product_license_consumers(
                product_license_id=request.pop(util.camelize('productLicenseId')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_product_license_consumers(
                    product_license_id=request.pop(util.camelize('productLicenseId')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_product_license_consumers(
                        product_license_id=request.pop(util.camelize('productLicenseId')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'license_manager',
            'ListProductLicenseConsumers',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'productLicenseConsumerCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_license_manager_ww_grp@oracle.com" jiraProject="LM" opsJiraProject="LM"
def test_list_product_licenses(testing_service_client):
    if not testing_service_client.is_api_enabled('license_manager', 'ListProductLicenses'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('license_manager', util.camelize('license_manager'), 'ListProductLicenses')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='license_manager', api_name='ListProductLicenses')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.license_manager.LicenseManagerClient(config, service_endpoint=service_endpoint)
            response = client.list_product_licenses(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_product_licenses(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_product_licenses(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'license_manager',
            'ListProductLicenses',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'productLicenseCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_license_manager_ww_grp@oracle.com" jiraProject="LM" opsJiraProject="LM"
def test_list_top_utilized_product_licenses(testing_service_client):
    if not testing_service_client.is_api_enabled('license_manager', 'ListTopUtilizedProductLicenses'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('license_manager', util.camelize('license_manager'), 'ListTopUtilizedProductLicenses')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='license_manager', api_name='ListTopUtilizedProductLicenses')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.license_manager.LicenseManagerClient(config, service_endpoint=service_endpoint)
            response = client.list_top_utilized_product_licenses(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_top_utilized_product_licenses(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_top_utilized_product_licenses(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'license_manager',
            'ListTopUtilizedProductLicenses',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'topUtilizedProductLicenseCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_license_manager_ww_grp@oracle.com" jiraProject="LM" opsJiraProject="LM"
def test_list_top_utilized_resources(testing_service_client):
    if not testing_service_client.is_api_enabled('license_manager', 'ListTopUtilizedResources'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('license_manager', util.camelize('license_manager'), 'ListTopUtilizedResources')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='license_manager', api_name='ListTopUtilizedResources')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.license_manager.LicenseManagerClient(config, service_endpoint=service_endpoint)
            response = client.list_top_utilized_resources(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_top_utilized_resources(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_top_utilized_resources(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'license_manager',
            'ListTopUtilizedResources',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'topUtilizedResourceCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_license_manager_ww_grp@oracle.com" jiraProject="LM" opsJiraProject="LM"
def test_update_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('license_manager', 'UpdateConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('license_manager', util.camelize('license_manager'), 'UpdateConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='license_manager', api_name='UpdateConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.license_manager.LicenseManagerClient(config, service_endpoint=service_endpoint)
            response = client.update_configuration(
                compartment_id=request.pop(util.camelize('compartmentId')),
                update_configuration_details=request.pop(util.camelize('UpdateConfigurationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'license_manager',
            'UpdateConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'configuration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_license_manager_ww_grp@oracle.com" jiraProject="LM" opsJiraProject="LM"
def test_update_license_record(testing_service_client):
    if not testing_service_client.is_api_enabled('license_manager', 'UpdateLicenseRecord'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('license_manager', util.camelize('license_manager'), 'UpdateLicenseRecord')
    )

    request_containers = testing_service_client.get_requests(service_name='license_manager', api_name='UpdateLicenseRecord')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.license_manager.LicenseManagerClient(config, service_endpoint=service_endpoint)
            response = client.update_license_record(
                license_record_id=request.pop(util.camelize('licenseRecordId')),
                update_license_record_details=request.pop(util.camelize('UpdateLicenseRecordDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'license_manager',
            'UpdateLicenseRecord',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'licenseRecord',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_license_manager_ww_grp@oracle.com" jiraProject="LM" opsJiraProject="LM"
def test_update_product_license(testing_service_client):
    if not testing_service_client.is_api_enabled('license_manager', 'UpdateProductLicense'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('license_manager', util.camelize('license_manager'), 'UpdateProductLicense')
    )

    request_containers = testing_service_client.get_requests(service_name='license_manager', api_name='UpdateProductLicense')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.license_manager.LicenseManagerClient(config, service_endpoint=service_endpoint)
            response = client.update_product_license(
                product_license_id=request.pop(util.camelize('productLicenseId')),
                update_product_license_details=request.pop(util.camelize('UpdateProductLicenseDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'license_manager',
            'UpdateProductLicense',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'productLicense',
            False,
            False
        )
