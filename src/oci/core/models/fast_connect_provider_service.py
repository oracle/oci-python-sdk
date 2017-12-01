# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FastConnectProviderService(object):

    def __init__(self, **kwargs):
        """
        Initializes a new FastConnectProviderService object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this FastConnectProviderService.
        :type description: str

        :param provider_name:
            The value to assign to the provider_name property of this FastConnectProviderService.
        :type provider_name: str

        :param provider_service_name:
            The value to assign to the provider_service_name property of this FastConnectProviderService.
        :type provider_service_name: str

        """
        self.swagger_types = {
            'description': 'str',
            'provider_name': 'str',
            'provider_service_name': 'str'
        }

        self.attribute_map = {
            'description': 'description',
            'provider_name': 'providerName',
            'provider_service_name': 'providerServiceName'
        }

        self._description = None
        self._provider_name = None
        self._provider_service_name = None

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
    def provider_name(self):
        """
        Gets the provider_name of this FastConnectProviderService.
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
        Gets the provider_service_name of this FastConnectProviderService.
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

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
