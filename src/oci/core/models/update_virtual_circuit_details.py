# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateVirtualCircuitDetails(object):

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateVirtualCircuitDetails object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param bandwidth_shape_name:
            The value to assign to the bandwidth_shape_name property of this UpdateVirtualCircuitDetails.
        :type bandwidth_shape_name: str

        :param cross_connect_mappings:
            The value to assign to the cross_connect_mappings property of this UpdateVirtualCircuitDetails.
        :type cross_connect_mappings: list[CrossConnectMapping]

        :param customer_bgp_asn:
            The value to assign to the customer_bgp_asn property of this UpdateVirtualCircuitDetails.
        :type customer_bgp_asn: int

        :param display_name:
            The value to assign to the display_name property of this UpdateVirtualCircuitDetails.
        :type display_name: str

        :param gateway_id:
            The value to assign to the gateway_id property of this UpdateVirtualCircuitDetails.
        :type gateway_id: str

        :param provider_state:
            The value to assign to the provider_state property of this UpdateVirtualCircuitDetails.
            Allowed values for this property are: "ACTIVE", "INACTIVE"
        :type provider_state: str

        :param reference_comment:
            The value to assign to the reference_comment property of this UpdateVirtualCircuitDetails.
        :type reference_comment: str

        """
        self.swagger_types = {
            'bandwidth_shape_name': 'str',
            'cross_connect_mappings': 'list[CrossConnectMapping]',
            'customer_bgp_asn': 'int',
            'display_name': 'str',
            'gateway_id': 'str',
            'provider_state': 'str',
            'reference_comment': 'str'
        }

        self.attribute_map = {
            'bandwidth_shape_name': 'bandwidthShapeName',
            'cross_connect_mappings': 'crossConnectMappings',
            'customer_bgp_asn': 'customerBgpAsn',
            'display_name': 'displayName',
            'gateway_id': 'gatewayId',
            'provider_state': 'providerState',
            'reference_comment': 'referenceComment'
        }

        self._bandwidth_shape_name = None
        self._cross_connect_mappings = None
        self._customer_bgp_asn = None
        self._display_name = None
        self._gateway_id = None
        self._provider_state = None
        self._reference_comment = None

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
        :rtype: list[CrossConnectMapping]
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
        :type: list[CrossConnectMapping]
        """
        self._cross_connect_mappings = cross_connect_mappings

    @property
    def customer_bgp_asn(self):
        """
        Gets the customer_bgp_asn of this UpdateVirtualCircuitDetails.
        The BGP ASN of the network at the other end of the BGP
        session from Oracle.

        If the BGP session is from the customer's edge router to Oracle, the
        required value is the customer's ASN, and it can be updated only
        by the customer.

        If the BGP session is from the provider's edge router to Oracle, the
        required value is the provider's ASN, and it can be updated only
        by the provider.


        :return: The customer_bgp_asn of this UpdateVirtualCircuitDetails.
        :rtype: int
        """
        return self._customer_bgp_asn

    @customer_bgp_asn.setter
    def customer_bgp_asn(self, customer_bgp_asn):
        """
        Sets the customer_bgp_asn of this UpdateVirtualCircuitDetails.
        The BGP ASN of the network at the other end of the BGP
        session from Oracle.

        If the BGP session is from the customer's edge router to Oracle, the
        required value is the customer's ASN, and it can be updated only
        by the customer.

        If the BGP session is from the provider's edge router to Oracle, the
        required value is the provider's ASN, and it can be updated only
        by the provider.


        :param customer_bgp_asn: The customer_bgp_asn of this UpdateVirtualCircuitDetails.
        :type: int
        """
        self._customer_bgp_asn = customer_bgp_asn

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateVirtualCircuitDetails.
        A user-friendly name. Does not have to be unique.
        Avoid entering confidential information.

        To be updated only by the customer who owns the virtual circuit.


        :return: The display_name of this UpdateVirtualCircuitDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateVirtualCircuitDetails.
        A user-friendly name. Does not have to be unique.
        Avoid entering confidential information.

        To be updated only by the customer who owns the virtual circuit.


        :param display_name: The display_name of this UpdateVirtualCircuitDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def gateway_id(self):
        """
        Gets the gateway_id of this UpdateVirtualCircuitDetails.
        The OCID of the :class:`Drg`
        that this private virtual circuit uses.

        To be updated only by the customer who owns the virtual circuit.


        :return: The gateway_id of this UpdateVirtualCircuitDetails.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        """
        Sets the gateway_id of this UpdateVirtualCircuitDetails.
        The OCID of the :class:`Drg`
        that this private virtual circuit uses.

        To be updated only by the customer who owns the virtual circuit.


        :param gateway_id: The gateway_id of this UpdateVirtualCircuitDetails.
        :type: str
        """
        self._gateway_id = gateway_id

    @property
    def provider_state(self):
        """
        Gets the provider_state of this UpdateVirtualCircuitDetails.
        The provider's state in relation to this virtual circuit. Relevant only
        if the customer is using FastConnect via a provider.  ACTIVE
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
        if the customer is using FastConnect via a provider.  ACTIVE
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

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
