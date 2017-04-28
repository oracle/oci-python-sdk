# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class TunnelStatus(object):

    def __init__(self):

        self.swagger_types = {
            'ip_address': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_state_modified': 'datetime'
        }

        self.attribute_map = {
            'ip_address': 'ipAddress',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_state_modified': 'timeStateModified'
        }

        self._ip_address = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_state_modified = None

    @property
    def ip_address(self):
        """
        Gets the ip_address of this TunnelStatus.
        The IP address of Oracle's VPN headend.

        Example: `129.146.17.50`


        :return: The ip_address of this TunnelStatus.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this TunnelStatus.
        The IP address of Oracle's VPN headend.

        Example: `129.146.17.50`


        :param ip_address: The ip_address of this TunnelStatus.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this TunnelStatus.
        The tunnel's current state.

        Allowed values for this property are: "UP", "DOWN", "DOWN_FOR_MAINTENANCE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this TunnelStatus.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this TunnelStatus.
        The tunnel's current state.


        :param lifecycle_state: The lifecycle_state of this TunnelStatus.
        :type: str
        """
        allowed_values = ["UP", "DOWN", "DOWN_FOR_MAINTENANCE"]
        if lifecycle_state not in allowed_values:
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this TunnelStatus.
        The date and time the IPSec connection was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this TunnelStatus.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this TunnelStatus.
        The date and time the IPSec connection was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this TunnelStatus.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_state_modified(self):
        """
        Gets the time_state_modified of this TunnelStatus.
        When the state of the tunnel last changed, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_state_modified of this TunnelStatus.
        :rtype: datetime
        """
        return self._time_state_modified

    @time_state_modified.setter
    def time_state_modified(self, time_state_modified):
        """
        Sets the time_state_modified of this TunnelStatus.
        When the state of the tunnel last changed, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_state_modified: The time_state_modified of this TunnelStatus.
        :type: datetime
        """
        self._time_state_modified = time_state_modified

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
