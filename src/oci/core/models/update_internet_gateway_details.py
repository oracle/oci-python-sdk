# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateInternetGatewayDetails(object):

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateInternetGatewayDetails object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateInternetGatewayDetails.
        :type display_name: str

        :param is_enabled:
            The value to assign to the is_enabled property of this UpdateInternetGatewayDetails.
        :type is_enabled: bool

        """
        self.swagger_types = {
            'display_name': 'str',
            'is_enabled': 'bool'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'is_enabled': 'isEnabled'
        }

        self._display_name = None
        self._is_enabled = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateInternetGatewayDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this UpdateInternetGatewayDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateInternetGatewayDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this UpdateInternetGatewayDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this UpdateInternetGatewayDetails.
        Whether the gateway is enabled.


        :return: The is_enabled of this UpdateInternetGatewayDetails.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this UpdateInternetGatewayDetails.
        Whether the gateway is enabled.


        :param is_enabled: The is_enabled of this UpdateInternetGatewayDetails.
        :type: bool
        """
        self._is_enabled = is_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
