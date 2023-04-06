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

        cassette_location = os.path.join('generated', 'data_safe_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_activate_target_database(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ActivateTargetDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ActivateTargetDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ActivateTargetDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.activate_target_database(
                activate_target_database_details=request.pop(util.camelize('ActivateTargetDatabaseDetails')),
                target_database_id=request.pop(util.camelize('targetDatabaseId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ActivateTargetDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'activate_target_database',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_add_masking_columns_from_sdm(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'AddMaskingColumnsFromSdm'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'AddMaskingColumnsFromSdm')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='AddMaskingColumnsFromSdm')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.add_masking_columns_from_sdm(
                masking_policy_id=request.pop(util.camelize('maskingPolicyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'AddMaskingColumnsFromSdm',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'add_masking_columns_from_sdm',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_alerts_update(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'AlertsUpdate'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'AlertsUpdate')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='AlertsUpdate')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.alerts_update(
                alerts_update_details=request.pop(util.camelize('AlertsUpdateDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'AlertsUpdate',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'alerts_update',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_apply_discovery_job_results(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ApplyDiscoveryJobResults'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ApplyDiscoveryJobResults')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ApplyDiscoveryJobResults')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.apply_discovery_job_results(
                sensitive_data_model_id=request.pop(util.camelize('sensitiveDataModelId')),
                apply_discovery_job_results_details=request.pop(util.camelize('ApplyDiscoveryJobResultsDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ApplyDiscoveryJobResults',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'apply_discovery_job_results',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_apply_sdm_masking_policy_difference(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ApplySdmMaskingPolicyDifference'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ApplySdmMaskingPolicyDifference')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ApplySdmMaskingPolicyDifference')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.apply_sdm_masking_policy_difference(
                masking_policy_id=request.pop(util.camelize('maskingPolicyId')),
                apply_sdm_masking_policy_difference_details=request.pop(util.camelize('ApplySdmMaskingPolicyDifferenceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ApplySdmMaskingPolicyDifference',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'apply_sdm_masking_policy_difference',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_calculate_audit_volume_available(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'CalculateAuditVolumeAvailable'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'CalculateAuditVolumeAvailable')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='CalculateAuditVolumeAvailable')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.calculate_audit_volume_available(
                audit_profile_id=request.pop(util.camelize('auditProfileId')),
                calculate_audit_volume_available_details=request.pop(util.camelize('CalculateAuditVolumeAvailableDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'CalculateAuditVolumeAvailable',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'calculate_audit_volume_available',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_calculate_audit_volume_collected(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'CalculateAuditVolumeCollected'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'CalculateAuditVolumeCollected')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='CalculateAuditVolumeCollected')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.calculate_audit_volume_collected(
                audit_profile_id=request.pop(util.camelize('auditProfileId')),
                calculate_audit_volume_collected_details=request.pop(util.camelize('CalculateAuditVolumeCollectedDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'CalculateAuditVolumeCollected',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'calculate_audit_volume_collected',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_cancel_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'CancelWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'CancelWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='CancelWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.cancel_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'CancelWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cancel_work_request',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_change_alert_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ChangeAlertCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ChangeAlertCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ChangeAlertCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.change_alert_compartment(
                alert_id=request.pop(util.camelize('alertId')),
                change_alert_compartment_details=request.pop(util.camelize('ChangeAlertCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ChangeAlertCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_alert_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_change_audit_archive_retrieval_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ChangeAuditArchiveRetrievalCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ChangeAuditArchiveRetrievalCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ChangeAuditArchiveRetrievalCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.change_audit_archive_retrieval_compartment(
                audit_archive_retrieval_id=request.pop(util.camelize('auditArchiveRetrievalId')),
                change_audit_archive_retrieval_compartment_details=request.pop(util.camelize('ChangeAuditArchiveRetrievalCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ChangeAuditArchiveRetrievalCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_audit_archive_retrieval_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_change_audit_policy_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ChangeAuditPolicyCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ChangeAuditPolicyCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ChangeAuditPolicyCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.change_audit_policy_compartment(
                audit_policy_id=request.pop(util.camelize('auditPolicyId')),
                change_audit_policy_compartment_details=request.pop(util.camelize('ChangeAuditPolicyCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ChangeAuditPolicyCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_audit_policy_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_change_audit_profile_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ChangeAuditProfileCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ChangeAuditProfileCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ChangeAuditProfileCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.change_audit_profile_compartment(
                audit_profile_id=request.pop(util.camelize('auditProfileId')),
                change_audit_profile_compartment_details=request.pop(util.camelize('ChangeAuditProfileCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ChangeAuditProfileCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_audit_profile_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_change_data_safe_private_endpoint_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ChangeDataSafePrivateEndpointCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ChangeDataSafePrivateEndpointCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ChangeDataSafePrivateEndpointCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.change_data_safe_private_endpoint_compartment(
                data_safe_private_endpoint_id=request.pop(util.camelize('dataSafePrivateEndpointId')),
                change_data_safe_private_endpoint_compartment_details=request.pop(util.camelize('ChangeDataSafePrivateEndpointCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ChangeDataSafePrivateEndpointCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_data_safe_private_endpoint_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_change_discovery_job_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ChangeDiscoveryJobCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ChangeDiscoveryJobCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ChangeDiscoveryJobCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.change_discovery_job_compartment(
                discovery_job_id=request.pop(util.camelize('discoveryJobId')),
                change_discovery_job_compartment_details=request.pop(util.camelize('ChangeDiscoveryJobCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ChangeDiscoveryJobCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_discovery_job_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_change_library_masking_format_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ChangeLibraryMaskingFormatCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ChangeLibraryMaskingFormatCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ChangeLibraryMaskingFormatCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.change_library_masking_format_compartment(
                library_masking_format_id=request.pop(util.camelize('libraryMaskingFormatId')),
                change_library_masking_format_compartment_details=request.pop(util.camelize('ChangeLibraryMaskingFormatCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ChangeLibraryMaskingFormatCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_library_masking_format_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_change_masking_policy_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ChangeMaskingPolicyCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ChangeMaskingPolicyCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ChangeMaskingPolicyCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.change_masking_policy_compartment(
                masking_policy_id=request.pop(util.camelize('maskingPolicyId')),
                change_masking_policy_compartment_details=request.pop(util.camelize('ChangeMaskingPolicyCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ChangeMaskingPolicyCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_masking_policy_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_change_on_prem_connector_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ChangeOnPremConnectorCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ChangeOnPremConnectorCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ChangeOnPremConnectorCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.change_on_prem_connector_compartment(
                on_prem_connector_id=request.pop(util.camelize('onPremConnectorId')),
                change_on_prem_connector_compartment_details=request.pop(util.camelize('ChangeOnPremConnectorCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ChangeOnPremConnectorCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_on_prem_connector_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_change_report_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ChangeReportCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ChangeReportCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ChangeReportCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.change_report_compartment(
                report_id=request.pop(util.camelize('reportId')),
                change_report_compartment_details=request.pop(util.camelize('ChangeReportCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ChangeReportCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_report_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_change_report_definition_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ChangeReportDefinitionCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ChangeReportDefinitionCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ChangeReportDefinitionCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.change_report_definition_compartment(
                report_definition_id=request.pop(util.camelize('reportDefinitionId')),
                change_report_definition_compartment_details=request.pop(util.camelize('ChangeReportDefinitionCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ChangeReportDefinitionCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_report_definition_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_change_retention(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ChangeRetention'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ChangeRetention')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ChangeRetention')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.change_retention(
                audit_profile_id=request.pop(util.camelize('auditProfileId')),
                change_retention_details=request.pop(util.camelize('ChangeRetentionDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ChangeRetention',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_retention',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_change_sdm_masking_policy_difference_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ChangeSdmMaskingPolicyDifferenceCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ChangeSdmMaskingPolicyDifferenceCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ChangeSdmMaskingPolicyDifferenceCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.change_sdm_masking_policy_difference_compartment(
                sdm_masking_policy_difference_id=request.pop(util.camelize('sdmMaskingPolicyDifferenceId')),
                change_sdm_masking_policy_difference_compartment_details=request.pop(util.camelize('ChangeSdmMaskingPolicyDifferenceCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ChangeSdmMaskingPolicyDifferenceCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_sdm_masking_policy_difference_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_change_security_assessment_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ChangeSecurityAssessmentCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ChangeSecurityAssessmentCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ChangeSecurityAssessmentCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.change_security_assessment_compartment(
                security_assessment_id=request.pop(util.camelize('securityAssessmentId')),
                change_security_assessment_compartment_details=request.pop(util.camelize('ChangeSecurityAssessmentCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ChangeSecurityAssessmentCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_security_assessment_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_change_sensitive_data_model_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ChangeSensitiveDataModelCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ChangeSensitiveDataModelCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ChangeSensitiveDataModelCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.change_sensitive_data_model_compartment(
                sensitive_data_model_id=request.pop(util.camelize('sensitiveDataModelId')),
                change_sensitive_data_model_compartment_details=request.pop(util.camelize('ChangeSensitiveDataModelCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ChangeSensitiveDataModelCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_sensitive_data_model_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_change_sensitive_type_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ChangeSensitiveTypeCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ChangeSensitiveTypeCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ChangeSensitiveTypeCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.change_sensitive_type_compartment(
                sensitive_type_id=request.pop(util.camelize('sensitiveTypeId')),
                change_sensitive_type_compartment_details=request.pop(util.camelize('ChangeSensitiveTypeCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ChangeSensitiveTypeCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_sensitive_type_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_change_target_alert_policy_association_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ChangeTargetAlertPolicyAssociationCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ChangeTargetAlertPolicyAssociationCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ChangeTargetAlertPolicyAssociationCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.change_target_alert_policy_association_compartment(
                target_alert_policy_association_id=request.pop(util.camelize('targetAlertPolicyAssociationId')),
                change_target_alert_policy_association_compartment_details=request.pop(util.camelize('ChangeTargetAlertPolicyAssociationCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ChangeTargetAlertPolicyAssociationCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_target_alert_policy_association_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_change_target_database_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ChangeTargetDatabaseCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ChangeTargetDatabaseCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ChangeTargetDatabaseCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.change_target_database_compartment(
                target_database_id=request.pop(util.camelize('targetDatabaseId')),
                change_target_database_compartment_details=request.pop(util.camelize('ChangeTargetDatabaseCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ChangeTargetDatabaseCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_target_database_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_change_user_assessment_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ChangeUserAssessmentCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ChangeUserAssessmentCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ChangeUserAssessmentCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.change_user_assessment_compartment(
                user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                change_user_assessment_compartment_details=request.pop(util.camelize('ChangeUserAssessmentCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ChangeUserAssessmentCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_user_assessment_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_compare_security_assessment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'CompareSecurityAssessment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'CompareSecurityAssessment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='CompareSecurityAssessment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.compare_security_assessment(
                security_assessment_id=request.pop(util.camelize('securityAssessmentId')),
                compare_security_assessment_details=request.pop(util.camelize('CompareSecurityAssessmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'CompareSecurityAssessment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'compare_security_assessment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_compare_user_assessment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'CompareUserAssessment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'CompareUserAssessment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='CompareUserAssessment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.compare_user_assessment(
                user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                compare_user_assessment_details=request.pop(util.camelize('CompareUserAssessmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'CompareUserAssessment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'compare_user_assessment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_create_audit_archive_retrieval(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'CreateAuditArchiveRetrieval'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'CreateAuditArchiveRetrieval')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='CreateAuditArchiveRetrieval')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.create_audit_archive_retrieval(
                create_audit_archive_retrieval_details=request.pop(util.camelize('CreateAuditArchiveRetrievalDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'CreateAuditArchiveRetrieval',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'auditArchiveRetrieval',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_create_data_safe_private_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'CreateDataSafePrivateEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'CreateDataSafePrivateEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='CreateDataSafePrivateEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.create_data_safe_private_endpoint(
                create_data_safe_private_endpoint_details=request.pop(util.camelize('CreateDataSafePrivateEndpointDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'CreateDataSafePrivateEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataSafePrivateEndpoint',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_create_discovery_job(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'CreateDiscoveryJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'CreateDiscoveryJob')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='CreateDiscoveryJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.create_discovery_job(
                create_discovery_job_details=request.pop(util.camelize('CreateDiscoveryJobDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'CreateDiscoveryJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'discoveryJob',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_create_library_masking_format(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'CreateLibraryMaskingFormat'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'CreateLibraryMaskingFormat')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='CreateLibraryMaskingFormat')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.create_library_masking_format(
                create_library_masking_format_details=request.pop(util.camelize('CreateLibraryMaskingFormatDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'CreateLibraryMaskingFormat',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'libraryMaskingFormat',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_create_masking_column(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'CreateMaskingColumn'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'CreateMaskingColumn')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='CreateMaskingColumn')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.create_masking_column(
                create_masking_column_details=request.pop(util.camelize('CreateMaskingColumnDetails')),
                masking_policy_id=request.pop(util.camelize('maskingPolicyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'CreateMaskingColumn',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_masking_column',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_create_masking_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'CreateMaskingPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'CreateMaskingPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='CreateMaskingPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.create_masking_policy(
                create_masking_policy_details=request.pop(util.camelize('CreateMaskingPolicyDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'CreateMaskingPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'maskingPolicy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_create_on_prem_connector(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'CreateOnPremConnector'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'CreateOnPremConnector')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='CreateOnPremConnector')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.create_on_prem_connector(
                create_on_prem_connector_details=request.pop(util.camelize('CreateOnPremConnectorDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'CreateOnPremConnector',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'onPremConnector',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_create_report_definition(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'CreateReportDefinition'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'CreateReportDefinition')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='CreateReportDefinition')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.create_report_definition(
                create_report_definition_details=request.pop(util.camelize('CreateReportDefinitionDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'CreateReportDefinition',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'reportDefinition',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_create_sdm_masking_policy_difference(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'CreateSdmMaskingPolicyDifference'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'CreateSdmMaskingPolicyDifference')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='CreateSdmMaskingPolicyDifference')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.create_sdm_masking_policy_difference(
                create_sdm_masking_policy_difference_details=request.pop(util.camelize('CreateSdmMaskingPolicyDifferenceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'CreateSdmMaskingPolicyDifference',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sdmMaskingPolicyDifference',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_create_security_assessment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'CreateSecurityAssessment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'CreateSecurityAssessment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='CreateSecurityAssessment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.create_security_assessment(
                create_security_assessment_details=request.pop(util.camelize('CreateSecurityAssessmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'CreateSecurityAssessment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'securityAssessment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_create_sensitive_column(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'CreateSensitiveColumn'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'CreateSensitiveColumn')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='CreateSensitiveColumn')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.create_sensitive_column(
                sensitive_data_model_id=request.pop(util.camelize('sensitiveDataModelId')),
                create_sensitive_column_details=request.pop(util.camelize('CreateSensitiveColumnDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'CreateSensitiveColumn',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_sensitive_column',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_create_sensitive_data_model(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'CreateSensitiveDataModel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'CreateSensitiveDataModel')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='CreateSensitiveDataModel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.create_sensitive_data_model(
                create_sensitive_data_model_details=request.pop(util.camelize('CreateSensitiveDataModelDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'CreateSensitiveDataModel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sensitiveDataModel',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_create_sensitive_type(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'CreateSensitiveType'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'CreateSensitiveType')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='CreateSensitiveType')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.create_sensitive_type(
                create_sensitive_type_details=request.pop(util.camelize('CreateSensitiveTypeDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'CreateSensitiveType',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sensitiveType',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_create_target_alert_policy_association(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'CreateTargetAlertPolicyAssociation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'CreateTargetAlertPolicyAssociation')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='CreateTargetAlertPolicyAssociation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.create_target_alert_policy_association(
                create_target_alert_policy_association_details=request.pop(util.camelize('CreateTargetAlertPolicyAssociationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'CreateTargetAlertPolicyAssociation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'targetAlertPolicyAssociation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_create_target_database(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'CreateTargetDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'CreateTargetDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='CreateTargetDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.create_target_database(
                create_target_database_details=request.pop(util.camelize('CreateTargetDatabaseDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'CreateTargetDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'targetDatabase',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_create_user_assessment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'CreateUserAssessment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'CreateUserAssessment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='CreateUserAssessment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.create_user_assessment(
                create_user_assessment_details=request.pop(util.camelize('CreateUserAssessmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'CreateUserAssessment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'userAssessment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_deactivate_target_database(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DeactivateTargetDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DeactivateTargetDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DeactivateTargetDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.deactivate_target_database(
                target_database_id=request.pop(util.camelize('targetDatabaseId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DeactivateTargetDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deactivate_target_database',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_delete_audit_archive_retrieval(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DeleteAuditArchiveRetrieval'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DeleteAuditArchiveRetrieval')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DeleteAuditArchiveRetrieval')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.delete_audit_archive_retrieval(
                audit_archive_retrieval_id=request.pop(util.camelize('auditArchiveRetrievalId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DeleteAuditArchiveRetrieval',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_audit_archive_retrieval',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_delete_audit_trail(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DeleteAuditTrail'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DeleteAuditTrail')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DeleteAuditTrail')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.delete_audit_trail(
                audit_trail_id=request.pop(util.camelize('auditTrailId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DeleteAuditTrail',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_audit_trail',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_delete_data_safe_private_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DeleteDataSafePrivateEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DeleteDataSafePrivateEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DeleteDataSafePrivateEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.delete_data_safe_private_endpoint(
                data_safe_private_endpoint_id=request.pop(util.camelize('dataSafePrivateEndpointId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DeleteDataSafePrivateEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_data_safe_private_endpoint',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_delete_discovery_job(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DeleteDiscoveryJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DeleteDiscoveryJob')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DeleteDiscoveryJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.delete_discovery_job(
                discovery_job_id=request.pop(util.camelize('discoveryJobId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DeleteDiscoveryJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_discovery_job',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_delete_discovery_job_result(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DeleteDiscoveryJobResult'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DeleteDiscoveryJobResult')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DeleteDiscoveryJobResult')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.delete_discovery_job_result(
                discovery_job_id=request.pop(util.camelize('discoveryJobId')),
                result_key=request.pop(util.camelize('resultKey')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DeleteDiscoveryJobResult',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_discovery_job_result',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_delete_library_masking_format(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DeleteLibraryMaskingFormat'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DeleteLibraryMaskingFormat')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DeleteLibraryMaskingFormat')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.delete_library_masking_format(
                library_masking_format_id=request.pop(util.camelize('libraryMaskingFormatId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DeleteLibraryMaskingFormat',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_library_masking_format',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_delete_masking_column(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DeleteMaskingColumn'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DeleteMaskingColumn')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DeleteMaskingColumn')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.delete_masking_column(
                masking_column_key=request.pop(util.camelize('maskingColumnKey')),
                masking_policy_id=request.pop(util.camelize('maskingPolicyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DeleteMaskingColumn',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_masking_column',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_delete_masking_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DeleteMaskingPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DeleteMaskingPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DeleteMaskingPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.delete_masking_policy(
                masking_policy_id=request.pop(util.camelize('maskingPolicyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DeleteMaskingPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_masking_policy',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_delete_on_prem_connector(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DeleteOnPremConnector'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DeleteOnPremConnector')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DeleteOnPremConnector')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.delete_on_prem_connector(
                on_prem_connector_id=request.pop(util.camelize('onPremConnectorId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DeleteOnPremConnector',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_on_prem_connector',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_delete_report_definition(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DeleteReportDefinition'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DeleteReportDefinition')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DeleteReportDefinition')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.delete_report_definition(
                report_definition_id=request.pop(util.camelize('reportDefinitionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DeleteReportDefinition',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_report_definition',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_delete_sdm_masking_policy_difference(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DeleteSdmMaskingPolicyDifference'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DeleteSdmMaskingPolicyDifference')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DeleteSdmMaskingPolicyDifference')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.delete_sdm_masking_policy_difference(
                sdm_masking_policy_difference_id=request.pop(util.camelize('sdmMaskingPolicyDifferenceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DeleteSdmMaskingPolicyDifference',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_sdm_masking_policy_difference',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_delete_security_assessment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DeleteSecurityAssessment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DeleteSecurityAssessment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DeleteSecurityAssessment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.delete_security_assessment(
                security_assessment_id=request.pop(util.camelize('securityAssessmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DeleteSecurityAssessment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_security_assessment',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_delete_sensitive_column(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DeleteSensitiveColumn'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DeleteSensitiveColumn')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DeleteSensitiveColumn')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.delete_sensitive_column(
                sensitive_data_model_id=request.pop(util.camelize('sensitiveDataModelId')),
                sensitive_column_key=request.pop(util.camelize('sensitiveColumnKey')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DeleteSensitiveColumn',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_sensitive_column',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_delete_sensitive_data_model(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DeleteSensitiveDataModel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DeleteSensitiveDataModel')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DeleteSensitiveDataModel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.delete_sensitive_data_model(
                sensitive_data_model_id=request.pop(util.camelize('sensitiveDataModelId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DeleteSensitiveDataModel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_sensitive_data_model',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_delete_sensitive_type(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DeleteSensitiveType'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DeleteSensitiveType')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DeleteSensitiveType')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.delete_sensitive_type(
                sensitive_type_id=request.pop(util.camelize('sensitiveTypeId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DeleteSensitiveType',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_sensitive_type',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_delete_target_alert_policy_association(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DeleteTargetAlertPolicyAssociation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DeleteTargetAlertPolicyAssociation')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DeleteTargetAlertPolicyAssociation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.delete_target_alert_policy_association(
                target_alert_policy_association_id=request.pop(util.camelize('targetAlertPolicyAssociationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DeleteTargetAlertPolicyAssociation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_target_alert_policy_association',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_delete_target_database(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DeleteTargetDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DeleteTargetDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DeleteTargetDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.delete_target_database(
                target_database_id=request.pop(util.camelize('targetDatabaseId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DeleteTargetDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_target_database',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_delete_user_assessment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DeleteUserAssessment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DeleteUserAssessment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DeleteUserAssessment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.delete_user_assessment(
                user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DeleteUserAssessment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_user_assessment',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_discover_audit_trails(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DiscoverAuditTrails'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DiscoverAuditTrails')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DiscoverAuditTrails')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.discover_audit_trails(
                audit_profile_id=request.pop(util.camelize('auditProfileId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DiscoverAuditTrails',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'discover_audit_trails',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_download_discovery_report(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DownloadDiscoveryReport'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DownloadDiscoveryReport')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DownloadDiscoveryReport')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.download_discovery_report(
                sensitive_data_model_id=request.pop(util.camelize('sensitiveDataModelId')),
                download_discovery_report_details=request.pop(util.camelize('DownloadDiscoveryReportDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DownloadDiscoveryReport',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_download_masking_log(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DownloadMaskingLog'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DownloadMaskingLog')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DownloadMaskingLog')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.download_masking_log(
                masking_policy_id=request.pop(util.camelize('maskingPolicyId')),
                download_masking_log_details=request.pop(util.camelize('DownloadMaskingLogDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DownloadMaskingLog',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_download_masking_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DownloadMaskingPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DownloadMaskingPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DownloadMaskingPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.download_masking_policy(
                masking_policy_id=request.pop(util.camelize('maskingPolicyId')),
                download_masking_policy_details=request.pop(util.camelize('DownloadMaskingPolicyDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DownloadMaskingPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_download_masking_report(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DownloadMaskingReport'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DownloadMaskingReport')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DownloadMaskingReport')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.download_masking_report(
                masking_policy_id=request.pop(util.camelize('maskingPolicyId')),
                download_masking_report_details=request.pop(util.camelize('DownloadMaskingReportDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DownloadMaskingReport',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_download_privilege_script(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DownloadPrivilegeScript'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DownloadPrivilegeScript')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DownloadPrivilegeScript')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.download_privilege_script(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DownloadPrivilegeScript',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_download_security_assessment_report(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DownloadSecurityAssessmentReport'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DownloadSecurityAssessmentReport')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DownloadSecurityAssessmentReport')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.download_security_assessment_report(
                security_assessment_id=request.pop(util.camelize('securityAssessmentId')),
                download_security_assessment_report_details=request.pop(util.camelize('DownloadSecurityAssessmentReportDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DownloadSecurityAssessmentReport',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_download_sensitive_data_model(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DownloadSensitiveDataModel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DownloadSensitiveDataModel')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DownloadSensitiveDataModel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.download_sensitive_data_model(
                sensitive_data_model_id=request.pop(util.camelize('sensitiveDataModelId')),
                download_sensitive_data_model_details=request.pop(util.camelize('DownloadSensitiveDataModelDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DownloadSensitiveDataModel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_download_user_assessment_report(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DownloadUserAssessmentReport'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DownloadUserAssessmentReport')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DownloadUserAssessmentReport')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.download_user_assessment_report(
                user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                download_user_assessment_report_details=request.pop(util.camelize('DownloadUserAssessmentReportDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DownloadUserAssessmentReport',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_enable_data_safe_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'EnableDataSafeConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'EnableDataSafeConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='EnableDataSafeConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.enable_data_safe_configuration(
                enable_data_safe_configuration_details=request.pop(util.camelize('EnableDataSafeConfigurationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'EnableDataSafeConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'enable_data_safe_configuration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_generate_discovery_report_for_download(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GenerateDiscoveryReportForDownload'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GenerateDiscoveryReportForDownload')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GenerateDiscoveryReportForDownload')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.generate_discovery_report_for_download(
                sensitive_data_model_id=request.pop(util.camelize('sensitiveDataModelId')),
                generate_discovery_report_for_download_details=request.pop(util.camelize('GenerateDiscoveryReportForDownloadDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GenerateDiscoveryReportForDownload',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'generate_discovery_report_for_download',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_generate_masking_policy_for_download(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GenerateMaskingPolicyForDownload'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GenerateMaskingPolicyForDownload')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GenerateMaskingPolicyForDownload')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.generate_masking_policy_for_download(
                masking_policy_id=request.pop(util.camelize('maskingPolicyId')),
                generate_masking_policy_for_download_details=request.pop(util.camelize('GenerateMaskingPolicyForDownloadDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GenerateMaskingPolicyForDownload',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'generate_masking_policy_for_download',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_generate_masking_report_for_download(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GenerateMaskingReportForDownload'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GenerateMaskingReportForDownload')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GenerateMaskingReportForDownload')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.generate_masking_report_for_download(
                masking_policy_id=request.pop(util.camelize('maskingPolicyId')),
                generate_masking_report_for_download_details=request.pop(util.camelize('GenerateMaskingReportForDownloadDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GenerateMaskingReportForDownload',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'generate_masking_report_for_download',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_generate_on_prem_connector_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GenerateOnPremConnectorConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GenerateOnPremConnectorConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GenerateOnPremConnectorConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.generate_on_prem_connector_configuration(
                generate_on_prem_connector_configuration_details=request.pop(util.camelize('GenerateOnPremConnectorConfigurationDetails')),
                on_prem_connector_id=request.pop(util.camelize('onPremConnectorId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GenerateOnPremConnectorConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_generate_report(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GenerateReport'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GenerateReport')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GenerateReport')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.generate_report(
                report_definition_id=request.pop(util.camelize('reportDefinitionId')),
                generate_report_details=request.pop(util.camelize('GenerateReportDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GenerateReport',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'generate_report',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_generate_security_assessment_report(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GenerateSecurityAssessmentReport'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GenerateSecurityAssessmentReport')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GenerateSecurityAssessmentReport')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.generate_security_assessment_report(
                security_assessment_id=request.pop(util.camelize('securityAssessmentId')),
                generate_security_assessment_report_details=request.pop(util.camelize('GenerateSecurityAssessmentReportDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GenerateSecurityAssessmentReport',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'generate_security_assessment_report',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_generate_sensitive_data_model_for_download(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GenerateSensitiveDataModelForDownload'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GenerateSensitiveDataModelForDownload')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GenerateSensitiveDataModelForDownload')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.generate_sensitive_data_model_for_download(
                sensitive_data_model_id=request.pop(util.camelize('sensitiveDataModelId')),
                generate_sensitive_data_model_for_download_details=request.pop(util.camelize('GenerateSensitiveDataModelForDownloadDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GenerateSensitiveDataModelForDownload',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'generate_sensitive_data_model_for_download',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_generate_user_assessment_report(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GenerateUserAssessmentReport'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GenerateUserAssessmentReport')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GenerateUserAssessmentReport')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.generate_user_assessment_report(
                user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                generate_user_assessment_report_details=request.pop(util.camelize('GenerateUserAssessmentReportDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GenerateUserAssessmentReport',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'generate_user_assessment_report',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_alert(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetAlert'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetAlert')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetAlert')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_alert(
                alert_id=request.pop(util.camelize('alertId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetAlert',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'alert',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_alert_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetAlertPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetAlertPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetAlertPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_alert_policy(
                alert_policy_id=request.pop(util.camelize('alertPolicyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetAlertPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'alertPolicy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_audit_archive_retrieval(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetAuditArchiveRetrieval'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetAuditArchiveRetrieval')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetAuditArchiveRetrieval')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_audit_archive_retrieval(
                audit_archive_retrieval_id=request.pop(util.camelize('auditArchiveRetrievalId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetAuditArchiveRetrieval',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'auditArchiveRetrieval',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_audit_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetAuditPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetAuditPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetAuditPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_audit_policy(
                audit_policy_id=request.pop(util.camelize('auditPolicyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetAuditPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'auditPolicy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_audit_profile(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetAuditProfile'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetAuditProfile')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetAuditProfile')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_audit_profile(
                audit_profile_id=request.pop(util.camelize('auditProfileId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetAuditProfile',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'auditProfile',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_audit_trail(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetAuditTrail'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetAuditTrail')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetAuditTrail')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_audit_trail(
                audit_trail_id=request.pop(util.camelize('auditTrailId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetAuditTrail',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'auditTrail',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_compatible_formats_for_data_types(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetCompatibleFormatsForDataTypes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetCompatibleFormatsForDataTypes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetCompatibleFormatsForDataTypes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_compatible_formats_for_data_types(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.get_compatible_formats_for_data_types(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.get_compatible_formats_for_data_types(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetCompatibleFormatsForDataTypes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'compatibleFormatsForDataTypes',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_compatible_formats_for_sensitive_types(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetCompatibleFormatsForSensitiveTypes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetCompatibleFormatsForSensitiveTypes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetCompatibleFormatsForSensitiveTypes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_compatible_formats_for_sensitive_types(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.get_compatible_formats_for_sensitive_types(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.get_compatible_formats_for_sensitive_types(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetCompatibleFormatsForSensitiveTypes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'compatibleFormatsForSensitiveTypes',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_data_safe_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetDataSafeConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetDataSafeConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetDataSafeConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_data_safe_configuration(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetDataSafeConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataSafeConfiguration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_data_safe_private_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetDataSafePrivateEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetDataSafePrivateEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetDataSafePrivateEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_data_safe_private_endpoint(
                data_safe_private_endpoint_id=request.pop(util.camelize('dataSafePrivateEndpointId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetDataSafePrivateEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataSafePrivateEndpoint',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_difference_column(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetDifferenceColumn'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetDifferenceColumn')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetDifferenceColumn')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_difference_column(
                sdm_masking_policy_difference_id=request.pop(util.camelize('sdmMaskingPolicyDifferenceId')),
                difference_column_key=request.pop(util.camelize('differenceColumnKey')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetDifferenceColumn',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'differenceColumn',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_discovery_job(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetDiscoveryJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetDiscoveryJob')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetDiscoveryJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_discovery_job(
                discovery_job_id=request.pop(util.camelize('discoveryJobId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetDiscoveryJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'discoveryJob',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_discovery_job_result(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetDiscoveryJobResult'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetDiscoveryJobResult')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetDiscoveryJobResult')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_discovery_job_result(
                discovery_job_id=request.pop(util.camelize('discoveryJobId')),
                result_key=request.pop(util.camelize('resultKey')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetDiscoveryJobResult',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'discoveryJobResult',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_library_masking_format(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetLibraryMaskingFormat'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetLibraryMaskingFormat')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetLibraryMaskingFormat')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_library_masking_format(
                library_masking_format_id=request.pop(util.camelize('libraryMaskingFormatId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetLibraryMaskingFormat',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'libraryMaskingFormat',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_masking_column(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetMaskingColumn'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetMaskingColumn')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetMaskingColumn')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_masking_column(
                masking_policy_id=request.pop(util.camelize('maskingPolicyId')),
                masking_column_key=request.pop(util.camelize('maskingColumnKey')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetMaskingColumn',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'maskingColumn',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_masking_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetMaskingPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetMaskingPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetMaskingPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_masking_policy(
                masking_policy_id=request.pop(util.camelize('maskingPolicyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetMaskingPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'maskingPolicy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_masking_report(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetMaskingReport'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetMaskingReport')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetMaskingReport')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_masking_report(
                masking_report_id=request.pop(util.camelize('maskingReportId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetMaskingReport',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'maskingReport',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_on_prem_connector(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetOnPremConnector'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetOnPremConnector')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetOnPremConnector')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_on_prem_connector(
                on_prem_connector_id=request.pop(util.camelize('onPremConnectorId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetOnPremConnector',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'onPremConnector',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_profile(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetProfile'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetProfile')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetProfile')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_profile(
                user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                profile_name=request.pop(util.camelize('profileName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetProfile',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'profile',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_report(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetReport'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetReport')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetReport')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_report(
                report_id=request.pop(util.camelize('reportId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetReport',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'report',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_report_content(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetReportContent'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetReportContent')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetReportContent')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_report_content(
                report_id=request.pop(util.camelize('reportId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetReportContent',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_report_definition(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetReportDefinition'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetReportDefinition')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetReportDefinition')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_report_definition(
                report_definition_id=request.pop(util.camelize('reportDefinitionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetReportDefinition',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'reportDefinition',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_sdm_masking_policy_difference(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetSdmMaskingPolicyDifference'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetSdmMaskingPolicyDifference')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetSdmMaskingPolicyDifference')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_sdm_masking_policy_difference(
                sdm_masking_policy_difference_id=request.pop(util.camelize('sdmMaskingPolicyDifferenceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetSdmMaskingPolicyDifference',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sdmMaskingPolicyDifference',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_security_assessment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetSecurityAssessment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetSecurityAssessment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetSecurityAssessment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_security_assessment(
                security_assessment_id=request.pop(util.camelize('securityAssessmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetSecurityAssessment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'securityAssessment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_security_assessment_comparison(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetSecurityAssessmentComparison'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetSecurityAssessmentComparison')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetSecurityAssessmentComparison')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_security_assessment_comparison(
                security_assessment_id=request.pop(util.camelize('securityAssessmentId')),
                comparison_security_assessment_id=request.pop(util.camelize('comparisonSecurityAssessmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetSecurityAssessmentComparison',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'securityAssessmentComparison',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_sensitive_column(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetSensitiveColumn'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetSensitiveColumn')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetSensitiveColumn')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_sensitive_column(
                sensitive_data_model_id=request.pop(util.camelize('sensitiveDataModelId')),
                sensitive_column_key=request.pop(util.camelize('sensitiveColumnKey')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetSensitiveColumn',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sensitiveColumn',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_sensitive_data_model(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetSensitiveDataModel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetSensitiveDataModel')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetSensitiveDataModel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_sensitive_data_model(
                sensitive_data_model_id=request.pop(util.camelize('sensitiveDataModelId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetSensitiveDataModel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sensitiveDataModel',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_sensitive_type(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetSensitiveType'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetSensitiveType')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetSensitiveType')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_sensitive_type(
                sensitive_type_id=request.pop(util.camelize('sensitiveTypeId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetSensitiveType',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sensitiveType',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_target_alert_policy_association(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetTargetAlertPolicyAssociation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetTargetAlertPolicyAssociation')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetTargetAlertPolicyAssociation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_target_alert_policy_association(
                target_alert_policy_association_id=request.pop(util.camelize('targetAlertPolicyAssociationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetTargetAlertPolicyAssociation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'targetAlertPolicyAssociation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_target_database(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetTargetDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetTargetDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetTargetDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_target_database(
                target_database_id=request.pop(util.camelize('targetDatabaseId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetTargetDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'targetDatabase',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_user_assessment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetUserAssessment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetUserAssessment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetUserAssessment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_user_assessment(
                user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetUserAssessment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'userAssessment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_user_assessment_comparison(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetUserAssessmentComparison'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetUserAssessmentComparison')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetUserAssessmentComparison')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_user_assessment_comparison(
                user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                comparison_user_assessment_id=request.pop(util.camelize('comparisonUserAssessmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetUserAssessmentComparison',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'userAssessmentComparison',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_alert_analytics(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListAlertAnalytics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListAlertAnalytics')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListAlertAnalytics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_alert_analytics(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_alert_analytics(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_alert_analytics(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListAlertAnalytics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'alertAnalyticsCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_alert_policies(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListAlertPolicies'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListAlertPolicies')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListAlertPolicies')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_alert_policies(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_alert_policies(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_alert_policies(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListAlertPolicies',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'alertPolicyCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_alert_policy_rules(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListAlertPolicyRules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListAlertPolicyRules')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListAlertPolicyRules')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_alert_policy_rules(
                alert_policy_id=request.pop(util.camelize('alertPolicyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_alert_policy_rules(
                    alert_policy_id=request.pop(util.camelize('alertPolicyId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_alert_policy_rules(
                        alert_policy_id=request.pop(util.camelize('alertPolicyId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListAlertPolicyRules',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'alertPolicyRuleCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_alerts(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListAlerts'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListAlerts')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListAlerts')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_alerts(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_alerts(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_alerts(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListAlerts',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'alertCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_audit_archive_retrievals(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListAuditArchiveRetrievals'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListAuditArchiveRetrievals')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListAuditArchiveRetrievals')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_audit_archive_retrievals(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_audit_archive_retrievals(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_audit_archive_retrievals(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListAuditArchiveRetrievals',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'auditArchiveRetrievalCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_audit_event_analytics(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListAuditEventAnalytics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListAuditEventAnalytics')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListAuditEventAnalytics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_audit_event_analytics(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_audit_event_analytics(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_audit_event_analytics(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListAuditEventAnalytics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'auditEventAnalyticsCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_audit_events(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListAuditEvents'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListAuditEvents')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListAuditEvents')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_audit_events(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_audit_events(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_audit_events(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListAuditEvents',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'auditEventCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_audit_policies(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListAuditPolicies'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListAuditPolicies')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListAuditPolicies')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_audit_policies(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_audit_policies(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_audit_policies(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListAuditPolicies',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'auditPolicyCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_audit_policy_analytics(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListAuditPolicyAnalytics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListAuditPolicyAnalytics')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListAuditPolicyAnalytics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_audit_policy_analytics(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_audit_policy_analytics(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_audit_policy_analytics(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListAuditPolicyAnalytics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'auditPolicyAnalyticCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_audit_profile_analytics(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListAuditProfileAnalytics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListAuditProfileAnalytics')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListAuditProfileAnalytics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_audit_profile_analytics(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_audit_profile_analytics(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_audit_profile_analytics(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListAuditProfileAnalytics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'auditProfileAnalyticCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_audit_profiles(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListAuditProfiles'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListAuditProfiles')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListAuditProfiles')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_audit_profiles(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_audit_profiles(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_audit_profiles(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListAuditProfiles',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'auditProfileCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_audit_trail_analytics(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListAuditTrailAnalytics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListAuditTrailAnalytics')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListAuditTrailAnalytics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_audit_trail_analytics(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_audit_trail_analytics(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_audit_trail_analytics(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListAuditTrailAnalytics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'auditTrailAnalyticCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_audit_trails(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListAuditTrails'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListAuditTrails')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListAuditTrails')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_audit_trails(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_audit_trails(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_audit_trails(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListAuditTrails',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'auditTrailCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_available_audit_volumes(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListAvailableAuditVolumes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListAvailableAuditVolumes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListAvailableAuditVolumes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_available_audit_volumes(
                audit_profile_id=request.pop(util.camelize('auditProfileId')),
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_available_audit_volumes(
                    audit_profile_id=request.pop(util.camelize('auditProfileId')),
                    work_request_id=request.pop(util.camelize('workRequestId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_available_audit_volumes(
                        audit_profile_id=request.pop(util.camelize('auditProfileId')),
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListAvailableAuditVolumes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'availableAuditVolumeCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_collected_audit_volumes(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListCollectedAuditVolumes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListCollectedAuditVolumes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListCollectedAuditVolumes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_collected_audit_volumes(
                audit_profile_id=request.pop(util.camelize('auditProfileId')),
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_collected_audit_volumes(
                    audit_profile_id=request.pop(util.camelize('auditProfileId')),
                    work_request_id=request.pop(util.camelize('workRequestId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_collected_audit_volumes(
                        audit_profile_id=request.pop(util.camelize('auditProfileId')),
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListCollectedAuditVolumes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'collectedAuditVolumeCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_columns(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListColumns'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListColumns')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListColumns')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_columns(
                target_database_id=request.pop(util.camelize('targetDatabaseId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_columns(
                    target_database_id=request.pop(util.camelize('targetDatabaseId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_columns(
                        target_database_id=request.pop(util.camelize('targetDatabaseId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListColumns',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'columnSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_data_safe_private_endpoints(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListDataSafePrivateEndpoints'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListDataSafePrivateEndpoints')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListDataSafePrivateEndpoints')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_data_safe_private_endpoints(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_data_safe_private_endpoints(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_data_safe_private_endpoints(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListDataSafePrivateEndpoints',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataSafePrivateEndpointSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_difference_columns(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListDifferenceColumns'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListDifferenceColumns')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListDifferenceColumns')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_difference_columns(
                sdm_masking_policy_difference_id=request.pop(util.camelize('sdmMaskingPolicyDifferenceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_difference_columns(
                    sdm_masking_policy_difference_id=request.pop(util.camelize('sdmMaskingPolicyDifferenceId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_difference_columns(
                        sdm_masking_policy_difference_id=request.pop(util.camelize('sdmMaskingPolicyDifferenceId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListDifferenceColumns',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sdmMaskingPolicyDifferenceColumnCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_discovery_analytics(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListDiscoveryAnalytics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListDiscoveryAnalytics')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListDiscoveryAnalytics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_discovery_analytics(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_discovery_analytics(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_discovery_analytics(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListDiscoveryAnalytics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'discoveryAnalyticsCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_discovery_job_results(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListDiscoveryJobResults'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListDiscoveryJobResults')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListDiscoveryJobResults')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_discovery_job_results(
                discovery_job_id=request.pop(util.camelize('discoveryJobId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_discovery_job_results(
                    discovery_job_id=request.pop(util.camelize('discoveryJobId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_discovery_job_results(
                        discovery_job_id=request.pop(util.camelize('discoveryJobId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListDiscoveryJobResults',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'discoveryJobResultCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_discovery_jobs(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListDiscoveryJobs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListDiscoveryJobs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListDiscoveryJobs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_discovery_jobs(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_discovery_jobs(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_discovery_jobs(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListDiscoveryJobs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'discoveryJobCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_findings(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListFindings'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListFindings')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListFindings')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_findings(
                security_assessment_id=request.pop(util.camelize('securityAssessmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_findings(
                    security_assessment_id=request.pop(util.camelize('securityAssessmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_findings(
                        security_assessment_id=request.pop(util.camelize('securityAssessmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListFindings',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'findingSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_grants(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListGrants'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListGrants')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListGrants')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_grants(
                user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                user_key=request.pop(util.camelize('userKey')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_grants(
                    user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                    user_key=request.pop(util.camelize('userKey')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_grants(
                        user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                        user_key=request.pop(util.camelize('userKey')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListGrants',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'grantSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_library_masking_formats(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListLibraryMaskingFormats'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListLibraryMaskingFormats')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListLibraryMaskingFormats')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_library_masking_formats(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_library_masking_formats(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_library_masking_formats(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListLibraryMaskingFormats',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'libraryMaskingFormatCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_masked_columns(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListMaskedColumns'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListMaskedColumns')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListMaskedColumns')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_masked_columns(
                masking_report_id=request.pop(util.camelize('maskingReportId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_masked_columns(
                    masking_report_id=request.pop(util.camelize('maskingReportId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_masked_columns(
                        masking_report_id=request.pop(util.camelize('maskingReportId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListMaskedColumns',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'maskedColumnCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_masking_analytics(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListMaskingAnalytics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListMaskingAnalytics')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListMaskingAnalytics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_masking_analytics(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_masking_analytics(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_masking_analytics(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListMaskingAnalytics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'maskingAnalyticsCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_masking_columns(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListMaskingColumns'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListMaskingColumns')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListMaskingColumns')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_masking_columns(
                masking_policy_id=request.pop(util.camelize('maskingPolicyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_masking_columns(
                    masking_policy_id=request.pop(util.camelize('maskingPolicyId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_masking_columns(
                        masking_policy_id=request.pop(util.camelize('maskingPolicyId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListMaskingColumns',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'maskingColumnCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_masking_objects(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListMaskingObjects'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListMaskingObjects')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListMaskingObjects')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_masking_objects(
                masking_policy_id=request.pop(util.camelize('maskingPolicyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_masking_objects(
                    masking_policy_id=request.pop(util.camelize('maskingPolicyId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_masking_objects(
                        masking_policy_id=request.pop(util.camelize('maskingPolicyId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListMaskingObjects',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'maskingObjectCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_masking_policies(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListMaskingPolicies'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListMaskingPolicies')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListMaskingPolicies')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_masking_policies(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_masking_policies(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_masking_policies(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListMaskingPolicies',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'maskingPolicyCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_masking_reports(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListMaskingReports'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListMaskingReports')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListMaskingReports')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_masking_reports(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_masking_reports(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_masking_reports(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListMaskingReports',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'maskingReportCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_masking_schemas(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListMaskingSchemas'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListMaskingSchemas')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListMaskingSchemas')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_masking_schemas(
                masking_policy_id=request.pop(util.camelize('maskingPolicyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_masking_schemas(
                    masking_policy_id=request.pop(util.camelize('maskingPolicyId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_masking_schemas(
                        masking_policy_id=request.pop(util.camelize('maskingPolicyId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListMaskingSchemas',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'maskingSchemaCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_on_prem_connectors(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListOnPremConnectors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListOnPremConnectors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListOnPremConnectors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_on_prem_connectors(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_on_prem_connectors(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_on_prem_connectors(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListOnPremConnectors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'onPremConnectorSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_profile_analytics(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListProfileAnalytics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListProfileAnalytics')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListProfileAnalytics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_profile_analytics(
                user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_profile_analytics(
                    user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_profile_analytics(
                        user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListProfileAnalytics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'profileAggregation',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_profile_summaries(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListProfileSummaries'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListProfileSummaries')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListProfileSummaries')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_profile_summaries(
                user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_profile_summaries(
                    user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_profile_summaries(
                        user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListProfileSummaries',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'profileSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_report_definitions(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListReportDefinitions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListReportDefinitions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListReportDefinitions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_report_definitions(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_report_definitions(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_report_definitions(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListReportDefinitions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'reportDefinitionCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_reports(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListReports'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListReports')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListReports')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_reports(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_reports(
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
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListReports',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'reportCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_roles(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListRoles'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListRoles')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListRoles')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_roles(
                target_database_id=request.pop(util.camelize('targetDatabaseId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_roles(
                    target_database_id=request.pop(util.camelize('targetDatabaseId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_roles(
                        target_database_id=request.pop(util.camelize('targetDatabaseId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListRoles',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'roleSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_schemas(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListSchemas'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListSchemas')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListSchemas')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_schemas(
                target_database_id=request.pop(util.camelize('targetDatabaseId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_schemas(
                    target_database_id=request.pop(util.camelize('targetDatabaseId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_schemas(
                        target_database_id=request.pop(util.camelize('targetDatabaseId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListSchemas',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'schemaSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_sdm_masking_policy_differences(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListSdmMaskingPolicyDifferences'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListSdmMaskingPolicyDifferences')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListSdmMaskingPolicyDifferences')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_sdm_masking_policy_differences(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_sdm_masking_policy_differences(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_sdm_masking_policy_differences(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListSdmMaskingPolicyDifferences',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sdmMaskingPolicyDifferenceCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_security_assessments(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListSecurityAssessments'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListSecurityAssessments')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListSecurityAssessments')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_security_assessments(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_security_assessments(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_security_assessments(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListSecurityAssessments',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'securityAssessmentSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_sensitive_columns(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListSensitiveColumns'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListSensitiveColumns')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListSensitiveColumns')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_sensitive_columns(
                sensitive_data_model_id=request.pop(util.camelize('sensitiveDataModelId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_sensitive_columns(
                    sensitive_data_model_id=request.pop(util.camelize('sensitiveDataModelId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_sensitive_columns(
                        sensitive_data_model_id=request.pop(util.camelize('sensitiveDataModelId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListSensitiveColumns',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sensitiveColumnCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_sensitive_data_models(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListSensitiveDataModels'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListSensitiveDataModels')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListSensitiveDataModels')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_sensitive_data_models(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_sensitive_data_models(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_sensitive_data_models(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListSensitiveDataModels',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sensitiveDataModelCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_sensitive_objects(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListSensitiveObjects'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListSensitiveObjects')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListSensitiveObjects')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_sensitive_objects(
                sensitive_data_model_id=request.pop(util.camelize('sensitiveDataModelId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_sensitive_objects(
                    sensitive_data_model_id=request.pop(util.camelize('sensitiveDataModelId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_sensitive_objects(
                        sensitive_data_model_id=request.pop(util.camelize('sensitiveDataModelId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListSensitiveObjects',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sensitiveObjectCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_sensitive_schemas(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListSensitiveSchemas'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListSensitiveSchemas')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListSensitiveSchemas')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_sensitive_schemas(
                sensitive_data_model_id=request.pop(util.camelize('sensitiveDataModelId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_sensitive_schemas(
                    sensitive_data_model_id=request.pop(util.camelize('sensitiveDataModelId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_sensitive_schemas(
                        sensitive_data_model_id=request.pop(util.camelize('sensitiveDataModelId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListSensitiveSchemas',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sensitiveSchemaCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_sensitive_types(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListSensitiveTypes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListSensitiveTypes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListSensitiveTypes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_sensitive_types(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_sensitive_types(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_sensitive_types(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListSensitiveTypes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sensitiveTypeCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_tables(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListTables'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListTables')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListTables')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_tables(
                target_database_id=request.pop(util.camelize('targetDatabaseId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_tables(
                    target_database_id=request.pop(util.camelize('targetDatabaseId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_tables(
                        target_database_id=request.pop(util.camelize('targetDatabaseId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListTables',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'tableSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_target_alert_policy_associations(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListTargetAlertPolicyAssociations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListTargetAlertPolicyAssociations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListTargetAlertPolicyAssociations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_target_alert_policy_associations(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_target_alert_policy_associations(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_target_alert_policy_associations(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListTargetAlertPolicyAssociations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'targetAlertPolicyAssociationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_target_databases(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListTargetDatabases'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListTargetDatabases')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListTargetDatabases')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_target_databases(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_target_databases(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_target_databases(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListTargetDatabases',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'targetDatabaseSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_user_analytics(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListUserAnalytics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListUserAnalytics')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListUserAnalytics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_user_analytics(
                user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_user_analytics(
                    user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_user_analytics(
                        user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListUserAnalytics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'userAggregation',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_user_assessments(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListUserAssessments'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListUserAssessments')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListUserAssessments')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_user_assessments(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_user_assessments(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_user_assessments(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListUserAssessments',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'userAssessmentSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_users(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListUsers'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListUsers')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListUsers')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_users(
                user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_users(
                    user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_users(
                        user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListUsers',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'userSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
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
            'data_safe',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestError',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
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
            'data_safe',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntry',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_work_requests(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_requests(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_requests(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_mask_data(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'MaskData'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'MaskData')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='MaskData')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.mask_data(
                masking_policy_id=request.pop(util.camelize('maskingPolicyId')),
                mask_data_details=request.pop(util.camelize('MaskDataDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'MaskData',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mask_data',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_modify_global_settings(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ModifyGlobalSettings'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ModifyGlobalSettings')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ModifyGlobalSettings')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.modify_global_settings(
                modify_global_settings_details=request.pop(util.camelize('ModifyGlobalSettingsDetails')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ModifyGlobalSettings',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'modify_global_settings',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_patch_alerts(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'PatchAlerts'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'PatchAlerts')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='PatchAlerts')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.patch_alerts(
                patch_alerts_details=request.pop(util.camelize('PatchAlertsDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'PatchAlerts',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'patch_alerts',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_patch_discovery_job_results(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'PatchDiscoveryJobResults'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'PatchDiscoveryJobResults')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='PatchDiscoveryJobResults')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.patch_discovery_job_results(
                discovery_job_id=request.pop(util.camelize('discoveryJobId')),
                patch_discovery_job_result_details=request.pop(util.camelize('PatchDiscoveryJobResultDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'PatchDiscoveryJobResults',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'patch_discovery_job_results',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_patch_masking_columns(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'PatchMaskingColumns'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'PatchMaskingColumns')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='PatchMaskingColumns')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.patch_masking_columns(
                masking_policy_id=request.pop(util.camelize('maskingPolicyId')),
                patch_masking_columns_details=request.pop(util.camelize('PatchMaskingColumnsDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'PatchMaskingColumns',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'patch_masking_columns',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_patch_sdm_masking_policy_difference_columns(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'PatchSdmMaskingPolicyDifferenceColumns'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'PatchSdmMaskingPolicyDifferenceColumns')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='PatchSdmMaskingPolicyDifferenceColumns')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.patch_sdm_masking_policy_difference_columns(
                sdm_masking_policy_difference_id=request.pop(util.camelize('sdmMaskingPolicyDifferenceId')),
                patch_sdm_masking_policy_difference_columns_details=request.pop(util.camelize('PatchSdmMaskingPolicyDifferenceColumnsDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'PatchSdmMaskingPolicyDifferenceColumns',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'patch_sdm_masking_policy_difference_columns',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_patch_sensitive_columns(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'PatchSensitiveColumns'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'PatchSensitiveColumns')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='PatchSensitiveColumns')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.patch_sensitive_columns(
                sensitive_data_model_id=request.pop(util.camelize('sensitiveDataModelId')),
                patch_sensitive_column_details=request.pop(util.camelize('PatchSensitiveColumnDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'PatchSensitiveColumns',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'patch_sensitive_columns',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_patch_target_alert_policy_association(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'PatchTargetAlertPolicyAssociation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'PatchTargetAlertPolicyAssociation')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='PatchTargetAlertPolicyAssociation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.patch_target_alert_policy_association(
                patch_target_alert_policy_association_details=request.pop(util.camelize('PatchTargetAlertPolicyAssociationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'PatchTargetAlertPolicyAssociation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'patch_target_alert_policy_association',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_provision_audit_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ProvisionAuditPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ProvisionAuditPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ProvisionAuditPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.provision_audit_policy(
                provision_audit_policy_details=request.pop(util.camelize('ProvisionAuditPolicyDetails')),
                audit_policy_id=request.pop(util.camelize('auditPolicyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ProvisionAuditPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'provision_audit_policy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_refresh_security_assessment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'RefreshSecurityAssessment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'RefreshSecurityAssessment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='RefreshSecurityAssessment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.refresh_security_assessment(
                security_assessment_id=request.pop(util.camelize('securityAssessmentId')),
                run_security_assessment_details=request.pop(util.camelize('RunSecurityAssessmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'RefreshSecurityAssessment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'refresh_security_assessment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_refresh_user_assessment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'RefreshUserAssessment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'RefreshUserAssessment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='RefreshUserAssessment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.refresh_user_assessment(
                user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                run_user_assessment_details=request.pop(util.camelize('RunUserAssessmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'RefreshUserAssessment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'refresh_user_assessment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_remove_schedule_report(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'RemoveScheduleReport'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'RemoveScheduleReport')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='RemoveScheduleReport')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.remove_schedule_report(
                report_definition_id=request.pop(util.camelize('reportDefinitionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'RemoveScheduleReport',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'remove_schedule_report',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_resume_audit_trail(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ResumeAuditTrail'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ResumeAuditTrail')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ResumeAuditTrail')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.resume_audit_trail(
                audit_trail_id=request.pop(util.camelize('auditTrailId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ResumeAuditTrail',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'resume_audit_trail',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_resume_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ResumeWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ResumeWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ResumeWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.resume_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ResumeWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'resume_work_request',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_retrieve_audit_policies(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'RetrieveAuditPolicies'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'RetrieveAuditPolicies')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='RetrieveAuditPolicies')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.retrieve_audit_policies(
                audit_policy_id=request.pop(util.camelize('auditPolicyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'RetrieveAuditPolicies',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'retrieve_audit_policies',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_schedule_report(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ScheduleReport'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ScheduleReport')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ScheduleReport')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.schedule_report(
                report_definition_id=request.pop(util.camelize('reportDefinitionId')),
                schedule_report_details=request.pop(util.camelize('ScheduleReportDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ScheduleReport',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'schedule_report',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_set_security_assessment_baseline(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'SetSecurityAssessmentBaseline'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'SetSecurityAssessmentBaseline')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='SetSecurityAssessmentBaseline')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.set_security_assessment_baseline(
                security_assessment_id=request.pop(util.camelize('securityAssessmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'SetSecurityAssessmentBaseline',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'set_security_assessment_baseline',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_set_user_assessment_baseline(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'SetUserAssessmentBaseline'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'SetUserAssessmentBaseline')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='SetUserAssessmentBaseline')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.set_user_assessment_baseline(
                user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'SetUserAssessmentBaseline',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'set_user_assessment_baseline',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_start_audit_trail(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'StartAuditTrail'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'StartAuditTrail')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='StartAuditTrail')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.start_audit_trail(
                start_audit_trail_details=request.pop(util.camelize('StartAuditTrailDetails')),
                audit_trail_id=request.pop(util.camelize('auditTrailId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'StartAuditTrail',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'start_audit_trail',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_stop_audit_trail(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'StopAuditTrail'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'StopAuditTrail')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='StopAuditTrail')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.stop_audit_trail(
                audit_trail_id=request.pop(util.camelize('auditTrailId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'StopAuditTrail',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stop_audit_trail',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_suspend_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'SuspendWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'SuspendWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='SuspendWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.suspend_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'SuspendWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'suspend_work_request',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_unset_security_assessment_baseline(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'UnsetSecurityAssessmentBaseline'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'UnsetSecurityAssessmentBaseline')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='UnsetSecurityAssessmentBaseline')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.unset_security_assessment_baseline(
                security_assessment_id=request.pop(util.camelize('securityAssessmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'UnsetSecurityAssessmentBaseline',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'unset_security_assessment_baseline',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_unset_user_assessment_baseline(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'UnsetUserAssessmentBaseline'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'UnsetUserAssessmentBaseline')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='UnsetUserAssessmentBaseline')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.unset_user_assessment_baseline(
                user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'UnsetUserAssessmentBaseline',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'unset_user_assessment_baseline',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_update_alert(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'UpdateAlert'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'UpdateAlert')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='UpdateAlert')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.update_alert(
                alert_id=request.pop(util.camelize('alertId')),
                update_alert_details=request.pop(util.camelize('UpdateAlertDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'UpdateAlert',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'alert',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_update_audit_archive_retrieval(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'UpdateAuditArchiveRetrieval'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'UpdateAuditArchiveRetrieval')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='UpdateAuditArchiveRetrieval')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.update_audit_archive_retrieval(
                audit_archive_retrieval_id=request.pop(util.camelize('auditArchiveRetrievalId')),
                update_audit_archive_retrieval_details=request.pop(util.camelize('UpdateAuditArchiveRetrievalDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'UpdateAuditArchiveRetrieval',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_audit_archive_retrieval',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_update_audit_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'UpdateAuditPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'UpdateAuditPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='UpdateAuditPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.update_audit_policy(
                audit_policy_id=request.pop(util.camelize('auditPolicyId')),
                update_audit_policy_details=request.pop(util.camelize('UpdateAuditPolicyDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'UpdateAuditPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_audit_policy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_update_audit_profile(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'UpdateAuditProfile'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'UpdateAuditProfile')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='UpdateAuditProfile')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.update_audit_profile(
                audit_profile_id=request.pop(util.camelize('auditProfileId')),
                update_audit_profile_details=request.pop(util.camelize('UpdateAuditProfileDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'UpdateAuditProfile',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_audit_profile',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_update_audit_trail(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'UpdateAuditTrail'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'UpdateAuditTrail')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='UpdateAuditTrail')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.update_audit_trail(
                audit_trail_id=request.pop(util.camelize('auditTrailId')),
                update_audit_trail_details=request.pop(util.camelize('UpdateAuditTrailDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'UpdateAuditTrail',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_audit_trail',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_update_data_safe_private_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'UpdateDataSafePrivateEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'UpdateDataSafePrivateEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='UpdateDataSafePrivateEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.update_data_safe_private_endpoint(
                data_safe_private_endpoint_id=request.pop(util.camelize('dataSafePrivateEndpointId')),
                update_data_safe_private_endpoint_details=request.pop(util.camelize('UpdateDataSafePrivateEndpointDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'UpdateDataSafePrivateEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_data_safe_private_endpoint',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_update_library_masking_format(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'UpdateLibraryMaskingFormat'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'UpdateLibraryMaskingFormat')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='UpdateLibraryMaskingFormat')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.update_library_masking_format(
                library_masking_format_id=request.pop(util.camelize('libraryMaskingFormatId')),
                update_library_masking_format_details=request.pop(util.camelize('UpdateLibraryMaskingFormatDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'UpdateLibraryMaskingFormat',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_library_masking_format',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_update_masking_column(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'UpdateMaskingColumn'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'UpdateMaskingColumn')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='UpdateMaskingColumn')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.update_masking_column(
                masking_column_key=request.pop(util.camelize('maskingColumnKey')),
                masking_policy_id=request.pop(util.camelize('maskingPolicyId')),
                update_masking_column_details=request.pop(util.camelize('UpdateMaskingColumnDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'UpdateMaskingColumn',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_masking_column',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_update_masking_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'UpdateMaskingPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'UpdateMaskingPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='UpdateMaskingPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.update_masking_policy(
                masking_policy_id=request.pop(util.camelize('maskingPolicyId')),
                update_masking_policy_details=request.pop(util.camelize('UpdateMaskingPolicyDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'UpdateMaskingPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_masking_policy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_update_on_prem_connector(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'UpdateOnPremConnector'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'UpdateOnPremConnector')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='UpdateOnPremConnector')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.update_on_prem_connector(
                on_prem_connector_id=request.pop(util.camelize('onPremConnectorId')),
                update_on_prem_connector_details=request.pop(util.camelize('UpdateOnPremConnectorDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'UpdateOnPremConnector',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_on_prem_connector',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_update_on_prem_connector_wallet(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'UpdateOnPremConnectorWallet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'UpdateOnPremConnectorWallet')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='UpdateOnPremConnectorWallet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.update_on_prem_connector_wallet(
                update_on_prem_connector_wallet_details=request.pop(util.camelize('UpdateOnPremConnectorWalletDetails')),
                on_prem_connector_id=request.pop(util.camelize('onPremConnectorId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'UpdateOnPremConnectorWallet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_on_prem_connector_wallet',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_update_report_definition(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'UpdateReportDefinition'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'UpdateReportDefinition')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='UpdateReportDefinition')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.update_report_definition(
                report_definition_id=request.pop(util.camelize('reportDefinitionId')),
                update_report_definition_details=request.pop(util.camelize('UpdateReportDefinitionDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'UpdateReportDefinition',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_report_definition',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_update_sdm_masking_policy_difference(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'UpdateSdmMaskingPolicyDifference'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'UpdateSdmMaskingPolicyDifference')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='UpdateSdmMaskingPolicyDifference')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.update_sdm_masking_policy_difference(
                sdm_masking_policy_difference_id=request.pop(util.camelize('sdmMaskingPolicyDifferenceId')),
                update_sdm_masking_policy_difference_details=request.pop(util.camelize('UpdateSdmMaskingPolicyDifferenceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'UpdateSdmMaskingPolicyDifference',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_sdm_masking_policy_difference',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_update_security_assessment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'UpdateSecurityAssessment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'UpdateSecurityAssessment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='UpdateSecurityAssessment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.update_security_assessment(
                security_assessment_id=request.pop(util.camelize('securityAssessmentId')),
                update_security_assessment_details=request.pop(util.camelize('UpdateSecurityAssessmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'UpdateSecurityAssessment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_security_assessment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_update_sensitive_column(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'UpdateSensitiveColumn'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'UpdateSensitiveColumn')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='UpdateSensitiveColumn')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.update_sensitive_column(
                sensitive_data_model_id=request.pop(util.camelize('sensitiveDataModelId')),
                sensitive_column_key=request.pop(util.camelize('sensitiveColumnKey')),
                update_sensitive_column_details=request.pop(util.camelize('UpdateSensitiveColumnDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'UpdateSensitiveColumn',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_sensitive_column',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_update_sensitive_data_model(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'UpdateSensitiveDataModel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'UpdateSensitiveDataModel')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='UpdateSensitiveDataModel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.update_sensitive_data_model(
                sensitive_data_model_id=request.pop(util.camelize('sensitiveDataModelId')),
                update_sensitive_data_model_details=request.pop(util.camelize('UpdateSensitiveDataModelDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'UpdateSensitiveDataModel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_sensitive_data_model',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_update_sensitive_type(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'UpdateSensitiveType'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'UpdateSensitiveType')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='UpdateSensitiveType')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.update_sensitive_type(
                sensitive_type_id=request.pop(util.camelize('sensitiveTypeId')),
                update_sensitive_type_details=request.pop(util.camelize('UpdateSensitiveTypeDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'UpdateSensitiveType',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_sensitive_type',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_update_target_alert_policy_association(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'UpdateTargetAlertPolicyAssociation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'UpdateTargetAlertPolicyAssociation')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='UpdateTargetAlertPolicyAssociation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.update_target_alert_policy_association(
                target_alert_policy_association_id=request.pop(util.camelize('targetAlertPolicyAssociationId')),
                update_target_alert_policy_association_details=request.pop(util.camelize('UpdateTargetAlertPolicyAssociationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'UpdateTargetAlertPolicyAssociation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_target_alert_policy_association',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_update_target_database(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'UpdateTargetDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'UpdateTargetDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='UpdateTargetDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.update_target_database(
                target_database_id=request.pop(util.camelize('targetDatabaseId')),
                update_target_database_details=request.pop(util.camelize('UpdateTargetDatabaseDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'UpdateTargetDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_target_database',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_update_user_assessment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'UpdateUserAssessment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'UpdateUserAssessment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='UpdateUserAssessment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.update_user_assessment(
                user_assessment_id=request.pop(util.camelize('userAssessmentId')),
                update_user_assessment_details=request.pop(util.camelize('UpdateUserAssessmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'UpdateUserAssessment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_user_assessment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_upload_masking_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'UploadMaskingPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'UploadMaskingPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='UploadMaskingPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.upload_masking_policy(
                upload_masking_policy_details=request.pop(util.camelize('UploadMaskingPolicyDetails')),
                masking_policy_id=request.pop(util.camelize('maskingPolicyId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'UploadMaskingPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'upload_masking_policy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_upload_sensitive_data_model(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'UploadSensitiveDataModel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'UploadSensitiveDataModel')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='UploadSensitiveDataModel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.upload_sensitive_data_model(
                sensitive_data_model_id=request.pop(util.camelize('sensitiveDataModelId')),
                upload_sensitive_data_model_details=request.pop(util.camelize('UploadSensitiveDataModelDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'UploadSensitiveDataModel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'upload_sensitive_data_model',
            False,
            False
        )
