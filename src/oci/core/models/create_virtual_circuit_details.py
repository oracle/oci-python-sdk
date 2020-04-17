# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateVirtualCircuitDetails(object):
    """
    CreateVirtualCircuitDetails model.
    """

    #: A constant which can be used with the type property of a CreateVirtualCircuitDetails.
    #: This constant has a value of "PUBLIC"
    TYPE_PUBLIC = "PUBLIC"

    #: A constant which can be used with the type property of a CreateVirtualCircuitDetails.
    #: This constant has a value of "PRIVATE"
    TYPE_PRIVATE = "PRIVATE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateVirtualCircuitDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param bandwidth_shape_name:
            The value to assign to the bandwidth_shape_name property of this CreateVirtualCircuitDetails.
        :type bandwidth_shape_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateVirtualCircuitDetails.
        :type compartment_id: str

        :param cross_connect_mappings:
            The value to assign to the cross_connect_mappings property of this CreateVirtualCircuitDetails.
        :type cross_connect_mappings: list[CrossConnectMapping]

        :param customer_bgp_asn:
            The value to assign to the customer_bgp_asn property of this CreateVirtualCircuitDetails.
        :type customer_bgp_asn: int

        :param customer_asn:
            The value to assign to the customer_asn property of this CreateVirtualCircuitDetails.
        :type customer_asn: int

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateVirtualCircuitDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CreateVirtualCircuitDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateVirtualCircuitDetails.
        :type freeform_tags: dict(str, str)

        :param gateway_id:
            The value to assign to the gateway_id property of this CreateVirtualCircuitDetails.
        :type gateway_id: str

        :param provider_name:
            The value to assign to the provider_name property of this CreateVirtualCircuitDetails.
        :type provider_name: str

        :param provider_service_id:
            The value to assign to the provider_service_id property of this CreateVirtualCircuitDetails.
        :type provider_service_id: str

        :param provider_service_key_name:
            The value to assign to the provider_service_key_name property of this CreateVirtualCircuitDetails.
        :type provider_service_key_name: str

        :param provider_service_name:
            The value to assign to the provider_service_name property of this CreateVirtualCircuitDetails.
        :type provider_service_name: str

        :param public_prefixes:
            The value to assign to the public_prefixes property of this CreateVirtualCircuitDetails.
        :type public_prefixes: list[CreateVirtualCircuitPublicPrefixDetails]

        :param region:
            The value to assign to the region property of this CreateVirtualCircuitDetails.
        :type region: str

        :param type:
            The value to assign to the type property of this CreateVirtualCircuitDetails.
            Allowed values for this property are: "PUBLIC", "PRIVATE"
        :type type: str

        """
        self.swagger_types = {
            'bandwidth_shape_name': 'str',
            'compartment_id': 'str',
            'cross_connect_mappings': 'list[CrossConnectMapping]',
            'customer_bgp_asn': 'int',
            'customer_asn': 'int',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'gateway_id': 'str',
            'provider_name': 'str',
            'provider_service_id': 'str',
            'provider_service_key_name': 'str',
            'provider_service_name': 'str',
            'public_prefixes': 'list[CreateVirtualCircuitPublicPrefixDetails]',
            'region': 'str',
            'type': 'str'
        }

        self.attribute_map = {
            'bandwidth_shape_name': 'bandwidthShapeName',
            'compartment_id': 'compartmentId',
            'cross_connect_mappings': 'crossConnectMappings',
            'customer_bgp_asn': 'customerBgpAsn',
            'customer_asn': 'customerAsn',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'gateway_id': 'gatewayId',
            'provider_name': 'providerName',
            'provider_service_id': 'providerServiceId',
            'provider_service_key_name': 'providerServiceKeyName',
            'provider_service_name': 'providerServiceName',
            'public_prefixes': 'publicPrefixes',
            'region': 'region',
            'type': 'type'
        }

        self._bandwidth_shape_name = None
        self._compartment_id = None
        self._cross_connect_mappings = None
        self._customer_bgp_asn = None
        self._customer_asn = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._gateway_id = None
        self._provider_name = None
        self._provider_service_id = None
        self._provider_service_key_name = None
        self._provider_service_name = None
        self._public_prefixes = None
        self._region = None
        self._type = None

    @property
    def bandwidth_shape_name(self):
        """
        Gets the bandwidth_shape_name of this CreateVirtualCircuitDetails.
        The provisioned data rate of the connection.  To get a list of the
        available bandwidth levels (that is, shapes), see
        :func:`list_fast_connect_provider_virtual_circuit_bandwidth_shapes`.

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
        available bandwidth levels (that is, shapes), see
        :func:`list_fast_connect_provider_virtual_circuit_bandwidth_shapes`.

        Example: `10 Gbps`


        :param bandwidth_shape_name: The bandwidth_shape_name of this CreateVirtualCircuitDetails.
        :type: str
        """
        self._bandwidth_shape_name = bandwidth_shape_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateVirtualCircuitDetails.
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
        Deprecated. Instead use `customerAsn`.
        If you specify values for both, the request will be rejected.


        :return: The customer_bgp_asn of this CreateVirtualCircuitDetails.
        :rtype: int
        """
        return self._customer_bgp_asn

    @customer_bgp_asn.setter
    def customer_bgp_asn(self, customer_bgp_asn):
        """
        Sets the customer_bgp_asn of this CreateVirtualCircuitDetails.
        Deprecated. Instead use `customerAsn`.
        If you specify values for both, the request will be rejected.


        :param customer_bgp_asn: The customer_bgp_asn of this CreateVirtualCircuitDetails.
        :type: int
        """
        self._customer_bgp_asn = customer_bgp_asn

    @property
    def customer_asn(self):
        """
        Gets the customer_asn of this CreateVirtualCircuitDetails.
        Your BGP ASN (either public or private). Provide this value only if
        there's a BGP session that goes from your edge router to Oracle.
        Otherwise, leave this empty or null.
        Can be a 2-byte or 4-byte ASN. Uses \"asplain\" format.

        Example: `12345` (2-byte) or `1587232876` (4-byte)


        :return: The customer_asn of this CreateVirtualCircuitDetails.
        :rtype: int
        """
        return self._customer_asn

    @customer_asn.setter
    def customer_asn(self, customer_asn):
        """
        Sets the customer_asn of this CreateVirtualCircuitDetails.
        Your BGP ASN (either public or private). Provide this value only if
        there's a BGP session that goes from your edge router to Oracle.
        Otherwise, leave this empty or null.
        Can be a 2-byte or 4-byte ASN. Uses \"asplain\" format.

        Example: `12345` (2-byte) or `1587232876` (4-byte)


        :param customer_asn: The customer_asn of this CreateVirtualCircuitDetails.
        :type: int
        """
        self._customer_asn = customer_asn

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateVirtualCircuitDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateVirtualCircuitDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateVirtualCircuitDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateVirtualCircuitDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateVirtualCircuitDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this CreateVirtualCircuitDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateVirtualCircuitDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this CreateVirtualCircuitDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateVirtualCircuitDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateVirtualCircuitDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateVirtualCircuitDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateVirtualCircuitDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def gateway_id(self):
        """
        Gets the gateway_id of this CreateVirtualCircuitDetails.
        For private virtual circuits only. The OCID of the :class:`Drg`
        that this virtual circuit uses.


        :return: The gateway_id of this CreateVirtualCircuitDetails.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        """
        Sets the gateway_id of this CreateVirtualCircuitDetails.
        For private virtual circuits only. The OCID of the :class:`Drg`
        that this virtual circuit uses.


        :param gateway_id: The gateway_id of this CreateVirtualCircuitDetails.
        :type: str
        """
        self._gateway_id = gateway_id

    @property
    def provider_name(self):
        """
        Gets the provider_name of this CreateVirtualCircuitDetails.
        Deprecated. Instead use `providerServiceId`.
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
        Deprecated. Instead use `providerServiceId`.
        To get a list of the provider names, see
        :func:`list_fast_connect_provider_services`.


        :param provider_name: The provider_name of this CreateVirtualCircuitDetails.
        :type: str
        """
        self._provider_name = provider_name

    @property
    def provider_service_id(self):
        """
        Gets the provider_service_id of this CreateVirtualCircuitDetails.
        The OCID of the service offered by the provider (if you're connecting
        via a provider). To get a list of the available service offerings, see
        :func:`list_fast_connect_provider_services`.


        :return: The provider_service_id of this CreateVirtualCircuitDetails.
        :rtype: str
        """
        return self._provider_service_id

    @provider_service_id.setter
    def provider_service_id(self, provider_service_id):
        """
        Sets the provider_service_id of this CreateVirtualCircuitDetails.
        The OCID of the service offered by the provider (if you're connecting
        via a provider). To get a list of the available service offerings, see
        :func:`list_fast_connect_provider_services`.


        :param provider_service_id: The provider_service_id of this CreateVirtualCircuitDetails.
        :type: str
        """
        self._provider_service_id = provider_service_id

    @property
    def provider_service_key_name(self):
        """
        Gets the provider_service_key_name of this CreateVirtualCircuitDetails.
        The service key name offered by the provider (if the customer is connecting via a provider).


        :return: The provider_service_key_name of this CreateVirtualCircuitDetails.
        :rtype: str
        """
        return self._provider_service_key_name

    @provider_service_key_name.setter
    def provider_service_key_name(self, provider_service_key_name):
        """
        Sets the provider_service_key_name of this CreateVirtualCircuitDetails.
        The service key name offered by the provider (if the customer is connecting via a provider).


        :param provider_service_key_name: The provider_service_key_name of this CreateVirtualCircuitDetails.
        :type: str
        """
        self._provider_service_key_name = provider_service_key_name

    @property
    def provider_service_name(self):
        """
        Gets the provider_service_name of this CreateVirtualCircuitDetails.
        Deprecated. Instead use `providerServiceId`.
        To get a list of the provider names, see
        :func:`list_fast_connect_provider_services`.


        :return: The provider_service_name of this CreateVirtualCircuitDetails.
        :rtype: str
        """
        return self._provider_service_name

    @provider_service_name.setter
    def provider_service_name(self, provider_service_name):
        """
        Sets the provider_service_name of this CreateVirtualCircuitDetails.
        Deprecated. Instead use `providerServiceId`.
        To get a list of the provider names, see
        :func:`list_fast_connect_provider_services`.


        :param provider_service_name: The provider_service_name of this CreateVirtualCircuitDetails.
        :type: str
        """
        self._provider_service_name = provider_service_name

    @property
    def public_prefixes(self):
        """
        Gets the public_prefixes of this CreateVirtualCircuitDetails.
        For a public virtual circuit. The public IP prefixes (CIDRs) the customer wants to
        advertise across the connection.


        :return: The public_prefixes of this CreateVirtualCircuitDetails.
        :rtype: list[CreateVirtualCircuitPublicPrefixDetails]
        """
        return self._public_prefixes

    @public_prefixes.setter
    def public_prefixes(self, public_prefixes):
        """
        Sets the public_prefixes of this CreateVirtualCircuitDetails.
        For a public virtual circuit. The public IP prefixes (CIDRs) the customer wants to
        advertise across the connection.


        :param public_prefixes: The public_prefixes of this CreateVirtualCircuitDetails.
        :type: list[CreateVirtualCircuitPublicPrefixDetails]
        """
        self._public_prefixes = public_prefixes

    @property
    def region(self):
        """
        Gets the region of this CreateVirtualCircuitDetails.
        The Oracle Cloud Infrastructure region where this virtual
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
        The Oracle Cloud Infrastructure region where this virtual
        circuit is located.
        Example: `phx`


        :param region: The region of this CreateVirtualCircuitDetails.
        :type: str
        """
        self._region = region

    @property
    def type(self):
        """
        **[Required]** Gets the type of this CreateVirtualCircuitDetails.
        The type of IP addresses used in this virtual circuit. PRIVATE
        means `RFC 1918`__ addresses
        (10.0.0.0/8, 172.16/12, and 192.168/16).

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
        (10.0.0.0/8, 172.16/12, and 192.168/16).

        __ https://tools.ietf.org/html/rfc1918


        :param type: The type of this CreateVirtualCircuitDetails.
        :type: str
        """
        allowed_values = ["PUBLIC", "PRIVATE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                "Invalid value for `type`, must be None or one of {0}"
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
