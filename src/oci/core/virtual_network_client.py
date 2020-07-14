# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from oci._vendor import requests  # noqa: F401
from oci._vendor import six

from oci import retry  # noqa: F401
from oci.base_client import BaseClient
from oci.config import get_config_value_or_default, validate_config
from oci.signer import Signer
from oci.util import Sentinel
from .models import core_type_mapping
missing = Sentinel("Missing")


class VirtualNetworkClient(object):
    """
    API covering the [Networking](/iaas/Content/Network/Concepts/overview.htm),
    [Compute](/iaas/Content/Compute/Concepts/computeoverview.htm), and
    [Block Volume](/iaas/Content/Block/Concepts/overview.htm) services. Use this API
    to manage resources such as virtual cloud networks (VCNs), compute instances, and
    block storage volumes.
    """

    def __init__(self, config, **kwargs):
        """
        Creates a new service client

        :param dict config:
            Configuration keys and values as per `SDK and Tool Configuration <https://docs.cloud.oracle.com/Content/API/Concepts/sdkconfig.htm>`__.
            The :py:meth:`~oci.config.from_file` method can be used to load configuration from a file. Alternatively, a ``dict`` can be passed. You can validate_config
            the dict using :py:meth:`~oci.config.validate_config`

        :param str service_endpoint: (optional)
            The endpoint of the service to call using this client. For example ``https://iaas.us-ashburn-1.oraclecloud.com``. If this keyword argument is
            not provided then it will be derived using the region in the config parameter. You should only provide this keyword argument if you have an explicit
            need to specify a service endpoint.

        :param timeout: (optional)
            The connection and read timeouts for the client. The default values are connection timeout 10 seconds and read timeout 60 seconds. This keyword argument can be provided
            as a single float, in which case the value provided is used for both the read and connection timeouts, or as a tuple of two floats. If
            a tuple is provided then the first value is used as the connection timeout and the second value as the read timeout.
        :type timeout: float or tuple(float, float)

        :param signer: (optional)
            The signer to use when signing requests made by the service client. The default is to use a :py:class:`~oci.signer.Signer` based on the values
            provided in the config parameter.

            One use case for this parameter is for `Instance Principals authentication <https://docs.cloud.oracle.com/Content/Identity/Tasks/callingservicesfrominstances.htm>`__
            by passing an instance of :py:class:`~oci.auth.signers.InstancePrincipalsSecurityTokenSigner` as the value for this keyword argument
        :type signer: :py:class:`~oci.signer.AbstractBaseSigner`

        :param obj retry_strategy: (optional)
            A retry strategy to apply to all calls made by this service client (i.e. at the client level). There is no retry strategy applied by default.
            Retry strategies can also be applied at the operation level by passing a ``retry_strategy`` keyword argument as part of calling the operation.
            Any value provided at the operation level will override whatever is specified at the client level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.
        """
        validate_config(config, signer=kwargs.get('signer'))
        if 'signer' in kwargs:
            signer = kwargs['signer']
        else:
            signer = Signer(
                tenancy=config["tenancy"],
                user=config["user"],
                fingerprint=config["fingerprint"],
                private_key_file_location=config.get("key_file"),
                pass_phrase=get_config_value_or_default(config, "pass_phrase"),
                private_key_content=config.get("key_content")
            )

        base_client_init_kwargs = {
            'regional_client': True,
            'service_endpoint': kwargs.get('service_endpoint'),
            'timeout': kwargs.get('timeout'),
            'base_path': '/20160918',
            'service_endpoint_template': 'https://iaas.{region}.{secondLevelDomain}',
            'skip_deserialization': kwargs.get('skip_deserialization', False)
        }
        self.base_client = BaseClient("virtual_network", config, signer, core_type_mapping, **base_client_init_kwargs)
        self.retry_strategy = kwargs.get('retry_strategy')
        self._config = config
        self._kwargs = kwargs

    def add_network_security_group_security_rules(self, network_security_group_id, add_network_security_group_security_rules_details, **kwargs):
        """
        Adds one or more security rules to the specified network security group.


        :param str network_security_group_id: (required)
            The `OCID`__ of the network security group.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param AddNetworkSecurityGroupSecurityRulesDetails add_network_security_group_security_rules_details: (required)
            Request with one or more security rules to be associated with the network security group.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.AddedNetworkSecurityGroupSecurityRules`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/networkSecurityGroups/{networkSecurityGroupId}/actions/addSecurityRules"
        method = "POST"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "add_network_security_group_security_rules got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "networkSecurityGroupId": network_security_group_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=add_network_security_group_security_rules_details,
                response_type="AddedNetworkSecurityGroupSecurityRules")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=add_network_security_group_security_rules_details,
                response_type="AddedNetworkSecurityGroupSecurityRules")

    def attach_service_id(self, service_gateway_id, attach_service_details, **kwargs):
        """
        Adds the specified :class:`Service` to the list of enabled
        `Service` objects for the specified gateway. You must also set up a route rule with the
        `cidrBlock` of the `Service` as the rule's destination and the service gateway as the rule's
        target. See :class:`RouteTable`.

        **Note:** The `AttachServiceId` operation is an easy way to add an individual `Service` to
        the service gateway. Compare it with
        :func:`update_service_gateway`, which replaces
        the entire existing list of enabled `Service` objects with the list that you provide in the
        `Update` call.


        :param str service_gateway_id: (required)
            The service gateway's `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param ServiceIdRequestDetails attach_service_details: (required)
            ServiceId of Service to be attached to a service gateway.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.ServiceGateway`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/serviceGateways/{serviceGatewayId}/actions/attachService"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "attach_service_id got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "serviceGatewayId": service_gateway_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=attach_service_details,
                response_type="ServiceGateway")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=attach_service_details,
                response_type="ServiceGateway")

    def bulk_add_virtual_circuit_public_prefixes(self, virtual_circuit_id, bulk_add_virtual_circuit_public_prefixes_details, **kwargs):
        """
        Adds one or more customer public IP prefixes to the specified public virtual circuit.
        Use this operation (and not :func:`update_virtual_circuit`)
        to add prefixes to the virtual circuit. Oracle must verify the customer's ownership
        of each prefix before traffic for that prefix will flow across the virtual circuit.


        :param str virtual_circuit_id: (required)
            The OCID of the virtual circuit.

        :param BulkAddVirtualCircuitPublicPrefixesDetails bulk_add_virtual_circuit_public_prefixes_details: (required)
            Request with publix prefixes to be added to the virtual circuit

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/virtualCircuits/{virtualCircuitId}/actions/bulkAddPublicPrefixes"
        method = "POST"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "bulk_add_virtual_circuit_public_prefixes got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "virtualCircuitId": virtual_circuit_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=bulk_add_virtual_circuit_public_prefixes_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=bulk_add_virtual_circuit_public_prefixes_details)

    def bulk_delete_virtual_circuit_public_prefixes(self, virtual_circuit_id, bulk_delete_virtual_circuit_public_prefixes_details, **kwargs):
        """
        Removes one or more customer public IP prefixes from the specified public virtual circuit.
        Use this operation (and not :func:`update_virtual_circuit`)
        to remove prefixes from the virtual circuit. When the virtual circuit's state switches
        back to PROVISIONED, Oracle stops advertising the specified prefixes across the connection.


        :param str virtual_circuit_id: (required)
            The OCID of the virtual circuit.

        :param BulkDeleteVirtualCircuitPublicPrefixesDetails bulk_delete_virtual_circuit_public_prefixes_details: (required)
            Request with publix prefixes to be deleted from the virtual circuit

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/virtualCircuits/{virtualCircuitId}/actions/bulkDeletePublicPrefixes"
        method = "POST"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "bulk_delete_virtual_circuit_public_prefixes got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "virtualCircuitId": virtual_circuit_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=bulk_delete_virtual_circuit_public_prefixes_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=bulk_delete_virtual_circuit_public_prefixes_details)

    def change_cpe_compartment(self, cpe_id, change_cpe_compartment_details, **kwargs):
        """
        Moves a CPE object into a different compartment within the same tenancy. For information
        about moving resources between compartments, see
        `Moving Resources to a Different Compartment`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes


        :param str cpe_id: (required)
            The OCID of the CPE.

        :param ChangeCpeCompartmentDetails change_cpe_compartment_details: (required)
            Request to change the compartment of a CPE.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/cpes/{cpeId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_cpe_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "cpeId": cpe_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_cpe_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_cpe_compartment_details)

    def change_cross_connect_compartment(self, cross_connect_id, change_cross_connect_compartment_details, **kwargs):
        """
        Moves a cross-connect into a different compartment within the same tenancy. For information
        about moving resources between compartments, see
        `Moving Resources to a Different Compartment`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes


        :param str cross_connect_id: (required)
            The OCID of the cross-connect.

        :param ChangeCrossConnectCompartmentDetails change_cross_connect_compartment_details: (required)
            Request to change the compartment of a Cross Connect.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/crossConnects/{crossConnectId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_cross_connect_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "crossConnectId": cross_connect_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_cross_connect_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_cross_connect_compartment_details)

    def change_cross_connect_group_compartment(self, cross_connect_group_id, change_cross_connect_group_compartment_details, **kwargs):
        """
        Moves a cross-connect group into a different compartment within the same tenancy. For information
        about moving resources between compartments, see
        `Moving Resources to a Different Compartment`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes


        :param str cross_connect_group_id: (required)
            The OCID of the cross-connect group.

        :param ChangeCrossConnectGroupCompartmentDetails change_cross_connect_group_compartment_details: (required)
            Request to change the compartment of a Cross Connect Group.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/crossConnectGroups/{crossConnectGroupId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_cross_connect_group_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "crossConnectGroupId": cross_connect_group_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_cross_connect_group_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_cross_connect_group_compartment_details)

    def change_dhcp_options_compartment(self, dhcp_id, change_dhcp_options_compartment_details, **kwargs):
        """
        Moves a set of DHCP options into a different compartment within the same tenancy. For information
        about moving resources between compartments, see
        `Moving Resources to a Different Compartment`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes


        :param str dhcp_id: (required)
            The OCID for the set of DHCP options.

        :param ChangeDhcpOptionsCompartmentDetails change_dhcp_options_compartment_details: (required)
            Request to change the compartment of a set of DHCP Options.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dhcps/{dhcpId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_dhcp_options_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dhcpId": dhcp_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_dhcp_options_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_dhcp_options_compartment_details)

    def change_drg_compartment(self, drg_id, change_drg_compartment_details, **kwargs):
        """
        Moves a DRG into a different compartment within the same tenancy. For information
        about moving resources between compartments, see
        `Moving Resources to a Different Compartment`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes


        :param str drg_id: (required)
            The OCID of the DRG.

        :param ChangeDrgCompartmentDetails change_drg_compartment_details: (required)
            Request to change the compartment of a DRG.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/drgs/{drgId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_drg_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "drgId": drg_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_drg_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_drg_compartment_details)

    def change_internet_gateway_compartment(self, ig_id, change_internet_gateway_compartment_details, **kwargs):
        """
        Moves an internet gateway into a different compartment within the same tenancy. For information
        about moving resources between compartments, see
        `Moving Resources to a Different Compartment`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes


        :param str ig_id: (required)
            The OCID of the internet gateway.

        :param ChangeInternetGatewayCompartmentDetails change_internet_gateway_compartment_details: (required)
            Request to change the compartment of an internet gateway.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/internetGateways/{igId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_internet_gateway_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "igId": ig_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_internet_gateway_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_internet_gateway_compartment_details)

    def change_ip_sec_connection_compartment(self, ipsc_id, change_ip_sec_connection_compartment_details, **kwargs):
        """
        Moves an IPSec connection into a different compartment within the same tenancy. For information
        about moving resources between compartments, see
        `Moving Resources to a Different Compartment`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes


        :param str ipsc_id: (required)
            The OCID of the IPSec connection.

        :param ChangeIPSecConnectionCompartmentDetails change_ip_sec_connection_compartment_details: (required)
            Request to change the compartment of a Ipsec Connection.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/ipsecConnections/{ipscId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_ip_sec_connection_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "ipscId": ipsc_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_ip_sec_connection_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_ip_sec_connection_compartment_details)

    def change_local_peering_gateway_compartment(self, local_peering_gateway_id, change_local_peering_gateway_compartment_details, **kwargs):
        """
        Moves a local peering gateway into a different compartment within the same tenancy. For information
        about moving resources between compartments, see
        `Moving Resources to a Different Compartment`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes


        :param str local_peering_gateway_id: (required)
            The OCID of the local peering gateway.

        :param ChangeLocalPeeringGatewayCompartmentDetails change_local_peering_gateway_compartment_details: (required)
            Request to change the compartment of a given local peering gateway.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/localPeeringGateways/{localPeeringGatewayId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_local_peering_gateway_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "localPeeringGatewayId": local_peering_gateway_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_local_peering_gateway_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_local_peering_gateway_compartment_details)

    def change_nat_gateway_compartment(self, nat_gateway_id, change_nat_gateway_compartment_details, **kwargs):
        """
        Moves a NAT gateway into a different compartment within the same tenancy. For information
        about moving resources between compartments, see
        `Moving Resources to a Different Compartment`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes


        :param str nat_gateway_id: (required)
            The NAT gateway's `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param ChangeNatGatewayCompartmentDetails change_nat_gateway_compartment_details: (required)
            Request to change the compartment of a given NAT Gateway.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/natGateways/{natGatewayId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_nat_gateway_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "natGatewayId": nat_gateway_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_nat_gateway_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_nat_gateway_compartment_details)

    def change_network_security_group_compartment(self, network_security_group_id, change_network_security_group_compartment_details, **kwargs):
        """
        Moves a network security group into a different compartment within the same tenancy. For
        information about moving resources between compartments, see `Moving Resources to a Different Compartment`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes


        :param str network_security_group_id: (required)
            The `OCID`__ of the network security group.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param ChangeNetworkSecurityGroupCompartmentDetails change_network_security_group_compartment_details: (required)
            Request to change the compartment of a network security group.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/networkSecurityGroups/{networkSecurityGroupId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_network_security_group_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "networkSecurityGroupId": network_security_group_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_network_security_group_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_network_security_group_compartment_details)

    def change_public_ip_compartment(self, public_ip_id, change_public_ip_compartment_details, **kwargs):
        """
        Moves a public IP into a different compartment within the same tenancy. For information
        about moving resources between compartments, see
        `Moving Resources to a Different Compartment`__.

        This operation applies only to reserved public IPs. Ephemeral public IPs always belong to the
        same compartment as their VNIC and move accordingly.

        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes


        :param str public_ip_id: (required)
            The OCID of the public IP.

        :param ChangePublicIpCompartmentDetails change_public_ip_compartment_details: (required)
            Request to change the compartment of a Public IP.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/publicIps/{publicIpId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_public_ip_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "publicIpId": public_ip_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_public_ip_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_public_ip_compartment_details)

    def change_remote_peering_connection_compartment(self, remote_peering_connection_id, change_remote_peering_connection_compartment_details, **kwargs):
        """
        Moves a remote peering connection (RPC) into a different compartment within the same tenancy. For information
        about moving resources between compartments, see
        `Moving Resources to a Different Compartment`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes


        :param str remote_peering_connection_id: (required)
            The OCID of the remote peering connection (RPC).

        :param ChangeRemotePeeringConnectionCompartmentDetails change_remote_peering_connection_compartment_details: (required)
            Request to change the compartment of a Remote Peering Connection.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/remotePeeringConnections/{remotePeeringConnectionId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_remote_peering_connection_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "remotePeeringConnectionId": remote_peering_connection_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_remote_peering_connection_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_remote_peering_connection_compartment_details)

    def change_route_table_compartment(self, rt_id, change_route_table_compartment_details, **kwargs):
        """
        Moves a route table into a different compartment within the same tenancy. For information
        about moving resources between compartments, see
        `Moving Resources to a Different Compartment`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes


        :param str rt_id: (required)
            The OCID of the route table.

        :param ChangeRouteTableCompartmentDetails change_route_table_compartment_details: (required)
            Request to change the compartment of a given route table.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/routeTables/{rtId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_route_table_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "rtId": rt_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_route_table_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_route_table_compartment_details)

    def change_security_list_compartment(self, security_list_id, change_security_list_compartment_details, **kwargs):
        """
        Moves a security list into a different compartment within the same tenancy. For information
        about moving resources between compartments, see
        `Moving Resources to a Different Compartment`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes


        :param str security_list_id: (required)
            The OCID of the security list.

        :param ChangeSecurityListCompartmentDetails change_security_list_compartment_details: (required)
            Request to change the compartment of a given security list.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/securityLists/{securityListId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_security_list_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "securityListId": security_list_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_security_list_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_security_list_compartment_details)

    def change_service_gateway_compartment(self, service_gateway_id, change_service_gateway_compartment_details, **kwargs):
        """
        Moves a service gateway into a different compartment within the same tenancy. For information
        about moving resources between compartments, see
        `Moving Resources to a Different Compartment`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes


        :param str service_gateway_id: (required)
            The service gateway's `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param ChangeServiceGatewayCompartmentDetails change_service_gateway_compartment_details: (required)
            Request to change the compartment of a given Service Gateway.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/serviceGateways/{serviceGatewayId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_service_gateway_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "serviceGatewayId": service_gateway_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_service_gateway_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_service_gateway_compartment_details)

    def change_subnet_compartment(self, subnet_id, change_subnet_compartment_details, **kwargs):
        """
        Moves a subnet into a different compartment within the same tenancy. For information
        about moving resources between compartments, see
        `Moving Resources to a Different Compartment`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes


        :param str subnet_id: (required)
            The OCID of the subnet.

        :param ChangeSubnetCompartmentDetails change_subnet_compartment_details: (required)
            Request to change the compartment of a given subnet.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/subnets/{subnetId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_subnet_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "subnetId": subnet_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_subnet_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_subnet_compartment_details)

    def change_vcn_compartment(self, vcn_id, change_vcn_compartment_details, **kwargs):
        """
        Moves a VCN into a different compartment within the same tenancy. For information
        about moving resources between compartments, see
        `Moving Resources to a Different Compartment`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes


        :param str vcn_id: (required)
            The `OCID`__ of the VCN.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param ChangeVcnCompartmentDetails change_vcn_compartment_details: (required)
            Request to change the compartment of a given VCN.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/vcns/{vcnId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_vcn_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "vcnId": vcn_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_vcn_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_vcn_compartment_details)

    def change_virtual_circuit_compartment(self, virtual_circuit_id, change_virtual_circuit_compartment_details, **kwargs):
        """
        Moves a virtual circuit into a different compartment within the same tenancy. For information
        about moving resources between compartments, see
        `Moving Resources to a Different Compartment`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes


        :param str virtual_circuit_id: (required)
            The OCID of the virtual circuit.

        :param ChangeVirtualCircuitCompartmentDetails change_virtual_circuit_compartment_details: (required)
            Request to change the compartment of a virtual circuit.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/virtualCircuits/{virtualCircuitId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_virtual_circuit_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "virtualCircuitId": virtual_circuit_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_virtual_circuit_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_virtual_circuit_compartment_details)

    def change_vlan_compartment(self, vlan_id, change_vlan_compartment_details, **kwargs):
        """
        Moves a VLAN into a different compartment within the same tenancy.
        For information about moving resources between compartments, see
        `Moving Resources to a Different Compartment`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes


        :param str vlan_id: (required)
            The `OCID`__ of the VLAN.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param ChangeVlanCompartmentDetails change_vlan_compartment_details: (required)
            Request to change the compartment of a given VLAN.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/vlans/{vlanId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_vlan_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "vlanId": vlan_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_vlan_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_vlan_compartment_details)

    def connect_local_peering_gateways(self, local_peering_gateway_id, connect_local_peering_gateways_details, **kwargs):
        """
        Connects this local peering gateway (LPG) to another one in the same region.

        This operation must be called by the VCN administrator who is designated as
        the *requestor* in the peering relationship. The *acceptor* must implement
        an Identity and Access Management (IAM) policy that gives the requestor permission
        to connect to LPGs in the acceptor's compartment. Without that permission, this
        operation will fail. For more information, see
        `VCN Peering`__.

        __ https://docs.cloud.oracle.com/Content/Network/Tasks/VCNpeering.htm


        :param str local_peering_gateway_id: (required)
            The OCID of the local peering gateway.

        :param ConnectLocalPeeringGatewaysDetails connect_local_peering_gateways_details: (required)
            Details regarding the local peering gateway to connect.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/localPeeringGateways/{localPeeringGatewayId}/actions/connect"
        method = "POST"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "connect_local_peering_gateways got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "localPeeringGatewayId": local_peering_gateway_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=connect_local_peering_gateways_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=connect_local_peering_gateways_details)

    def connect_remote_peering_connections(self, remote_peering_connection_id, connect_remote_peering_connections_details, **kwargs):
        """
        Connects this RPC to another one in a different region.

        This operation must be called by the VCN administrator who is designated as
        the *requestor* in the peering relationship. The *acceptor* must implement
        an Identity and Access Management (IAM) policy that gives the requestor permission
        to connect to RPCs in the acceptor's compartment. Without that permission, this
        operation will fail. For more information, see
        `VCN Peering`__.

        __ https://docs.cloud.oracle.com/Content/Network/Tasks/VCNpeering.htm


        :param str remote_peering_connection_id: (required)
            The OCID of the remote peering connection (RPC).

        :param ConnectRemotePeeringConnectionsDetails connect_remote_peering_connections_details: (required)
            Details to connect peering connection with peering connection from remote region

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/remotePeeringConnections/{remotePeeringConnectionId}/actions/connect"
        method = "POST"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "connect_remote_peering_connections got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "remotePeeringConnectionId": remote_peering_connection_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=connect_remote_peering_connections_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=connect_remote_peering_connections_details)

    def create_cpe(self, create_cpe_details, **kwargs):
        """
        Creates a new virtual customer-premises equipment (CPE) object in the specified compartment. For
        more information, see `IPSec VPNs`__.

        For the purposes of access control, you must provide the OCID of the compartment where you want
        the CPE to reside. Notice that the CPE doesn't have to be in the same compartment as the IPSec
        connection or other Networking Service components. If you're not sure which compartment to
        use, put the CPE in the same compartment as the DRG. For more information about
        compartments and access control, see `Overview of the IAM Service`__.
        For information about OCIDs, see `Resource Identifiers`__.

        You must provide the public IP address of your on-premises router. See
        `Configuring Your On-Premises Router for an IPSec VPN`__.

        You may optionally specify a *display name* for the CPE, otherwise a default is provided. It does not have to
        be unique, and you can change it. Avoid entering confidential information.

        __ https://docs.cloud.oracle.com/Content/Network/Tasks/managingIPsec.htm
        __ https://docs.cloud.oracle.com/Content/Identity/Concepts/overview.htm
        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Tasks/configuringCPE.htm


        :param CreateCpeDetails create_cpe_details: (required)
            Details for creating a CPE.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.Cpe`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/cpes"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_cpe got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_cpe_details,
                response_type="Cpe")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_cpe_details,
                response_type="Cpe")

    def create_cross_connect(self, create_cross_connect_details, **kwargs):
        """
        Creates a new cross-connect. Oracle recommends you create each cross-connect in a
        :class:`CrossConnectGroup` so you can use link aggregation
        with the connection.

        After creating the `CrossConnect` object, you need to go the FastConnect location
        and request to have the physical cable installed. For more information, see
        `FastConnect Overview`__.

        For the purposes of access control, you must provide the OCID of the
        compartment where you want the cross-connect to reside. If you're
        not sure which compartment to use, put the cross-connect in the
        same compartment with your VCN. For more information about
        compartments and access control, see
        `Overview of the IAM Service`__.
        For information about OCIDs, see
        `Resource Identifiers`__.

        You may optionally specify a *display name* for the cross-connect.
        It does not have to be unique, and you can change it. Avoid entering confidential information.

        __ https://docs.cloud.oracle.com/Content/Network/Concepts/fastconnect.htm
        __ https://docs.cloud.oracle.com/Content/Identity/Concepts/overview.htm
        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param CreateCrossConnectDetails create_cross_connect_details: (required)
            Details to create a CrossConnect

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.CrossConnect`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/crossConnects"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_cross_connect got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_cross_connect_details,
                response_type="CrossConnect")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_cross_connect_details,
                response_type="CrossConnect")

    def create_cross_connect_group(self, create_cross_connect_group_details, **kwargs):
        """
        Creates a new cross-connect group to use with Oracle Cloud Infrastructure
        FastConnect. For more information, see
        `FastConnect Overview`__.

        For the purposes of access control, you must provide the OCID of the
        compartment where you want the cross-connect group to reside. If you're
        not sure which compartment to use, put the cross-connect group in the
        same compartment with your VCN. For more information about
        compartments and access control, see
        `Overview of the IAM Service`__.
        For information about OCIDs, see
        `Resource Identifiers`__.

        You may optionally specify a *display name* for the cross-connect group.
        It does not have to be unique, and you can change it. Avoid entering confidential information.

        __ https://docs.cloud.oracle.com/Content/Network/Concepts/fastconnect.htm
        __ https://docs.cloud.oracle.com/Content/Identity/Concepts/overview.htm
        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param CreateCrossConnectGroupDetails create_cross_connect_group_details: (required)
            Details to create a CrossConnectGroup

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.CrossConnectGroup`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/crossConnectGroups"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_cross_connect_group got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_cross_connect_group_details,
                response_type="CrossConnectGroup")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_cross_connect_group_details,
                response_type="CrossConnectGroup")

    def create_dhcp_options(self, create_dhcp_details, **kwargs):
        """
        Creates a new set of DHCP options for the specified VCN. For more information, see
        :class:`DhcpOptions`.

        For the purposes of access control, you must provide the OCID of the compartment where you want the set of
        DHCP options to reside. Notice that the set of options doesn't have to be in the same compartment as the VCN,
        subnets, or other Networking Service components. If you're not sure which compartment to use, put the set
        of DHCP options in the same compartment as the VCN. For more information about compartments and access control, see
        `Overview of the IAM Service`__. For information about OCIDs, see
        `Resource Identifiers`__.

        You may optionally specify a *display name* for the set of DHCP options, otherwise a default is provided.
        It does not have to be unique, and you can change it. Avoid entering confidential information.

        __ https://docs.cloud.oracle.com/Content/Identity/Concepts/overview.htm
        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param CreateDhcpDetails create_dhcp_details: (required)
            Request object for creating a new set of DHCP options.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.DhcpOptions`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dhcps"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_dhcp_options got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_dhcp_details,
                response_type="DhcpOptions")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_dhcp_details,
                response_type="DhcpOptions")

    def create_drg(self, create_drg_details, **kwargs):
        """
        Creates a new dynamic routing gateway (DRG) in the specified compartment. For more information,
        see `Dynamic Routing Gateways (DRGs)`__.

        For the purposes of access control, you must provide the OCID of the compartment where you want
        the DRG to reside. Notice that the DRG doesn't have to be in the same compartment as the VCN,
        the DRG attachment, or other Networking Service components. If you're not sure which compartment
        to use, put the DRG in the same compartment as the VCN. For more information about compartments
        and access control, see `Overview of the IAM Service`__.
        For information about OCIDs, see `Resource Identifiers`__.

        You may optionally specify a *display name* for the DRG, otherwise a default is provided.
        It does not have to be unique, and you can change it. Avoid entering confidential information.

        __ https://docs.cloud.oracle.com/Content/Network/Tasks/managingDRGs.htm
        __ https://docs.cloud.oracle.com/Content/Identity/Concepts/overview.htm
        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param CreateDrgDetails create_drg_details: (required)
            Details for creating a DRG.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.Drg`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/drgs"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_drg got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_drg_details,
                response_type="Drg")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_drg_details,
                response_type="Drg")

    def create_drg_attachment(self, create_drg_attachment_details, **kwargs):
        """
        Attaches the specified DRG to the specified VCN. A VCN can be attached to only one DRG at a time,
        and vice versa. The response includes a `DrgAttachment` object with its own OCID. For more
        information about DRGs, see
        `Dynamic Routing Gateways (DRGs)`__.

        You may optionally specify a *display name* for the attachment, otherwise a default is provided.
        It does not have to be unique, and you can change it. Avoid entering confidential information.

        For the purposes of access control, the DRG attachment is automatically placed into the same compartment
        as the VCN. For more information about compartments and access control, see
        `Overview of the IAM Service`__.

        __ https://docs.cloud.oracle.com/Content/Network/Tasks/managingDRGs.htm
        __ https://docs.cloud.oracle.com/Content/Identity/Concepts/overview.htm


        :param CreateDrgAttachmentDetails create_drg_attachment_details: (required)
            Details for creating a `DrgAttachment`.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.DrgAttachment`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/drgAttachments"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_drg_attachment got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_drg_attachment_details,
                response_type="DrgAttachment")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_drg_attachment_details,
                response_type="DrgAttachment")

    def create_internet_gateway(self, create_internet_gateway_details, **kwargs):
        """
        Creates a new internet gateway for the specified VCN. For more information, see
        `Access to the Internet`__.

        For the purposes of access control, you must provide the OCID of the compartment where you want the Internet
        Gateway to reside. Notice that the internet gateway doesn't have to be in the same compartment as the VCN or
        other Networking Service components. If you're not sure which compartment to use, put the Internet
        Gateway in the same compartment with the VCN. For more information about compartments and access control, see
        `Overview of the IAM Service`__. For information about OCIDs, see
        `Resource Identifiers`__.

        You may optionally specify a *display name* for the internet gateway, otherwise a default is provided. It
        does not have to be unique, and you can change it. Avoid entering confidential information.

        For traffic to flow between a subnet and an internet gateway, you must create a route rule accordingly in
        the subnet's route table (for example, 0.0.0.0/0 > internet gateway). See
        :func:`update_route_table`.

        You must specify whether the internet gateway is enabled when you create it. If it's disabled, that means no
        traffic will flow to/from the internet even if there's a route rule that enables that traffic. You can later
        use :func:`update_internet_gateway` to easily disable/enable
        the gateway without changing the route rule.

        __ https://docs.cloud.oracle.com/Content/Network/Tasks/managingIGs.htm
        __ https://docs.cloud.oracle.com/Content/Identity/Concepts/overview.htm
        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param CreateInternetGatewayDetails create_internet_gateway_details: (required)
            Details for creating a new internet gateway.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.InternetGateway`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/internetGateways"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_internet_gateway got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_internet_gateway_details,
                response_type="InternetGateway")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_internet_gateway_details,
                response_type="InternetGateway")

    def create_ip_sec_connection(self, create_ip_sec_connection_details, **kwargs):
        """
        Creates a new IPSec connection between the specified DRG and CPE. For more information, see
        `IPSec VPNs`__.

        If you configure at least one tunnel to use static routing, then in the request you must provide
        at least one valid static route (you're allowed a maximum of 10). For example: 10.0.0.0/16.
        If you configure both tunnels to use BGP dynamic routing, you can provide an empty list for
        the static routes. For more information, see the important note in
        :class:`IPSecConnection`.

        For the purposes of access control, you must provide the OCID of the compartment where you want the
        IPSec connection to reside. Notice that the IPSec connection doesn't have to be in the same compartment
        as the DRG, CPE, or other Networking Service components. If you're not sure which compartment to
        use, put the IPSec connection in the same compartment as the DRG. For more information about
        compartments and access control, see
        `Overview of the IAM Service`__.
        For information about OCIDs, see `Resource Identifiers`__.

        You may optionally specify a *display name* for the IPSec connection, otherwise a default is provided.
        It does not have to be unique, and you can change it. Avoid entering confidential information.

        After creating the IPSec connection, you need to configure your on-premises router
        with tunnel-specific information. For tunnel status and the required configuration information, see:

          * :class:`IPSecConnectionTunnel`
          * :class:`IPSecConnectionTunnelSharedSecret`

        For each tunnel, you need the IP address of Oracle's VPN headend and the shared secret
        (that is, the pre-shared key). For more information, see
        `Configuring Your On-Premises Router for an IPSec VPN`__.

        __ https://docs.cloud.oracle.com/Content/Network/Tasks/managingIPsec.htm
        __ https://docs.cloud.oracle.com/Content/Identity/Concepts/overview.htm
        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Tasks/configuringCPE.htm


        :param CreateIPSecConnectionDetails create_ip_sec_connection_details: (required)
            Details for creating an `IPSecConnection`.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.IPSecConnection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/ipsecConnections"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_ip_sec_connection got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_ip_sec_connection_details,
                response_type="IPSecConnection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_ip_sec_connection_details,
                response_type="IPSecConnection")

    def create_ipv6(self, create_ipv6_details, **kwargs):
        """
        Creates an IPv6 for the specified VNIC.


        :param CreateIpv6Details create_ipv6_details: (required)
            Create IPv6 details.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.Ipv6`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/ipv6"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_ipv6 got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_ipv6_details,
                response_type="Ipv6")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_ipv6_details,
                response_type="Ipv6")

    def create_local_peering_gateway(self, create_local_peering_gateway_details, **kwargs):
        """
        Creates a new local peering gateway (LPG) for the specified VCN.


        :param CreateLocalPeeringGatewayDetails create_local_peering_gateway_details: (required)
            Details for creating a new local peering gateway.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.LocalPeeringGateway`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/localPeeringGateways"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_local_peering_gateway got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_local_peering_gateway_details,
                response_type="LocalPeeringGateway")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_local_peering_gateway_details,
                response_type="LocalPeeringGateway")

    def create_nat_gateway(self, create_nat_gateway_details, **kwargs):
        """
        Creates a new NAT gateway for the specified VCN. You must also set up a route rule with the
        NAT gateway as the rule's target. See :class:`RouteTable`.


        :param CreateNatGatewayDetails create_nat_gateway_details: (required)
            Details for creating a NAT gateway.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.NatGateway`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/natGateways"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_nat_gateway got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_nat_gateway_details,
                response_type="NatGateway")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_nat_gateway_details,
                response_type="NatGateway")

    def create_network_security_group(self, create_network_security_group_details, **kwargs):
        """
        Creates a new network security group for the specified VCN.


        :param CreateNetworkSecurityGroupDetails create_network_security_group_details: (required)
            Details for creating a network security group.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.NetworkSecurityGroup`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/networkSecurityGroups"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_network_security_group got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_network_security_group_details,
                response_type="NetworkSecurityGroup")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_network_security_group_details,
                response_type="NetworkSecurityGroup")

    def create_private_ip(self, create_private_ip_details, **kwargs):
        """
        Creates a secondary private IP for the specified VNIC.
        For more information about secondary private IPs, see
        `IP Addresses`__.

        __ https://docs.cloud.oracle.com/Content/Network/Tasks/managingIPaddresses.htm


        :param CreatePrivateIpDetails create_private_ip_details: (required)
            Create private IP details.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.PrivateIp`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/privateIps"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_private_ip got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_private_ip_details,
                response_type="PrivateIp")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_private_ip_details,
                response_type="PrivateIp")

    def create_public_ip(self, create_public_ip_details, **kwargs):
        """
        Creates a public IP. Use the `lifetime` property to specify whether it's an ephemeral or
        reserved public IP. For information about limits on how many you can create, see
        `Public IP Addresses`__.

        * **For an ephemeral public IP assigned to a private IP:** You must also specify a `privateIpId`
        with the OCID of the primary private IP you want to assign the public IP to. The public IP is
        created in the same availability domain as the private IP. An ephemeral public IP must always be
        assigned to a private IP, and only to the *primary* private IP on a VNIC, not a secondary
        private IP. Exception: If you create a :class:`NatGateway`, Oracle
        automatically assigns the NAT gateway a regional ephemeral public IP that you cannot remove.

        * **For a reserved public IP:** You may also optionally assign the public IP to a private
        IP by specifying `privateIpId`. Or you can later assign the public IP with
        :func:`update_public_ip`.

        **Note:** When assigning a public IP to a private IP, the private IP must not already have
        a public IP with `lifecycleState` = ASSIGNING or ASSIGNED. If it does, an error is returned.

        Also, for reserved public IPs, the optional assignment part of this operation is
        asynchronous. Poll the public IP's `lifecycleState` to determine if the assignment
        succeeded.

        __ https://docs.cloud.oracle.com/Content/Network/Tasks/managingpublicIPs.htm


        :param CreatePublicIpDetails create_public_ip_details: (required)
            Create public IP details.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.PublicIp`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/publicIps"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_public_ip got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_public_ip_details,
                response_type="PublicIp")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_public_ip_details,
                response_type="PublicIp")

    def create_remote_peering_connection(self, create_remote_peering_connection_details, **kwargs):
        """
        Creates a new remote peering connection (RPC) for the specified DRG.


        :param CreateRemotePeeringConnectionDetails create_remote_peering_connection_details: (required)
            Request to create peering connection to remote region

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.RemotePeeringConnection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/remotePeeringConnections"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_remote_peering_connection got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_remote_peering_connection_details,
                response_type="RemotePeeringConnection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_remote_peering_connection_details,
                response_type="RemotePeeringConnection")

    def create_route_table(self, create_route_table_details, **kwargs):
        """
        Creates a new route table for the specified VCN. In the request you must also include at least one route
        rule for the new route table. For information on the number of rules you can have in a route table, see
        `Service Limits`__. For general information about route
        tables in your VCN and the types of targets you can use in route rules,
        see `Route Tables`__.

        For the purposes of access control, you must provide the OCID of the compartment where you want the route
        table to reside. Notice that the route table doesn't have to be in the same compartment as the VCN, subnets,
        or other Networking Service components. If you're not sure which compartment to use, put the route
        table in the same compartment as the VCN. For more information about compartments and access control, see
        `Overview of the IAM Service`__. For information about OCIDs, see
        `Resource Identifiers`__.

        You may optionally specify a *display name* for the route table, otherwise a default is provided.
        It does not have to be unique, and you can change it. Avoid entering confidential information.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/servicelimits.htm
        __ https://docs.cloud.oracle.com/Content/Network/Tasks/managingroutetables.htm
        __ https://docs.cloud.oracle.com/Content/Identity/Concepts/overview.htm
        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param CreateRouteTableDetails create_route_table_details: (required)
            Details for creating a new route table.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.RouteTable`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/routeTables"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_route_table got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_route_table_details,
                response_type="RouteTable")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_route_table_details,
                response_type="RouteTable")

    def create_security_list(self, create_security_list_details, **kwargs):
        """
        Creates a new security list for the specified VCN. For more information
        about security lists, see `Security Lists`__.
        For information on the number of rules you can have in a security list, see
        `Service Limits`__.

        For the purposes of access control, you must provide the OCID of the compartment where you want the security
        list to reside. Notice that the security list doesn't have to be in the same compartment as the VCN, subnets,
        or other Networking Service components. If you're not sure which compartment to use, put the security
        list in the same compartment as the VCN. For more information about compartments and access control, see
        `Overview of the IAM Service`__. For information about OCIDs, see
        `Resource Identifiers`__.

        You may optionally specify a *display name* for the security list, otherwise a default is provided.
        It does not have to be unique, and you can change it. Avoid entering confidential information.

        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securitylists.htm
        __ https://docs.cloud.oracle.com/Content/General/Concepts/servicelimits.htm
        __ https://docs.cloud.oracle.com/Content/Identity/Concepts/overview.htm
        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param CreateSecurityListDetails create_security_list_details: (required)
            Details regarding the security list to create.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.SecurityList`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/securityLists"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_security_list got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_security_list_details,
                response_type="SecurityList")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_security_list_details,
                response_type="SecurityList")

    def create_service_gateway(self, create_service_gateway_details, **kwargs):
        """
        Creates a new service gateway in the specified compartment.

        For the purposes of access control, you must provide the OCID of the compartment where you want
        the service gateway to reside. For more information about compartments and access control, see
        `Overview of the IAM Service`__.
        For information about OCIDs, see `Resource Identifiers`__.

        You may optionally specify a *display name* for the service gateway, otherwise a default is provided.
        It does not have to be unique, and you can change it. Avoid entering confidential information.

        __ https://docs.cloud.oracle.com/Content/Identity/Concepts/overview.htm
        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param CreateServiceGatewayDetails create_service_gateway_details: (required)
            Details for creating a service gateway.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.ServiceGateway`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/serviceGateways"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_service_gateway got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_service_gateway_details,
                response_type="ServiceGateway")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_service_gateway_details,
                response_type="ServiceGateway")

    def create_subnet(self, create_subnet_details, **kwargs):
        """
        Creates a new subnet in the specified VCN. You can't change the size of the subnet after creation,
        so it's important to think about the size of subnets you need before creating them.
        For more information, see `VCNs and Subnets`__.
        For information on the number of subnets you can have in a VCN, see
        `Service Limits`__.

        For the purposes of access control, you must provide the OCID of the compartment where you want the subnet
        to reside. Notice that the subnet doesn't have to be in the same compartment as the VCN, route tables, or
        other Networking Service components. If you're not sure which compartment to use, put the subnet in
        the same compartment as the VCN. For more information about compartments and access control, see
        `Overview of the IAM Service`__. For information about OCIDs,
        see `Resource Identifiers`__.

        You may optionally associate a route table with the subnet. If you don't, the subnet will use the
        VCN's default route table. For more information about route tables, see
        `Route Tables`__.

        You may optionally associate a security list with the subnet. If you don't, the subnet will use the
        VCN's default security list. For more information about security lists, see
        `Security Lists`__.

        You may optionally associate a set of DHCP options with the subnet. If you don't, the subnet will use the
        VCN's default set. For more information about DHCP options, see
        `DHCP Options`__.

        You may optionally specify a *display name* for the subnet, otherwise a default is provided.
        It does not have to be unique, and you can change it. Avoid entering confidential information.

        You can also add a DNS label for the subnet, which is required if you want the Internet and
        VCN Resolver to resolve hostnames for instances in the subnet. For more information, see
        `DNS in Your Virtual Cloud Network`__.

        __ https://docs.cloud.oracle.com/Content/Network/Tasks/managingVCNs.htm
        __ https://docs.cloud.oracle.com/Content/General/Concepts/servicelimits.htm
        __ https://docs.cloud.oracle.com/Content/Identity/Concepts/overview.htm
        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Tasks/managingroutetables.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securitylists.htm
        __ https://docs.cloud.oracle.com/Content/Network/Tasks/managingDHCP.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/dns.htm


        :param CreateSubnetDetails create_subnet_details: (required)
            Details for creating a subnet.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.Subnet`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/subnets"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_subnet got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_subnet_details,
                response_type="Subnet")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_subnet_details,
                response_type="Subnet")

    def create_vcn(self, create_vcn_details, **kwargs):
        """
        Creates a new virtual cloud network (VCN). For more information, see
        `VCNs and Subnets`__.

        For the VCN you must specify a single, contiguous IPv4 CIDR block. Oracle recommends using one of the
        private IP address ranges specified in `RFC 1918`__ (10.0.0.0/8,
        172.16/12, and 192.168/16). Example: 172.16.0.0/16. The CIDR block can range from /16 to /30, and it
        must not overlap with your on-premises network. You can't change the size of the VCN after creation.

        For the purposes of access control, you must provide the OCID of the compartment where you want the VCN to
        reside. Consult an Oracle Cloud Infrastructure administrator in your organization if you're not sure which
        compartment to use. Notice that the VCN doesn't have to be in the same compartment as the subnets or other
        Networking Service components. For more information about compartments and access control, see
        `Overview of the IAM Service`__. For information about OCIDs, see
        `Resource Identifiers`__.

        You may optionally specify a *display name* for the VCN, otherwise a default is provided. It does not have to
        be unique, and you can change it. Avoid entering confidential information.

        You can also add a DNS label for the VCN, which is required if you want the instances to use the
        Interent and VCN Resolver option for DNS in the VCN. For more information, see
        `DNS in Your Virtual Cloud Network`__.

        The VCN automatically comes with a default route table, default security list, and default set of DHCP options.
        The OCID for each is returned in the response. You can't delete these default objects, but you can change their
        contents (that is, change the route rules, security list rules, and so on).

        The VCN and subnets you create are not accessible until you attach an internet gateway or set up an IPSec VPN
        or FastConnect. For more information, see
        `Overview of the Networking Service`__.

        __ https://docs.cloud.oracle.com/Content/Network/Tasks/managingVCNs.htm
        __ https://tools.ietf.org/html/rfc1918
        __ https://docs.cloud.oracle.com/Content/Identity/Concepts/overview.htm
        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/dns.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/overview.htm


        :param CreateVcnDetails create_vcn_details: (required)
            Details for creating a new VCN.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.Vcn`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/vcns"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_vcn got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_vcn_details,
                response_type="Vcn")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_vcn_details,
                response_type="Vcn")

    def create_virtual_circuit(self, create_virtual_circuit_details, **kwargs):
        """
        Creates a new virtual circuit to use with Oracle Cloud
        Infrastructure FastConnect. For more information, see
        `FastConnect Overview`__.

        For the purposes of access control, you must provide the OCID of the
        compartment where you want the virtual circuit to reside. If you're
        not sure which compartment to use, put the virtual circuit in the
        same compartment with the DRG it's using. For more information about
        compartments and access control, see
        `Overview of the IAM Service`__.
        For information about OCIDs, see
        `Resource Identifiers`__.

        You may optionally specify a *display name* for the virtual circuit.
        It does not have to be unique, and you can change it. Avoid entering confidential information.

        **Important:** When creating a virtual circuit, you specify a DRG for
        the traffic to flow through. Make sure you attach the DRG to your
        VCN and confirm the VCN's routing sends traffic to the DRG. Otherwise
        traffic will not flow. For more information, see
        `Route Tables`__.

        __ https://docs.cloud.oracle.com/Content/Network/Concepts/fastconnect.htm
        __ https://docs.cloud.oracle.com/Content/Identity/Concepts/overview.htm
        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Tasks/managingroutetables.htm


        :param CreateVirtualCircuitDetails create_virtual_circuit_details: (required)
            Details to create a VirtualCircuit.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.VirtualCircuit`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/virtualCircuits"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_virtual_circuit got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_virtual_circuit_details,
                response_type="VirtualCircuit")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_virtual_circuit_details,
                response_type="VirtualCircuit")

    def create_vlan(self, create_vlan_details, **kwargs):
        """
        Creates a VLAN in the specified VCN and the specified compartment.


        :param CreateVlanDetails create_vlan_details: (required)
            Details for creating a VLAN

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.Vlan`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/vlans"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_vlan got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_vlan_details,
                response_type="Vlan")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_vlan_details,
                response_type="Vlan")

    def delete_cpe(self, cpe_id, **kwargs):
        """
        Deletes the specified CPE object. The CPE must not be connected to a DRG. This is an asynchronous
        operation. The CPE's `lifecycleState` will change to TERMINATING temporarily until the CPE is completely
        removed.


        :param str cpe_id: (required)
            The OCID of the CPE.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/cpes/{cpeId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_cpe got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "cpeId": cpe_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_cross_connect(self, cross_connect_id, **kwargs):
        """
        Deletes the specified cross-connect. It must not be mapped to a
        :class:`VirtualCircuit`.


        :param str cross_connect_id: (required)
            The OCID of the cross-connect.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/crossConnects/{crossConnectId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_cross_connect got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "crossConnectId": cross_connect_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_cross_connect_group(self, cross_connect_group_id, **kwargs):
        """
        Deletes the specified cross-connect group. It must not contain any
        cross-connects, and it cannot be mapped to a
        :class:`VirtualCircuit`.


        :param str cross_connect_group_id: (required)
            The OCID of the cross-connect group.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/crossConnectGroups/{crossConnectGroupId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_cross_connect_group got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "crossConnectGroupId": cross_connect_group_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_dhcp_options(self, dhcp_id, **kwargs):
        """
        Deletes the specified set of DHCP options, but only if it's not associated with a subnet. You can't delete a
        VCN's default set of DHCP options.

        This is an asynchronous operation. The state of the set of options will switch to TERMINATING temporarily
        until the set is completely removed.


        :param str dhcp_id: (required)
            The OCID for the set of DHCP options.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dhcps/{dhcpId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_dhcp_options got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dhcpId": dhcp_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_drg(self, drg_id, **kwargs):
        """
        Deletes the specified DRG. The DRG must not be attached to a VCN or be connected to your on-premise
        network. Also, there must not be a route table that lists the DRG as a target. This is an asynchronous
        operation. The DRG's `lifecycleState` will change to TERMINATING temporarily until the DRG is completely
        removed.


        :param str drg_id: (required)
            The OCID of the DRG.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/drgs/{drgId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_drg got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "drgId": drg_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_drg_attachment(self, drg_attachment_id, **kwargs):
        """
        Detaches a DRG from a VCN by deleting the corresponding `DrgAttachment`. This is an asynchronous
        operation. The attachment's `lifecycleState` will change to DETACHING temporarily until the attachment
        is completely removed.


        :param str drg_attachment_id: (required)
            The OCID of the DRG attachment.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/drgAttachments/{drgAttachmentId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_drg_attachment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "drgAttachmentId": drg_attachment_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_internet_gateway(self, ig_id, **kwargs):
        """
        Deletes the specified internet gateway. The internet gateway does not have to be disabled, but
        there must not be a route table that lists it as a target.

        This is an asynchronous operation. The gateway's `lifecycleState` will change to TERMINATING temporarily
        until the gateway is completely removed.


        :param str ig_id: (required)
            The OCID of the internet gateway.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/internetGateways/{igId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_internet_gateway got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "igId": ig_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_ip_sec_connection(self, ipsc_id, **kwargs):
        """
        Deletes the specified IPSec connection. If your goal is to disable the IPSec VPN between your VCN and
        on-premises network, it's easiest to simply detach the DRG but keep all the IPSec VPN components intact.
        If you were to delete all the components and then later need to create an IPSec VPN again, you would
        need to configure your on-premises router again with the new information returned from
        :func:`create_ip_sec_connection`.

        This is an asynchronous operation. The connection's `lifecycleState` will change to TERMINATING temporarily
        until the connection is completely removed.


        :param str ipsc_id: (required)
            The OCID of the IPSec connection.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/ipsecConnections/{ipscId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_ip_sec_connection got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "ipscId": ipsc_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_ipv6(self, ipv6_id, **kwargs):
        """
        Unassigns and deletes the specified IPv6. You must specify the object's OCID.
        The IPv6 address is returned to the subnet's pool of available addresses.


        :param str ipv6_id: (required)
            The `OCID`__ of the IPv6.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/ipv6/{ipv6Id}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_ipv6 got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "ipv6Id": ipv6_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_local_peering_gateway(self, local_peering_gateway_id, **kwargs):
        """
        Deletes the specified local peering gateway (LPG).

        This is an asynchronous operation; the local peering gateway's `lifecycleState` changes to TERMINATING temporarily
        until the local peering gateway is completely removed.


        :param str local_peering_gateway_id: (required)
            The OCID of the local peering gateway.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/localPeeringGateways/{localPeeringGatewayId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_local_peering_gateway got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "localPeeringGatewayId": local_peering_gateway_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_nat_gateway(self, nat_gateway_id, **kwargs):
        """
        Deletes the specified NAT gateway. The NAT gateway does not have to be disabled, but there
        must not be a route rule that lists the NAT gateway as a target.

        This is an asynchronous operation. The NAT gateway's `lifecycleState` will change to
        TERMINATING temporarily until the NAT gateway is completely removed.


        :param str nat_gateway_id: (required)
            The NAT gateway's `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/natGateways/{natGatewayId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_nat_gateway got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "natGatewayId": nat_gateway_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_network_security_group(self, network_security_group_id, **kwargs):
        """
        Deletes the specified network security group. The group must not contain any VNICs.

        To get a list of the VNICs in a network security group, use
        :func:`list_network_security_group_vnics`.
        Each returned :class:`NetworkSecurityGroupVnic` object
        contains both the OCID of the VNIC and the OCID of the VNIC's parent resource (for example,
        the Compute instance that the VNIC is attached to).


        :param str network_security_group_id: (required)
            The `OCID`__ of the network security group.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/networkSecurityGroups/{networkSecurityGroupId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_network_security_group got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "networkSecurityGroupId": network_security_group_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_private_ip(self, private_ip_id, **kwargs):
        """
        Unassigns and deletes the specified private IP. You must
        specify the object's OCID. The private IP address is returned to
        the subnet's pool of available addresses.

        This operation cannot be used with primary private IPs, which are
        automatically unassigned and deleted when the VNIC is terminated.

        **Important:** If a secondary private IP is the
        `target of a route rule`__,
        unassigning it from the VNIC causes that route rule to blackhole and the traffic
        will be dropped.

        __ https://docs.cloud.oracle.com/Content/Network/Tasks/managingroutetables.htm#privateip


        :param str private_ip_id: (required)
            The OCID of the private IP.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/privateIps/{privateIpId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_private_ip got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "privateIpId": private_ip_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_public_ip(self, public_ip_id, **kwargs):
        """
        Unassigns and deletes the specified public IP (either ephemeral or reserved).
        You must specify the object's OCID. The public IP address is returned to the
        Oracle Cloud Infrastructure public IP pool.

        **Note:** You cannot update, unassign, or delete the public IP that Oracle automatically
        assigned to an entity for you (such as a load balancer or NAT gateway). The public IP is
        automatically deleted if the assigned entity is terminated.

        For an assigned reserved public IP, the initial unassignment portion of this operation
        is asynchronous. Poll the public IP's `lifecycleState` to determine
        if the operation succeeded.

        If you want to simply unassign a reserved public IP and return it to your pool
        of reserved public IPs, instead use
        :func:`update_public_ip`.


        :param str public_ip_id: (required)
            The OCID of the public IP.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/publicIps/{publicIpId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_public_ip got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "publicIpId": public_ip_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_remote_peering_connection(self, remote_peering_connection_id, **kwargs):
        """
        Deletes the remote peering connection (RPC).

        This is an asynchronous operation; the RPC's `lifecycleState` changes to TERMINATING temporarily
        until the RPC is completely removed.


        :param str remote_peering_connection_id: (required)
            The OCID of the remote peering connection (RPC).

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/remotePeeringConnections/{remotePeeringConnectionId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_remote_peering_connection got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "remotePeeringConnectionId": remote_peering_connection_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_route_table(self, rt_id, **kwargs):
        """
        Deletes the specified route table, but only if it's not associated with a subnet. You can't delete a
        VCN's default route table.

        This is an asynchronous operation. The route table's `lifecycleState` will change to TERMINATING temporarily
        until the route table is completely removed.


        :param str rt_id: (required)
            The OCID of the route table.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/routeTables/{rtId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_route_table got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "rtId": rt_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_security_list(self, security_list_id, **kwargs):
        """
        Deletes the specified security list, but only if it's not associated with a subnet. You can't delete
        a VCN's default security list.

        This is an asynchronous operation. The security list's `lifecycleState` will change to TERMINATING temporarily
        until the security list is completely removed.


        :param str security_list_id: (required)
            The OCID of the security list.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/securityLists/{securityListId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_security_list got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "securityListId": security_list_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_service_gateway(self, service_gateway_id, **kwargs):
        """
        Deletes the specified service gateway. There must not be a route table that lists the service
        gateway as a target.


        :param str service_gateway_id: (required)
            The service gateway's `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/serviceGateways/{serviceGatewayId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_service_gateway got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "serviceGatewayId": service_gateway_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_subnet(self, subnet_id, **kwargs):
        """
        Deletes the specified subnet, but only if there are no instances in the subnet. This is an asynchronous
        operation. The subnet's `lifecycleState` will change to TERMINATING temporarily. If there are any
        instances in the subnet, the state will instead change back to AVAILABLE.


        :param str subnet_id: (required)
            The OCID of the subnet.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/subnets/{subnetId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_subnet got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "subnetId": subnet_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_vcn(self, vcn_id, **kwargs):
        """
        Deletes the specified VCN. The VCN must be empty and have no attached gateways. This is an asynchronous
        operation. The VCN's `lifecycleState` will change to TERMINATING temporarily until the VCN is completely
        removed.


        :param str vcn_id: (required)
            The `OCID`__ of the VCN.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/vcns/{vcnId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_vcn got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "vcnId": vcn_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_virtual_circuit(self, virtual_circuit_id, **kwargs):
        """
        Deletes the specified virtual circuit.

        **Important:** If you're using FastConnect via a provider,
        make sure to also terminate the connection with
        the provider, or else the provider may continue to bill you.


        :param str virtual_circuit_id: (required)
            The OCID of the virtual circuit.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/virtualCircuits/{virtualCircuitId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_virtual_circuit got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "virtualCircuitId": virtual_circuit_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_vlan(self, vlan_id, **kwargs):
        """
        Deletes the specified VLAN, but only if there are no VNICs in the VLAN.


        :param str vlan_id: (required)
            The `OCID`__ of the VLAN.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/vlans/{vlanId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_vlan got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "vlanId": vlan_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def detach_service_id(self, service_gateway_id, detach_service_details, **kwargs):
        """
        Removes the specified :class:`Service` from the list of enabled
        `Service` objects for the specified gateway. You do not need to remove any route
        rules that specify this `Service` object's `cidrBlock` as the destination CIDR. However, consider
        removing the rules if your intent is to permanently disable use of the `Service` through this
        service gateway.

        **Note:** The `DetachServiceId` operation is an easy way to remove an individual `Service` from
        the service gateway. Compare it with
        :func:`update_service_gateway`, which replaces
        the entire existing list of enabled `Service` objects with the list that you provide in the
        `Update` call. `UpdateServiceGateway` also lets you block all traffic through the service
        gateway without having to remove each of the individual `Service` objects.


        :param str service_gateway_id: (required)
            The service gateway's `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param ServiceIdRequestDetails detach_service_details: (required)
            ServiceId of Service to be detached from a service gateway.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.ServiceGateway`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/serviceGateways/{serviceGatewayId}/actions/detachService"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "detach_service_id got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "serviceGatewayId": service_gateway_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=detach_service_details,
                response_type="ServiceGateway")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=detach_service_details,
                response_type="ServiceGateway")

    def get_cpe(self, cpe_id, **kwargs):
        """
        Gets the specified CPE's information.


        :param str cpe_id: (required)
            The OCID of the CPE.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.Cpe`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/cpes/{cpeId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_cpe got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "cpeId": cpe_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Cpe")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Cpe")

    def get_cpe_device_config_content(self, cpe_id, **kwargs):
        """
        Renders a set of CPE configuration content that can help a network engineer configure the actual
        CPE device (for example, a hardware router) represented by the specified :class:`Cpe`
        object.

        The rendered content is specific to the type of CPE device (for example, Cisco ASA). Therefore the
        :class:`Cpe` must have the CPE's device type specified by the `cpeDeviceShapeId`
        attribute. The content optionally includes answers that the customer provides (see
        :func:`update_tunnel_cpe_device_config`),
        merged with a template of other information specific to the CPE device type.

        The operation returns configuration information for *all* of the
        :class:`IPSecConnection` objects that use the specified CPE.
        Here are similar operations:

          * :func:`get_ipsec_cpe_device_config_content`
          returns CPE configuration content for all tunnels in a single IPSec connection.
          * :func:`get_tunnel_cpe_device_config_content`
          returns CPE configuration content for a specific tunnel within an IPSec connection.


        :param str cpe_id: (required)
            The OCID of the CPE.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type stream
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/cpes/{cpeId}/cpeConfigContent"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_cpe_device_config_content got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "cpeId": cpe_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "text/plain; charset&#x3D;utf-8",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="stream")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="stream")

    def get_cpe_device_shape(self, cpe_device_shape_id, **kwargs):
        """
        Gets the detailed information about the specified CPE device type. This might include a set of questions
        that are specific to the particular CPE device type. The customer must supply answers to those questions
        (see :func:`update_tunnel_cpe_device_config`).
        The service merges the answers with a template of other information for the CPE device type. The following
        operations return the merged content:

          * :func:`get_cpe_device_config_content`
          * :func:`get_ipsec_cpe_device_config_content`
          * :func:`get_tunnel_cpe_device_config_content`


        :param str cpe_device_shape_id: (required)
            The `OCID`__ of the CPE device shape.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.CpeDeviceShapeDetail`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/cpeDeviceShapes/{cpeDeviceShapeId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_cpe_device_shape got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "cpeDeviceShapeId": cpe_device_shape_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="CpeDeviceShapeDetail")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="CpeDeviceShapeDetail")

    def get_cross_connect(self, cross_connect_id, **kwargs):
        """
        Gets the specified cross-connect's information.


        :param str cross_connect_id: (required)
            The OCID of the cross-connect.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.CrossConnect`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/crossConnects/{crossConnectId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_cross_connect got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "crossConnectId": cross_connect_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="CrossConnect")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="CrossConnect")

    def get_cross_connect_group(self, cross_connect_group_id, **kwargs):
        """
        Gets the specified cross-connect group's information.


        :param str cross_connect_group_id: (required)
            The OCID of the cross-connect group.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.CrossConnectGroup`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/crossConnectGroups/{crossConnectGroupId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_cross_connect_group got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "crossConnectGroupId": cross_connect_group_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="CrossConnectGroup")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="CrossConnectGroup")

    def get_cross_connect_letter_of_authority(self, cross_connect_id, **kwargs):
        """
        Gets the Letter of Authority for the specified cross-connect.


        :param str cross_connect_id: (required)
            The OCID of the cross-connect.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.LetterOfAuthority`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/crossConnects/{crossConnectId}/letterOfAuthority"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_cross_connect_letter_of_authority got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "crossConnectId": cross_connect_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json, text/html",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="LetterOfAuthority")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="LetterOfAuthority")

    def get_cross_connect_status(self, cross_connect_id, **kwargs):
        """
        Gets the status of the specified cross-connect.


        :param str cross_connect_id: (required)
            The OCID of the cross-connect.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.CrossConnectStatus`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/crossConnects/{crossConnectId}/status"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_cross_connect_status got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "crossConnectId": cross_connect_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="CrossConnectStatus")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="CrossConnectStatus")

    def get_dhcp_options(self, dhcp_id, **kwargs):
        """
        Gets the specified set of DHCP options.


        :param str dhcp_id: (required)
            The OCID for the set of DHCP options.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.DhcpOptions`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dhcps/{dhcpId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_dhcp_options got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dhcpId": dhcp_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="DhcpOptions")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="DhcpOptions")

    def get_drg(self, drg_id, **kwargs):
        """
        Gets the specified DRG's information.


        :param str drg_id: (required)
            The OCID of the DRG.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.Drg`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/drgs/{drgId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_drg got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "drgId": drg_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Drg")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Drg")

    def get_drg_attachment(self, drg_attachment_id, **kwargs):
        """
        Gets the information for the specified `DrgAttachment`.


        :param str drg_attachment_id: (required)
            The OCID of the DRG attachment.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.DrgAttachment`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/drgAttachments/{drgAttachmentId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_drg_attachment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "drgAttachmentId": drg_attachment_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="DrgAttachment")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="DrgAttachment")

    def get_drg_redundancy_status(self, drg_id, **kwargs):
        """
        Gets the redundancy status for the specified DRG. For more information, see
        `Redundancy Remedies`__.

        __ https://docs.cloud.oracle.com/Content/Network/Troubleshoot/drgredundancy.htm


        :param str drg_id: (required)
            The OCID of the DRG.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.DrgRedundancyStatus`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/drgs/{drgId}/redundancyStatus"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_drg_redundancy_status got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "drgId": drg_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="DrgRedundancyStatus")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="DrgRedundancyStatus")

    def get_fast_connect_provider_service(self, provider_service_id, **kwargs):
        """
        Gets the specified provider service.
        For more information, see `FastConnect Overview`__.

        __ https://docs.cloud.oracle.com/Content/Network/Concepts/fastconnect.htm


        :param str provider_service_id: (required)
            The OCID of the provider service.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.FastConnectProviderService`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/fastConnectProviderServices/{providerServiceId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_fast_connect_provider_service got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "providerServiceId": provider_service_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="FastConnectProviderService")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="FastConnectProviderService")

    def get_fast_connect_provider_service_key(self, provider_service_id, provider_service_key_name, **kwargs):
        """
        Gets the specified provider service key's information. Use this operation to validate a
        provider service key. An invalid key returns a 404 error.


        :param str provider_service_id: (required)
            The OCID of the provider service.

        :param str provider_service_key_name: (required)
            The provider service key that the provider gives you when you set up a virtual circuit connection
            from the provider to Oracle Cloud Infrastructure. You can set up that connection and get your
            provider service key at the provider's website or portal. For the portal location, see the `description`
            attribute of the :class:`FastConnectProviderService`.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.FastConnectProviderServiceKey`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/fastConnectProviderServices/{providerServiceId}/providerServiceKeys/{providerServiceKeyName}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_fast_connect_provider_service_key got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "providerServiceId": provider_service_id,
            "providerServiceKeyName": provider_service_key_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="FastConnectProviderServiceKey")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="FastConnectProviderServiceKey")

    def get_internet_gateway(self, ig_id, **kwargs):
        """
        Gets the specified internet gateway's information.


        :param str ig_id: (required)
            The OCID of the internet gateway.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.InternetGateway`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/internetGateways/{igId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_internet_gateway got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "igId": ig_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="InternetGateway")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="InternetGateway")

    def get_ip_sec_connection(self, ipsc_id, **kwargs):
        """
        Gets the specified IPSec connection's basic information, including the static routes for the
        on-premises router. If you want the status of the connection (whether it's up or down), use
        :func:`get_ip_sec_connection_tunnel`.


        :param str ipsc_id: (required)
            The OCID of the IPSec connection.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.IPSecConnection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/ipsecConnections/{ipscId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_ip_sec_connection got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "ipscId": ipsc_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="IPSecConnection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="IPSecConnection")

    def get_ip_sec_connection_device_config(self, ipsc_id, **kwargs):
        """
        Deprecated. To get tunnel information, instead use:

        * :func:`get_ip_sec_connection_tunnel`
        * :func:`get_ip_sec_connection_tunnel_shared_secret`


        :param str ipsc_id: (required)
            The OCID of the IPSec connection.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.IPSecConnectionDeviceConfig`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/ipsecConnections/{ipscId}/deviceConfig"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_ip_sec_connection_device_config got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "ipscId": ipsc_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="IPSecConnectionDeviceConfig")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="IPSecConnectionDeviceConfig")

    def get_ip_sec_connection_device_status(self, ipsc_id, **kwargs):
        """
        Deprecated. To get the tunnel status, instead use
        :func:`get_ip_sec_connection_tunnel`.


        :param str ipsc_id: (required)
            The OCID of the IPSec connection.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.IPSecConnectionDeviceStatus`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/ipsecConnections/{ipscId}/deviceStatus"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_ip_sec_connection_device_status got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "ipscId": ipsc_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="IPSecConnectionDeviceStatus")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="IPSecConnectionDeviceStatus")

    def get_ip_sec_connection_tunnel(self, ipsc_id, tunnel_id, **kwargs):
        """
        Gets the specified tunnel's information. The resulting object does not include the tunnel's
        shared secret (pre-shared key). To retrieve that, use
        :func:`get_ip_sec_connection_tunnel_shared_secret`.


        :param str ipsc_id: (required)
            The OCID of the IPSec connection.

        :param str tunnel_id: (required)
            The `OCID`__ of the tunnel.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.IPSecConnectionTunnel`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/ipsecConnections/{ipscId}/tunnels/{tunnelId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_ip_sec_connection_tunnel got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "ipscId": ipsc_id,
            "tunnelId": tunnel_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="IPSecConnectionTunnel")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="IPSecConnectionTunnel")

    def get_ip_sec_connection_tunnel_shared_secret(self, ipsc_id, tunnel_id, **kwargs):
        """
        Gets the specified tunnel's shared secret (pre-shared key). To get other information
        about the tunnel, use :func:`get_ip_sec_connection_tunnel`.


        :param str ipsc_id: (required)
            The OCID of the IPSec connection.

        :param str tunnel_id: (required)
            The `OCID`__ of the tunnel.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.IPSecConnectionTunnelSharedSecret`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/ipsecConnections/{ipscId}/tunnels/{tunnelId}/sharedSecret"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_ip_sec_connection_tunnel_shared_secret got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "ipscId": ipsc_id,
            "tunnelId": tunnel_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="IPSecConnectionTunnelSharedSecret")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="IPSecConnectionTunnelSharedSecret")

    def get_ipsec_cpe_device_config_content(self, ipsc_id, **kwargs):
        """
        Renders a set of CPE configuration content for the specified IPSec connection (for all the
        tunnels in the connection). The content helps a network engineer configure the actual CPE
        device (for example, a hardware router) that the specified IPSec connection terminates on.

        The rendered content is specific to the type of CPE device (for example, Cisco ASA). Therefore the
        :class:`Cpe` used by the specified :class:`IPSecConnection`
        must have the CPE's device type specified by the `cpeDeviceShapeId` attribute. The content
        optionally includes answers that the customer provides (see
        :func:`update_tunnel_cpe_device_config`),
        merged with a template of other information specific to the CPE device type.

        The operation returns configuration information for all tunnels in the single specified
        :class:`IPSecConnection` object. Here are other similar
        operations:

          * :func:`get_tunnel_cpe_device_config_content`
          returns CPE configuration content for a specific tunnel within an IPSec connection.
          * :func:`get_cpe_device_config_content`
          returns CPE configuration content for *all* IPSec connections that use a specific CPE.


        :param str ipsc_id: (required)
            The OCID of the IPSec connection.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type stream
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/ipsecConnections/{ipscId}/cpeConfigContent"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_ipsec_cpe_device_config_content got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "ipscId": ipsc_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "text/plain; charset&#x3D;utf-8",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="stream")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="stream")

    def get_ipv6(self, ipv6_id, **kwargs):
        """
        Gets the specified IPv6. You must specify the object's OCID.
        Alternatively, you can get the object by using
        :func:`list_ipv6s`
        with the IPv6 address (for example, 2001:0db8:0123:1111:98fe:dcba:9876:4321) and subnet OCID.


        :param str ipv6_id: (required)
            The `OCID`__ of the IPv6.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.Ipv6`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/ipv6/{ipv6Id}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_ipv6 got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "ipv6Id": ipv6_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Ipv6")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Ipv6")

    def get_local_peering_gateway(self, local_peering_gateway_id, **kwargs):
        """
        Gets the specified local peering gateway's information.


        :param str local_peering_gateway_id: (required)
            The OCID of the local peering gateway.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.LocalPeeringGateway`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/localPeeringGateways/{localPeeringGatewayId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_local_peering_gateway got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "localPeeringGatewayId": local_peering_gateway_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="LocalPeeringGateway")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="LocalPeeringGateway")

    def get_nat_gateway(self, nat_gateway_id, **kwargs):
        """
        Gets the specified NAT gateway's information.


        :param str nat_gateway_id: (required)
            The NAT gateway's `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.NatGateway`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/natGateways/{natGatewayId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_nat_gateway got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "natGatewayId": nat_gateway_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="NatGateway")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="NatGateway")

    def get_network_security_group(self, network_security_group_id, **kwargs):
        """
        Gets the specified network security group's information.

        To list the VNICs in an NSG, see
        :func:`list_network_security_group_vnics`.

        To list the security rules in an NSG, see
        :func:`list_network_security_group_security_rules`.


        :param str network_security_group_id: (required)
            The `OCID`__ of the network security group.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.NetworkSecurityGroup`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/networkSecurityGroups/{networkSecurityGroupId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_network_security_group got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "networkSecurityGroupId": network_security_group_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="NetworkSecurityGroup")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="NetworkSecurityGroup")

    def get_private_ip(self, private_ip_id, **kwargs):
        """
        Gets the specified private IP. You must specify the object's OCID.
        Alternatively, you can get the object by using
        :func:`list_private_ips`
        with the private IP address (for example, 10.0.3.3) and subnet OCID.


        :param str private_ip_id: (required)
            The OCID of the private IP.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.PrivateIp`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/privateIps/{privateIpId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_private_ip got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "privateIpId": private_ip_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="PrivateIp")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="PrivateIp")

    def get_public_ip(self, public_ip_id, **kwargs):
        """
        Gets the specified public IP. You must specify the object's OCID.

        Alternatively, you can get the object by using :func:`get_public_ip_by_ip_address`
        with the public IP address (for example, 203.0.113.2).

        Or you can use :func:`get_public_ip_by_private_ip_id`
        with the OCID of the private IP that the public IP is assigned to.

        **Note:** If you're fetching a reserved public IP that is in the process of being
        moved to a different private IP, the service returns the public IP object with
        `lifecycleState` = ASSIGNING and `assignedEntityId` = OCID of the target private IP.


        :param str public_ip_id: (required)
            The OCID of the public IP.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.PublicIp`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/publicIps/{publicIpId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_public_ip got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "publicIpId": public_ip_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="PublicIp")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="PublicIp")

    def get_public_ip_by_ip_address(self, get_public_ip_by_ip_address_details, **kwargs):
        """
        Gets the public IP based on the public IP address (for example, 203.0.113.2).

        **Note:** If you're fetching a reserved public IP that is in the process of being
        moved to a different private IP, the service returns the public IP object with
        `lifecycleState` = ASSIGNING and `assignedEntityId` = OCID of the target private IP.


        :param GetPublicIpByIpAddressDetails get_public_ip_by_ip_address_details: (required)
            IP address details for fetching the public IP.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.PublicIp`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/publicIps/actions/getByIpAddress"
        method = "POST"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_public_ip_by_ip_address got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=get_public_ip_by_ip_address_details,
                response_type="PublicIp")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=get_public_ip_by_ip_address_details,
                response_type="PublicIp")

    def get_public_ip_by_private_ip_id(self, get_public_ip_by_private_ip_id_details, **kwargs):
        """
        Gets the public IP assigned to the specified private IP. You must specify the OCID
        of the private IP. If no public IP is assigned, a 404 is returned.

        **Note:** If you're fetching a reserved public IP that is in the process of being
        moved to a different private IP, and you provide the OCID of the original private
        IP, this operation returns a 404. If you instead provide the OCID of the target
        private IP, or if you instead call
        :func:`get_public_ip` or
        :func:`get_public_ip_by_ip_address`, the
        service returns the public IP object with `lifecycleState` = ASSIGNING and
        `assignedEntityId` = OCID of the target private IP.


        :param GetPublicIpByPrivateIpIdDetails get_public_ip_by_private_ip_id_details: (required)
            Private IP details for fetching the public IP.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.PublicIp`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/publicIps/actions/getByPrivateIpId"
        method = "POST"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_public_ip_by_private_ip_id got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=get_public_ip_by_private_ip_id_details,
                response_type="PublicIp")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=get_public_ip_by_private_ip_id_details,
                response_type="PublicIp")

    def get_remote_peering_connection(self, remote_peering_connection_id, **kwargs):
        """
        Get the specified remote peering connection's information.


        :param str remote_peering_connection_id: (required)
            The OCID of the remote peering connection (RPC).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.RemotePeeringConnection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/remotePeeringConnections/{remotePeeringConnectionId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_remote_peering_connection got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "remotePeeringConnectionId": remote_peering_connection_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="RemotePeeringConnection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="RemotePeeringConnection")

    def get_route_table(self, rt_id, **kwargs):
        """
        Gets the specified route table's information.


        :param str rt_id: (required)
            The OCID of the route table.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.RouteTable`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/routeTables/{rtId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_route_table got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "rtId": rt_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="RouteTable")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="RouteTable")

    def get_security_list(self, security_list_id, **kwargs):
        """
        Gets the specified security list's information.


        :param str security_list_id: (required)
            The OCID of the security list.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.SecurityList`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/securityLists/{securityListId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_security_list got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "securityListId": security_list_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="SecurityList")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="SecurityList")

    def get_service(self, service_id, **kwargs):
        """
        Gets the specified :class:`Service` object.


        :param str service_id: (required)
            The service's `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.Service`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/services/{serviceId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_service got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "serviceId": service_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Service")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Service")

    def get_service_gateway(self, service_gateway_id, **kwargs):
        """
        Gets the specified service gateway's information.


        :param str service_gateway_id: (required)
            The service gateway's `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.ServiceGateway`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/serviceGateways/{serviceGatewayId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_service_gateway got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "serviceGatewayId": service_gateway_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="ServiceGateway")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="ServiceGateway")

    def get_subnet(self, subnet_id, **kwargs):
        """
        Gets the specified subnet's information.


        :param str subnet_id: (required)
            The OCID of the subnet.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.Subnet`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/subnets/{subnetId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_subnet got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "subnetId": subnet_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Subnet")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Subnet")

    def get_tunnel_cpe_device_config(self, ipsc_id, tunnel_id, **kwargs):
        """
        Gets the set of CPE configuration answers for the tunnel, which the customer provided in
        :func:`update_tunnel_cpe_device_config`.
        To get the full set of content for the tunnel (any answers merged with the template of other
        information specific to the CPE device type), use
        :func:`get_tunnel_cpe_device_config_content`.


        :param str ipsc_id: (required)
            The OCID of the IPSec connection.

        :param str tunnel_id: (required)
            The `OCID`__ of the tunnel.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.TunnelCpeDeviceConfig`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/ipsecConnections/{ipscId}/tunnels/{tunnelId}/tunnelDeviceConfig"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_tunnel_cpe_device_config got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "ipscId": ipsc_id,
            "tunnelId": tunnel_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="TunnelCpeDeviceConfig")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="TunnelCpeDeviceConfig")

    def get_tunnel_cpe_device_config_content(self, ipsc_id, tunnel_id, **kwargs):
        """
        Renders a set of CPE configuration content for the specified IPSec tunnel. The content helps a
        network engineer configure the actual CPE device (for example, a hardware router) that the specified
        IPSec tunnel terminates on.

        The rendered content is specific to the type of CPE device (for example, Cisco ASA). Therefore the
        :class:`Cpe` used by the specified :class:`IPSecConnection`
        must have the CPE's device type specified by the `cpeDeviceShapeId` attribute. The content
        optionally includes answers that the customer provides (see
        :func:`update_tunnel_cpe_device_config`),
        merged with a template of other information specific to the CPE device type.

        The operation returns configuration information for only the specified IPSec tunnel.
        Here are other similar operations:

          * :func:`get_ipsec_cpe_device_config_content`
          returns CPE configuration content for all tunnels in a single IPSec connection.
          * :func:`get_cpe_device_config_content`
          returns CPE configuration content for *all* IPSec connections that use a specific CPE.


        :param str ipsc_id: (required)
            The OCID of the IPSec connection.

        :param str tunnel_id: (required)
            The `OCID`__ of the tunnel.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type stream
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/ipsecConnections/{ipscId}/tunnels/{tunnelId}/tunnelDeviceConfig/content"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_tunnel_cpe_device_config_content got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "ipscId": ipsc_id,
            "tunnelId": tunnel_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "text/plain; charset&#x3D;utf-8",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="stream")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="stream")

    def get_vcn(self, vcn_id, **kwargs):
        """
        Gets the specified VCN's information.


        :param str vcn_id: (required)
            The `OCID`__ of the VCN.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.Vcn`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/vcns/{vcnId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_vcn got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "vcnId": vcn_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Vcn")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Vcn")

    def get_virtual_circuit(self, virtual_circuit_id, **kwargs):
        """
        Gets the specified virtual circuit's information.


        :param str virtual_circuit_id: (required)
            The OCID of the virtual circuit.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.VirtualCircuit`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/virtualCircuits/{virtualCircuitId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_virtual_circuit got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "virtualCircuitId": virtual_circuit_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="VirtualCircuit")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="VirtualCircuit")

    def get_vlan(self, vlan_id, **kwargs):
        """
        Gets the specified VLAN's information.


        :param str vlan_id: (required)
            The `OCID`__ of the VLAN.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.Vlan`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/vlans/{vlanId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_vlan got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "vlanId": vlan_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Vlan")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Vlan")

    def get_vnic(self, vnic_id, **kwargs):
        """
        Gets the information for the specified virtual network interface card (VNIC).
        You can get the VNIC OCID from the
        :func:`list_vnic_attachments`
        operation.


        :param str vnic_id: (required)
            The OCID of the VNIC.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.Vnic`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/vnics/{vnicId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_vnic got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "vnicId": vnic_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Vnic")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Vnic")

    def list_allowed_peer_regions_for_remote_peering(self, **kwargs):
        """
        Lists the regions that support remote VCN peering (which is peering across regions).
        For more information, see `VCN Peering`__.

        __ https://docs.cloud.oracle.com/Content/Network/Tasks/VCNpeering.htm


        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.PeerRegionForRemotePeering`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/allowedPeerRegionsForRemotePeering"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_allowed_peer_regions_for_remote_peering got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                response_type="list[PeerRegionForRemotePeering]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                response_type="list[PeerRegionForRemotePeering]")

    def list_cpe_device_shapes(self, **kwargs):
        """
        Lists the CPE device types that the Networking service provides CPE configuration
        content for (example: Cisco ASA). The content helps a network engineer configure
        the actual CPE device represented by a :class:`Cpe` object.

        If you want to generate CPE configuration content for one of the returned CPE device types,
        ensure that the :class:`Cpe` object's `cpeDeviceShapeId` attribute is set
        to the CPE device type's OCID (returned by this operation).

        For information about generating CPE configuration content, see these operations:

          * :func:`get_cpe_device_config_content`
          * :func:`get_ipsec_cpe_device_config_content`
          * :func:`get_tunnel_cpe_device_config_content`


        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.CpeDeviceShapeSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/cpeDeviceShapes"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_cpe_device_shapes got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[CpeDeviceShapeSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[CpeDeviceShapeSummary]")

    def list_cpes(self, compartment_id, **kwargs):
        """
        Lists the customer-premises equipment objects (CPEs) in the specified compartment.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.Cpe`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/cpes"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_cpes got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[Cpe]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[Cpe]")

    def list_cross_connect_groups(self, compartment_id, **kwargs):
        """
        Lists the cross-connect groups in the specified compartment.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str display_name: (optional)
            A filter to return only resources that match the given display name exactly.

        :param str sort_by: (optional)
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these \"List\" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.

            Allowed values are: "ASC", "DESC"

        :param str lifecycle_state: (optional)
            A filter to return only resources that match the specified lifecycle state. The value is case insensitive.

            Allowed values are: "PROVISIONING", "PROVISIONED", "INACTIVE", "TERMINATING", "TERMINATED"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.CrossConnectGroup`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/crossConnectGroups"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page",
            "display_name",
            "sort_by",
            "sort_order",
            "lifecycle_state"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_cross_connect_groups got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "DISPLAYNAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["PROVISIONING", "PROVISIONED", "INACTIVE", "TERMINATING", "TERMINATED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "displayName": kwargs.get("display_name", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[CrossConnectGroup]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[CrossConnectGroup]")

    def list_cross_connect_locations(self, compartment_id, **kwargs):
        """
        Lists the available FastConnect locations for cross-connect installation. You need
        this information so you can specify your desired location when you create a cross-connect.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.CrossConnectLocation`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/crossConnectLocations"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_cross_connect_locations got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[CrossConnectLocation]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[CrossConnectLocation]")

    def list_cross_connects(self, compartment_id, **kwargs):
        """
        Lists the cross-connects in the specified compartment. You can filter the list
        by specifying the OCID of a cross-connect group.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str cross_connect_group_id: (optional)
            The OCID of the cross-connect group.

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str display_name: (optional)
            A filter to return only resources that match the given display name exactly.

        :param str sort_by: (optional)
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these \"List\" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.

            Allowed values are: "ASC", "DESC"

        :param str lifecycle_state: (optional)
            A filter to return only resources that match the specified lifecycle state. The value is case insensitive.

            Allowed values are: "PENDING_CUSTOMER", "PROVISIONING", "PROVISIONED", "INACTIVE", "TERMINATING", "TERMINATED"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.CrossConnect`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/crossConnects"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "cross_connect_group_id",
            "limit",
            "page",
            "display_name",
            "sort_by",
            "sort_order",
            "lifecycle_state"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_cross_connects got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "DISPLAYNAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["PENDING_CUSTOMER", "PROVISIONING", "PROVISIONED", "INACTIVE", "TERMINATING", "TERMINATED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "crossConnectGroupId": kwargs.get("cross_connect_group_id", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "displayName": kwargs.get("display_name", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[CrossConnect]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[CrossConnect]")

    def list_crossconnect_port_speed_shapes(self, compartment_id, **kwargs):
        """
        Lists the available port speeds for cross-connects. You need this information
        so you can specify your desired port speed (that is, shape) when you create a
        cross-connect.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.CrossConnectPortSpeedShape`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/crossConnectPortSpeedShapes"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_crossconnect_port_speed_shapes got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[CrossConnectPortSpeedShape]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[CrossConnectPortSpeedShape]")

    def list_dhcp_options(self, compartment_id, **kwargs):
        """
        Lists the sets of DHCP options in the specified VCN and specified compartment.
        If the VCN ID is not provided, then the list includes the sets of DHCP options from all VCNs in the specified compartment.
        The response includes the default set of options that automatically comes with each VCN,
        plus any other sets you've created.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str vcn_id: (optional)
            The `OCID`__ of the VCN.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str display_name: (optional)
            A filter to return only resources that match the given display name exactly.

        :param str sort_by: (optional)
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these \"List\" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.

            Allowed values are: "ASC", "DESC"

        :param str lifecycle_state: (optional)
            A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.

            Allowed values are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.DhcpOptions`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dhcps"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "vcn_id",
            "limit",
            "page",
            "display_name",
            "sort_by",
            "sort_order",
            "lifecycle_state"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_dhcp_options got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "DISPLAYNAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "vcnId": kwargs.get("vcn_id", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "displayName": kwargs.get("display_name", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[DhcpOptions]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[DhcpOptions]")

    def list_drg_attachments(self, compartment_id, **kwargs):
        """
        Lists the `DrgAttachment` objects for the specified compartment. You can filter the
        results by VCN or DRG.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str vcn_id: (optional)
            The `OCID`__ of the VCN.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str drg_id: (optional)
            The OCID of the DRG.

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.DrgAttachment`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/drgAttachments"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "vcn_id",
            "drg_id",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_drg_attachments got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "vcnId": kwargs.get("vcn_id", missing),
            "drgId": kwargs.get("drg_id", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[DrgAttachment]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[DrgAttachment]")

    def list_drgs(self, compartment_id, **kwargs):
        """
        Lists the DRGs in the specified compartment.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.Drg`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/drgs"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_drgs got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[Drg]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[Drg]")

    def list_fast_connect_provider_services(self, compartment_id, **kwargs):
        """
        Lists the service offerings from supported providers. You need this
        information so you can specify your desired provider and service
        offering when you create a virtual circuit.

        For the compartment ID, provide the OCID of your tenancy (the root compartment).

        For more information, see `FastConnect Overview`__.

        __ https://docs.cloud.oracle.com/Content/Network/Concepts/fastconnect.htm


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.FastConnectProviderService`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/fastConnectProviderServices"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_fast_connect_provider_services got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[FastConnectProviderService]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[FastConnectProviderService]")

    def list_fast_connect_provider_virtual_circuit_bandwidth_shapes(self, provider_service_id, **kwargs):
        """
        Gets the list of available virtual circuit bandwidth levels for a provider.
        You need this information so you can specify your desired bandwidth level (shape) when you create a virtual circuit.

        For more information about virtual circuits, see `FastConnect Overview`__.

        __ https://docs.cloud.oracle.com/Content/Network/Concepts/fastconnect.htm


        :param str provider_service_id: (required)
            The OCID of the provider service.

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.VirtualCircuitBandwidthShape`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/fastConnectProviderServices/{providerServiceId}/virtualCircuitBandwidthShapes"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_fast_connect_provider_virtual_circuit_bandwidth_shapes got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "providerServiceId": provider_service_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[VirtualCircuitBandwidthShape]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[VirtualCircuitBandwidthShape]")

    def list_internet_gateways(self, compartment_id, **kwargs):
        """
        Lists the internet gateways in the specified VCN and the specified compartment.
        If the VCN ID is not provided, then the list includes the internet gateways from all VCNs in the specified compartment.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str vcn_id: (optional)
            The `OCID`__ of the VCN.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str display_name: (optional)
            A filter to return only resources that match the given display name exactly.

        :param str sort_by: (optional)
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these \"List\" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.

            Allowed values are: "ASC", "DESC"

        :param str lifecycle_state: (optional)
            A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.

            Allowed values are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.InternetGateway`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/internetGateways"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "vcn_id",
            "limit",
            "page",
            "display_name",
            "sort_by",
            "sort_order",
            "lifecycle_state"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_internet_gateways got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "DISPLAYNAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "vcnId": kwargs.get("vcn_id", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "displayName": kwargs.get("display_name", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[InternetGateway]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[InternetGateway]")

    def list_ip_sec_connection_tunnels(self, ipsc_id, **kwargs):
        """
        Lists the tunnel information for the specified IPSec connection.


        :param str ipsc_id: (required)
            The OCID of the IPSec connection.

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.IPSecConnectionTunnel`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/ipsecConnections/{ipscId}/tunnels"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_ip_sec_connection_tunnels got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "ipscId": ipsc_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[IPSecConnectionTunnel]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[IPSecConnectionTunnel]")

    def list_ip_sec_connections(self, compartment_id, **kwargs):
        """
        Lists the IPSec connections for the specified compartment. You can filter the
        results by DRG or CPE.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str drg_id: (optional)
            The OCID of the DRG.

        :param str cpe_id: (optional)
            The OCID of the CPE.

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.IPSecConnection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/ipsecConnections"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "drg_id",
            "cpe_id",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_ip_sec_connections got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "drgId": kwargs.get("drg_id", missing),
            "cpeId": kwargs.get("cpe_id", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[IPSecConnection]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[IPSecConnection]")

    def list_ipv6s(self, **kwargs):
        """
        Lists the :class:`Ipv6` objects based
        on one of these filters:

          * Subnet OCID.
          * VNIC OCID.
          * Both IPv6 address and subnet OCID: This lets you get an `Ipv6` object based on its private
          IPv6 address (for example, 2001:0db8:0123:1111:abcd:ef01:2345:6789) and not its OCID. For comparison,
          :func:`get_ipv6` requires the OCID.


        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str ip_address: (optional)
            An IP address. This could be either IPv4 or IPv6, depending on the resource.
            Example: `10.0.3.3`

        :param str subnet_id: (optional)
            The OCID of the subnet.

        :param str vnic_id: (optional)
            The OCID of the VNIC.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.Ipv6`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/ipv6"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page",
            "ip_address",
            "subnet_id",
            "vnic_id",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_ipv6s got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "ipAddress": kwargs.get("ip_address", missing),
            "subnetId": kwargs.get("subnet_id", missing),
            "vnicId": kwargs.get("vnic_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[Ipv6]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[Ipv6]")

    def list_local_peering_gateways(self, compartment_id, **kwargs):
        """
        Lists the local peering gateways (LPGs) for the specified VCN and specified compartment.
        If the VCN ID is not provided, then the list includes the LPGs from all VCNs in the specified compartment.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str vcn_id: (optional)
            The `OCID`__ of the VCN.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.LocalPeeringGateway`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/localPeeringGateways"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page",
            "vcn_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_local_peering_gateways got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "vcnId": kwargs.get("vcn_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[LocalPeeringGateway]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[LocalPeeringGateway]")

    def list_nat_gateways(self, compartment_id, **kwargs):
        """
        Lists the NAT gateways in the specified compartment. You may optionally specify a VCN OCID
        to filter the results by VCN.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str vcn_id: (optional)
            The `OCID`__ of the VCN.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str display_name: (optional)
            A filter to return only resources that match the given display name exactly.

        :param str sort_by: (optional)
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these \"List\" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.

            Allowed values are: "ASC", "DESC"

        :param str lifecycle_state: (optional)
            A filter to return only resources that match the specified lifecycle state. The value is case insensitive.

            Allowed values are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.NatGateway`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/natGateways"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "vcn_id",
            "limit",
            "page",
            "display_name",
            "sort_by",
            "sort_order",
            "lifecycle_state"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_nat_gateways got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "DISPLAYNAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "vcnId": kwargs.get("vcn_id", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "displayName": kwargs.get("display_name", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[NatGateway]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[NatGateway]")

    def list_network_security_group_security_rules(self, network_security_group_id, **kwargs):
        """
        Lists the security rules in the specified network security group.


        :param str network_security_group_id: (required)
            The `OCID`__ of the network security group.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str direction: (optional)
            Direction of the security rule. Set to `EGRESS` for rules that allow outbound IP packets,
            or `INGRESS` for rules that allow inbound IP packets.

            Allowed values are: "EGRESS", "INGRESS"

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str sort_by: (optional)
            The field to sort by.

            Allowed values are: "TIMECREATED"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.

            Allowed values are: "ASC", "DESC"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.SecurityRule`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/networkSecurityGroups/{networkSecurityGroupId}/securityRules"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "direction",
            "limit",
            "page",
            "sort_by",
            "sort_order"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_network_security_group_security_rules got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "networkSecurityGroupId": network_security_group_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'direction' in kwargs:
            direction_allowed_values = ["EGRESS", "INGRESS"]
            if kwargs['direction'] not in direction_allowed_values:
                raise ValueError(
                    "Invalid value for `direction`, must be one of {0}".format(direction_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        query_params = {
            "direction": kwargs.get("direction", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[SecurityRule]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[SecurityRule]")

    def list_network_security_group_vnics(self, network_security_group_id, **kwargs):
        """
        Lists the VNICs in the specified network security group.


        :param str network_security_group_id: (required)
            The `OCID`__ of the network security group.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str sort_by: (optional)
            The field to sort by.

            Allowed values are: "TIMEASSOCIATED"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.

            Allowed values are: "ASC", "DESC"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.NetworkSecurityGroupVnic`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/networkSecurityGroups/{networkSecurityGroupId}/vnics"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page",
            "sort_by",
            "sort_order"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_network_security_group_vnics got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "networkSecurityGroupId": network_security_group_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMEASSOCIATED"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[NetworkSecurityGroupVnic]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[NetworkSecurityGroupVnic]")

    def list_network_security_groups(self, compartment_id, **kwargs):
        """
        Lists the network security groups in the specified compartment.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str vcn_id: (optional)
            The `OCID`__ of the VCN.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str display_name: (optional)
            A filter to return only resources that match the given display name exactly.

        :param str sort_by: (optional)
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these \"List\" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.

            Allowed values are: "ASC", "DESC"

        :param str lifecycle_state: (optional)
            A filter to return only resources that match the specified lifecycle state. The value is case insensitive.

            Allowed values are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.NetworkSecurityGroup`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/networkSecurityGroups"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "vcn_id",
            "limit",
            "page",
            "display_name",
            "sort_by",
            "sort_order",
            "lifecycle_state"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_network_security_groups got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "DISPLAYNAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "vcnId": kwargs.get("vcn_id", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "displayName": kwargs.get("display_name", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[NetworkSecurityGroup]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[NetworkSecurityGroup]")

    def list_private_ips(self, **kwargs):
        """
        Lists the :class:`PrivateIp` objects based
        on one of these filters:

          - Subnet OCID.
          - VNIC OCID.
          - Both private IP address and subnet OCID: This lets
          you get a `privateIP` object based on its private IP
          address (for example, 10.0.3.3) and not its OCID. For comparison,
          :func:`get_private_ip`
          requires the OCID.

        If you're listing all the private IPs associated with a given subnet
        or VNIC, the response includes both primary and secondary private IPs.

        If you are an Oracle Cloud VMware Solution customer and have VLANs
        in your VCN, you can filter the list by VLAN OCID. See :class:`Vlan`.


        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str ip_address: (optional)
            An IP address. This could be either IPv4 or IPv6, depending on the resource.
            Example: `10.0.3.3`

        :param str subnet_id: (optional)
            The OCID of the subnet.

        :param str vnic_id: (optional)
            The OCID of the VNIC.

        :param str vlan_id: (optional)
            The `OCID`__ of the VLAN.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.PrivateIp`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/privateIps"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page",
            "ip_address",
            "subnet_id",
            "vnic_id",
            "vlan_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_private_ips got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "ipAddress": kwargs.get("ip_address", missing),
            "subnetId": kwargs.get("subnet_id", missing),
            "vnicId": kwargs.get("vnic_id", missing),
            "vlanId": kwargs.get("vlan_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[PrivateIp]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[PrivateIp]")

    def list_public_ips(self, scope, compartment_id, **kwargs):
        """
        Lists the :class:`PublicIp` objects
        in the specified compartment. You can filter the list by using query parameters.

        To list your reserved public IPs:
          * Set `scope` = `REGION`  (required)
          * Leave the `availabilityDomain` parameter empty
          * Set `lifetime` = `RESERVED`

        To list the ephemeral public IPs assigned to a regional entity such as a NAT gateway:
          * Set `scope` = `REGION`  (required)
          * Leave the `availabilityDomain` parameter empty
          * Set `lifetime` = `EPHEMERAL`

        To list the ephemeral public IPs assigned to private IPs:
          * Set `scope` = `AVAILABILITY_DOMAIN` (required)
          * Set the `availabilityDomain` parameter to the desired availability domain (required)
          * Set `lifetime` = `EPHEMERAL`

        **Note:** An ephemeral public IP assigned to a private IP
        is always in the same availability domain and compartment as the private IP.


        :param str scope: (required)
            Whether the public IP is regional or specific to a particular availability domain.

            * `REGION`: The public IP exists within a region and is assigned to a regional entity
            (such as a :class:`NatGateway`), or can be assigned to a private IP
            in any availability domain in the region. Reserved public IPs have `scope` = `REGION`, as do
            ephemeral public IPs assigned to a regional entity.

            * `AVAILABILITY_DOMAIN`: The public IP exists within the availability domain of the entity
            it's assigned to, which is specified by the `availabilityDomain` property of the public IP object.
            Ephemeral public IPs that are assigned to private IPs have `scope` = `AVAILABILITY_DOMAIN`.

            Allowed values are: "REGION", "AVAILABILITY_DOMAIN"

        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str availability_domain: (optional)
            The name of the availability domain.

            Example: `Uocm:PHX-AD-1`

        :param str lifetime: (optional)
            A filter to return only public IPs that match given lifetime.

            Allowed values are: "EPHEMERAL", "RESERVED"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.PublicIp`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/publicIps"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page",
            "availability_domain",
            "lifetime"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_public_ips got unknown kwargs: {!r}".format(extra_kwargs))

        scope_allowed_values = ["REGION", "AVAILABILITY_DOMAIN"]
        if scope not in scope_allowed_values:
            raise ValueError(
                "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
            )

        if 'lifetime' in kwargs:
            lifetime_allowed_values = ["EPHEMERAL", "RESERVED"]
            if kwargs['lifetime'] not in lifetime_allowed_values:
                raise ValueError(
                    "Invalid value for `lifetime`, must be one of {0}".format(lifetime_allowed_values)
                )

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "scope": scope,
            "availabilityDomain": kwargs.get("availability_domain", missing),
            "lifetime": kwargs.get("lifetime", missing),
            "compartmentId": compartment_id
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[PublicIp]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[PublicIp]")

    def list_remote_peering_connections(self, compartment_id, **kwargs):
        """
        Lists the remote peering connections (RPCs) for the specified DRG and compartment
        (the RPC's compartment).


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str drg_id: (optional)
            The OCID of the DRG.

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.RemotePeeringConnection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/remotePeeringConnections"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "drg_id",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_remote_peering_connections got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "drgId": kwargs.get("drg_id", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[RemotePeeringConnection]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[RemotePeeringConnection]")

    def list_route_tables(self, compartment_id, **kwargs):
        """
        Lists the route tables in the specified VCN and specified compartment.
        If the VCN ID is not provided, then the list includes the route tables from all VCNs in the specified compartment.
        The response includes the default route table that automatically comes with
        each VCN in the specified compartment, plus any route tables you've created.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str vcn_id: (optional)
            The `OCID`__ of the VCN.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str display_name: (optional)
            A filter to return only resources that match the given display name exactly.

        :param str sort_by: (optional)
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these \"List\" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.

            Allowed values are: "ASC", "DESC"

        :param str lifecycle_state: (optional)
            A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.

            Allowed values are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.RouteTable`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/routeTables"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page",
            "vcn_id",
            "display_name",
            "sort_by",
            "sort_order",
            "lifecycle_state"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_route_tables got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "DISPLAYNAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "vcnId": kwargs.get("vcn_id", missing),
            "displayName": kwargs.get("display_name", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[RouteTable]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[RouteTable]")

    def list_security_lists(self, compartment_id, **kwargs):
        """
        Lists the security lists in the specified VCN and compartment.
        If the VCN ID is not provided, then the list includes the security lists from all VCNs in the specified compartment.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str vcn_id: (optional)
            The `OCID`__ of the VCN.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str display_name: (optional)
            A filter to return only resources that match the given display name exactly.

        :param str sort_by: (optional)
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these \"List\" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.

            Allowed values are: "ASC", "DESC"

        :param str lifecycle_state: (optional)
            A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.

            Allowed values are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.SecurityList`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/securityLists"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page",
            "vcn_id",
            "display_name",
            "sort_by",
            "sort_order",
            "lifecycle_state"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_security_lists got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "DISPLAYNAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "vcnId": kwargs.get("vcn_id", missing),
            "displayName": kwargs.get("display_name", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[SecurityList]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[SecurityList]")

    def list_service_gateways(self, compartment_id, **kwargs):
        """
        Lists the service gateways in the specified compartment. You may optionally specify a VCN OCID
        to filter the results by VCN.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str vcn_id: (optional)
            The `OCID`__ of the VCN.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str sort_by: (optional)
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these \"List\" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.

            Allowed values are: "ASC", "DESC"

        :param str lifecycle_state: (optional)
            A filter to return only resources that match the given lifecycle state.  The state value is case-insensitive.

            Allowed values are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.ServiceGateway`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/serviceGateways"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "vcn_id",
            "limit",
            "page",
            "sort_by",
            "sort_order",
            "lifecycle_state"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_service_gateways got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "DISPLAYNAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "vcnId": kwargs.get("vcn_id", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[ServiceGateway]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[ServiceGateway]")

    def list_services(self, **kwargs):
        """
        Lists the available :class:`Service` objects that you can enable for a
        service gateway in this region.


        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.Service`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/services"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_services got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[Service]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[Service]")

    def list_subnets(self, compartment_id, **kwargs):
        """
        Lists the subnets in the specified VCN and the specified compartment.
        If the VCN ID is not provided, then the list includes the subnets from all VCNs in the specified compartment.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str vcn_id: (optional)
            The `OCID`__ of the VCN.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str display_name: (optional)
            A filter to return only resources that match the given display name exactly.

        :param str sort_by: (optional)
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these \"List\" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.

            Allowed values are: "ASC", "DESC"

        :param str lifecycle_state: (optional)
            A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.

            Allowed values are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.Subnet`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/subnets"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page",
            "vcn_id",
            "display_name",
            "sort_by",
            "sort_order",
            "lifecycle_state"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_subnets got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "DISPLAYNAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "vcnId": kwargs.get("vcn_id", missing),
            "displayName": kwargs.get("display_name", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[Subnet]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[Subnet]")

    def list_vcns(self, compartment_id, **kwargs):
        """
        Lists the virtual cloud networks (VCNs) in the specified compartment.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str display_name: (optional)
            A filter to return only resources that match the given display name exactly.

        :param str sort_by: (optional)
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these \"List\" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.

            Allowed values are: "ASC", "DESC"

        :param str lifecycle_state: (optional)
            A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.

            Allowed values are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.Vcn`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/vcns"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page",
            "display_name",
            "sort_by",
            "sort_order",
            "lifecycle_state"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_vcns got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "DISPLAYNAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "displayName": kwargs.get("display_name", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[Vcn]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[Vcn]")

    def list_virtual_circuit_bandwidth_shapes(self, compartment_id, **kwargs):
        """
        The deprecated operation lists available bandwidth levels for virtual circuits. For the compartment ID, provide the OCID of your tenancy (the root compartment).


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.VirtualCircuitBandwidthShape`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/virtualCircuitBandwidthShapes"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_virtual_circuit_bandwidth_shapes got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[VirtualCircuitBandwidthShape]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[VirtualCircuitBandwidthShape]")

    def list_virtual_circuit_public_prefixes(self, virtual_circuit_id, **kwargs):
        """
        Lists the public IP prefixes and their details for the specified
        public virtual circuit.


        :param str virtual_circuit_id: (required)
            The OCID of the virtual circuit.

        :param str verification_state: (optional)
            A filter to only return resources that match the given verification state.
            The state value is case-insensitive.

            Allowed values are: "IN_PROGRESS", "COMPLETED", "FAILED"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.VirtualCircuitPublicPrefix`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/virtualCircuits/{virtualCircuitId}/publicPrefixes"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "verification_state"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_virtual_circuit_public_prefixes got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "virtualCircuitId": virtual_circuit_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'verification_state' in kwargs:
            verification_state_allowed_values = ["IN_PROGRESS", "COMPLETED", "FAILED"]
            if kwargs['verification_state'] not in verification_state_allowed_values:
                raise ValueError(
                    "Invalid value for `verification_state`, must be one of {0}".format(verification_state_allowed_values)
                )

        query_params = {
            "verificationState": kwargs.get("verification_state", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[VirtualCircuitPublicPrefix]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[VirtualCircuitPublicPrefix]")

    def list_virtual_circuits(self, compartment_id, **kwargs):
        """
        Lists the virtual circuits in the specified compartment.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str display_name: (optional)
            A filter to return only resources that match the given display name exactly.

        :param str sort_by: (optional)
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these \"List\" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.

            Allowed values are: "ASC", "DESC"

        :param str lifecycle_state: (optional)
            A filter to return only resources that match the specified lifecycle state. The value is case insensitive.

            Allowed values are: "PENDING_PROVIDER", "VERIFYING", "PROVISIONING", "PROVISIONED", "FAILED", "INACTIVE", "TERMINATING", "TERMINATED"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.VirtualCircuit`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/virtualCircuits"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page",
            "display_name",
            "sort_by",
            "sort_order",
            "lifecycle_state"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_virtual_circuits got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "DISPLAYNAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["PENDING_PROVIDER", "VERIFYING", "PROVISIONING", "PROVISIONED", "FAILED", "INACTIVE", "TERMINATING", "TERMINATED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "displayName": kwargs.get("display_name", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[VirtualCircuit]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[VirtualCircuit]")

    def list_vlans(self, compartment_id, vcn_id, **kwargs):
        """
        Lists the VLANs in the specified VCN and the specified compartment.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str vcn_id: (required)
            The `OCID`__ of the VCN.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str display_name: (optional)
            A filter to return only resources that match the given display name exactly.

        :param str sort_by: (optional)
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these \"List\" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.

            Allowed values are: "ASC", "DESC"

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param str lifecycle_state: (optional)
            A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.

            Allowed values are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "UPDATING"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.Vlan`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/vlans"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page",
            "display_name",
            "sort_by",
            "sort_order",
            "opc_request_id",
            "lifecycle_state"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_vlans got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "DISPLAYNAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "UPDATING"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "vcnId": vcn_id,
            "displayName": kwargs.get("display_name", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[Vlan]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[Vlan]")

    def remove_network_security_group_security_rules(self, network_security_group_id, remove_network_security_group_security_rules_details, **kwargs):
        """
        Removes one or more security rules from the specified network security group.


        :param str network_security_group_id: (required)
            The `OCID`__ of the network security group.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param RemoveNetworkSecurityGroupSecurityRulesDetails remove_network_security_group_security_rules_details: (required)
            Request with one or more security rules associated with the network security group that
            will be removed.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/networkSecurityGroups/{networkSecurityGroupId}/actions/removeSecurityRules"
        method = "POST"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "remove_network_security_group_security_rules got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "networkSecurityGroupId": network_security_group_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=remove_network_security_group_security_rules_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=remove_network_security_group_security_rules_details)

    def update_cpe(self, cpe_id, update_cpe_details, **kwargs):
        """
        Updates the specified CPE's display name or tags.
        Avoid entering confidential information.


        :param str cpe_id: (required)
            The OCID of the CPE.

        :param UpdateCpeDetails update_cpe_details: (required)
            Details object for updating a CPE.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.Cpe`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/cpes/{cpeId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_cpe got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "cpeId": cpe_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_cpe_details,
                response_type="Cpe")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_cpe_details,
                response_type="Cpe")

    def update_cross_connect(self, cross_connect_id, update_cross_connect_details, **kwargs):
        """
        Updates the specified cross-connect.


        :param str cross_connect_id: (required)
            The OCID of the cross-connect.

        :param UpdateCrossConnectDetails update_cross_connect_details: (required)
            Update CrossConnect fields.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.CrossConnect`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/crossConnects/{crossConnectId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_cross_connect got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "crossConnectId": cross_connect_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_cross_connect_details,
                response_type="CrossConnect")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_cross_connect_details,
                response_type="CrossConnect")

    def update_cross_connect_group(self, cross_connect_group_id, update_cross_connect_group_details, **kwargs):
        """
        Updates the specified cross-connect group's display name.
        Avoid entering confidential information.


        :param str cross_connect_group_id: (required)
            The OCID of the cross-connect group.

        :param UpdateCrossConnectGroupDetails update_cross_connect_group_details: (required)
            Update CrossConnectGroup fields

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.CrossConnectGroup`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/crossConnectGroups/{crossConnectGroupId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_cross_connect_group got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "crossConnectGroupId": cross_connect_group_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_cross_connect_group_details,
                response_type="CrossConnectGroup")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_cross_connect_group_details,
                response_type="CrossConnectGroup")

    def update_dhcp_options(self, dhcp_id, update_dhcp_details, **kwargs):
        """
        Updates the specified set of DHCP options. You can update the display name or the options
        themselves. Avoid entering confidential information.

        Note that the `options` object you provide replaces the entire existing set of options.


        :param str dhcp_id: (required)
            The OCID for the set of DHCP options.

        :param UpdateDhcpDetails update_dhcp_details: (required)
            Request object for updating a set of DHCP options.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.DhcpOptions`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dhcps/{dhcpId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_dhcp_options got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dhcpId": dhcp_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_dhcp_details,
                response_type="DhcpOptions")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_dhcp_details,
                response_type="DhcpOptions")

    def update_drg(self, drg_id, update_drg_details, **kwargs):
        """
        Updates the specified DRG's display name or tags. Avoid entering confidential information.


        :param str drg_id: (required)
            The OCID of the DRG.

        :param UpdateDrgDetails update_drg_details: (required)
            Details object for updating a DRG.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.Drg`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/drgs/{drgId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_drg got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "drgId": drg_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_drg_details,
                response_type="Drg")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_drg_details,
                response_type="Drg")

    def update_drg_attachment(self, drg_attachment_id, update_drg_attachment_details, **kwargs):
        """
        Updates the display name for the specified `DrgAttachment`.
        Avoid entering confidential information.


        :param str drg_attachment_id: (required)
            The OCID of the DRG attachment.

        :param UpdateDrgAttachmentDetails update_drg_attachment_details: (required)
            Details object for updating a `DrgAttachment`.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.DrgAttachment`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/drgAttachments/{drgAttachmentId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_drg_attachment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "drgAttachmentId": drg_attachment_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_drg_attachment_details,
                response_type="DrgAttachment")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_drg_attachment_details,
                response_type="DrgAttachment")

    def update_internet_gateway(self, ig_id, update_internet_gateway_details, **kwargs):
        """
        Updates the specified internet gateway. You can disable/enable it, or change its display name
        or tags. Avoid entering confidential information.

        If the gateway is disabled, that means no traffic will flow to/from the internet even if there's
        a route rule that enables that traffic.


        :param str ig_id: (required)
            The OCID of the internet gateway.

        :param UpdateInternetGatewayDetails update_internet_gateway_details: (required)
            Details for updating the internet gateway.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.InternetGateway`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/internetGateways/{igId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_internet_gateway got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "igId": ig_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_internet_gateway_details,
                response_type="InternetGateway")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_internet_gateway_details,
                response_type="InternetGateway")

    def update_ip_sec_connection(self, ipsc_id, update_ip_sec_connection_details, **kwargs):
        """
        Updates the specified IPSec connection.

        To update an individual IPSec tunnel's attributes, use
        :func:`update_ip_sec_connection_tunnel`.


        :param str ipsc_id: (required)
            The OCID of the IPSec connection.

        :param UpdateIPSecConnectionDetails update_ip_sec_connection_details: (required)
            Details object for updating a IPSec connection.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.IPSecConnection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/ipsecConnections/{ipscId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_ip_sec_connection got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "ipscId": ipsc_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_ip_sec_connection_details,
                response_type="IPSecConnection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_ip_sec_connection_details,
                response_type="IPSecConnection")

    def update_ip_sec_connection_tunnel(self, ipsc_id, tunnel_id, update_ip_sec_connection_tunnel_details, **kwargs):
        """
        Updates the specified tunnel. This operation lets you change tunnel attributes such as the
        routing type (BGP dynamic routing or static routing). Here are some important notes:

          * If you change the tunnel's routing type or BGP session configuration, the tunnel will go
            down while it's reprovisioned.

          * If you want to switch the tunnel's `routing` from `STATIC` to `BGP`, make sure the tunnel's
            BGP session configuration attributes have been set (:func:`bgp_session_info`).

          * If you want to switch the tunnel's `routing` from `BGP` to `STATIC`, make sure the
            :class:`IPSecConnection` already has at least one valid CIDR
            static route.


        :param str ipsc_id: (required)
            The OCID of the IPSec connection.

        :param str tunnel_id: (required)
            The `OCID`__ of the tunnel.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateIPSecConnectionTunnelDetails update_ip_sec_connection_tunnel_details: (required)
            Details object for updating a IPSecConnection tunnel's details.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.IPSecConnectionTunnel`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/ipsecConnections/{ipscId}/tunnels/{tunnelId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_ip_sec_connection_tunnel got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "ipscId": ipsc_id,
            "tunnelId": tunnel_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_ip_sec_connection_tunnel_details,
                response_type="IPSecConnectionTunnel")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_ip_sec_connection_tunnel_details,
                response_type="IPSecConnectionTunnel")

    def update_ip_sec_connection_tunnel_shared_secret(self, ipsc_id, tunnel_id, update_ip_sec_connection_tunnel_shared_secret_details, **kwargs):
        """
        Updates the shared secret (pre-shared key) for the specified tunnel.

        **Important:** If you change the shared secret, the tunnel will go down while it's reprovisioned.


        :param str ipsc_id: (required)
            The OCID of the IPSec connection.

        :param str tunnel_id: (required)
            The `OCID`__ of the tunnel.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateIPSecConnectionTunnelSharedSecretDetails update_ip_sec_connection_tunnel_shared_secret_details: (required)
            Details object for updating a IPSec connection tunnel's sharedSecret.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.IPSecConnectionTunnelSharedSecret`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/ipsecConnections/{ipscId}/tunnels/{tunnelId}/sharedSecret"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_ip_sec_connection_tunnel_shared_secret got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "ipscId": ipsc_id,
            "tunnelId": tunnel_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_ip_sec_connection_tunnel_shared_secret_details,
                response_type="IPSecConnectionTunnelSharedSecret")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_ip_sec_connection_tunnel_shared_secret_details,
                response_type="IPSecConnectionTunnelSharedSecret")

    def update_ipv6(self, ipv6_id, update_ipv6_details, **kwargs):
        """
        Updates the specified IPv6. You must specify the object's OCID.
        Use this operation if you want to:

          * Move an IPv6 to a different VNIC in the same subnet.
          * Enable/disable internet access for an IPv6.
          * Change the display name for an IPv6.
          * Update resource tags for an IPv6.


        :param str ipv6_id: (required)
            The `OCID`__ of the IPv6.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateIpv6Details update_ipv6_details: (required)
            IPv6 details to be updated.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.Ipv6`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/ipv6/{ipv6Id}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_ipv6 got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "ipv6Id": ipv6_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_ipv6_details,
                response_type="Ipv6")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_ipv6_details,
                response_type="Ipv6")

    def update_local_peering_gateway(self, local_peering_gateway_id, update_local_peering_gateway_details, **kwargs):
        """
        Updates the specified local peering gateway (LPG).


        :param str local_peering_gateway_id: (required)
            The OCID of the local peering gateway.

        :param UpdateLocalPeeringGatewayDetails update_local_peering_gateway_details: (required)
            Details object for updating a local peering gateway.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.LocalPeeringGateway`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/localPeeringGateways/{localPeeringGatewayId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_local_peering_gateway got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "localPeeringGatewayId": local_peering_gateway_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_local_peering_gateway_details,
                response_type="LocalPeeringGateway")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_local_peering_gateway_details,
                response_type="LocalPeeringGateway")

    def update_nat_gateway(self, nat_gateway_id, update_nat_gateway_details, **kwargs):
        """
        Updates the specified NAT gateway.


        :param str nat_gateway_id: (required)
            The NAT gateway's `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateNatGatewayDetails update_nat_gateway_details: (required)
            Details object for updating a NAT gateway.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.NatGateway`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/natGateways/{natGatewayId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_nat_gateway got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "natGatewayId": nat_gateway_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_nat_gateway_details,
                response_type="NatGateway")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_nat_gateway_details,
                response_type="NatGateway")

    def update_network_security_group(self, network_security_group_id, update_network_security_group_details, **kwargs):
        """
        Updates the specified network security group.

        To add or remove an existing VNIC from the group, use
        :func:`update_vnic`.

        To add a VNIC to the group *when you create the VNIC*, specify the NSG's OCID during creation.
        For example, see the `nsgIds` attribute in :func:`create_vnic_details`.

        To add or remove security rules from the group, use
        :func:`add_network_security_group_security_rules`
        or
        :func:`remove_network_security_group_security_rules`.

        To edit the contents of existing security rules in the group, use
        :func:`update_network_security_group_security_rules`.


        :param str network_security_group_id: (required)
            The `OCID`__ of the network security group.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateNetworkSecurityGroupDetails update_network_security_group_details: (required)
            Details object for updating a network security group.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.NetworkSecurityGroup`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/networkSecurityGroups/{networkSecurityGroupId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_network_security_group got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "networkSecurityGroupId": network_security_group_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_network_security_group_details,
                response_type="NetworkSecurityGroup")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_network_security_group_details,
                response_type="NetworkSecurityGroup")

    def update_network_security_group_security_rules(self, network_security_group_id, update_network_security_group_security_rules_details, **kwargs):
        """
        Updates one or more security rules in the specified network security group.


        :param str network_security_group_id: (required)
            The `OCID`__ of the network security group.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateNetworkSecurityGroupSecurityRulesDetails update_network_security_group_security_rules_details: (required)
            Request with one or more security rules associated with the network security group that
            will be updated.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.UpdatedNetworkSecurityGroupSecurityRules`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/networkSecurityGroups/{networkSecurityGroupId}/actions/updateSecurityRules"
        method = "POST"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_network_security_group_security_rules got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "networkSecurityGroupId": network_security_group_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_network_security_group_security_rules_details,
                response_type="UpdatedNetworkSecurityGroupSecurityRules")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_network_security_group_security_rules_details,
                response_type="UpdatedNetworkSecurityGroupSecurityRules")

    def update_private_ip(self, private_ip_id, update_private_ip_details, **kwargs):
        """
        Updates the specified private IP. You must specify the object's OCID.
        Use this operation if you want to:

          - Move a secondary private IP to a different VNIC in the same subnet.
          - Change the display name for a secondary private IP.
          - Change the hostname for a secondary private IP.

        This operation cannot be used with primary private IPs.
        To update the hostname for the primary IP on a VNIC, use
        :func:`update_vnic`.


        :param str private_ip_id: (required)
            The OCID of the private IP.

        :param UpdatePrivateIpDetails update_private_ip_details: (required)
            Private IP details.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.PrivateIp`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/privateIps/{privateIpId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_private_ip got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "privateIpId": private_ip_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_private_ip_details,
                response_type="PrivateIp")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_private_ip_details,
                response_type="PrivateIp")

    def update_public_ip(self, public_ip_id, update_public_ip_details, **kwargs):
        """
        Updates the specified public IP. You must specify the object's OCID. Use this operation if you want to:

        * Assign a reserved public IP in your pool to a private IP.
        * Move a reserved public IP to a different private IP.
        * Unassign a reserved public IP from a private IP (which returns it to your pool
        of reserved public IPs).
        * Change the display name or tags for a public IP.

        Assigning, moving, and unassigning a reserved public IP are asynchronous
        operations. Poll the public IP's `lifecycleState` to determine if the operation
        succeeded.

        **Note:** When moving a reserved public IP, the target private IP
        must not already have a public IP with `lifecycleState` = ASSIGNING or ASSIGNED. If it
        does, an error is returned. Also, the initial unassignment from the original
        private IP always succeeds, but the assignment to the target private IP is asynchronous and
        could fail silently (for example, if the target private IP is deleted or has a different public IP
        assigned to it in the interim). If that occurs, the public IP remains unassigned and its
        `lifecycleState` switches to AVAILABLE (it is not reassigned to its original private IP).
        You must poll the public IP's `lifecycleState` to determine if the move succeeded.

        Regarding ephemeral public IPs:

        * If you want to assign an ephemeral public IP to a primary private IP, use
        :func:`create_public_ip`.
        * You can't move an ephemeral public IP to a different private IP.
        * If you want to unassign an ephemeral public IP from its private IP, use
        :func:`delete_public_ip`, which
        unassigns and deletes the ephemeral public IP.

        **Note:** If a public IP is assigned to a secondary private
        IP (see :class:`PrivateIp`), and you move that secondary
        private IP to another VNIC, the public IP moves with it.

        **Note:** There's a limit to the number of :class:`PublicIp`
        a VNIC or instance can have. If you try to move a reserved public IP
        to a VNIC or instance that has already reached its public IP limit, an error is
        returned. For information about the public IP limits, see
        `Public IP Addresses`__.

        __ https://docs.cloud.oracle.com/Content/Network/Tasks/managingpublicIPs.htm


        :param str public_ip_id: (required)
            The OCID of the public IP.

        :param UpdatePublicIpDetails update_public_ip_details: (required)
            Public IP details.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.PublicIp`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/publicIps/{publicIpId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_public_ip got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "publicIpId": public_ip_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_public_ip_details,
                response_type="PublicIp")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_public_ip_details,
                response_type="PublicIp")

    def update_remote_peering_connection(self, remote_peering_connection_id, update_remote_peering_connection_details, **kwargs):
        """
        Updates the specified remote peering connection (RPC).


        :param str remote_peering_connection_id: (required)
            The OCID of the remote peering connection (RPC).

        :param UpdateRemotePeeringConnectionDetails update_remote_peering_connection_details: (required)
            Request to the update the peering connection to remote region

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.RemotePeeringConnection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/remotePeeringConnections/{remotePeeringConnectionId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_remote_peering_connection got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "remotePeeringConnectionId": remote_peering_connection_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_remote_peering_connection_details,
                response_type="RemotePeeringConnection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_remote_peering_connection_details,
                response_type="RemotePeeringConnection")

    def update_route_table(self, rt_id, update_route_table_details, **kwargs):
        """
        Updates the specified route table's display name or route rules.
        Avoid entering confidential information.

        Note that the `routeRules` object you provide replaces the entire existing set of rules.


        :param str rt_id: (required)
            The OCID of the route table.

        :param UpdateRouteTableDetails update_route_table_details: (required)
            Details object for updating a route table.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.RouteTable`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/routeTables/{rtId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_route_table got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "rtId": rt_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_route_table_details,
                response_type="RouteTable")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_route_table_details,
                response_type="RouteTable")

    def update_security_list(self, security_list_id, update_security_list_details, **kwargs):
        """
        Updates the specified security list's display name or rules.
        Avoid entering confidential information.

        Note that the `egressSecurityRules` or `ingressSecurityRules` objects you provide replace the entire
        existing objects.


        :param str security_list_id: (required)
            The OCID of the security list.

        :param UpdateSecurityListDetails update_security_list_details: (required)
            Updated details for the security list.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.SecurityList`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/securityLists/{securityListId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_security_list got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "securityListId": security_list_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_security_list_details,
                response_type="SecurityList")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_security_list_details,
                response_type="SecurityList")

    def update_service_gateway(self, service_gateway_id, update_service_gateway_details, **kwargs):
        """
        Updates the specified service gateway. The information you provide overwrites the existing
        attributes of the gateway.


        :param str service_gateway_id: (required)
            The service gateway's `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateServiceGatewayDetails update_service_gateway_details: (required)
            Details object for updating a service gateway.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.ServiceGateway`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/serviceGateways/{serviceGatewayId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_service_gateway got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "serviceGatewayId": service_gateway_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_service_gateway_details,
                response_type="ServiceGateway")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_service_gateway_details,
                response_type="ServiceGateway")

    def update_subnet(self, subnet_id, update_subnet_details, **kwargs):
        """
        Updates the specified subnet.


        :param str subnet_id: (required)
            The OCID of the subnet.

        :param UpdateSubnetDetails update_subnet_details: (required)
            Details object for updating a subnet.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.Subnet`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/subnets/{subnetId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_subnet got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "subnetId": subnet_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_subnet_details,
                response_type="Subnet")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_subnet_details,
                response_type="Subnet")

    def update_tunnel_cpe_device_config(self, ipsc_id, tunnel_id, update_tunnel_cpe_device_config_details, **kwargs):
        """
        Creates or updates the set of CPE configuration answers for the specified tunnel.
        The answers correlate to the questions that are specific to the CPE device type (see the
        `parameters` attribute of :class:`CpeDeviceShapeDetail`).


        :param str ipsc_id: (required)
            The OCID of the IPSec connection.

        :param str tunnel_id: (required)
            The `OCID`__ of the tunnel.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateTunnelCpeDeviceConfigDetails update_tunnel_cpe_device_config_details: (required)
            Request to input the tunnel's cpe configuration parameters

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.TunnelCpeDeviceConfig`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/ipsecConnections/{ipscId}/tunnels/{tunnelId}/tunnelDeviceConfig"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_retry_token",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_tunnel_cpe_device_config got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "ipscId": ipsc_id,
            "tunnelId": tunnel_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_tunnel_cpe_device_config_details,
                response_type="TunnelCpeDeviceConfig")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_tunnel_cpe_device_config_details,
                response_type="TunnelCpeDeviceConfig")

    def update_vcn(self, vcn_id, update_vcn_details, **kwargs):
        """
        Updates the specified VCN.


        :param str vcn_id: (required)
            The `OCID`__ of the VCN.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateVcnDetails update_vcn_details: (required)
            Details object for updating a VCN.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.Vcn`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/vcns/{vcnId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_vcn got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "vcnId": vcn_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_vcn_details,
                response_type="Vcn")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_vcn_details,
                response_type="Vcn")

    def update_virtual_circuit(self, virtual_circuit_id, update_virtual_circuit_details, **kwargs):
        """
        Updates the specified virtual circuit. This can be called by
        either the customer who owns the virtual circuit, or the
        provider (when provisioning or de-provisioning the virtual
        circuit from their end). The documentation for
        :func:`update_virtual_circuit_details`
        indicates who can update each property of the virtual circuit.

        **Important:** If the virtual circuit is working and in the
        PROVISIONED state, updating any of the network-related properties
        (such as the DRG being used, the BGP ASN, and so on) will cause the virtual
        circuit's state to switch to PROVISIONING and the related BGP
        session to go down. After Oracle re-provisions the virtual circuit,
        its state will return to PROVISIONED. Make sure you confirm that
        the associated BGP session is back up. For more information
        about the various states and how to test connectivity, see
        `FastConnect Overview`__.

        To change the list of public IP prefixes for a public virtual circuit,
        use :func:`bulk_add_virtual_circuit_public_prefixes`
        and
        :func:`bulk_delete_virtual_circuit_public_prefixes`.
        Updating the list of prefixes does NOT cause the BGP session to go down. However,
        Oracle must verify the customer's ownership of each added prefix before
        traffic for that prefix will flow across the virtual circuit.

        __ https://docs.cloud.oracle.com/Content/Network/Concepts/fastconnect.htm


        :param str virtual_circuit_id: (required)
            The OCID of the virtual circuit.

        :param UpdateVirtualCircuitDetails update_virtual_circuit_details: (required)
            Update VirtualCircuit fields.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.VirtualCircuit`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/virtualCircuits/{virtualCircuitId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_virtual_circuit got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "virtualCircuitId": virtual_circuit_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_virtual_circuit_details,
                response_type="VirtualCircuit")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_virtual_circuit_details,
                response_type="VirtualCircuit")

    def update_vlan(self, vlan_id, update_vlan_details, **kwargs):
        """
        Updates the specified VLAN. This could result in changes to all
        the VNICs in the VLAN, which can take time. During that transition
        period, the VLAN will be in the UPDATING state.


        :param str vlan_id: (required)
            The `OCID`__ of the VLAN.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateVlanDetails update_vlan_details: (required)
            Details object for updating a subnet.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.Vlan`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/vlans/{vlanId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_vlan got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "vlanId": vlan_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_vlan_details,
                response_type="Vlan")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_vlan_details,
                response_type="Vlan")

    def update_vnic(self, vnic_id, update_vnic_details, **kwargs):
        """
        Updates the specified VNIC.


        :param str vnic_id: (required)
            The OCID of the VNIC.

        :param UpdateVnicDetails update_vnic_details: (required)
            Details object for updating a VNIC.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.Vnic`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/vnics/{vnicId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_vnic got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "vnicId": vnic_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_vnic_details,
                response_type="Vnic")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_vnic_details,
                response_type="Vnic")
