# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FastConnectProviderService(object):

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
            Allowed values for this property are: "CUSTOMER_MANAGED", "PROVIDER_MANAGED", "ORACLE_MANAGED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type private_peering_bgp_management: str

        :param provider_name:
            The value to assign to the provider_name property of this FastConnectProviderService.
        :type provider_name: str

        :param provider_service_name:
            The value to assign to the provider_service_name property of this FastConnectProviderService.
        :type provider_service_name: str

        :param public_peering_bgp_management:
            The value to assign to the public_peering_bgp_management property of this FastConnectProviderService.
            Allowed values for this property are: "CUSTOMER_MANAGED", "PROVIDER_MANAGED", "ORACLE_MANAGED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type public_peering_bgp_management: str

        :param supported_virtual_circuit_types:
            The value to assign to the supported_virtual_circuit_types property of this FastConnectProviderService.
            Allowed values for items in this list are: "PUBLIC", "PRIVATE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type supported_virtual_circuit_types: list[str]

        :param type:
            The value to assign to the type property of this FastConnectProviderService.
            Allowed values for this property are: "LAYER2", "LAYER3", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
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
        A description of the service offered by the provider.


        :return: The description of this FastConnectProviderService.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this FastConnectProviderService.
        A description of the service offered by the provider.


        :param description: The description of this FastConnectProviderService.
        :type: str
        """
        self._description = description

    @property
    def id(self):
        """
        **[Required]** Gets the id of this FastConnectProviderService.
        The OCID of the service offered by the provider.


        :return: The id of this FastConnectProviderService.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FastConnectProviderService.
        The OCID of the service offered by the provider.


        :param id: The id of this FastConnectProviderService.
        :type: str
        """
        self._id = id

    @property
    def private_peering_bgp_management(self):
        """
        **[Required]** Gets the private_peering_bgp_management of this FastConnectProviderService.
        Private peering BGP management.

        Allowed values for this property are: "CUSTOMER_MANAGED", "PROVIDER_MANAGED", "ORACLE_MANAGED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The private_peering_bgp_management of this FastConnectProviderService.
        :rtype: str
        """
        return self._private_peering_bgp_management

    @private_peering_bgp_management.setter
    def private_peering_bgp_management(self, private_peering_bgp_management):
        """
        Sets the private_peering_bgp_management of this FastConnectProviderService.
        Private peering BGP management.


        :param private_peering_bgp_management: The private_peering_bgp_management of this FastConnectProviderService.
        :type: str
        """
        allowed_values = ["CUSTOMER_MANAGED", "PROVIDER_MANAGED", "ORACLE_MANAGED"]
        if not value_allowed_none_or_none_sentinel(private_peering_bgp_management, allowed_values):
            private_peering_bgp_management = 'UNKNOWN_ENUM_VALUE'
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
        Public peering BGP management.

        Allowed values for this property are: "CUSTOMER_MANAGED", "PROVIDER_MANAGED", "ORACLE_MANAGED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The public_peering_bgp_management of this FastConnectProviderService.
        :rtype: str
        """
        return self._public_peering_bgp_management

    @public_peering_bgp_management.setter
    def public_peering_bgp_management(self, public_peering_bgp_management):
        """
        Sets the public_peering_bgp_management of this FastConnectProviderService.
        Public peering BGP management.


        :param public_peering_bgp_management: The public_peering_bgp_management of this FastConnectProviderService.
        :type: str
        """
        allowed_values = ["CUSTOMER_MANAGED", "PROVIDER_MANAGED", "ORACLE_MANAGED"]
        if not value_allowed_none_or_none_sentinel(public_peering_bgp_management, allowed_values):
            public_peering_bgp_management = 'UNKNOWN_ENUM_VALUE'
        self._public_peering_bgp_management = public_peering_bgp_management

    @property
    def supported_virtual_circuit_types(self):
        """
        Gets the supported_virtual_circuit_types of this FastConnectProviderService.
        An array of virtual circuit types supported by this service.

        Allowed values for items in this list are: "PUBLIC", "PRIVATE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


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
        supported_virtual_circuit_types[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in supported_virtual_circuit_types]
        self._supported_virtual_circuit_types = supported_virtual_circuit_types

    @property
    def type(self):
        """
        **[Required]** Gets the type of this FastConnectProviderService.
        Provider service type.

        Allowed values for this property are: "LAYER2", "LAYER3", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


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
