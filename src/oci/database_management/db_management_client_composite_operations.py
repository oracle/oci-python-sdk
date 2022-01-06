# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci  # noqa: F401
from oci.util import WAIT_RESOURCE_NOT_FOUND  # noqa: F401


class DbManagementClientCompositeOperations(object):
    """
    This class provides a wrapper around :py:class:`~oci.database_management.DbManagementClient` and offers convenience methods
    for operations that would otherwise need to be chained together. For example, instead of performing an action
    on a resource (e.g. launching an instance, creating a load balancer) and then using a waiter to wait for the resource
    to enter a given state, you can call a single method in this class to accomplish the same functionality
    """

    def __init__(self, client, **kwargs):
        """
        Creates a new DbManagementClientCompositeOperations object

        :param DbManagementClient client:
            The service client which will be wrapped by this object
        """
        self.client = client

    def create_db_management_private_endpoint_and_wait_for_state(self, create_db_management_private_endpoint_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database_management.DbManagementClient.create_db_management_private_endpoint` and waits for the :py:class:`~oci.database_management.models.WorkRequest`
        to enter the given state(s).

        :param oci.database_management.models.CreateDbManagementPrivateEndpointDetails create_db_management_private_endpoint_details: (required)
            Details used to create a new Database Management private endpoint.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database_management.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database_management.DbManagementClient.create_db_management_private_endpoint`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_db_management_private_endpoint(create_db_management_private_endpoint_details, **operation_kwargs)
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

    def create_job_and_wait_for_state(self, create_job_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database_management.DbManagementClient.create_job` and waits for the :py:class:`~oci.database_management.models.Job` acted upon
        to enter the given state(s).

        :param oci.database_management.models.CreateJobDetails create_job_details: (required)
            The details required to create a job.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database_management.models.Job.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database_management.DbManagementClient.create_job`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_job(create_job_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_job(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_managed_database_group_and_wait_for_state(self, create_managed_database_group_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database_management.DbManagementClient.create_managed_database_group` and waits for the :py:class:`~oci.database_management.models.ManagedDatabaseGroup` acted upon
        to enter the given state(s).

        :param oci.database_management.models.CreateManagedDatabaseGroupDetails create_managed_database_group_details: (required)
            The details required to create a Managed Database Group.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database_management.models.ManagedDatabaseGroup.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database_management.DbManagementClient.create_managed_database_group`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_managed_database_group(create_managed_database_group_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_managed_database_group(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_db_management_private_endpoint_and_wait_for_state(self, db_management_private_endpoint_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database_management.DbManagementClient.delete_db_management_private_endpoint` and waits for the :py:class:`~oci.database_management.models.WorkRequest`
        to enter the given state(s).

        :param str db_management_private_endpoint_id: (required)
            The `OCID`__ of the Database Management private endpoint.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database_management.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database_management.DbManagementClient.delete_db_management_private_endpoint`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = None
        try:
            operation_result = self.client.delete_db_management_private_endpoint(db_management_private_endpoint_id, **operation_kwargs)
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

    def delete_job_and_wait_for_state(self, job_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database_management.DbManagementClient.delete_job` and waits for the :py:class:`~oci.database_management.models.Job` acted upon
        to enter the given state(s).

        :param str job_id: (required)
            The identifier of the job.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database_management.models.Job.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database_management.DbManagementClient.delete_job`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_job(job_id)
        operation_result = None
        try:
            operation_result = self.client.delete_job(job_id, **operation_kwargs)
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

    def delete_managed_database_group_and_wait_for_state(self, managed_database_group_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database_management.DbManagementClient.delete_managed_database_group` and waits for the :py:class:`~oci.database_management.models.ManagedDatabaseGroup` acted upon
        to enter the given state(s).

        :param str managed_database_group_id: (required)
            The `OCID`__ of the Managed Database Group.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database_management.models.ManagedDatabaseGroup.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database_management.DbManagementClient.delete_managed_database_group`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_managed_database_group(managed_database_group_id)
        operation_result = None
        try:
            operation_result = self.client.delete_managed_database_group(managed_database_group_id, **operation_kwargs)
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

    def update_db_management_private_endpoint_and_wait_for_state(self, db_management_private_endpoint_id, update_db_management_private_endpoint_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database_management.DbManagementClient.update_db_management_private_endpoint` and waits for the :py:class:`~oci.database_management.models.DbManagementPrivateEndpoint` acted upon
        to enter the given state(s).

        :param str db_management_private_endpoint_id: (required)
            The `OCID`__ of the Database Management private endpoint.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.database_management.models.UpdateDbManagementPrivateEndpointDetails update_db_management_private_endpoint_details: (required)
            The details used to update a Database Management private endpoint.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database_management.models.DbManagementPrivateEndpoint.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database_management.DbManagementClient.update_db_management_private_endpoint`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_db_management_private_endpoint(db_management_private_endpoint_id, update_db_management_private_endpoint_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_db_management_private_endpoint(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_job_and_wait_for_state(self, job_id, update_job_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database_management.DbManagementClient.update_job` and waits for the :py:class:`~oci.database_management.models.Job` acted upon
        to enter the given state(s).

        :param str job_id: (required)
            The identifier of the job.

        :param oci.database_management.models.UpdateJobDetails update_job_details: (required)
            The details required to update a job.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database_management.models.Job.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database_management.DbManagementClient.update_job`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_job(job_id, update_job_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_job(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_managed_database_group_and_wait_for_state(self, managed_database_group_id, update_managed_database_group_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database_management.DbManagementClient.update_managed_database_group` and waits for the :py:class:`~oci.database_management.models.ManagedDatabaseGroup` acted upon
        to enter the given state(s).

        :param str managed_database_group_id: (required)
            The `OCID`__ of the Managed Database Group.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.database_management.models.UpdateManagedDatabaseGroupDetails update_managed_database_group_details: (required)
            The details required to update a Managed Database Group.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database_management.models.ManagedDatabaseGroup.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database_management.DbManagementClient.update_managed_database_group`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_managed_database_group(managed_database_group_id, update_managed_database_group_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_managed_database_group(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
