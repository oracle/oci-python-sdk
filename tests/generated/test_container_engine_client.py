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

    cassette_location = os.path.join('generated', 'container_engine_{name}.yml'.format(name=request.function.__name__))
    with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
        yield


def test_create_cluster(testing_service_client, config):
    if not testing_service_client.is_api_enabled('container_engine', 'CreateCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='CreateCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.container_engine.ContainerEngineClient(config)
            response = client.create_cluster(
                create_cluster_details=request.pop(util.camelize('create_cluster_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'CreateCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_cluster',
            False,
            False
        )


def test_create_kubeconfig(testing_service_client, config):
    if not testing_service_client.is_api_enabled('container_engine', 'CreateKubeconfig'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='CreateKubeconfig')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.container_engine.ContainerEngineClient(config)
            response = client.create_kubeconfig(
                cluster_id=request.pop(util.camelize('cluster_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'CreateKubeconfig',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


def test_create_node_pool(testing_service_client, config):
    if not testing_service_client.is_api_enabled('container_engine', 'CreateNodePool'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='CreateNodePool')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.container_engine.ContainerEngineClient(config)
            response = client.create_node_pool(
                create_node_pool_details=request.pop(util.camelize('create_node_pool_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'CreateNodePool',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_node_pool',
            False,
            False
        )


def test_delete_cluster(testing_service_client, config):
    if not testing_service_client.is_api_enabled('container_engine', 'DeleteCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='DeleteCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.container_engine.ContainerEngineClient(config)
            response = client.delete_cluster(
                cluster_id=request.pop(util.camelize('cluster_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'DeleteCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_cluster',
            True,
            False
        )


def test_delete_node_pool(testing_service_client, config):
    if not testing_service_client.is_api_enabled('container_engine', 'DeleteNodePool'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='DeleteNodePool')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.container_engine.ContainerEngineClient(config)
            response = client.delete_node_pool(
                node_pool_id=request.pop(util.camelize('node_pool_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'DeleteNodePool',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_node_pool',
            True,
            False
        )


def test_delete_work_request(testing_service_client, config):
    if not testing_service_client.is_api_enabled('container_engine', 'DeleteWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='DeleteWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.container_engine.ContainerEngineClient(config)
            response = client.delete_work_request(
                work_request_id=request.pop(util.camelize('work_request_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'DeleteWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_work_request',
            True,
            False
        )


def test_get_cluster(testing_service_client, config):
    if not testing_service_client.is_api_enabled('container_engine', 'GetCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='GetCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.container_engine.ContainerEngineClient(config)
            response = client.get_cluster(
                cluster_id=request.pop(util.camelize('cluster_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'GetCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cluster',
            False,
            False
        )


def test_get_cluster_options(testing_service_client, config):
    if not testing_service_client.is_api_enabled('container_engine', 'GetClusterOptions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='GetClusterOptions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.container_engine.ContainerEngineClient(config)
            response = client.get_cluster_options(
                cluster_option_id=request.pop(util.camelize('cluster_option_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'GetClusterOptions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'clusterOptions',
            False,
            False
        )


def test_get_node_pool(testing_service_client, config):
    if not testing_service_client.is_api_enabled('container_engine', 'GetNodePool'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='GetNodePool')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.container_engine.ContainerEngineClient(config)
            response = client.get_node_pool(
                node_pool_id=request.pop(util.camelize('node_pool_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'GetNodePool',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'nodePool',
            False,
            False
        )


def test_get_node_pool_options(testing_service_client, config):
    if not testing_service_client.is_api_enabled('container_engine', 'GetNodePoolOptions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='GetNodePoolOptions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.container_engine.ContainerEngineClient(config)
            response = client.get_node_pool_options(
                node_pool_option_id=request.pop(util.camelize('node_pool_option_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'GetNodePoolOptions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'nodePoolOptions',
            False,
            False
        )


def test_get_work_request(testing_service_client, config):
    if not testing_service_client.is_api_enabled('container_engine', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.container_engine.ContainerEngineClient(config)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('work_request_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


def test_list_clusters(testing_service_client, config):
    if not testing_service_client.is_api_enabled('container_engine', 'ListClusters'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='ListClusters')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.container_engine.ContainerEngineClient(config)
            response = client.list_clusters(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_clusters(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_clusters(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'ListClusters',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'clusterSummary',
            False,
            True
        )


def test_list_node_pools(testing_service_client, config):
    if not testing_service_client.is_api_enabled('container_engine', 'ListNodePools'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='ListNodePools')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.container_engine.ContainerEngineClient(config)
            response = client.list_node_pools(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_node_pools(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_node_pools(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'ListNodePools',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'nodePoolSummary',
            False,
            True
        )


def test_list_work_request_errors(testing_service_client, config):
    if not testing_service_client.is_api_enabled('container_engine', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.container_engine.ContainerEngineClient(config)
            response = client.list_work_request_errors(
                compartment_id=request.pop(util.camelize('compartment_id')),
                work_request_id=request.pop(util.camelize('work_request_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestError',
            False,
            False
        )


def test_list_work_request_logs(testing_service_client, config):
    if not testing_service_client.is_api_enabled('container_engine', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.container_engine.ContainerEngineClient(config)
            response = client.list_work_request_logs(
                compartment_id=request.pop(util.camelize('compartment_id')),
                work_request_id=request.pop(util.camelize('work_request_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntry',
            False,
            False
        )


def test_list_work_requests(testing_service_client, config):
    if not testing_service_client.is_api_enabled('container_engine', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.container_engine.ContainerEngineClient(config)
            response = client.list_work_requests(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_requests(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_requests(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestSummary',
            False,
            True
        )


def test_update_cluster(testing_service_client, config):
    if not testing_service_client.is_api_enabled('container_engine', 'UpdateCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='UpdateCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.container_engine.ContainerEngineClient(config)
            response = client.update_cluster(
                cluster_id=request.pop(util.camelize('cluster_id')),
                update_cluster_details=request.pop(util.camelize('update_cluster_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'UpdateCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_cluster',
            False,
            False
        )


def test_update_node_pool(testing_service_client, config):
    if not testing_service_client.is_api_enabled('container_engine', 'UpdateNodePool'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='UpdateNodePool')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.container_engine.ContainerEngineClient(config)
            response = client.update_node_pool(
                node_pool_id=request.pop(util.camelize('node_pool_id')),
                update_node_pool_details=request.pop(util.camelize('update_node_pool_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'UpdateNodePool',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_node_pool',
            False,
            False
        )


