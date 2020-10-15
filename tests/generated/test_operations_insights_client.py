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

        cassette_location = os.path.join('generated', 'opsi_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="sqlLoader" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_ingest_sql_bucket(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'IngestSqlBucket'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'IngestSqlBucket')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='IngestSqlBucket')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.ingest_sql_bucket(
                compartment_id=request.pop(util.camelize('compartmentId')),
                database_id=request.pop(util.camelize('databaseId')),
                ingest_sql_bucket_details=request.pop(util.camelize('IngestSqlBucketDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'IngestSqlBucket',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'ingestSqlBucketResponseDetails',
            False,
            False
        )


# IssueRoutingInfo tag="sqlLoader" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_ingest_sql_plan_lines(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'IngestSqlPlanLines'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'IngestSqlPlanLines')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='IngestSqlPlanLines')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.ingest_sql_plan_lines(
                compartment_id=request.pop(util.camelize('compartmentId')),
                database_id=request.pop(util.camelize('databaseId')),
                ingest_sql_plan_lines_details=request.pop(util.camelize('IngestSqlPlanLinesDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'IngestSqlPlanLines',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'ingestSqlPlanLinesResponseDetails',
            False,
            False
        )


# IssueRoutingInfo tag="sqlLoader" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_ingest_sql_text(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'IngestSqlText'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'IngestSqlText')
    )

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='IngestSqlText')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.ingest_sql_text(
                compartment_id=request.pop(util.camelize('compartmentId')),
                database_id=request.pop(util.camelize('databaseId')),
                ingest_sql_text_details=request.pop(util.camelize('IngestSqlTextDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'IngestSqlText',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'ingestSqlTextResponseDetails',
            False,
            False
        )


# IssueRoutingInfo tag="resourcePlanning" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_list_database_insights(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ListDatabaseInsights'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ListDatabaseInsights')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ListDatabaseInsights')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.list_database_insights(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_database_insights(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_database_insights(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ListDatabaseInsights',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'databaseInsightsCollection',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_list_sql_plans(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ListSqlPlans'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ListSqlPlans')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ListSqlPlans')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.list_sql_plans(
                compartment_id=request.pop(util.camelize('compartmentId')),
                database_id=request.pop(util.camelize('databaseId')),
                sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                plan_hash=request.pop(util.camelize('planHash')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_sql_plans(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    database_id=request.pop(util.camelize('databaseId')),
                    sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                    plan_hash=request.pop(util.camelize('planHash')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_sql_plans(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        database_id=request.pop(util.camelize('databaseId')),
                        sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                        plan_hash=request.pop(util.camelize('planHash')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ListSqlPlans',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sqlPlanCollection',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_list_sql_searches(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ListSqlSearches'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ListSqlSearches')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ListSqlSearches')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.list_sql_searches(
                compartment_id=request.pop(util.camelize('compartmentId')),
                sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_sql_searches(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_sql_searches(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ListSqlSearches',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sqlSearchCollection',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_list_sql_texts(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'ListSqlTexts'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'ListSqlTexts')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='ListSqlTexts')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.list_sql_texts(
                compartment_id=request.pop(util.camelize('compartmentId')),
                sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_sql_texts(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_sql_texts(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'ListSqlTexts',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sqlTextCollection',
            False,
            True
        )


# IssueRoutingInfo tag="resourcePlanning" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_database_insight_resource_capacity_trend(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeDatabaseInsightResourceCapacityTrend'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeDatabaseInsightResourceCapacityTrend')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeDatabaseInsightResourceCapacityTrend')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_database_insight_resource_capacity_trend(
                compartment_id=request.pop(util.camelize('compartmentId')),
                resource_metric=request.pop(util.camelize('resourceMetric')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_database_insight_resource_capacity_trend(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    resource_metric=request.pop(util.camelize('resourceMetric')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_database_insight_resource_capacity_trend(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        resource_metric=request.pop(util.camelize('resourceMetric')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeDatabaseInsightResourceCapacityTrend',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'summarizeDatabaseInsightResourceCapacityTrendAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="resourcePlanning" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_database_insight_resource_forecast_trend(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeDatabaseInsightResourceForecastTrend'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeDatabaseInsightResourceForecastTrend')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeDatabaseInsightResourceForecastTrend')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_database_insight_resource_forecast_trend(
                compartment_id=request.pop(util.camelize('compartmentId')),
                resource_metric=request.pop(util.camelize('resourceMetric')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_database_insight_resource_forecast_trend(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    resource_metric=request.pop(util.camelize('resourceMetric')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_database_insight_resource_forecast_trend(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        resource_metric=request.pop(util.camelize('resourceMetric')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeDatabaseInsightResourceForecastTrend',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'summarizeDatabaseInsightResourceForecastTrendAggregation',
            False,
            True
        )


# IssueRoutingInfo tag="resourcePlanning" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_database_insight_resource_statistics(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeDatabaseInsightResourceStatistics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeDatabaseInsightResourceStatistics')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeDatabaseInsightResourceStatistics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_database_insight_resource_statistics(
                compartment_id=request.pop(util.camelize('compartmentId')),
                resource_metric=request.pop(util.camelize('resourceMetric')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_database_insight_resource_statistics(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    resource_metric=request.pop(util.camelize('resourceMetric')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_database_insight_resource_statistics(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        resource_metric=request.pop(util.camelize('resourceMetric')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeDatabaseInsightResourceStatistics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'summarizeDatabaseInsightResourceStatisticsAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="resourcePlanning" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_database_insight_resource_usage(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeDatabaseInsightResourceUsage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeDatabaseInsightResourceUsage')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeDatabaseInsightResourceUsage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_database_insight_resource_usage(
                compartment_id=request.pop(util.camelize('compartmentId')),
                resource_metric=request.pop(util.camelize('resourceMetric')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_database_insight_resource_usage(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    resource_metric=request.pop(util.camelize('resourceMetric')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_database_insight_resource_usage(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        resource_metric=request.pop(util.camelize('resourceMetric')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeDatabaseInsightResourceUsage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'summarizeDatabaseInsightResourceUsageAggregation',
            False,
            True
        )


# IssueRoutingInfo tag="resourcePlanning" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_database_insight_resource_usage_trend(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeDatabaseInsightResourceUsageTrend'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeDatabaseInsightResourceUsageTrend')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeDatabaseInsightResourceUsageTrend')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_database_insight_resource_usage_trend(
                compartment_id=request.pop(util.camelize('compartmentId')),
                resource_metric=request.pop(util.camelize('resourceMetric')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_database_insight_resource_usage_trend(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    resource_metric=request.pop(util.camelize('resourceMetric')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_database_insight_resource_usage_trend(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        resource_metric=request.pop(util.camelize('resourceMetric')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeDatabaseInsightResourceUsageTrend',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'summarizeDatabaseInsightResourceUsageTrendAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="resourcePlanning" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_database_insight_resource_utilization_insight(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeDatabaseInsightResourceUtilizationInsight'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeDatabaseInsightResourceUtilizationInsight')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeDatabaseInsightResourceUtilizationInsight')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_database_insight_resource_utilization_insight(
                compartment_id=request.pop(util.camelize('compartmentId')),
                resource_metric=request.pop(util.camelize('resourceMetric')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_database_insight_resource_utilization_insight(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    resource_metric=request.pop(util.camelize('resourceMetric')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_database_insight_resource_utilization_insight(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        resource_metric=request.pop(util.camelize('resourceMetric')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeDatabaseInsightResourceUtilizationInsight',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'summarizeDatabaseInsightResourceUtilizationInsightAggregation',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_sql_insights(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeSqlInsights'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeSqlInsights')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeSqlInsights')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_sql_insights(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_sql_insights(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_sql_insights(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeSqlInsights',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sqlInsightAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_sql_plan_insights(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeSqlPlanInsights'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeSqlPlanInsights')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeSqlPlanInsights')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_sql_plan_insights(
                compartment_id=request.pop(util.camelize('compartmentId')),
                database_id=request.pop(util.camelize('databaseId')),
                sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_sql_plan_insights(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    database_id=request.pop(util.camelize('databaseId')),
                    sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_sql_plan_insights(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        database_id=request.pop(util.camelize('databaseId')),
                        sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeSqlPlanInsights',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sqlPlanInsightAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_sql_response_time_distributions(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeSqlResponseTimeDistributions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeSqlResponseTimeDistributions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeSqlResponseTimeDistributions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_sql_response_time_distributions(
                compartment_id=request.pop(util.camelize('compartmentId')),
                database_id=request.pop(util.camelize('databaseId')),
                sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_sql_response_time_distributions(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    database_id=request.pop(util.camelize('databaseId')),
                    sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_sql_response_time_distributions(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        database_id=request.pop(util.camelize('databaseId')),
                        sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeSqlResponseTimeDistributions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sqlResponseTimeDistributionAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_sql_statistics(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeSqlStatistics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeSqlStatistics')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeSqlStatistics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_sql_statistics(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_sql_statistics(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_sql_statistics(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeSqlStatistics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sqlStatisticAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_sql_statistics_time_series(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeSqlStatisticsTimeSeries'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeSqlStatisticsTimeSeries')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeSqlStatisticsTimeSeries')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_sql_statistics_time_series(
                compartment_id=request.pop(util.camelize('compartmentId')),
                sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_sql_statistics_time_series(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_sql_statistics_time_series(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeSqlStatisticsTimeSeries',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sqlStatisticsTimeSeriesAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="sqlWarehouse" email="dbx_dev_ww_grp@oracle.com" jiraProject="DBX" opsJiraProject="DBXSD"
def test_summarize_sql_statistics_time_series_by_plan(testing_service_client):
    if not testing_service_client.is_api_enabled('opsi', 'SummarizeSqlStatisticsTimeSeriesByPlan'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opsi', util.camelize('operations_insights'), 'SummarizeSqlStatisticsTimeSeriesByPlan')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opsi', api_name='SummarizeSqlStatisticsTimeSeriesByPlan')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opsi.OperationsInsightsClient(config, service_endpoint=service_endpoint)
            response = client.summarize_sql_statistics_time_series_by_plan(
                compartment_id=request.pop(util.camelize('compartmentId')),
                database_id=request.pop(util.camelize('databaseId')),
                sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_sql_statistics_time_series_by_plan(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    database_id=request.pop(util.camelize('databaseId')),
                    sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_sql_statistics_time_series_by_plan(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        database_id=request.pop(util.camelize('databaseId')),
                        sql_identifier=request.pop(util.camelize('sqlIdentifier')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opsi',
            'SummarizeSqlStatisticsTimeSeriesByPlan',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sqlStatisticsTimeSeriesByPlanAggregationCollection',
            False,
            True
        )
