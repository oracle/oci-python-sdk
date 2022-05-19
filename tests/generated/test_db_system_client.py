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

        cassette_location = os.path.join('generated', 'mysql_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="mysql-cloud-dev_ww_grp@oracle.com" jiraProject="MY" opsJiraProject="MYOPS"
def test_add_analytics_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('mysql', 'AddAnalyticsCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('mysql', util.camelize('db_system'), 'AddAnalyticsCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='mysql', api_name='AddAnalyticsCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.mysql.DbSystemClient(config, service_endpoint=service_endpoint)
            response = client.add_analytics_cluster(
                db_system_id=request.pop(util.camelize('dbSystemId')),
                add_analytics_cluster_details=request.pop(util.camelize('AddAnalyticsClusterDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'mysql',
            'AddAnalyticsCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'analyticsCluster',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="mysql-cloud-dev_ww_grp@oracle.com" jiraProject="MY" opsJiraProject="MYOPS"
def test_add_heat_wave_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('mysql', 'AddHeatWaveCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('mysql', util.camelize('db_system'), 'AddHeatWaveCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='mysql', api_name='AddHeatWaveCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.mysql.DbSystemClient(config, service_endpoint=service_endpoint)
            response = client.add_heat_wave_cluster(
                db_system_id=request.pop(util.camelize('dbSystemId')),
                add_heat_wave_cluster_details=request.pop(util.camelize('AddHeatWaveClusterDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'mysql',
            'AddHeatWaveCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'heatWaveCluster',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="mysql-cloud-dev_ww_grp@oracle.com" jiraProject="MY" opsJiraProject="MYOPS"
def test_create_db_system(testing_service_client):
    if not testing_service_client.is_api_enabled('mysql', 'CreateDbSystem'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('mysql', util.camelize('db_system'), 'CreateDbSystem')
    )

    request_containers = testing_service_client.get_requests(service_name='mysql', api_name='CreateDbSystem')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.mysql.DbSystemClient(config, service_endpoint=service_endpoint)
            response = client.create_db_system(
                create_db_system_details=request.pop(util.camelize('CreateDbSystemDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'mysql',
            'CreateDbSystem',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dbSystem',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="mysql-cloud-dev_ww_grp@oracle.com" jiraProject="MY" opsJiraProject="MYOPS"
def test_delete_analytics_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('mysql', 'DeleteAnalyticsCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('mysql', util.camelize('db_system'), 'DeleteAnalyticsCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='mysql', api_name='DeleteAnalyticsCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.mysql.DbSystemClient(config, service_endpoint=service_endpoint)
            response = client.delete_analytics_cluster(
                db_system_id=request.pop(util.camelize('dbSystemId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'mysql',
            'DeleteAnalyticsCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_analytics_cluster',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="mysql-cloud-dev_ww_grp@oracle.com" jiraProject="MY" opsJiraProject="MYOPS"
def test_delete_db_system(testing_service_client):
    if not testing_service_client.is_api_enabled('mysql', 'DeleteDbSystem'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('mysql', util.camelize('db_system'), 'DeleteDbSystem')
    )

    request_containers = testing_service_client.get_requests(service_name='mysql', api_name='DeleteDbSystem')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.mysql.DbSystemClient(config, service_endpoint=service_endpoint)
            response = client.delete_db_system(
                db_system_id=request.pop(util.camelize('dbSystemId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'mysql',
            'DeleteDbSystem',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_db_system',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="mysql-cloud-dev_ww_grp@oracle.com" jiraProject="MY" opsJiraProject="MYOPS"
def test_delete_heat_wave_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('mysql', 'DeleteHeatWaveCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('mysql', util.camelize('db_system'), 'DeleteHeatWaveCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='mysql', api_name='DeleteHeatWaveCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.mysql.DbSystemClient(config, service_endpoint=service_endpoint)
            response = client.delete_heat_wave_cluster(
                db_system_id=request.pop(util.camelize('dbSystemId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'mysql',
            'DeleteHeatWaveCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_heat_wave_cluster',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="mysql-cloud-dev_ww_grp@oracle.com" jiraProject="MY" opsJiraProject="MYOPS"
def test_generate_analytics_cluster_memory_estimate(testing_service_client):
    if not testing_service_client.is_api_enabled('mysql', 'GenerateAnalyticsClusterMemoryEstimate'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('mysql', util.camelize('db_system'), 'GenerateAnalyticsClusterMemoryEstimate')
    )

    request_containers = testing_service_client.get_requests(service_name='mysql', api_name='GenerateAnalyticsClusterMemoryEstimate')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.mysql.DbSystemClient(config, service_endpoint=service_endpoint)
            response = client.generate_analytics_cluster_memory_estimate(
                db_system_id=request.pop(util.camelize('dbSystemId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'mysql',
            'GenerateAnalyticsClusterMemoryEstimate',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'analyticsClusterMemoryEstimate',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="mysql-cloud-dev_ww_grp@oracle.com" jiraProject="MY" opsJiraProject="MYOPS"
def test_generate_heat_wave_cluster_memory_estimate(testing_service_client):
    if not testing_service_client.is_api_enabled('mysql', 'GenerateHeatWaveClusterMemoryEstimate'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('mysql', util.camelize('db_system'), 'GenerateHeatWaveClusterMemoryEstimate')
    )

    request_containers = testing_service_client.get_requests(service_name='mysql', api_name='GenerateHeatWaveClusterMemoryEstimate')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.mysql.DbSystemClient(config, service_endpoint=service_endpoint)
            response = client.generate_heat_wave_cluster_memory_estimate(
                db_system_id=request.pop(util.camelize('dbSystemId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'mysql',
            'GenerateHeatWaveClusterMemoryEstimate',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'heatWaveClusterMemoryEstimate',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="mysql-cloud-dev_ww_grp@oracle.com" jiraProject="MY" opsJiraProject="MYOPS"
def test_get_analytics_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('mysql', 'GetAnalyticsCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('mysql', util.camelize('db_system'), 'GetAnalyticsCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='mysql', api_name='GetAnalyticsCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.mysql.DbSystemClient(config, service_endpoint=service_endpoint)
            response = client.get_analytics_cluster(
                db_system_id=request.pop(util.camelize('dbSystemId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'mysql',
            'GetAnalyticsCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'analyticsCluster',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="mysql-cloud-dev_ww_grp@oracle.com" jiraProject="MY" opsJiraProject="MYOPS"
def test_get_analytics_cluster_memory_estimate(testing_service_client):
    if not testing_service_client.is_api_enabled('mysql', 'GetAnalyticsClusterMemoryEstimate'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('mysql', util.camelize('db_system'), 'GetAnalyticsClusterMemoryEstimate')
    )

    request_containers = testing_service_client.get_requests(service_name='mysql', api_name='GetAnalyticsClusterMemoryEstimate')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.mysql.DbSystemClient(config, service_endpoint=service_endpoint)
            response = client.get_analytics_cluster_memory_estimate(
                db_system_id=request.pop(util.camelize('dbSystemId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'mysql',
            'GetAnalyticsClusterMemoryEstimate',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'analyticsClusterMemoryEstimate',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="mysql-cloud-dev_ww_grp@oracle.com" jiraProject="MY" opsJiraProject="MYOPS"
def test_get_db_system(testing_service_client):
    if not testing_service_client.is_api_enabled('mysql', 'GetDbSystem'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('mysql', util.camelize('db_system'), 'GetDbSystem')
    )

    request_containers = testing_service_client.get_requests(service_name='mysql', api_name='GetDbSystem')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.mysql.DbSystemClient(config, service_endpoint=service_endpoint)
            response = client.get_db_system(
                db_system_id=request.pop(util.camelize('dbSystemId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'mysql',
            'GetDbSystem',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dbSystem',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="mysql-cloud-dev_ww_grp@oracle.com" jiraProject="MY" opsJiraProject="MYOPS"
def test_get_heat_wave_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('mysql', 'GetHeatWaveCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('mysql', util.camelize('db_system'), 'GetHeatWaveCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='mysql', api_name='GetHeatWaveCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.mysql.DbSystemClient(config, service_endpoint=service_endpoint)
            response = client.get_heat_wave_cluster(
                db_system_id=request.pop(util.camelize('dbSystemId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'mysql',
            'GetHeatWaveCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'heatWaveCluster',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="mysql-cloud-dev_ww_grp@oracle.com" jiraProject="MY" opsJiraProject="MYOPS"
def test_get_heat_wave_cluster_memory_estimate(testing_service_client):
    if not testing_service_client.is_api_enabled('mysql', 'GetHeatWaveClusterMemoryEstimate'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('mysql', util.camelize('db_system'), 'GetHeatWaveClusterMemoryEstimate')
    )

    request_containers = testing_service_client.get_requests(service_name='mysql', api_name='GetHeatWaveClusterMemoryEstimate')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.mysql.DbSystemClient(config, service_endpoint=service_endpoint)
            response = client.get_heat_wave_cluster_memory_estimate(
                db_system_id=request.pop(util.camelize('dbSystemId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'mysql',
            'GetHeatWaveClusterMemoryEstimate',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'heatWaveClusterMemoryEstimate',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="mysql-cloud-dev_ww_grp@oracle.com" jiraProject="MY" opsJiraProject="MYOPS"
def test_list_db_systems(testing_service_client):
    if not testing_service_client.is_api_enabled('mysql', 'ListDbSystems'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('mysql', util.camelize('db_system'), 'ListDbSystems')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='mysql', api_name='ListDbSystems')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.mysql.DbSystemClient(config, service_endpoint=service_endpoint)
            response = client.list_db_systems(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_db_systems(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_db_systems(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'mysql',
            'ListDbSystems',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dbSystemSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="mysql-cloud-dev_ww_grp@oracle.com" jiraProject="MY" opsJiraProject="MYOPS"
def test_restart_analytics_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('mysql', 'RestartAnalyticsCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('mysql', util.camelize('db_system'), 'RestartAnalyticsCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='mysql', api_name='RestartAnalyticsCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.mysql.DbSystemClient(config, service_endpoint=service_endpoint)
            response = client.restart_analytics_cluster(
                db_system_id=request.pop(util.camelize('dbSystemId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'mysql',
            'RestartAnalyticsCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'restart_analytics_cluster',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="mysql-cloud-dev_ww_grp@oracle.com" jiraProject="MY" opsJiraProject="MYOPS"
def test_restart_db_system(testing_service_client):
    if not testing_service_client.is_api_enabled('mysql', 'RestartDbSystem'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('mysql', util.camelize('db_system'), 'RestartDbSystem')
    )

    request_containers = testing_service_client.get_requests(service_name='mysql', api_name='RestartDbSystem')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.mysql.DbSystemClient(config, service_endpoint=service_endpoint)
            response = client.restart_db_system(
                db_system_id=request.pop(util.camelize('dbSystemId')),
                restart_db_system_details=request.pop(util.camelize('RestartDbSystemDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'mysql',
            'RestartDbSystem',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'restart_db_system',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="mysql-cloud-dev_ww_grp@oracle.com" jiraProject="MY" opsJiraProject="MYOPS"
def test_restart_heat_wave_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('mysql', 'RestartHeatWaveCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('mysql', util.camelize('db_system'), 'RestartHeatWaveCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='mysql', api_name='RestartHeatWaveCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.mysql.DbSystemClient(config, service_endpoint=service_endpoint)
            response = client.restart_heat_wave_cluster(
                db_system_id=request.pop(util.camelize('dbSystemId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'mysql',
            'RestartHeatWaveCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'restart_heat_wave_cluster',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="mysql-cloud-dev_ww_grp@oracle.com" jiraProject="MY" opsJiraProject="MYOPS"
def test_start_analytics_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('mysql', 'StartAnalyticsCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('mysql', util.camelize('db_system'), 'StartAnalyticsCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='mysql', api_name='StartAnalyticsCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.mysql.DbSystemClient(config, service_endpoint=service_endpoint)
            response = client.start_analytics_cluster(
                db_system_id=request.pop(util.camelize('dbSystemId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'mysql',
            'StartAnalyticsCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'start_analytics_cluster',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="mysql-cloud-dev_ww_grp@oracle.com" jiraProject="MY" opsJiraProject="MYOPS"
def test_start_db_system(testing_service_client):
    if not testing_service_client.is_api_enabled('mysql', 'StartDbSystem'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('mysql', util.camelize('db_system'), 'StartDbSystem')
    )

    request_containers = testing_service_client.get_requests(service_name='mysql', api_name='StartDbSystem')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.mysql.DbSystemClient(config, service_endpoint=service_endpoint)
            response = client.start_db_system(
                db_system_id=request.pop(util.camelize('dbSystemId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'mysql',
            'StartDbSystem',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'start_db_system',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="mysql-cloud-dev_ww_grp@oracle.com" jiraProject="MY" opsJiraProject="MYOPS"
def test_start_heat_wave_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('mysql', 'StartHeatWaveCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('mysql', util.camelize('db_system'), 'StartHeatWaveCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='mysql', api_name='StartHeatWaveCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.mysql.DbSystemClient(config, service_endpoint=service_endpoint)
            response = client.start_heat_wave_cluster(
                db_system_id=request.pop(util.camelize('dbSystemId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'mysql',
            'StartHeatWaveCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'start_heat_wave_cluster',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="mysql-cloud-dev_ww_grp@oracle.com" jiraProject="MY" opsJiraProject="MYOPS"
def test_stop_analytics_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('mysql', 'StopAnalyticsCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('mysql', util.camelize('db_system'), 'StopAnalyticsCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='mysql', api_name='StopAnalyticsCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.mysql.DbSystemClient(config, service_endpoint=service_endpoint)
            response = client.stop_analytics_cluster(
                db_system_id=request.pop(util.camelize('dbSystemId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'mysql',
            'StopAnalyticsCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stop_analytics_cluster',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="mysql-cloud-dev_ww_grp@oracle.com" jiraProject="MY" opsJiraProject="MYOPS"
def test_stop_db_system(testing_service_client):
    if not testing_service_client.is_api_enabled('mysql', 'StopDbSystem'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('mysql', util.camelize('db_system'), 'StopDbSystem')
    )

    request_containers = testing_service_client.get_requests(service_name='mysql', api_name='StopDbSystem')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.mysql.DbSystemClient(config, service_endpoint=service_endpoint)
            response = client.stop_db_system(
                db_system_id=request.pop(util.camelize('dbSystemId')),
                stop_db_system_details=request.pop(util.camelize('StopDbSystemDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'mysql',
            'StopDbSystem',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stop_db_system',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="mysql-cloud-dev_ww_grp@oracle.com" jiraProject="MY" opsJiraProject="MYOPS"
def test_stop_heat_wave_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('mysql', 'StopHeatWaveCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('mysql', util.camelize('db_system'), 'StopHeatWaveCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='mysql', api_name='StopHeatWaveCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.mysql.DbSystemClient(config, service_endpoint=service_endpoint)
            response = client.stop_heat_wave_cluster(
                db_system_id=request.pop(util.camelize('dbSystemId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'mysql',
            'StopHeatWaveCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stop_heat_wave_cluster',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="mysql-cloud-dev_ww_grp@oracle.com" jiraProject="MY" opsJiraProject="MYOPS"
def test_update_analytics_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('mysql', 'UpdateAnalyticsCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('mysql', util.camelize('db_system'), 'UpdateAnalyticsCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='mysql', api_name='UpdateAnalyticsCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.mysql.DbSystemClient(config, service_endpoint=service_endpoint)
            response = client.update_analytics_cluster(
                db_system_id=request.pop(util.camelize('dbSystemId')),
                update_analytics_cluster_details=request.pop(util.camelize('UpdateAnalyticsClusterDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'mysql',
            'UpdateAnalyticsCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_analytics_cluster',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="mysql-cloud-dev_ww_grp@oracle.com" jiraProject="MY" opsJiraProject="MYOPS"
def test_update_db_system(testing_service_client):
    if not testing_service_client.is_api_enabled('mysql', 'UpdateDbSystem'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('mysql', util.camelize('db_system'), 'UpdateDbSystem')
    )

    request_containers = testing_service_client.get_requests(service_name='mysql', api_name='UpdateDbSystem')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.mysql.DbSystemClient(config, service_endpoint=service_endpoint)
            response = client.update_db_system(
                db_system_id=request.pop(util.camelize('dbSystemId')),
                update_db_system_details=request.pop(util.camelize('UpdateDbSystemDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'mysql',
            'UpdateDbSystem',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_db_system',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="mysql-cloud-dev_ww_grp@oracle.com" jiraProject="MY" opsJiraProject="MYOPS"
def test_update_heat_wave_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('mysql', 'UpdateHeatWaveCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('mysql', util.camelize('db_system'), 'UpdateHeatWaveCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='mysql', api_name='UpdateHeatWaveCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.mysql.DbSystemClient(config, service_endpoint=service_endpoint)
            response = client.update_heat_wave_cluster(
                db_system_id=request.pop(util.camelize('dbSystemId')),
                update_heat_wave_cluster_details=request.pop(util.camelize('UpdateHeatWaveClusterDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'mysql',
            'UpdateHeatWaveCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_heat_wave_cluster',
            False,
            False
        )
