# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci  # noqa: F401
from oci.util import WAIT_RESOURCE_NOT_FOUND  # noqa: F401


class DashboardClientCompositeOperations(object):
    """
    This class provides a wrapper around :py:class:`~oci.dashboard_service.DashboardClient` and offers convenience methods
    for operations that would otherwise need to be chained together. For example, instead of performing an action
    on a resource (e.g. launching an instance, creating a load balancer) and then using a waiter to wait for the resource
    to enter a given state, you can call a single method in this class to accomplish the same functionality
    """

    def __init__(self, client, **kwargs):
        """
        Creates a new DashboardClientCompositeOperations object

        :param DashboardClient client:
            The service client which will be wrapped by this object
        """
        self.client = client

    def create_dashboard_and_wait_for_state(self, create_dashboard_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.dashboard_service.DashboardClient.create_dashboard` and waits for the :py:class:`~oci.dashboard_service.models.Dashboard` acted upon
        to enter the given state(s).

        :param oci.dashboard_service.models.CreateDashboardDetails create_dashboard_details: (required)
            Details about the dashboard being created.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.dashboard_service.models.Dashboard.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.dashboard_service.DashboardClient.create_dashboard`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_dashboard(create_dashboard_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        dashboard_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_dashboard(dashboard_id),  # noqa: F821
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

    def delete_dashboard_and_wait_for_state(self, dashboard_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.dashboard_service.DashboardClient.delete_dashboard` and waits for the :py:class:`~oci.dashboard_service.models.Dashboard` acted upon
        to enter the given state(s).

        :param str dashboard_id: (required)
            The `OCID`__ of the dashboard.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.dashboard_service.models.Dashboard.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.dashboard_service.DashboardClient.delete_dashboard`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_dashboard(dashboard_id)
        operation_result = None
        try:
            operation_result = self.client.delete_dashboard(dashboard_id, **operation_kwargs)
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

    def update_dashboard_and_wait_for_state(self, dashboard_id, update_dashboard_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.dashboard_service.DashboardClient.update_dashboard` and waits for the :py:class:`~oci.dashboard_service.models.Dashboard` acted upon
        to enter the given state(s).

        :param str dashboard_id: (required)
            The `OCID`__ of the dashboard.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param oci.dashboard_service.models.UpdateDashboardDetails update_dashboard_details: (required)
            The dashboard details to be updated.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.dashboard_service.models.Dashboard.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.dashboard_service.DashboardClient.update_dashboard`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_dashboard(dashboard_id, update_dashboard_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        dashboard_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_dashboard(dashboard_id),  # noqa: F821
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
