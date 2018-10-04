# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

import oci   # noqa: F401


class VirtualNetworkClientCompositeOperations(object):
    """
    This class provides a wrapper around :py:class:`~oci.core.VirtualNetworkClient` and offers convenience methods
    for operations that would otherwise need to be chained together. For example, instead of performing an action
    on a resource (e.g. launching an instance, creating a load balancer) and then using a waiter to wait for the resource
    to enter a given state, you can call a single method in this class to accomplish the same functionality
    """

    def __init__(self, client, **kwargs):
        """
        Creates a new VirtualNetworkClientCompositeOperations object

        :param VirtualNetworkClient client:
            The service client which will be wrapped by this object
        """
        self.client = client

    def attach_service_id_and_wait_for_state(self, service_gateway_id, attach_service_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.attach_service_id` and waits for the :py:class:`~oci.core.models.ServiceGateway` acted upon
        to enter the given state(s).

        :param str service_gateway_id: (required)
            The service gateway's `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param ServiceIdRequestDetails attach_service_details: (required)
            ServiceId of Service to be attached to a service gateway.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.ServiceGateway.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.attach_service_id`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.attach_service_id(service_gateway_id, attach_service_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_service_gateway(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_cross_connect_and_wait_for_state(self, create_cross_connect_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.create_cross_connect` and waits for the :py:class:`~oci.core.models.CrossConnect` acted upon
        to enter the given state(s).

        :param CreateCrossConnectDetails create_cross_connect_details: (required)
            Details to create a CrossConnect

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.CrossConnect.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.create_cross_connect`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_cross_connect(create_cross_connect_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_cross_connect(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_cross_connect_group_and_wait_for_state(self, create_cross_connect_group_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.create_cross_connect_group` and waits for the :py:class:`~oci.core.models.CrossConnectGroup` acted upon
        to enter the given state(s).

        :param CreateCrossConnectGroupDetails create_cross_connect_group_details: (required)
            Details to create a CrossConnectGroup

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.CrossConnectGroup.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.create_cross_connect_group`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_cross_connect_group(create_cross_connect_group_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_cross_connect_group(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_dhcp_options_and_wait_for_state(self, create_dhcp_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.create_dhcp_options` and waits for the :py:class:`~oci.core.models.DhcpOptions` acted upon
        to enter the given state(s).

        :param CreateDhcpDetails create_dhcp_details: (required)
            Request object for creating a new set of DHCP options.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.DhcpOptions.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.create_dhcp_options`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_dhcp_options(create_dhcp_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_dhcp_options(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_drg_and_wait_for_state(self, create_drg_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.create_drg` and waits for the :py:class:`~oci.core.models.Drg` acted upon
        to enter the given state(s).

        :param CreateDrgDetails create_drg_details: (required)
            Details for creating a DRG.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.Drg.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.create_drg`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_drg(create_drg_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_drg(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_drg_attachment_and_wait_for_state(self, create_drg_attachment_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.create_drg_attachment` and waits for the :py:class:`~oci.core.models.DrgAttachment` acted upon
        to enter the given state(s).

        :param CreateDrgAttachmentDetails create_drg_attachment_details: (required)
            Details for creating a `DrgAttachment`.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.DrgAttachment.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.create_drg_attachment`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_drg_attachment(create_drg_attachment_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_drg_attachment(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_internet_gateway_and_wait_for_state(self, create_internet_gateway_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.create_internet_gateway` and waits for the :py:class:`~oci.core.models.InternetGateway` acted upon
        to enter the given state(s).

        :param CreateInternetGatewayDetails create_internet_gateway_details: (required)
            Details for creating a new internet gateway.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.InternetGateway.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.create_internet_gateway`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_internet_gateway(create_internet_gateway_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_internet_gateway(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_ip_sec_connection_and_wait_for_state(self, create_ip_sec_connection_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.create_ip_sec_connection` and waits for the :py:class:`~oci.core.models.IPSecConnection` acted upon
        to enter the given state(s).

        :param CreateIPSecConnectionDetails create_ip_sec_connection_details: (required)
            Details for creating an `IPSecConnection`.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.IPSecConnection.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.create_ip_sec_connection`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_ip_sec_connection(create_ip_sec_connection_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_ip_sec_connection(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_local_peering_gateway_and_wait_for_state(self, create_local_peering_gateway_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.create_local_peering_gateway` and waits for the :py:class:`~oci.core.models.LocalPeeringGateway` acted upon
        to enter the given state(s).

        :param CreateLocalPeeringGatewayDetails create_local_peering_gateway_details: (required)
            Details for creating a new local peering gateway.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.LocalPeeringGateway.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.create_local_peering_gateway`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_local_peering_gateway(create_local_peering_gateway_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_local_peering_gateway(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_nat_gateway_and_wait_for_state(self, create_nat_gateway_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.create_nat_gateway` and waits for the :py:class:`~oci.core.models.NatGateway` acted upon
        to enter the given state(s).

        :param CreateNatGatewayDetails create_nat_gateway_details: (required)
            Details for creating a NAT gateway.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.NatGateway.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.create_nat_gateway`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_nat_gateway(create_nat_gateway_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_nat_gateway(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_public_ip_and_wait_for_state(self, create_public_ip_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.create_public_ip` and waits for the :py:class:`~oci.core.models.PublicIp` acted upon
        to enter the given state(s).

        :param CreatePublicIpDetails create_public_ip_details: (required)
            Create public IP details.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.PublicIp.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.create_public_ip`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_public_ip(create_public_ip_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_public_ip(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_remote_peering_connection_and_wait_for_state(self, create_remote_peering_connection_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.create_remote_peering_connection` and waits for the :py:class:`~oci.core.models.RemotePeeringConnection` acted upon
        to enter the given state(s).

        :param CreateRemotePeeringConnectionDetails create_remote_peering_connection_details: (required)
            Request to create peering connection to remote region

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.RemotePeeringConnection.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.create_remote_peering_connection`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_remote_peering_connection(create_remote_peering_connection_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_remote_peering_connection(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_route_table_and_wait_for_state(self, create_route_table_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.create_route_table` and waits for the :py:class:`~oci.core.models.RouteTable` acted upon
        to enter the given state(s).

        :param CreateRouteTableDetails create_route_table_details: (required)
            Details for creating a new route table.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.RouteTable.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.create_route_table`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_route_table(create_route_table_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_route_table(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_security_list_and_wait_for_state(self, create_security_list_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.create_security_list` and waits for the :py:class:`~oci.core.models.SecurityList` acted upon
        to enter the given state(s).

        :param CreateSecurityListDetails create_security_list_details: (required)
            Details regarding the security list to create.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.SecurityList.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.create_security_list`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_security_list(create_security_list_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_security_list(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_service_gateway_and_wait_for_state(self, create_service_gateway_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.create_service_gateway` and waits for the :py:class:`~oci.core.models.ServiceGateway` acted upon
        to enter the given state(s).

        :param CreateServiceGatewayDetails create_service_gateway_details: (required)
            Details for creating a service gateway.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.ServiceGateway.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.create_service_gateway`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_service_gateway(create_service_gateway_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_service_gateway(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_subnet_and_wait_for_state(self, create_subnet_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.create_subnet` and waits for the :py:class:`~oci.core.models.Subnet` acted upon
        to enter the given state(s).

        :param CreateSubnetDetails create_subnet_details: (required)
            Details for creating a subnet.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.Subnet.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.create_subnet`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_subnet(create_subnet_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_subnet(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_vcn_and_wait_for_state(self, create_vcn_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.create_vcn` and waits for the :py:class:`~oci.core.models.Vcn` acted upon
        to enter the given state(s).

        :param CreateVcnDetails create_vcn_details: (required)
            Details for creating a new VCN.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.Vcn.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.create_vcn`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_vcn(create_vcn_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_vcn(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_virtual_circuit_and_wait_for_state(self, create_virtual_circuit_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.create_virtual_circuit` and waits for the :py:class:`~oci.core.models.VirtualCircuit` acted upon
        to enter the given state(s).

        :param CreateVirtualCircuitDetails create_virtual_circuit_details: (required)
            Details to create a VirtualCircuit.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.VirtualCircuit.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.create_virtual_circuit`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_virtual_circuit(create_virtual_circuit_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_virtual_circuit(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_cross_connect_and_wait_for_state(self, cross_connect_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.delete_cross_connect` and waits for the :py:class:`~oci.core.models.CrossConnect` acted upon
        to enter the given state(s).

        :param str cross_connect_id: (required)
            The OCID of the cross-connect.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.CrossConnect.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.delete_cross_connect`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_cross_connect(cross_connect_id)
        operation_result = self.client.delete_cross_connect(cross_connect_id, **operation_kwargs)
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

    def delete_cross_connect_group_and_wait_for_state(self, cross_connect_group_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.delete_cross_connect_group` and waits for the :py:class:`~oci.core.models.CrossConnectGroup` acted upon
        to enter the given state(s).

        :param str cross_connect_group_id: (required)
            The OCID of the cross-connect group.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.CrossConnectGroup.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.delete_cross_connect_group`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_cross_connect_group(cross_connect_group_id)
        operation_result = self.client.delete_cross_connect_group(cross_connect_group_id, **operation_kwargs)
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

    def delete_dhcp_options_and_wait_for_state(self, dhcp_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.delete_dhcp_options` and waits for the :py:class:`~oci.core.models.DhcpOptions` acted upon
        to enter the given state(s).

        :param str dhcp_id: (required)
            The OCID for the set of DHCP options.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.DhcpOptions.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.delete_dhcp_options`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_dhcp_options(dhcp_id)
        operation_result = self.client.delete_dhcp_options(dhcp_id, **operation_kwargs)
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

    def delete_drg_and_wait_for_state(self, drg_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.delete_drg` and waits for the :py:class:`~oci.core.models.Drg` acted upon
        to enter the given state(s).

        :param str drg_id: (required)
            The OCID of the DRG.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.Drg.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.delete_drg`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_drg(drg_id)
        operation_result = self.client.delete_drg(drg_id, **operation_kwargs)
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

    def delete_drg_attachment_and_wait_for_state(self, drg_attachment_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.delete_drg_attachment` and waits for the :py:class:`~oci.core.models.DrgAttachment` acted upon
        to enter the given state(s).

        :param str drg_attachment_id: (required)
            The OCID of the DRG attachment.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.DrgAttachment.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.delete_drg_attachment`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_drg_attachment(drg_attachment_id)
        operation_result = self.client.delete_drg_attachment(drg_attachment_id, **operation_kwargs)
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

    def delete_internet_gateway_and_wait_for_state(self, ig_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.delete_internet_gateway` and waits for the :py:class:`~oci.core.models.InternetGateway` acted upon
        to enter the given state(s).

        :param str ig_id: (required)
            The OCID of the internet gateway.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.InternetGateway.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.delete_internet_gateway`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_internet_gateway(ig_id)
        operation_result = self.client.delete_internet_gateway(ig_id, **operation_kwargs)
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

    def delete_ip_sec_connection_and_wait_for_state(self, ipsc_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.delete_ip_sec_connection` and waits for the :py:class:`~oci.core.models.IPSecConnection` acted upon
        to enter the given state(s).

        :param str ipsc_id: (required)
            The OCID of the IPSec connection.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.IPSecConnection.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.delete_ip_sec_connection`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_ip_sec_connection(ipsc_id)
        operation_result = self.client.delete_ip_sec_connection(ipsc_id, **operation_kwargs)
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

    def delete_local_peering_gateway_and_wait_for_state(self, local_peering_gateway_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.delete_local_peering_gateway` and waits for the :py:class:`~oci.core.models.LocalPeeringGateway` acted upon
        to enter the given state(s).

        :param str local_peering_gateway_id: (required)
            The OCID of the local peering gateway.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.LocalPeeringGateway.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.delete_local_peering_gateway`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_local_peering_gateway(local_peering_gateway_id)
        operation_result = self.client.delete_local_peering_gateway(local_peering_gateway_id, **operation_kwargs)
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

    def delete_nat_gateway_and_wait_for_state(self, nat_gateway_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.delete_nat_gateway` and waits for the :py:class:`~oci.core.models.NatGateway` acted upon
        to enter the given state(s).

        :param str nat_gateway_id: (required)
            The NAT gateway's `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.NatGateway.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.delete_nat_gateway`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_nat_gateway(nat_gateway_id)
        operation_result = self.client.delete_nat_gateway(nat_gateway_id, **operation_kwargs)
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

    def delete_public_ip_and_wait_for_state(self, public_ip_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.delete_public_ip` and waits for the :py:class:`~oci.core.models.PublicIp` acted upon
        to enter the given state(s).

        :param str public_ip_id: (required)
            The OCID of the public IP.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.PublicIp.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.delete_public_ip`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_public_ip(public_ip_id)
        operation_result = self.client.delete_public_ip(public_ip_id, **operation_kwargs)
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

    def delete_remote_peering_connection_and_wait_for_state(self, remote_peering_connection_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.delete_remote_peering_connection` and waits for the :py:class:`~oci.core.models.RemotePeeringConnection` acted upon
        to enter the given state(s).

        :param str remote_peering_connection_id: (required)
            The OCID of the remote peering connection (RPC).

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.RemotePeeringConnection.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.delete_remote_peering_connection`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_remote_peering_connection(remote_peering_connection_id)
        operation_result = self.client.delete_remote_peering_connection(remote_peering_connection_id, **operation_kwargs)
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

    def delete_route_table_and_wait_for_state(self, rt_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.delete_route_table` and waits for the :py:class:`~oci.core.models.RouteTable` acted upon
        to enter the given state(s).

        :param str rt_id: (required)
            The OCID of the route table.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.RouteTable.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.delete_route_table`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_route_table(rt_id)
        operation_result = self.client.delete_route_table(rt_id, **operation_kwargs)
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

    def delete_security_list_and_wait_for_state(self, security_list_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.delete_security_list` and waits for the :py:class:`~oci.core.models.SecurityList` acted upon
        to enter the given state(s).

        :param str security_list_id: (required)
            The OCID of the security list.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.SecurityList.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.delete_security_list`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_security_list(security_list_id)
        operation_result = self.client.delete_security_list(security_list_id, **operation_kwargs)
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

    def delete_service_gateway_and_wait_for_state(self, service_gateway_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.delete_service_gateway` and waits for the :py:class:`~oci.core.models.ServiceGateway` acted upon
        to enter the given state(s).

        :param str service_gateway_id: (required)
            The service gateway's `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.ServiceGateway.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.delete_service_gateway`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_service_gateway(service_gateway_id)
        operation_result = self.client.delete_service_gateway(service_gateway_id, **operation_kwargs)
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

    def delete_subnet_and_wait_for_state(self, subnet_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.delete_subnet` and waits for the :py:class:`~oci.core.models.Subnet` acted upon
        to enter the given state(s).

        :param str subnet_id: (required)
            The OCID of the subnet.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.Subnet.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.delete_subnet`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_subnet(subnet_id)
        operation_result = self.client.delete_subnet(subnet_id, **operation_kwargs)
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

    def delete_vcn_and_wait_for_state(self, vcn_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.delete_vcn` and waits for the :py:class:`~oci.core.models.Vcn` acted upon
        to enter the given state(s).

        :param str vcn_id: (required)
            The OCID of the VCN.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.Vcn.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.delete_vcn`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_vcn(vcn_id)
        operation_result = self.client.delete_vcn(vcn_id, **operation_kwargs)
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

    def delete_virtual_circuit_and_wait_for_state(self, virtual_circuit_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.delete_virtual_circuit` and waits for the :py:class:`~oci.core.models.VirtualCircuit` acted upon
        to enter the given state(s).

        :param str virtual_circuit_id: (required)
            The OCID of the virtual circuit.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.VirtualCircuit.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.delete_virtual_circuit`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_virtual_circuit(virtual_circuit_id)
        operation_result = self.client.delete_virtual_circuit(virtual_circuit_id, **operation_kwargs)
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

    def detach_service_id_and_wait_for_state(self, service_gateway_id, detach_service_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.detach_service_id` and waits for the :py:class:`~oci.core.models.ServiceGateway` acted upon
        to enter the given state(s).

        :param str service_gateway_id: (required)
            The service gateway's `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param ServiceIdRequestDetails detach_service_details: (required)
            ServiceId of Service to be detached from a service gateway.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.ServiceGateway.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.detach_service_id`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.detach_service_id(service_gateway_id, detach_service_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_service_gateway(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_cross_connect_and_wait_for_state(self, cross_connect_id, update_cross_connect_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.update_cross_connect` and waits for the :py:class:`~oci.core.models.CrossConnect` acted upon
        to enter the given state(s).

        :param str cross_connect_id: (required)
            The OCID of the cross-connect.

        :param UpdateCrossConnectDetails update_cross_connect_details: (required)
            Update CrossConnect fields.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.CrossConnect.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.update_cross_connect`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_cross_connect(cross_connect_id, update_cross_connect_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_cross_connect(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_cross_connect_group_and_wait_for_state(self, cross_connect_group_id, update_cross_connect_group_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.update_cross_connect_group` and waits for the :py:class:`~oci.core.models.CrossConnectGroup` acted upon
        to enter the given state(s).

        :param str cross_connect_group_id: (required)
            The OCID of the cross-connect group.

        :param UpdateCrossConnectGroupDetails update_cross_connect_group_details: (required)
            Update CrossConnectGroup fields

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.CrossConnectGroup.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.update_cross_connect_group`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_cross_connect_group(cross_connect_group_id, update_cross_connect_group_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_cross_connect_group(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_dhcp_options_and_wait_for_state(self, dhcp_id, update_dhcp_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.update_dhcp_options` and waits for the :py:class:`~oci.core.models.DhcpOptions` acted upon
        to enter the given state(s).

        :param str dhcp_id: (required)
            The OCID for the set of DHCP options.

        :param UpdateDhcpDetails update_dhcp_details: (required)
            Request object for updating a set of DHCP options.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.DhcpOptions.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.update_dhcp_options`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_dhcp_options(dhcp_id, update_dhcp_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_dhcp_options(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_drg_and_wait_for_state(self, drg_id, update_drg_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.update_drg` and waits for the :py:class:`~oci.core.models.Drg` acted upon
        to enter the given state(s).

        :param str drg_id: (required)
            The OCID of the DRG.

        :param UpdateDrgDetails update_drg_details: (required)
            Details object for updating a DRG.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.Drg.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.update_drg`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_drg(drg_id, update_drg_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_drg(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_drg_attachment_and_wait_for_state(self, drg_attachment_id, update_drg_attachment_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.update_drg_attachment` and waits for the :py:class:`~oci.core.models.DrgAttachment` acted upon
        to enter the given state(s).

        :param str drg_attachment_id: (required)
            The OCID of the DRG attachment.

        :param UpdateDrgAttachmentDetails update_drg_attachment_details: (required)
            Details object for updating a `DrgAttachment`.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.DrgAttachment.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.update_drg_attachment`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_drg_attachment(drg_attachment_id, update_drg_attachment_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_drg_attachment(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_internet_gateway_and_wait_for_state(self, ig_id, update_internet_gateway_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.update_internet_gateway` and waits for the :py:class:`~oci.core.models.InternetGateway` acted upon
        to enter the given state(s).

        :param str ig_id: (required)
            The OCID of the internet gateway.

        :param UpdateInternetGatewayDetails update_internet_gateway_details: (required)
            Details for updating the internet gateway.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.InternetGateway.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.update_internet_gateway`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_internet_gateway(ig_id, update_internet_gateway_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_internet_gateway(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_ip_sec_connection_and_wait_for_state(self, ipsc_id, update_ip_sec_connection_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.update_ip_sec_connection` and waits for the :py:class:`~oci.core.models.IPSecConnection` acted upon
        to enter the given state(s).

        :param str ipsc_id: (required)
            The OCID of the IPSec connection.

        :param UpdateIPSecConnectionDetails update_ip_sec_connection_details: (required)
            Details object for updating a IPSec connection.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.IPSecConnection.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.update_ip_sec_connection`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_ip_sec_connection(ipsc_id, update_ip_sec_connection_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_ip_sec_connection(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_local_peering_gateway_and_wait_for_state(self, local_peering_gateway_id, update_local_peering_gateway_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.update_local_peering_gateway` and waits for the :py:class:`~oci.core.models.LocalPeeringGateway` acted upon
        to enter the given state(s).

        :param str local_peering_gateway_id: (required)
            The OCID of the local peering gateway.

        :param UpdateLocalPeeringGatewayDetails update_local_peering_gateway_details: (required)
            Details object for updating a local peering gateway.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.LocalPeeringGateway.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.update_local_peering_gateway`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_local_peering_gateway(local_peering_gateway_id, update_local_peering_gateway_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_local_peering_gateway(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_nat_gateway_and_wait_for_state(self, nat_gateway_id, update_nat_gateway_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.update_nat_gateway` and waits for the :py:class:`~oci.core.models.NatGateway` acted upon
        to enter the given state(s).

        :param str nat_gateway_id: (required)
            The NAT gateway's `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param UpdateNatGatewayDetails update_nat_gateway_details: (required)
            Details object for updating a NAT gateway.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.NatGateway.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.update_nat_gateway`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_nat_gateway(nat_gateway_id, update_nat_gateway_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_nat_gateway(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_public_ip_and_wait_for_state(self, public_ip_id, update_public_ip_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.update_public_ip` and waits for the :py:class:`~oci.core.models.PublicIp` acted upon
        to enter the given state(s).

        :param str public_ip_id: (required)
            The OCID of the public IP.

        :param UpdatePublicIpDetails update_public_ip_details: (required)
            Public IP details.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.PublicIp.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.update_public_ip`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_public_ip(public_ip_id, update_public_ip_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_public_ip(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_remote_peering_connection_and_wait_for_state(self, remote_peering_connection_id, update_remote_peering_connection_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.update_remote_peering_connection` and waits for the :py:class:`~oci.core.models.RemotePeeringConnection` acted upon
        to enter the given state(s).

        :param str remote_peering_connection_id: (required)
            The OCID of the remote peering connection (RPC).

        :param UpdateRemotePeeringConnectionDetails update_remote_peering_connection_details: (required)
            Request to the update the peering connection to remote region

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.RemotePeeringConnection.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.update_remote_peering_connection`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_remote_peering_connection(remote_peering_connection_id, update_remote_peering_connection_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_remote_peering_connection(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_route_table_and_wait_for_state(self, rt_id, update_route_table_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.update_route_table` and waits for the :py:class:`~oci.core.models.RouteTable` acted upon
        to enter the given state(s).

        :param str rt_id: (required)
            The OCID of the route table.

        :param UpdateRouteTableDetails update_route_table_details: (required)
            Details object for updating a route table.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.RouteTable.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.update_route_table`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_route_table(rt_id, update_route_table_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_route_table(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_security_list_and_wait_for_state(self, security_list_id, update_security_list_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.update_security_list` and waits for the :py:class:`~oci.core.models.SecurityList` acted upon
        to enter the given state(s).

        :param str security_list_id: (required)
            The OCID of the security list.

        :param UpdateSecurityListDetails update_security_list_details: (required)
            Updated details for the security list.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.SecurityList.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.update_security_list`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_security_list(security_list_id, update_security_list_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_security_list(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_service_gateway_and_wait_for_state(self, service_gateway_id, update_service_gateway_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.update_service_gateway` and waits for the :py:class:`~oci.core.models.ServiceGateway` acted upon
        to enter the given state(s).

        :param str service_gateway_id: (required)
            The service gateway's `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param UpdateServiceGatewayDetails update_service_gateway_details: (required)
            Details object for updating a service gateway.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.ServiceGateway.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.update_service_gateway`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_service_gateway(service_gateway_id, update_service_gateway_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_service_gateway(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_subnet_and_wait_for_state(self, subnet_id, update_subnet_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.update_subnet` and waits for the :py:class:`~oci.core.models.Subnet` acted upon
        to enter the given state(s).

        :param str subnet_id: (required)
            The OCID of the subnet.

        :param UpdateSubnetDetails update_subnet_details: (required)
            Details object for updating a subnet.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.Subnet.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.update_subnet`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_subnet(subnet_id, update_subnet_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_subnet(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_vcn_and_wait_for_state(self, vcn_id, update_vcn_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.update_vcn` and waits for the :py:class:`~oci.core.models.Vcn` acted upon
        to enter the given state(s).

        :param str vcn_id: (required)
            The OCID of the VCN.

        :param UpdateVcnDetails update_vcn_details: (required)
            Details object for updating a VCN.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.Vcn.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.update_vcn`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_vcn(vcn_id, update_vcn_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_vcn(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_virtual_circuit_and_wait_for_state(self, virtual_circuit_id, update_virtual_circuit_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.update_virtual_circuit` and waits for the :py:class:`~oci.core.models.VirtualCircuit` acted upon
        to enter the given state(s).

        :param str virtual_circuit_id: (required)
            The OCID of the virtual circuit.

        :param UpdateVirtualCircuitDetails update_virtual_circuit_details: (required)
            Update VirtualCircuit fields.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.VirtualCircuit.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.update_virtual_circuit`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_virtual_circuit(virtual_circuit_id, update_virtual_circuit_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_virtual_circuit(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_vnic_and_wait_for_state(self, vnic_id, update_vnic_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.core.VirtualNetworkClient.update_vnic` and waits for the :py:class:`~oci.core.models.Vnic` acted upon
        to enter the given state(s).

        :param str vnic_id: (required)
            The OCID of the VNIC.

        :param UpdateVnicDetails update_vnic_details: (required)
            Details object for updating a VNIC.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.core.models.Vnic.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.core.VirtualNetworkClient.update_vnic`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_vnic(vnic_id, update_vnic_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_vnic(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
