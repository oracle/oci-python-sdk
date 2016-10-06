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


class IPSecConnectionDeviceStatus(object):

    def __init__(self):

        self.swagger_types = {
            'compartment_id': 'str',
            'id': 'str',
            'time_created': 'datetime',
            'tunnels': 'list[TunnelStatus]'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'id': 'id',
            'time_created': 'timeCreated',
            'tunnels': 'tunnels'
        }

        self._compartment_id = None
        self._id = None
        self._time_created = None
        self._tunnels = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this IPSecConnectionDeviceStatus.
        The OCID of the compartment containing the IPSec connection.

        :return: The compartment_id of this IPSecConnectionDeviceStatus.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this IPSecConnectionDeviceStatus.
        The OCID of the compartment containing the IPSec connection.

        :param compartment_id: The compartment_id of this IPSecConnectionDeviceStatus.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def id(self):
        """
        Gets the id of this IPSecConnectionDeviceStatus.
        The IPSec connection's Oracle ID (OCID).

        :return: The id of this IPSecConnectionDeviceStatus.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this IPSecConnectionDeviceStatus.
        The IPSec connection's Oracle ID (OCID).

        :param id: The id of this IPSecConnectionDeviceStatus.
        :type: str
        """
        self._id = id

    @property
    def time_created(self):
        """
        Gets the time_created of this IPSecConnectionDeviceStatus.
        The date and time the IPSec connection was created.

        :return: The time_created of this IPSecConnectionDeviceStatus.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this IPSecConnectionDeviceStatus.
        The date and time the IPSec connection was created.

        :param time_created: The time_created of this IPSecConnectionDeviceStatus.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def tunnels(self):
        """
        Gets the tunnels of this IPSecConnectionDeviceStatus.
        Two TunnelStatus objects.

        :return: The tunnels of this IPSecConnectionDeviceStatus.
        :rtype: list[TunnelStatus]
        """
        return self._tunnels

    @tunnels.setter
    def tunnels(self, tunnels):
        """
        Sets the tunnels of this IPSecConnectionDeviceStatus.
        Two TunnelStatus objects.

        :param tunnels: The tunnels of this IPSecConnectionDeviceStatus.
        :type: list[TunnelStatus]
        """
        self._tunnels = tunnels

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
