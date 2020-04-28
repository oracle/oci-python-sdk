# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci  # noqa: F401
from oci.util import WAIT_RESOURCE_NOT_FOUND  # noqa: F401


class OsManagementClientCompositeOperations(object):
    """
    This class provides a wrapper around :py:class:`~oci.os_management.OsManagementClient` and offers convenience methods
    for operations that would otherwise need to be chained together. For example, instead of performing an action
    on a resource (e.g. launching an instance, creating a load balancer) and then using a waiter to wait for the resource
    to enter a given state, you can call a single method in this class to accomplish the same functionality
    """

    def __init__(self, client, **kwargs):
        """
        Creates a new OsManagementClientCompositeOperations object

        :param OsManagementClient client:
            The service client which will be wrapped by this object
        """
        self.client = client

    def create_managed_instance_group_and_wait_for_state(self, create_managed_instance_group_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management.OsManagementClient.create_managed_instance_group` and waits for the :py:class:`~oci.os_management.models.ManagedInstanceGroup` acted upon
        to enter the given state(s).

        :param CreateManagedInstanceGroupDetails create_managed_instance_group_details: (required)
            Details about a Managed Instance Group to create

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management.models.ManagedInstanceGroup.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management.OsManagementClient.create_managed_instance_group`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_managed_instance_group(create_managed_instance_group_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_managed_instance_group(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_scheduled_job_and_wait_for_state(self, create_scheduled_job_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management.OsManagementClient.create_scheduled_job` and waits for the :py:class:`~oci.os_management.models.ScheduledJob` acted upon
        to enter the given state(s).

        :param CreateScheduledJobDetails create_scheduled_job_details: (required)
            Details about a Scheduled Job to create

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management.models.ScheduledJob.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management.OsManagementClient.create_scheduled_job`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_scheduled_job(create_scheduled_job_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_scheduled_job(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_software_source_and_wait_for_state(self, create_software_source_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management.OsManagementClient.create_software_source` and waits for the :py:class:`~oci.os_management.models.SoftwareSource` acted upon
        to enter the given state(s).

        :param CreateSoftwareSourceDetails create_software_source_details: (required)
            Details about a Sofware Source to create

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management.models.SoftwareSource.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management.OsManagementClient.create_software_source`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_software_source(create_software_source_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_software_source(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_managed_instance_group_and_wait_for_state(self, managed_instance_group_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management.OsManagementClient.delete_managed_instance_group` and waits for the :py:class:`~oci.os_management.models.ManagedInstanceGroup` acted upon
        to enter the given state(s).

        :param str managed_instance_group_id: (required)
            OCID for the managed instance group

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management.models.ManagedInstanceGroup.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management.OsManagementClient.delete_managed_instance_group`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_managed_instance_group(managed_instance_group_id)
        operation_result = None
        try:
            operation_result = self.client.delete_managed_instance_group(managed_instance_group_id, **operation_kwargs)
        except oci.exceptions.ServiceError as e:
            if e.status == 404:
                return WAIT_RESOURCE_NOT_FOUND
            else:
                raise e

        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]

        try:
            waiter_result = oci.wait_until(
                self.client,
                initial_get_result,
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                succeed_on_not_found=True,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_scheduled_job_and_wait_for_state(self, scheduled_job_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management.OsManagementClient.delete_scheduled_job` and waits for the :py:class:`~oci.os_management.models.ScheduledJob` acted upon
        to enter the given state(s).

        :param str scheduled_job_id: (required)
            The ID of the scheduled job.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management.models.ScheduledJob.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management.OsManagementClient.delete_scheduled_job`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_scheduled_job(scheduled_job_id)
        operation_result = None
        try:
            operation_result = self.client.delete_scheduled_job(scheduled_job_id, **operation_kwargs)
        except oci.exceptions.ServiceError as e:
            if e.status == 404:
                return WAIT_RESOURCE_NOT_FOUND
            else:
                raise e

        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]

        try:
            waiter_result = oci.wait_until(
                self.client,
                initial_get_result,
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                succeed_on_not_found=True,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_software_source_and_wait_for_state(self, software_source_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management.OsManagementClient.delete_software_source` and waits for the :py:class:`~oci.os_management.models.SoftwareSource` acted upon
        to enter the given state(s).

        :param str software_source_id: (required)
            The OCID of the software source.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management.models.SoftwareSource.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management.OsManagementClient.delete_software_source`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_software_source(software_source_id)
        operation_result = None
        try:
            operation_result = self.client.delete_software_source(software_source_id, **operation_kwargs)
        except oci.exceptions.ServiceError as e:
            if e.status == 404:
                return WAIT_RESOURCE_NOT_FOUND
            else:
                raise e

        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]

        try:
            waiter_result = oci.wait_until(
                self.client,
                initial_get_result,
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                succeed_on_not_found=True,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def install_all_package_updates_on_managed_instance_and_wait_for_state(self, managed_instance_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management.OsManagementClient.install_all_package_updates_on_managed_instance` and waits for the :py:class:`~oci.os_management.models.WorkRequest`
        to enter the given state(s).

        :param str managed_instance_id: (required)
            OCID for the managed instance

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management.OsManagementClient.install_all_package_updates_on_managed_instance`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.install_all_package_updates_on_managed_instance(managed_instance_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def install_all_windows_updates_on_managed_instance_and_wait_for_state(self, managed_instance_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management.OsManagementClient.install_all_windows_updates_on_managed_instance` and waits for the :py:class:`~oci.os_management.models.WorkRequest`
        to enter the given state(s).

        :param str managed_instance_id: (required)
            OCID for the managed instance

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management.OsManagementClient.install_all_windows_updates_on_managed_instance`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.install_all_windows_updates_on_managed_instance(managed_instance_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def install_package_on_managed_instance_and_wait_for_state(self, managed_instance_id, software_package_name, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management.OsManagementClient.install_package_on_managed_instance` and waits for the :py:class:`~oci.os_management.models.WorkRequest`
        to enter the given state(s).

        :param str managed_instance_id: (required)
            OCID for the managed instance

        :param str software_package_name: (required)
            Package name

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management.OsManagementClient.install_package_on_managed_instance`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.install_package_on_managed_instance(managed_instance_id, software_package_name, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def install_package_update_on_managed_instance_and_wait_for_state(self, managed_instance_id, software_package_name, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management.OsManagementClient.install_package_update_on_managed_instance` and waits for the :py:class:`~oci.os_management.models.WorkRequest`
        to enter the given state(s).

        :param str managed_instance_id: (required)
            OCID for the managed instance

        :param str software_package_name: (required)
            Package name

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management.OsManagementClient.install_package_update_on_managed_instance`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.install_package_update_on_managed_instance(managed_instance_id, software_package_name, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def install_windows_update_on_managed_instance_and_wait_for_state(self, managed_instance_id, windows_update_name, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management.OsManagementClient.install_windows_update_on_managed_instance` and waits for the :py:class:`~oci.os_management.models.WorkRequest`
        to enter the given state(s).

        :param str managed_instance_id: (required)
            OCID for the managed instance

        :param str windows_update_name: (required)
            Unique identifier for the Windows update. NOTE - This is not an OCID,
            but is a unique identifier assigned by Microsoft.
            Example: `6981d463-cd91-4a26-b7c4-ea4ded9183ed`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management.OsManagementClient.install_windows_update_on_managed_instance`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.install_windows_update_on_managed_instance(managed_instance_id, windows_update_name, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def remove_package_from_managed_instance_and_wait_for_state(self, managed_instance_id, software_package_name, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management.OsManagementClient.remove_package_from_managed_instance` and waits for the :py:class:`~oci.os_management.models.WorkRequest`
        to enter the given state(s).

        :param str managed_instance_id: (required)
            OCID for the managed instance

        :param str software_package_name: (required)
            Package name

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management.OsManagementClient.remove_package_from_managed_instance`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.remove_package_from_managed_instance(managed_instance_id, software_package_name, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_managed_instance_group_and_wait_for_state(self, managed_instance_group_id, update_managed_instance_group_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management.OsManagementClient.update_managed_instance_group` and waits for the :py:class:`~oci.os_management.models.ManagedInstanceGroup` acted upon
        to enter the given state(s).

        :param str managed_instance_group_id: (required)
            OCID for the managed instance group

        :param UpdateManagedInstanceGroupDetails update_managed_instance_group_details: (required)
            Details about a Managed Instance Group to update

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management.models.ManagedInstanceGroup.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management.OsManagementClient.update_managed_instance_group`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_managed_instance_group(managed_instance_group_id, update_managed_instance_group_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_managed_instance_group(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_scheduled_job_and_wait_for_state(self, scheduled_job_id, update_scheduled_job_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management.OsManagementClient.update_scheduled_job` and waits for the :py:class:`~oci.os_management.models.ScheduledJob` acted upon
        to enter the given state(s).

        :param str scheduled_job_id: (required)
            The ID of the scheduled job.

        :param UpdateScheduledJobDetails update_scheduled_job_details: (required)
            Details about a Scheduled Job to update

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management.models.ScheduledJob.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management.OsManagementClient.update_scheduled_job`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_scheduled_job(scheduled_job_id, update_scheduled_job_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_scheduled_job(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_software_source_and_wait_for_state(self, software_source_id, update_software_source_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management.OsManagementClient.update_software_source` and waits for the :py:class:`~oci.os_management.models.SoftwareSource` acted upon
        to enter the given state(s).

        :param str software_source_id: (required)
            The OCID of the software source.

        :param UpdateSoftwareSourceDetails update_software_source_details: (required)
            Details about a Sofware Source to update

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management.models.SoftwareSource.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management.OsManagementClient.update_software_source`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_software_source(software_source_id, update_software_source_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_software_source(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
