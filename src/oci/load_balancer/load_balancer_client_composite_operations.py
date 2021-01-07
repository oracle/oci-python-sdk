# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci  # noqa: F401
from oci.util import WAIT_RESOURCE_NOT_FOUND  # noqa: F401


class LoadBalancerClientCompositeOperations(object):
    """
    This class provides a wrapper around :py:class:`~oci.load_balancer.LoadBalancerClient` and offers convenience methods
    for operations that would otherwise need to be chained together. For example, instead of performing an action
    on a resource (e.g. launching an instance, creating a load balancer) and then using a waiter to wait for the resource
    to enter a given state, you can call a single method in this class to accomplish the same functionality
    """

    def __init__(self, client, **kwargs):
        """
        Creates a new LoadBalancerClientCompositeOperations object

        :param LoadBalancerClient client:
            The service client which will be wrapped by this object
        """
        self.client = client

    def change_load_balancer_compartment_and_wait_for_state(self, load_balancer_id, change_load_balancer_compartment_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.load_balancer.LoadBalancerClient.change_load_balancer_compartment` and waits for the :py:class:`~oci.load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer to move.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param oci.load_balancer.models.ChangeLoadBalancerCompartmentDetails change_load_balancer_compartment_details: (required)
            The configuration details for moving a load balancer to a different compartment.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.load_balancer.models.WorkRequest.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.load_balancer.LoadBalancerClient.change_load_balancer_compartment`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.change_load_balancer_compartment(load_balancer_id, change_load_balancer_compartment_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_backend_and_wait_for_state(self, create_backend_details, load_balancer_id, backend_set_name, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.load_balancer.LoadBalancerClient.create_backend` and waits for the :py:class:`~oci.load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param oci.load_balancer.models.CreateBackendDetails create_backend_details: (required)
            The details to add a backend server to a backend set.

        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer associated with the backend set and servers.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str backend_set_name: (required)
            The name of the backend set to add the backend server to.

            Example: `example_backend_set`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.load_balancer.models.WorkRequest.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.load_balancer.LoadBalancerClient.create_backend`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_backend(create_backend_details, load_balancer_id, backend_set_name, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_backend_set_and_wait_for_state(self, create_backend_set_details, load_balancer_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.load_balancer.LoadBalancerClient.create_backend_set` and waits for the :py:class:`~oci.load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param oci.load_balancer.models.CreateBackendSetDetails create_backend_set_details: (required)
            The details for adding a backend set.

        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer on which to add a backend set.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.load_balancer.models.WorkRequest.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.load_balancer.LoadBalancerClient.create_backend_set`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_backend_set(create_backend_set_details, load_balancer_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_certificate_and_wait_for_state(self, create_certificate_details, load_balancer_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.load_balancer.LoadBalancerClient.create_certificate` and waits for the :py:class:`~oci.load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param oci.load_balancer.models.CreateCertificateDetails create_certificate_details: (required)
            The details of the certificate bundle to add.

        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer on which to add the certificate bundle.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.load_balancer.models.WorkRequest.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.load_balancer.LoadBalancerClient.create_certificate`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_certificate(create_certificate_details, load_balancer_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_hostname_and_wait_for_state(self, create_hostname_details, load_balancer_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.load_balancer.LoadBalancerClient.create_hostname` and waits for the :py:class:`~oci.load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param oci.load_balancer.models.CreateHostnameDetails create_hostname_details: (required)
            The details of the hostname resource to add to the specified load balancer.

        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer to add the hostname to.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.load_balancer.models.WorkRequest.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.load_balancer.LoadBalancerClient.create_hostname`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_hostname(create_hostname_details, load_balancer_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_listener_and_wait_for_state(self, create_listener_details, load_balancer_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.load_balancer.LoadBalancerClient.create_listener` and waits for the :py:class:`~oci.load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param oci.load_balancer.models.CreateListenerDetails create_listener_details: (required)
            Details to add a listener.

        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer on which to add a listener.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.load_balancer.models.WorkRequest.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.load_balancer.LoadBalancerClient.create_listener`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_listener(create_listener_details, load_balancer_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_load_balancer_and_wait_for_state(self, create_load_balancer_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.load_balancer.LoadBalancerClient.create_load_balancer` and waits for the :py:class:`~oci.load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param oci.load_balancer.models.CreateLoadBalancerDetails create_load_balancer_details: (required)
            The configuration details for creating a load balancer.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.load_balancer.models.WorkRequest.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.load_balancer.LoadBalancerClient.create_load_balancer`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_load_balancer(create_load_balancer_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = self.client.get_load_balancer(waiter_result.data.load_balancer_id)

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_path_route_set_and_wait_for_state(self, create_path_route_set_details, load_balancer_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.load_balancer.LoadBalancerClient.create_path_route_set` and waits for the :py:class:`~oci.load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param oci.load_balancer.models.CreatePathRouteSetDetails create_path_route_set_details: (required)
            The details of the path route set to add.

        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer to add the path route set to.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.load_balancer.models.WorkRequest.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.load_balancer.LoadBalancerClient.create_path_route_set`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_path_route_set(create_path_route_set_details, load_balancer_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_rule_set_and_wait_for_state(self, load_balancer_id, create_rule_set_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.load_balancer.LoadBalancerClient.create_rule_set` and waits for the :py:class:`~oci.load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param str load_balancer_id: (required)
            The `OCID`__ of the specified load balancer.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.load_balancer.models.CreateRuleSetDetails create_rule_set_details: (required)
            The configuration details for the rule set to create.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.load_balancer.models.WorkRequest.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.load_balancer.LoadBalancerClient.create_rule_set`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_rule_set(load_balancer_id, create_rule_set_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_ssl_cipher_suite_and_wait_for_state(self, create_ssl_cipher_suite_details, load_balancer_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.load_balancer.LoadBalancerClient.create_ssl_cipher_suite` and waits for the :py:class:`~oci.load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param oci.load_balancer.models.CreateSSLCipherSuiteDetails create_ssl_cipher_suite_details: (required)
            The details of the SSL cipher suite to add.

        :param str load_balancer_id: (required)
            The `OCID`__ of the associated load balancer.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.load_balancer.models.WorkRequest.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.load_balancer.LoadBalancerClient.create_ssl_cipher_suite`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_ssl_cipher_suite(create_ssl_cipher_suite_details, load_balancer_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_backend_and_wait_for_state(self, load_balancer_id, backend_set_name, backend_name, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.load_balancer.LoadBalancerClient.delete_backend` and waits for the :py:class:`~oci.load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer associated with the backend set and server.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str backend_set_name: (required)
            The name of the backend set associated with the backend server.

            Example: `example_backend_set`

        :param str backend_name: (required)
            The IP address and port of the backend server to remove.

            Example: `10.0.0.3:8080`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.load_balancer.models.WorkRequest.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.load_balancer.LoadBalancerClient.delete_backend`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = None
        try:
            operation_result = self.client.delete_backend(load_balancer_id, backend_set_name, backend_name, **operation_kwargs)
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
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_backend_set_and_wait_for_state(self, load_balancer_id, backend_set_name, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.load_balancer.LoadBalancerClient.delete_backend_set` and waits for the :py:class:`~oci.load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer associated with the backend set.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str backend_set_name: (required)
            The name of the backend set to delete.

            Example: `example_backend_set`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.load_balancer.models.WorkRequest.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.load_balancer.LoadBalancerClient.delete_backend_set`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = None
        try:
            operation_result = self.client.delete_backend_set(load_balancer_id, backend_set_name, **operation_kwargs)
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
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_certificate_and_wait_for_state(self, load_balancer_id, certificate_name, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.load_balancer.LoadBalancerClient.delete_certificate` and waits for the :py:class:`~oci.load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer associated with the certificate bundle
            to be deleted.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str certificate_name: (required)
            The name of the certificate bundle to delete.

            Example: `example_certificate_bundle`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.load_balancer.models.WorkRequest.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.load_balancer.LoadBalancerClient.delete_certificate`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = None
        try:
            operation_result = self.client.delete_certificate(load_balancer_id, certificate_name, **operation_kwargs)
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
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_hostname_and_wait_for_state(self, load_balancer_id, name, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.load_balancer.LoadBalancerClient.delete_hostname` and waits for the :py:class:`~oci.load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer associated with the hostname to delete.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str name: (required)
            The name of the hostname resource to delete.

            Example: `example_hostname_001`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.load_balancer.models.WorkRequest.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.load_balancer.LoadBalancerClient.delete_hostname`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = None
        try:
            operation_result = self.client.delete_hostname(load_balancer_id, name, **operation_kwargs)
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
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_listener_and_wait_for_state(self, load_balancer_id, listener_name, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.load_balancer.LoadBalancerClient.delete_listener` and waits for the :py:class:`~oci.load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer associated with the listener to delete.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str listener_name: (required)
            The name of the listener to delete.

            Example: `example_listener`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.load_balancer.models.WorkRequest.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.load_balancer.LoadBalancerClient.delete_listener`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = None
        try:
            operation_result = self.client.delete_listener(load_balancer_id, listener_name, **operation_kwargs)
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
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_load_balancer_and_wait_for_state(self, load_balancer_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.load_balancer.LoadBalancerClient.delete_load_balancer` and waits for the :py:class:`~oci.load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer to delete.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.load_balancer.models.WorkRequest.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.load_balancer.LoadBalancerClient.delete_load_balancer`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = None
        try:
            operation_result = self.client.delete_load_balancer(load_balancer_id, **operation_kwargs)
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
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_path_route_set_and_wait_for_state(self, load_balancer_id, path_route_set_name, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.load_balancer.LoadBalancerClient.delete_path_route_set` and waits for the :py:class:`~oci.load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer associated with the path route set to delete.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str path_route_set_name: (required)
            The name of the path route set to delete.

            Example: `example_path_route_set`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.load_balancer.models.WorkRequest.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.load_balancer.LoadBalancerClient.delete_path_route_set`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = None
        try:
            operation_result = self.client.delete_path_route_set(load_balancer_id, path_route_set_name, **operation_kwargs)
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
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_rule_set_and_wait_for_state(self, load_balancer_id, rule_set_name, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.load_balancer.LoadBalancerClient.delete_rule_set` and waits for the :py:class:`~oci.load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param str load_balancer_id: (required)
            The `OCID`__ of the specified load balancer.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str rule_set_name: (required)
            The name of the rule set to delete.

            Example: `example_rule_set`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.load_balancer.models.WorkRequest.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.load_balancer.LoadBalancerClient.delete_rule_set`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = None
        try:
            operation_result = self.client.delete_rule_set(load_balancer_id, rule_set_name, **operation_kwargs)
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
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_ssl_cipher_suite_and_wait_for_state(self, load_balancer_id, name, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.load_balancer.LoadBalancerClient.delete_ssl_cipher_suite` and waits for the :py:class:`~oci.load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param str load_balancer_id: (required)
            The `OCID`__ of the associated load balancer.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str name: (required)
            The name of the SSL cipher suite to delete.

            example: `example_cipher_suite`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.load_balancer.models.WorkRequest.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.load_balancer.LoadBalancerClient.delete_ssl_cipher_suite`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = None
        try:
            operation_result = self.client.delete_ssl_cipher_suite(load_balancer_id, name, **operation_kwargs)
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
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_backend_and_wait_for_state(self, update_backend_details, load_balancer_id, backend_set_name, backend_name, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.load_balancer.LoadBalancerClient.update_backend` and waits for the :py:class:`~oci.load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param oci.load_balancer.models.UpdateBackendDetails update_backend_details: (required)
            Details for updating a backend server.

        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer associated with the backend set and server.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str backend_set_name: (required)
            The name of the backend set associated with the backend server.

            Example: `example_backend_set`

        :param str backend_name: (required)
            The IP address and port of the backend server to update.

            Example: `10.0.0.3:8080`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.load_balancer.models.WorkRequest.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.load_balancer.LoadBalancerClient.update_backend`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_backend(update_backend_details, load_balancer_id, backend_set_name, backend_name, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_backend_set_and_wait_for_state(self, update_backend_set_details, load_balancer_id, backend_set_name, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.load_balancer.LoadBalancerClient.update_backend_set` and waits for the :py:class:`~oci.load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param oci.load_balancer.models.UpdateBackendSetDetails update_backend_set_details: (required)
            The details to update a backend set.

        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer associated with the backend set.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str backend_set_name: (required)
            The name of the backend set to update.

            Example: `example_backend_set`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.load_balancer.models.WorkRequest.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.load_balancer.LoadBalancerClient.update_backend_set`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_backend_set(update_backend_set_details, load_balancer_id, backend_set_name, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_health_checker_and_wait_for_state(self, health_checker, load_balancer_id, backend_set_name, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.load_balancer.LoadBalancerClient.update_health_checker` and waits for the :py:class:`~oci.load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param oci.load_balancer.models.UpdateHealthCheckerDetails health_checker: (required)
            The health check policy configuration details.

        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer associated with the health check policy to be updated.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str backend_set_name: (required)
            The name of the backend set associated with the health check policy to be retrieved.

            Example: `example_backend_set`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.load_balancer.models.WorkRequest.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.load_balancer.LoadBalancerClient.update_health_checker`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_health_checker(health_checker, load_balancer_id, backend_set_name, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_hostname_and_wait_for_state(self, update_hostname_details, load_balancer_id, name, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.load_balancer.LoadBalancerClient.update_hostname` and waits for the :py:class:`~oci.load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param oci.load_balancer.models.UpdateHostnameDetails update_hostname_details: (required)
            The configuration details to update a virtual hostname.

        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer associated with the virtual hostname
            to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str name: (required)
            The name of the hostname resource to update.

            Example: `example_hostname_001`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.load_balancer.models.WorkRequest.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.load_balancer.LoadBalancerClient.update_hostname`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_hostname(update_hostname_details, load_balancer_id, name, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_listener_and_wait_for_state(self, update_listener_details, load_balancer_id, listener_name, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.load_balancer.LoadBalancerClient.update_listener` and waits for the :py:class:`~oci.load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param oci.load_balancer.models.UpdateListenerDetails update_listener_details: (required)
            Details to update a listener.

        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer associated with the listener to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str listener_name: (required)
            The name of the listener to update.

            Example: `example_listener`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.load_balancer.models.WorkRequest.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.load_balancer.LoadBalancerClient.update_listener`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_listener(update_listener_details, load_balancer_id, listener_name, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_load_balancer_and_wait_for_state(self, update_load_balancer_details, load_balancer_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.load_balancer.LoadBalancerClient.update_load_balancer` and waits for the :py:class:`~oci.load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param oci.load_balancer.models.UpdateLoadBalancerDetails update_load_balancer_details: (required)
            The details for updating a load balancer's configuration.

        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.load_balancer.models.WorkRequest.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.load_balancer.LoadBalancerClient.update_load_balancer`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_load_balancer(update_load_balancer_details, load_balancer_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = self.client.get_load_balancer(waiter_result.data.load_balancer_id)

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_load_balancer_shape_and_wait_for_state(self, load_balancer_id, update_load_balancer_shape_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.load_balancer.LoadBalancerClient.update_load_balancer_shape` and waits for the :py:class:`~oci.load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer whose shape will be updated.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param oci.load_balancer.models.UpdateLoadBalancerShapeDetails update_load_balancer_shape_details: (required)
            The details for updating a load balancer's shape. This contains the new, desired shape.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.load_balancer.models.WorkRequest.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.load_balancer.LoadBalancerClient.update_load_balancer_shape`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_load_balancer_shape(load_balancer_id, update_load_balancer_shape_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_network_security_groups_and_wait_for_state(self, update_network_security_groups_details, load_balancer_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.load_balancer.LoadBalancerClient.update_network_security_groups` and waits for the :py:class:`~oci.load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param oci.load_balancer.models.UpdateNetworkSecurityGroupsDetails update_network_security_groups_details: (required)
            The details for updating the NSGs associated with the specified load balancer.

        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer to update the NSGs for.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.load_balancer.models.WorkRequest.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.load_balancer.LoadBalancerClient.update_network_security_groups`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_network_security_groups(update_network_security_groups_details, load_balancer_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_path_route_set_and_wait_for_state(self, update_path_route_set_details, load_balancer_id, path_route_set_name, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.load_balancer.LoadBalancerClient.update_path_route_set` and waits for the :py:class:`~oci.load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param oci.load_balancer.models.UpdatePathRouteSetDetails update_path_route_set_details: (required)
            The configuration details to update a path route set.

        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer associated with the path route set to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str path_route_set_name: (required)
            The name of the path route set to update.

            Example: `example_path_route_set`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.load_balancer.models.WorkRequest.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.load_balancer.LoadBalancerClient.update_path_route_set`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_path_route_set(update_path_route_set_details, load_balancer_id, path_route_set_name, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_rule_set_and_wait_for_state(self, load_balancer_id, rule_set_name, update_rule_set_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.load_balancer.LoadBalancerClient.update_rule_set` and waits for the :py:class:`~oci.load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param str load_balancer_id: (required)
            The `OCID`__ of the specified load balancer.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str rule_set_name: (required)
            The name of the rule set to update.

            Example: `example_rule_set`

        :param oci.load_balancer.models.UpdateRuleSetDetails update_rule_set_details: (required)
            The configuration details to update a set of rules.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.load_balancer.models.WorkRequest.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.load_balancer.LoadBalancerClient.update_rule_set`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_rule_set(load_balancer_id, rule_set_name, update_rule_set_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_ssl_cipher_suite_and_wait_for_state(self, update_ssl_cipher_suite_details, load_balancer_id, name, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.load_balancer.LoadBalancerClient.update_ssl_cipher_suite` and waits for the :py:class:`~oci.load_balancer.models.WorkRequest`
        to enter the given state(s).

        :param oci.load_balancer.models.UpdateSSLCipherSuiteDetails update_ssl_cipher_suite_details: (required)
            The configuration details to update an SSL cipher suite.

        :param str load_balancer_id: (required)
            The `OCID`__ of the associated load balancer.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str name: (required)
            The name of the SSL cipher suite to update.

            example: `example_cipher_suite`

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.load_balancer.models.WorkRequest.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.load_balancer.LoadBalancerClient.update_ssl_cipher_suite`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_ssl_cipher_suite(update_ssl_cipher_suite_details, load_balancer_id, name, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
