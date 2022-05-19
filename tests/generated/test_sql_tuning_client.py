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

        cassette_location = os.path.join('generated', 'database_management_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_clone_sql_tuning_task(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'CloneSqlTuningTask'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('sql_tuning'), 'CloneSqlTuningTask')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='CloneSqlTuningTask')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.SqlTuningClient(config, service_endpoint=service_endpoint)
            response = client.clone_sql_tuning_task(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                clone_sql_tuning_task_details=request.pop(util.camelize('CloneSqlTuningTaskDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'CloneSqlTuningTask',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sqlTuningTaskReturn',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_drop_sql_tuning_task(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'DropSqlTuningTask'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('sql_tuning'), 'DropSqlTuningTask')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='DropSqlTuningTask')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.SqlTuningClient(config, service_endpoint=service_endpoint)
            response = client.drop_sql_tuning_task(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                drop_sql_tuning_task_details=request.pop(util.camelize('DropSqlTuningTaskDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'DropSqlTuningTask',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'drop_sql_tuning_task',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_execution_plan_stats_comparision(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetExecutionPlanStatsComparision'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('sql_tuning'), 'GetExecutionPlanStatsComparision')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetExecutionPlanStatsComparision')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.SqlTuningClient(config, service_endpoint=service_endpoint)
            response = client.get_execution_plan_stats_comparision(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                sql_tuning_advisor_task_id=request.pop(util.camelize('sqlTuningAdvisorTaskId')),
                sql_object_id=request.pop(util.camelize('sqlObjectId')),
                execution_id=request.pop(util.camelize('executionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetExecutionPlanStatsComparision',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'executionPlanStatsComparision',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_sql_execution_plan(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetSqlExecutionPlan'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('sql_tuning'), 'GetSqlExecutionPlan')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetSqlExecutionPlan')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.SqlTuningClient(config, service_endpoint=service_endpoint)
            response = client.get_sql_execution_plan(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                sql_tuning_advisor_task_id=request.pop(util.camelize('sqlTuningAdvisorTaskId')),
                sql_object_id=request.pop(util.camelize('sqlObjectId')),
                attribute=request.pop(util.camelize('attribute')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetSqlExecutionPlan',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sqlTuningAdvisorTaskSqlExecutionPlan',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_sql_tuning_advisor_task_summary_report(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetSqlTuningAdvisorTaskSummaryReport'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('sql_tuning'), 'GetSqlTuningAdvisorTaskSummaryReport')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetSqlTuningAdvisorTaskSummaryReport')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.SqlTuningClient(config, service_endpoint=service_endpoint)
            response = client.get_sql_tuning_advisor_task_summary_report(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                sql_tuning_advisor_task_id=request.pop(util.camelize('sqlTuningAdvisorTaskId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetSqlTuningAdvisorTaskSummaryReport',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sqlTuningAdvisorTaskSummaryReport',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_sql_tuning_advisor_task_findings(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListSqlTuningAdvisorTaskFindings'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('sql_tuning'), 'ListSqlTuningAdvisorTaskFindings')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListSqlTuningAdvisorTaskFindings')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.SqlTuningClient(config, service_endpoint=service_endpoint)
            response = client.list_sql_tuning_advisor_task_findings(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                sql_tuning_advisor_task_id=request.pop(util.camelize('sqlTuningAdvisorTaskId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_sql_tuning_advisor_task_findings(
                    managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                    sql_tuning_advisor_task_id=request.pop(util.camelize('sqlTuningAdvisorTaskId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_sql_tuning_advisor_task_findings(
                        managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                        sql_tuning_advisor_task_id=request.pop(util.camelize('sqlTuningAdvisorTaskId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListSqlTuningAdvisorTaskFindings',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sqlTuningAdvisorTaskFindingCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_sql_tuning_advisor_task_recommendations(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListSqlTuningAdvisorTaskRecommendations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('sql_tuning'), 'ListSqlTuningAdvisorTaskRecommendations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListSqlTuningAdvisorTaskRecommendations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.SqlTuningClient(config, service_endpoint=service_endpoint)
            response = client.list_sql_tuning_advisor_task_recommendations(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                sql_tuning_advisor_task_id=request.pop(util.camelize('sqlTuningAdvisorTaskId')),
                sql_object_id=request.pop(util.camelize('sqlObjectId')),
                execution_id=request.pop(util.camelize('executionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_sql_tuning_advisor_task_recommendations(
                    managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                    sql_tuning_advisor_task_id=request.pop(util.camelize('sqlTuningAdvisorTaskId')),
                    sql_object_id=request.pop(util.camelize('sqlObjectId')),
                    execution_id=request.pop(util.camelize('executionId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_sql_tuning_advisor_task_recommendations(
                        managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                        sql_tuning_advisor_task_id=request.pop(util.camelize('sqlTuningAdvisorTaskId')),
                        sql_object_id=request.pop(util.camelize('sqlObjectId')),
                        execution_id=request.pop(util.camelize('executionId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListSqlTuningAdvisorTaskRecommendations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sqlTuningAdvisorTaskRecommendationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_sql_tuning_advisor_tasks(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListSqlTuningAdvisorTasks'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('sql_tuning'), 'ListSqlTuningAdvisorTasks')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListSqlTuningAdvisorTasks')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.SqlTuningClient(config, service_endpoint=service_endpoint)
            response = client.list_sql_tuning_advisor_tasks(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_sql_tuning_advisor_tasks(
                    managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_sql_tuning_advisor_tasks(
                        managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListSqlTuningAdvisorTasks',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sqlTuningAdvisorTaskCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_start_sql_tuning_task(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'StartSqlTuningTask'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('sql_tuning'), 'StartSqlTuningTask')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='StartSqlTuningTask')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.SqlTuningClient(config, service_endpoint=service_endpoint)
            response = client.start_sql_tuning_task(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                start_sql_tuning_task_details=request.pop(util.camelize('StartSqlTuningTaskDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'StartSqlTuningTask',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sqlTuningTaskReturn',
            False,
            False
        )
