# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class UpdateInternetGatewayDetails(object):

    def __init__(self):

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


        :return: The display_name of this UpdateInternetGatewayDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateInternetGatewayDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.


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
