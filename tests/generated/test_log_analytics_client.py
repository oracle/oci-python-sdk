# Code generated. DO NOT EDIT.
# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
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

        cassette_location = os.path.join('generated', 'log_analytics_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_add_entity_association(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'AddEntityAssociation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'AddEntityAssociation')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='AddEntityAssociation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.add_entity_association(
                namespace_name=request.pop(util.camelize('namespaceName')),
                log_analytics_entity_id=request.pop(util.camelize('logAnalyticsEntityId')),
                add_entity_association_details=request.pop(util.camelize('AddEntityAssociationDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'AddEntityAssociation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'add_entity_association',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_append_lookup_data(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'AppendLookupData'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'AppendLookupData')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='AppendLookupData')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.append_lookup_data(
                namespace_name=request.pop(util.camelize('namespaceName')),
                lookup_name=request.pop(util.camelize('lookupName')),
                append_lookup_file_body=request.pop(util.camelize('AppendLookupFileBody')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'AppendLookupData',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'append_lookup_data',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_batch_get_basic_info(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'BatchGetBasicInfo'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'BatchGetBasicInfo')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='BatchGetBasicInfo')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.batch_get_basic_info(
                namespace_name=request.pop(util.camelize('namespaceName')),
                basic_details=request.pop(util.camelize('BasicDetails')),
                is_include_deleted=request.pop(util.camelize('isIncludeDeleted')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.batch_get_basic_info(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    basic_details=request.pop(util.camelize('BasicDetails')),
                    is_include_deleted=request.pop(util.camelize('isIncludeDeleted')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.batch_get_basic_info(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        basic_details=request.pop(util.camelize('BasicDetails')),
                        is_include_deleted=request.pop(util.camelize('isIncludeDeleted')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'BatchGetBasicInfo',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsLabelCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_cancel_query_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'CancelQueryWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'CancelQueryWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='CancelQueryWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.cancel_query_work_request(
                namespace_name=request.pop(util.camelize('namespaceName')),
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'CancelQueryWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cancel_query_work_request',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_change_log_analytics_entity_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ChangeLogAnalyticsEntityCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ChangeLogAnalyticsEntityCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ChangeLogAnalyticsEntityCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.change_log_analytics_entity_compartment(
                namespace_name=request.pop(util.camelize('namespaceName')),
                log_analytics_entity_id=request.pop(util.camelize('logAnalyticsEntityId')),
                change_log_analytics_entity_compartment_details=request.pop(util.camelize('ChangeLogAnalyticsEntityCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ChangeLogAnalyticsEntityCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_log_analytics_entity_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_change_log_analytics_log_group_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ChangeLogAnalyticsLogGroupCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ChangeLogAnalyticsLogGroupCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ChangeLogAnalyticsLogGroupCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.change_log_analytics_log_group_compartment(
                namespace_name=request.pop(util.camelize('namespaceName')),
                log_analytics_log_group_id=request.pop(util.camelize('logAnalyticsLogGroupId')),
                change_log_analytics_log_group_compartment_details=request.pop(util.camelize('ChangeLogAnalyticsLogGroupCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ChangeLogAnalyticsLogGroupCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_log_analytics_log_group_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_change_log_analytics_object_collection_rule_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ChangeLogAnalyticsObjectCollectionRuleCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ChangeLogAnalyticsObjectCollectionRuleCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ChangeLogAnalyticsObjectCollectionRuleCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.change_log_analytics_object_collection_rule_compartment(
                namespace_name=request.pop(util.camelize('namespaceName')),
                log_analytics_object_collection_rule_id=request.pop(util.camelize('logAnalyticsObjectCollectionRuleId')),
                change_log_analytics_object_collection_rule_compartment_details=request.pop(util.camelize('ChangeLogAnalyticsObjectCollectionRuleCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ChangeLogAnalyticsObjectCollectionRuleCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_log_analytics_object_collection_rule_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_change_scheduled_task_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ChangeScheduledTaskCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ChangeScheduledTaskCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ChangeScheduledTaskCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.change_scheduled_task_compartment(
                namespace_name=request.pop(util.camelize('namespaceName')),
                scheduled_task_id=request.pop(util.camelize('scheduledTaskId')),
                change_scheduled_task_compartment_details=request.pop(util.camelize('ChangeScheduledTaskCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ChangeScheduledTaskCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_scheduled_task_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_clean(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'Clean'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'Clean')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='Clean')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.clean(
                namespace_name=request.pop(util.camelize('namespaceName')),
                scheduled_task_id=request.pop(util.camelize('scheduledTaskId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'Clean',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'clean',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_create_log_analytics_entity(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'CreateLogAnalyticsEntity'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'CreateLogAnalyticsEntity')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='CreateLogAnalyticsEntity')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.create_log_analytics_entity(
                namespace_name=request.pop(util.camelize('namespaceName')),
                create_log_analytics_entity_details=request.pop(util.camelize('CreateLogAnalyticsEntityDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'CreateLogAnalyticsEntity',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsEntity',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_create_log_analytics_entity_type(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'CreateLogAnalyticsEntityType'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'CreateLogAnalyticsEntityType')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='CreateLogAnalyticsEntityType')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.create_log_analytics_entity_type(
                namespace_name=request.pop(util.camelize('namespaceName')),
                create_log_analytics_entity_type_details=request.pop(util.camelize('CreateLogAnalyticsEntityTypeDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'CreateLogAnalyticsEntityType',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_log_analytics_entity_type',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_create_log_analytics_log_group(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'CreateLogAnalyticsLogGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'CreateLogAnalyticsLogGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='CreateLogAnalyticsLogGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.create_log_analytics_log_group(
                namespace_name=request.pop(util.camelize('namespaceName')),
                create_log_analytics_log_group_details=request.pop(util.camelize('CreateLogAnalyticsLogGroupDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'CreateLogAnalyticsLogGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsLogGroup',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_create_log_analytics_object_collection_rule(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'CreateLogAnalyticsObjectCollectionRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'CreateLogAnalyticsObjectCollectionRule')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='CreateLogAnalyticsObjectCollectionRule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.create_log_analytics_object_collection_rule(
                namespace_name=request.pop(util.camelize('namespaceName')),
                create_log_analytics_object_collection_rule_details=request.pop(util.camelize('CreateLogAnalyticsObjectCollectionRuleDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'CreateLogAnalyticsObjectCollectionRule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsObjectCollectionRule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_create_scheduled_task(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'CreateScheduledTask'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'CreateScheduledTask')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='CreateScheduledTask')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.create_scheduled_task(
                namespace_name=request.pop(util.camelize('namespaceName')),
                create_scheduled_task_details=request.pop(util.camelize('CreateScheduledTaskDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'CreateScheduledTask',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'scheduledTask',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_delete_associations(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'DeleteAssociations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'DeleteAssociations')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='DeleteAssociations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.delete_associations(
                namespace_name=request.pop(util.camelize('namespaceName')),
                delete_log_analytics_association_details=request.pop(util.camelize('DeleteLogAnalyticsAssociationDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'DeleteAssociations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_associations',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_delete_field(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'DeleteField'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'DeleteField')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='DeleteField')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.delete_field(
                namespace_name=request.pop(util.camelize('namespaceName')),
                field_name=request.pop(util.camelize('fieldName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'DeleteField',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_field',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_delete_label(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'DeleteLabel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'DeleteLabel')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='DeleteLabel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.delete_label(
                namespace_name=request.pop(util.camelize('namespaceName')),
                label_name=request.pop(util.camelize('labelName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'DeleteLabel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_label',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_delete_log_analytics_entity(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'DeleteLogAnalyticsEntity'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'DeleteLogAnalyticsEntity')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='DeleteLogAnalyticsEntity')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.delete_log_analytics_entity(
                namespace_name=request.pop(util.camelize('namespaceName')),
                log_analytics_entity_id=request.pop(util.camelize('logAnalyticsEntityId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'DeleteLogAnalyticsEntity',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_log_analytics_entity',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_delete_log_analytics_entity_type(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'DeleteLogAnalyticsEntityType'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'DeleteLogAnalyticsEntityType')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='DeleteLogAnalyticsEntityType')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.delete_log_analytics_entity_type(
                namespace_name=request.pop(util.camelize('namespaceName')),
                entity_type_name=request.pop(util.camelize('entityTypeName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'DeleteLogAnalyticsEntityType',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_log_analytics_entity_type',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_delete_log_analytics_log_group(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'DeleteLogAnalyticsLogGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'DeleteLogAnalyticsLogGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='DeleteLogAnalyticsLogGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.delete_log_analytics_log_group(
                namespace_name=request.pop(util.camelize('namespaceName')),
                log_analytics_log_group_id=request.pop(util.camelize('logAnalyticsLogGroupId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'DeleteLogAnalyticsLogGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_log_analytics_log_group',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_delete_log_analytics_object_collection_rule(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'DeleteLogAnalyticsObjectCollectionRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'DeleteLogAnalyticsObjectCollectionRule')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='DeleteLogAnalyticsObjectCollectionRule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.delete_log_analytics_object_collection_rule(
                namespace_name=request.pop(util.camelize('namespaceName')),
                log_analytics_object_collection_rule_id=request.pop(util.camelize('logAnalyticsObjectCollectionRuleId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'DeleteLogAnalyticsObjectCollectionRule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_log_analytics_object_collection_rule',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_delete_lookup(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'DeleteLookup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'DeleteLookup')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='DeleteLookup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.delete_lookup(
                namespace_name=request.pop(util.camelize('namespaceName')),
                lookup_name=request.pop(util.camelize('lookupName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'DeleteLookup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_lookup',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_delete_parser(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'DeleteParser'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'DeleteParser')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='DeleteParser')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.delete_parser(
                namespace_name=request.pop(util.camelize('namespaceName')),
                parser_name=request.pop(util.camelize('parserName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'DeleteParser',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_parser',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_delete_scheduled_task(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'DeleteScheduledTask'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'DeleteScheduledTask')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='DeleteScheduledTask')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.delete_scheduled_task(
                namespace_name=request.pop(util.camelize('namespaceName')),
                scheduled_task_id=request.pop(util.camelize('scheduledTaskId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'DeleteScheduledTask',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_scheduled_task',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_delete_source(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'DeleteSource'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'DeleteSource')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='DeleteSource')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.delete_source(
                namespace_name=request.pop(util.camelize('namespaceName')),
                source_name=request.pop(util.camelize('sourceName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'DeleteSource',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_source',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_delete_upload(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'DeleteUpload'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'DeleteUpload')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='DeleteUpload')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.delete_upload(
                namespace_name=request.pop(util.camelize('namespaceName')),
                upload_reference=request.pop(util.camelize('uploadReference')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'DeleteUpload',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_upload',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_delete_upload_file(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'DeleteUploadFile'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'DeleteUploadFile')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='DeleteUploadFile')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.delete_upload_file(
                namespace_name=request.pop(util.camelize('namespaceName')),
                upload_reference=request.pop(util.camelize('uploadReference')),
                file_reference=request.pop(util.camelize('fileReference')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'DeleteUploadFile',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_upload_file',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_delete_upload_warning(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'DeleteUploadWarning'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'DeleteUploadWarning')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='DeleteUploadWarning')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.delete_upload_warning(
                namespace_name=request.pop(util.camelize('namespaceName')),
                upload_reference=request.pop(util.camelize('uploadReference')),
                warning_reference=request.pop(util.camelize('warningReference')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'DeleteUploadWarning',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_upload_warning',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_disable_archiving(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'DisableArchiving'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'DisableArchiving')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='DisableArchiving')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.disable_archiving(
                namespace_name=request.pop(util.camelize('namespaceName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'DisableArchiving',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'success',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_enable_archiving(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'EnableArchiving'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'EnableArchiving')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='EnableArchiving')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.enable_archiving(
                namespace_name=request.pop(util.camelize('namespaceName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'EnableArchiving',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'success',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_estimate_purge_data_size(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'EstimatePurgeDataSize'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'EstimatePurgeDataSize')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='EstimatePurgeDataSize')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.estimate_purge_data_size(
                namespace_name=request.pop(util.camelize('namespaceName')),
                estimate_purge_data_size_details=request.pop(util.camelize('EstimatePurgeDataSizeDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'EstimatePurgeDataSize',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'estimatePurgeDataSizeResult',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_estimate_recall_data_size(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'EstimateRecallDataSize'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'EstimateRecallDataSize')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='EstimateRecallDataSize')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.estimate_recall_data_size(
                namespace_name=request.pop(util.camelize('namespaceName')),
                estimate_recall_data_size_details=request.pop(util.camelize('EstimateRecallDataSizeDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'EstimateRecallDataSize',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'estimateRecallDataSizeResult',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_estimate_release_data_size(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'EstimateReleaseDataSize'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'EstimateReleaseDataSize')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='EstimateReleaseDataSize')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.estimate_release_data_size(
                namespace_name=request.pop(util.camelize('namespaceName')),
                estimate_release_data_size_details=request.pop(util.camelize('EstimateReleaseDataSizeDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'EstimateReleaseDataSize',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'estimateReleaseDataSizeResult',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_export_custom_content(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ExportCustomContent'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ExportCustomContent')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ExportCustomContent')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.export_custom_content(
                namespace_name=request.pop(util.camelize('namespaceName')),
                export_custom_content_details=request.pop(util.camelize('ExportCustomContentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ExportCustomContent',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_export_query_result(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ExportQueryResult'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ExportQueryResult')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ExportQueryResult')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.export_query_result(
                namespace_name=request.pop(util.camelize('namespaceName')),
                export_details=request.pop(util.camelize('ExportDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ExportQueryResult',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_extract_structured_log_field_paths(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ExtractStructuredLogFieldPaths'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ExtractStructuredLogFieldPaths')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ExtractStructuredLogFieldPaths')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.extract_structured_log_field_paths(
                namespace_name=request.pop(util.camelize('namespaceName')),
                logan_parser_details=request.pop(util.camelize('LoganParserDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ExtractStructuredLogFieldPaths',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'extractLogFieldResults',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_extract_structured_log_header_paths(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ExtractStructuredLogHeaderPaths'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ExtractStructuredLogHeaderPaths')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ExtractStructuredLogHeaderPaths')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.extract_structured_log_header_paths(
                namespace_name=request.pop(util.camelize('namespaceName')),
                logan_parser_details=request.pop(util.camelize('LoganParserDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ExtractStructuredLogHeaderPaths',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'extractLogHeaderResults',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_filter(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'Filter'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'Filter')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='Filter')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.filter(
                namespace_name=request.pop(util.camelize('namespaceName')),
                filter_details=request.pop(util.camelize('FilterDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'Filter',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'filterOutput',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_get_association_summary(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'GetAssociationSummary'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'GetAssociationSummary')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='GetAssociationSummary')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.get_association_summary(
                namespace_name=request.pop(util.camelize('namespaceName')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'GetAssociationSummary',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'associationSummaryReport',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_get_column_names(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'GetColumnNames'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'GetColumnNames')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='GetColumnNames')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.get_column_names(
                namespace_name=request.pop(util.camelize('namespaceName')),
                sql_query=request.pop(util.camelize('sqlQuery')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'GetColumnNames',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'columnNameCollection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_get_config_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'GetConfigWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'GetConfigWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='GetConfigWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.get_config_work_request(
                namespace_name=request.pop(util.camelize('namespaceName')),
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'GetConfigWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsConfigWorkRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_get_field(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'GetField'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'GetField')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='GetField')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.get_field(
                namespace_name=request.pop(util.camelize('namespaceName')),
                field_name=request.pop(util.camelize('fieldName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'GetField',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsField',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_get_fields_summary(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'GetFieldsSummary'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'GetFieldsSummary')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='GetFieldsSummary')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.get_fields_summary(
                namespace_name=request.pop(util.camelize('namespaceName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'GetFieldsSummary',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fieldSummaryReport',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_get_label(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'GetLabel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'GetLabel')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='GetLabel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.get_label(
                namespace_name=request.pop(util.camelize('namespaceName')),
                label_name=request.pop(util.camelize('labelName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'GetLabel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsLabel',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_get_label_summary(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'GetLabelSummary'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'GetLabelSummary')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='GetLabelSummary')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.get_label_summary(
                namespace_name=request.pop(util.camelize('namespaceName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'GetLabelSummary',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'labelSummaryReport',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_get_log_analytics_entities_summary(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'GetLogAnalyticsEntitiesSummary'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'GetLogAnalyticsEntitiesSummary')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='GetLogAnalyticsEntitiesSummary')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.get_log_analytics_entities_summary(
                namespace_name=request.pop(util.camelize('namespaceName')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'GetLogAnalyticsEntitiesSummary',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsEntitySummaryReport',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_get_log_analytics_entity(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'GetLogAnalyticsEntity'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'GetLogAnalyticsEntity')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='GetLogAnalyticsEntity')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.get_log_analytics_entity(
                namespace_name=request.pop(util.camelize('namespaceName')),
                log_analytics_entity_id=request.pop(util.camelize('logAnalyticsEntityId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'GetLogAnalyticsEntity',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsEntity',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_get_log_analytics_entity_type(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'GetLogAnalyticsEntityType'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'GetLogAnalyticsEntityType')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='GetLogAnalyticsEntityType')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.get_log_analytics_entity_type(
                namespace_name=request.pop(util.camelize('namespaceName')),
                entity_type_name=request.pop(util.camelize('entityTypeName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'GetLogAnalyticsEntityType',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsEntityType',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_get_log_analytics_log_group(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'GetLogAnalyticsLogGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'GetLogAnalyticsLogGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='GetLogAnalyticsLogGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.get_log_analytics_log_group(
                namespace_name=request.pop(util.camelize('namespaceName')),
                log_analytics_log_group_id=request.pop(util.camelize('logAnalyticsLogGroupId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'GetLogAnalyticsLogGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsLogGroup',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_get_log_analytics_log_groups_summary(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'GetLogAnalyticsLogGroupsSummary'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'GetLogAnalyticsLogGroupsSummary')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='GetLogAnalyticsLogGroupsSummary')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.get_log_analytics_log_groups_summary(
                namespace_name=request.pop(util.camelize('namespaceName')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'GetLogAnalyticsLogGroupsSummary',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logGroupSummaryReport',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_get_log_analytics_object_collection_rule(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'GetLogAnalyticsObjectCollectionRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'GetLogAnalyticsObjectCollectionRule')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='GetLogAnalyticsObjectCollectionRule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.get_log_analytics_object_collection_rule(
                namespace_name=request.pop(util.camelize('namespaceName')),
                log_analytics_object_collection_rule_id=request.pop(util.camelize('logAnalyticsObjectCollectionRuleId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'GetLogAnalyticsObjectCollectionRule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsObjectCollectionRule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_get_lookup(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'GetLookup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'GetLookup')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='GetLookup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.get_lookup(
                namespace_name=request.pop(util.camelize('namespaceName')),
                lookup_name=request.pop(util.camelize('lookupName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'GetLookup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsLookup',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_get_namespace(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'GetNamespace'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'GetNamespace')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='GetNamespace')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.get_namespace(
                namespace_name=request.pop(util.camelize('namespaceName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'GetNamespace',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'namespace',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_get_parser(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'GetParser'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'GetParser')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='GetParser')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.get_parser(
                namespace_name=request.pop(util.camelize('namespaceName')),
                parser_name=request.pop(util.camelize('parserName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'GetParser',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsParser',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_get_parser_summary(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'GetParserSummary'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'GetParserSummary')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='GetParserSummary')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.get_parser_summary(
                namespace_name=request.pop(util.camelize('namespaceName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'GetParserSummary',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'parserSummaryReport',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_get_query_result(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'GetQueryResult'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'GetQueryResult')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='GetQueryResult')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.get_query_result(
                namespace_name=request.pop(util.camelize('namespaceName')),
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.get_query_result(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    work_request_id=request.pop(util.camelize('workRequestId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.get_query_result(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'GetQueryResult',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'queryAggregation',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_get_query_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'GetQueryWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'GetQueryWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='GetQueryWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.get_query_work_request(
                namespace_name=request.pop(util.camelize('namespaceName')),
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'GetQueryWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'queryWorkRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_get_scheduled_task(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'GetScheduledTask'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'GetScheduledTask')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='GetScheduledTask')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.get_scheduled_task(
                namespace_name=request.pop(util.camelize('namespaceName')),
                scheduled_task_id=request.pop(util.camelize('scheduledTaskId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'GetScheduledTask',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'scheduledTask',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_get_source(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'GetSource'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'GetSource')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='GetSource')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.get_source(
                namespace_name=request.pop(util.camelize('namespaceName')),
                source_name=request.pop(util.camelize('sourceName')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'GetSource',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsSource',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_get_source_summary(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'GetSourceSummary'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'GetSourceSummary')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='GetSourceSummary')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.get_source_summary(
                namespace_name=request.pop(util.camelize('namespaceName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'GetSourceSummary',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sourceSummaryReport',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_get_storage(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'GetStorage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'GetStorage')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='GetStorage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.get_storage(
                namespace_name=request.pop(util.camelize('namespaceName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'GetStorage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'storage',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_get_storage_usage(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'GetStorageUsage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'GetStorageUsage')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='GetStorageUsage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.get_storage_usage(
                namespace_name=request.pop(util.camelize('namespaceName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'GetStorageUsage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'storageUsage',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_get_storage_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'GetStorageWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'GetStorageWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='GetStorageWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.get_storage_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                namespace_name=request.pop(util.camelize('namespaceName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'GetStorageWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'storageWorkRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_get_upload(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'GetUpload'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'GetUpload')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='GetUpload')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.get_upload(
                namespace_name=request.pop(util.camelize('namespaceName')),
                upload_reference=request.pop(util.camelize('uploadReference')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'GetUpload',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'upload',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                namespace_name=request.pop(util.camelize('namespaceName')),
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_import_custom_content(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ImportCustomContent'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ImportCustomContent')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ImportCustomContent')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.import_custom_content(
                namespace_name=request.pop(util.camelize('namespaceName')),
                import_custom_content_file_body=request.pop(util.camelize('ImportCustomContentFileBody')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ImportCustomContent',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsImportCustomContent',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_associated_entities(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListAssociatedEntities'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListAssociatedEntities')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListAssociatedEntities')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_associated_entities(
                namespace_name=request.pop(util.camelize('namespaceName')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_associated_entities(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_associated_entities(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListAssociatedEntities',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsAssociatedEntityCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_config_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListConfigWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListConfigWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListConfigWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_config_work_requests(
                namespace_name=request.pop(util.camelize('namespaceName')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_config_work_requests(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_config_work_requests(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListConfigWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsConfigWorkRequestCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_entity_associations(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListEntityAssociations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListEntityAssociations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListEntityAssociations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_entity_associations(
                namespace_name=request.pop(util.camelize('namespaceName')),
                log_analytics_entity_id=request.pop(util.camelize('logAnalyticsEntityId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_entity_associations(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    log_analytics_entity_id=request.pop(util.camelize('logAnalyticsEntityId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_entity_associations(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        log_analytics_entity_id=request.pop(util.camelize('logAnalyticsEntityId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListEntityAssociations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsEntityCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_entity_source_associations(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListEntitySourceAssociations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListEntitySourceAssociations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListEntitySourceAssociations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_entity_source_associations(
                namespace_name=request.pop(util.camelize('namespaceName')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_entity_source_associations(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_entity_source_associations(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListEntitySourceAssociations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsAssociationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_fields(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListFields'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListFields')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListFields')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_fields(
                namespace_name=request.pop(util.camelize('namespaceName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_fields(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_fields(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListFields',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsFieldCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_label_priorities(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListLabelPriorities'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListLabelPriorities')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListLabelPriorities')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_label_priorities(
                namespace_name=request.pop(util.camelize('namespaceName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_label_priorities(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_label_priorities(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListLabelPriorities',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'labelPriorityCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_label_source_details(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListLabelSourceDetails'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListLabelSourceDetails')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListLabelSourceDetails')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_label_source_details(
                namespace_name=request.pop(util.camelize('namespaceName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_label_source_details(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_label_source_details(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListLabelSourceDetails',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'labelSourceCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_labels(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListLabels'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListLabels')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListLabels')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_labels(
                namespace_name=request.pop(util.camelize('namespaceName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_labels(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_labels(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListLabels',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsLabelCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_log_analytics_entities(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListLogAnalyticsEntities'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListLogAnalyticsEntities')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListLogAnalyticsEntities')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_log_analytics_entities(
                namespace_name=request.pop(util.camelize('namespaceName')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_log_analytics_entities(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_log_analytics_entities(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListLogAnalyticsEntities',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsEntityCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_log_analytics_entity_types(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListLogAnalyticsEntityTypes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListLogAnalyticsEntityTypes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListLogAnalyticsEntityTypes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_log_analytics_entity_types(
                namespace_name=request.pop(util.camelize('namespaceName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_log_analytics_entity_types(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_log_analytics_entity_types(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListLogAnalyticsEntityTypes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsEntityTypeCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_log_analytics_log_groups(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListLogAnalyticsLogGroups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListLogAnalyticsLogGroups')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListLogAnalyticsLogGroups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_log_analytics_log_groups(
                namespace_name=request.pop(util.camelize('namespaceName')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_log_analytics_log_groups(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_log_analytics_log_groups(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListLogAnalyticsLogGroups',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsLogGroupSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_log_analytics_object_collection_rules(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListLogAnalyticsObjectCollectionRules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListLogAnalyticsObjectCollectionRules')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListLogAnalyticsObjectCollectionRules')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_log_analytics_object_collection_rules(
                namespace_name=request.pop(util.camelize('namespaceName')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_log_analytics_object_collection_rules(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_log_analytics_object_collection_rules(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListLogAnalyticsObjectCollectionRules',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsObjectCollectionRuleCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_lookups(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListLookups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListLookups')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListLookups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_lookups(
                namespace_name=request.pop(util.camelize('namespaceName')),
                type=request.pop(util.camelize('type')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_lookups(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    type=request.pop(util.camelize('type')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_lookups(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        type=request.pop(util.camelize('type')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListLookups',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsLookupCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_meta_source_types(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListMetaSourceTypes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListMetaSourceTypes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListMetaSourceTypes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_meta_source_types(
                namespace_name=request.pop(util.camelize('namespaceName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_meta_source_types(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_meta_source_types(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListMetaSourceTypes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsMetaSourceTypeCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_namespaces(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListNamespaces'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListNamespaces')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListNamespaces')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_namespaces(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListNamespaces',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'namespaceCollection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_parser_functions(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListParserFunctions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListParserFunctions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListParserFunctions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_parser_functions(
                namespace_name=request.pop(util.camelize('namespaceName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_parser_functions(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_parser_functions(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListParserFunctions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsParserFunctionCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_parser_meta_plugins(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListParserMetaPlugins'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListParserMetaPlugins')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListParserMetaPlugins')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_parser_meta_plugins(
                namespace_name=request.pop(util.camelize('namespaceName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_parser_meta_plugins(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_parser_meta_plugins(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListParserMetaPlugins',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsParserMetaPluginCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_parsers(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListParsers'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListParsers')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListParsers')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_parsers(
                namespace_name=request.pop(util.camelize('namespaceName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_parsers(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_parsers(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListParsers',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsParserCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_query_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListQueryWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListQueryWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListQueryWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_query_work_requests(
                namespace_name=request.pop(util.camelize('namespaceName')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_query_work_requests(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_query_work_requests(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListQueryWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'queryWorkRequestCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_recalled_data(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListRecalledData'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListRecalledData')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListRecalledData')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_recalled_data(
                namespace_name=request.pop(util.camelize('namespaceName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_recalled_data(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_recalled_data(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListRecalledData',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'recalledDataCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_scheduled_tasks(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListScheduledTasks'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListScheduledTasks')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListScheduledTasks')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_scheduled_tasks(
                namespace_name=request.pop(util.camelize('namespaceName')),
                task_type=request.pop(util.camelize('taskType')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_scheduled_tasks(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    task_type=request.pop(util.camelize('taskType')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_scheduled_tasks(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        task_type=request.pop(util.camelize('taskType')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListScheduledTasks',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'scheduledTaskCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_source_associations(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListSourceAssociations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListSourceAssociations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListSourceAssociations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_source_associations(
                namespace_name=request.pop(util.camelize('namespaceName')),
                source_name=request.pop(util.camelize('sourceName')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_source_associations(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    source_name=request.pop(util.camelize('sourceName')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_source_associations(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        source_name=request.pop(util.camelize('sourceName')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListSourceAssociations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsAssociationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_source_extended_field_definitions(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListSourceExtendedFieldDefinitions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListSourceExtendedFieldDefinitions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListSourceExtendedFieldDefinitions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_source_extended_field_definitions(
                namespace_name=request.pop(util.camelize('namespaceName')),
                source_name=request.pop(util.camelize('sourceName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_source_extended_field_definitions(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    source_name=request.pop(util.camelize('sourceName')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_source_extended_field_definitions(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        source_name=request.pop(util.camelize('sourceName')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListSourceExtendedFieldDefinitions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsSourceExtendedFieldDefinitionCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_source_label_operators(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListSourceLabelOperators'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListSourceLabelOperators')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListSourceLabelOperators')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_source_label_operators(
                namespace_name=request.pop(util.camelize('namespaceName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_source_label_operators(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_source_label_operators(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListSourceLabelOperators',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsLabelOperatorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_source_meta_functions(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListSourceMetaFunctions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListSourceMetaFunctions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListSourceMetaFunctions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_source_meta_functions(
                namespace_name=request.pop(util.camelize('namespaceName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_source_meta_functions(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_source_meta_functions(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListSourceMetaFunctions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsMetaFunctionCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_source_patterns(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListSourcePatterns'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListSourcePatterns')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListSourcePatterns')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_source_patterns(
                namespace_name=request.pop(util.camelize('namespaceName')),
                source_name=request.pop(util.camelize('sourceName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_source_patterns(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    source_name=request.pop(util.camelize('sourceName')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_source_patterns(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        source_name=request.pop(util.camelize('sourceName')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListSourcePatterns',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsSourcePatternCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_sources(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListSources'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListSources')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListSources')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_sources(
                namespace_name=request.pop(util.camelize('namespaceName')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_sources(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_sources(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListSources',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsSourceCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_storage_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListStorageWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListStorageWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListStorageWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_storage_work_request_errors(
                compartment_id=request.pop(util.camelize('compartmentId')),
                work_request_id=request.pop(util.camelize('workRequestId')),
                namespace_name=request.pop(util.camelize('namespaceName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_storage_work_request_errors(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    work_request_id=request.pop(util.camelize('workRequestId')),
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_storage_work_request_errors(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListStorageWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestErrorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_storage_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListStorageWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListStorageWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListStorageWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_storage_work_requests(
                compartment_id=request.pop(util.camelize('compartmentId')),
                namespace_name=request.pop(util.camelize('namespaceName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_storage_work_requests(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_storage_work_requests(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListStorageWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'storageWorkRequestCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_supported_char_encodings(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListSupportedCharEncodings'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListSupportedCharEncodings')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListSupportedCharEncodings')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_supported_char_encodings(
                namespace_name=request.pop(util.camelize('namespaceName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_supported_char_encodings(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_supported_char_encodings(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListSupportedCharEncodings',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'charEncodingCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_supported_timezones(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListSupportedTimezones'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListSupportedTimezones')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListSupportedTimezones')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_supported_timezones(
                namespace_name=request.pop(util.camelize('namespaceName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_supported_timezones(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_supported_timezones(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListSupportedTimezones',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'timezoneCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_upload_files(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListUploadFiles'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListUploadFiles')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListUploadFiles')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_upload_files(
                namespace_name=request.pop(util.camelize('namespaceName')),
                upload_reference=request.pop(util.camelize('uploadReference')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_upload_files(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    upload_reference=request.pop(util.camelize('uploadReference')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_upload_files(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        upload_reference=request.pop(util.camelize('uploadReference')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListUploadFiles',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'uploadFileCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_upload_warnings(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListUploadWarnings'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListUploadWarnings')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListUploadWarnings')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_upload_warnings(
                namespace_name=request.pop(util.camelize('namespaceName')),
                upload_reference=request.pop(util.camelize('uploadReference')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_upload_warnings(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    upload_reference=request.pop(util.camelize('uploadReference')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_upload_warnings(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        upload_reference=request.pop(util.camelize('uploadReference')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListUploadWarnings',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'uploadWarningCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_uploads(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListUploads'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListUploads')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListUploads')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_uploads(
                namespace_name=request.pop(util.camelize('namespaceName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_uploads(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_uploads(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListUploads',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'uploadCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_warnings(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListWarnings'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListWarnings')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListWarnings')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_warnings(
                namespace_name=request.pop(util.camelize('namespaceName')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_warnings(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_warnings(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListWarnings',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsWarningCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_errors(
                namespace_name=request.pop(util.camelize('namespaceName')),
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_errors(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    work_request_id=request.pop(util.camelize('workRequestId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_request_errors(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestErrorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_logs(
                namespace_name=request.pop(util.camelize('namespaceName')),
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_logs(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    work_request_id=request.pop(util.camelize('workRequestId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_request_logs(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_work_requests(
                namespace_name=request.pop(util.camelize('namespaceName')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_requests(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_requests(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_offboard_namespace(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'OffboardNamespace'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'OffboardNamespace')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='OffboardNamespace')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.offboard_namespace(
                namespace_name=request.pop(util.camelize('namespaceName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'OffboardNamespace',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'offboard_namespace',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_onboard_namespace(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'OnboardNamespace'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'OnboardNamespace')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='OnboardNamespace')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.onboard_namespace(
                namespace_name=request.pop(util.camelize('namespaceName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'OnboardNamespace',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'onboard_namespace',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_parse_query(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ParseQuery'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ParseQuery')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ParseQuery')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.parse_query(
                namespace_name=request.pop(util.camelize('namespaceName')),
                parse_query_details=request.pop(util.camelize('ParseQueryDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ParseQuery',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'parseQueryOutput',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_pause_scheduled_task(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'PauseScheduledTask'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'PauseScheduledTask')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='PauseScheduledTask')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.pause_scheduled_task(
                namespace_name=request.pop(util.camelize('namespaceName')),
                scheduled_task_id=request.pop(util.camelize('scheduledTaskId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'PauseScheduledTask',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'scheduledTask',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_purge_storage_data(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'PurgeStorageData'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'PurgeStorageData')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='PurgeStorageData')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.purge_storage_data(
                namespace_name=request.pop(util.camelize('namespaceName')),
                purge_storage_data_details=request.pop(util.camelize('PurgeStorageDataDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'PurgeStorageData',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'purge_storage_data',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_put_query_work_request_background(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'PutQueryWorkRequestBackground'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'PutQueryWorkRequestBackground')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='PutQueryWorkRequestBackground')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.put_query_work_request_background(
                namespace_name=request.pop(util.camelize('namespaceName')),
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'PutQueryWorkRequestBackground',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'queryWorkRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_query(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'Query'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'Query')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='Query')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.query(
                namespace_name=request.pop(util.camelize('namespaceName')),
                query_details=request.pop(util.camelize('QueryDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.query(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    query_details=request.pop(util.camelize('QueryDetails')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.query(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        query_details=request.pop(util.camelize('QueryDetails')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'Query',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'queryAggregation',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_recall_archived_data(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'RecallArchivedData'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'RecallArchivedData')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='RecallArchivedData')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.recall_archived_data(
                namespace_name=request.pop(util.camelize('namespaceName')),
                recall_archived_data_details=request.pop(util.camelize('RecallArchivedDataDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'RecallArchivedData',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'recall_archived_data',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_register_lookup(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'RegisterLookup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'RegisterLookup')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='RegisterLookup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.register_lookup(
                namespace_name=request.pop(util.camelize('namespaceName')),
                type=request.pop(util.camelize('type')),
                register_lookup_content_file_body=request.pop(util.camelize('RegisterLookupContentFileBody')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'RegisterLookup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsLookup',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_release_recalled_data(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ReleaseRecalledData'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ReleaseRecalledData')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ReleaseRecalledData')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.release_recalled_data(
                namespace_name=request.pop(util.camelize('namespaceName')),
                release_recalled_data_details=request.pop(util.camelize('ReleaseRecalledDataDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ReleaseRecalledData',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'release_recalled_data',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_remove_entity_associations(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'RemoveEntityAssociations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'RemoveEntityAssociations')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='RemoveEntityAssociations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.remove_entity_associations(
                namespace_name=request.pop(util.camelize('namespaceName')),
                log_analytics_entity_id=request.pop(util.camelize('logAnalyticsEntityId')),
                remove_entity_associations_details=request.pop(util.camelize('RemoveEntityAssociationsDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'RemoveEntityAssociations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'remove_entity_associations',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_resume_scheduled_task(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ResumeScheduledTask'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ResumeScheduledTask')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ResumeScheduledTask')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.resume_scheduled_task(
                namespace_name=request.pop(util.camelize('namespaceName')),
                scheduled_task_id=request.pop(util.camelize('scheduledTaskId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ResumeScheduledTask',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'scheduledTask',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_run(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'Run'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'Run')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='Run')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.run(
                namespace_name=request.pop(util.camelize('namespaceName')),
                scheduled_task_id=request.pop(util.camelize('scheduledTaskId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'Run',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'run',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_suggest(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'Suggest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'Suggest')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='Suggest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.suggest(
                namespace_name=request.pop(util.camelize('namespaceName')),
                suggest_details=request.pop(util.camelize('SuggestDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'Suggest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'suggestOutput',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_suppress_warning(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'SuppressWarning'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'SuppressWarning')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='SuppressWarning')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.suppress_warning(
                namespace_name=request.pop(util.camelize('namespaceName')),
                warning_reference_details=request.pop(util.camelize('WarningReferenceDetails')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'SuppressWarning',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'suppress_warning',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_test_parser(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'TestParser'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'TestParser')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='TestParser')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.test_parser(
                namespace_name=request.pop(util.camelize('namespaceName')),
                test_parser_payload_details=request.pop(util.camelize('TestParserPayloadDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'TestParser',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'parserTestResult',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_unsuppress_warning(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'UnsuppressWarning'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'UnsuppressWarning')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='UnsuppressWarning')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.unsuppress_warning(
                namespace_name=request.pop(util.camelize('namespaceName')),
                warning_reference_details=request.pop(util.camelize('WarningReferenceDetails')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'UnsuppressWarning',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'unsuppress_warning',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_update_log_analytics_entity(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'UpdateLogAnalyticsEntity'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'UpdateLogAnalyticsEntity')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='UpdateLogAnalyticsEntity')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.update_log_analytics_entity(
                namespace_name=request.pop(util.camelize('namespaceName')),
                log_analytics_entity_id=request.pop(util.camelize('logAnalyticsEntityId')),
                update_log_analytics_entity_details=request.pop(util.camelize('UpdateLogAnalyticsEntityDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'UpdateLogAnalyticsEntity',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsEntity',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_update_log_analytics_entity_type(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'UpdateLogAnalyticsEntityType'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'UpdateLogAnalyticsEntityType')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='UpdateLogAnalyticsEntityType')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.update_log_analytics_entity_type(
                namespace_name=request.pop(util.camelize('namespaceName')),
                update_log_analytics_entity_type_details=request.pop(util.camelize('UpdateLogAnalyticsEntityTypeDetails')),
                entity_type_name=request.pop(util.camelize('entityTypeName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'UpdateLogAnalyticsEntityType',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_log_analytics_entity_type',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_update_log_analytics_log_group(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'UpdateLogAnalyticsLogGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'UpdateLogAnalyticsLogGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='UpdateLogAnalyticsLogGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.update_log_analytics_log_group(
                namespace_name=request.pop(util.camelize('namespaceName')),
                log_analytics_log_group_id=request.pop(util.camelize('logAnalyticsLogGroupId')),
                update_log_analytics_log_group_details=request.pop(util.camelize('UpdateLogAnalyticsLogGroupDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'UpdateLogAnalyticsLogGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsLogGroup',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_update_log_analytics_object_collection_rule(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'UpdateLogAnalyticsObjectCollectionRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'UpdateLogAnalyticsObjectCollectionRule')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='UpdateLogAnalyticsObjectCollectionRule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.update_log_analytics_object_collection_rule(
                namespace_name=request.pop(util.camelize('namespaceName')),
                log_analytics_object_collection_rule_id=request.pop(util.camelize('logAnalyticsObjectCollectionRuleId')),
                update_log_analytics_object_collection_rule_details=request.pop(util.camelize('UpdateLogAnalyticsObjectCollectionRuleDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'UpdateLogAnalyticsObjectCollectionRule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsObjectCollectionRule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_update_lookup(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'UpdateLookup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'UpdateLookup')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='UpdateLookup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.update_lookup(
                namespace_name=request.pop(util.camelize('namespaceName')),
                lookup_name=request.pop(util.camelize('lookupName')),
                update_lookup_metadata_details=request.pop(util.camelize('UpdateLookupMetadataDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'UpdateLookup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsLookup',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_update_lookup_data(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'UpdateLookupData'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'UpdateLookupData')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='UpdateLookupData')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.update_lookup_data(
                namespace_name=request.pop(util.camelize('namespaceName')),
                lookup_name=request.pop(util.camelize('lookupName')),
                update_lookup_file_body=request.pop(util.camelize('UpdateLookupFileBody')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'UpdateLookupData',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_lookup_data',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_update_scheduled_task(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'UpdateScheduledTask'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'UpdateScheduledTask')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='UpdateScheduledTask')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.update_scheduled_task(
                namespace_name=request.pop(util.camelize('namespaceName')),
                scheduled_task_id=request.pop(util.camelize('scheduledTaskId')),
                update_scheduled_task_details=request.pop(util.camelize('UpdateScheduledTaskDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'UpdateScheduledTask',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'scheduledTask',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_update_storage(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'UpdateStorage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'UpdateStorage')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='UpdateStorage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.update_storage(
                namespace_name=request.pop(util.camelize('namespaceName')),
                update_storage_details=request.pop(util.camelize('UpdateStorageDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'UpdateStorage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'storage',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_upload_log_file(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'UploadLogFile'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'UploadLogFile')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='UploadLogFile')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.upload_log_file(
                namespace_name=request.pop(util.camelize('namespaceName')),
                upload_name=request.pop(util.camelize('uploadName')),
                log_source_name=request.pop(util.camelize('logSourceName')),
                filename=request.pop(util.camelize('filename')),
                opc_meta_loggrpid=request.pop(util.camelize('opc-meta-loggrpid')),
                upload_log_file_body=request.pop(util.camelize('UploadLogFileBody')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'UploadLogFile',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'upload',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_upsert_associations(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'UpsertAssociations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'UpsertAssociations')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='UpsertAssociations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.upsert_associations(
                namespace_name=request.pop(util.camelize('namespaceName')),
                upsert_log_analytics_association_details=request.pop(util.camelize('UpsertLogAnalyticsAssociationDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'UpsertAssociations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'upsert_associations',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_upsert_field(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'UpsertField'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'UpsertField')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='UpsertField')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.upsert_field(
                namespace_name=request.pop(util.camelize('namespaceName')),
                upsert_log_analytics_field_details=request.pop(util.camelize('UpsertLogAnalyticsFieldDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'UpsertField',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsField',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_upsert_label(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'UpsertLabel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'UpsertLabel')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='UpsertLabel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.upsert_label(
                namespace_name=request.pop(util.camelize('namespaceName')),
                upsert_log_analytics_label_details=request.pop(util.camelize('UpsertLogAnalyticsLabelDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'UpsertLabel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsLabel',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_upsert_parser(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'UpsertParser'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'UpsertParser')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='UpsertParser')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.upsert_parser(
                namespace_name=request.pop(util.camelize('namespaceName')),
                upsert_log_analytics_parser_details=request.pop(util.camelize('UpsertLogAnalyticsParserDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'UpsertParser',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsParser',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_upsert_source(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'UpsertSource'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'UpsertSource')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='UpsertSource')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.upsert_source(
                namespace_name=request.pop(util.camelize('namespaceName')),
                upsert_log_analytics_source_details=request.pop(util.camelize('UpsertLogAnalyticsSourceDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'UpsertSource',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsSource',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_validate_association_parameters(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ValidateAssociationParameters'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ValidateAssociationParameters')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ValidateAssociationParameters')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.validate_association_parameters(
                namespace_name=request.pop(util.camelize('namespaceName')),
                upsert_log_analytics_association_details=request.pop(util.camelize('UpsertLogAnalyticsAssociationDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.validate_association_parameters(
                    namespace_name=request.pop(util.camelize('namespaceName')),
                    upsert_log_analytics_association_details=request.pop(util.camelize('UpsertLogAnalyticsAssociationDetails')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.validate_association_parameters(
                        namespace_name=request.pop(util.camelize('namespaceName')),
                        upsert_log_analytics_association_details=request.pop(util.camelize('UpsertLogAnalyticsAssociationDetails')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ValidateAssociationParameters',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'logAnalyticsAssociationParameterCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_validate_file(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ValidateFile'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ValidateFile')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ValidateFile')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.validate_file(
                namespace_name=request.pop(util.camelize('namespaceName')),
                object_location=request.pop(util.camelize('objectLocation')),
                filename=request.pop(util.camelize('filename')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ValidateFile',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fileValidationResponse',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_validate_source(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ValidateSource'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ValidateSource')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ValidateSource')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.validate_source(
                namespace_name=request.pop(util.camelize('namespaceName')),
                upsert_log_analytics_source_details=request.pop(util.camelize('UpsertLogAnalyticsSourceDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ValidateSource',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sourceValidateResults',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_validate_source_extended_field_details(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ValidateSourceExtendedFieldDetails'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ValidateSourceExtendedFieldDetails')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ValidateSourceExtendedFieldDetails')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.validate_source_extended_field_details(
                namespace_name=request.pop(util.camelize('namespaceName')),
                log_analytics_source=request.pop(util.camelize('LogAnalyticsSource')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ValidateSourceExtendedFieldDetails',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'extendedFieldsValidationResult',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omc_loganalytics_dev_ww_grp@oracle.com" jiraProject="LOGAN" opsJiraProject="LOGAN"
def test_validate_source_mapping(testing_service_client):
    if not testing_service_client.is_api_enabled('log_analytics', 'ValidateSourceMapping'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('log_analytics', util.camelize('log_analytics'), 'ValidateSourceMapping')
    )

    request_containers = testing_service_client.get_requests(service_name='log_analytics', api_name='ValidateSourceMapping')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.log_analytics.LogAnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.validate_source_mapping(
                namespace_name=request.pop(util.camelize('namespaceName')),
                object_location=request.pop(util.camelize('objectLocation')),
                filename=request.pop(util.camelize('filename')),
                log_source_name=request.pop(util.camelize('logSourceName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'log_analytics',
            'ValidateSourceMapping',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sourceMappingResponse',
            False,
            False
        )
