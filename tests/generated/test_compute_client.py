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

        cassette_location = os.path.join('generated', 'core_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="sic_block_storage_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BS"
def test_accept_shielded_integrity_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'AcceptShieldedIntegrityPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'AcceptShieldedIntegrityPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='AcceptShieldedIntegrityPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.accept_shielded_integrity_policy(
                instance_id=request.pop(util.camelize('instanceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'AcceptShieldedIntegrityPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'accept_shielded_integrity_policy',
            False,
            False
        )


# IssueRoutingInfo tag="computeImaging" email="imaging_dev_us_grp@oracle.com" jiraProject="COM" opsJiraProject="COM"
def test_add_image_shape_compatibility_entry(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'AddImageShapeCompatibilityEntry'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'AddImageShapeCompatibilityEntry')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='AddImageShapeCompatibilityEntry')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.add_image_shape_compatibility_entry(
                image_id=request.pop(util.camelize('imageId')),
                shape_name=request.pop(util.camelize('shapeName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'AddImageShapeCompatibilityEntry',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'imageShapeCompatibilityEntry',
            False,
            False
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_attach_boot_volume(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'AttachBootVolume'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'AttachBootVolume')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='AttachBootVolume')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.attach_boot_volume(
                attach_boot_volume_details=request.pop(util.camelize('AttachBootVolumeDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'AttachBootVolume',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bootVolumeAttachment',
            False,
            False
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_attach_vnic(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'AttachVnic'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'AttachVnic')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='AttachVnic')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.attach_vnic(
                attach_vnic_details=request.pop(util.camelize('AttachVnicDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'AttachVnic',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'vnicAttachment',
            False,
            False
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_attach_volume(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'AttachVolume'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'AttachVolume')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='AttachVolume')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.attach_volume(
                attach_volume_details=request.pop(util.camelize('AttachVolumeDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'AttachVolume',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'volumeAttachment',
            False,
            False
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_capture_console_history(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CaptureConsoleHistory'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'CaptureConsoleHistory')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CaptureConsoleHistory')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.capture_console_history(
                capture_console_history_details=request.pop(util.camelize('CaptureConsoleHistoryDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CaptureConsoleHistory',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'consoleHistory',
            False,
            False
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_change_compute_capacity_reservation_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ChangeComputeCapacityReservationCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'ChangeComputeCapacityReservationCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ChangeComputeCapacityReservationCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.change_compute_capacity_reservation_compartment(
                capacity_reservation_id=request.pop(util.camelize('capacityReservationId')),
                change_compute_capacity_reservation_compartment_details=request.pop(util.camelize('ChangeComputeCapacityReservationCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ChangeComputeCapacityReservationCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_compute_capacity_reservation_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="computeImaging" email="imaging_dev_us_grp@oracle.com" jiraProject="COM" opsJiraProject="COM"
def test_change_compute_image_capability_schema_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ChangeComputeImageCapabilitySchemaCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'ChangeComputeImageCapabilitySchemaCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ChangeComputeImageCapabilitySchemaCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.change_compute_image_capability_schema_compartment(
                compute_image_capability_schema_id=request.pop(util.camelize('computeImageCapabilitySchemaId')),
                change_compute_image_capability_schema_compartment_details=request.pop(util.camelize('ChangeComputeImageCapabilitySchemaCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ChangeComputeImageCapabilitySchemaCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_compute_image_capability_schema_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_change_dedicated_vm_host_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ChangeDedicatedVmHostCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'ChangeDedicatedVmHostCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ChangeDedicatedVmHostCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.change_dedicated_vm_host_compartment(
                dedicated_vm_host_id=request.pop(util.camelize('dedicatedVmHostId')),
                change_dedicated_vm_host_compartment_details=request.pop(util.camelize('ChangeDedicatedVmHostCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ChangeDedicatedVmHostCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_dedicated_vm_host_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="computeImaging" email="imaging_dev_us_grp@oracle.com" jiraProject="COM" opsJiraProject="COM"
def test_change_image_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ChangeImageCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'ChangeImageCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ChangeImageCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.change_image_compartment(
                image_id=request.pop(util.camelize('imageId')),
                change_image_compartment_details=request.pop(util.camelize('ChangeImageCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ChangeImageCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_image_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_change_instance_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ChangeInstanceCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'ChangeInstanceCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ChangeInstanceCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.change_instance_compartment(
                instance_id=request.pop(util.camelize('instanceId')),
                change_instance_compartment_details=request.pop(util.camelize('ChangeInstanceCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ChangeInstanceCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_instance_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="computeImaging" email="imaging_dev_us_grp@oracle.com" jiraProject="COM" opsJiraProject="COM"
def test_create_app_catalog_subscription(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CreateAppCatalogSubscription'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'CreateAppCatalogSubscription')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CreateAppCatalogSubscription')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.create_app_catalog_subscription(
                create_app_catalog_subscription_details=request.pop(util.camelize('CreateAppCatalogSubscriptionDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CreateAppCatalogSubscription',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'appCatalogSubscription',
            False,
            False
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_create_compute_capacity_reservation(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CreateComputeCapacityReservation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'CreateComputeCapacityReservation')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CreateComputeCapacityReservation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.create_compute_capacity_reservation(
                create_compute_capacity_reservation_details=request.pop(util.camelize('CreateComputeCapacityReservationDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CreateComputeCapacityReservation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'computeCapacityReservation',
            False,
            False
        )


# IssueRoutingInfo tag="computeImaging" email="imaging_dev_us_grp@oracle.com" jiraProject="COM" opsJiraProject="COM"
def test_create_compute_image_capability_schema(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CreateComputeImageCapabilitySchema'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'CreateComputeImageCapabilitySchema')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CreateComputeImageCapabilitySchema')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.create_compute_image_capability_schema(
                create_compute_image_capability_schema_details=request.pop(util.camelize('CreateComputeImageCapabilitySchemaDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CreateComputeImageCapabilitySchema',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'computeImageCapabilitySchema',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_block_storage_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BS"
def test_create_dedicated_vm_host(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CreateDedicatedVmHost'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'CreateDedicatedVmHost')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CreateDedicatedVmHost')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.create_dedicated_vm_host(
                create_dedicated_vm_host_details=request.pop(util.camelize('CreateDedicatedVmHostDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CreateDedicatedVmHost',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dedicatedVmHost',
            False,
            False
        )


# IssueRoutingInfo tag="computeImaging" email="imaging_dev_us_grp@oracle.com" jiraProject="COM" opsJiraProject="COM"
def test_create_image(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CreateImage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'CreateImage')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CreateImage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.create_image(
                create_image_details=request.pop(util.camelize('CreateImageDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CreateImage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'image',
            False,
            False
        )


# IssueRoutingInfo tag="computeServices" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="COM"
def test_create_instance_console_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CreateInstanceConsoleConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'CreateInstanceConsoleConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CreateInstanceConsoleConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.create_instance_console_connection(
                create_instance_console_connection_details=request.pop(util.camelize('CreateInstanceConsoleConnectionDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CreateInstanceConsoleConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'instanceConsoleConnection',
            False,
            False
        )


# IssueRoutingInfo tag="computeImaging" email="imaging_dev_us_grp@oracle.com" jiraProject="COM" opsJiraProject="COM"
def test_delete_app_catalog_subscription(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeleteAppCatalogSubscription'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'DeleteAppCatalogSubscription')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeleteAppCatalogSubscription')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.delete_app_catalog_subscription(
                listing_id=request.pop(util.camelize('listingId')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                resource_version=request.pop(util.camelize('resourceVersion')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeleteAppCatalogSubscription',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_app_catalog_subscription',
            True,
            False
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_delete_compute_capacity_reservation(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeleteComputeCapacityReservation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'DeleteComputeCapacityReservation')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeleteComputeCapacityReservation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.delete_compute_capacity_reservation(
                capacity_reservation_id=request.pop(util.camelize('capacityReservationId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeleteComputeCapacityReservation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_compute_capacity_reservation',
            True,
            False
        )


# IssueRoutingInfo tag="computeImaging" email="imaging_dev_us_grp@oracle.com" jiraProject="COM" opsJiraProject="COM"
def test_delete_compute_image_capability_schema(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeleteComputeImageCapabilitySchema'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'DeleteComputeImageCapabilitySchema')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeleteComputeImageCapabilitySchema')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.delete_compute_image_capability_schema(
                compute_image_capability_schema_id=request.pop(util.camelize('computeImageCapabilitySchemaId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeleteComputeImageCapabilitySchema',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_compute_image_capability_schema',
            True,
            False
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_delete_console_history(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeleteConsoleHistory'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'DeleteConsoleHistory')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeleteConsoleHistory')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.delete_console_history(
                instance_console_history_id=request.pop(util.camelize('instanceConsoleHistoryId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeleteConsoleHistory',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_console_history',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="sic_block_storage_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BS"
def test_delete_dedicated_vm_host(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeleteDedicatedVmHost'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'DeleteDedicatedVmHost')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeleteDedicatedVmHost')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.delete_dedicated_vm_host(
                dedicated_vm_host_id=request.pop(util.camelize('dedicatedVmHostId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeleteDedicatedVmHost',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_dedicated_vm_host',
            True,
            False
        )


# IssueRoutingInfo tag="computeImaging" email="imaging_dev_us_grp@oracle.com" jiraProject="COM" opsJiraProject="COM"
def test_delete_image(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeleteImage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'DeleteImage')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeleteImage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.delete_image(
                image_id=request.pop(util.camelize('imageId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeleteImage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_image',
            True,
            False
        )


# IssueRoutingInfo tag="computeServices" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="COM"
def test_delete_instance_console_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeleteInstanceConsoleConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'DeleteInstanceConsoleConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeleteInstanceConsoleConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.delete_instance_console_connection(
                instance_console_connection_id=request.pop(util.camelize('instanceConsoleConnectionId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeleteInstanceConsoleConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_instance_console_connection',
            True,
            False
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_detach_boot_volume(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DetachBootVolume'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'DetachBootVolume')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DetachBootVolume')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.detach_boot_volume(
                boot_volume_attachment_id=request.pop(util.camelize('bootVolumeAttachmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DetachBootVolume',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'detach_boot_volume',
            True,
            False
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_detach_vnic(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DetachVnic'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'DetachVnic')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DetachVnic')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.detach_vnic(
                vnic_attachment_id=request.pop(util.camelize('vnicAttachmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DetachVnic',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'detach_vnic',
            True,
            False
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_detach_volume(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DetachVolume'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'DetachVolume')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DetachVolume')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.detach_volume(
                volume_attachment_id=request.pop(util.camelize('volumeAttachmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DetachVolume',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'detach_volume',
            True,
            False
        )


# IssueRoutingInfo tag="computeImaging" email="imaging_dev_us_grp@oracle.com" jiraProject="COM" opsJiraProject="COM"
def test_export_image(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ExportImage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'ExportImage')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ExportImage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.export_image(
                image_id=request.pop(util.camelize('imageId')),
                export_image_details=request.pop(util.camelize('ExportImageDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ExportImage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'image',
            False,
            False
        )


# IssueRoutingInfo tag="computeImaging" email="imaging_dev_us_grp@oracle.com" jiraProject="COM" opsJiraProject="COM"
def test_get_app_catalog_listing(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetAppCatalogListing'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'GetAppCatalogListing')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetAppCatalogListing')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.get_app_catalog_listing(
                listing_id=request.pop(util.camelize('listingId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetAppCatalogListing',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'appCatalogListing',
            False,
            False
        )


# IssueRoutingInfo tag="computeImaging" email="imaging_dev_us_grp@oracle.com" jiraProject="COM" opsJiraProject="COM"
def test_get_app_catalog_listing_agreements(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetAppCatalogListingAgreements'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'GetAppCatalogListingAgreements')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetAppCatalogListingAgreements')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.get_app_catalog_listing_agreements(
                listing_id=request.pop(util.camelize('listingId')),
                resource_version=request.pop(util.camelize('resourceVersion')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetAppCatalogListingAgreements',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'appCatalogListingResourceVersionAgreements',
            False,
            False
        )


# IssueRoutingInfo tag="computeImaging" email="imaging_dev_us_grp@oracle.com" jiraProject="COM" opsJiraProject="COM"
def test_get_app_catalog_listing_resource_version(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetAppCatalogListingResourceVersion'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'GetAppCatalogListingResourceVersion')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetAppCatalogListingResourceVersion')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.get_app_catalog_listing_resource_version(
                listing_id=request.pop(util.camelize('listingId')),
                resource_version=request.pop(util.camelize('resourceVersion')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetAppCatalogListingResourceVersion',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'appCatalogListingResourceVersion',
            False,
            False
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_get_boot_volume_attachment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetBootVolumeAttachment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'GetBootVolumeAttachment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetBootVolumeAttachment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.get_boot_volume_attachment(
                boot_volume_attachment_id=request.pop(util.camelize('bootVolumeAttachmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetBootVolumeAttachment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bootVolumeAttachment',
            False,
            False
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_get_compute_capacity_reservation(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetComputeCapacityReservation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'GetComputeCapacityReservation')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetComputeCapacityReservation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.get_compute_capacity_reservation(
                capacity_reservation_id=request.pop(util.camelize('capacityReservationId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetComputeCapacityReservation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'computeCapacityReservation',
            False,
            False
        )


# IssueRoutingInfo tag="computeImaging" email="imaging_dev_us_grp@oracle.com" jiraProject="COM" opsJiraProject="COM"
def test_get_compute_global_image_capability_schema(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetComputeGlobalImageCapabilitySchema'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'GetComputeGlobalImageCapabilitySchema')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetComputeGlobalImageCapabilitySchema')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.get_compute_global_image_capability_schema(
                compute_global_image_capability_schema_id=request.pop(util.camelize('computeGlobalImageCapabilitySchemaId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetComputeGlobalImageCapabilitySchema',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'computeGlobalImageCapabilitySchema',
            False,
            False
        )


# IssueRoutingInfo tag="computeImaging" email="imaging_dev_us_grp@oracle.com" jiraProject="COM" opsJiraProject="COM"
def test_get_compute_global_image_capability_schema_version(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetComputeGlobalImageCapabilitySchemaVersion'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'GetComputeGlobalImageCapabilitySchemaVersion')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetComputeGlobalImageCapabilitySchemaVersion')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.get_compute_global_image_capability_schema_version(
                compute_global_image_capability_schema_id=request.pop(util.camelize('computeGlobalImageCapabilitySchemaId')),
                compute_global_image_capability_schema_version_name=request.pop(util.camelize('computeGlobalImageCapabilitySchemaVersionName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetComputeGlobalImageCapabilitySchemaVersion',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'computeGlobalImageCapabilitySchemaVersion',
            False,
            False
        )


# IssueRoutingInfo tag="computeImaging" email="imaging_dev_us_grp@oracle.com" jiraProject="COM" opsJiraProject="COM"
def test_get_compute_image_capability_schema(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetComputeImageCapabilitySchema'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'GetComputeImageCapabilitySchema')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetComputeImageCapabilitySchema')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.get_compute_image_capability_schema(
                compute_image_capability_schema_id=request.pop(util.camelize('computeImageCapabilitySchemaId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetComputeImageCapabilitySchema',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'computeImageCapabilitySchema',
            False,
            False
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_get_console_history(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetConsoleHistory'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'GetConsoleHistory')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetConsoleHistory')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.get_console_history(
                instance_console_history_id=request.pop(util.camelize('instanceConsoleHistoryId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetConsoleHistory',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'consoleHistory',
            False,
            False
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_get_console_history_content(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetConsoleHistoryContent'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'GetConsoleHistoryContent')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetConsoleHistoryContent')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.get_console_history_content(
                instance_console_history_id=request.pop(util.camelize('instanceConsoleHistoryId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetConsoleHistoryContent',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'str',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_block_storage_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BS"
def test_get_dedicated_vm_host(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetDedicatedVmHost'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'GetDedicatedVmHost')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetDedicatedVmHost')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.get_dedicated_vm_host(
                dedicated_vm_host_id=request.pop(util.camelize('dedicatedVmHostId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetDedicatedVmHost',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dedicatedVmHost',
            False,
            False
        )


# IssueRoutingInfo tag="computeImaging" email="imaging_dev_us_grp@oracle.com" jiraProject="COM" opsJiraProject="COM"
def test_get_image(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetImage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'GetImage')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetImage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.get_image(
                image_id=request.pop(util.camelize('imageId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetImage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'image',
            False,
            False
        )


# IssueRoutingInfo tag="computeImaging" email="imaging_dev_us_grp@oracle.com" jiraProject="COM" opsJiraProject="COM"
def test_get_image_shape_compatibility_entry(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetImageShapeCompatibilityEntry'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'GetImageShapeCompatibilityEntry')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetImageShapeCompatibilityEntry')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.get_image_shape_compatibility_entry(
                image_id=request.pop(util.camelize('imageId')),
                shape_name=request.pop(util.camelize('shapeName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetImageShapeCompatibilityEntry',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'imageShapeCompatibilityEntry',
            False,
            False
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_get_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'GetInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.get_instance(
                instance_id=request.pop(util.camelize('instanceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'instance',
            False,
            False
        )


# IssueRoutingInfo tag="computeServices" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="COM"
def test_get_instance_console_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetInstanceConsoleConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'GetInstanceConsoleConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetInstanceConsoleConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.get_instance_console_connection(
                instance_console_connection_id=request.pop(util.camelize('instanceConsoleConnectionId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetInstanceConsoleConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'instanceConsoleConnection',
            False,
            False
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_get_measured_boot_report(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetMeasuredBootReport'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'GetMeasuredBootReport')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetMeasuredBootReport')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.get_measured_boot_report(
                instance_id=request.pop(util.camelize('instanceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetMeasuredBootReport',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'measuredBootReport',
            False,
            False
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_get_vnic_attachment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetVnicAttachment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'GetVnicAttachment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetVnicAttachment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.get_vnic_attachment(
                vnic_attachment_id=request.pop(util.camelize('vnicAttachmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetVnicAttachment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'vnicAttachment',
            False,
            False
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_get_volume_attachment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetVolumeAttachment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'GetVolumeAttachment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetVolumeAttachment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.get_volume_attachment(
                volume_attachment_id=request.pop(util.camelize('volumeAttachmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetVolumeAttachment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'volumeAttachment',
            False,
            False
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_get_windows_instance_initial_credentials(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetWindowsInstanceInitialCredentials'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'GetWindowsInstanceInitialCredentials')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetWindowsInstanceInitialCredentials')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.get_windows_instance_initial_credentials(
                instance_id=request.pop(util.camelize('instanceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetWindowsInstanceInitialCredentials',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'instanceCredentials',
            False,
            False
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_instance_action(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'InstanceAction'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'InstanceAction')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='InstanceAction')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.instance_action(
                instance_id=request.pop(util.camelize('instanceId')),
                action=request.pop(util.camelize('action')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'InstanceAction',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'instance',
            False,
            False
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_launch_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'LaunchInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'LaunchInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='LaunchInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.launch_instance(
                launch_instance_details=request.pop(util.camelize('LaunchInstanceDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'LaunchInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'instance',
            False,
            False
        )


# IssueRoutingInfo tag="computeImaging" email="imaging_dev_us_grp@oracle.com" jiraProject="COM" opsJiraProject="COM"
def test_list_app_catalog_listing_resource_versions(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListAppCatalogListingResourceVersions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'ListAppCatalogListingResourceVersions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListAppCatalogListingResourceVersions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.list_app_catalog_listing_resource_versions(
                listing_id=request.pop(util.camelize('listingId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_app_catalog_listing_resource_versions(
                    listing_id=request.pop(util.camelize('listingId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_app_catalog_listing_resource_versions(
                        listing_id=request.pop(util.camelize('listingId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListAppCatalogListingResourceVersions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'appCatalogListingResourceVersionSummary',
            False,
            True
        )


# IssueRoutingInfo tag="computeImaging" email="imaging_dev_us_grp@oracle.com" jiraProject="COM" opsJiraProject="COM"
def test_list_app_catalog_listings(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListAppCatalogListings'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'ListAppCatalogListings')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListAppCatalogListings')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.list_app_catalog_listings(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_app_catalog_listings(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_app_catalog_listings(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListAppCatalogListings',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'appCatalogListingSummary',
            False,
            True
        )


# IssueRoutingInfo tag="computeImaging" email="imaging_dev_us_grp@oracle.com" jiraProject="COM" opsJiraProject="COM"
def test_list_app_catalog_subscriptions(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListAppCatalogSubscriptions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'ListAppCatalogSubscriptions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListAppCatalogSubscriptions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.list_app_catalog_subscriptions(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_app_catalog_subscriptions(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_app_catalog_subscriptions(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListAppCatalogSubscriptions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'appCatalogSubscriptionSummary',
            False,
            True
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_list_boot_volume_attachments(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListBootVolumeAttachments'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'ListBootVolumeAttachments')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListBootVolumeAttachments')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.list_boot_volume_attachments(
                availability_domain=request.pop(util.camelize('availabilityDomain')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_boot_volume_attachments(
                    availability_domain=request.pop(util.camelize('availabilityDomain')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_boot_volume_attachments(
                        availability_domain=request.pop(util.camelize('availabilityDomain')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListBootVolumeAttachments',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bootVolumeAttachment',
            False,
            True
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_list_compute_capacity_reservation_instance_shapes(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListComputeCapacityReservationInstanceShapes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'ListComputeCapacityReservationInstanceShapes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListComputeCapacityReservationInstanceShapes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.list_compute_capacity_reservation_instance_shapes(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_compute_capacity_reservation_instance_shapes(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_compute_capacity_reservation_instance_shapes(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListComputeCapacityReservationInstanceShapes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'computeCapacityReservationInstanceShapeSummary',
            False,
            True
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_list_compute_capacity_reservation_instances(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListComputeCapacityReservationInstances'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'ListComputeCapacityReservationInstances')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListComputeCapacityReservationInstances')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.list_compute_capacity_reservation_instances(
                capacity_reservation_id=request.pop(util.camelize('capacityReservationId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_compute_capacity_reservation_instances(
                    capacity_reservation_id=request.pop(util.camelize('capacityReservationId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_compute_capacity_reservation_instances(
                        capacity_reservation_id=request.pop(util.camelize('capacityReservationId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListComputeCapacityReservationInstances',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'capacityReservationInstanceSummary',
            False,
            True
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_list_compute_capacity_reservations(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListComputeCapacityReservations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'ListComputeCapacityReservations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListComputeCapacityReservations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.list_compute_capacity_reservations(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_compute_capacity_reservations(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_compute_capacity_reservations(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListComputeCapacityReservations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'computeCapacityReservationSummary',
            False,
            True
        )


# IssueRoutingInfo tag="computeImaging" email="imaging_dev_us_grp@oracle.com" jiraProject="COM" opsJiraProject="COM"
def test_list_compute_global_image_capability_schema_versions(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListComputeGlobalImageCapabilitySchemaVersions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'ListComputeGlobalImageCapabilitySchemaVersions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListComputeGlobalImageCapabilitySchemaVersions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.list_compute_global_image_capability_schema_versions(
                compute_global_image_capability_schema_id=request.pop(util.camelize('computeGlobalImageCapabilitySchemaId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_compute_global_image_capability_schema_versions(
                    compute_global_image_capability_schema_id=request.pop(util.camelize('computeGlobalImageCapabilitySchemaId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_compute_global_image_capability_schema_versions(
                        compute_global_image_capability_schema_id=request.pop(util.camelize('computeGlobalImageCapabilitySchemaId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListComputeGlobalImageCapabilitySchemaVersions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'computeGlobalImageCapabilitySchemaVersionSummary',
            False,
            True
        )


# IssueRoutingInfo tag="computeImaging" email="imaging_dev_us_grp@oracle.com" jiraProject="COM" opsJiraProject="COM"
def test_list_compute_global_image_capability_schemas(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListComputeGlobalImageCapabilitySchemas'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'ListComputeGlobalImageCapabilitySchemas')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListComputeGlobalImageCapabilitySchemas')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.list_compute_global_image_capability_schemas(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_compute_global_image_capability_schemas(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_compute_global_image_capability_schemas(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListComputeGlobalImageCapabilitySchemas',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'computeGlobalImageCapabilitySchemaSummary',
            False,
            True
        )


# IssueRoutingInfo tag="computeImaging" email="imaging_dev_us_grp@oracle.com" jiraProject="COM" opsJiraProject="COM"
def test_list_compute_image_capability_schemas(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListComputeImageCapabilitySchemas'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'ListComputeImageCapabilitySchemas')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListComputeImageCapabilitySchemas')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.list_compute_image_capability_schemas(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_compute_image_capability_schemas(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_compute_image_capability_schemas(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListComputeImageCapabilitySchemas',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'computeImageCapabilitySchemaSummary',
            False,
            True
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_list_console_histories(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListConsoleHistories'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'ListConsoleHistories')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListConsoleHistories')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.list_console_histories(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_console_histories(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_console_histories(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListConsoleHistories',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'consoleHistory',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sic_block_storage_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BS"
def test_list_dedicated_vm_host_instance_shapes(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListDedicatedVmHostInstanceShapes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'ListDedicatedVmHostInstanceShapes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListDedicatedVmHostInstanceShapes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.list_dedicated_vm_host_instance_shapes(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_dedicated_vm_host_instance_shapes(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_dedicated_vm_host_instance_shapes(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListDedicatedVmHostInstanceShapes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dedicatedVmHostInstanceShapeSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sic_block_storage_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BS"
def test_list_dedicated_vm_host_instances(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListDedicatedVmHostInstances'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'ListDedicatedVmHostInstances')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListDedicatedVmHostInstances')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.list_dedicated_vm_host_instances(
                compartment_id=request.pop(util.camelize('compartmentId')),
                dedicated_vm_host_id=request.pop(util.camelize('dedicatedVmHostId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_dedicated_vm_host_instances(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    dedicated_vm_host_id=request.pop(util.camelize('dedicatedVmHostId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_dedicated_vm_host_instances(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        dedicated_vm_host_id=request.pop(util.camelize('dedicatedVmHostId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListDedicatedVmHostInstances',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dedicatedVmHostInstanceSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sic_block_storage_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BS"
def test_list_dedicated_vm_host_shapes(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListDedicatedVmHostShapes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'ListDedicatedVmHostShapes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListDedicatedVmHostShapes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.list_dedicated_vm_host_shapes(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_dedicated_vm_host_shapes(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_dedicated_vm_host_shapes(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListDedicatedVmHostShapes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dedicatedVmHostShapeSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sic_block_storage_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BS"
def test_list_dedicated_vm_hosts(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListDedicatedVmHosts'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'ListDedicatedVmHosts')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListDedicatedVmHosts')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.list_dedicated_vm_hosts(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_dedicated_vm_hosts(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_dedicated_vm_hosts(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListDedicatedVmHosts',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dedicatedVmHostSummary',
            False,
            True
        )


# IssueRoutingInfo tag="computeImaging" email="imaging_dev_us_grp@oracle.com" jiraProject="COM" opsJiraProject="COM"
def test_list_image_shape_compatibility_entries(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListImageShapeCompatibilityEntries'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'ListImageShapeCompatibilityEntries')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListImageShapeCompatibilityEntries')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.list_image_shape_compatibility_entries(
                image_id=request.pop(util.camelize('imageId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_image_shape_compatibility_entries(
                    image_id=request.pop(util.camelize('imageId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_image_shape_compatibility_entries(
                        image_id=request.pop(util.camelize('imageId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListImageShapeCompatibilityEntries',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'imageShapeCompatibilitySummary',
            False,
            True
        )


# IssueRoutingInfo tag="computeImaging" email="imaging_dev_us_grp@oracle.com" jiraProject="COM" opsJiraProject="COM"
def test_list_images(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListImages'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'ListImages')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListImages')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.list_images(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_images(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_images(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListImages',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'image',
            False,
            True
        )


# IssueRoutingInfo tag="computeServices" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="COM"
def test_list_instance_console_connections(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListInstanceConsoleConnections'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'ListInstanceConsoleConnections')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListInstanceConsoleConnections')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.list_instance_console_connections(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_instance_console_connections(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_instance_console_connections(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListInstanceConsoleConnections',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'instanceConsoleConnection',
            False,
            True
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_list_instance_devices(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListInstanceDevices'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'ListInstanceDevices')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListInstanceDevices')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.list_instance_devices(
                instance_id=request.pop(util.camelize('instanceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_instance_devices(
                    instance_id=request.pop(util.camelize('instanceId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_instance_devices(
                        instance_id=request.pop(util.camelize('instanceId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListInstanceDevices',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'device',
            False,
            True
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_list_instances(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListInstances'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'ListInstances')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListInstances')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.list_instances(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_instances(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_instances(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListInstances',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'instance',
            False,
            True
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_list_shapes(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListShapes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'ListShapes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListShapes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.list_shapes(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_shapes(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_shapes(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListShapes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'shape',
            False,
            True
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_list_vnic_attachments(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListVnicAttachments'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'ListVnicAttachments')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListVnicAttachments')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.list_vnic_attachments(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_vnic_attachments(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_vnic_attachments(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListVnicAttachments',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'vnicAttachment',
            False,
            True
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_list_volume_attachments(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListVolumeAttachments'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'ListVolumeAttachments')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListVolumeAttachments')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.list_volume_attachments(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_volume_attachments(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_volume_attachments(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListVolumeAttachments',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'volumeAttachment',
            False,
            True
        )


# IssueRoutingInfo tag="computeImaging" email="imaging_dev_us_grp@oracle.com" jiraProject="COM" opsJiraProject="COM"
def test_remove_image_shape_compatibility_entry(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'RemoveImageShapeCompatibilityEntry'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'RemoveImageShapeCompatibilityEntry')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='RemoveImageShapeCompatibilityEntry')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.remove_image_shape_compatibility_entry(
                image_id=request.pop(util.camelize('imageId')),
                shape_name=request.pop(util.camelize('shapeName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'RemoveImageShapeCompatibilityEntry',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'remove_image_shape_compatibility_entry',
            True,
            False
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_terminate_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'TerminateInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'TerminateInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='TerminateInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.terminate_instance(
                instance_id=request.pop(util.camelize('instanceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'TerminateInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'terminate_instance',
            True,
            False
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_update_compute_capacity_reservation(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateComputeCapacityReservation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'UpdateComputeCapacityReservation')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateComputeCapacityReservation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.update_compute_capacity_reservation(
                capacity_reservation_id=request.pop(util.camelize('capacityReservationId')),
                update_compute_capacity_reservation_details=request.pop(util.camelize('UpdateComputeCapacityReservationDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateComputeCapacityReservation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_compute_capacity_reservation',
            False,
            False
        )


# IssueRoutingInfo tag="computeImaging" email="imaging_dev_us_grp@oracle.com" jiraProject="COM" opsJiraProject="COM"
def test_update_compute_image_capability_schema(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateComputeImageCapabilitySchema'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'UpdateComputeImageCapabilitySchema')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateComputeImageCapabilitySchema')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.update_compute_image_capability_schema(
                compute_image_capability_schema_id=request.pop(util.camelize('computeImageCapabilitySchemaId')),
                update_compute_image_capability_schema_details=request.pop(util.camelize('UpdateComputeImageCapabilitySchemaDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateComputeImageCapabilitySchema',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'computeImageCapabilitySchema',
            False,
            False
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_update_console_history(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateConsoleHistory'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'UpdateConsoleHistory')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateConsoleHistory')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.update_console_history(
                instance_console_history_id=request.pop(util.camelize('instanceConsoleHistoryId')),
                update_console_history_details=request.pop(util.camelize('UpdateConsoleHistoryDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateConsoleHistory',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'consoleHistory',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_block_storage_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BS"
def test_update_dedicated_vm_host(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateDedicatedVmHost'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'UpdateDedicatedVmHost')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateDedicatedVmHost')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.update_dedicated_vm_host(
                dedicated_vm_host_id=request.pop(util.camelize('dedicatedVmHostId')),
                update_dedicated_vm_host_details=request.pop(util.camelize('UpdateDedicatedVmHostDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateDedicatedVmHost',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dedicatedVmHost',
            False,
            False
        )


# IssueRoutingInfo tag="computeImaging" email="imaging_dev_us_grp@oracle.com" jiraProject="COM" opsJiraProject="COM"
def test_update_image(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateImage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'UpdateImage')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateImage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.update_image(
                image_id=request.pop(util.camelize('imageId')),
                update_image_details=request.pop(util.camelize('UpdateImageDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateImage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'image',
            False,
            False
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_update_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'UpdateInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.update_instance(
                instance_id=request.pop(util.camelize('instanceId')),
                update_instance_details=request.pop(util.camelize('UpdateInstanceDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'instance',
            False,
            False
        )


# IssueRoutingInfo tag="computeServices" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="COM"
def test_update_instance_console_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateInstanceConsoleConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'UpdateInstanceConsoleConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateInstanceConsoleConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.update_instance_console_connection(
                instance_console_connection_id=request.pop(util.camelize('instanceConsoleConnectionId')),
                update_instance_console_connection_details=request.pop(util.camelize('UpdateInstanceConsoleConnectionDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateInstanceConsoleConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'instanceConsoleConnection',
            False,
            False
        )


# IssueRoutingInfo tag="computeSharedOwnershipVmAndBm" email="compute_dev_us_grp@oracle.com" jiraProject="BMI" opsJiraProject="NONE"
def test_update_volume_attachment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateVolumeAttachment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('compute'), 'UpdateVolumeAttachment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateVolumeAttachment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.ComputeClient(config, service_endpoint=service_endpoint)
            response = client.update_volume_attachment(
                volume_attachment_id=request.pop(util.camelize('volumeAttachmentId')),
                update_volume_attachment_details=request.pop(util.camelize('UpdateVolumeAttachmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateVolumeAttachment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'volumeAttachment',
            False,
            False
        )
