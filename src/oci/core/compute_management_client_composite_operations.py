# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci  # noqa: F401
from oci.util import WAIT_RESOURCE_NOT_FOUND  # noqa: F401


class ComputeManagementClientCompositeOperations(object):
    """
    This class provides a wrapper around :py:class:`~oci.core.ComputeManagementClient` and offers convenience methods
    for operations that would otherwise need to be chained together. For example, instead of performing an action
    on a resource (e.g. launching an instance, creating a load balancer) and then using a waiter to wait for the resource
    to enter a given state, you can call a single method in this class to accomplish the same functionality
    """

    def __init__(self, client, work_request_client=None, **kwargs):
        """
        Creates a new ComputeManagementClientCompositeOperations object

        :param ComputeManagementClient client:
            The service client which will be wrapped by this object

        :param oci.work_requests.WorkRequestClient work_request_client: (optional)
            The work request service client which will be used to wait for work request states. Default is None.
        """
        self.client = client
        self._work_request_client = work_request_client if work_request_client else oci.work_requests.WorkRequestClient(self.client._config, **self.client._kwargs)

    def attach_load_balancer_and_wait_for_state(self, instance_pool_id, attach_load_balancer_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeManagementClient.attach_load_balancer` and waits for the :py:class:`~oci.core.models.InstancePool` acted upon
        to enter the given state(s).

        :param str instance_pool_id: (required)
            The `OCID`__ of the instance pool.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param AttachLoadBalancerDetails attach_load_balancer_details: (required)
            Load balancer being attached

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.InstancePool.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeManagementClient.attach_load_balancer`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.attach_load_balancer(instance_pool_id, attach_load_balancer_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_instance_pool(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_cluster_network_and_wait_for_work_request(self, create_cluster_network_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeManagementClient.create_cluster_network` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param CreateClusterNetworkDetails create_cluster_network_details: (required)
            Cluster network creation details

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeManagementClient.create_cluster_network`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_cluster_network(create_cluster_network_details, **operation_kwargs)
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

    def create_cluster_network_and_wait_for_state(self, create_cluster_network_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeManagementClient.create_cluster_network` and waits for the :py:class:`~oci.core.models.ClusterNetwork` acted upon
        to enter the given state(s).

        :param CreateClusterNetworkDetails create_cluster_network_details: (required)
            Cluster network creation details

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.ClusterNetwork.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeManagementClient.create_cluster_network`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_cluster_network(create_cluster_network_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_cluster_network(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_instance_pool_and_wait_for_state(self, create_instance_pool_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeManagementClient.create_instance_pool` and waits for the :py:class:`~oci.core.models.InstancePool` acted upon
        to enter the given state(s).

        :param CreateInstancePoolDetails create_instance_pool_details: (required)
            Instance pool creation details

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.InstancePool.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeManagementClient.create_instance_pool`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_instance_pool(create_instance_pool_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_instance_pool(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def detach_load_balancer_and_wait_for_state(self, instance_pool_id, detach_load_balancer_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeManagementClient.detach_load_balancer` and waits for the :py:class:`~oci.core.models.InstancePool` acted upon
        to enter the given state(s).

        :param str instance_pool_id: (required)
            The `OCID`__ of the instance pool.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param DetachLoadBalancerDetails detach_load_balancer_details: (required)
            Load balancer being detached

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.InstancePool.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeManagementClient.detach_load_balancer`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.detach_load_balancer(instance_pool_id, detach_load_balancer_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_instance_pool(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def launch_instance_configuration_and_wait_for_work_request(self, instance_configuration_id, instance_configuration, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeManagementClient.launch_instance_configuration` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str instance_configuration_id: (required)
            The OCID of the instance configuration.

        :param InstanceConfigurationInstanceDetails instance_configuration: (required)
            Instance configuration Instance Details

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeManagementClient.launch_instance_configuration`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.launch_instance_configuration(instance_configuration_id, instance_configuration, **operation_kwargs)
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

    def reset_instance_pool_and_wait_for_state(self, instance_pool_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeManagementClient.reset_instance_pool` and waits for the :py:class:`~oci.core.models.InstancePool` acted upon
        to enter the given state(s).

        :param str instance_pool_id: (required)
            The `OCID`__ of the instance pool.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.InstancePool.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeManagementClient.reset_instance_pool`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.reset_instance_pool(instance_pool_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_instance_pool(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def softreset_instance_pool_and_wait_for_state(self, instance_pool_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeManagementClient.softreset_instance_pool` and waits for the :py:class:`~oci.core.models.InstancePool` acted upon
        to enter the given state(s).

        :param str instance_pool_id: (required)
            The `OCID`__ of the instance pool.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.InstancePool.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeManagementClient.softreset_instance_pool`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.softreset_instance_pool(instance_pool_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_instance_pool(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def start_instance_pool_and_wait_for_state(self, instance_pool_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeManagementClient.start_instance_pool` and waits for the :py:class:`~oci.core.models.InstancePool` acted upon
        to enter the given state(s).

        :param str instance_pool_id: (required)
            The `OCID`__ of the instance pool.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.InstancePool.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeManagementClient.start_instance_pool`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.start_instance_pool(instance_pool_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_instance_pool(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def stop_instance_pool_and_wait_for_state(self, instance_pool_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeManagementClient.stop_instance_pool` and waits for the :py:class:`~oci.core.models.InstancePool` acted upon
        to enter the given state(s).

        :param str instance_pool_id: (required)
            The `OCID`__ of the instance pool.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.InstancePool.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeManagementClient.stop_instance_pool`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.stop_instance_pool(instance_pool_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_instance_pool(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def terminate_cluster_network_and_wait_for_work_request(self, cluster_network_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeManagementClient.terminate_cluster_network` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str cluster_network_id: (required)
            The `OCID`__ of the cluster network.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeManagementClient.terminate_cluster_network`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.terminate_cluster_network(cluster_network_id, **operation_kwargs)
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

    def terminate_instance_pool_and_wait_for_state(self, instance_pool_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeManagementClient.terminate_instance_pool` and waits for the :py:class:`~oci.core.models.InstancePool` acted upon
        to enter the given state(s).

        :param str instance_pool_id: (required)
            The `OCID`__ of the instance pool.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.InstancePool.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeManagementClient.terminate_instance_pool`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_instance_pool(instance_pool_id)
        operation_result = None
        try:
            operation_result = self.client.terminate_instance_pool(instance_pool_id, **operation_kwargs)
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

    def update_cluster_network_and_wait_for_state(self, cluster_network_id, update_cluster_network_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeManagementClient.update_cluster_network` and waits for the :py:class:`~oci.core.models.ClusterNetwork` acted upon
        to enter the given state(s).

        :param str cluster_network_id: (required)
            The `OCID`__ of the cluster network.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param UpdateClusterNetworkDetails update_cluster_network_details: (required)
            Update cluster network

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.ClusterNetwork.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeManagementClient.update_cluster_network`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_cluster_network(cluster_network_id, update_cluster_network_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_cluster_network(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_instance_pool_and_wait_for_state(self, instance_pool_id, update_instance_pool_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.ComputeManagementClient.update_instance_pool` and waits for the :py:class:`~oci.core.models.InstancePool` acted upon
        to enter the given state(s).

        :param str instance_pool_id: (required)
            The `OCID`__ of the instance pool.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateInstancePoolDetails update_instance_pool_details: (required)
            Update instance pool configuration

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.InstancePool.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.ComputeManagementClient.update_instance_pool`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_instance_pool(instance_pool_id, update_instance_pool_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_instance_pool(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
