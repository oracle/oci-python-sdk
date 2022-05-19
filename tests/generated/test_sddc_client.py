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

        cassette_location = os.path.join('generated', 'ocvp_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="sic_ocvp_us_grp@oracle.com" jiraProject="OCVP" opsJiraProject="OCVP"
def test_cancel_downgrade_hcx(testing_service_client):
    if not testing_service_client.is_api_enabled('ocvp', 'CancelDowngradeHcx'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ocvp', util.camelize('sddc'), 'CancelDowngradeHcx')
    )

    request_containers = testing_service_client.get_requests(service_name='ocvp', api_name='CancelDowngradeHcx')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ocvp.SddcClient(config, service_endpoint=service_endpoint)
            response = client.cancel_downgrade_hcx(
                sddc_id=request.pop(util.camelize('sddcId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ocvp',
            'CancelDowngradeHcx',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cancel_downgrade_hcx',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_ocvp_us_grp@oracle.com" jiraProject="OCVP" opsJiraProject="OCVP"
def test_change_sddc_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('ocvp', 'ChangeSddcCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ocvp', util.camelize('sddc'), 'ChangeSddcCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='ocvp', api_name='ChangeSddcCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ocvp.SddcClient(config, service_endpoint=service_endpoint)
            response = client.change_sddc_compartment(
                sddc_id=request.pop(util.camelize('sddcId')),
                change_sddc_compartment_details=request.pop(util.camelize('ChangeSddcCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ocvp',
            'ChangeSddcCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_sddc_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_ocvp_us_grp@oracle.com" jiraProject="OCVP" opsJiraProject="OCVP"
def test_create_sddc(testing_service_client):
    if not testing_service_client.is_api_enabled('ocvp', 'CreateSddc'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ocvp', util.camelize('sddc'), 'CreateSddc')
    )

    request_containers = testing_service_client.get_requests(service_name='ocvp', api_name='CreateSddc')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ocvp.SddcClient(config, service_endpoint=service_endpoint)
            response = client.create_sddc(
                create_sddc_details=request.pop(util.camelize('CreateSddcDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ocvp',
            'CreateSddc',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_sddc',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_ocvp_us_grp@oracle.com" jiraProject="OCVP" opsJiraProject="OCVP"
def test_delete_sddc(testing_service_client):
    if not testing_service_client.is_api_enabled('ocvp', 'DeleteSddc'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ocvp', util.camelize('sddc'), 'DeleteSddc')
    )

    request_containers = testing_service_client.get_requests(service_name='ocvp', api_name='DeleteSddc')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ocvp.SddcClient(config, service_endpoint=service_endpoint)
            response = client.delete_sddc(
                sddc_id=request.pop(util.camelize('sddcId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ocvp',
            'DeleteSddc',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_sddc',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="sic_ocvp_us_grp@oracle.com" jiraProject="OCVP" opsJiraProject="OCVP"
def test_downgrade_hcx(testing_service_client):
    if not testing_service_client.is_api_enabled('ocvp', 'DowngradeHcx'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ocvp', util.camelize('sddc'), 'DowngradeHcx')
    )

    request_containers = testing_service_client.get_requests(service_name='ocvp', api_name='DowngradeHcx')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ocvp.SddcClient(config, service_endpoint=service_endpoint)
            response = client.downgrade_hcx(
                downgrade_hcx_details=request.pop(util.camelize('DowngradeHcxDetails')),
                sddc_id=request.pop(util.camelize('sddcId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ocvp',
            'DowngradeHcx',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'downgrade_hcx',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_ocvp_us_grp@oracle.com" jiraProject="OCVP" opsJiraProject="OCVP"
def test_get_sddc(testing_service_client):
    if not testing_service_client.is_api_enabled('ocvp', 'GetSddc'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ocvp', util.camelize('sddc'), 'GetSddc')
    )

    request_containers = testing_service_client.get_requests(service_name='ocvp', api_name='GetSddc')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ocvp.SddcClient(config, service_endpoint=service_endpoint)
            response = client.get_sddc(
                sddc_id=request.pop(util.camelize('sddcId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ocvp',
            'GetSddc',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sddc',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_ocvp_us_grp@oracle.com" jiraProject="OCVP" opsJiraProject="OCVP"
def test_list_sddcs(testing_service_client):
    if not testing_service_client.is_api_enabled('ocvp', 'ListSddcs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ocvp', util.camelize('sddc'), 'ListSddcs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='ocvp', api_name='ListSddcs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ocvp.SddcClient(config, service_endpoint=service_endpoint)
            response = client.list_sddcs(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_sddcs(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_sddcs(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ocvp',
            'ListSddcs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sddcCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sic_ocvp_us_grp@oracle.com" jiraProject="OCVP" opsJiraProject="OCVP"
def test_list_supported_host_shapes(testing_service_client):
    if not testing_service_client.is_api_enabled('ocvp', 'ListSupportedHostShapes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ocvp', util.camelize('sddc'), 'ListSupportedHostShapes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='ocvp', api_name='ListSupportedHostShapes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ocvp.SddcClient(config, service_endpoint=service_endpoint)
            response = client.list_supported_host_shapes(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_supported_host_shapes(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_supported_host_shapes(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ocvp',
            'ListSupportedHostShapes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'supportedHostShapeCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sic_ocvp_us_grp@oracle.com" jiraProject="OCVP" opsJiraProject="OCVP"
def test_list_supported_skus(testing_service_client):
    if not testing_service_client.is_api_enabled('ocvp', 'ListSupportedSkus'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ocvp', util.camelize('sddc'), 'ListSupportedSkus')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='ocvp', api_name='ListSupportedSkus')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ocvp.SddcClient(config, service_endpoint=service_endpoint)
            response = client.list_supported_skus(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_supported_skus(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_supported_skus(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ocvp',
            'ListSupportedSkus',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'supportedSkuSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sic_ocvp_us_grp@oracle.com" jiraProject="OCVP" opsJiraProject="OCVP"
def test_list_supported_vmware_software_versions(testing_service_client):
    if not testing_service_client.is_api_enabled('ocvp', 'ListSupportedVmwareSoftwareVersions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ocvp', util.camelize('sddc'), 'ListSupportedVmwareSoftwareVersions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='ocvp', api_name='ListSupportedVmwareSoftwareVersions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ocvp.SddcClient(config, service_endpoint=service_endpoint)
            response = client.list_supported_vmware_software_versions(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_supported_vmware_software_versions(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_supported_vmware_software_versions(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ocvp',
            'ListSupportedVmwareSoftwareVersions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'supportedVmwareSoftwareVersionCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sic_ocvp_us_grp@oracle.com" jiraProject="OCVP" opsJiraProject="OCVP"
def test_refresh_hcx_license_status(testing_service_client):
    if not testing_service_client.is_api_enabled('ocvp', 'RefreshHcxLicenseStatus'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ocvp', util.camelize('sddc'), 'RefreshHcxLicenseStatus')
    )

    request_containers = testing_service_client.get_requests(service_name='ocvp', api_name='RefreshHcxLicenseStatus')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ocvp.SddcClient(config, service_endpoint=service_endpoint)
            response = client.refresh_hcx_license_status(
                sddc_id=request.pop(util.camelize('sddcId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ocvp',
            'RefreshHcxLicenseStatus',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'refresh_hcx_license_status',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_ocvp_us_grp@oracle.com" jiraProject="OCVP" opsJiraProject="OCVP"
def test_update_sddc(testing_service_client):
    if not testing_service_client.is_api_enabled('ocvp', 'UpdateSddc'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ocvp', util.camelize('sddc'), 'UpdateSddc')
    )

    request_containers = testing_service_client.get_requests(service_name='ocvp', api_name='UpdateSddc')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ocvp.SddcClient(config, service_endpoint=service_endpoint)
            response = client.update_sddc(
                sddc_id=request.pop(util.camelize('sddcId')),
                update_sddc_details=request.pop(util.camelize('UpdateSddcDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ocvp',
            'UpdateSddc',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sddc',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_ocvp_us_grp@oracle.com" jiraProject="OCVP" opsJiraProject="OCVP"
def test_upgrade_hcx(testing_service_client):
    if not testing_service_client.is_api_enabled('ocvp', 'UpgradeHcx'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ocvp', util.camelize('sddc'), 'UpgradeHcx')
    )

    request_containers = testing_service_client.get_requests(service_name='ocvp', api_name='UpgradeHcx')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ocvp.SddcClient(config, service_endpoint=service_endpoint)
            response = client.upgrade_hcx(
                sddc_id=request.pop(util.camelize('sddcId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ocvp',
            'UpgradeHcx',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'upgrade_hcx',
            False,
            False
        )
