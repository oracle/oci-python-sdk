# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VirtualCircuit(object):
    """
    For use with Oracle Cloud Infrastructure FastConnect.

    A virtual circuit is an isolated network path that runs over one or more physical
    network connections to provide a single, logical connection between the edge router
    on the customer's existing network and Oracle Cloud Infrastructure. *Private*
    virtual circuits support private peering, and *public* virtual circuits support
    public peering. For more information, see `FastConnect Overview`__.

    Each virtual circuit is made up of information shared between a customer, Oracle,
    and a provider (if the customer is using FastConnect via a provider). Who fills in
    a given property of a virtual circuit depends on whether the BGP session related to
    that virtual circuit goes from the customer's edge router to Oracle, or from the provider's
    edge router to Oracle. Also, in the case where the customer is using a provider, values
    for some of the properties may not be present immediately, but may get filled in as the
    provider and Oracle each do their part to provision the virtual circuit.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator. If you're an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/fastconnect.htm
    __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the bgp_management property of a VirtualCircuit.
    #: This constant has a value of "CUSTOMER_MANAGED"
    BGP_MANAGEMENT_CUSTOMER_MANAGED = "CUSTOMER_MANAGED"

    #: A constant which can be used with the bgp_management property of a VirtualCircuit.
    #: This constant has a value of "PROVIDER_MANAGED"
    BGP_MANAGEMENT_PROVIDER_MANAGED = "PROVIDER_MANAGED"

    #: A constant which can be used with the bgp_management property of a VirtualCircuit.
    #: This constant has a value of "ORACLE_MANAGED"
    BGP_MANAGEMENT_ORACLE_MANAGED = "ORACLE_MANAGED"

    #: A constant which can be used with the bgp_session_state property of a VirtualCircuit.
    #: This constant has a value of "UP"
    BGP_SESSION_STATE_UP = "UP"

    #: A constant which can be used with the bgp_session_state property of a VirtualCircuit.
    #: This constant has a value of "DOWN"
    BGP_SESSION_STATE_DOWN = "DOWN"

    #: A constant which can be used with the lifecycle_state property of a VirtualCircuit.
    #: This constant has a value of "PENDING_PROVIDER"
    LIFECYCLE_STATE_PENDING_PROVIDER = "PENDING_PROVIDER"

    #: A constant which can be used with the lifecycle_state property of a VirtualCircuit.
    #: This constant has a value of "VERIFYING"
    LIFECYCLE_STATE_VERIFYING = "VERIFYING"

    #: A constant which can be used with the lifecycle_state property of a VirtualCircuit.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a VirtualCircuit.
    #: This constant has a value of "PROVISIONED"
    LIFECYCLE_STATE_PROVISIONED = "PROVISIONED"

    #: A constant which can be used with the lifecycle_state property of a VirtualCircuit.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a VirtualCircuit.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a VirtualCircuit.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a VirtualCircuit.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the provider_state property of a VirtualCircuit.
    #: This constant has a value of "ACTIVE"
    PROVIDER_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the provider_state property of a VirtualCircuit.
    #: This constant has a value of "INACTIVE"
    PROVIDER_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the service_type property of a VirtualCircuit.
    #: This constant has a value of "COLOCATED"
    SERVICE_TYPE_COLOCATED = "COLOCATED"

    #: A constant which can be used with the service_type property of a VirtualCircuit.
    #: This constant has a value of "LAYER2"
    SERVICE_TYPE_LAYER2 = "LAYER2"

    #: A constant which can be used with the service_type property of a VirtualCircuit.
    #: This constant has a value of "LAYER3"
    SERVICE_TYPE_LAYER3 = "LAYER3"

    #: A constant which can be used with the type property of a VirtualCircuit.
    #: This constant has a value of "PUBLIC"
    TYPE_PUBLIC = "PUBLIC"

    #: A constant which can be used with the type property of a VirtualCircuit.
    #: This constant has a value of "PRIVATE"
    TYPE_PRIVATE = "PRIVATE"

    def __init__(self, **kwargs):
        """
        Initializes a new VirtualCircuit object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param bandwidth_shape_name:
            The value to assign to the bandwidth_shape_name property of this VirtualCircuit.
        :type bandwidth_shape_name: str

        :param bgp_management:
            The value to assign to the bgp_management property of this VirtualCircuit.
            Allowed values for this property are: "CUSTOMER_MANAGED", "PROVIDER_MANAGED", "ORACLE_MANAGED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type bgp_management: str

        :param bgp_session_state:
            The value to assign to the bgp_session_state property of this VirtualCircuit.
            Allowed values for this property are: "UP", "DOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type bgp_session_state: str

        :param compartment_id:
            The value to assign to the compartment_id property of this VirtualCircuit.
        :type compartment_id: str

        :param cross_connect_mappings:
            The value to assign to the cross_connect_mappings property of this VirtualCircuit.
        :type cross_connect_mappings: list[CrossConnectMapping]

        :param customer_bgp_asn:
            The value to assign to the customer_bgp_asn property of this VirtualCircuit.
        :type customer_bgp_asn: int

        :param display_name:
            The value to assign to the display_name property of this VirtualCircuit.
        :type display_name: str

        :param gateway_id:
            The value to assign to the gateway_id property of this VirtualCircuit.
        :type gateway_id: str

        :param id:
            The value to assign to the id property of this VirtualCircuit.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this VirtualCircuit.
            Allowed values for this property are: "PENDING_PROVIDER", "VERIFYING", "PROVISIONING", "PROVISIONED", "FAILED", "INACTIVE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param oracle_bgp_asn:
            The value to assign to the oracle_bgp_asn property of this VirtualCircuit.
        :type oracle_bgp_asn: int

        :param provider_name:
            The value to assign to the provider_name property of this VirtualCircuit.
        :type provider_name: str

        :param provider_service_id:
            The value to assign to the provider_service_id property of this VirtualCircuit.
        :type provider_service_id: str

        :param provider_service_name:
            The value to assign to the provider_service_name property of this VirtualCircuit.
        :type provider_service_name: str

        :param provider_state:
            The value to assign to the provider_state property of this VirtualCircuit.
            Allowed values for this property are: "ACTIVE", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type provider_state: str

        :param public_prefixes:
            The value to assign to the public_prefixes property of this VirtualCircuit.
        :type public_prefixes: list[str]

        :param reference_comment:
            The value to assign to the reference_comment property of this VirtualCircuit.
        :type reference_comment: str

        :param region:
            The value to assign to the region property of this VirtualCircuit.
        :type region: str

        :param service_type:
            The value to assign to the service_type property of this VirtualCircuit.
            Allowed values for this property are: "COLOCATED", "LAYER2", "LAYER3", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type service_type: str

        :param time_created:
            The value to assign to the time_created property of this VirtualCircuit.
        :type time_created: datetime

        :param type:
            The value to assign to the type property of this VirtualCircuit.
            Allowed values for this property are: "PUBLIC", "PRIVATE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        """
        self.swagger_types = {
            'bandwidth_shape_name': 'str',
            'bgp_management': 'str',
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
            'provider_service_id': 'str',
            'provider_service_name': 'str',
            'provider_state': 'str',
            'public_prefixes': 'list[str]',
            'reference_comment': 'str',
            'region': 'str',
            'service_type': 'str',
            'time_created': 'datetime',
            'type': 'str'
        }

        self.attribute_map = {
            'bandwidth_shape_name': 'bandwidthShapeName',
            'bgp_management': 'bgpManagement',
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
            'provider_service_id': 'providerServiceId',
            'provider_service_name': 'providerServiceName',
            'provider_state': 'providerState',
            'public_prefixes': 'publicPrefixes',
            'reference_comment': 'referenceComment',
            'region': 'region',
            'service_type': 'serviceType',
            'time_created': 'timeCreated',
            'type': 'type'
        }

        self._bandwidth_shape_name = None
        self._bgp_management = None
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
        self._provider_service_id = None
        self._provider_service_name = None
        self._provider_state = None
        self._public_prefixes = None
        self._reference_comment = None
        self._region = None
        self._service_type = None
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
    def bgp_management(self):
        """
        Gets the bgp_management of this VirtualCircuit.
        BGP management option.

        Allowed values for this property are: "CUSTOMER_MANAGED", "PROVIDER_MANAGED", "ORACLE_MANAGED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The bgp_management of this VirtualCircuit.
        :rtype: str
        """
        return self._bgp_management

    @bgp_management.setter
    def bgp_management(self, bgp_management):
        """
        Sets the bgp_management of this VirtualCircuit.
        BGP management option.


        :param bgp_management: The bgp_management of this VirtualCircuit.
        :type: str
        """
        allowed_values = ["CUSTOMER_MANAGED", "PROVIDER_MANAGED", "ORACLE_MANAGED"]
        if not value_allowed_none_or_none_sentinel(bgp_management, allowed_values):
            bgp_management = 'UNKNOWN_ENUM_VALUE'
        self._bgp_management = bgp_management

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
        if not value_allowed_none_or_none_sentinel(bgp_session_state, allowed_values):
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
        Avoid entering confidential information.


        :return: The display_name of this VirtualCircuit.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this VirtualCircuit.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this VirtualCircuit.
        :type: str
        """
        self._display_name = display_name

    @property
    def gateway_id(self):
        """
        Gets the gateway_id of this VirtualCircuit.
        The OCID of the customer's :class:`Drg`
        that this virtual circuit uses. Applicable only to private virtual circuits.


        :return: The gateway_id of this VirtualCircuit.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        """
        Sets the gateway_id of this VirtualCircuit.
        The OCID of the customer's :class:`Drg`
        that this virtual circuit uses. Applicable only to private virtual circuits.


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
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
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
        Deprecated. Instead use `providerServiceId`.


        :return: The provider_name of this VirtualCircuit.
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """
        Sets the provider_name of this VirtualCircuit.
        Deprecated. Instead use `providerServiceId`.


        :param provider_name: The provider_name of this VirtualCircuit.
        :type: str
        """
        self._provider_name = provider_name

    @property
    def provider_service_id(self):
        """
        Gets the provider_service_id of this VirtualCircuit.
        The OCID of the service offered by the provider (if the customer is connecting via a provider).


        :return: The provider_service_id of this VirtualCircuit.
        :rtype: str
        """
        return self._provider_service_id

    @provider_service_id.setter
    def provider_service_id(self, provider_service_id):
        """
        Sets the provider_service_id of this VirtualCircuit.
        The OCID of the service offered by the provider (if the customer is connecting via a provider).


        :param provider_service_id: The provider_service_id of this VirtualCircuit.
        :type: str
        """
        self._provider_service_id = provider_service_id

    @property
    def provider_service_name(self):
        """
        Gets the provider_service_name of this VirtualCircuit.
        Deprecated. Instead use `providerServiceId`.


        :return: The provider_service_name of this VirtualCircuit.
        :rtype: str
        """
        return self._provider_service_name

    @provider_service_name.setter
    def provider_service_name(self, provider_service_name):
        """
        Sets the provider_service_name of this VirtualCircuit.
        Deprecated. Instead use `providerServiceId`.


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
        if not value_allowed_none_or_none_sentinel(provider_state, allowed_values):
            provider_state = 'UNKNOWN_ENUM_VALUE'
        self._provider_state = provider_state

    @property
    def public_prefixes(self):
        """
        Gets the public_prefixes of this VirtualCircuit.
        For a public virtual circuit. The public IP prefixes (CIDRs) the customer wants to
        advertise across the connection. Each prefix must be /24 or less specific.


        :return: The public_prefixes of this VirtualCircuit.
        :rtype: list[str]
        """
        return self._public_prefixes

    @public_prefixes.setter
    def public_prefixes(self, public_prefixes):
        """
        Sets the public_prefixes of this VirtualCircuit.
        For a public virtual circuit. The public IP prefixes (CIDRs) the customer wants to
        advertise across the connection. Each prefix must be /24 or less specific.


        :param public_prefixes: The public_prefixes of this VirtualCircuit.
        :type: list[str]
        """
        self._public_prefixes = public_prefixes

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
        The Oracle Cloud Infrastructure region where this virtual
        circuit is located.


        :return: The region of this VirtualCircuit.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this VirtualCircuit.
        The Oracle Cloud Infrastructure region where this virtual
        circuit is located.


        :param region: The region of this VirtualCircuit.
        :type: str
        """
        self._region = region

    @property
    def service_type(self):
        """
        Gets the service_type of this VirtualCircuit.
        Provider service type.

        Allowed values for this property are: "COLOCATED", "LAYER2", "LAYER3", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The service_type of this VirtualCircuit.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """
        Sets the service_type of this VirtualCircuit.
        Provider service type.


        :param service_type: The service_type of this VirtualCircuit.
        :type: str
        """
        allowed_values = ["COLOCATED", "LAYER2", "LAYER3"]
        if not value_allowed_none_or_none_sentinel(service_type, allowed_values):
            service_type = 'UNKNOWN_ENUM_VALUE'
        self._service_type = service_type

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
        Whether the virtual circuit supports private or public peering. For more information,
        see `FastConnect Overview`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/fastconnect.htm

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
        Whether the virtual circuit supports private or public peering. For more information,
        see `FastConnect Overview`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/fastconnect.htm


        :param type: The type of this VirtualCircuit.
        :type: str
        """
        allowed_values = ["PUBLIC", "PRIVATE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
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
