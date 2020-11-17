# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci  # noqa: F401
from oci.util import WAIT_RESOURCE_NOT_FOUND  # noqa: F401


class LogAnalyticsClientCompositeOperations(object):
    """
    This class provides a wrapper around :py:class:`~oci.log_analytics.LogAnalyticsClient` and offers convenience methods
    for operations that would otherwise need to be chained together. For example, instead of performing an action
    on a resource (e.g. launching an instance, creating a load balancer) and then using a waiter to wait for the resource
    to enter a given state, you can call a single method in this class to accomplish the same functionality
    """

    def __init__(self, client, **kwargs):
        """
        Creates a new LogAnalyticsClientCompositeOperations object

        :param LogAnalyticsClient client:
            The service client which will be wrapped by this object
        """
        self.client = client

    def create_log_analytics_entity_and_wait_for_state(self, namespace_name, create_log_analytics_entity_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.log_analytics.LogAnalyticsClient.create_log_analytics_entity` and waits for the :py:class:`~oci.log_analytics.models.LogAnalyticsEntity` acted upon
        to enter the given state(s).

        :param str namespace_name: (required)
            The Logging Analytics namespace used for the request.

        :param CreateLogAnalyticsEntityDetails create_log_analytics_entity_details: (required)
            Details for the new log analytics entity.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.log_analytics.models.LogAnalyticsEntity.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.log_analytics.LogAnalyticsClient.create_log_analytics_entity`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_log_analytics_entity(namespace_name, create_log_analytics_entity_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_log_analytics_entity(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_log_analytics_object_collection_rule_and_wait_for_state(self, namespace_name, create_log_analytics_object_collection_rule_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.log_analytics.LogAnalyticsClient.create_log_analytics_object_collection_rule` and waits for the :py:class:`~oci.log_analytics.models.LogAnalyticsObjectCollectionRule` acted upon
        to enter the given state(s).

        :param str namespace_name: (required)
            The Logging Analytics namespace used for the request.

        :param CreateLogAnalyticsObjectCollectionRuleDetails create_log_analytics_object_collection_rule_details: (required)
            Details of the rule to be created.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.log_analytics.models.LogAnalyticsObjectCollectionRule.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.log_analytics.LogAnalyticsClient.create_log_analytics_object_collection_rule`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_log_analytics_object_collection_rule(namespace_name, create_log_analytics_object_collection_rule_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_log_analytics_object_collection_rule(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_scheduled_task_and_wait_for_state(self, namespace_name, create_scheduled_task_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.log_analytics.LogAnalyticsClient.create_scheduled_task` and waits for the :py:class:`~oci.log_analytics.models.ScheduledTask` acted upon
        to enter the given state(s).

        :param str namespace_name: (required)
            The Logging Analytics namespace used for the request.

        :param CreateScheduledTaskDetails create_scheduled_task_details: (required)
            Scheduled task to be created.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.log_analytics.models.ScheduledTask.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.log_analytics.LogAnalyticsClient.create_scheduled_task`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_scheduled_task(namespace_name, create_scheduled_task_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_scheduled_task(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_associations_and_wait_for_state(self, namespace_name, delete_log_analytics_association_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.log_analytics.LogAnalyticsClient.delete_associations` and waits for the :py:class:`~oci.log_analytics.models.WorkRequest`
        to enter the given state(s).

        :param str namespace_name: (required)
            The Logging Analytics namespace used for the request.

        :param DeleteLogAnalyticsAssociationDetails delete_log_analytics_association_details: (required)
            details for association

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.log_analytics.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.log_analytics.LogAnalyticsClient.delete_associations`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.delete_associations(namespace_name, delete_log_analytics_association_details, **operation_kwargs)
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

    def offboard_namespace_and_wait_for_state(self, namespace_name, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.log_analytics.LogAnalyticsClient.offboard_namespace` and waits for the :py:class:`~oci.log_analytics.models.WorkRequest`
        to enter the given state(s).

        :param str namespace_name: (required)
            The Logging Analytics namespace used for the request.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.log_analytics.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.log_analytics.LogAnalyticsClient.offboard_namespace`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.offboard_namespace(namespace_name, **operation_kwargs)
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

    def onboard_namespace_and_wait_for_state(self, namespace_name, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.log_analytics.LogAnalyticsClient.onboard_namespace` and waits for the :py:class:`~oci.log_analytics.models.WorkRequest`
        to enter the given state(s).

        :param str namespace_name: (required)
            The Logging Analytics namespace used for the request.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.log_analytics.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.log_analytics.LogAnalyticsClient.onboard_namespace`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.onboard_namespace(namespace_name, **operation_kwargs)
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

    def purge_storage_data_and_wait_for_state(self, namespace_name, purge_storage_data_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.log_analytics.LogAnalyticsClient.purge_storage_data` and waits for the :py:class:`~oci.log_analytics.models.WorkRequest`
        to enter the given state(s).

        :param str namespace_name: (required)
            The Logging Analytics namespace used for the request.

        :param PurgeStorageDataDetails purge_storage_data_details: (required)
            This is the input to purge old data.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.log_analytics.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.log_analytics.LogAnalyticsClient.purge_storage_data`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.purge_storage_data(namespace_name, purge_storage_data_details, **operation_kwargs)
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

    def query_and_wait_for_state(self, namespace_name, query_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.log_analytics.LogAnalyticsClient.query` and waits for the :py:class:`~oci.log_analytics.models.WorkRequest`
        to enter the given state(s).

        :param str namespace_name: (required)
            The Logging Analytics namespace used for the request.

        :param QueryDetails query_details: (required)
            Query to be executed.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.log_analytics.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.log_analytics.LogAnalyticsClient.query`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.query(namespace_name, query_details, **operation_kwargs)
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

    def recall_archived_data_and_wait_for_state(self, namespace_name, recall_archived_data_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.log_analytics.LogAnalyticsClient.recall_archived_data` and waits for the :py:class:`~oci.log_analytics.models.WorkRequest`
        to enter the given state(s).

        :param str namespace_name: (required)
            The Logging Analytics namespace used for the request.

        :param RecallArchivedDataDetails recall_archived_data_details: (required)
            This is the input to recall archived data.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.log_analytics.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.log_analytics.LogAnalyticsClient.recall_archived_data`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.recall_archived_data(namespace_name, recall_archived_data_details, **operation_kwargs)
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

    def release_recalled_data_and_wait_for_state(self, namespace_name, release_recalled_data_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.log_analytics.LogAnalyticsClient.release_recalled_data` and waits for the :py:class:`~oci.log_analytics.models.WorkRequest`
        to enter the given state(s).

        :param str namespace_name: (required)
            The Logging Analytics namespace used for the request.

        :param ReleaseRecalledDataDetails release_recalled_data_details: (required)
            This is the input to release recalled data

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.log_analytics.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.log_analytics.LogAnalyticsClient.release_recalled_data`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.release_recalled_data(namespace_name, release_recalled_data_details, **operation_kwargs)
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

    def update_log_analytics_entity_and_wait_for_state(self, namespace_name, log_analytics_entity_id, update_log_analytics_entity_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.log_analytics.LogAnalyticsClient.update_log_analytics_entity` and waits for the :py:class:`~oci.log_analytics.models.LogAnalyticsEntity` acted upon
        to enter the given state(s).

        :param str namespace_name: (required)
            The Logging Analytics namespace used for the request.

        :param str log_analytics_entity_id: (required)
            The log analytics entity OCID.

        :param UpdateLogAnalyticsEntityDetails update_log_analytics_entity_details: (required)
            The information to be updated.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.log_analytics.models.LogAnalyticsEntity.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.log_analytics.LogAnalyticsClient.update_log_analytics_entity`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_log_analytics_entity(namespace_name, log_analytics_entity_id, update_log_analytics_entity_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_log_analytics_entity(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_log_analytics_object_collection_rule_and_wait_for_state(self, namespace_name, log_analytics_object_collection_rule_id, update_log_analytics_object_collection_rule_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.log_analytics.LogAnalyticsClient.update_log_analytics_object_collection_rule` and waits for the :py:class:`~oci.log_analytics.models.LogAnalyticsObjectCollectionRule` acted upon
        to enter the given state(s).

        :param str namespace_name: (required)
            The Logging Analytics namespace used for the request.

        :param str log_analytics_object_collection_rule_id: (required)
            The Logging Analytics Object Collection Rule `OCID`__

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param UpdateLogAnalyticsObjectCollectionRuleDetails update_log_analytics_object_collection_rule_details: (required)
            The rule config to be updated.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.log_analytics.models.LogAnalyticsObjectCollectionRule.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.log_analytics.LogAnalyticsClient.update_log_analytics_object_collection_rule`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_log_analytics_object_collection_rule(namespace_name, log_analytics_object_collection_rule_id, update_log_analytics_object_collection_rule_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_log_analytics_object_collection_rule(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_scheduled_task_and_wait_for_state(self, namespace_name, scheduled_task_id, update_scheduled_task_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.log_analytics.LogAnalyticsClient.update_scheduled_task` and waits for the :py:class:`~oci.log_analytics.models.ScheduledTask` acted upon
        to enter the given state(s).

        :param str namespace_name: (required)
            The Logging Analytics namespace used for the request.

        :param str scheduled_task_id: (required)
            Unique scheduledTask id returned from task create.
            If invalid will lead to a 404 not found.

        :param UpdateScheduledTaskDetails update_scheduled_task_details: (required)
            Update details.
            Schedules may be updated only for taskType SAVED_SEARCH and PURGE.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.log_analytics.models.ScheduledTask.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.log_analytics.LogAnalyticsClient.update_scheduled_task`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_scheduled_task(namespace_name, scheduled_task_id, update_scheduled_task_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_scheduled_task(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def upsert_associations_and_wait_for_state(self, namespace_name, upsert_log_analytics_association_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.log_analytics.LogAnalyticsClient.upsert_associations` and waits for the :py:class:`~oci.log_analytics.models.WorkRequest`
        to enter the given state(s).

        :param str namespace_name: (required)
            The Logging Analytics namespace used for the request.

        :param UpsertLogAnalyticsAssociationDetails upsert_log_analytics_association_details: (required)
            list of association details

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.log_analytics.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.log_analytics.LogAnalyticsClient.upsert_associations`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.upsert_associations(namespace_name, upsert_log_analytics_association_details, **operation_kwargs)
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
