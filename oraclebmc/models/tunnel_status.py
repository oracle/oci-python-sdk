# coding: utf-8

# This is a modified version of the same template from swagger-codegen.
# The original can be found at https://github.com/swagger-api/swagger-codegen.
# The original license is below.
#
#     Copyright 2016 SmartBear Software
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#
#     Ref: https://github.com/swagger-api/swagger-codegen


from ..util import formatted_flat_dict


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
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this TunnelStatus.
        The tunnel's current state.

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
            raise ValueError(
                "Invalid value for `lifecycle_state`, must be one of {0}"
                .format(allowed_values)
            )
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this TunnelStatus.
        The date and time the IPSec connection was created.

        :return: The time_created of this TunnelStatus.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this TunnelStatus.
        The date and time the IPSec connection was created.

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


    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

