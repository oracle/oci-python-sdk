# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class VirtualCircuit(object):

    def __init__(self):

        self.swagger_types = {
            'bandwidth_shape_name': 'str',
            'bgp_session_state': 'str',
            'compartment_id': 'str',
            'cross_connect_mappings': 'list[CrossConnectMapping]',
            'customer_bgp_asn': 'int',
            'display_name': 'str',
            'gateway_id': 'str',
            'id': 'str',
            'lifecycle_state': 'str',
            'oracle_bgp_asn': 'int',
            'provider_name': 'str',
            'provider_service_name': 'str',
            'provider_state': 'str',
            'reference_comment': 'str',
            'region': 'str',
            'time_created': 'datetime',
            'type': 'str'
        }

        self.attribute_map = {
            'bandwidth_shape_name': 'bandwidthShapeName',
            'bgp_session_state': 'bgpSessionState',
            'compartment_id': 'compartmentId',
            'cross_connect_mappings': 'crossConnectMappings',
            'customer_bgp_asn': 'customerBgpAsn',
            'display_name': 'displayName',
            'gateway_id': 'gatewayId',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'oracle_bgp_asn': 'oracleBgpAsn',
            'provider_name': 'providerName',
            'provider_service_name': 'providerServiceName',
            'provider_state': 'providerState',
            'reference_comment': 'referenceComment',
            'region': 'region',
            'time_created': 'timeCreated',
            'type': 'type'
        }

        self._bandwidth_shape_name = None
        self._bgp_session_state = None
        self._compartment_id = None
        self._cross_connect_mappings = None
        self._customer_bgp_asn = None
        self._display_name = None
        self._gateway_id = None
        self._id = None
        self._lifecycle_state = None
        self._oracle_bgp_asn = None
        self._provider_name = None
        self._provider_service_name = None
        self._provider_state = None
        self._reference_comment = None
        self._region = None
        self._time_created = None
        self._type = None

    @property
    def bandwidth_shape_name(self):
        """
        Gets the bandwidth_shape_name of this VirtualCircuit.
        The provisioned data rate of the connection.


        :return: The bandwidth_shape_name of this VirtualCircuit.
        :rtype: str
        """
        return self._bandwidth_shape_name

    @bandwidth_shape_name.setter
    def bandwidth_shape_name(self, bandwidth_shape_name):
        """
        Sets the bandwidth_shape_name of this VirtualCircuit.
        The provisioned data rate of the connection.


        :param bandwidth_shape_name: The bandwidth_shape_name of this VirtualCircuit.
        :type: str
        """
        self._bandwidth_shape_name = bandwidth_shape_name

    @property
    def bgp_session_state(self):
        """
        Gets the bgp_session_state of this VirtualCircuit.
        The state of the BGP session associated with the virtual circuit.

        Allowed values for this property are: "UP", "DOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The bgp_session_state of this VirtualCircuit.
        :rtype: str
        """
        return self._bgp_session_state

    @bgp_session_state.setter
    def bgp_session_state(self, bgp_session_state):
        """
        Sets the bgp_session_state of this VirtualCircuit.
        The state of the BGP session associated with the virtual circuit.


        :param bgp_session_state: The bgp_session_state of this VirtualCircuit.
        :type: str
        """
        allowed_values = ["UP", "DOWN"]
        if bgp_session_state not in allowed_values:
            bgp_session_state = 'UNKNOWN_ENUM_VALUE'
        self._bgp_session_state = bgp_session_state

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this VirtualCircuit.
        The OCID of the compartment containing the virtual circuit.


        :return: The compartment_id of this VirtualCircuit.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this VirtualCircuit.
        The OCID of the compartment containing the virtual circuit.


        :param compartment_id: The compartment_id of this VirtualCircuit.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def cross_connect_mappings(self):
        """
        Gets the cross_connect_mappings of this VirtualCircuit.
        An array of mappings, each containing properties for a
        cross-connect or cross-connect group that is associated with this
        virtual circuit.


        :return: The cross_connect_mappings of this VirtualCircuit.
        :rtype: list[CrossConnectMapping]
        """
        return self._cross_connect_mappings

    @cross_connect_mappings.setter
    def cross_connect_mappings(self, cross_connect_mappings):
        """
        Sets the cross_connect_mappings of this VirtualCircuit.
        An array of mappings, each containing properties for a
        cross-connect or cross-connect group that is associated with this
        virtual circuit.


        :param cross_connect_mappings: The cross_connect_mappings of this VirtualCircuit.
        :type: list[CrossConnectMapping]
        """
        self._cross_connect_mappings = cross_connect_mappings

    @property
    def customer_bgp_asn(self):
        """
        Gets the customer_bgp_asn of this VirtualCircuit.
        The BGP ASN of the network at the other end of the BGP
        session from Oracle. If the session is between the customer's
        edge router and Oracle, the value is the customer's ASN. If the BGP
        session is between the provider's edge router and Oracle, the value
        is the provider's ASN.


        :return: The customer_bgp_asn of this VirtualCircuit.
        :rtype: int
        """
        return self._customer_bgp_asn

    @customer_bgp_asn.setter
    def customer_bgp_asn(self, customer_bgp_asn):
        """
        Sets the customer_bgp_asn of this VirtualCircuit.
        The BGP ASN of the network at the other end of the BGP
        session from Oracle. If the session is between the customer's
        edge router and Oracle, the value is the customer's ASN. If the BGP
        session is between the provider's edge router and Oracle, the value
        is the provider's ASN.


        :param customer_bgp_asn: The customer_bgp_asn of this VirtualCircuit.
        :type: int
        """
        self._customer_bgp_asn = customer_bgp_asn

    @property
    def display_name(self):
        """
        Gets the display_name of this VirtualCircuit.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :return: The display_name of this VirtualCircuit.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this VirtualCircuit.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :param display_name: The display_name of this VirtualCircuit.
        :type: str
        """
        self._display_name = display_name

    @property
    def gateway_id(self):
        """
        Gets the gateway_id of this VirtualCircuit.
        The OCID of the customer's :class:`Drg`
        that this virtual circuit uses.


        :return: The gateway_id of this VirtualCircuit.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        """
        Sets the gateway_id of this VirtualCircuit.
        The OCID of the customer's :class:`Drg`
        that this virtual circuit uses.


        :param gateway_id: The gateway_id of this VirtualCircuit.
        :type: str
        """
        self._gateway_id = gateway_id

    @property
    def id(self):
        """
        Gets the id of this VirtualCircuit.
        The virtual circuit's Oracle ID (OCID).


        :return: The id of this VirtualCircuit.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VirtualCircuit.
        The virtual circuit's Oracle ID (OCID).


        :param id: The id of this VirtualCircuit.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this VirtualCircuit.
        The virtual circuit's current state. For information about
        the different states, see
        `FastConnect Overview`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/fastconnect.htm

        Allowed values for this property are: "PENDING_PROVIDER", "VERIFYING", "PROVISIONING", "PROVISIONED", "FAILED", "INACTIVE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this VirtualCircuit.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this VirtualCircuit.
        The virtual circuit's current state. For information about
        the different states, see
        `FastConnect Overview`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/fastconnect.htm


        :param lifecycle_state: The lifecycle_state of this VirtualCircuit.
        :type: str
        """
        allowed_values = ["PENDING_PROVIDER", "VERIFYING", "PROVISIONING", "PROVISIONED", "FAILED", "INACTIVE", "TERMINATING", "TERMINATED"]
        if lifecycle_state not in allowed_values:
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def oracle_bgp_asn(self):
        """
        Gets the oracle_bgp_asn of this VirtualCircuit.
        The Oracle BGP ASN.


        :return: The oracle_bgp_asn of this VirtualCircuit.
        :rtype: int
        """
        return self._oracle_bgp_asn

    @oracle_bgp_asn.setter
    def oracle_bgp_asn(self, oracle_bgp_asn):
        """
        Sets the oracle_bgp_asn of this VirtualCircuit.
        The Oracle BGP ASN.


        :param oracle_bgp_asn: The oracle_bgp_asn of this VirtualCircuit.
        :type: int
        """
        self._oracle_bgp_asn = oracle_bgp_asn

    @property
    def provider_name(self):
        """
        Gets the provider_name of this VirtualCircuit.
        The name of the provider (if the customer is connecting via a provider).


        :return: The provider_name of this VirtualCircuit.
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """
        Sets the provider_name of this VirtualCircuit.
        The name of the provider (if the customer is connecting via a provider).


        :param provider_name: The provider_name of this VirtualCircuit.
        :type: str
        """
        self._provider_name = provider_name

    @property
    def provider_service_name(self):
        """
        Gets the provider_service_name of this VirtualCircuit.
        The name of the service offered by the provider (if the customer is connecting via a provider).


        :return: The provider_service_name of this VirtualCircuit.
        :rtype: str
        """
        return self._provider_service_name

    @provider_service_name.setter
    def provider_service_name(self, provider_service_name):
        """
        Sets the provider_service_name of this VirtualCircuit.
        The name of the service offered by the provider (if the customer is connecting via a provider).


        :param provider_service_name: The provider_service_name of this VirtualCircuit.
        :type: str
        """
        self._provider_service_name = provider_service_name

    @property
    def provider_state(self):
        """
        Gets the provider_state of this VirtualCircuit.
        The provider's state in relation to this virtual circuit (if the
        customer is connecting via a provider). ACTIVE means
        the provider has provisioned the virtual circuit from their end.
        INACTIVE means the provider has not yet provisioned the virtual
        circuit, or has de-provisioned it.

        Allowed values for this property are: "ACTIVE", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The provider_state of this VirtualCircuit.
        :rtype: str
        """
        return self._provider_state

    @provider_state.setter
    def provider_state(self, provider_state):
        """
        Sets the provider_state of this VirtualCircuit.
        The provider's state in relation to this virtual circuit (if the
        customer is connecting via a provider). ACTIVE means
        the provider has provisioned the virtual circuit from their end.
        INACTIVE means the provider has not yet provisioned the virtual
        circuit, or has de-provisioned it.


        :param provider_state: The provider_state of this VirtualCircuit.
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE"]
        if provider_state not in allowed_values:
            provider_state = 'UNKNOWN_ENUM_VALUE'
        self._provider_state = provider_state

    @property
    def reference_comment(self):
        """
        Gets the reference_comment of this VirtualCircuit.
        Provider-supplied reference information about this virtual circuit
        (if the customer is connecting via a provider).


        :return: The reference_comment of this VirtualCircuit.
        :rtype: str
        """
        return self._reference_comment

    @reference_comment.setter
    def reference_comment(self, reference_comment):
        """
        Sets the reference_comment of this VirtualCircuit.
        Provider-supplied reference information about this virtual circuit
        (if the customer is connecting via a provider).


        :param reference_comment: The reference_comment of this VirtualCircuit.
        :type: str
        """
        self._reference_comment = reference_comment

    @property
    def region(self):
        """
        Gets the region of this VirtualCircuit.
        The Oracle Bare Metal Cloud Services region where this virtual
        circuit is located.


        :return: The region of this VirtualCircuit.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this VirtualCircuit.
        The Oracle Bare Metal Cloud Services region where this virtual
        circuit is located.


        :param region: The region of this VirtualCircuit.
        :type: str
        """
        self._region = region

    @property
    def time_created(self):
        """
        Gets the time_created of this VirtualCircuit.
        The date and time the virtual circuit was created,
        in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this VirtualCircuit.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this VirtualCircuit.
        The date and time the virtual circuit was created,
        in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this VirtualCircuit.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def type(self):
        """
        Gets the type of this VirtualCircuit.
        The type of IP addresses used in this virtual circuit. PRIVATE means
        `RFC 1918`__ addresses
        (10.0.0.0/8, 172.16/12, and 192.168/16). Only PRIVATE is supported.

        __ https://tools.ietf.org/html/rfc1918

        Allowed values for this property are: "PUBLIC", "PRIVATE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this VirtualCircuit.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this VirtualCircuit.
        The type of IP addresses used in this virtual circuit. PRIVATE means
        `RFC 1918`__ addresses
        (10.0.0.0/8, 172.16/12, and 192.168/16). Only PRIVATE is supported.

        __ https://tools.ietf.org/html/rfc1918


        :param type: The type of this VirtualCircuit.
        :type: str
        """
        allowed_values = ["PUBLIC", "PRIVATE"]
        if type not in allowed_values:
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
