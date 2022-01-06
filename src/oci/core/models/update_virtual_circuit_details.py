# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateVirtualCircuitDetails(object):
    """
    UpdateVirtualCircuitDetails model.
    """

    #: A constant which can be used with the routing_policy property of a UpdateVirtualCircuitDetails.
    #: This constant has a value of "ORACLE_SERVICE_NETWORK"
    ROUTING_POLICY_ORACLE_SERVICE_NETWORK = "ORACLE_SERVICE_NETWORK"

    #: A constant which can be used with the routing_policy property of a UpdateVirtualCircuitDetails.
    #: This constant has a value of "REGIONAL"
    ROUTING_POLICY_REGIONAL = "REGIONAL"

    #: A constant which can be used with the routing_policy property of a UpdateVirtualCircuitDetails.
    #: This constant has a value of "MARKET_LEVEL"
    ROUTING_POLICY_MARKET_LEVEL = "MARKET_LEVEL"

    #: A constant which can be used with the routing_policy property of a UpdateVirtualCircuitDetails.
    #: This constant has a value of "GLOBAL"
    ROUTING_POLICY_GLOBAL = "GLOBAL"

    #: A constant which can be used with the provider_state property of a UpdateVirtualCircuitDetails.
    #: This constant has a value of "ACTIVE"
    PROVIDER_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the provider_state property of a UpdateVirtualCircuitDetails.
    #: This constant has a value of "INACTIVE"
    PROVIDER_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the ip_mtu property of a UpdateVirtualCircuitDetails.
    #: This constant has a value of "MTU_1500"
    IP_MTU_MTU_1500 = "MTU_1500"

    #: A constant which can be used with the ip_mtu property of a UpdateVirtualCircuitDetails.
    #: This constant has a value of "MTU_9000"
    IP_MTU_MTU_9000 = "MTU_9000"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateVirtualCircuitDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param bandwidth_shape_name:
            The value to assign to the bandwidth_shape_name property of this UpdateVirtualCircuitDetails.
        :type bandwidth_shape_name: str

        :param cross_connect_mappings:
            The value to assign to the cross_connect_mappings property of this UpdateVirtualCircuitDetails.
        :type cross_connect_mappings: list[oci.core.models.CrossConnectMapping]

        :param routing_policy:
            The value to assign to the routing_policy property of this UpdateVirtualCircuitDetails.
            Allowed values for items in this list are: "ORACLE_SERVICE_NETWORK", "REGIONAL", "MARKET_LEVEL", "GLOBAL"
        :type routing_policy: list[str]

        :param customer_bgp_asn:
            The value to assign to the customer_bgp_asn property of this UpdateVirtualCircuitDetails.
        :type customer_bgp_asn: int

        :param customer_asn:
            The value to assign to the customer_asn property of this UpdateVirtualCircuitDetails.
        :type customer_asn: int

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateVirtualCircuitDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this UpdateVirtualCircuitDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateVirtualCircuitDetails.
        :type freeform_tags: dict(str, str)

        :param gateway_id:
            The value to assign to the gateway_id property of this UpdateVirtualCircuitDetails.
        :type gateway_id: str

        :param provider_state:
            The value to assign to the provider_state property of this UpdateVirtualCircuitDetails.
            Allowed values for this property are: "ACTIVE", "INACTIVE"
        :type provider_state: str

        :param provider_service_key_name:
            The value to assign to the provider_service_key_name property of this UpdateVirtualCircuitDetails.
        :type provider_service_key_name: str

        :param reference_comment:
            The value to assign to the reference_comment property of this UpdateVirtualCircuitDetails.
        :type reference_comment: str

        :param ip_mtu:
            The value to assign to the ip_mtu property of this UpdateVirtualCircuitDetails.
            Allowed values for this property are: "MTU_1500", "MTU_9000"
        :type ip_mtu: str

        """
        self.swagger_types = {
            'bandwidth_shape_name': 'str',
            'cross_connect_mappings': 'list[CrossConnectMapping]',
            'routing_policy': 'list[str]',
            'customer_bgp_asn': 'int',
            'customer_asn': 'int',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'gateway_id': 'str',
            'provider_state': 'str',
            'provider_service_key_name': 'str',
            'reference_comment': 'str',
            'ip_mtu': 'str'
        }

        self.attribute_map = {
            'bandwidth_shape_name': 'bandwidthShapeName',
            'cross_connect_mappings': 'crossConnectMappings',
            'routing_policy': 'routingPolicy',
            'customer_bgp_asn': 'customerBgpAsn',
            'customer_asn': 'customerAsn',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'gateway_id': 'gatewayId',
            'provider_state': 'providerState',
            'provider_service_key_name': 'providerServiceKeyName',
            'reference_comment': 'referenceComment',
            'ip_mtu': 'ipMtu'
        }

        self._bandwidth_shape_name = None
        self._cross_connect_mappings = None
        self._routing_policy = None
        self._customer_bgp_asn = None
        self._customer_asn = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._gateway_id = None
        self._provider_state = None
        self._provider_service_key_name = None
        self._reference_comment = None
        self._ip_mtu = None

    @property
    def bandwidth_shape_name(self):
        """
        Gets the bandwidth_shape_name of this UpdateVirtualCircuitDetails.
        The provisioned data rate of the connection. To get a list of the
        available bandwidth levels (that is, shapes), see
        :func:`list_fast_connect_provider_virtual_circuit_bandwidth_shapes`.
        To be updated only by the customer who owns the virtual circuit.


        :return: The bandwidth_shape_name of this UpdateVirtualCircuitDetails.
        :rtype: str
        """
        return self._bandwidth_shape_name

    @bandwidth_shape_name.setter
    def bandwidth_shape_name(self, bandwidth_shape_name):
        """
        Sets the bandwidth_shape_name of this UpdateVirtualCircuitDetails.
        The provisioned data rate of the connection. To get a list of the
        available bandwidth levels (that is, shapes), see
        :func:`list_fast_connect_provider_virtual_circuit_bandwidth_shapes`.
        To be updated only by the customer who owns the virtual circuit.


        :param bandwidth_shape_name: The bandwidth_shape_name of this UpdateVirtualCircuitDetails.
        :type: str
        """
        self._bandwidth_shape_name = bandwidth_shape_name

    @property
    def cross_connect_mappings(self):
        """
        Gets the cross_connect_mappings of this UpdateVirtualCircuitDetails.
        An array of mappings, each containing properties for a cross-connect or
        cross-connect group associated with this virtual circuit.

        The customer and provider can update different properties in the mapping
        depending on the situation. See the description of the
        :class:`CrossConnectMapping`.


        :return: The cross_connect_mappings of this UpdateVirtualCircuitDetails.
        :rtype: list[oci.core.models.CrossConnectMapping]
        """
        return self._cross_connect_mappings

    @cross_connect_mappings.setter
    def cross_connect_mappings(self, cross_connect_mappings):
        """
        Sets the cross_connect_mappings of this UpdateVirtualCircuitDetails.
        An array of mappings, each containing properties for a cross-connect or
        cross-connect group associated with this virtual circuit.

        The customer and provider can update different properties in the mapping
        depending on the situation. See the description of the
        :class:`CrossConnectMapping`.


        :param cross_connect_mappings: The cross_connect_mappings of this UpdateVirtualCircuitDetails.
        :type: list[oci.core.models.CrossConnectMapping]
        """
        self._cross_connect_mappings = cross_connect_mappings

    @property
    def routing_policy(self):
        """
        Gets the routing_policy of this UpdateVirtualCircuitDetails.
        The routing policy sets how routing information about the Oracle cloud is shared over a public virtual circuit.
        Policies available are: `ORACLE_SERVICE_NETWORK`, `REGIONAL`, `MARKET_LEVEL`, and `GLOBAL`.
        See `Route Filtering`__ for details.
        By default, routing information is shared for all routes in the same market.

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/routingonprem.htm#route_filtering

        Allowed values for items in this list are: "ORACLE_SERVICE_NETWORK", "REGIONAL", "MARKET_LEVEL", "GLOBAL"


        :return: The routing_policy of this UpdateVirtualCircuitDetails.
        :rtype: list[str]
        """
        return self._routing_policy

    @routing_policy.setter
    def routing_policy(self, routing_policy):
        """
        Sets the routing_policy of this UpdateVirtualCircuitDetails.
        The routing policy sets how routing information about the Oracle cloud is shared over a public virtual circuit.
        Policies available are: `ORACLE_SERVICE_NETWORK`, `REGIONAL`, `MARKET_LEVEL`, and `GLOBAL`.
        See `Route Filtering`__ for details.
        By default, routing information is shared for all routes in the same market.

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/routingonprem.htm#route_filtering


        :param routing_policy: The routing_policy of this UpdateVirtualCircuitDetails.
        :type: list[str]
        """
        allowed_values = ["ORACLE_SERVICE_NETWORK", "REGIONAL", "MARKET_LEVEL", "GLOBAL"]

        if routing_policy and routing_policy is not NONE_SENTINEL:
            for value in routing_policy:
                if not value_allowed_none_or_none_sentinel(value, allowed_values):
                    raise ValueError(
                        "Invalid value for `routing_policy`, must be None or one of {0}"
                        .format(allowed_values)
                    )
        self._routing_policy = routing_policy

    @property
    def customer_bgp_asn(self):
        """
        Gets the customer_bgp_asn of this UpdateVirtualCircuitDetails.
        Deprecated. Instead use `customerAsn`.
        If you specify values for both, the request will be rejected.


        :return: The customer_bgp_asn of this UpdateVirtualCircuitDetails.
        :rtype: int
        """
        return self._customer_bgp_asn

    @customer_bgp_asn.setter
    def customer_bgp_asn(self, customer_bgp_asn):
        """
        Sets the customer_bgp_asn of this UpdateVirtualCircuitDetails.
        Deprecated. Instead use `customerAsn`.
        If you specify values for both, the request will be rejected.


        :param customer_bgp_asn: The customer_bgp_asn of this UpdateVirtualCircuitDetails.
        :type: int
        """
        self._customer_bgp_asn = customer_bgp_asn

    @property
    def customer_asn(self):
        """
        Gets the customer_asn of this UpdateVirtualCircuitDetails.
        The BGP ASN of the network at the other end of the BGP
        session from Oracle.

        If the BGP session is from the customer's edge router to Oracle, the
        required value is the customer's ASN, and it can be updated only
        by the customer.

        If the BGP session is from the provider's edge router to Oracle, the
        required value is the provider's ASN, and it can be updated only
        by the provider.

        Can be a 2-byte or 4-byte ASN. Uses \"asplain\" format.


        :return: The customer_asn of this UpdateVirtualCircuitDetails.
        :rtype: int
        """
        return self._customer_asn

    @customer_asn.setter
    def customer_asn(self, customer_asn):
        """
        Sets the customer_asn of this UpdateVirtualCircuitDetails.
        The BGP ASN of the network at the other end of the BGP
        session from Oracle.

        If the BGP session is from the customer's edge router to Oracle, the
        required value is the customer's ASN, and it can be updated only
        by the customer.

        If the BGP session is from the provider's edge router to Oracle, the
        required value is the provider's ASN, and it can be updated only
        by the provider.

        Can be a 2-byte or 4-byte ASN. Uses \"asplain\" format.


        :param customer_asn: The customer_asn of this UpdateVirtualCircuitDetails.
        :type: int
        """
        self._customer_asn = customer_asn

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateVirtualCircuitDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateVirtualCircuitDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateVirtualCircuitDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateVirtualCircuitDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateVirtualCircuitDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this UpdateVirtualCircuitDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateVirtualCircuitDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this UpdateVirtualCircuitDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateVirtualCircuitDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateVirtualCircuitDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateVirtualCircuitDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateVirtualCircuitDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def gateway_id(self):
        """
        Gets the gateway_id of this UpdateVirtualCircuitDetails.
        The `OCID`__ of the :class:`Drg`
        that this private virtual circuit uses.

        To be updated only by the customer who owns the virtual circuit.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The gateway_id of this UpdateVirtualCircuitDetails.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        """
        Sets the gateway_id of this UpdateVirtualCircuitDetails.
        The `OCID`__ of the :class:`Drg`
        that this private virtual circuit uses.

        To be updated only by the customer who owns the virtual circuit.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param gateway_id: The gateway_id of this UpdateVirtualCircuitDetails.
        :type: str
        """
        self._gateway_id = gateway_id

    @property
    def provider_state(self):
        """
        Gets the provider_state of this UpdateVirtualCircuitDetails.
        The provider's state in relation to this virtual circuit. Relevant only
        if the customer is using FastConnect via a provider. ACTIVE
        means the provider has provisioned the virtual circuit from their
        end. INACTIVE means the provider has not yet provisioned the virtual
        circuit, or has de-provisioned it.

        To be updated only by the provider.

        Allowed values for this property are: "ACTIVE", "INACTIVE"


        :return: The provider_state of this UpdateVirtualCircuitDetails.
        :rtype: str
        """
        return self._provider_state

    @provider_state.setter
    def provider_state(self, provider_state):
        """
        Sets the provider_state of this UpdateVirtualCircuitDetails.
        The provider's state in relation to this virtual circuit. Relevant only
        if the customer is using FastConnect via a provider. ACTIVE
        means the provider has provisioned the virtual circuit from their
        end. INACTIVE means the provider has not yet provisioned the virtual
        circuit, or has de-provisioned it.

        To be updated only by the provider.


        :param provider_state: The provider_state of this UpdateVirtualCircuitDetails.
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE"]
        if not value_allowed_none_or_none_sentinel(provider_state, allowed_values):
            raise ValueError(
                "Invalid value for `provider_state`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._provider_state = provider_state

    @property
    def provider_service_key_name(self):
        """
        Gets the provider_service_key_name of this UpdateVirtualCircuitDetails.
        The service key name offered by the provider (if the customer is connecting via a provider).


        :return: The provider_service_key_name of this UpdateVirtualCircuitDetails.
        :rtype: str
        """
        return self._provider_service_key_name

    @provider_service_key_name.setter
    def provider_service_key_name(self, provider_service_key_name):
        """
        Sets the provider_service_key_name of this UpdateVirtualCircuitDetails.
        The service key name offered by the provider (if the customer is connecting via a provider).


        :param provider_service_key_name: The provider_service_key_name of this UpdateVirtualCircuitDetails.
        :type: str
        """
        self._provider_service_key_name = provider_service_key_name

    @property
    def reference_comment(self):
        """
        Gets the reference_comment of this UpdateVirtualCircuitDetails.
        Provider-supplied reference information about this virtual circuit.
        Relevant only if the customer is using FastConnect via a provider.

        To be updated only by the provider.


        :return: The reference_comment of this UpdateVirtualCircuitDetails.
        :rtype: str
        """
        return self._reference_comment

    @reference_comment.setter
    def reference_comment(self, reference_comment):
        """
        Sets the reference_comment of this UpdateVirtualCircuitDetails.
        Provider-supplied reference information about this virtual circuit.
        Relevant only if the customer is using FastConnect via a provider.

        To be updated only by the provider.


        :param reference_comment: The reference_comment of this UpdateVirtualCircuitDetails.
        :type: str
        """
        self._reference_comment = reference_comment

    @property
    def ip_mtu(self):
        """
        Gets the ip_mtu of this UpdateVirtualCircuitDetails.
        The layer 3 IP MTU to use on this virtual circuit.

        Allowed values for this property are: "MTU_1500", "MTU_9000"


        :return: The ip_mtu of this UpdateVirtualCircuitDetails.
        :rtype: str
        """
        return self._ip_mtu

    @ip_mtu.setter
    def ip_mtu(self, ip_mtu):
        """
        Sets the ip_mtu of this UpdateVirtualCircuitDetails.
        The layer 3 IP MTU to use on this virtual circuit.


        :param ip_mtu: The ip_mtu of this UpdateVirtualCircuitDetails.
        :type: str
        """
        allowed_values = ["MTU_1500", "MTU_9000"]
        if not value_allowed_none_or_none_sentinel(ip_mtu, allowed_values):
            raise ValueError(
                "Invalid value for `ip_mtu`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._ip_mtu = ip_mtu

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
