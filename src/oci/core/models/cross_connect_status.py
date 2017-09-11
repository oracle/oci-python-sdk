# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class CrossConnectStatus(object):

    def __init__(self):

        self.swagger_types = {
            'cross_connect_id': 'str',
            'interface_state': 'str',
            'light_level_ind_bm': 'float',
            'light_level_indicator': 'str'
        }

        self.attribute_map = {
            'cross_connect_id': 'crossConnectId',
            'interface_state': 'interfaceState',
            'light_level_ind_bm': 'lightLevelIndBm',
            'light_level_indicator': 'lightLevelIndicator'
        }

        self._cross_connect_id = None
        self._interface_state = None
        self._light_level_ind_bm = None
        self._light_level_indicator = None

    @property
    def cross_connect_id(self):
        """
        Gets the cross_connect_id of this CrossConnectStatus.
        The OCID of the cross-connect.


        :return: The cross_connect_id of this CrossConnectStatus.
        :rtype: str
        """
        return self._cross_connect_id

    @cross_connect_id.setter
    def cross_connect_id(self, cross_connect_id):
        """
        Sets the cross_connect_id of this CrossConnectStatus.
        The OCID of the cross-connect.


        :param cross_connect_id: The cross_connect_id of this CrossConnectStatus.
        :type: str
        """
        self._cross_connect_id = cross_connect_id

    @property
    def interface_state(self):
        """
        Gets the interface_state of this CrossConnectStatus.
        Whether Oracle's side of the interface is up or down.

        Allowed values for this property are: "UP", "DOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The interface_state of this CrossConnectStatus.
        :rtype: str
        """
        return self._interface_state

    @interface_state.setter
    def interface_state(self, interface_state):
        """
        Sets the interface_state of this CrossConnectStatus.
        Whether Oracle's side of the interface is up or down.


        :param interface_state: The interface_state of this CrossConnectStatus.
        :type: str
        """
        allowed_values = ["UP", "DOWN"]
        if interface_state not in allowed_values:
            interface_state = 'UNKNOWN_ENUM_VALUE'
        self._interface_state = interface_state

    @property
    def light_level_ind_bm(self):
        """
        Gets the light_level_ind_bm of this CrossConnectStatus.
        The light level of the cross-connect (in dBm).

        Example: `14.0`


        :return: The light_level_ind_bm of this CrossConnectStatus.
        :rtype: float
        """
        return self._light_level_ind_bm

    @light_level_ind_bm.setter
    def light_level_ind_bm(self, light_level_ind_bm):
        """
        Sets the light_level_ind_bm of this CrossConnectStatus.
        The light level of the cross-connect (in dBm).

        Example: `14.0`


        :param light_level_ind_bm: The light_level_ind_bm of this CrossConnectStatus.
        :type: float
        """
        self._light_level_ind_bm = light_level_ind_bm

    @property
    def light_level_indicator(self):
        """
        Gets the light_level_indicator of this CrossConnectStatus.
        Status indicator corresponding to the light level.

          * **NO_LIGHT:** No measurable light

          * **LOW_WARN:** There's measurable light but it's too low

          * **HIGH_WARN:** Light level is too high

          * **BAD:** There's measurable light but the signal-to-noise ratio is bad

          * **GOOD:** Good light level

        Allowed values for this property are: "NO_LIGHT", "LOW_WARN", "HIGH_WARN", "BAD", "GOOD", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The light_level_indicator of this CrossConnectStatus.
        :rtype: str
        """
        return self._light_level_indicator

    @light_level_indicator.setter
    def light_level_indicator(self, light_level_indicator):
        """
        Sets the light_level_indicator of this CrossConnectStatus.
        Status indicator corresponding to the light level.

          * **NO_LIGHT:** No measurable light

          * **LOW_WARN:** There's measurable light but it's too low

          * **HIGH_WARN:** Light level is too high

          * **BAD:** There's measurable light but the signal-to-noise ratio is bad

          * **GOOD:** Good light level


        :param light_level_indicator: The light_level_indicator of this CrossConnectStatus.
        :type: str
        """
        allowed_values = ["NO_LIGHT", "LOW_WARN", "HIGH_WARN", "BAD", "GOOD"]
        if light_level_indicator not in allowed_values:
            light_level_indicator = 'UNKNOWN_ENUM_VALUE'
        self._light_level_indicator = light_level_indicator

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
