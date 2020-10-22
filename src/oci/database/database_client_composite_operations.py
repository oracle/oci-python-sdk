# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci  # noqa: F401
from oci.util import WAIT_RESOURCE_NOT_FOUND  # noqa: F401


class DatabaseClientCompositeOperations(object):
    """
    This class provides a wrapper around :py:class:`~oci.database.DatabaseClient` and offers convenience methods
    for operations that would otherwise need to be chained together. For example, instead of performing an action
    on a resource (e.g. launching an instance, creating a load balancer) and then using a waiter to wait for the resource
    to enter a given state, you can call a single method in this class to accomplish the same functionality
    """

    def __init__(self, client, work_request_client=None, **kwargs):
        """
        Creates a new DatabaseClientCompositeOperations object

        :param DatabaseClient client:
            The service client which will be wrapped by this object

        :param oci.work_requests.WorkRequestClient work_request_client: (optional)
            The work request service client which will be used to wait for work request states. Default is None.
        """
        self.client = client
        self._work_request_client = work_request_client if work_request_client else oci.work_requests.WorkRequestClient(self.client._config, **self.client._kwargs)

    def activate_exadata_infrastructure_and_wait_for_work_request(self, exadata_infrastructure_id, activate_exadata_infrastructure_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.activate_exadata_infrastructure` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str exadata_infrastructure_id: (required)
            The Exadata infrastructure `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param ActivateExadataInfrastructureDetails activate_exadata_infrastructure_details: (required)
            The activation details for the Exadata infrastructure.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.activate_exadata_infrastructure`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.activate_exadata_infrastructure(exadata_infrastructure_id, activate_exadata_infrastructure_details, **operation_kwargs)
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

    def activate_exadata_infrastructure_and_wait_for_state(self, exadata_infrastructure_id, activate_exadata_infrastructure_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.activate_exadata_infrastructure` and waits for the :py:class:`~oci.database.models.ExadataInfrastructure` acted upon
        to enter the given state(s).

        :param str exadata_infrastructure_id: (required)
            The Exadata infrastructure `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param ActivateExadataInfrastructureDetails activate_exadata_infrastructure_details: (required)
            The activation details for the Exadata infrastructure.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.ExadataInfrastructure.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.activate_exadata_infrastructure`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.activate_exadata_infrastructure(exadata_infrastructure_id, activate_exadata_infrastructure_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_exadata_infrastructure(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def autonomous_database_manual_refresh_and_wait_for_work_request(self, autonomous_database_id, autonomous_database_manual_refresh_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.autonomous_database_manual_refresh` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str autonomous_database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param AutonomousDatabaseManualRefreshDetails autonomous_database_manual_refresh_details: (required)
            Request details for manually refreshing an Autonomous Database refreshable clone.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.autonomous_database_manual_refresh`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.autonomous_database_manual_refresh(autonomous_database_id, autonomous_database_manual_refresh_details, **operation_kwargs)
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

    def autonomous_database_manual_refresh_and_wait_for_state(self, autonomous_database_id, autonomous_database_manual_refresh_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.autonomous_database_manual_refresh` and waits for the :py:class:`~oci.database.models.AutonomousDatabase` acted upon
        to enter the given state(s).

        :param str autonomous_database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param AutonomousDatabaseManualRefreshDetails autonomous_database_manual_refresh_details: (required)
            Request details for manually refreshing an Autonomous Database refreshable clone.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.AutonomousDatabase.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.autonomous_database_manual_refresh`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.autonomous_database_manual_refresh(autonomous_database_id, autonomous_database_manual_refresh_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_autonomous_database(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def change_autonomous_container_database_compartment_and_wait_for_work_request(self, change_compartment_details, autonomous_container_database_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.change_autonomous_container_database_compartment` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param ChangeCompartmentDetails change_compartment_details: (required)
            Request to move Autonomous Container Database to a different compartment

        :param str autonomous_container_database_id: (required)
            The Autonomous Container Database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.change_autonomous_container_database_compartment`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.change_autonomous_container_database_compartment(change_compartment_details, autonomous_container_database_id, **operation_kwargs)
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

    def change_autonomous_database_compartment_and_wait_for_work_request(self, change_compartment_details, autonomous_database_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.change_autonomous_database_compartment` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param ChangeCompartmentDetails change_compartment_details: (required)
            Request to move Autonomous Database to a different compartment

        :param str autonomous_database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.change_autonomous_database_compartment`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.change_autonomous_database_compartment(change_compartment_details, autonomous_database_id, **operation_kwargs)
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

    def change_autonomous_exadata_infrastructure_compartment_and_wait_for_work_request(self, change_compartment_details, autonomous_exadata_infrastructure_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.change_autonomous_exadata_infrastructure_compartment` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param ChangeCompartmentDetails change_compartment_details: (required)
            Request to move an Autonomous Exadata Infrastructure resource to a different compartment.

        :param str autonomous_exadata_infrastructure_id: (required)
            The Autonomous Exadata Infrastructure  `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.change_autonomous_exadata_infrastructure_compartment`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.change_autonomous_exadata_infrastructure_compartment(change_compartment_details, autonomous_exadata_infrastructure_id, **operation_kwargs)
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

    def change_autonomous_vm_cluster_compartment_and_wait_for_work_request(self, change_autonomous_vm_cluster_compartment_details, autonomous_vm_cluster_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.change_autonomous_vm_cluster_compartment` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param ChangeAutonomousVmClusterCompartmentDetails change_autonomous_vm_cluster_compartment_details: (required)
            Request to move Autonomous VM cluster to a different compartment

        :param str autonomous_vm_cluster_id: (required)
            The autonomous VM cluster `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.change_autonomous_vm_cluster_compartment`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.change_autonomous_vm_cluster_compartment(change_autonomous_vm_cluster_compartment_details, autonomous_vm_cluster_id, **operation_kwargs)
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

    def change_backup_destination_compartment_and_wait_for_work_request(self, change_compartment_details, backup_destination_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.change_backup_destination_compartment` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param ChangeCompartmentDetails change_compartment_details: (required)
            Request to move backup destination to a different compartment.

        :param str backup_destination_id: (required)
            The `OCID`__ of the backup destination.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.change_backup_destination_compartment`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.change_backup_destination_compartment(change_compartment_details, backup_destination_id, **operation_kwargs)
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

    def change_cloud_exadata_infrastructure_compartment_and_wait_for_work_request(self, change_cloud_exadata_infrastructure_compartment_details, cloud_exadata_infrastructure_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.change_cloud_exadata_infrastructure_compartment` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param ChangeCloudExadataInfrastructureCompartmentDetails change_cloud_exadata_infrastructure_compartment_details: (required)
            Request to move cloud Exadata infrastructure resource to a different compartment.

        :param str cloud_exadata_infrastructure_id: (required)
            The cloud Exadata infrastructure `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.change_cloud_exadata_infrastructure_compartment`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.change_cloud_exadata_infrastructure_compartment(change_cloud_exadata_infrastructure_compartment_details, cloud_exadata_infrastructure_id, **operation_kwargs)
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

    def change_cloud_vm_cluster_compartment_and_wait_for_work_request(self, change_cloud_vm_cluster_compartment_details, cloud_vm_cluster_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.change_cloud_vm_cluster_compartment` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param ChangeCloudVmClusterCompartmentDetails change_cloud_vm_cluster_compartment_details: (required)
            Request to move cloud VM cluster to a different compartment

        :param str cloud_vm_cluster_id: (required)
            The cloud VM cluster `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.change_cloud_vm_cluster_compartment`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.change_cloud_vm_cluster_compartment(change_cloud_vm_cluster_compartment_details, cloud_vm_cluster_id, **operation_kwargs)
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

    def change_database_software_image_compartment_and_wait_for_work_request(self, change_compartment_details, database_software_image_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.change_database_software_image_compartment` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param ChangeCompartmentDetails change_compartment_details: (required)
            Request to move Database Software Image to a different compartment

        :param str database_software_image_id: (required)
            The DB system `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.change_database_software_image_compartment`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.change_database_software_image_compartment(change_compartment_details, database_software_image_id, **operation_kwargs)
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

    def change_db_system_compartment_and_wait_for_work_request(self, change_compartment_details, db_system_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.change_db_system_compartment` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param ChangeCompartmentDetails change_compartment_details: (required)
            Request to move the DB system to a different compartment.

        :param str db_system_id: (required)
            The DB system `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.change_db_system_compartment`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.change_db_system_compartment(change_compartment_details, db_system_id, **operation_kwargs)
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

    def change_exadata_infrastructure_compartment_and_wait_for_work_request(self, change_exadata_infrastructure_compartment_details, exadata_infrastructure_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.change_exadata_infrastructure_compartment` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param ChangeExadataInfrastructureCompartmentDetails change_exadata_infrastructure_compartment_details: (required)
            Request to move Exadata infrastructure to a different compartment

        :param str exadata_infrastructure_id: (required)
            The Exadata infrastructure `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.change_exadata_infrastructure_compartment`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.change_exadata_infrastructure_compartment(change_exadata_infrastructure_compartment_details, exadata_infrastructure_id, **operation_kwargs)
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

    def change_key_store_compartment_and_wait_for_work_request(self, change_key_store_compartment_details, key_store_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.change_key_store_compartment` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param ChangeKeyStoreCompartmentDetails change_key_store_compartment_details: (required)
            Request to move key store to a different compartment

        :param str key_store_id: (required)
            The `OCID`__ of the key store.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.change_key_store_compartment`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.change_key_store_compartment(change_key_store_compartment_details, key_store_id, **operation_kwargs)
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

    def change_vm_cluster_compartment_and_wait_for_work_request(self, change_vm_cluster_compartment_details, vm_cluster_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.change_vm_cluster_compartment` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param ChangeVmClusterCompartmentDetails change_vm_cluster_compartment_details: (required)
            Request to move the Exadata Cloud@Customer VM cluster to a different compartment.

        :param str vm_cluster_id: (required)
            The VM cluster `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.change_vm_cluster_compartment`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.change_vm_cluster_compartment(change_vm_cluster_compartment_details, vm_cluster_id, **operation_kwargs)
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

    def complete_external_backup_job_and_wait_for_work_request(self, backup_id, complete_external_backup_job_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.complete_external_backup_job` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str backup_id: (required)
            The backup `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param CompleteExternalBackupJobDetails complete_external_backup_job_details: (required)
            Updates the status of the backup resource.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.complete_external_backup_job`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.complete_external_backup_job(backup_id, complete_external_backup_job_details, **operation_kwargs)
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

    def create_autonomous_container_database_and_wait_for_work_request(self, create_autonomous_container_database_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.create_autonomous_container_database` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param CreateAutonomousContainerDatabaseDetails create_autonomous_container_database_details: (required)
            Request to create an Autonomous Container Database in a specified Autonomous Exadata Infrastructure.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.create_autonomous_container_database`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_autonomous_container_database(create_autonomous_container_database_details, **operation_kwargs)
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

    def create_autonomous_container_database_and_wait_for_state(self, create_autonomous_container_database_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.create_autonomous_container_database` and waits for the :py:class:`~oci.database.models.AutonomousContainerDatabase` acted upon
        to enter the given state(s).

        :param CreateAutonomousContainerDatabaseDetails create_autonomous_container_database_details: (required)
            Request to create an Autonomous Container Database in a specified Autonomous Exadata Infrastructure.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.AutonomousContainerDatabase.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.create_autonomous_container_database`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_autonomous_container_database(create_autonomous_container_database_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_autonomous_container_database(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_autonomous_data_warehouse_and_wait_for_state(self, create_autonomous_data_warehouse_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.create_autonomous_data_warehouse` and waits for the :py:class:`~oci.database.models.AutonomousDataWarehouse` acted upon
        to enter the given state(s).

        :param CreateAutonomousDataWarehouseDetails create_autonomous_data_warehouse_details: (required)
            Request to create a new Autonomous Data Warehouse.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.AutonomousDataWarehouse.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.create_autonomous_data_warehouse`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_autonomous_data_warehouse(create_autonomous_data_warehouse_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_autonomous_data_warehouse(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_autonomous_data_warehouse_backup_and_wait_for_state(self, create_autonomous_data_warehouse_backup_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.create_autonomous_data_warehouse_backup` and waits for the :py:class:`~oci.database.models.AutonomousDataWarehouseBackup` acted upon
        to enter the given state(s).

        :param CreateAutonomousDataWarehouseBackupDetails create_autonomous_data_warehouse_backup_details: (required)
            Request to create a new Autonomous Data Warehouse backup.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.AutonomousDataWarehouseBackup.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.create_autonomous_data_warehouse_backup`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_autonomous_data_warehouse_backup(create_autonomous_data_warehouse_backup_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_autonomous_data_warehouse_backup(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_autonomous_database_and_wait_for_work_request(self, create_autonomous_database_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.create_autonomous_database` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param CreateAutonomousDatabaseBase create_autonomous_database_details: (required)
            Request to create a new Autonomous Database.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.create_autonomous_database`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_autonomous_database(create_autonomous_database_details, **operation_kwargs)
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

    def create_autonomous_database_and_wait_for_state(self, create_autonomous_database_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.create_autonomous_database` and waits for the :py:class:`~oci.database.models.AutonomousDatabase` acted upon
        to enter the given state(s).

        :param CreateAutonomousDatabaseBase create_autonomous_database_details: (required)
            Request to create a new Autonomous Database.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.AutonomousDatabase.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.create_autonomous_database`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_autonomous_database(create_autonomous_database_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_autonomous_database(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_autonomous_database_backup_and_wait_for_work_request(self, create_autonomous_database_backup_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.create_autonomous_database_backup` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param CreateAutonomousDatabaseBackupDetails create_autonomous_database_backup_details: (required)
            Request to create a new Autonomous Database backup.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.create_autonomous_database_backup`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_autonomous_database_backup(create_autonomous_database_backup_details, **operation_kwargs)
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

    def create_autonomous_database_backup_and_wait_for_state(self, create_autonomous_database_backup_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.create_autonomous_database_backup` and waits for the :py:class:`~oci.database.models.AutonomousDatabaseBackup` acted upon
        to enter the given state(s).

        :param CreateAutonomousDatabaseBackupDetails create_autonomous_database_backup_details: (required)
            Request to create a new Autonomous Database backup.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.AutonomousDatabaseBackup.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.create_autonomous_database_backup`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_autonomous_database_backup(create_autonomous_database_backup_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_autonomous_database_backup(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_autonomous_vm_cluster_and_wait_for_work_request(self, create_autonomous_vm_cluster_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.create_autonomous_vm_cluster` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param CreateAutonomousVmClusterDetails create_autonomous_vm_cluster_details: (required)
            Request to create an Autonomous VM cluster.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.create_autonomous_vm_cluster`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_autonomous_vm_cluster(create_autonomous_vm_cluster_details, **operation_kwargs)
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

    def create_autonomous_vm_cluster_and_wait_for_state(self, create_autonomous_vm_cluster_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.create_autonomous_vm_cluster` and waits for the :py:class:`~oci.database.models.AutonomousVmCluster` acted upon
        to enter the given state(s).

        :param CreateAutonomousVmClusterDetails create_autonomous_vm_cluster_details: (required)
            Request to create an Autonomous VM cluster.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.AutonomousVmCluster.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.create_autonomous_vm_cluster`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_autonomous_vm_cluster(create_autonomous_vm_cluster_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_autonomous_vm_cluster(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_backup_and_wait_for_work_request(self, create_backup_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.create_backup` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param CreateBackupDetails create_backup_details: (required)
            Request to create a new database backup.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.create_backup`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_backup(create_backup_details, **operation_kwargs)
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

    def create_backup_and_wait_for_state(self, create_backup_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.create_backup` and waits for the :py:class:`~oci.database.models.Backup` acted upon
        to enter the given state(s).

        :param CreateBackupDetails create_backup_details: (required)
            Request to create a new database backup.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.Backup.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.create_backup`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_backup(create_backup_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_backup(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_backup_destination_and_wait_for_state(self, create_backup_destination_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.create_backup_destination` and waits for the :py:class:`~oci.database.models.BackupDestination` acted upon
        to enter the given state(s).

        :param CreateBackupDestinationDetails create_backup_destination_details: (required)
            Request to create a new backup destination.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.BackupDestination.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.create_backup_destination`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_backup_destination(create_backup_destination_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_backup_destination(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_cloud_exadata_infrastructure_and_wait_for_work_request(self, create_cloud_exadata_infrastructure_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.create_cloud_exadata_infrastructure` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param CreateCloudExadataInfrastructureDetails create_cloud_exadata_infrastructure_details: (required)
            Request to create cloud Exadata infrastructure.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.create_cloud_exadata_infrastructure`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_cloud_exadata_infrastructure(create_cloud_exadata_infrastructure_details, **operation_kwargs)
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

    def create_cloud_exadata_infrastructure_and_wait_for_state(self, create_cloud_exadata_infrastructure_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.create_cloud_exadata_infrastructure` and waits for the :py:class:`~oci.database.models.CloudExadataInfrastructure` acted upon
        to enter the given state(s).

        :param CreateCloudExadataInfrastructureDetails create_cloud_exadata_infrastructure_details: (required)
            Request to create cloud Exadata infrastructure.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.CloudExadataInfrastructure.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.create_cloud_exadata_infrastructure`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_cloud_exadata_infrastructure(create_cloud_exadata_infrastructure_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_cloud_exadata_infrastructure(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_cloud_vm_cluster_and_wait_for_work_request(self, create_cloud_vm_cluster_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.create_cloud_vm_cluster` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param CreateCloudVmClusterDetails create_cloud_vm_cluster_details: (required)
            Request to create a cloud VM cluster.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.create_cloud_vm_cluster`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_cloud_vm_cluster(create_cloud_vm_cluster_details, **operation_kwargs)
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

    def create_cloud_vm_cluster_and_wait_for_state(self, create_cloud_vm_cluster_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.create_cloud_vm_cluster` and waits for the :py:class:`~oci.database.models.CloudVmCluster` acted upon
        to enter the given state(s).

        :param CreateCloudVmClusterDetails create_cloud_vm_cluster_details: (required)
            Request to create a cloud VM cluster.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.CloudVmCluster.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.create_cloud_vm_cluster`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_cloud_vm_cluster(create_cloud_vm_cluster_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_cloud_vm_cluster(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_console_connection_and_wait_for_state(self, create_console_connection_details, db_node_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.create_console_connection` and waits for the :py:class:`~oci.database.models.ConsoleConnection` acted upon
        to enter the given state(s).

        :param CreateConsoleConnectionDetails create_console_connection_details: (required)
            Request object for creating an CreateConsoleConnection

        :param str db_node_id: (required)
            The database node `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.ConsoleConnection.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.create_console_connection`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_console_connection(create_console_connection_details, db_node_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_console_connection(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_data_guard_association_and_wait_for_work_request(self, database_id, create_data_guard_association_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.create_data_guard_association` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param CreateDataGuardAssociationDetails create_data_guard_association_details: (required)
            A request to create a Data Guard association.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.create_data_guard_association`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_data_guard_association(database_id, create_data_guard_association_details, **operation_kwargs)
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

    def create_data_guard_association_and_wait_for_state(self, database_id, create_data_guard_association_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.create_data_guard_association` and waits for the :py:class:`~oci.database.models.DataGuardAssociation` acted upon
        to enter the given state(s).

        :param str database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param CreateDataGuardAssociationDetails create_data_guard_association_details: (required)
            A request to create a Data Guard association.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.DataGuardAssociation.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.create_data_guard_association`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_data_guard_association(database_id, create_data_guard_association_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_data_guard_association(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_database_and_wait_for_work_request(self, create_new_database_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.create_database` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param CreateDatabaseBase create_new_database_details: (required)
            Request to create a new database.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.create_database`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_database(create_new_database_details, **operation_kwargs)
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

    def create_database_and_wait_for_state(self, create_new_database_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.create_database` and waits for the :py:class:`~oci.database.models.Database` acted upon
        to enter the given state(s).

        :param CreateDatabaseBase create_new_database_details: (required)
            Request to create a new database.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.Database.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.create_database`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_database(create_new_database_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_database(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_database_software_image_and_wait_for_work_request(self, create_database_software_image_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.create_database_software_image` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param CreateDatabaseSoftwareImageDetails create_database_software_image_details: (required)
            Request to create database software image.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.create_database_software_image`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_database_software_image(create_database_software_image_details, **operation_kwargs)
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

    def create_database_software_image_and_wait_for_state(self, create_database_software_image_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.create_database_software_image` and waits for the :py:class:`~oci.database.models.DatabaseSoftwareImage` acted upon
        to enter the given state(s).

        :param CreateDatabaseSoftwareImageDetails create_database_software_image_details: (required)
            Request to create database software image.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.DatabaseSoftwareImage.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.create_database_software_image`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_database_software_image(create_database_software_image_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_database_software_image(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_db_home_and_wait_for_work_request(self, create_db_home_with_db_system_id_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.create_db_home` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param CreateDbHomeBase create_db_home_with_db_system_id_details: (required)
            Request to create a new Database Home.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.create_db_home`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_db_home(create_db_home_with_db_system_id_details, **operation_kwargs)
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

    def create_db_home_and_wait_for_state(self, create_db_home_with_db_system_id_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.create_db_home` and waits for the :py:class:`~oci.database.models.DbHome` acted upon
        to enter the given state(s).

        :param CreateDbHomeBase create_db_home_with_db_system_id_details: (required)
            Request to create a new Database Home.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.DbHome.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.create_db_home`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_db_home(create_db_home_with_db_system_id_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_db_home(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_exadata_infrastructure_and_wait_for_work_request(self, create_exadata_infrastructure_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.create_exadata_infrastructure` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param CreateExadataInfrastructureDetails create_exadata_infrastructure_details: (required)
            Request to create Exadata Cloud@Customer infrastructure.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.create_exadata_infrastructure`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_exadata_infrastructure(create_exadata_infrastructure_details, **operation_kwargs)
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

    def create_exadata_infrastructure_and_wait_for_state(self, create_exadata_infrastructure_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.create_exadata_infrastructure` and waits for the :py:class:`~oci.database.models.ExadataInfrastructure` acted upon
        to enter the given state(s).

        :param CreateExadataInfrastructureDetails create_exadata_infrastructure_details: (required)
            Request to create Exadata Cloud@Customer infrastructure.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.ExadataInfrastructure.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.create_exadata_infrastructure`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_exadata_infrastructure(create_exadata_infrastructure_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_exadata_infrastructure(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_external_backup_job_and_wait_for_work_request(self, create_external_backup_job_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.create_external_backup_job` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param CreateExternalBackupJobDetails create_external_backup_job_details: (required)
            Request to create a cloud backup resource for a database running outside the cloud.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.create_external_backup_job`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_external_backup_job(create_external_backup_job_details, **operation_kwargs)
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

    def create_key_store_and_wait_for_state(self, create_key_store_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.create_key_store` and waits for the :py:class:`~oci.database.models.KeyStore` acted upon
        to enter the given state(s).

        :param CreateKeyStoreDetails create_key_store_details: (required)
            Request to create a new key store.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.KeyStore.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.create_key_store`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_key_store(create_key_store_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_key_store(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_vm_cluster_and_wait_for_work_request(self, create_vm_cluster_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.create_vm_cluster` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param CreateVmClusterDetails create_vm_cluster_details: (required)
            Request to create an Exadata Cloud@Customer VM cluster.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.create_vm_cluster`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_vm_cluster(create_vm_cluster_details, **operation_kwargs)
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

    def create_vm_cluster_and_wait_for_state(self, create_vm_cluster_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.create_vm_cluster` and waits for the :py:class:`~oci.database.models.VmCluster` acted upon
        to enter the given state(s).

        :param CreateVmClusterDetails create_vm_cluster_details: (required)
            Request to create an Exadata Cloud@Customer VM cluster.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.VmCluster.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.create_vm_cluster`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_vm_cluster(create_vm_cluster_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_vm_cluster(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_vm_cluster_network_and_wait_for_work_request(self, exadata_infrastructure_id, vm_cluster_network_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.create_vm_cluster_network` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str exadata_infrastructure_id: (required)
            The Exadata infrastructure `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param VmClusterNetworkDetails vm_cluster_network_details: (required)
            Request to create the Cloud@Customer VM cluster network.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.create_vm_cluster_network`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_vm_cluster_network(exadata_infrastructure_id, vm_cluster_network_details, **operation_kwargs)
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

    def create_vm_cluster_network_and_wait_for_state(self, exadata_infrastructure_id, vm_cluster_network_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.create_vm_cluster_network` and waits for the :py:class:`~oci.database.models.VmClusterNetwork` acted upon
        to enter the given state(s).

        :param str exadata_infrastructure_id: (required)
            The Exadata infrastructure `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param VmClusterNetworkDetails vm_cluster_network_details: (required)
            Request to create the Cloud@Customer VM cluster network.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.VmClusterNetwork.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.create_vm_cluster_network`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_vm_cluster_network(exadata_infrastructure_id, vm_cluster_network_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_vm_cluster_network(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def db_node_action_and_wait_for_work_request(self, db_node_id, action, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.db_node_action` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str db_node_id: (required)
            The database node `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str action: (required)
            The action to perform on the DB Node.

            Allowed values are: "STOP", "START", "SOFTRESET", "RESET"

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.db_node_action`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.db_node_action(db_node_id, action, **operation_kwargs)
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

    def db_node_action_and_wait_for_state(self, db_node_id, action, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.db_node_action` and waits for the :py:class:`~oci.database.models.DbNode` acted upon
        to enter the given state(s).

        :param str db_node_id: (required)
            The database node `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str action: (required)
            The action to perform on the DB Node.

            Allowed values are: "STOP", "START", "SOFTRESET", "RESET"

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.DbNode.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.db_node_action`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.db_node_action(db_node_id, action, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_db_node(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_autonomous_data_warehouse_and_wait_for_state(self, autonomous_data_warehouse_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.delete_autonomous_data_warehouse` and waits for the :py:class:`~oci.database.models.AutonomousDataWarehouse` acted upon
        to enter the given state(s).

        :param str autonomous_data_warehouse_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.AutonomousDataWarehouse.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.delete_autonomous_data_warehouse`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_autonomous_data_warehouse(autonomous_data_warehouse_id)
        operation_result = None
        try:
            operation_result = self.client.delete_autonomous_data_warehouse(autonomous_data_warehouse_id, **operation_kwargs)
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

    def delete_autonomous_database_and_wait_for_work_request(self, autonomous_database_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.delete_autonomous_database` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str autonomous_database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.delete_autonomous_database`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.delete_autonomous_database(autonomous_database_id, **operation_kwargs)
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

    def delete_autonomous_vm_cluster_and_wait_for_work_request(self, autonomous_vm_cluster_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.delete_autonomous_vm_cluster` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str autonomous_vm_cluster_id: (required)
            The autonomous VM cluster `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.delete_autonomous_vm_cluster`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.delete_autonomous_vm_cluster(autonomous_vm_cluster_id, **operation_kwargs)
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

    def delete_backup_and_wait_for_work_request(self, backup_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.delete_backup` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str backup_id: (required)
            The backup `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.delete_backup`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.delete_backup(backup_id, **operation_kwargs)
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

    def delete_backup_destination_and_wait_for_state(self, backup_destination_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.delete_backup_destination` and waits for the :py:class:`~oci.database.models.BackupDestination` acted upon
        to enter the given state(s).

        :param str backup_destination_id: (required)
            The `OCID`__ of the backup destination.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.BackupDestination.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.delete_backup_destination`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_backup_destination(backup_destination_id)
        operation_result = None
        try:
            operation_result = self.client.delete_backup_destination(backup_destination_id, **operation_kwargs)
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

    def delete_cloud_exadata_infrastructure_and_wait_for_work_request(self, cloud_exadata_infrastructure_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.delete_cloud_exadata_infrastructure` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str cloud_exadata_infrastructure_id: (required)
            The cloud Exadata infrastructure `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.delete_cloud_exadata_infrastructure`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.delete_cloud_exadata_infrastructure(cloud_exadata_infrastructure_id, **operation_kwargs)
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

    def delete_cloud_vm_cluster_and_wait_for_work_request(self, cloud_vm_cluster_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.delete_cloud_vm_cluster` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str cloud_vm_cluster_id: (required)
            The cloud VM cluster `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.delete_cloud_vm_cluster`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.delete_cloud_vm_cluster(cloud_vm_cluster_id, **operation_kwargs)
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

    def delete_database_and_wait_for_work_request(self, database_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.delete_database` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.delete_database`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.delete_database(database_id, **operation_kwargs)
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

    def delete_database_software_image_and_wait_for_work_request(self, database_software_image_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.delete_database_software_image` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str database_software_image_id: (required)
            The DB system `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.delete_database_software_image`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.delete_database_software_image(database_software_image_id, **operation_kwargs)
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

    def delete_db_home_and_wait_for_work_request(self, db_home_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.delete_db_home` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str db_home_id: (required)
            The Database Home `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.delete_db_home`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.delete_db_home(db_home_id, **operation_kwargs)
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

    def delete_exadata_infrastructure_and_wait_for_work_request(self, exadata_infrastructure_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.delete_exadata_infrastructure` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str exadata_infrastructure_id: (required)
            The Exadata infrastructure `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.delete_exadata_infrastructure`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.delete_exadata_infrastructure(exadata_infrastructure_id, **operation_kwargs)
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

    def delete_key_store_and_wait_for_state(self, key_store_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.delete_key_store` and waits for the :py:class:`~oci.database.models.KeyStore` acted upon
        to enter the given state(s).

        :param str key_store_id: (required)
            The `OCID`__ of the key store.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.KeyStore.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.delete_key_store`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_key_store(key_store_id)
        operation_result = None
        try:
            operation_result = self.client.delete_key_store(key_store_id, **operation_kwargs)
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

    def delete_vm_cluster_and_wait_for_work_request(self, vm_cluster_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.delete_vm_cluster` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str vm_cluster_id: (required)
            The VM cluster `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.delete_vm_cluster`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.delete_vm_cluster(vm_cluster_id, **operation_kwargs)
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

    def delete_vm_cluster_network_and_wait_for_work_request(self, exadata_infrastructure_id, vm_cluster_network_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.delete_vm_cluster_network` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str exadata_infrastructure_id: (required)
            The Exadata infrastructure `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str vm_cluster_network_id: (required)
            The VM cluster network `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.delete_vm_cluster_network`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.delete_vm_cluster_network(exadata_infrastructure_id, vm_cluster_network_id, **operation_kwargs)
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

    def deregister_autonomous_database_data_safe_and_wait_for_work_request(self, autonomous_database_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.deregister_autonomous_database_data_safe` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str autonomous_database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.deregister_autonomous_database_data_safe`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.deregister_autonomous_database_data_safe(autonomous_database_id, **operation_kwargs)
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

    def disable_autonomous_database_operations_insights_and_wait_for_work_request(self, autonomous_database_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.disable_autonomous_database_operations_insights` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str autonomous_database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.disable_autonomous_database_operations_insights`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.disable_autonomous_database_operations_insights(autonomous_database_id, **operation_kwargs)
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

    def enable_autonomous_database_operations_insights_and_wait_for_work_request(self, autonomous_database_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.enable_autonomous_database_operations_insights` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str autonomous_database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.enable_autonomous_database_operations_insights`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.enable_autonomous_database_operations_insights(autonomous_database_id, **operation_kwargs)
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

    def fail_over_autonomous_database_and_wait_for_work_request(self, autonomous_database_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.fail_over_autonomous_database` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str autonomous_database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.fail_over_autonomous_database`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.fail_over_autonomous_database(autonomous_database_id, **operation_kwargs)
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

    def fail_over_autonomous_database_and_wait_for_state(self, autonomous_database_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.fail_over_autonomous_database` and waits for the :py:class:`~oci.database.models.AutonomousDatabase` acted upon
        to enter the given state(s).

        :param str autonomous_database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.AutonomousDatabase.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.fail_over_autonomous_database`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.fail_over_autonomous_database(autonomous_database_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_autonomous_database(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def failover_autonomous_container_database_dataguard_association_and_wait_for_work_request(self, autonomous_container_database_id, autonomous_container_database_dataguard_association_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.failover_autonomous_container_database_dataguard_association` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str autonomous_container_database_id: (required)
            The Autonomous Container Database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str autonomous_container_database_dataguard_association_id: (required)
            The Autonomous Container Database-Autonomous Data Guard association `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.failover_autonomous_container_database_dataguard_association`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.failover_autonomous_container_database_dataguard_association(autonomous_container_database_id, autonomous_container_database_dataguard_association_id, **operation_kwargs)
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

    def failover_autonomous_container_database_dataguard_association_and_wait_for_state(self, autonomous_container_database_id, autonomous_container_database_dataguard_association_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.failover_autonomous_container_database_dataguard_association` and waits for the :py:class:`~oci.database.models.AutonomousContainerDatabaseDataguardAssociation` acted upon
        to enter the given state(s).

        :param str autonomous_container_database_id: (required)
            The Autonomous Container Database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str autonomous_container_database_dataguard_association_id: (required)
            The Autonomous Container Database-Autonomous Data Guard association `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.AutonomousContainerDatabaseDataguardAssociation.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.failover_autonomous_container_database_dataguard_association`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.failover_autonomous_container_database_dataguard_association(autonomous_container_database_id, autonomous_container_database_dataguard_association_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_autonomous_container_database_dataguard_association(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def failover_data_guard_association_and_wait_for_work_request(self, database_id, data_guard_association_id, failover_data_guard_association_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.failover_data_guard_association` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str data_guard_association_id: (required)
            The Data Guard association's `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param FailoverDataGuardAssociationDetails failover_data_guard_association_details: (required)
            A request to perform a failover, transitioning a standby database into a primary database.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.failover_data_guard_association`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.failover_data_guard_association(database_id, data_guard_association_id, failover_data_guard_association_details, **operation_kwargs)
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

    def failover_data_guard_association_and_wait_for_state(self, database_id, data_guard_association_id, failover_data_guard_association_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.failover_data_guard_association` and waits for the :py:class:`~oci.database.models.DataGuardAssociation` acted upon
        to enter the given state(s).

        :param str database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str data_guard_association_id: (required)
            The Data Guard association's `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param FailoverDataGuardAssociationDetails failover_data_guard_association_details: (required)
            A request to perform a failover, transitioning a standby database into a primary database.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.DataGuardAssociation.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.failover_data_guard_association`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.failover_data_guard_association(database_id, data_guard_association_id, failover_data_guard_association_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_data_guard_association(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def launch_autonomous_exadata_infrastructure_and_wait_for_work_request(self, launch_autonomous_exadata_infrastructure_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.launch_autonomous_exadata_infrastructure` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param LaunchAutonomousExadataInfrastructureDetails launch_autonomous_exadata_infrastructure_details: (required)
            Request to create an Autonomous Exadata Infrastructure resource.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.launch_autonomous_exadata_infrastructure`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.launch_autonomous_exadata_infrastructure(launch_autonomous_exadata_infrastructure_details, **operation_kwargs)
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

    def launch_autonomous_exadata_infrastructure_and_wait_for_state(self, launch_autonomous_exadata_infrastructure_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.launch_autonomous_exadata_infrastructure` and waits for the :py:class:`~oci.database.models.AutonomousExadataInfrastructure` acted upon
        to enter the given state(s).

        :param LaunchAutonomousExadataInfrastructureDetails launch_autonomous_exadata_infrastructure_details: (required)
            Request to create an Autonomous Exadata Infrastructure resource.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.AutonomousExadataInfrastructure.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.launch_autonomous_exadata_infrastructure`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.launch_autonomous_exadata_infrastructure(launch_autonomous_exadata_infrastructure_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_autonomous_exadata_infrastructure(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def launch_db_system_and_wait_for_work_request(self, launch_db_system_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.launch_db_system` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param LaunchDbSystemBase launch_db_system_details: (required)
            Request to launch a DB system.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.launch_db_system`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.launch_db_system(launch_db_system_details, **operation_kwargs)
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

    def launch_db_system_and_wait_for_state(self, launch_db_system_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.launch_db_system` and waits for the :py:class:`~oci.database.models.DbSystem` acted upon
        to enter the given state(s).

        :param LaunchDbSystemBase launch_db_system_details: (required)
            Request to launch a DB system.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.DbSystem.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.launch_db_system`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.launch_db_system(launch_db_system_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_db_system(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def migrate_exadata_db_system_resource_model_and_wait_for_work_request(self, db_system_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.migrate_exadata_db_system_resource_model` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str db_system_id: (required)
            The DB system `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.migrate_exadata_db_system_resource_model`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.migrate_exadata_db_system_resource_model(db_system_id, **operation_kwargs)
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

    def register_autonomous_database_data_safe_and_wait_for_work_request(self, autonomous_database_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.register_autonomous_database_data_safe` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str autonomous_database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.register_autonomous_database_data_safe`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.register_autonomous_database_data_safe(autonomous_database_id, **operation_kwargs)
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

    def reinstate_autonomous_container_database_dataguard_association_and_wait_for_work_request(self, autonomous_container_database_id, autonomous_container_database_dataguard_association_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.reinstate_autonomous_container_database_dataguard_association` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str autonomous_container_database_id: (required)
            The Autonomous Container Database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str autonomous_container_database_dataguard_association_id: (required)
            The Autonomous Container Database-Autonomous Data Guard association `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.reinstate_autonomous_container_database_dataguard_association`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.reinstate_autonomous_container_database_dataguard_association(autonomous_container_database_id, autonomous_container_database_dataguard_association_id, **operation_kwargs)
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

    def reinstate_autonomous_container_database_dataguard_association_and_wait_for_state(self, autonomous_container_database_id, autonomous_container_database_dataguard_association_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.reinstate_autonomous_container_database_dataguard_association` and waits for the :py:class:`~oci.database.models.AutonomousContainerDatabaseDataguardAssociation` acted upon
        to enter the given state(s).

        :param str autonomous_container_database_id: (required)
            The Autonomous Container Database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str autonomous_container_database_dataguard_association_id: (required)
            The Autonomous Container Database-Autonomous Data Guard association `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.AutonomousContainerDatabaseDataguardAssociation.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.reinstate_autonomous_container_database_dataguard_association`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.reinstate_autonomous_container_database_dataguard_association(autonomous_container_database_id, autonomous_container_database_dataguard_association_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_autonomous_container_database_dataguard_association(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def reinstate_data_guard_association_and_wait_for_work_request(self, database_id, data_guard_association_id, reinstate_data_guard_association_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.reinstate_data_guard_association` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str data_guard_association_id: (required)
            The Data Guard association's `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param ReinstateDataGuardAssociationDetails reinstate_data_guard_association_details: (required)
            A request to reinstate a database in a standby role.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.reinstate_data_guard_association`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.reinstate_data_guard_association(database_id, data_guard_association_id, reinstate_data_guard_association_details, **operation_kwargs)
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

    def reinstate_data_guard_association_and_wait_for_state(self, database_id, data_guard_association_id, reinstate_data_guard_association_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.reinstate_data_guard_association` and waits for the :py:class:`~oci.database.models.DataGuardAssociation` acted upon
        to enter the given state(s).

        :param str database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str data_guard_association_id: (required)
            The Data Guard association's `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param ReinstateDataGuardAssociationDetails reinstate_data_guard_association_details: (required)
            A request to reinstate a database in a standby role.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.DataGuardAssociation.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.reinstate_data_guard_association`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.reinstate_data_guard_association(database_id, data_guard_association_id, reinstate_data_guard_association_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_data_guard_association(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def restart_autonomous_container_database_and_wait_for_work_request(self, autonomous_container_database_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.restart_autonomous_container_database` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str autonomous_container_database_id: (required)
            The Autonomous Container Database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.restart_autonomous_container_database`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.restart_autonomous_container_database(autonomous_container_database_id, **operation_kwargs)
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

    def restart_autonomous_container_database_and_wait_for_state(self, autonomous_container_database_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.restart_autonomous_container_database` and waits for the :py:class:`~oci.database.models.AutonomousContainerDatabase` acted upon
        to enter the given state(s).

        :param str autonomous_container_database_id: (required)
            The Autonomous Container Database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.AutonomousContainerDatabase.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.restart_autonomous_container_database`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.restart_autonomous_container_database(autonomous_container_database_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_autonomous_container_database(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def restart_autonomous_database_and_wait_for_work_request(self, autonomous_database_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.restart_autonomous_database` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str autonomous_database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.restart_autonomous_database`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.restart_autonomous_database(autonomous_database_id, **operation_kwargs)
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

    def restart_autonomous_database_and_wait_for_state(self, autonomous_database_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.restart_autonomous_database` and waits for the :py:class:`~oci.database.models.AutonomousDatabase` acted upon
        to enter the given state(s).

        :param str autonomous_database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.AutonomousDatabase.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.restart_autonomous_database`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.restart_autonomous_database(autonomous_database_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_autonomous_database(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def restore_autonomous_data_warehouse_and_wait_for_state(self, autonomous_data_warehouse_id, restore_autonomous_data_warehouse_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.restore_autonomous_data_warehouse` and waits for the :py:class:`~oci.database.models.AutonomousDataWarehouse` acted upon
        to enter the given state(s).

        :param str autonomous_data_warehouse_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param RestoreAutonomousDataWarehouseDetails restore_autonomous_data_warehouse_details: (required)
            Request to perform an Autonomous Data Warehouse restore.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.AutonomousDataWarehouse.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.restore_autonomous_data_warehouse`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.restore_autonomous_data_warehouse(autonomous_data_warehouse_id, restore_autonomous_data_warehouse_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_autonomous_data_warehouse(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def restore_autonomous_database_and_wait_for_work_request(self, autonomous_database_id, restore_autonomous_database_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.restore_autonomous_database` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str autonomous_database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param RestoreAutonomousDatabaseDetails restore_autonomous_database_details: (required)
            Request to perform an Autonomous Database restore.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.restore_autonomous_database`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.restore_autonomous_database(autonomous_database_id, restore_autonomous_database_details, **operation_kwargs)
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

    def restore_autonomous_database_and_wait_for_state(self, autonomous_database_id, restore_autonomous_database_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.restore_autonomous_database` and waits for the :py:class:`~oci.database.models.AutonomousDatabase` acted upon
        to enter the given state(s).

        :param str autonomous_database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param RestoreAutonomousDatabaseDetails restore_autonomous_database_details: (required)
            Request to perform an Autonomous Database restore.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.AutonomousDatabase.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.restore_autonomous_database`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.restore_autonomous_database(autonomous_database_id, restore_autonomous_database_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_autonomous_database(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def restore_database_and_wait_for_work_request(self, database_id, restore_database_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.restore_database` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param RestoreDatabaseDetails restore_database_details: (required)
            Request to perform database restore.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.restore_database`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.restore_database(database_id, restore_database_details, **operation_kwargs)
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

    def restore_database_and_wait_for_state(self, database_id, restore_database_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.restore_database` and waits for the :py:class:`~oci.database.models.Database` acted upon
        to enter the given state(s).

        :param str database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param RestoreDatabaseDetails restore_database_details: (required)
            Request to perform database restore.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.Database.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.restore_database`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.restore_database(database_id, restore_database_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_database(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def rotate_autonomous_container_database_encryption_key_and_wait_for_work_request(self, autonomous_container_database_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.rotate_autonomous_container_database_encryption_key` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str autonomous_container_database_id: (required)
            The Autonomous Container Database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.rotate_autonomous_container_database_encryption_key`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.rotate_autonomous_container_database_encryption_key(autonomous_container_database_id, **operation_kwargs)
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

    def rotate_autonomous_container_database_encryption_key_and_wait_for_state(self, autonomous_container_database_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.rotate_autonomous_container_database_encryption_key` and waits for the :py:class:`~oci.database.models.AutonomousContainerDatabase` acted upon
        to enter the given state(s).

        :param str autonomous_container_database_id: (required)
            The Autonomous Container Database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.AutonomousContainerDatabase.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.rotate_autonomous_container_database_encryption_key`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.rotate_autonomous_container_database_encryption_key(autonomous_container_database_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_autonomous_container_database(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def rotate_autonomous_database_encryption_key_and_wait_for_work_request(self, autonomous_database_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.rotate_autonomous_database_encryption_key` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str autonomous_database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.rotate_autonomous_database_encryption_key`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.rotate_autonomous_database_encryption_key(autonomous_database_id, **operation_kwargs)
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

    def rotate_autonomous_database_encryption_key_and_wait_for_state(self, autonomous_database_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.rotate_autonomous_database_encryption_key` and waits for the :py:class:`~oci.database.models.AutonomousDatabase` acted upon
        to enter the given state(s).

        :param str autonomous_database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.AutonomousDatabase.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.rotate_autonomous_database_encryption_key`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.rotate_autonomous_database_encryption_key(autonomous_database_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_autonomous_database(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def start_autonomous_data_warehouse_and_wait_for_state(self, autonomous_data_warehouse_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.start_autonomous_data_warehouse` and waits for the :py:class:`~oci.database.models.AutonomousDataWarehouse` acted upon
        to enter the given state(s).

        :param str autonomous_data_warehouse_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.AutonomousDataWarehouse.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.start_autonomous_data_warehouse`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.start_autonomous_data_warehouse(autonomous_data_warehouse_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_autonomous_data_warehouse(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def start_autonomous_database_and_wait_for_work_request(self, autonomous_database_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.start_autonomous_database` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str autonomous_database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.start_autonomous_database`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.start_autonomous_database(autonomous_database_id, **operation_kwargs)
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

    def start_autonomous_database_and_wait_for_state(self, autonomous_database_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.start_autonomous_database` and waits for the :py:class:`~oci.database.models.AutonomousDatabase` acted upon
        to enter the given state(s).

        :param str autonomous_database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.AutonomousDatabase.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.start_autonomous_database`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.start_autonomous_database(autonomous_database_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_autonomous_database(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def stop_autonomous_data_warehouse_and_wait_for_state(self, autonomous_data_warehouse_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.stop_autonomous_data_warehouse` and waits for the :py:class:`~oci.database.models.AutonomousDataWarehouse` acted upon
        to enter the given state(s).

        :param str autonomous_data_warehouse_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.AutonomousDataWarehouse.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.stop_autonomous_data_warehouse`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.stop_autonomous_data_warehouse(autonomous_data_warehouse_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_autonomous_data_warehouse(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def stop_autonomous_database_and_wait_for_work_request(self, autonomous_database_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.stop_autonomous_database` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str autonomous_database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.stop_autonomous_database`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.stop_autonomous_database(autonomous_database_id, **operation_kwargs)
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

    def stop_autonomous_database_and_wait_for_state(self, autonomous_database_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.stop_autonomous_database` and waits for the :py:class:`~oci.database.models.AutonomousDatabase` acted upon
        to enter the given state(s).

        :param str autonomous_database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.AutonomousDatabase.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.stop_autonomous_database`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.stop_autonomous_database(autonomous_database_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_autonomous_database(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def switchover_autonomous_container_database_dataguard_association_and_wait_for_work_request(self, autonomous_container_database_id, autonomous_container_database_dataguard_association_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.switchover_autonomous_container_database_dataguard_association` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str autonomous_container_database_id: (required)
            The Autonomous Container Database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str autonomous_container_database_dataguard_association_id: (required)
            The Autonomous Container Database-Autonomous Data Guard association `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.switchover_autonomous_container_database_dataguard_association`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.switchover_autonomous_container_database_dataguard_association(autonomous_container_database_id, autonomous_container_database_dataguard_association_id, **operation_kwargs)
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

    def switchover_autonomous_container_database_dataguard_association_and_wait_for_state(self, autonomous_container_database_id, autonomous_container_database_dataguard_association_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.switchover_autonomous_container_database_dataguard_association` and waits for the :py:class:`~oci.database.models.AutonomousContainerDatabaseDataguardAssociation` acted upon
        to enter the given state(s).

        :param str autonomous_container_database_id: (required)
            The Autonomous Container Database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str autonomous_container_database_dataguard_association_id: (required)
            The Autonomous Container Database-Autonomous Data Guard association `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.AutonomousContainerDatabaseDataguardAssociation.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.switchover_autonomous_container_database_dataguard_association`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.switchover_autonomous_container_database_dataguard_association(autonomous_container_database_id, autonomous_container_database_dataguard_association_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_autonomous_container_database_dataguard_association(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def switchover_autonomous_database_and_wait_for_work_request(self, autonomous_database_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.switchover_autonomous_database` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str autonomous_database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.switchover_autonomous_database`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.switchover_autonomous_database(autonomous_database_id, **operation_kwargs)
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

    def switchover_autonomous_database_and_wait_for_state(self, autonomous_database_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.switchover_autonomous_database` and waits for the :py:class:`~oci.database.models.AutonomousDatabase` acted upon
        to enter the given state(s).

        :param str autonomous_database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.AutonomousDatabase.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.switchover_autonomous_database`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.switchover_autonomous_database(autonomous_database_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_autonomous_database(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def switchover_data_guard_association_and_wait_for_work_request(self, database_id, data_guard_association_id, switchover_data_guard_association_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.switchover_data_guard_association` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str data_guard_association_id: (required)
            The Data Guard association's `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param SwitchoverDataGuardAssociationDetails switchover_data_guard_association_details: (required)
            Request to swtichover a primary to a standby.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.switchover_data_guard_association`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.switchover_data_guard_association(database_id, data_guard_association_id, switchover_data_guard_association_details, **operation_kwargs)
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

    def switchover_data_guard_association_and_wait_for_state(self, database_id, data_guard_association_id, switchover_data_guard_association_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.switchover_data_guard_association` and waits for the :py:class:`~oci.database.models.DataGuardAssociation` acted upon
        to enter the given state(s).

        :param str database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str data_guard_association_id: (required)
            The Data Guard association's `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param SwitchoverDataGuardAssociationDetails switchover_data_guard_association_details: (required)
            Request to swtichover a primary to a standby.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.DataGuardAssociation.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.switchover_data_guard_association`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.switchover_data_guard_association(database_id, data_guard_association_id, switchover_data_guard_association_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_data_guard_association(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def terminate_autonomous_container_database_and_wait_for_work_request(self, autonomous_container_database_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.terminate_autonomous_container_database` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str autonomous_container_database_id: (required)
            The Autonomous Container Database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.terminate_autonomous_container_database`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.terminate_autonomous_container_database(autonomous_container_database_id, **operation_kwargs)
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

    def terminate_autonomous_exadata_infrastructure_and_wait_for_work_request(self, autonomous_exadata_infrastructure_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.terminate_autonomous_exadata_infrastructure` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str autonomous_exadata_infrastructure_id: (required)
            The Autonomous Exadata Infrastructure  `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.terminate_autonomous_exadata_infrastructure`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.terminate_autonomous_exadata_infrastructure(autonomous_exadata_infrastructure_id, **operation_kwargs)
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

    def terminate_db_system_and_wait_for_work_request(self, db_system_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.terminate_db_system` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str db_system_id: (required)
            The DB system `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.terminate_db_system`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.terminate_db_system(db_system_id, **operation_kwargs)
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

    def update_autonomous_container_database_and_wait_for_work_request(self, autonomous_container_database_id, update_autonomous_container_database_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.update_autonomous_container_database` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str autonomous_container_database_id: (required)
            The Autonomous Container Database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateAutonomousContainerDatabaseDetails update_autonomous_container_database_details: (required)
            Request to update the properties of an Autonomous Container Database.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.update_autonomous_container_database`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_autonomous_container_database(autonomous_container_database_id, update_autonomous_container_database_details, **operation_kwargs)
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

    def update_autonomous_container_database_and_wait_for_state(self, autonomous_container_database_id, update_autonomous_container_database_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.update_autonomous_container_database` and waits for the :py:class:`~oci.database.models.AutonomousContainerDatabase` acted upon
        to enter the given state(s).

        :param str autonomous_container_database_id: (required)
            The Autonomous Container Database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateAutonomousContainerDatabaseDetails update_autonomous_container_database_details: (required)
            Request to update the properties of an Autonomous Container Database.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.AutonomousContainerDatabase.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.update_autonomous_container_database`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_autonomous_container_database(autonomous_container_database_id, update_autonomous_container_database_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_autonomous_container_database(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_autonomous_data_warehouse_and_wait_for_state(self, autonomous_data_warehouse_id, update_autonomous_data_warehouse_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.update_autonomous_data_warehouse` and waits for the :py:class:`~oci.database.models.AutonomousDataWarehouse` acted upon
        to enter the given state(s).

        :param str autonomous_data_warehouse_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateAutonomousDataWarehouseDetails update_autonomous_data_warehouse_details: (required)
            Request to update the properties of an Autonomous Data Warehouse.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.AutonomousDataWarehouse.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.update_autonomous_data_warehouse`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_autonomous_data_warehouse(autonomous_data_warehouse_id, update_autonomous_data_warehouse_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_autonomous_data_warehouse(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_autonomous_database_and_wait_for_work_request(self, autonomous_database_id, update_autonomous_database_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.update_autonomous_database` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str autonomous_database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateAutonomousDatabaseDetails update_autonomous_database_details: (required)
            Request to update the properties of an Autonomous Database.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.update_autonomous_database`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_autonomous_database(autonomous_database_id, update_autonomous_database_details, **operation_kwargs)
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

    def update_autonomous_database_and_wait_for_state(self, autonomous_database_id, update_autonomous_database_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.update_autonomous_database` and waits for the :py:class:`~oci.database.models.AutonomousDatabase` acted upon
        to enter the given state(s).

        :param str autonomous_database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateAutonomousDatabaseDetails update_autonomous_database_details: (required)
            Request to update the properties of an Autonomous Database.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.AutonomousDatabase.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.update_autonomous_database`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_autonomous_database(autonomous_database_id, update_autonomous_database_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_autonomous_database(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_autonomous_database_regional_wallet_and_wait_for_work_request(self, update_autonomous_database_wallet_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.update_autonomous_database_regional_wallet` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param UpdateAutonomousDatabaseWalletDetails update_autonomous_database_wallet_details: (required)
            Request to update the properties of Autonomous Database regional wallet.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.update_autonomous_database_regional_wallet`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_autonomous_database_regional_wallet(update_autonomous_database_wallet_details, **operation_kwargs)
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

    def update_autonomous_database_wallet_and_wait_for_work_request(self, autonomous_database_id, update_autonomous_database_wallet_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.update_autonomous_database_wallet` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str autonomous_database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateAutonomousDatabaseWalletDetails update_autonomous_database_wallet_details: (required)
            Request to update the properties of an Autonomous Database wallet.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.update_autonomous_database_wallet`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_autonomous_database_wallet(autonomous_database_id, update_autonomous_database_wallet_details, **operation_kwargs)
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

    def update_autonomous_exadata_infrastructure_and_wait_for_work_request(self, autonomous_exadata_infrastructure_id, update_autonomous_exadata_infrastructures_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.update_autonomous_exadata_infrastructure` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str autonomous_exadata_infrastructure_id: (required)
            The Autonomous Exadata Infrastructure  `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateAutonomousExadataInfrastructureDetails update_autonomous_exadata_infrastructures_details: (required)
            Request to update the properties of a Autonomous Exadata Infrastructure.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.update_autonomous_exadata_infrastructure`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_autonomous_exadata_infrastructure(autonomous_exadata_infrastructure_id, update_autonomous_exadata_infrastructures_details, **operation_kwargs)
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

    def update_autonomous_exadata_infrastructure_and_wait_for_state(self, autonomous_exadata_infrastructure_id, update_autonomous_exadata_infrastructures_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.update_autonomous_exadata_infrastructure` and waits for the :py:class:`~oci.database.models.AutonomousExadataInfrastructure` acted upon
        to enter the given state(s).

        :param str autonomous_exadata_infrastructure_id: (required)
            The Autonomous Exadata Infrastructure  `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateAutonomousExadataInfrastructureDetails update_autonomous_exadata_infrastructures_details: (required)
            Request to update the properties of a Autonomous Exadata Infrastructure.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.AutonomousExadataInfrastructure.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.update_autonomous_exadata_infrastructure`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_autonomous_exadata_infrastructure(autonomous_exadata_infrastructure_id, update_autonomous_exadata_infrastructures_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_autonomous_exadata_infrastructure(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_autonomous_vm_cluster_and_wait_for_work_request(self, autonomous_vm_cluster_id, update_autonomous_vm_cluster_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.update_autonomous_vm_cluster` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str autonomous_vm_cluster_id: (required)
            The autonomous VM cluster `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateAutonomousVmClusterDetails update_autonomous_vm_cluster_details: (required)
            Request to update the attributes of an Autonomous VM cluster.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.update_autonomous_vm_cluster`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_autonomous_vm_cluster(autonomous_vm_cluster_id, update_autonomous_vm_cluster_details, **operation_kwargs)
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

    def update_autonomous_vm_cluster_and_wait_for_state(self, autonomous_vm_cluster_id, update_autonomous_vm_cluster_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.update_autonomous_vm_cluster` and waits for the :py:class:`~oci.database.models.AutonomousVmCluster` acted upon
        to enter the given state(s).

        :param str autonomous_vm_cluster_id: (required)
            The autonomous VM cluster `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateAutonomousVmClusterDetails update_autonomous_vm_cluster_details: (required)
            Request to update the attributes of an Autonomous VM cluster.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.AutonomousVmCluster.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.update_autonomous_vm_cluster`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_autonomous_vm_cluster(autonomous_vm_cluster_id, update_autonomous_vm_cluster_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_autonomous_vm_cluster(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_backup_destination_and_wait_for_state(self, backup_destination_id, update_backup_destination_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.update_backup_destination` and waits for the :py:class:`~oci.database.models.BackupDestination` acted upon
        to enter the given state(s).

        :param str backup_destination_id: (required)
            The `OCID`__ of the backup destination.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateBackupDestinationDetails update_backup_destination_details: (required)
            For a RECOVERY_APPLIANCE backup destination, request to update the connection string and/or the list of VPC users.
            For an NFS backup destination, request to update the NFS location.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.BackupDestination.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.update_backup_destination`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_backup_destination(backup_destination_id, update_backup_destination_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_backup_destination(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_cloud_exadata_infrastructure_and_wait_for_work_request(self, cloud_exadata_infrastructure_id, update_cloud_exadata_infrastructure_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.update_cloud_exadata_infrastructure` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str cloud_exadata_infrastructure_id: (required)
            The cloud Exadata infrastructure `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateCloudExadataInfrastructureDetails update_cloud_exadata_infrastructure_details: (required)
            Request to update the properties of an cloud Exadata infrastructure resource.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.update_cloud_exadata_infrastructure`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_cloud_exadata_infrastructure(cloud_exadata_infrastructure_id, update_cloud_exadata_infrastructure_details, **operation_kwargs)
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

    def update_cloud_exadata_infrastructure_and_wait_for_state(self, cloud_exadata_infrastructure_id, update_cloud_exadata_infrastructure_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.update_cloud_exadata_infrastructure` and waits for the :py:class:`~oci.database.models.CloudExadataInfrastructure` acted upon
        to enter the given state(s).

        :param str cloud_exadata_infrastructure_id: (required)
            The cloud Exadata infrastructure `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateCloudExadataInfrastructureDetails update_cloud_exadata_infrastructure_details: (required)
            Request to update the properties of an cloud Exadata infrastructure resource.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.CloudExadataInfrastructure.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.update_cloud_exadata_infrastructure`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_cloud_exadata_infrastructure(cloud_exadata_infrastructure_id, update_cloud_exadata_infrastructure_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_cloud_exadata_infrastructure(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_cloud_vm_cluster_and_wait_for_work_request(self, cloud_vm_cluster_id, update_cloud_vm_cluster_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.update_cloud_vm_cluster` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str cloud_vm_cluster_id: (required)
            The cloud VM cluster `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateCloudVmClusterDetails update_cloud_vm_cluster_details: (required)
            Request to update the attributes of a cloud VM cluster.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.update_cloud_vm_cluster`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_cloud_vm_cluster(cloud_vm_cluster_id, update_cloud_vm_cluster_details, **operation_kwargs)
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

    def update_cloud_vm_cluster_and_wait_for_state(self, cloud_vm_cluster_id, update_cloud_vm_cluster_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.update_cloud_vm_cluster` and waits for the :py:class:`~oci.database.models.CloudVmCluster` acted upon
        to enter the given state(s).

        :param str cloud_vm_cluster_id: (required)
            The cloud VM cluster `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateCloudVmClusterDetails update_cloud_vm_cluster_details: (required)
            Request to update the attributes of a cloud VM cluster.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.CloudVmCluster.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.update_cloud_vm_cluster`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_cloud_vm_cluster(cloud_vm_cluster_id, update_cloud_vm_cluster_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_cloud_vm_cluster(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_cloud_vm_cluster_iorm_config_and_wait_for_work_request(self, cloud_vm_cluster_id, cloud_vm_cluster_iorm_config_update_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.update_cloud_vm_cluster_iorm_config` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str cloud_vm_cluster_id: (required)
            The cloud VM cluster `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param ExadataIormConfigUpdateDetails cloud_vm_cluster_iorm_config_update_details: (required)
            Request to perform database update.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.update_cloud_vm_cluster_iorm_config`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_cloud_vm_cluster_iorm_config(cloud_vm_cluster_id, cloud_vm_cluster_iorm_config_update_details, **operation_kwargs)
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

    def update_database_and_wait_for_work_request(self, database_id, update_database_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.update_database` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateDatabaseDetails update_database_details: (required)
            Request to perform database update.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.update_database`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_database(database_id, update_database_details, **operation_kwargs)
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

    def update_database_and_wait_for_state(self, database_id, update_database_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.update_database` and waits for the :py:class:`~oci.database.models.Database` acted upon
        to enter the given state(s).

        :param str database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateDatabaseDetails update_database_details: (required)
            Request to perform database update.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.Database.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.update_database`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_database(database_id, update_database_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_database(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_database_software_image_and_wait_for_state(self, database_software_image_id, update_database_software_image_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.update_database_software_image` and waits for the :py:class:`~oci.database.models.DatabaseSoftwareImage` acted upon
        to enter the given state(s).

        :param str database_software_image_id: (required)
            The DB system `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateDatabaseSoftwareImageDetails update_database_software_image_details: (required)
            Request to update the properties of a DB system.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.DatabaseSoftwareImage.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.update_database_software_image`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_database_software_image(database_software_image_id, update_database_software_image_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_database_software_image(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_db_home_and_wait_for_work_request(self, db_home_id, update_db_home_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.update_db_home` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str db_home_id: (required)
            The Database Home `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateDbHomeDetails update_db_home_details: (required)
            Request to update the properties of a Database Home.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.update_db_home`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_db_home(db_home_id, update_db_home_details, **operation_kwargs)
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

    def update_db_home_and_wait_for_state(self, db_home_id, update_db_home_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.update_db_home` and waits for the :py:class:`~oci.database.models.DbHome` acted upon
        to enter the given state(s).

        :param str db_home_id: (required)
            The Database Home `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateDbHomeDetails update_db_home_details: (required)
            Request to update the properties of a Database Home.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.DbHome.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.update_db_home`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_db_home(db_home_id, update_db_home_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_db_home(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_db_system_and_wait_for_work_request(self, db_system_id, update_db_system_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.update_db_system` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str db_system_id: (required)
            The DB system `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateDbSystemDetails update_db_system_details: (required)
            Request to update the properties of a DB system.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.update_db_system`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_db_system(db_system_id, update_db_system_details, **operation_kwargs)
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

    def update_db_system_and_wait_for_state(self, db_system_id, update_db_system_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.update_db_system` and waits for the :py:class:`~oci.database.models.DbSystem` acted upon
        to enter the given state(s).

        :param str db_system_id: (required)
            The DB system `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateDbSystemDetails update_db_system_details: (required)
            Request to update the properties of a DB system.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.DbSystem.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.update_db_system`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_db_system(db_system_id, update_db_system_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_db_system(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_exadata_infrastructure_and_wait_for_work_request(self, exadata_infrastructure_id, update_exadata_infrastructure_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.update_exadata_infrastructure` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str exadata_infrastructure_id: (required)
            The Exadata infrastructure `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateExadataInfrastructureDetails update_exadata_infrastructure_details: (required)
            Request to update the properties of an Exadata Cloud@Customer infrastructure.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.update_exadata_infrastructure`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_exadata_infrastructure(exadata_infrastructure_id, update_exadata_infrastructure_details, **operation_kwargs)
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

    def update_exadata_infrastructure_and_wait_for_state(self, exadata_infrastructure_id, update_exadata_infrastructure_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.update_exadata_infrastructure` and waits for the :py:class:`~oci.database.models.ExadataInfrastructure` acted upon
        to enter the given state(s).

        :param str exadata_infrastructure_id: (required)
            The Exadata infrastructure `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateExadataInfrastructureDetails update_exadata_infrastructure_details: (required)
            Request to update the properties of an Exadata Cloud@Customer infrastructure.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.ExadataInfrastructure.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.update_exadata_infrastructure`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_exadata_infrastructure(exadata_infrastructure_id, update_exadata_infrastructure_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_exadata_infrastructure(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_exadata_iorm_config_and_wait_for_work_request(self, db_system_id, exadata_iorm_config_update_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.update_exadata_iorm_config` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str db_system_id: (required)
            The DB system `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param ExadataIormConfigUpdateDetails exadata_iorm_config_update_details: (required)
            Request to perform database update.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.update_exadata_iorm_config`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_exadata_iorm_config(db_system_id, exadata_iorm_config_update_details, **operation_kwargs)
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

    def update_exadata_iorm_config_and_wait_for_state(self, db_system_id, exadata_iorm_config_update_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.update_exadata_iorm_config` and waits for the :py:class:`~oci.database.models.ExadataIormConfig` acted upon
        to enter the given state(s).

        :param str db_system_id: (required)
            The DB system `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param ExadataIormConfigUpdateDetails exadata_iorm_config_update_details: (required)
            Request to perform database update.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.ExadataIormConfig.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.update_exadata_iorm_config`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_exadata_iorm_config(db_system_id, exadata_iorm_config_update_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_exadata_iorm_config(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_key_store_and_wait_for_state(self, key_store_id, update_key_store_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.update_key_store` and waits for the :py:class:`~oci.database.models.KeyStore` acted upon
        to enter the given state(s).

        :param str key_store_id: (required)
            The `OCID`__ of the key store.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateKeyStoreDetails update_key_store_details: (required)
            Request to update the attributes of a key store.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.KeyStore.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.update_key_store`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_key_store(key_store_id, update_key_store_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_key_store(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_maintenance_run_and_wait_for_state(self, maintenance_run_id, update_maintenance_run_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.update_maintenance_run` and waits for the :py:class:`~oci.database.models.MaintenanceRun` acted upon
        to enter the given state(s).

        :param str maintenance_run_id: (required)
            The maintenance run OCID.

        :param UpdateMaintenanceRunDetails update_maintenance_run_details: (required)
            Request to update the properties of a maintenance run.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.MaintenanceRun.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.update_maintenance_run`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_maintenance_run(maintenance_run_id, update_maintenance_run_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_maintenance_run(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_vm_cluster_and_wait_for_work_request(self, vm_cluster_id, update_vm_cluster_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.update_vm_cluster` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str vm_cluster_id: (required)
            The VM cluster `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateVmClusterDetails update_vm_cluster_details: (required)
            Request to update the attributes of a VM cluster.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.update_vm_cluster`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_vm_cluster(vm_cluster_id, update_vm_cluster_details, **operation_kwargs)
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

    def update_vm_cluster_and_wait_for_state(self, vm_cluster_id, update_vm_cluster_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.update_vm_cluster` and waits for the :py:class:`~oci.database.models.VmCluster` acted upon
        to enter the given state(s).

        :param str vm_cluster_id: (required)
            The VM cluster `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateVmClusterDetails update_vm_cluster_details: (required)
            Request to update the attributes of a VM cluster.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.VmCluster.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.update_vm_cluster`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_vm_cluster(vm_cluster_id, update_vm_cluster_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_vm_cluster(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_vm_cluster_network_and_wait_for_work_request(self, exadata_infrastructure_id, vm_cluster_network_id, update_vm_cluster_network_details, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.update_vm_cluster_network` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str exadata_infrastructure_id: (required)
            The Exadata infrastructure `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str vm_cluster_network_id: (required)
            The VM cluster network `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateVmClusterNetworkDetails update_vm_cluster_network_details: (required)
            Request to update the properties of a VM cluster network.

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.update_vm_cluster_network`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_vm_cluster_network(exadata_infrastructure_id, vm_cluster_network_id, update_vm_cluster_network_details, **operation_kwargs)
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

    def update_vm_cluster_network_and_wait_for_state(self, exadata_infrastructure_id, vm_cluster_network_id, update_vm_cluster_network_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.update_vm_cluster_network` and waits for the :py:class:`~oci.database.models.VmClusterNetwork` acted upon
        to enter the given state(s).

        :param str exadata_infrastructure_id: (required)
            The Exadata infrastructure `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str vm_cluster_network_id: (required)
            The VM cluster network `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateVmClusterNetworkDetails update_vm_cluster_network_details: (required)
            Request to update the properties of a VM cluster network.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.VmClusterNetwork.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.update_vm_cluster_network`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_vm_cluster_network(exadata_infrastructure_id, vm_cluster_network_id, update_vm_cluster_network_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_vm_cluster_network(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def validate_vm_cluster_network_and_wait_for_work_request(self, exadata_infrastructure_id, vm_cluster_network_id, work_request_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.validate_vm_cluster_network` and waits for the oci.work_requests.models.WorkRequest
        to enter the given state(s).

        :param str exadata_infrastructure_id: (required)
            The Exadata infrastructure `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str vm_cluster_network_id: (required)
            The VM cluster network `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] work_request_states: (optional)
            An array of work requests states to wait on. These should be valid values for :py:attr:`~oci.work_requests.models.WorkRequest.status`
            Default values are termination states: [STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELED]

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.validate_vm_cluster_network`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.validate_vm_cluster_network(exadata_infrastructure_id, vm_cluster_network_id, **operation_kwargs)
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

    def validate_vm_cluster_network_and_wait_for_state(self, exadata_infrastructure_id, vm_cluster_network_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database.DatabaseClient.validate_vm_cluster_network` and waits for the :py:class:`~oci.database.models.VmClusterNetwork` acted upon
        to enter the given state(s).

        :param str exadata_infrastructure_id: (required)
            The Exadata infrastructure `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str vm_cluster_network_id: (required)
            The VM cluster network `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database.models.VmClusterNetwork.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database.DatabaseClient.validate_vm_cluster_network`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.validate_vm_cluster_network(exadata_infrastructure_id, vm_cluster_network_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_vm_cluster_network(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
