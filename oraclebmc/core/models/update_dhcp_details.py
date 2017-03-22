# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class UpdateDhcpDetails(object):

    def __init__(self):

        self.swagger_types = {
            'display_name': 'str',
            'options': 'list[DhcpOption]'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'options': 'options'
        }

        self._display_name = None
        self._options = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateDhcpDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :return: The display_name of this UpdateDhcpDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateDhcpDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :param display_name: The display_name of this UpdateDhcpDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def options(self):
        """
        Gets the options of this UpdateDhcpDetails.

        :return: The options of this UpdateDhcpDetails.
        :rtype: list[DhcpOption]
        """
        return self._options

    @options.setter
    def options(self, options):
        """
        Sets the options of this UpdateDhcpDetails.

        :param options: The options of this UpdateDhcpDetails.
        :type: list[DhcpOption]
        """
        self._options = options

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
