# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class CreateVirtualCircuitDetails(object):

    def __init__(self):

        self.swagger_types = {
            'bandwidth_shape_name': 'str',
            'compartment_id': 'str',
            'cross_connect_mappings': 'list[CrossConnectMapping]',
            'customer_bgp_asn': 'int',
            'display_name': 'str',
            'gateway_id': 'str',
            'provider_name': 'str',
            'provider_service_name': 'str',
            'region': 'str',
            'type': 'str'
        }

        self.attribute_map = {
            'bandwidth_shape_name': 'bandwidthShapeName',
            'compartment_id': 'compartmentId',
            'cross_connect_mappings': 'crossConnectMappings',
            'customer_bgp_asn': 'customerBgpAsn',
            'display_name': 'displayName',
            'gateway_id': 'gatewayId',
            'provider_name': 'providerName',
            'provider_service_name': 'providerServiceName',
            'region': 'region',
            'type': 'type'
        }

        self._bandwidth_shape_name = None
        self._compartment_id = None
        self._cross_connect_mappings = None
        self._customer_bgp_asn = None
        self._display_name = None
        self._gateway_id = None
        self._provider_name = None
        self._provider_service_name = None
        self._region = None
        self._type = None

    @property
    def bandwidth_shape_name(self):
        """
        Gets the bandwidth_shape_name of this CreateVirtualCircuitDetails.
        The provisioned data rate of the connection.  To get a list of the
        available bandwidth levels (i.e., shapes), see
        :func:`list_virtual_circuit_bandwidth_shapes`.

        Example: `10 Gbps`


        :return: The bandwidth_shape_name of this CreateVirtualCircuitDetails.
        :rtype: str
        """
        return self._bandwidth_shape_name

    @bandwidth_shape_name.setter
    def bandwidth_shape_name(self, bandwidth_shape_name):
        """
        Sets the bandwidth_shape_name of this CreateVirtualCircuitDetails.
        The provisioned data rate of the connection.  To get a list of the
        available bandwidth levels (i.e., shapes), see
        :func:`list_virtual_circuit_bandwidth_shapes`.

        Example: `10 Gbps`


        :param bandwidth_shape_name: The bandwidth_shape_name of this CreateVirtualCircuitDetails.
        :type: str
        """
        self._bandwidth_shape_name = bandwidth_shape_name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CreateVirtualCircuitDetails.
        The OCID of the compartment to contain the virtual circuit.


        :return: The compartment_id of this CreateVirtualCircuitDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateVirtualCircuitDetails.
        The OCID of the compartment to contain the virtual circuit.


        :param compartment_id: The compartment_id of this CreateVirtualCircuitDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def cross_connect_mappings(self):
        """
        Gets the cross_connect_mappings of this CreateVirtualCircuitDetails.
        Create a `CrossConnectMapping` for each cross-connect or cross-connect
        group this virtual circuit will run on.


        :return: The cross_connect_mappings of this CreateVirtualCircuitDetails.
        :rtype: list[CrossConnectMapping]
        """
        return self._cross_connect_mappings

    @cross_connect_mappings.setter
    def cross_connect_mappings(self, cross_connect_mappings):
        """
        Sets the cross_connect_mappings of this CreateVirtualCircuitDetails.
        Create a `CrossConnectMapping` for each cross-connect or cross-connect
        group this virtual circuit will run on.


        :param cross_connect_mappings: The cross_connect_mappings of this CreateVirtualCircuitDetails.
        :type: list[CrossConnectMapping]
        """
        self._cross_connect_mappings = cross_connect_mappings

    @property
    def customer_bgp_asn(self):
        """
        Gets the customer_bgp_asn of this CreateVirtualCircuitDetails.
        Your BGP ASN (either public or private). Provide this value only if
        there's a BGP session that goes from your edge router to Oracle.
        Otherwise, leave this empty or null.


        :return: The customer_bgp_asn of this CreateVirtualCircuitDetails.
        :rtype: int
        """
        return self._customer_bgp_asn

    @customer_bgp_asn.setter
    def customer_bgp_asn(self, customer_bgp_asn):
        """
        Sets the customer_bgp_asn of this CreateVirtualCircuitDetails.
        Your BGP ASN (either public or private). Provide this value only if
        there's a BGP session that goes from your edge router to Oracle.
        Otherwise, leave this empty or null.


        :param customer_bgp_asn: The customer_bgp_asn of this CreateVirtualCircuitDetails.
        :type: int
        """
        self._customer_bgp_asn = customer_bgp_asn

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateVirtualCircuitDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :return: The display_name of this CreateVirtualCircuitDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateVirtualCircuitDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :param display_name: The display_name of this CreateVirtualCircuitDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def gateway_id(self):
        """
        Gets the gateway_id of this CreateVirtualCircuitDetails.
        The OCID of the :class:`Drg`
        that this virtual circuit uses.


        :return: The gateway_id of this CreateVirtualCircuitDetails.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        """
        Sets the gateway_id of this CreateVirtualCircuitDetails.
        The OCID of the :class:`Drg`
        that this virtual circuit uses.


        :param gateway_id: The gateway_id of this CreateVirtualCircuitDetails.
        :type: str
        """
        self._gateway_id = gateway_id

    @property
    def provider_name(self):
        """
        Gets the provider_name of this CreateVirtualCircuitDetails.
        The name of the provider (if you're connecting via a provider).
        To get a list of the provider names, see
        :func:`list_fast_connect_provider_services`.


        :return: The provider_name of this CreateVirtualCircuitDetails.
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """
        Sets the provider_name of this CreateVirtualCircuitDetails.
        The name of the provider (if you're connecting via a provider).
        To get a list of the provider names, see
        :func:`list_fast_connect_provider_services`.


        :param provider_name: The provider_name of this CreateVirtualCircuitDetails.
        :type: str
        """
        self._provider_name = provider_name

    @property
    def provider_service_name(self):
        """
        Gets the provider_service_name of this CreateVirtualCircuitDetails.
        The name of the service offered by the provider (if you're connecting
        via a provider). To get a list of the available service offerings, see
        :func:`list_fast_connect_provider_services`.


        :return: The provider_service_name of this CreateVirtualCircuitDetails.
        :rtype: str
        """
        return self._provider_service_name

    @provider_service_name.setter
    def provider_service_name(self, provider_service_name):
        """
        Sets the provider_service_name of this CreateVirtualCircuitDetails.
        The name of the service offered by the provider (if you're connecting
        via a provider). To get a list of the available service offerings, see
        :func:`list_fast_connect_provider_services`.


        :param provider_service_name: The provider_service_name of this CreateVirtualCircuitDetails.
        :type: str
        """
        self._provider_service_name = provider_service_name

    @property
    def region(self):
        """
        Gets the region of this CreateVirtualCircuitDetails.
        The Oracle Bare Metal Cloud Services region where this virtual
        circuit is located.

        Example: `phx`


        :return: The region of this CreateVirtualCircuitDetails.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this CreateVirtualCircuitDetails.
        The Oracle Bare Metal Cloud Services region where this virtual
        circuit is located.

        Example: `phx`


        :param region: The region of this CreateVirtualCircuitDetails.
        :type: str
        """
        self._region = region

    @property
    def type(self):
        """
        Gets the type of this CreateVirtualCircuitDetails.
        The type of IP addresses used in this virtual circuit. PRIVATE
        means `RFC 1918`__ addresses
        (10.0.0.0/8, 172.16/12, and 192.168/16). Only PRIVATE is supported.

        __ https://tools.ietf.org/html/rfc1918

        Allowed values for this property are: "PUBLIC", "PRIVATE"


        :return: The type of this CreateVirtualCircuitDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CreateVirtualCircuitDetails.
        The type of IP addresses used in this virtual circuit. PRIVATE
        means `RFC 1918`__ addresses
        (10.0.0.0/8, 172.16/12, and 192.168/16). Only PRIVATE is supported.

        __ https://tools.ietf.org/html/rfc1918


        :param type: The type of this CreateVirtualCircuitDetails.
        :type: str
        """
        allowed_values = ["PUBLIC", "PRIVATE"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type`, must be one of {0}"
                .format(allowed_values)
            )
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
