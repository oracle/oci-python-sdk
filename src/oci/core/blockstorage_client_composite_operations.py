# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci  # noqa: F401
from oci.util import WAIT_RESOURCE_NOT_FOUND  # noqa: F401


class BlockstorageClientCompositeOperations(object):
    """
    This class provides a wrapper around :py:class:`~oci.core.BlockstorageClient` and offers convenience methods
    for operations that would otherwise need to be chained together. For example, instead of performing an action
    on a resource (e.g. launching an instance, creating a load balancer) and then using a waiter to wait for the resource
    to enter a given state, you can call a single method in this class to accomplish the same functionality
    """

    def __init__(self, client, work_request_client=None, **kwargs):
        """
        Creates a new BlockstorageClientCompositeOperations object

        :param BlockstorageClient client:
            The service client which will be wrapped by this object

        :param oci.work_requests.WorkRequestClient work_request_client: (optional)
            The work request service client which will be used to wait for work request states. Default is None.
        """
        self.client = client
        self._work_request_client = work_request_client if work_request_client else oci.work_requests.WorkRequestClient(self.client._config, **self.client._kwargs)

    def copy_boot_volume_backup_and_wait_for_work_request(self, boot_volume_backup_id, copy_boot_volume_backup_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.BlockstorageClient.copy_boot_volume_backup` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str boot_volume_backup_id: (required)
            The OCID of the boot volume backup.

        :param oci.core.models.CopyBootVolumeBackupDetails copy_boot_volume_backup_details: (required)
            Request to create a cross-region copy of given boot volume backup.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.BlockstorageClient.copy_boot_volume_backup`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.copy_boot_volume_backup(boot_volume_backup_id, copy_boot_volume_backup_details, **operation_kwargs)
        work_request_states = work_request_states if work_request_states else oci.waiter._WORK_REQUEST_TERMINATION_STATES
        lowered_work_request_states = [w.lower() for w in work_request_states]
        work_request_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self._work_request_client,
                self._work_request_client.get_work_request(work_request_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_work_request_states,
                **waiter_kwargs
            )
            return waiter_result
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def copy_boot_volume_backup_and_wait_for_state(self, boot_volume_backup_id, copy_boot_volume_backup_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.BlockstorageClient.copy_boot_volume_backup` and waits for the :py:class:`~oci.core.models.BootVolumeBackup` acted upon
        to enter the given state(s).

        :param str boot_volume_backup_id: (required)
            The OCID of the boot volume backup.

        :param oci.core.models.CopyBootVolumeBackupDetails copy_boot_volume_backup_details: (required)
            Request to create a cross-region copy of given boot volume backup.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.BootVolumeBackup.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.BlockstorageClient.copy_boot_volume_backup`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.copy_boot_volume_backup(boot_volume_backup_id, copy_boot_volume_backup_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_boot_volume_backup(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def copy_volume_backup_and_wait_for_work_request(self, volume_backup_id, copy_volume_backup_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.BlockstorageClient.copy_volume_backup` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str volume_backup_id: (required)
            The OCID of the volume backup.

        :param oci.core.models.CopyVolumeBackupDetails copy_volume_backup_details: (required)
            Request to create a cross-region copy of given backup.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.BlockstorageClient.copy_volume_backup`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.copy_volume_backup(volume_backup_id, copy_volume_backup_details, **operation_kwargs)
        work_request_states = work_request_states if work_request_states else oci.waiter._WORK_REQUEST_TERMINATION_STATES
        lowered_work_request_states = [w.lower() for w in work_request_states]
        work_request_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self._work_request_client,
                self._work_request_client.get_work_request(work_request_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_work_request_states,
                **waiter_kwargs
            )
            return waiter_result
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def copy_volume_backup_and_wait_for_state(self, volume_backup_id, copy_volume_backup_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.BlockstorageClient.copy_volume_backup` and waits for the :py:class:`~oci.core.models.VolumeBackup` acted upon
        to enter the given state(s).

        :param str volume_backup_id: (required)
            The OCID of the volume backup.

        :param oci.core.models.CopyVolumeBackupDetails copy_volume_backup_details: (required)
            Request to create a cross-region copy of given backup.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.VolumeBackup.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.BlockstorageClient.copy_volume_backup`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.copy_volume_backup(volume_backup_id, copy_volume_backup_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_volume_backup(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def copy_volume_group_backup_and_wait_for_state(self, volume_group_backup_id, copy_volume_group_backup_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.BlockstorageClient.copy_volume_group_backup` and waits for the :py:class:`~oci.core.models.VolumeGroupBackup` acted upon
        to enter the given state(s).

        :param str volume_group_backup_id: (required)
            The Oracle Cloud ID (OCID) that uniquely identifies the volume group backup.

        :param oci.core.models.CopyVolumeGroupBackupDetails copy_volume_group_backup_details: (required)
            Request to create a cross-region copy of given volume group backup.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.VolumeGroupBackup.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.BlockstorageClient.copy_volume_group_backup`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.copy_volume_group_backup(volume_group_backup_id, copy_volume_group_backup_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_volume_group_backup(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_boot_volume_and_wait_for_state(self, create_boot_volume_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.BlockstorageClient.create_boot_volume` and waits for the :py:class:`~oci.core.models.BootVolume` acted upon
        to enter the given state(s).

        :param oci.core.models.CreateBootVolumeDetails create_boot_volume_details: (required)
            Request to create a new boot volume.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.BootVolume.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.BlockstorageClient.create_boot_volume`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_boot_volume(create_boot_volume_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_boot_volume(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_boot_volume_backup_and_wait_for_state(self, create_boot_volume_backup_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.BlockstorageClient.create_boot_volume_backup` and waits for the :py:class:`~oci.core.models.BootVolumeBackup` acted upon
        to enter the given state(s).

        :param oci.core.models.CreateBootVolumeBackupDetails create_boot_volume_backup_details: (required)
            Request to create a new backup of given boot volume.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.BootVolumeBackup.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.BlockstorageClient.create_boot_volume_backup`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_boot_volume_backup(create_boot_volume_backup_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_boot_volume_backup(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_volume_and_wait_for_state(self, create_volume_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.BlockstorageClient.create_volume` and waits for the :py:class:`~oci.core.models.Volume` acted upon
        to enter the given state(s).

        :param oci.core.models.CreateVolumeDetails create_volume_details: (required)
            Request to create a new volume.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.Volume.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.BlockstorageClient.create_volume`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_volume(create_volume_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_volume(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_volume_backup_and_wait_for_state(self, create_volume_backup_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.BlockstorageClient.create_volume_backup` and waits for the :py:class:`~oci.core.models.VolumeBackup` acted upon
        to enter the given state(s).

        :param oci.core.models.CreateVolumeBackupDetails create_volume_backup_details: (required)
            Request to create a new backup of given volume.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.VolumeBackup.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.BlockstorageClient.create_volume_backup`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_volume_backup(create_volume_backup_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_volume_backup(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_volume_group_and_wait_for_state(self, create_volume_group_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.BlockstorageClient.create_volume_group` and waits for the :py:class:`~oci.core.models.VolumeGroup` acted upon
        to enter the given state(s).

        :param oci.core.models.CreateVolumeGroupDetails create_volume_group_details: (required)
            Request to create a new volume group.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.VolumeGroup.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.BlockstorageClient.create_volume_group`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_volume_group(create_volume_group_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_volume_group(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_volume_group_backup_and_wait_for_state(self, create_volume_group_backup_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.BlockstorageClient.create_volume_group_backup` and waits for the :py:class:`~oci.core.models.VolumeGroupBackup` acted upon
        to enter the given state(s).

        :param oci.core.models.CreateVolumeGroupBackupDetails create_volume_group_backup_details: (required)
            Request to create a new backup group of given volume group.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.VolumeGroupBackup.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.BlockstorageClient.create_volume_group_backup`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_volume_group_backup(create_volume_group_backup_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_volume_group_backup(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_boot_volume_and_wait_for_state(self, boot_volume_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.BlockstorageClient.delete_boot_volume` and waits for the :py:class:`~oci.core.models.BootVolume` acted upon
        to enter the given state(s).

        :param str boot_volume_id: (required)
            The OCID of the boot volume.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.BootVolume.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.BlockstorageClient.delete_boot_volume`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_boot_volume(boot_volume_id)
        operation_result = None
        try:
            operation_result = self.client.delete_boot_volume(boot_volume_id, **operation_kwargs)
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

    def delete_boot_volume_backup_and_wait_for_state(self, boot_volume_backup_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.BlockstorageClient.delete_boot_volume_backup` and waits for the :py:class:`~oci.core.models.BootVolumeBackup` acted upon
        to enter the given state(s).

        :param str boot_volume_backup_id: (required)
            The OCID of the boot volume backup.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.BootVolumeBackup.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.BlockstorageClient.delete_boot_volume_backup`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_boot_volume_backup(boot_volume_backup_id)
        operation_result = None
        try:
            operation_result = self.client.delete_boot_volume_backup(boot_volume_backup_id, **operation_kwargs)
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

    def delete_volume_and_wait_for_state(self, volume_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.BlockstorageClient.delete_volume` and waits for the :py:class:`~oci.core.models.Volume` acted upon
        to enter the given state(s).

        :param str volume_id: (required)
            The OCID of the volume.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.Volume.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.BlockstorageClient.delete_volume`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_volume(volume_id)
        operation_result = None
        try:
            operation_result = self.client.delete_volume(volume_id, **operation_kwargs)
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

    def delete_volume_backup_and_wait_for_state(self, volume_backup_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.BlockstorageClient.delete_volume_backup` and waits for the :py:class:`~oci.core.models.VolumeBackup` acted upon
        to enter the given state(s).

        :param str volume_backup_id: (required)
            The OCID of the volume backup.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.VolumeBackup.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.BlockstorageClient.delete_volume_backup`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_volume_backup(volume_backup_id)
        operation_result = None
        try:
            operation_result = self.client.delete_volume_backup(volume_backup_id, **operation_kwargs)
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

    def delete_volume_group_and_wait_for_state(self, volume_group_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.BlockstorageClient.delete_volume_group` and waits for the :py:class:`~oci.core.models.VolumeGroup` acted upon
        to enter the given state(s).

        :param str volume_group_id: (required)
            The Oracle Cloud ID (OCID) that uniquely identifies the volume group.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.VolumeGroup.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.BlockstorageClient.delete_volume_group`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_volume_group(volume_group_id)
        operation_result = None
        try:
            operation_result = self.client.delete_volume_group(volume_group_id, **operation_kwargs)
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

    def delete_volume_group_backup_and_wait_for_state(self, volume_group_backup_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.BlockstorageClient.delete_volume_group_backup` and waits for the :py:class:`~oci.core.models.VolumeGroupBackup` acted upon
        to enter the given state(s).

        :param str volume_group_backup_id: (required)
            The Oracle Cloud ID (OCID) that uniquely identifies the volume group backup.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.VolumeGroupBackup.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.BlockstorageClient.delete_volume_group_backup`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_volume_group_backup(volume_group_backup_id)
        operation_result = None
        try:
            operation_result = self.client.delete_volume_group_backup(volume_group_backup_id, **operation_kwargs)
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

    def update_boot_volume_and_wait_for_state(self, boot_volume_id, update_boot_volume_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.BlockstorageClient.update_boot_volume` and waits for the :py:class:`~oci.core.models.BootVolume` acted upon
        to enter the given state(s).

        :param str boot_volume_id: (required)
            The OCID of the boot volume.

        :param oci.core.models.UpdateBootVolumeDetails update_boot_volume_details: (required)
            Update boot volume's display name.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.BootVolume.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.BlockstorageClient.update_boot_volume`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_boot_volume(boot_volume_id, update_boot_volume_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_boot_volume(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_boot_volume_backup_and_wait_for_state(self, boot_volume_backup_id, update_boot_volume_backup_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.BlockstorageClient.update_boot_volume_backup` and waits for the :py:class:`~oci.core.models.BootVolumeBackup` acted upon
        to enter the given state(s).

        :param str boot_volume_backup_id: (required)
            The OCID of the boot volume backup.

        :param oci.core.models.UpdateBootVolumeBackupDetails update_boot_volume_backup_details: (required)
            Update boot volume backup fields

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.BootVolumeBackup.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.BlockstorageClient.update_boot_volume_backup`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_boot_volume_backup(boot_volume_backup_id, update_boot_volume_backup_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_boot_volume_backup(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_volume_and_wait_for_state(self, volume_id, update_volume_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.BlockstorageClient.update_volume` and waits for the :py:class:`~oci.core.models.Volume` acted upon
        to enter the given state(s).

        :param str volume_id: (required)
            The OCID of the volume.

        :param oci.core.models.UpdateVolumeDetails update_volume_details: (required)
            Update volume's display name. Avoid entering confidential information.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.Volume.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.BlockstorageClient.update_volume`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_volume(volume_id, update_volume_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_volume(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_volume_backup_and_wait_for_state(self, volume_backup_id, update_volume_backup_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.BlockstorageClient.update_volume_backup` and waits for the :py:class:`~oci.core.models.VolumeBackup` acted upon
        to enter the given state(s).

        :param str volume_backup_id: (required)
            The OCID of the volume backup.

        :param oci.core.models.UpdateVolumeBackupDetails update_volume_backup_details: (required)
            Update volume backup fields

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.VolumeBackup.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.BlockstorageClient.update_volume_backup`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_volume_backup(volume_backup_id, update_volume_backup_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_volume_backup(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_volume_group_and_wait_for_state(self, volume_group_id, update_volume_group_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.BlockstorageClient.update_volume_group` and waits for the :py:class:`~oci.core.models.VolumeGroup` acted upon
        to enter the given state(s).

        :param str volume_group_id: (required)
            The Oracle Cloud ID (OCID) that uniquely identifies the volume group.

        :param oci.core.models.UpdateVolumeGroupDetails update_volume_group_details: (required)
            Update volume group's set of volumes and/or display name

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.VolumeGroup.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.BlockstorageClient.update_volume_group`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_volume_group(volume_group_id, update_volume_group_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_volume_group(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_volume_group_backup_and_wait_for_state(self, volume_group_backup_id, update_volume_group_backup_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.BlockstorageClient.update_volume_group_backup` and waits for the :py:class:`~oci.core.models.VolumeGroupBackup` acted upon
        to enter the given state(s).

        :param str volume_group_backup_id: (required)
            The Oracle Cloud ID (OCID) that uniquely identifies the volume group backup.

        :param oci.core.models.UpdateVolumeGroupBackupDetails update_volume_group_backup_details: (required)
            Update volume group backup fields

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.VolumeGroupBackup.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.BlockstorageClient.update_volume_group_backup`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_volume_group_backup(volume_group_backup_id, update_volume_group_backup_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_volume_group_backup(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
