# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci  # noqa: F401
from oci.util import WAIT_RESOURCE_NOT_FOUND  # noqa: F401


class NetworkLoadBalancerClientCompositeOperations(object):
    """
    This class provides a wrapper around :py:class:`~oci.network_load_balancer.NetworkLoadBalancerClient` and offers convenience methods
    for operations that would otherwise need to be chained together. For example, instead of performing an action
    on a resource (e.g. launching an instance, creating a load balancer) and then using a waiter to wait for the resource
    to enter a given state, you can call a single method in this class to accomplish the same functionality
    """

    def __init__(self, client, **kwargs):
        """
        Creates a new NetworkLoadBalancerClientCompositeOperations object

        :param NetworkLoadBalancerClient client:
            The service client which will be wrapped by this object
        """
        self.client = client

    def change_network_load_balancer_compartment_and_wait_for_state(self, network_load_balancer_id, change_network_load_balancer_compartment_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.network_load_balancer.NetworkLoadBalancerClient.change_network_load_balancer_compartment` and waits for the :py:class:`~oci.network_load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.network_load_balancer.models.ChangeNetworkLoadBalancerCompartmentDetails change_network_load_balancer_compartment_details: (required)
            The configuration details for moving a network load balancer to a different compartment.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.network_load_balancer.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.network_load_balancer.NetworkLoadBalancerClient.change_network_load_balancer_compartment`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.change_network_load_balancer_compartment(network_load_balancer_id, change_network_load_balancer_compartment_details, **operation_kwargs)
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

    def create_backend_and_wait_for_state(self, network_load_balancer_id, create_backend_details, backend_set_name, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.network_load_balancer.NetworkLoadBalancerClient.create_backend` and waits for the :py:class:`~oci.network_load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.network_load_balancer.models.CreateBackendDetails create_backend_details: (required)
            The details to add a backend server to a backend set.

        :param str backend_set_name: (required)
            The name of the backend set to which to add the backend server.

            Example: `example_backend_set`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.network_load_balancer.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.network_load_balancer.NetworkLoadBalancerClient.create_backend`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_backend(network_load_balancer_id, create_backend_details, backend_set_name, **operation_kwargs)
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

    def create_backend_set_and_wait_for_state(self, network_load_balancer_id, create_backend_set_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.network_load_balancer.NetworkLoadBalancerClient.create_backend_set` and waits for the :py:class:`~oci.network_load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.network_load_balancer.models.CreateBackendSetDetails create_backend_set_details: (required)
            The details for adding a backend set.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.network_load_balancer.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.network_load_balancer.NetworkLoadBalancerClient.create_backend_set`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_backend_set(network_load_balancer_id, create_backend_set_details, **operation_kwargs)
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

    def create_listener_and_wait_for_state(self, network_load_balancer_id, create_listener_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.network_load_balancer.NetworkLoadBalancerClient.create_listener` and waits for the :py:class:`~oci.network_load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.network_load_balancer.models.CreateListenerDetails create_listener_details: (required)
            Details to add a listener.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.network_load_balancer.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.network_load_balancer.NetworkLoadBalancerClient.create_listener`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_listener(network_load_balancer_id, create_listener_details, **operation_kwargs)
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

    def create_network_load_balancer_and_wait_for_state(self, create_network_load_balancer_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.network_load_balancer.NetworkLoadBalancerClient.create_network_load_balancer` and waits for the :py:class:`~oci.network_load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param oci.network_load_balancer.models.CreateNetworkLoadBalancerDetails create_network_load_balancer_details: (required)
            Details for the new network load balancer.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.network_load_balancer.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.network_load_balancer.NetworkLoadBalancerClient.create_network_load_balancer`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_network_load_balancer(create_network_load_balancer_details, **operation_kwargs)
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

    def delete_backend_and_wait_for_state(self, network_load_balancer_id, backend_set_name, backend_name, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.network_load_balancer.NetworkLoadBalancerClient.delete_backend` and waits for the :py:class:`~oci.network_load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str backend_set_name: (required)
            The name of the backend set associated with the backend server.

            Example: `example_backend_set`

        :param str backend_name: (required)
            The name of the backend server to remove. This is specified as <ip>:<port>, or as <ip> <OCID>:<port>.

            Example: `10.0.0.3:8080` or `ocid1.privateip..oc1.<var>&lt;unique_ID&gt;</var>:8080`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.network_load_balancer.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.network_load_balancer.NetworkLoadBalancerClient.delete_backend`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = None
        try:
            operation_result = self.client.delete_backend(network_load_balancer_id, backend_set_name, backend_name, **operation_kwargs)
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

    def delete_backend_set_and_wait_for_state(self, network_load_balancer_id, backend_set_name, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.network_load_balancer.NetworkLoadBalancerClient.delete_backend_set` and waits for the :py:class:`~oci.network_load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str backend_set_name: (required)
            The name of the backend set to delete.

            Example: `example_backend_set`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.network_load_balancer.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.network_load_balancer.NetworkLoadBalancerClient.delete_backend_set`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = None
        try:
            operation_result = self.client.delete_backend_set(network_load_balancer_id, backend_set_name, **operation_kwargs)
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

    def delete_listener_and_wait_for_state(self, network_load_balancer_id, listener_name, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.network_load_balancer.NetworkLoadBalancerClient.delete_listener` and waits for the :py:class:`~oci.network_load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str listener_name: (required)
            The name of the listener to delete.

            Example: `example_listener`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.network_load_balancer.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.network_load_balancer.NetworkLoadBalancerClient.delete_listener`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = None
        try:
            operation_result = self.client.delete_listener(network_load_balancer_id, listener_name, **operation_kwargs)
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

    def delete_network_load_balancer_and_wait_for_state(self, network_load_balancer_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.network_load_balancer.NetworkLoadBalancerClient.delete_network_load_balancer` and waits for the :py:class:`~oci.network_load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.network_load_balancer.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.network_load_balancer.NetworkLoadBalancerClient.delete_network_load_balancer`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = None
        try:
            operation_result = self.client.delete_network_load_balancer(network_load_balancer_id, **operation_kwargs)
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

    def update_backend_and_wait_for_state(self, network_load_balancer_id, update_backend_details, backend_set_name, backend_name, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.network_load_balancer.NetworkLoadBalancerClient.update_backend` and waits for the :py:class:`~oci.network_load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.network_load_balancer.models.UpdateBackendDetails update_backend_details: (required)
            Details for updating a backend server.

        :param str backend_set_name: (required)
            The name of the backend set associated with the backend server.

            Example: `example_backend_set`

        :param str backend_name: (required)
            The name of the backend server to update. This is specified as <ip>:<port>, or as <ip> <OCID>:<port>.

            Example: `10.0.0.3:8080` or `ocid1.privateip..oc1.<var>&lt;unique_ID&gt;</var>:8080`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.network_load_balancer.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.network_load_balancer.NetworkLoadBalancerClient.update_backend`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_backend(network_load_balancer_id, update_backend_details, backend_set_name, backend_name, **operation_kwargs)
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

    def update_backend_set_and_wait_for_state(self, network_load_balancer_id, update_backend_set_details, backend_set_name, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.network_load_balancer.NetworkLoadBalancerClient.update_backend_set` and waits for the :py:class:`~oci.network_load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.network_load_balancer.models.UpdateBackendSetDetails update_backend_set_details: (required)
            The details to update a backend set.

        :param str backend_set_name: (required)
            The name of the backend set to update.

            Example: `example_backend_set`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.network_load_balancer.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.network_load_balancer.NetworkLoadBalancerClient.update_backend_set`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_backend_set(network_load_balancer_id, update_backend_set_details, backend_set_name, **operation_kwargs)
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

    def update_health_checker_and_wait_for_state(self, network_load_balancer_id, update_health_checker_details, backend_set_name, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.network_load_balancer.NetworkLoadBalancerClient.update_health_checker` and waits for the :py:class:`~oci.network_load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.network_load_balancer.models.UpdateHealthCheckerDetails update_health_checker_details: (required)
            The health check policy configuration details.

        :param str backend_set_name: (required)
            The name of the backend set associated with the health check policy to be retrieved.

            Example: `example_backend_set`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.network_load_balancer.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.network_load_balancer.NetworkLoadBalancerClient.update_health_checker`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_health_checker(network_load_balancer_id, update_health_checker_details, backend_set_name, **operation_kwargs)
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

    def update_listener_and_wait_for_state(self, network_load_balancer_id, update_listener_details, listener_name, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.network_load_balancer.NetworkLoadBalancerClient.update_listener` and waits for the :py:class:`~oci.network_load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.network_load_balancer.models.UpdateListenerDetails update_listener_details: (required)
            Details to update a listener.

        :param str listener_name: (required)
            The name of the listener to update.

            Example: `example_listener`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.network_load_balancer.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.network_load_balancer.NetworkLoadBalancerClient.update_listener`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_listener(network_load_balancer_id, update_listener_details, listener_name, **operation_kwargs)
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

    def update_network_load_balancer_and_wait_for_state(self, network_load_balancer_id, update_network_load_balancer_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.network_load_balancer.NetworkLoadBalancerClient.update_network_load_balancer` and waits for the :py:class:`~oci.network_load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.network_load_balancer.models.UpdateNetworkLoadBalancerDetails update_network_load_balancer_details: (required)
            The information to be updated.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.network_load_balancer.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.network_load_balancer.NetworkLoadBalancerClient.update_network_load_balancer`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_network_load_balancer(network_load_balancer_id, update_network_load_balancer_details, **operation_kwargs)
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

    def update_network_security_groups_and_wait_for_state(self, network_load_balancer_id, update_network_security_groups_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.network_load_balancer.NetworkLoadBalancerClient.update_network_security_groups` and waits for the :py:class:`~oci.network_load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.network_load_balancer.models.UpdateNetworkSecurityGroupsDetails update_network_security_groups_details: (required)
            The details for updating the network security groups associated with the specified network load balancer.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.network_load_balancer.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.network_load_balancer.NetworkLoadBalancerClient.update_network_security_groups`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_network_security_groups(network_load_balancer_id, update_network_security_groups_details, **operation_kwargs)
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
