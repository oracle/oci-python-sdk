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

        cassette_location = os.path.join('generated', 'os_management_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_add_packages_to_software_source(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'AddPackagesToSoftwareSource'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'AddPackagesToSoftwareSource')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='AddPackagesToSoftwareSource')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.add_packages_to_software_source(
                software_source_id=request.pop(util.camelize('softwareSourceId')),
                add_packages_to_software_source_details=request.pop(util.camelize('AddPackagesToSoftwareSourceDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'AddPackagesToSoftwareSource',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'add_packages_to_software_source',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_attach_child_software_source_to_managed_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'AttachChildSoftwareSourceToManagedInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'AttachChildSoftwareSourceToManagedInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='AttachChildSoftwareSourceToManagedInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.attach_child_software_source_to_managed_instance(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                attach_child_software_source_to_managed_instance_details=request.pop(util.camelize('AttachChildSoftwareSourceToManagedInstanceDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'AttachChildSoftwareSourceToManagedInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'attach_child_software_source_to_managed_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_attach_managed_instance_to_managed_instance_group(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'AttachManagedInstanceToManagedInstanceGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'AttachManagedInstanceToManagedInstanceGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='AttachManagedInstanceToManagedInstanceGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.attach_managed_instance_to_managed_instance_group(
                managed_instance_group_id=request.pop(util.camelize('managedInstanceGroupId')),
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'AttachManagedInstanceToManagedInstanceGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'attach_managed_instance_to_managed_instance_group',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_attach_parent_software_source_to_managed_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'AttachParentSoftwareSourceToManagedInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'AttachParentSoftwareSourceToManagedInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='AttachParentSoftwareSourceToManagedInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.attach_parent_software_source_to_managed_instance(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                attach_parent_software_source_to_managed_instance_details=request.pop(util.camelize('AttachParentSoftwareSourceToManagedInstanceDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'AttachParentSoftwareSourceToManagedInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'attach_parent_software_source_to_managed_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_change_managed_instance_group_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'ChangeManagedInstanceGroupCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'ChangeManagedInstanceGroupCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='ChangeManagedInstanceGroupCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.change_managed_instance_group_compartment(
                managed_instance_group_id=request.pop(util.camelize('managedInstanceGroupId')),
                change_managed_instance_group_compartment_details=request.pop(util.camelize('ChangeManagedInstanceGroupCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'ChangeManagedInstanceGroupCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_managed_instance_group_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_change_scheduled_job_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'ChangeScheduledJobCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'ChangeScheduledJobCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='ChangeScheduledJobCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.change_scheduled_job_compartment(
                scheduled_job_id=request.pop(util.camelize('scheduledJobId')),
                change_scheduled_job_compartment_details=request.pop(util.camelize('ChangeScheduledJobCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'ChangeScheduledJobCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_scheduled_job_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_change_software_source_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'ChangeSoftwareSourceCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'ChangeSoftwareSourceCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='ChangeSoftwareSourceCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.change_software_source_compartment(
                software_source_id=request.pop(util.camelize('softwareSourceId')),
                change_software_source_compartment_details=request.pop(util.camelize('ChangeSoftwareSourceCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'ChangeSoftwareSourceCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_software_source_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_create_managed_instance_group(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'CreateManagedInstanceGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'CreateManagedInstanceGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='CreateManagedInstanceGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_managed_instance_group(
                create_managed_instance_group_details=request.pop(util.camelize('CreateManagedInstanceGroupDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'CreateManagedInstanceGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managedInstanceGroup',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_create_scheduled_job(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'CreateScheduledJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'CreateScheduledJob')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='CreateScheduledJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_scheduled_job(
                create_scheduled_job_details=request.pop(util.camelize('CreateScheduledJobDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'CreateScheduledJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'scheduledJob',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_create_software_source(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'CreateSoftwareSource'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'CreateSoftwareSource')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='CreateSoftwareSource')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_software_source(
                create_software_source_details=request.pop(util.camelize('CreateSoftwareSourceDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'CreateSoftwareSource',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'softwareSource',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_delete_managed_instance_group(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'DeleteManagedInstanceGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'DeleteManagedInstanceGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='DeleteManagedInstanceGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.delete_managed_instance_group(
                managed_instance_group_id=request.pop(util.camelize('managedInstanceGroupId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'DeleteManagedInstanceGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_managed_instance_group',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_delete_scheduled_job(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'DeleteScheduledJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'DeleteScheduledJob')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='DeleteScheduledJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.delete_scheduled_job(
                scheduled_job_id=request.pop(util.camelize('scheduledJobId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'DeleteScheduledJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_scheduled_job',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_delete_software_source(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'DeleteSoftwareSource'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'DeleteSoftwareSource')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='DeleteSoftwareSource')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.delete_software_source(
                software_source_id=request.pop(util.camelize('softwareSourceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'DeleteSoftwareSource',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_software_source',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_detach_child_software_source_from_managed_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'DetachChildSoftwareSourceFromManagedInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'DetachChildSoftwareSourceFromManagedInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='DetachChildSoftwareSourceFromManagedInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.detach_child_software_source_from_managed_instance(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                detach_child_software_source_from_managed_instance_details=request.pop(util.camelize('DetachChildSoftwareSourceFromManagedInstanceDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'DetachChildSoftwareSourceFromManagedInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'detach_child_software_source_from_managed_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_detach_managed_instance_from_managed_instance_group(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'DetachManagedInstanceFromManagedInstanceGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'DetachManagedInstanceFromManagedInstanceGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='DetachManagedInstanceFromManagedInstanceGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.detach_managed_instance_from_managed_instance_group(
                managed_instance_group_id=request.pop(util.camelize('managedInstanceGroupId')),
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'DetachManagedInstanceFromManagedInstanceGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'detach_managed_instance_from_managed_instance_group',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_detach_parent_software_source_from_managed_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'DetachParentSoftwareSourceFromManagedInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'DetachParentSoftwareSourceFromManagedInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='DetachParentSoftwareSourceFromManagedInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.detach_parent_software_source_from_managed_instance(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                detach_parent_software_source_from_managed_instance_details=request.pop(util.camelize('DetachParentSoftwareSourceFromManagedInstanceDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'DetachParentSoftwareSourceFromManagedInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'detach_parent_software_source_from_managed_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_get_erratum(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'GetErratum'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'GetErratum')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='GetErratum')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_erratum(
                erratum_id=request.pop(util.camelize('erratumId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'GetErratum',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'erratum',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_get_managed_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'GetManagedInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'GetManagedInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='GetManagedInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_managed_instance(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'GetManagedInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managedInstance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_get_managed_instance_group(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'GetManagedInstanceGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'GetManagedInstanceGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='GetManagedInstanceGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_managed_instance_group(
                managed_instance_group_id=request.pop(util.camelize('managedInstanceGroupId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'GetManagedInstanceGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managedInstanceGroup',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_get_scheduled_job(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'GetScheduledJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'GetScheduledJob')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='GetScheduledJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_scheduled_job(
                scheduled_job_id=request.pop(util.camelize('scheduledJobId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'GetScheduledJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'scheduledJob',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_get_software_package(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'GetSoftwarePackage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'GetSoftwarePackage')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='GetSoftwarePackage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_software_package(
                software_source_id=request.pop(util.camelize('softwareSourceId')),
                software_package_name=request.pop(util.camelize('softwarePackageName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'GetSoftwarePackage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'softwarePackage',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_get_software_source(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'GetSoftwareSource'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'GetSoftwareSource')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='GetSoftwareSource')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_software_source(
                software_source_id=request.pop(util.camelize('softwareSourceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'GetSoftwareSource',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'softwareSource',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_install_all_package_updates_on_managed_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'InstallAllPackageUpdatesOnManagedInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'InstallAllPackageUpdatesOnManagedInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='InstallAllPackageUpdatesOnManagedInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.install_all_package_updates_on_managed_instance(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'InstallAllPackageUpdatesOnManagedInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'install_all_package_updates_on_managed_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_install_package_on_managed_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'InstallPackageOnManagedInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'InstallPackageOnManagedInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='InstallPackageOnManagedInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.install_package_on_managed_instance(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                software_package_name=request.pop(util.camelize('softwarePackageName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'InstallPackageOnManagedInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'install_package_on_managed_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_install_package_update_on_managed_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'InstallPackageUpdateOnManagedInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'InstallPackageUpdateOnManagedInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='InstallPackageUpdateOnManagedInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.install_package_update_on_managed_instance(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                software_package_name=request.pop(util.camelize('softwarePackageName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'InstallPackageUpdateOnManagedInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'install_package_update_on_managed_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_list_available_packages_for_managed_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'ListAvailablePackagesForManagedInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'ListAvailablePackagesForManagedInstance')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='ListAvailablePackagesForManagedInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_available_packages_for_managed_instance(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_available_packages_for_managed_instance(
                    managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_available_packages_for_managed_instance(
                        managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'ListAvailablePackagesForManagedInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'installablePackageSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_list_available_software_sources_for_managed_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'ListAvailableSoftwareSourcesForManagedInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'ListAvailableSoftwareSourcesForManagedInstance')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='ListAvailableSoftwareSourcesForManagedInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_available_software_sources_for_managed_instance(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_available_software_sources_for_managed_instance(
                    managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_available_software_sources_for_managed_instance(
                        managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'ListAvailableSoftwareSourcesForManagedInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'availableSoftwareSourceSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_list_available_updates_for_managed_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'ListAvailableUpdatesForManagedInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'ListAvailableUpdatesForManagedInstance')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='ListAvailableUpdatesForManagedInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_available_updates_for_managed_instance(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_available_updates_for_managed_instance(
                    managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_available_updates_for_managed_instance(
                        managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'ListAvailableUpdatesForManagedInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'availableUpdateSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_list_managed_instance_groups(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'ListManagedInstanceGroups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'ListManagedInstanceGroups')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='ListManagedInstanceGroups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_managed_instance_groups(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_managed_instance_groups(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_managed_instance_groups(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'ListManagedInstanceGroups',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managedInstanceGroupSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_list_managed_instances(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'ListManagedInstances'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'ListManagedInstances')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='ListManagedInstances')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_managed_instances(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_managed_instances(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_managed_instances(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'ListManagedInstances',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managedInstanceSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_list_packages_installed_on_managed_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'ListPackagesInstalledOnManagedInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'ListPackagesInstalledOnManagedInstance')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='ListPackagesInstalledOnManagedInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_packages_installed_on_managed_instance(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_packages_installed_on_managed_instance(
                    managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_packages_installed_on_managed_instance(
                        managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'ListPackagesInstalledOnManagedInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'installedPackageSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_list_scheduled_jobs(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'ListScheduledJobs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'ListScheduledJobs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='ListScheduledJobs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_scheduled_jobs(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_scheduled_jobs(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_scheduled_jobs(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'ListScheduledJobs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'scheduledJobSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_list_software_source_packages(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'ListSoftwareSourcePackages'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'ListSoftwareSourcePackages')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='ListSoftwareSourcePackages')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_software_source_packages(
                software_source_id=request.pop(util.camelize('softwareSourceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_software_source_packages(
                    software_source_id=request.pop(util.camelize('softwareSourceId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_software_source_packages(
                        software_source_id=request.pop(util.camelize('softwareSourceId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'ListSoftwareSourcePackages',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'softwarePackageSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_list_software_sources(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'ListSoftwareSources'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'ListSoftwareSources')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='ListSoftwareSources')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_software_sources(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_software_sources(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_software_sources(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'ListSoftwareSources',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'softwareSourceSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_list_upcoming_scheduled_jobs(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'ListUpcomingScheduledJobs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'ListUpcomingScheduledJobs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='ListUpcomingScheduledJobs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_upcoming_scheduled_jobs(
                compartment_id=request.pop(util.camelize('compartmentId')),
                time_end=request.pop(util.camelize('timeEnd')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_upcoming_scheduled_jobs(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    time_end=request.pop(util.camelize('timeEnd')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_upcoming_scheduled_jobs(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        time_end=request.pop(util.camelize('timeEnd')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'ListUpcomingScheduledJobs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'scheduledJobSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_errors(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_errors(
                    work_request_id=request.pop(util.camelize('workRequestId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_request_errors(
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestError',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_logs(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_logs(
                    work_request_id=request.pop(util.camelize('workRequestId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_request_logs(
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntry',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_work_requests(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_requests(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_requests(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_remove_package_from_managed_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'RemovePackageFromManagedInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'RemovePackageFromManagedInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='RemovePackageFromManagedInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.remove_package_from_managed_instance(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                software_package_name=request.pop(util.camelize('softwarePackageName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'RemovePackageFromManagedInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'remove_package_from_managed_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_remove_packages_from_software_source(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'RemovePackagesFromSoftwareSource'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'RemovePackagesFromSoftwareSource')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='RemovePackagesFromSoftwareSource')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.remove_packages_from_software_source(
                software_source_id=request.pop(util.camelize('softwareSourceId')),
                remove_packages_from_software_source_details=request.pop(util.camelize('RemovePackagesFromSoftwareSourceDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'RemovePackagesFromSoftwareSource',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'remove_packages_from_software_source',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_run_scheduled_job_now(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'RunScheduledJobNow'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'RunScheduledJobNow')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='RunScheduledJobNow')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.run_scheduled_job_now(
                scheduled_job_id=request.pop(util.camelize('scheduledJobId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'RunScheduledJobNow',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'run_scheduled_job_now',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_search_software_packages(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'SearchSoftwarePackages'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'SearchSoftwarePackages')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='SearchSoftwarePackages')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.search_software_packages(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.search_software_packages(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.search_software_packages(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'SearchSoftwarePackages',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'softwarePackageSearchSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_skip_next_scheduled_job_execution(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'SkipNextScheduledJobExecution'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'SkipNextScheduledJobExecution')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='SkipNextScheduledJobExecution')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.skip_next_scheduled_job_execution(
                scheduled_job_id=request.pop(util.camelize('scheduledJobId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'SkipNextScheduledJobExecution',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'skip_next_scheduled_job_execution',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_update_managed_instance_group(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'UpdateManagedInstanceGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'UpdateManagedInstanceGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='UpdateManagedInstanceGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_managed_instance_group(
                managed_instance_group_id=request.pop(util.camelize('managedInstanceGroupId')),
                update_managed_instance_group_details=request.pop(util.camelize('UpdateManagedInstanceGroupDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'UpdateManagedInstanceGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managedInstanceGroup',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_update_scheduled_job(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'UpdateScheduledJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'UpdateScheduledJob')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='UpdateScheduledJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_scheduled_job(
                scheduled_job_id=request.pop(util.camelize('scheduledJobId')),
                update_scheduled_job_details=request.pop(util.camelize('UpdateScheduledJobDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'UpdateScheduledJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'scheduledJob',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_update_software_source(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'UpdateSoftwareSource'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('os_management'), 'UpdateSoftwareSource')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='UpdateSoftwareSource')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.OsManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_software_source(
                software_source_id=request.pop(util.camelize('softwareSourceId')),
                update_software_source_details=request.pop(util.camelize('UpdateSoftwareSourceDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'UpdateSoftwareSource',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'softwareSource',
            False,
            False
        )
