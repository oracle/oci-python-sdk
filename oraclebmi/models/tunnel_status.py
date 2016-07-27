# coding: utf-8

"""
This is a modified version of the same template from swagger-codegen.
The original can be found at https://github.com/swagger-api/swagger-codegen.
The original license is below.

    Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems

class TunnelStatus(object):

    def __init__(self):
        """
        TunnelStatus - a model defined in Swagger
        """
        self.swagger_types = {
            'ip_address': 'str',
            'state': 'str',
            'time_created': 'datetime',
            'time_state_modified': 'datetime'
        }

        self.attribute_map = {
            'ip_address': 'ipAddress',
            'state': 'state',
            'time_created': 'timeCreated',
            'time_state_modified': 'timeStateModified'
        }

        self._ip_address = None
        self._state = None
        self._time_created = None
        self._time_state_modified = None

    @property
    def ip_address(self):
        """
        Gets the ip_address of this TunnelStatus.
        The IP address of Oracle's VPN headend.

        :return: The ip_address of this TunnelStatus.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this TunnelStatus.
        The IP address of Oracle's VPN headend.

        :param ip_address: The ip_address of this TunnelStatus.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def state(self):
        """
        Gets the state of this TunnelStatus.
        The tunnel's current state.

        :return: The state of this TunnelStatus.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this TunnelStatus.
        The tunnel's current state.

        :param state: The state of this TunnelStatus.
        :type: str
        """
        allowed_values = ["UP", "DOWN", "DOWN_FOR_MAINTENANCE"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state`, must be one of {0}"
                .format(allowed_values)
            )
        self._state = state

    @property
    def time_created(self):
        """
        Gets the time_created of this TunnelStatus.
        Date and time the IPsec connection was created.

        :return: The time_created of this TunnelStatus.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this TunnelStatus.
        Date and time the IPsec connection was created.

        :param time_created: The time_created of this TunnelStatus.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_state_modified(self):
        """
        Gets the time_state_modified of this TunnelStatus.
        When the state of the tunnel last changed.

        :return: The time_state_modified of this TunnelStatus.
        :rtype: datetime
        """
        return self._time_state_modified

    @time_state_modified.setter
    def time_state_modified(self, time_state_modified):
        """
        Sets the time_state_modified of this TunnelStatus.
        When the state of the tunnel last changed.

        :param time_state_modified: The time_state_modified of this TunnelStatus.
        :type: datetime
        """
        self._time_state_modified = time_state_modified

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if objects are not equal
        """
        return not self == other

