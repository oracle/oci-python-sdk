# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FastConnectProviderService(object):
    """
    A service offering from a supported provider. For more information,
    see `FastConnect Overview`__.

    __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/fastconnect.htm
    """

    #: A constant which can be used with the private_peering_bgp_management property of a FastConnectProviderService.
    #: This constant has a value of "CUSTOMER_MANAGED"
    PRIVATE_PEERING_BGP_MANAGEMENT_CUSTOMER_MANAGED = "CUSTOMER_MANAGED"

    #: A constant which can be used with the private_peering_bgp_management property of a FastConnectProviderService.
    #: This constant has a value of "PROVIDER_MANAGED"
    PRIVATE_PEERING_BGP_MANAGEMENT_PROVIDER_MANAGED = "PROVIDER_MANAGED"

    #: A constant which can be used with the private_peering_bgp_management property of a FastConnectProviderService.
    #: This constant has a value of "ORACLE_MANAGED"
    PRIVATE_PEERING_BGP_MANAGEMENT_ORACLE_MANAGED = "ORACLE_MANAGED"

    #: A constant which can be used with the public_peering_bgp_management property of a FastConnectProviderService.
    #: This constant has a value of "CUSTOMER_MANAGED"
    PUBLIC_PEERING_BGP_MANAGEMENT_CUSTOMER_MANAGED = "CUSTOMER_MANAGED"

    #: A constant which can be used with the public_peering_bgp_management property of a FastConnectProviderService.
    #: This constant has a value of "PROVIDER_MANAGED"
    PUBLIC_PEERING_BGP_MANAGEMENT_PROVIDER_MANAGED = "PROVIDER_MANAGED"

    #: A constant which can be used with the public_peering_bgp_management property of a FastConnectProviderService.
    #: This constant has a value of "ORACLE_MANAGED"
    PUBLIC_PEERING_BGP_MANAGEMENT_ORACLE_MANAGED = "ORACLE_MANAGED"

    #: A constant which can be used with the supported_virtual_circuit_types property of a FastConnectProviderService.
    #: This constant has a value of "PUBLIC"
    SUPPORTED_VIRTUAL_CIRCUIT_TYPES_PUBLIC = "PUBLIC"

    #: A constant which can be used with the supported_virtual_circuit_types property of a FastConnectProviderService.
    #: This constant has a value of "PRIVATE"
    SUPPORTED_VIRTUAL_CIRCUIT_TYPES_PRIVATE = "PRIVATE"

    #: A constant which can be used with the type property of a FastConnectProviderService.
    #: This constant has a value of "LAYER2"
    TYPE_LAYER2 = "LAYER2"

    #: A constant which can be used with the type property of a FastConnectProviderService.
    #: This constant has a value of "LAYER3"
    TYPE_LAYER3 = "LAYER3"

    def __init__(self, **kwargs):
        """
        Initializes a new FastConnectProviderService object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this FastConnectProviderService.
        :type description: str

        :param id:
            The value to assign to the id property of this FastConnectProviderService.
        :type id: str

        :param private_peering_bgp_management:
            The value to assign to the private_peering_bgp_management property of this FastConnectProviderService.
            Allowed values for this property are: "CUSTOMER_MANAGED", "PROVIDER_MANAGED", "ORACLE_MANAGED"
        :type private_peering_bgp_management: str

        :param provider_name:
            The value to assign to the provider_name property of this FastConnectProviderService.
        :type provider_name: str

        :param provider_service_name:
            The value to assign to the provider_service_name property of this FastConnectProviderService.
        :type provider_service_name: str

        :param public_peering_bgp_management:
            The value to assign to the public_peering_bgp_management property of this FastConnectProviderService.
            Allowed values for this property are: "CUSTOMER_MANAGED", "PROVIDER_MANAGED", "ORACLE_MANAGED"
        :type public_peering_bgp_management: str

        :param supported_virtual_circuit_types:
            The value to assign to the supported_virtual_circuit_types property of this FastConnectProviderService.
            Allowed values for items in this list are: "PUBLIC", "PRIVATE"
        :type supported_virtual_circuit_types: list[str]

        :param type:
            The value to assign to the type property of this FastConnectProviderService.
            Allowed values for this property are: "LAYER2", "LAYER3"
        :type type: str

        """
        self.swagger_types = {
            'description': 'str',
            'id': 'str',
            'private_peering_bgp_management': 'str',
            'provider_name': 'str',
            'provider_service_name': 'str',
            'public_peering_bgp_management': 'str',
            'supported_virtual_circuit_types': 'list[str]',
            'type': 'str'
        }

        self.attribute_map = {
            'description': 'description',
            'id': 'id',
            'private_peering_bgp_management': 'privatePeeringBgpManagement',
            'provider_name': 'providerName',
            'provider_service_name': 'providerServiceName',
            'public_peering_bgp_management': 'publicPeeringBgpManagement',
            'supported_virtual_circuit_types': 'supportedVirtualCircuitTypes',
            'type': 'type'
        }

        self._description = None
        self._id = None
        self._private_peering_bgp_management = None
        self._provider_name = None
        self._provider_service_name = None
        self._public_peering_bgp_management = None
        self._supported_virtual_circuit_types = None
        self._type = None

    @property
    def description(self):
        """
        Gets the description of this FastConnectProviderService.
        The location of the provider's website or portal. This portal is where you can get information
        about the provider service, create a virtual circuit connection from the provider to Oracle
        Cloud Infrastructure, and retrieve your provider service key for that virtual circuit connection.

        Example: `https://example.com`


        :return: The description of this FastConnectProviderService.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this FastConnectProviderService.
        The location of the provider's website or portal. This portal is where you can get information
        about the provider service, create a virtual circuit connection from the provider to Oracle
        Cloud Infrastructure, and retrieve your provider service key for that virtual circuit connection.

        Example: `https://example.com`


        :param description: The description of this FastConnectProviderService.
        :type: str
        """
        self._description = description

    @property
    def id(self):
        """
        **[Required]** Gets the id of this FastConnectProviderService.
        The `OCID`__ of the service offered by the provider.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this FastConnectProviderService.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FastConnectProviderService.
        The `OCID`__ of the service offered by the provider.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this FastConnectProviderService.
        :type: str
        """
        self._id = id

    @property
    def private_peering_bgp_management(self):
        """
        **[Required]** Gets the private_peering_bgp_management of this FastConnectProviderService.
        Who is responsible for managing the private peering BGP information.

        Allowed values for this property are: "CUSTOMER_MANAGED", "PROVIDER_MANAGED", "ORACLE_MANAGED"


        :return: The private_peering_bgp_management of this FastConnectProviderService.
        :rtype: str
        """
        return self._private_peering_bgp_management

    @private_peering_bgp_management.setter
    def private_peering_bgp_management(self, private_peering_bgp_management):
        """
        Sets the private_peering_bgp_management of this FastConnectProviderService.
        Who is responsible for managing the private peering BGP information.


        :param private_peering_bgp_management: The private_peering_bgp_management of this FastConnectProviderService.
        :type: str
        """
        allowed_values = ["CUSTOMER_MANAGED", "PROVIDER_MANAGED", "ORACLE_MANAGED"]
        if not value_allowed_none_or_none_sentinel(private_peering_bgp_management, allowed_values):
            raise ValueError(
                "Invalid value for `private_peering_bgp_management`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._private_peering_bgp_management = private_peering_bgp_management

    @property
    def provider_name(self):
        """
        **[Required]** Gets the provider_name of this FastConnectProviderService.
        The name of the provider.


        :return: The provider_name of this FastConnectProviderService.
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """
        Sets the provider_name of this FastConnectProviderService.
        The name of the provider.


        :param provider_name: The provider_name of this FastConnectProviderService.
        :type: str
        """
        self._provider_name = provider_name

    @property
    def provider_service_name(self):
        """
        **[Required]** Gets the provider_service_name of this FastConnectProviderService.
        The name of the service offered by the provider.


        :return: The provider_service_name of this FastConnectProviderService.
        :rtype: str
        """
        return self._provider_service_name

    @provider_service_name.setter
    def provider_service_name(self, provider_service_name):
        """
        Sets the provider_service_name of this FastConnectProviderService.
        The name of the service offered by the provider.


        :param provider_service_name: The provider_service_name of this FastConnectProviderService.
        :type: str
        """
        self._provider_service_name = provider_service_name

    @property
    def public_peering_bgp_management(self):
        """
        **[Required]** Gets the public_peering_bgp_management of this FastConnectProviderService.
        Who is responsible for managing the public peering BGP information.

        Allowed values for this property are: "CUSTOMER_MANAGED", "PROVIDER_MANAGED", "ORACLE_MANAGED"


        :return: The public_peering_bgp_management of this FastConnectProviderService.
        :rtype: str
        """
        return self._public_peering_bgp_management

    @public_peering_bgp_management.setter
    def public_peering_bgp_management(self, public_peering_bgp_management):
        """
        Sets the public_peering_bgp_management of this FastConnectProviderService.
        Who is responsible for managing the public peering BGP information.


        :param public_peering_bgp_management: The public_peering_bgp_management of this FastConnectProviderService.
        :type: str
        """
        allowed_values = ["CUSTOMER_MANAGED", "PROVIDER_MANAGED", "ORACLE_MANAGED"]
        if not value_allowed_none_or_none_sentinel(public_peering_bgp_management, allowed_values):
            raise ValueError(
                "Invalid value for `public_peering_bgp_management`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._public_peering_bgp_management = public_peering_bgp_management

    @property
    def supported_virtual_circuit_types(self):
        """
        Gets the supported_virtual_circuit_types of this FastConnectProviderService.
        An array of virtual circuit types supported by this service.

        Allowed values for items in this list are: "PUBLIC", "PRIVATE"


        :return: The supported_virtual_circuit_types of this FastConnectProviderService.
        :rtype: list[str]
        """
        return self._supported_virtual_circuit_types

    @supported_virtual_circuit_types.setter
    def supported_virtual_circuit_types(self, supported_virtual_circuit_types):
        """
        Sets the supported_virtual_circuit_types of this FastConnectProviderService.
        An array of virtual circuit types supported by this service.


        :param supported_virtual_circuit_types: The supported_virtual_circuit_types of this FastConnectProviderService.
        :type: list[str]
        """
        allowed_values = ["PUBLIC", "PRIVATE"]

        if supported_virtual_circuit_types and supported_virtual_circuit_types is not NONE_SENTINEL:
            for value in supported_virtual_circuit_types:
                if not value_allowed_none_or_none_sentinel(value, allowed_values):
                    raise ValueError(
                        "Invalid value for `supported_virtual_circuit_types`, must be None or one of {0}"
                        .format(allowed_values)
                    )
        self._supported_virtual_circuit_types = supported_virtual_circuit_types

    @property
    def type(self):
        """
        **[Required]** Gets the type of this FastConnectProviderService.
        Provider service type.

        Allowed values for this property are: "LAYER2", "LAYER3"


        :return: The type of this FastConnectProviderService.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this FastConnectProviderService.
        Provider service type.


        :param type: The type of this FastConnectProviderService.
        :type: str
        """
        allowed_values = ["LAYER2", "LAYER3"]
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
