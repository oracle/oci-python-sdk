# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CrossConnectStatus(object):
    """
    The status of the cross-connect.
    """

    #: A constant which can be used with the interface_state property of a CrossConnectStatus.
    #: This constant has a value of "UP"
    INTERFACE_STATE_UP = "UP"

    #: A constant which can be used with the interface_state property of a CrossConnectStatus.
    #: This constant has a value of "DOWN"
    INTERFACE_STATE_DOWN = "DOWN"

    #: A constant which can be used with the light_level_indicator property of a CrossConnectStatus.
    #: This constant has a value of "NO_LIGHT"
    LIGHT_LEVEL_INDICATOR_NO_LIGHT = "NO_LIGHT"

    #: A constant which can be used with the light_level_indicator property of a CrossConnectStatus.
    #: This constant has a value of "LOW_WARN"
    LIGHT_LEVEL_INDICATOR_LOW_WARN = "LOW_WARN"

    #: A constant which can be used with the light_level_indicator property of a CrossConnectStatus.
    #: This constant has a value of "HIGH_WARN"
    LIGHT_LEVEL_INDICATOR_HIGH_WARN = "HIGH_WARN"

    #: A constant which can be used with the light_level_indicator property of a CrossConnectStatus.
    #: This constant has a value of "BAD"
    LIGHT_LEVEL_INDICATOR_BAD = "BAD"

    #: A constant which can be used with the light_level_indicator property of a CrossConnectStatus.
    #: This constant has a value of "GOOD"
    LIGHT_LEVEL_INDICATOR_GOOD = "GOOD"

    def __init__(self, **kwargs):
        """
        Initializes a new CrossConnectStatus object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cross_connect_id:
            The value to assign to the cross_connect_id property of this CrossConnectStatus.
        :type cross_connect_id: str

        :param interface_state:
            The value to assign to the interface_state property of this CrossConnectStatus.
            Allowed values for this property are: "UP", "DOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type interface_state: str

        :param light_level_ind_bm:
            The value to assign to the light_level_ind_bm property of this CrossConnectStatus.
        :type light_level_ind_bm: float

        :param light_level_indicator:
            The value to assign to the light_level_indicator property of this CrossConnectStatus.
            Allowed values for this property are: "NO_LIGHT", "LOW_WARN", "HIGH_WARN", "BAD", "GOOD", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type light_level_indicator: str

        """
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
        **[Required]** Gets the cross_connect_id of this CrossConnectStatus.
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
        if not value_allowed_none_or_none_sentinel(interface_state, allowed_values):
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
        if not value_allowed_none_or_none_sentinel(light_level_indicator, allowed_values):
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
