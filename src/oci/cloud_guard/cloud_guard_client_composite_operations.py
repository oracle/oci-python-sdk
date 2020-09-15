# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci  # noqa: F401
from oci.util import WAIT_RESOURCE_NOT_FOUND  # noqa: F401


class CloudGuardClientCompositeOperations(object):
    """
    This class provides a wrapper around :py:class:`~oci.cloud_guard.CloudGuardClient` and offers convenience methods
    for operations that would otherwise need to be chained together. For example, instead of performing an action
    on a resource (e.g. launching an instance, creating a load balancer) and then using a waiter to wait for the resource
    to enter a given state, you can call a single method in this class to accomplish the same functionality
    """

    def __init__(self, client, **kwargs):
        """
        Creates a new CloudGuardClientCompositeOperations object

        :param CloudGuardClient client:
            The service client which will be wrapped by this object
        """
        self.client = client

    def create_detector_recipe_and_wait_for_state(self, create_detector_recipe_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.cloud_guard.CloudGuardClient.create_detector_recipe` and waits for the :py:class:`~oci.cloud_guard.models.DetectorRecipe` acted upon
        to enter the given state(s).

        :param CreateDetectorRecipeDetails create_detector_recipe_details: (required)
            Details for the new DetectorRecipe.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.cloud_guard.models.DetectorRecipe.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.cloud_guard.CloudGuardClient.create_detector_recipe`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_detector_recipe(create_detector_recipe_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_detector_recipe(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_managed_list_and_wait_for_state(self, create_managed_list_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.cloud_guard.CloudGuardClient.create_managed_list` and waits for the :py:class:`~oci.cloud_guard.models.ManagedList` acted upon
        to enter the given state(s).

        :param CreateManagedListDetails create_managed_list_details: (required)
            Details for the new ManagedList.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.cloud_guard.models.ManagedList.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.cloud_guard.CloudGuardClient.create_managed_list`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_managed_list(create_managed_list_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_managed_list(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_responder_recipe_and_wait_for_state(self, create_responder_recipe_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.cloud_guard.CloudGuardClient.create_responder_recipe` and waits for the :py:class:`~oci.cloud_guard.models.ResponderRecipe` acted upon
        to enter the given state(s).

        :param CreateResponderRecipeDetails create_responder_recipe_details: (required)
            Details for ResponderRecipe.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.cloud_guard.models.ResponderRecipe.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.cloud_guard.CloudGuardClient.create_responder_recipe`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_responder_recipe(create_responder_recipe_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_responder_recipe(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_target_and_wait_for_state(self, create_target_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.cloud_guard.CloudGuardClient.create_target` and waits for the :py:class:`~oci.cloud_guard.models.Target` acted upon
        to enter the given state(s).

        :param CreateTargetDetails create_target_details: (required)
            Details for the new Target.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.cloud_guard.models.Target.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.cloud_guard.CloudGuardClient.create_target`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_target(create_target_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_target(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_target_detector_recipe_and_wait_for_state(self, target_id, attach_target_detector_recipe_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.cloud_guard.CloudGuardClient.create_target_detector_recipe` and waits for the :py:class:`~oci.cloud_guard.models.TargetDetectorRecipe` acted upon
        to enter the given state(s).

        :param str target_id: (required)
            OCID of target

        :param AttachTargetDetectorRecipeDetails attach_target_detector_recipe_details: (required)
            Details for associating DetectorRecipe to Target

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.cloud_guard.models.TargetDetectorRecipe.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.cloud_guard.CloudGuardClient.create_target_detector_recipe`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_target_detector_recipe(target_id, attach_target_detector_recipe_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_target_detector_recipe(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_detector_recipe_and_wait_for_state(self, detector_recipe_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.cloud_guard.CloudGuardClient.delete_detector_recipe` and waits for the :py:class:`~oci.cloud_guard.models.DetectorRecipe` acted upon
        to enter the given state(s).

        :param str detector_recipe_id: (required)
            DetectorRecipe OCID

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.cloud_guard.models.DetectorRecipe.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.cloud_guard.CloudGuardClient.delete_detector_recipe`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_detector_recipe(detector_recipe_id)
        operation_result = None
        try:
            operation_result = self.client.delete_detector_recipe(detector_recipe_id, **operation_kwargs)
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

    def delete_managed_list_and_wait_for_state(self, managed_list_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.cloud_guard.CloudGuardClient.delete_managed_list` and waits for the :py:class:`~oci.cloud_guard.models.ManagedList` acted upon
        to enter the given state(s).

        :param str managed_list_id: (required)
            The cloudguard list OCID to be passed in the request.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.cloud_guard.models.ManagedList.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.cloud_guard.CloudGuardClient.delete_managed_list`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_managed_list(managed_list_id)
        operation_result = None
        try:
            operation_result = self.client.delete_managed_list(managed_list_id, **operation_kwargs)
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

    def delete_responder_recipe_and_wait_for_state(self, responder_recipe_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.cloud_guard.CloudGuardClient.delete_responder_recipe` and waits for the :py:class:`~oci.cloud_guard.models.ResponderRecipe` acted upon
        to enter the given state(s).

        :param str responder_recipe_id: (required)
            OCID of ResponderRecipe

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.cloud_guard.models.ResponderRecipe.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.cloud_guard.CloudGuardClient.delete_responder_recipe`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_responder_recipe(responder_recipe_id)
        operation_result = None
        try:
            operation_result = self.client.delete_responder_recipe(responder_recipe_id, **operation_kwargs)
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

    def delete_target_and_wait_for_state(self, target_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.cloud_guard.CloudGuardClient.delete_target` and waits for the :py:class:`~oci.cloud_guard.models.Target` acted upon
        to enter the given state(s).

        :param str target_id: (required)
            OCID of target

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.cloud_guard.models.Target.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.cloud_guard.CloudGuardClient.delete_target`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_target(target_id)
        operation_result = None
        try:
            operation_result = self.client.delete_target(target_id, **operation_kwargs)
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

    def update_detector_recipe_and_wait_for_state(self, detector_recipe_id, update_detector_recipe_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.cloud_guard.CloudGuardClient.update_detector_recipe` and waits for the :py:class:`~oci.cloud_guard.models.DetectorRecipe` acted upon
        to enter the given state(s).

        :param str detector_recipe_id: (required)
            DetectorRecipe OCID

        :param UpdateDetectorRecipeDetails update_detector_recipe_details: (required)
            Details for the DetectorRecipe to be updated

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.cloud_guard.models.DetectorRecipe.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.cloud_guard.CloudGuardClient.update_detector_recipe`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_detector_recipe(detector_recipe_id, update_detector_recipe_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_detector_recipe(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_detector_recipe_detector_rule_and_wait_for_state(self, detector_recipe_id, detector_rule_id, update_detector_recipe_detector_rule_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.cloud_guard.CloudGuardClient.update_detector_recipe_detector_rule` and waits for the :py:class:`~oci.cloud_guard.models.DetectorRecipeDetectorRule` acted upon
        to enter the given state(s).

        :param str detector_recipe_id: (required)
            DetectorRecipe OCID

        :param str detector_rule_id: (required)
            The key of Detector Rule.

        :param UpdateDetectorRecipeDetectorRuleDetails update_detector_recipe_detector_rule_details: (required)
            The details to be updated for DetectorRule.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.cloud_guard.models.DetectorRecipeDetectorRule.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.cloud_guard.CloudGuardClient.update_detector_recipe_detector_rule`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_detector_recipe_detector_rule(detector_recipe_id, detector_rule_id, update_detector_recipe_detector_rule_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_detector_recipe_detector_rule(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_managed_list_and_wait_for_state(self, managed_list_id, update_managed_list_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.cloud_guard.CloudGuardClient.update_managed_list` and waits for the :py:class:`~oci.cloud_guard.models.ManagedList` acted upon
        to enter the given state(s).

        :param str managed_list_id: (required)
            The cloudguard list OCID to be passed in the request.

        :param UpdateManagedListDetails update_managed_list_details: (required)
            Details for the ManagedList to be updated

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.cloud_guard.models.ManagedList.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.cloud_guard.CloudGuardClient.update_managed_list`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_managed_list(managed_list_id, update_managed_list_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_managed_list(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_problem_status_and_wait_for_state(self, problem_id, update_problem_status_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.cloud_guard.CloudGuardClient.update_problem_status` and waits for the :py:class:`~oci.cloud_guard.models.Problem` acted upon
        to enter the given state(s).

        :param str problem_id: (required)
            OCId of the problem.

        :param UpdateProblemStatusDetails update_problem_status_details: (required)
            The additional details for the problem.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.cloud_guard.models.Problem.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.cloud_guard.CloudGuardClient.update_problem_status`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_problem_status(problem_id, update_problem_status_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_problem(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_responder_recipe_and_wait_for_state(self, responder_recipe_id, update_responder_recipe_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.cloud_guard.CloudGuardClient.update_responder_recipe` and waits for the :py:class:`~oci.cloud_guard.models.ResponderRecipe` acted upon
        to enter the given state(s).

        :param str responder_recipe_id: (required)
            OCID of ResponderRecipe

        :param UpdateResponderRecipeDetails update_responder_recipe_details: (required)
            The details to be updated.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.cloud_guard.models.ResponderRecipe.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.cloud_guard.CloudGuardClient.update_responder_recipe`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_responder_recipe(responder_recipe_id, update_responder_recipe_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_responder_recipe(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_responder_recipe_responder_rule_and_wait_for_state(self, responder_recipe_id, responder_rule_id, update_responder_recipe_responder_rule_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.cloud_guard.CloudGuardClient.update_responder_recipe_responder_rule` and waits for the :py:class:`~oci.cloud_guard.models.ResponderRecipeResponderRule` acted upon
        to enter the given state(s).

        :param str responder_recipe_id: (required)
            OCID of ResponderRecipe

        :param str responder_rule_id: (required)
            The id of ResponderRule

        :param UpdateResponderRecipeResponderRuleDetails update_responder_recipe_responder_rule_details: (required)
            The details to be updated for ResponderRule.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.cloud_guard.models.ResponderRecipeResponderRule.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.cloud_guard.CloudGuardClient.update_responder_recipe_responder_rule`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_responder_recipe_responder_rule(responder_recipe_id, responder_rule_id, update_responder_recipe_responder_rule_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_responder_recipe_responder_rule(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_target_and_wait_for_state(self, target_id, update_target_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.cloud_guard.CloudGuardClient.update_target` and waits for the :py:class:`~oci.cloud_guard.models.Target` acted upon
        to enter the given state(s).

        :param str target_id: (required)
            OCID of target

        :param UpdateTargetDetails update_target_details: (required)
            The information to be updated.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.cloud_guard.models.Target.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.cloud_guard.CloudGuardClient.update_target`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_target(target_id, update_target_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_target(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_target_detector_recipe_and_wait_for_state(self, target_id, target_detector_recipe_id, update_target_detector_recipe_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.cloud_guard.CloudGuardClient.update_target_detector_recipe` and waits for the :py:class:`~oci.cloud_guard.models.TargetDetectorRecipe` acted upon
        to enter the given state(s).

        :param str target_id: (required)
            OCID of target

        :param str target_detector_recipe_id: (required)
            OCID of TargetDetectorRecipe

        :param UpdateTargetDetectorRecipeDetails update_target_detector_recipe_details: (required)
            The details to be updated.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.cloud_guard.models.TargetDetectorRecipe.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.cloud_guard.CloudGuardClient.update_target_detector_recipe`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_target_detector_recipe(target_id, target_detector_recipe_id, update_target_detector_recipe_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_target_detector_recipe(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_target_detector_recipe_detector_rule_and_wait_for_state(self, target_id, target_detector_recipe_id, detector_rule_id, update_target_detector_recipe_detector_rule_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.cloud_guard.CloudGuardClient.update_target_detector_recipe_detector_rule` and waits for the :py:class:`~oci.cloud_guard.models.TargetDetectorRecipeDetectorRule` acted upon
        to enter the given state(s).

        :param str target_id: (required)
            OCID of target

        :param str target_detector_recipe_id: (required)
            OCID of TargetDetectorRecipe

        :param str detector_rule_id: (required)
            The id of DetectorRule

        :param UpdateTargetDetectorRecipeDetectorRuleDetails update_target_detector_recipe_detector_rule_details: (required)
            The details to be updated for DetectorRule.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.cloud_guard.models.TargetDetectorRecipeDetectorRule.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.cloud_guard.CloudGuardClient.update_target_detector_recipe_detector_rule`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_target_detector_recipe_detector_rule(target_id, target_detector_recipe_id, detector_rule_id, update_target_detector_recipe_detector_rule_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_target_detector_recipe_detector_rule(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_target_responder_recipe_responder_rule_and_wait_for_state(self, target_id, target_responder_recipe_id, responder_rule_id, update_target_responder_recipe_responder_rule_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.cloud_guard.CloudGuardClient.update_target_responder_recipe_responder_rule` and waits for the :py:class:`~oci.cloud_guard.models.TargetResponderRecipeResponderRule` acted upon
        to enter the given state(s).

        :param str target_id: (required)
            OCID of target

        :param str target_responder_recipe_id: (required)
            OCID of TargetResponderRecipe

        :param str responder_rule_id: (required)
            The id of ResponderRule

        :param UpdateTargetResponderRecipeResponderRuleDetails update_target_responder_recipe_responder_rule_details: (required)
            The details to be updated for ResponderRule.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.cloud_guard.models.TargetResponderRecipeResponderRule.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.cloud_guard.CloudGuardClient.update_target_responder_recipe_responder_rule`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_target_responder_recipe_responder_rule(target_id, target_responder_recipe_id, responder_rule_id, update_target_responder_recipe_responder_rule_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_target_responder_recipe_responder_rule(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
