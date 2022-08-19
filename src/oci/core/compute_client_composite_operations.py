# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci  # noqa: F401
from oci.util import WAIT_RESOURCE_NOT_FOUND  # noqa: F401


class ComputeClientCompositeOperations(object):
    """
    This class provides a wrapper around :py:class:`~oci.core.ComputeClient` and offers convenience methods
    for operations that would otherwise need to be chained together. For example, instead of performing an action
    on a resource (e.g. launching an instance, creating a load balancer) and then using a waiter to wait for the resource
    to enter a given state, you can call a single method in this class to accomplish the same functionality
    """

    def __init__(self, client, work_request_client=None, **kwargs):
        """
        Creates a new ComputeClientCompositeOperations object

        :param ComputeClient client:
            The service client which will be wrapped by this object

        :param oci.work_requests.WorkRequestClient work_request_client: (optional)
            The work request service client which will be used to wait for work request states. Default is None.
        """
        self.client = client
        self._work_request_client = work_request_client if work_request_client else oci.work_requests.WorkRequestClient(self.client._config, **self.client._kwargs)

    def attach_boot_volume_and_wait_for_state(self, attach_boot_volume_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeClient.attach_boot_volume` and waits for the :py:class:`~oci.core.models.BootVolumeAttachment` acted upon
        to enter the given state(s).

        :param oci.core.models.AttachBootVolumeDetails attach_boot_volume_details: (required)
            Attach boot volume request

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.BootVolumeAttachment.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeClient.attach_boot_volume`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.attach_boot_volume(attach_boot_volume_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        boot_volume_attachment_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_boot_volume_attachment(boot_volume_attachment_id),  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def attach_vnic_and_wait_for_state(self, attach_vnic_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeClient.attach_vnic` and waits for the :py:class:`~oci.core.models.VnicAttachment` acted upon
        to enter the given state(s).

        :param oci.core.models.AttachVnicDetails attach_vnic_details: (required)
            Attach VNIC details.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.VnicAttachment.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeClient.attach_vnic`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.attach_vnic(attach_vnic_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        vnic_attachment_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_vnic_attachment(vnic_attachment_id),  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def attach_volume_and_wait_for_state(self, attach_volume_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeClient.attach_volume` and waits for the :py:class:`~oci.core.models.VolumeAttachment` acted upon
        to enter the given state(s).

        :param oci.core.models.AttachVolumeDetails attach_volume_details: (required)
            Attach volume request

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.VolumeAttachment.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeClient.attach_volume`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.attach_volume(attach_volume_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        volume_attachment_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_volume_attachment(volume_attachment_id),  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def capture_console_history_and_wait_for_state(self, capture_console_history_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeClient.capture_console_history` and waits for the :py:class:`~oci.core.models.ConsoleHistory` acted upon
        to enter the given state(s).

        :param oci.core.models.CaptureConsoleHistoryDetails capture_console_history_details: (required)
            Console history details

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.ConsoleHistory.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeClient.capture_console_history`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.capture_console_history(capture_console_history_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        instance_console_history_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_console_history(instance_console_history_id),  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def change_compute_capacity_reservation_compartment_and_wait_for_work_request(self, capacity_reservation_id, change_compute_capacity_reservation_compartment_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeClient.change_compute_capacity_reservation_compartment` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str capacity_reservation_id: (required)
            The OCID of the compute capacity reservation.

        :param oci.core.models.ChangeComputeCapacityReservationCompartmentDetails change_compute_capacity_reservation_compartment_details: (required)
            The configuration details for the move operation.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeClient.change_compute_capacity_reservation_compartment`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.change_compute_capacity_reservation_compartment(capacity_reservation_id, change_compute_capacity_reservation_compartment_details, **operation_kwargs)
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

    def change_dedicated_vm_host_compartment_and_wait_for_work_request(self, dedicated_vm_host_id, change_dedicated_vm_host_compartment_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeClient.change_dedicated_vm_host_compartment` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str dedicated_vm_host_id: (required)
            The OCID of the dedicated VM host.

        :param oci.core.models.ChangeDedicatedVmHostCompartmentDetails change_dedicated_vm_host_compartment_details: (required)
            The request to move the dedicated virtual machine host to a different compartment.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeClient.change_dedicated_vm_host_compartment`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.change_dedicated_vm_host_compartment(dedicated_vm_host_id, change_dedicated_vm_host_compartment_details, **operation_kwargs)
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

    def change_instance_compartment_and_wait_for_work_request(self, instance_id, change_instance_compartment_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeClient.change_instance_compartment` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str instance_id: (required)
            The `OCID`__ of the instance.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param oci.core.models.ChangeInstanceCompartmentDetails change_instance_compartment_details: (required)
            Request to change the compartment of a given instance.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeClient.change_instance_compartment`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.change_instance_compartment(instance_id, change_instance_compartment_details, **operation_kwargs)
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

    def create_compute_capacity_reservation_and_wait_for_work_request(self, create_compute_capacity_reservation_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeClient.create_compute_capacity_reservation` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param oci.core.models.CreateComputeCapacityReservationDetails create_compute_capacity_reservation_details: (required)
            Details for creating a new compute capacity reservation.

            **Caution:** Avoid using any confidential information when you use the API to supply string values.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeClient.create_compute_capacity_reservation`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_compute_capacity_reservation(create_compute_capacity_reservation_details, **operation_kwargs)
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

    def create_compute_capacity_reservation_and_wait_for_state(self, create_compute_capacity_reservation_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeClient.create_compute_capacity_reservation` and waits for the :py:class:`~oci.core.models.ComputeCapacityReservation` acted upon
        to enter the given state(s).

        :param oci.core.models.CreateComputeCapacityReservationDetails create_compute_capacity_reservation_details: (required)
            Details for creating a new compute capacity reservation.

            **Caution:** Avoid using any confidential information when you use the API to supply string values.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.ComputeCapacityReservation.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeClient.create_compute_capacity_reservation`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_compute_capacity_reservation(create_compute_capacity_reservation_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        capacity_reservation_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_compute_capacity_reservation(capacity_reservation_id),  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_dedicated_vm_host_and_wait_for_work_request(self, create_dedicated_vm_host_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeClient.create_dedicated_vm_host` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param oci.core.models.CreateDedicatedVmHostDetails create_dedicated_vm_host_details: (required)
            The details for creating a new dedicated virtual machine host.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeClient.create_dedicated_vm_host`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_dedicated_vm_host(create_dedicated_vm_host_details, **operation_kwargs)
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

    def create_dedicated_vm_host_and_wait_for_state(self, create_dedicated_vm_host_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeClient.create_dedicated_vm_host` and waits for the :py:class:`~oci.core.models.DedicatedVmHost` acted upon
        to enter the given state(s).

        :param oci.core.models.CreateDedicatedVmHostDetails create_dedicated_vm_host_details: (required)
            The details for creating a new dedicated virtual machine host.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.DedicatedVmHost.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeClient.create_dedicated_vm_host`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_dedicated_vm_host(create_dedicated_vm_host_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        dedicated_vm_host_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_dedicated_vm_host(dedicated_vm_host_id),  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_image_and_wait_for_work_request(self, create_image_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeClient.create_image` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param oci.core.models.CreateImageDetails create_image_details: (required)
            Image creation details

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeClient.create_image`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_image(create_image_details, **operation_kwargs)
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

    def create_image_and_wait_for_state(self, create_image_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeClient.create_image` and waits for the :py:class:`~oci.core.models.Image` acted upon
        to enter the given state(s).

        :param oci.core.models.CreateImageDetails create_image_details: (required)
            Image creation details

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.Image.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeClient.create_image`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_image(create_image_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        image_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_image(image_id),  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_instance_console_connection_and_wait_for_state(self, create_instance_console_connection_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeClient.create_instance_console_connection` and waits for the :py:class:`~oci.core.models.InstanceConsoleConnection` acted upon
        to enter the given state(s).

        :param oci.core.models.CreateInstanceConsoleConnectionDetails create_instance_console_connection_details: (required)
            Request object for creating an InstanceConsoleConnection

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.InstanceConsoleConnection.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeClient.create_instance_console_connection`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_instance_console_connection(create_instance_console_connection_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        instance_console_connection_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_instance_console_connection(instance_console_connection_id),  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_compute_capacity_reservation_and_wait_for_work_request(self, capacity_reservation_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeClient.delete_compute_capacity_reservation` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str capacity_reservation_id: (required)
            The OCID of the compute capacity reservation.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeClient.delete_compute_capacity_reservation`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.delete_compute_capacity_reservation(capacity_reservation_id, **operation_kwargs)
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

    def delete_console_history_and_wait_for_state(self, instance_console_history_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeClient.delete_console_history` and waits for the :py:class:`~oci.core.models.ConsoleHistory` acted upon
        to enter the given state(s).

        :param str instance_console_history_id: (required)
            The OCID of the console history.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.ConsoleHistory.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeClient.delete_console_history`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_console_history(instance_console_history_id)
        operation_result = None
        try:
            operation_result = self.client.delete_console_history(instance_console_history_id, **operation_kwargs)
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
                initial_get_result,  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                succeed_on_not_found=True,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_dedicated_vm_host_and_wait_for_work_request(self, dedicated_vm_host_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeClient.delete_dedicated_vm_host` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str dedicated_vm_host_id: (required)
            The OCID of the dedicated VM host.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeClient.delete_dedicated_vm_host`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.delete_dedicated_vm_host(dedicated_vm_host_id, **operation_kwargs)
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

    def delete_image_and_wait_for_state(self, image_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeClient.delete_image` and waits for the :py:class:`~oci.core.models.Image` acted upon
        to enter the given state(s).

        :param str image_id: (required)
            The `OCID`__ of the image.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.Image.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeClient.delete_image`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_image(image_id)
        operation_result = None
        try:
            operation_result = self.client.delete_image(image_id, **operation_kwargs)
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
                initial_get_result,  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                succeed_on_not_found=True,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_instance_console_connection_and_wait_for_state(self, instance_console_connection_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeClient.delete_instance_console_connection` and waits for the :py:class:`~oci.core.models.InstanceConsoleConnection` acted upon
        to enter the given state(s).

        :param str instance_console_connection_id: (required)
            The OCID of the instance console connection.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.InstanceConsoleConnection.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeClient.delete_instance_console_connection`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_instance_console_connection(instance_console_connection_id)
        operation_result = None
        try:
            operation_result = self.client.delete_instance_console_connection(instance_console_connection_id, **operation_kwargs)
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
                initial_get_result,  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                succeed_on_not_found=True,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def detach_boot_volume_and_wait_for_state(self, boot_volume_attachment_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeClient.detach_boot_volume` and waits for the :py:class:`~oci.core.models.BootVolumeAttachment` acted upon
        to enter the given state(s).

        :param str boot_volume_attachment_id: (required)
            The OCID of the boot volume attachment.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.BootVolumeAttachment.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeClient.detach_boot_volume`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_boot_volume_attachment(boot_volume_attachment_id)
        operation_result = None
        try:
            operation_result = self.client.detach_boot_volume(boot_volume_attachment_id, **operation_kwargs)
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
                initial_get_result,  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                succeed_on_not_found=True,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def detach_vnic_and_wait_for_state(self, vnic_attachment_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeClient.detach_vnic` and waits for the :py:class:`~oci.core.models.VnicAttachment` acted upon
        to enter the given state(s).

        :param str vnic_attachment_id: (required)
            The OCID of the VNIC attachment.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.VnicAttachment.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeClient.detach_vnic`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_vnic_attachment(vnic_attachment_id)
        operation_result = None
        try:
            operation_result = self.client.detach_vnic(vnic_attachment_id, **operation_kwargs)
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
                initial_get_result,  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                succeed_on_not_found=True,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def detach_volume_and_wait_for_state(self, volume_attachment_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeClient.detach_volume` and waits for the :py:class:`~oci.core.models.VolumeAttachment` acted upon
        to enter the given state(s).

        :param str volume_attachment_id: (required)
            The OCID of the volume attachment.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.VolumeAttachment.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeClient.detach_volume`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_volume_attachment(volume_attachment_id)
        operation_result = None
        try:
            operation_result = self.client.detach_volume(volume_attachment_id, **operation_kwargs)
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
                initial_get_result,  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                succeed_on_not_found=True,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def export_image_and_wait_for_work_request(self, image_id, export_image_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeClient.export_image` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str image_id: (required)
            The `OCID`__ of the image.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param oci.core.models.ExportImageDetails export_image_details: (required)
            Details for the image export.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeClient.export_image`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.export_image(image_id, export_image_details, **operation_kwargs)
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

    def export_image_and_wait_for_state(self, image_id, export_image_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeClient.export_image` and waits for the :py:class:`~oci.core.models.Image` acted upon
        to enter the given state(s).

        :param str image_id: (required)
            The `OCID`__ of the image.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param oci.core.models.ExportImageDetails export_image_details: (required)
            Details for the image export.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.Image.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeClient.export_image`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.export_image(image_id, export_image_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        image_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_image(image_id),  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def instance_action_and_wait_for_state(self, instance_id, action, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeClient.instance_action` and waits for the :py:class:`~oci.core.models.Instance` acted upon
        to enter the given state(s).

        :param str instance_id: (required)
            The `OCID`__ of the instance.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str action: (required)
            The action to perform on the instance.

            Allowed values are: "STOP", "START", "SOFTRESET", "RESET", "SOFTSTOP", "SENDDIAGNOSTICINTERRUPT", "DIAGNOSTICREBOOT", "REBOOTMIGRATE"

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.Instance.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeClient.instance_action`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.instance_action(instance_id, action, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        instance_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_instance(instance_id),  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def launch_instance_and_wait_for_work_request(self, launch_instance_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeClient.launch_instance` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param oci.core.models.LaunchInstanceDetails launch_instance_details: (required)
            Instance details

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeClient.launch_instance`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.launch_instance(launch_instance_details, **operation_kwargs)
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

    def launch_instance_and_wait_for_state(self, launch_instance_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeClient.launch_instance` and waits for the :py:class:`~oci.core.models.Instance` acted upon
        to enter the given state(s).

        :param oci.core.models.LaunchInstanceDetails launch_instance_details: (required)
            Instance details

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.Instance.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeClient.launch_instance`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.launch_instance(launch_instance_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        instance_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_instance(instance_id),  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def terminate_instance_and_wait_for_state(self, instance_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeClient.terminate_instance` and waits for the :py:class:`~oci.core.models.Instance` acted upon
        to enter the given state(s).

        :param str instance_id: (required)
            The `OCID`__ of the instance.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.Instance.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeClient.terminate_instance`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_instance(instance_id)
        operation_result = None
        try:
            operation_result = self.client.terminate_instance(instance_id, **operation_kwargs)
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
                initial_get_result,  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                succeed_on_not_found=True,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_compute_capacity_reservation_and_wait_for_work_request(self, capacity_reservation_id, update_compute_capacity_reservation_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeClient.update_compute_capacity_reservation` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str capacity_reservation_id: (required)
            The OCID of the compute capacity reservation.

        :param oci.core.models.UpdateComputeCapacityReservationDetails update_compute_capacity_reservation_details: (required)
            Update compute capacity reservation details.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeClient.update_compute_capacity_reservation`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_compute_capacity_reservation(capacity_reservation_id, update_compute_capacity_reservation_details, **operation_kwargs)
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

    def update_console_history_and_wait_for_state(self, instance_console_history_id, update_console_history_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeClient.update_console_history` and waits for the :py:class:`~oci.core.models.ConsoleHistory` acted upon
        to enter the given state(s).

        :param str instance_console_history_id: (required)
            The OCID of the console history.

        :param oci.core.models.UpdateConsoleHistoryDetails update_console_history_details: (required)
            Update instance fields

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.ConsoleHistory.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeClient.update_console_history`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_console_history(instance_console_history_id, update_console_history_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        instance_console_history_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_console_history(instance_console_history_id),  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_dedicated_vm_host_and_wait_for_state(self, dedicated_vm_host_id, update_dedicated_vm_host_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeClient.update_dedicated_vm_host` and waits for the :py:class:`~oci.core.models.DedicatedVmHost` acted upon
        to enter the given state(s).

        :param str dedicated_vm_host_id: (required)
            The OCID of the dedicated VM host.

        :param oci.core.models.UpdateDedicatedVmHostDetails update_dedicated_vm_host_details: (required)
            Update dedicated VM host details

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.DedicatedVmHost.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeClient.update_dedicated_vm_host`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_dedicated_vm_host(dedicated_vm_host_id, update_dedicated_vm_host_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        dedicated_vm_host_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_dedicated_vm_host(dedicated_vm_host_id),  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_image_and_wait_for_state(self, image_id, update_image_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeClient.update_image` and waits for the :py:class:`~oci.core.models.Image` acted upon
        to enter the given state(s).

        :param str image_id: (required)
            The `OCID`__ of the image.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param oci.core.models.UpdateImageDetails update_image_details: (required)
            Updates the image display name field. Avoid entering confidential information.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.Image.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeClient.update_image`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_image(image_id, update_image_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        image_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_image(image_id),  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_instance_and_wait_for_work_request(self, instance_id, update_instance_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeClient.update_instance` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str instance_id: (required)
            The `OCID`__ of the instance.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param oci.core.models.UpdateInstanceDetails update_instance_details: (required)
            Update instance fields

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeClient.update_instance`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_instance(instance_id, update_instance_details, **operation_kwargs)
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

    def update_instance_and_wait_for_state(self, instance_id, update_instance_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeClient.update_instance` and waits for the :py:class:`~oci.core.models.Instance` acted upon
        to enter the given state(s).

        :param str instance_id: (required)
            The `OCID`__ of the instance.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param oci.core.models.UpdateInstanceDetails update_instance_details: (required)
            Update instance fields

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.Instance.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeClient.update_instance`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_instance(instance_id, update_instance_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        instance_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_instance(instance_id),  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_instance_console_connection_and_wait_for_state(self, instance_console_connection_id, update_instance_console_connection_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeClient.update_instance_console_connection` and waits for the :py:class:`~oci.core.models.InstanceConsoleConnection` acted upon
        to enter the given state(s).

        :param str instance_console_connection_id: (required)
            The OCID of the instance console connection.

        :param oci.core.models.UpdateInstanceConsoleConnectionDetails update_instance_console_connection_details: (required)
            Update instanceConsoleConnection tags

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.InstanceConsoleConnection.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeClient.update_instance_console_connection`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_instance_console_connection(instance_console_connection_id, update_instance_console_connection_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        instance_console_connection_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_instance_console_connection(instance_console_connection_id),  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_volume_attachment_and_wait_for_state(self, volume_attachment_id, update_volume_attachment_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeClient.update_volume_attachment` and waits for the :py:class:`~oci.core.models.VolumeAttachment` acted upon
        to enter the given state(s).

        :param str volume_attachment_id: (required)
            The OCID of the volume attachment.

        :param oci.core.models.UpdateVolumeAttachmentDetails update_volume_attachment_details: (required)
            Update information about the specified volume attachment.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.VolumeAttachment.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeClient.update_volume_attachment`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_volume_attachment(volume_attachment_id, update_volume_attachment_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        volume_attachment_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_volume_attachment(volume_attachment_id),  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
