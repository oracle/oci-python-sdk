# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci  # noqa: F401
from oci.util import WAIT_RESOURCE_NOT_FOUND  # noqa: F401


class DisasterRecoveryClientCompositeOperations(object):
    """
    This class provides a wrapper around :py:class:`~oci.disaster_recovery.DisasterRecoveryClient` and offers convenience methods
    for operations that would otherwise need to be chained together. For example, instead of performing an action
    on a resource (e.g. launching an instance, creating a load balancer) and then using a waiter to wait for the resource
    to enter a given state, you can call a single method in this class to accomplish the same functionality
    """

    def __init__(self, client, **kwargs):
        """
        Creates a new DisasterRecoveryClientCompositeOperations object

        :param DisasterRecoveryClient client:
            The service client which will be wrapped by this object
        """
        self.client = client

    def associate_dr_protection_group_and_wait_for_state(self, associate_dr_protection_group_details, dr_protection_group_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.disaster_recovery.DisasterRecoveryClient.associate_dr_protection_group` and waits for the :py:class:`~oci.disaster_recovery.models.WorkRequest`
        to enter the given state(s).

        :param oci.disaster_recovery.models.AssociateDrProtectionGroupDetails associate_dr_protection_group_details: (required)
            Details for creating an association between two DR Protection Groups.

        :param str dr_protection_group_id: (required)
            The OCID of the DR Protection Group.

            Example: `ocid1.drprotectiongroup.oc1.phx.exampleocid`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.disaster_recovery.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.disaster_recovery.DisasterRecoveryClient.associate_dr_protection_group`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.associate_dr_protection_group(associate_dr_protection_group_details, dr_protection_group_id, **operation_kwargs)
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

    def cancel_dr_plan_execution_and_wait_for_state(self, cancel_dr_plan_execution_details, dr_plan_execution_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.disaster_recovery.DisasterRecoveryClient.cancel_dr_plan_execution` and waits for the :py:class:`~oci.disaster_recovery.models.WorkRequest`
        to enter the given state(s).

        :param oci.disaster_recovery.models.CancelDrPlanExecutionDetails cancel_dr_plan_execution_details: (required)
            Details for canceling a DR Plan Execution.

        :param str dr_plan_execution_id: (required)
            The OCID of the DR Plan Execution.

            Example: `ocid1.drplanexecution.oc1.iad.exampleocid`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.disaster_recovery.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.disaster_recovery.DisasterRecoveryClient.cancel_dr_plan_execution`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.cancel_dr_plan_execution(cancel_dr_plan_execution_details, dr_plan_execution_id, **operation_kwargs)
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

    def change_dr_protection_group_compartment_and_wait_for_state(self, change_dr_protection_group_compartment_details, dr_protection_group_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.disaster_recovery.DisasterRecoveryClient.change_dr_protection_group_compartment` and waits for the :py:class:`~oci.disaster_recovery.models.WorkRequest`
        to enter the given state(s).

        :param oci.disaster_recovery.models.ChangeDrProtectionGroupCompartmentDetails change_dr_protection_group_compartment_details: (required)
            Details of DR Protection Group compartment to change.

        :param str dr_protection_group_id: (required)
            The OCID of the DR Protection Group.

            Example: `ocid1.drprotectiongroup.oc1.phx.exampleocid`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.disaster_recovery.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.disaster_recovery.DisasterRecoveryClient.change_dr_protection_group_compartment`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.change_dr_protection_group_compartment(change_dr_protection_group_compartment_details, dr_protection_group_id, **operation_kwargs)
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

    def create_dr_plan_and_wait_for_state(self, create_dr_plan_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.disaster_recovery.DisasterRecoveryClient.create_dr_plan` and waits for the :py:class:`~oci.disaster_recovery.models.WorkRequest`
        to enter the given state(s).

        :param oci.disaster_recovery.models.CreateDrPlanDetails create_dr_plan_details: (required)
            Details for creating the new DR Plan.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.disaster_recovery.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.disaster_recovery.DisasterRecoveryClient.create_dr_plan`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_dr_plan(create_dr_plan_details, **operation_kwargs)
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

    def create_dr_plan_execution_and_wait_for_state(self, create_dr_plan_execution_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.disaster_recovery.DisasterRecoveryClient.create_dr_plan_execution` and waits for the :py:class:`~oci.disaster_recovery.models.WorkRequest`
        to enter the given state(s).

        :param oci.disaster_recovery.models.CreateDrPlanExecutionDetails create_dr_plan_execution_details: (required)
            Details for the new DR Plan Execution.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.disaster_recovery.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.disaster_recovery.DisasterRecoveryClient.create_dr_plan_execution`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_dr_plan_execution(create_dr_plan_execution_details, **operation_kwargs)
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

    def create_dr_protection_group_and_wait_for_state(self, create_dr_protection_group_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.disaster_recovery.DisasterRecoveryClient.create_dr_protection_group` and waits for the :py:class:`~oci.disaster_recovery.models.WorkRequest`
        to enter the given state(s).

        :param oci.disaster_recovery.models.CreateDrProtectionGroupDetails create_dr_protection_group_details: (required)
            Details for the new DR Protection Group.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.disaster_recovery.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.disaster_recovery.DisasterRecoveryClient.create_dr_protection_group`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_dr_protection_group(create_dr_protection_group_details, **operation_kwargs)
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

    def delete_dr_plan_and_wait_for_state(self, dr_plan_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.disaster_recovery.DisasterRecoveryClient.delete_dr_plan` and waits for the :py:class:`~oci.disaster_recovery.models.DrPlan` acted upon
        to enter the given state(s).

        :param str dr_plan_id: (required)
            The OCID of the DR Plan.

            Example: `ocid1.drplan.oc1.iad.exampleocid`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.disaster_recovery.models.DrPlan.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.disaster_recovery.DisasterRecoveryClient.delete_dr_plan`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_dr_plan(dr_plan_id)
        operation_result = None
        try:
            operation_result = self.client.delete_dr_plan(dr_plan_id, **operation_kwargs)
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

    def delete_dr_plan_execution_and_wait_for_state(self, dr_plan_execution_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.disaster_recovery.DisasterRecoveryClient.delete_dr_plan_execution` and waits for the :py:class:`~oci.disaster_recovery.models.WorkRequest`
        to enter the given state(s).

        :param str dr_plan_execution_id: (required)
            The OCID of the DR Plan Execution.

            Example: `ocid1.drplanexecution.oc1.iad.exampleocid`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.disaster_recovery.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.disaster_recovery.DisasterRecoveryClient.delete_dr_plan_execution`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = None
        try:
            operation_result = self.client.delete_dr_plan_execution(dr_plan_execution_id, **operation_kwargs)
        except oci.exceptions.ServiceError as e:
            if e.status == 404:
                return WAIT_RESOURCE_NOT_FOUND
            else:
                raise e

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

    def delete_dr_protection_group_and_wait_for_state(self, dr_protection_group_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.disaster_recovery.DisasterRecoveryClient.delete_dr_protection_group` and waits for the :py:class:`~oci.disaster_recovery.models.WorkRequest`
        to enter the given state(s).

        :param str dr_protection_group_id: (required)
            The OCID of the DR Protection Group.

            Example: `ocid1.drprotectiongroup.oc1.phx.exampleocid`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.disaster_recovery.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.disaster_recovery.DisasterRecoveryClient.delete_dr_protection_group`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = None
        try:
            operation_result = self.client.delete_dr_protection_group(dr_protection_group_id, **operation_kwargs)
        except oci.exceptions.ServiceError as e:
            if e.status == 404:
                return WAIT_RESOURCE_NOT_FOUND
            else:
                raise e

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

    def disassociate_dr_protection_group_and_wait_for_state(self, disassociate_dr_protection_group_details, dr_protection_group_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.disaster_recovery.DisasterRecoveryClient.disassociate_dr_protection_group` and waits for the :py:class:`~oci.disaster_recovery.models.WorkRequest`
        to enter the given state(s).

        :param oci.disaster_recovery.models.DisassociateDrProtectionGroupDetails disassociate_dr_protection_group_details: (required)
            Details for removing an association between two DR Protection Groups.

        :param str dr_protection_group_id: (required)
            The OCID of the DR Protection Group.

            Example: `ocid1.drprotectiongroup.oc1.phx.exampleocid`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.disaster_recovery.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.disaster_recovery.DisasterRecoveryClient.disassociate_dr_protection_group`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.disassociate_dr_protection_group(disassociate_dr_protection_group_details, dr_protection_group_id, **operation_kwargs)
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

    def ignore_dr_plan_execution_and_wait_for_state(self, ignore_dr_plan_execution_details, dr_plan_execution_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.disaster_recovery.DisasterRecoveryClient.ignore_dr_plan_execution` and waits for the :py:class:`~oci.disaster_recovery.models.WorkRequest`
        to enter the given state(s).

        :param oci.disaster_recovery.models.IgnoreDrPlanExecutionDetails ignore_dr_plan_execution_details: (required)
            Details of the failed group or step to ignore.

        :param str dr_plan_execution_id: (required)
            The OCID of the DR Plan Execution.

            Example: `ocid1.drplanexecution.oc1.iad.exampleocid`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.disaster_recovery.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.disaster_recovery.DisasterRecoveryClient.ignore_dr_plan_execution`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.ignore_dr_plan_execution(ignore_dr_plan_execution_details, dr_plan_execution_id, **operation_kwargs)
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

    def pause_dr_plan_execution_and_wait_for_state(self, pause_dr_plan_execution_details, dr_plan_execution_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.disaster_recovery.DisasterRecoveryClient.pause_dr_plan_execution` and waits for the :py:class:`~oci.disaster_recovery.models.WorkRequest`
        to enter the given state(s).

        :param oci.disaster_recovery.models.PauseDrPlanExecutionDetails pause_dr_plan_execution_details: (required)
            Details for pausing a DR Plan Execution.

        :param str dr_plan_execution_id: (required)
            The OCID of the DR Plan Execution.

            Example: `ocid1.drplanexecution.oc1.iad.exampleocid`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.disaster_recovery.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.disaster_recovery.DisasterRecoveryClient.pause_dr_plan_execution`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.pause_dr_plan_execution(pause_dr_plan_execution_details, dr_plan_execution_id, **operation_kwargs)
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

    def resume_dr_plan_execution_and_wait_for_state(self, resume_dr_plan_execution_details, dr_plan_execution_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.disaster_recovery.DisasterRecoveryClient.resume_dr_plan_execution` and waits for the :py:class:`~oci.disaster_recovery.models.WorkRequest`
        to enter the given state(s).

        :param oci.disaster_recovery.models.ResumeDrPlanExecutionDetails resume_dr_plan_execution_details: (required)
            Details for resuming a DR Plan Execution.

        :param str dr_plan_execution_id: (required)
            The OCID of the DR Plan Execution.

            Example: `ocid1.drplanexecution.oc1.iad.exampleocid`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.disaster_recovery.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.disaster_recovery.DisasterRecoveryClient.resume_dr_plan_execution`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.resume_dr_plan_execution(resume_dr_plan_execution_details, dr_plan_execution_id, **operation_kwargs)
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

    def retry_dr_plan_execution_and_wait_for_state(self, retry_dr_plan_execution_details, dr_plan_execution_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.disaster_recovery.DisasterRecoveryClient.retry_dr_plan_execution` and waits for the :py:class:`~oci.disaster_recovery.models.WorkRequest`
        to enter the given state(s).

        :param oci.disaster_recovery.models.RetryDrPlanExecutionDetails retry_dr_plan_execution_details: (required)
            Details of the failed group or step to retry.

        :param str dr_plan_execution_id: (required)
            The OCID of the DR Plan Execution.

            Example: `ocid1.drplanexecution.oc1.iad.exampleocid`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.disaster_recovery.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.disaster_recovery.DisasterRecoveryClient.retry_dr_plan_execution`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.retry_dr_plan_execution(retry_dr_plan_execution_details, dr_plan_execution_id, **operation_kwargs)
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

    def update_dr_plan_and_wait_for_state(self, update_dr_plan_details, dr_plan_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.disaster_recovery.DisasterRecoveryClient.update_dr_plan` and waits for the :py:class:`~oci.disaster_recovery.models.WorkRequest`
        to enter the given state(s).

        :param oci.disaster_recovery.models.UpdateDrPlanDetails update_dr_plan_details: (required)
            Details of DR Plan to update.

        :param str dr_plan_id: (required)
            The OCID of the DR Plan.

            Example: `ocid1.drplan.oc1.iad.exampleocid`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.disaster_recovery.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.disaster_recovery.DisasterRecoveryClient.update_dr_plan`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_dr_plan(update_dr_plan_details, dr_plan_id, **operation_kwargs)
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

    def update_dr_plan_execution_and_wait_for_state(self, update_dr_plan_execution_details, dr_plan_execution_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.disaster_recovery.DisasterRecoveryClient.update_dr_plan_execution` and waits for the :py:class:`~oci.disaster_recovery.models.WorkRequest`
        to enter the given state(s).

        :param oci.disaster_recovery.models.UpdateDrPlanExecutionDetails update_dr_plan_execution_details: (required)
            Details of DR Plan Execution to update.

        :param str dr_plan_execution_id: (required)
            The OCID of the DR Plan Execution.

            Example: `ocid1.drplanexecution.oc1.iad.exampleocid`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.disaster_recovery.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.disaster_recovery.DisasterRecoveryClient.update_dr_plan_execution`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_dr_plan_execution(update_dr_plan_execution_details, dr_plan_execution_id, **operation_kwargs)
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

    def update_dr_protection_group_and_wait_for_state(self, update_dr_protection_group_details, dr_protection_group_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.disaster_recovery.DisasterRecoveryClient.update_dr_protection_group` and waits for the :py:class:`~oci.disaster_recovery.models.WorkRequest`
        to enter the given state(s).

        :param oci.disaster_recovery.models.UpdateDrProtectionGroupDetails update_dr_protection_group_details: (required)
            Details of DR Protection Group to update.

        :param str dr_protection_group_id: (required)
            The OCID of the DR Protection Group.

            Example: `ocid1.drprotectiongroup.oc1.phx.exampleocid`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.disaster_recovery.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.disaster_recovery.DisasterRecoveryClient.update_dr_protection_group`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_dr_protection_group(update_dr_protection_group_details, dr_protection_group_id, **operation_kwargs)
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

    def update_dr_protection_group_role_and_wait_for_state(self, update_dr_protection_group_role_details, dr_protection_group_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.disaster_recovery.DisasterRecoveryClient.update_dr_protection_group_role` and waits for the :py:class:`~oci.disaster_recovery.models.WorkRequest`
        to enter the given state(s).

        :param oci.disaster_recovery.models.UpdateDrProtectionGroupRoleDetails update_dr_protection_group_role_details: (required)
            The role details for the DR Protection Group.

        :param str dr_protection_group_id: (required)
            The OCID of the DR Protection Group.

            Example: `ocid1.drprotectiongroup.oc1.phx.exampleocid`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.disaster_recovery.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.disaster_recovery.DisasterRecoveryClient.update_dr_protection_group_role`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_dr_protection_group_role(update_dr_protection_group_role_details, dr_protection_group_id, **operation_kwargs)
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
