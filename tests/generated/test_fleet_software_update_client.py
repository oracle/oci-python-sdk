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

        cassette_location = os.path.join('generated', 'fleet_software_update_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_abort_fsu_discovery(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'AbortFsuDiscovery'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'AbortFsuDiscovery')
    )

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='AbortFsuDiscovery')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.abort_fsu_discovery(
                fsu_discovery_id=request.pop(util.camelize('fsuDiscoveryId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'AbortFsuDiscovery',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'abort_fsu_discovery',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_add_fsu_collection_targets(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'AddFsuCollectionTargets'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'AddFsuCollectionTargets')
    )

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='AddFsuCollectionTargets')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.add_fsu_collection_targets(
                fsu_collection_id=request.pop(util.camelize('fsuCollectionId')),
                add_fsu_collection_targets_details=request.pop(util.camelize('AddFsuCollectionTargetsDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'AddFsuCollectionTargets',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'add_fsu_collection_targets',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_cancel_fsu_action(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'CancelFsuAction'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'CancelFsuAction')
    )

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='CancelFsuAction')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.cancel_fsu_action(
                fsu_action_id=request.pop(util.camelize('fsuActionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'CancelFsuAction',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cancel_fsu_action',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_change_fsu_action_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'ChangeFsuActionCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'ChangeFsuActionCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='ChangeFsuActionCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.change_fsu_action_compartment(
                fsu_action_id=request.pop(util.camelize('fsuActionId')),
                change_fsu_action_compartment_details=request.pop(util.camelize('ChangeFsuActionCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'ChangeFsuActionCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_fsu_action_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_change_fsu_collection_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'ChangeFsuCollectionCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'ChangeFsuCollectionCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='ChangeFsuCollectionCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.change_fsu_collection_compartment(
                fsu_collection_id=request.pop(util.camelize('fsuCollectionId')),
                change_fsu_collection_compartment_details=request.pop(util.camelize('ChangeFsuCollectionCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'ChangeFsuCollectionCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_fsu_collection_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_change_fsu_cycle_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'ChangeFsuCycleCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'ChangeFsuCycleCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='ChangeFsuCycleCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.change_fsu_cycle_compartment(
                fsu_cycle_id=request.pop(util.camelize('fsuCycleId')),
                change_fsu_cycle_compartment_details=request.pop(util.camelize('ChangeFsuCycleCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'ChangeFsuCycleCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_fsu_cycle_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_change_fsu_discovery_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'ChangeFsuDiscoveryCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'ChangeFsuDiscoveryCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='ChangeFsuDiscoveryCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.change_fsu_discovery_compartment(
                fsu_discovery_id=request.pop(util.camelize('fsuDiscoveryId')),
                change_fsu_discovery_compartment_details=request.pop(util.camelize('ChangeFsuDiscoveryCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'ChangeFsuDiscoveryCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_fsu_discovery_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_clone_fsu_cycle(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'CloneFsuCycle'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'CloneFsuCycle')
    )

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='CloneFsuCycle')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.clone_fsu_cycle(
                fsu_cycle_id=request.pop(util.camelize('fsuCycleId')),
                clone_fsu_cycle_details=request.pop(util.camelize('CloneFsuCycleDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'CloneFsuCycle',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fsuCycle',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_create_fsu_action(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'CreateFsuAction'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'CreateFsuAction')
    )

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='CreateFsuAction')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.create_fsu_action(
                create_fsu_action_details=request.pop(util.camelize('CreateFsuActionDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'CreateFsuAction',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fsuAction',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_create_fsu_collection(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'CreateFsuCollection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'CreateFsuCollection')
    )

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='CreateFsuCollection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.create_fsu_collection(
                create_fsu_collection_details=request.pop(util.camelize('CreateFsuCollectionDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'CreateFsuCollection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fsuCollection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_create_fsu_cycle(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'CreateFsuCycle'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'CreateFsuCycle')
    )

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='CreateFsuCycle')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.create_fsu_cycle(
                create_fsu_cycle_details=request.pop(util.camelize('CreateFsuCycleDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'CreateFsuCycle',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fsuCycle',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_create_fsu_discovery(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'CreateFsuDiscovery'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'CreateFsuDiscovery')
    )

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='CreateFsuDiscovery')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.create_fsu_discovery(
                create_fsu_discovery_details=request.pop(util.camelize('CreateFsuDiscoveryDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'CreateFsuDiscovery',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fsuDiscovery',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_delete_fsu_action(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'DeleteFsuAction'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'DeleteFsuAction')
    )

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='DeleteFsuAction')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.delete_fsu_action(
                fsu_action_id=request.pop(util.camelize('fsuActionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'DeleteFsuAction',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_fsu_action',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_delete_fsu_collection(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'DeleteFsuCollection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'DeleteFsuCollection')
    )

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='DeleteFsuCollection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.delete_fsu_collection(
                fsu_collection_id=request.pop(util.camelize('fsuCollectionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'DeleteFsuCollection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_fsu_collection',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_delete_fsu_cycle(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'DeleteFsuCycle'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'DeleteFsuCycle')
    )

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='DeleteFsuCycle')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.delete_fsu_cycle(
                fsu_cycle_id=request.pop(util.camelize('fsuCycleId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'DeleteFsuCycle',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_fsu_cycle',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_delete_fsu_discovery(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'DeleteFsuDiscovery'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'DeleteFsuDiscovery')
    )

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='DeleteFsuDiscovery')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.delete_fsu_discovery(
                fsu_discovery_id=request.pop(util.camelize('fsuDiscoveryId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'DeleteFsuDiscovery',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_fsu_discovery',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_delete_fsu_job(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'DeleteFsuJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'DeleteFsuJob')
    )

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='DeleteFsuJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.delete_fsu_job(
                fsu_job_id=request.pop(util.camelize('fsuJobId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'DeleteFsuJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_fsu_job',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_get_fsu_action(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'GetFsuAction'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'GetFsuAction')
    )

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='GetFsuAction')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.get_fsu_action(
                fsu_action_id=request.pop(util.camelize('fsuActionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'GetFsuAction',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fsuAction',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_get_fsu_action_output_content(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'GetFsuActionOutputContent'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'GetFsuActionOutputContent')
    )

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='GetFsuActionOutputContent')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.get_fsu_action_output_content(
                fsu_action_id=request.pop(util.camelize('fsuActionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'GetFsuActionOutputContent',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_get_fsu_collection(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'GetFsuCollection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'GetFsuCollection')
    )

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='GetFsuCollection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.get_fsu_collection(
                fsu_collection_id=request.pop(util.camelize('fsuCollectionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'GetFsuCollection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fsuCollection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_get_fsu_cycle(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'GetFsuCycle'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'GetFsuCycle')
    )

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='GetFsuCycle')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.get_fsu_cycle(
                fsu_cycle_id=request.pop(util.camelize('fsuCycleId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'GetFsuCycle',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fsuCycle',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_get_fsu_discovery(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'GetFsuDiscovery'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'GetFsuDiscovery')
    )

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='GetFsuDiscovery')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.get_fsu_discovery(
                fsu_discovery_id=request.pop(util.camelize('fsuDiscoveryId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'GetFsuDiscovery',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fsuDiscovery',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_get_fsu_job(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'GetFsuJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'GetFsuJob')
    )

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='GetFsuJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.get_fsu_job(
                fsu_job_id=request.pop(util.camelize('fsuJobId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'GetFsuJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fsuJob',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_get_fsu_job_output_content(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'GetFsuJobOutputContent'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'GetFsuJobOutputContent')
    )

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='GetFsuJobOutputContent')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.get_fsu_job_output_content(
                fsu_job_id=request.pop(util.camelize('fsuJobId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'GetFsuJobOutputContent',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_list_fsu_actions(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'ListFsuActions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'ListFsuActions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='ListFsuActions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.list_fsu_actions(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_fsu_actions(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_fsu_actions(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'ListFsuActions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fsuActionSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_list_fsu_collection_targets(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'ListFsuCollectionTargets'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'ListFsuCollectionTargets')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='ListFsuCollectionTargets')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.list_fsu_collection_targets(
                fsu_collection_id=request.pop(util.camelize('fsuCollectionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_fsu_collection_targets(
                    fsu_collection_id=request.pop(util.camelize('fsuCollectionId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_fsu_collection_targets(
                        fsu_collection_id=request.pop(util.camelize('fsuCollectionId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'ListFsuCollectionTargets',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'targetSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_list_fsu_collections(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'ListFsuCollections'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'ListFsuCollections')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='ListFsuCollections')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.list_fsu_collections(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_fsu_collections(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_fsu_collections(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'ListFsuCollections',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fsuCollectionSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_list_fsu_cycles(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'ListFsuCycles'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'ListFsuCycles')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='ListFsuCycles')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.list_fsu_cycles(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_fsu_cycles(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_fsu_cycles(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'ListFsuCycles',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fsuCycleSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_list_fsu_discoveries(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'ListFsuDiscoveries'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'ListFsuDiscoveries')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='ListFsuDiscoveries')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.list_fsu_discoveries(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_fsu_discoveries(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_fsu_discoveries(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'ListFsuDiscoveries',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fsuDiscoverySummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_list_fsu_discovery_targets(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'ListFsuDiscoveryTargets'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'ListFsuDiscoveryTargets')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='ListFsuDiscoveryTargets')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.list_fsu_discovery_targets(
                fsu_discovery_id=request.pop(util.camelize('fsuDiscoveryId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_fsu_discovery_targets(
                    fsu_discovery_id=request.pop(util.camelize('fsuDiscoveryId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_fsu_discovery_targets(
                        fsu_discovery_id=request.pop(util.camelize('fsuDiscoveryId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'ListFsuDiscoveryTargets',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'targetSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_list_fsu_job_outputs(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'ListFsuJobOutputs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'ListFsuJobOutputs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='ListFsuJobOutputs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.list_fsu_job_outputs(
                fsu_job_id=request.pop(util.camelize('fsuJobId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_fsu_job_outputs(
                    fsu_job_id=request.pop(util.camelize('fsuJobId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_fsu_job_outputs(
                        fsu_job_id=request.pop(util.camelize('fsuJobId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'ListFsuJobOutputs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fsuJobOutputSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_list_fsu_jobs(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'ListFsuJobs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'ListFsuJobs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='ListFsuJobs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.list_fsu_jobs(
                fsu_action_id=request.pop(util.camelize('fsuActionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_fsu_jobs(
                    fsu_action_id=request.pop(util.camelize('fsuActionId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_fsu_jobs(
                        fsu_action_id=request.pop(util.camelize('fsuActionId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'ListFsuJobs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fsuJobCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
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
            'fleet_software_update',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestErrorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
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
            'fleet_software_update',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
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
            'fleet_software_update',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_remove_fsu_collection_targets(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'RemoveFsuCollectionTargets'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'RemoveFsuCollectionTargets')
    )

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='RemoveFsuCollectionTargets')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.remove_fsu_collection_targets(
                fsu_collection_id=request.pop(util.camelize('fsuCollectionId')),
                remove_fsu_collection_targets_details=request.pop(util.camelize('RemoveFsuCollectionTargetsDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'RemoveFsuCollectionTargets',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'remove_fsu_collection_targets',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_resume_fsu_action(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'ResumeFsuAction'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'ResumeFsuAction')
    )

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='ResumeFsuAction')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.resume_fsu_action(
                fsu_action_id=request.pop(util.camelize('fsuActionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'ResumeFsuAction',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'resume_fsu_action',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_retry_fsu_job(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'RetryFsuJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'RetryFsuJob')
    )

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='RetryFsuJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.retry_fsu_job(
                fsu_job_id=request.pop(util.camelize('fsuJobId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'RetryFsuJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'retry_fsu_job',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_update_fsu_action(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'UpdateFsuAction'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'UpdateFsuAction')
    )

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='UpdateFsuAction')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.update_fsu_action(
                fsu_action_id=request.pop(util.camelize('fsuActionId')),
                update_fsu_action_details=request.pop(util.camelize('UpdateFsuActionDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'UpdateFsuAction',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_fsu_action',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_update_fsu_collection(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'UpdateFsuCollection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'UpdateFsuCollection')
    )

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='UpdateFsuCollection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.update_fsu_collection(
                fsu_collection_id=request.pop(util.camelize('fsuCollectionId')),
                update_fsu_collection_details=request.pop(util.camelize('UpdateFsuCollectionDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'UpdateFsuCollection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_fsu_collection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_update_fsu_cycle(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'UpdateFsuCycle'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'UpdateFsuCycle')
    )

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='UpdateFsuCycle')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.update_fsu_cycle(
                fsu_cycle_id=request.pop(util.camelize('fsuCycleId')),
                update_fsu_cycle_details=request.pop(util.camelize('UpdateFsuCycleDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'UpdateFsuCycle',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_fsu_cycle',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_update_fsu_discovery(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'UpdateFsuDiscovery'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'UpdateFsuDiscovery')
    )

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='UpdateFsuDiscovery')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.update_fsu_discovery(
                fsu_discovery_id=request.pop(util.camelize('fsuDiscoveryId')),
                update_fsu_discovery_details=request.pop(util.camelize('UpdateFsuDiscoveryDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'UpdateFsuDiscovery',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_fsu_discovery',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fppcsdev_ww_grp@oracle.com" jiraProject="FPPCS" opsJiraProject="FPPCS"
def test_update_fsu_job(testing_service_client):
    if not testing_service_client.is_api_enabled('fleet_software_update', 'UpdateFsuJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fleet_software_update', util.camelize('fleet_software_update'), 'UpdateFsuJob')
    )

    request_containers = testing_service_client.get_requests(service_name='fleet_software_update', api_name='UpdateFsuJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fleet_software_update.FleetSoftwareUpdateClient(config, service_endpoint=service_endpoint)
            response = client.update_fsu_job(
                fsu_job_id=request.pop(util.camelize('fsuJobId')),
                update_fsu_job_details=request.pop(util.camelize('UpdateFsuJobDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fleet_software_update',
            'UpdateFsuJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fsuJob',
            False,
            False
        )
