# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class UpdateCrossConnectDetails(object):

    def __init__(self):

        self.swagger_types = {
            'display_name': 'str',
            'is_active': 'bool'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'is_active': 'isActive'
        }

        self._display_name = None
        self._is_active = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateCrossConnectDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :return: The display_name of this UpdateCrossConnectDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateCrossConnectDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :param display_name: The display_name of this UpdateCrossConnectDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def is_active(self):
        """
        Gets the is_active of this UpdateCrossConnectDetails.
        Set to true to activate the cross-connect. You activate it after the physical cabling
        is complete, and you've confirmed the cross-connect's light levels are good and your side
        of the interface is up. Activation indicates to Oracle that the physical connection is ready.

        Example: `true`


        :return: The is_active of this UpdateCrossConnectDetails.
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """
        Sets the is_active of this UpdateCrossConnectDetails.
        Set to true to activate the cross-connect. You activate it after the physical cabling
        is complete, and you've confirmed the cross-connect's light levels are good and your side
        of the interface is up. Activation indicates to Oracle that the physical connection is ready.

        Example: `true`


        :param is_active: The is_active of this UpdateCrossConnectDetails.
        :type: bool
        """
        self._is_active = is_active

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
