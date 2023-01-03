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

        cassette_location = os.path.join('generated', 'oda_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_create_imported_package(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'CreateImportedPackage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('odapackage'), 'CreateImportedPackage')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='CreateImportedPackage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.OdapackageClient(config, service_endpoint=service_endpoint)
            response = client.create_imported_package(
                create_imported_package_details=request.pop(util.camelize('CreateImportedPackageDetails')),
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'CreateImportedPackage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'importedPackage',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_delete_imported_package(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'DeleteImportedPackage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('odapackage'), 'DeleteImportedPackage')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='DeleteImportedPackage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.OdapackageClient(config, service_endpoint=service_endpoint)
            response = client.delete_imported_package(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                package_id=request.pop(util.camelize('packageId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'DeleteImportedPackage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_imported_package',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_get_imported_package(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'GetImportedPackage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('odapackage'), 'GetImportedPackage')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='GetImportedPackage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.OdapackageClient(config, service_endpoint=service_endpoint)
            response = client.get_imported_package(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                package_id=request.pop(util.camelize('packageId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'GetImportedPackage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'importedPackage',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_get_package(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'GetPackage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('odapackage'), 'GetPackage')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='GetPackage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.OdapackageClient(config, service_endpoint=service_endpoint)
            response = client.get_package(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                package_id=request.pop(util.camelize('packageId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'GetPackage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'package',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_list_imported_packages(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'ListImportedPackages'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('odapackage'), 'ListImportedPackages')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='ListImportedPackages')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.OdapackageClient(config, service_endpoint=service_endpoint)
            response = client.list_imported_packages(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_imported_packages(
                    oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_imported_packages(
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
            'ListImportedPackages',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'importedPackageSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_list_packages(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'ListPackages'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('odapackage'), 'ListPackages')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='ListPackages')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.OdapackageClient(config, service_endpoint=service_endpoint)
            response = client.list_packages(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_packages(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_packages(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'ListPackages',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'packageSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_update_imported_package(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'UpdateImportedPackage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('odapackage'), 'UpdateImportedPackage')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='UpdateImportedPackage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.OdapackageClient(config, service_endpoint=service_endpoint)
            response = client.update_imported_package(
                update_imported_package_details=request.pop(util.camelize('UpdateImportedPackageDetails')),
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                package_id=request.pop(util.camelize('packageId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'UpdateImportedPackage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'importedPackage',
            False,
            False
        )
