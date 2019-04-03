# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

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
    # use the default matching logic (link below) with the exception of 'session_agnostic_query_matcher'
    # instead of 'query' matcher (which ignores sessionId in the url)
    # https://vcrpy.readthedocs.io/en/latest/configuration.html#request-matching
    custom_vcr = test_config_container.create_vcr()
    custom_vcr.register_matcher('session_agnostic_query_matcher', session_agnostic_query_matcher)

    cassette_location = os.path.join('generated', 'monitoring_{name}.yml'.format(name=request.function.__name__))
    with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
        yield


# IssueRoutingInfo tag="default" email="pic_ion_dev_grp@oracle.com" jiraProject="https://jira.oci.oraclecorp.com/projects/TEL" opsJiraProject="https://jira-sd.mc1.oracleiaas.com/projects/TEL"
def test_create_alarm(testing_service_client):
    if not testing_service_client.is_api_enabled('monitoring', 'CreateAlarm'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('monitoring', util.camelize('monitoring'), 'CreateAlarm')
    )

    request_containers = testing_service_client.get_requests(service_name='monitoring', api_name='CreateAlarm')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.monitoring.MonitoringClient(config)
            response = client.create_alarm(
                create_alarm_details=request.pop(util.camelize('create_alarm_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'monitoring',
            'CreateAlarm',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'alarm',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="pic_ion_dev_grp@oracle.com" jiraProject="https://jira.oci.oraclecorp.com/projects/TEL" opsJiraProject="https://jira-sd.mc1.oracleiaas.com/projects/TEL"
def test_delete_alarm(testing_service_client):
    if not testing_service_client.is_api_enabled('monitoring', 'DeleteAlarm'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('monitoring', util.camelize('monitoring'), 'DeleteAlarm')
    )

    request_containers = testing_service_client.get_requests(service_name='monitoring', api_name='DeleteAlarm')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.monitoring.MonitoringClient(config)
            response = client.delete_alarm(
                alarm_id=request.pop(util.camelize('alarm_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'monitoring',
            'DeleteAlarm',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_alarm',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="pic_ion_dev_grp@oracle.com" jiraProject="https://jira.oci.oraclecorp.com/projects/TEL" opsJiraProject="https://jira-sd.mc1.oracleiaas.com/projects/TEL"
def test_get_alarm(testing_service_client):
    if not testing_service_client.is_api_enabled('monitoring', 'GetAlarm'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('monitoring', util.camelize('monitoring'), 'GetAlarm')
    )

    request_containers = testing_service_client.get_requests(service_name='monitoring', api_name='GetAlarm')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.monitoring.MonitoringClient(config)
            response = client.get_alarm(
                alarm_id=request.pop(util.camelize('alarm_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'monitoring',
            'GetAlarm',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'alarm',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="pic_ion_dev_grp@oracle.com" jiraProject="https://jira.oci.oraclecorp.com/projects/TEL" opsJiraProject="https://jira-sd.mc1.oracleiaas.com/projects/TEL"
def test_get_alarm_history(testing_service_client):
    if not testing_service_client.is_api_enabled('monitoring', 'GetAlarmHistory'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('monitoring', util.camelize('monitoring'), 'GetAlarmHistory')
    )

    request_containers = testing_service_client.get_requests(service_name='monitoring', api_name='GetAlarmHistory')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.monitoring.MonitoringClient(config)
            response = client.get_alarm_history(
                alarm_id=request.pop(util.camelize('alarm_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.get_alarm_history(
                    alarm_id=request.pop(util.camelize('alarm_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.get_alarm_history(
                        alarm_id=request.pop(util.camelize('alarm_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'monitoring',
            'GetAlarmHistory',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'alarmHistoryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="pic_ion_dev_grp@oracle.com" jiraProject="https://jira.oci.oraclecorp.com/projects/TEL" opsJiraProject="https://jira-sd.mc1.oracleiaas.com/projects/TEL"
def test_list_alarms(testing_service_client):
    if not testing_service_client.is_api_enabled('monitoring', 'ListAlarms'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('monitoring', util.camelize('monitoring'), 'ListAlarms')
    )

    request_containers = testing_service_client.get_requests(service_name='monitoring', api_name='ListAlarms')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.monitoring.MonitoringClient(config)
            response = client.list_alarms(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_alarms(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_alarms(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'monitoring',
            'ListAlarms',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'alarmSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="pic_ion_dev_grp@oracle.com" jiraProject="https://jira.oci.oraclecorp.com/projects/TEL" opsJiraProject="https://jira-sd.mc1.oracleiaas.com/projects/TEL"
def test_list_alarms_status(testing_service_client):
    if not testing_service_client.is_api_enabled('monitoring', 'ListAlarmsStatus'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('monitoring', util.camelize('monitoring'), 'ListAlarmsStatus')
    )

    request_containers = testing_service_client.get_requests(service_name='monitoring', api_name='ListAlarmsStatus')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.monitoring.MonitoringClient(config)
            response = client.list_alarms_status(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_alarms_status(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_alarms_status(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'monitoring',
            'ListAlarmsStatus',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'alarmStatusSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="pic_ion_dev_grp@oracle.com" jiraProject="https://jira.oci.oraclecorp.com/projects/TEL" opsJiraProject="https://jira-sd.mc1.oracleiaas.com/projects/TEL"
def test_list_metrics(testing_service_client):
    if not testing_service_client.is_api_enabled('monitoring', 'ListMetrics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('monitoring', util.camelize('monitoring'), 'ListMetrics')
    )

    request_containers = testing_service_client.get_requests(service_name='monitoring', api_name='ListMetrics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.monitoring.MonitoringClient(config)
            response = client.list_metrics(
                compartment_id=request.pop(util.camelize('compartment_id')),
                list_metrics_details=request.pop(util.camelize('list_metrics_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_metrics(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    list_metrics_details=request.pop(util.camelize('list_metrics_details')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_metrics(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        list_metrics_details=request.pop(util.camelize('list_metrics_details')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'monitoring',
            'ListMetrics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'metric',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="pic_ion_dev_grp@oracle.com" jiraProject="https://jira.oci.oraclecorp.com/projects/TEL" opsJiraProject="https://jira-sd.mc1.oracleiaas.com/projects/TEL"
def test_post_metric_data(testing_service_client):
    if not testing_service_client.is_api_enabled('monitoring', 'PostMetricData'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('monitoring', util.camelize('monitoring'), 'PostMetricData')
    )

    request_containers = testing_service_client.get_requests(service_name='monitoring', api_name='PostMetricData')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.monitoring.MonitoringClient(config)
            response = client.post_metric_data(
                post_metric_data_details=request.pop(util.camelize('post_metric_data_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'monitoring',
            'PostMetricData',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'postMetricDataResponseDetails',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="pic_ion_dev_grp@oracle.com" jiraProject="https://jira.oci.oraclecorp.com/projects/TEL" opsJiraProject="https://jira-sd.mc1.oracleiaas.com/projects/TEL"
def test_remove_alarm_suppression(testing_service_client):
    if not testing_service_client.is_api_enabled('monitoring', 'RemoveAlarmSuppression'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('monitoring', util.camelize('monitoring'), 'RemoveAlarmSuppression')
    )

    request_containers = testing_service_client.get_requests(service_name='monitoring', api_name='RemoveAlarmSuppression')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.monitoring.MonitoringClient(config)
            response = client.remove_alarm_suppression(
                alarm_id=request.pop(util.camelize('alarm_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'monitoring',
            'RemoveAlarmSuppression',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'remove_alarm_suppression',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="pic_ion_dev_grp@oracle.com" jiraProject="https://jira.oci.oraclecorp.com/projects/TEL" opsJiraProject="https://jira-sd.mc1.oracleiaas.com/projects/TEL"
def test_summarize_metrics_data(testing_service_client):
    if not testing_service_client.is_api_enabled('monitoring', 'SummarizeMetricsData'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('monitoring', util.camelize('monitoring'), 'SummarizeMetricsData')
    )

    request_containers = testing_service_client.get_requests(service_name='monitoring', api_name='SummarizeMetricsData')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.monitoring.MonitoringClient(config)
            response = client.summarize_metrics_data(
                compartment_id=request.pop(util.camelize('compartment_id')),
                summarize_metrics_data_details=request.pop(util.camelize('summarize_metrics_data_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'monitoring',
            'SummarizeMetricsData',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'metricData',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="pic_ion_dev_grp@oracle.com" jiraProject="https://jira.oci.oraclecorp.com/projects/TEL" opsJiraProject="https://jira-sd.mc1.oracleiaas.com/projects/TEL"
def test_update_alarm(testing_service_client):
    if not testing_service_client.is_api_enabled('monitoring', 'UpdateAlarm'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('monitoring', util.camelize('monitoring'), 'UpdateAlarm')
    )

    request_containers = testing_service_client.get_requests(service_name='monitoring', api_name='UpdateAlarm')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.monitoring.MonitoringClient(config)
            response = client.update_alarm(
                alarm_id=request.pop(util.camelize('alarm_id')),
                update_alarm_details=request.pop(util.camelize('update_alarm_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'monitoring',
            'UpdateAlarm',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'alarm',
            False,
            False
        )
