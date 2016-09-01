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

from pprint import pformat
from six import iteritems

class IPSecConnectionDeviceConfig(object):

    def __init__(self):

        self.swagger_types = {
            'compartment_id': 'str',
            'id': 'str',
            'time_created': 'datetime',
            'tunnels': 'list[TunnelConfig]'
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
        Gets the compartment_id of this IPSecConnectionDeviceConfig.
        The OCID of the compartment containing the IPsec connection.

        :return: The compartment_id of this IPSecConnectionDeviceConfig.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this IPSecConnectionDeviceConfig.
        The OCID of the compartment containing the IPsec connection.

        :param compartment_id: The compartment_id of this IPSecConnectionDeviceConfig.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def id(self):
        """
        Gets the id of this IPSecConnectionDeviceConfig.
        The IPsec connection's Oracle ID (OCID).

        :return: The id of this IPSecConnectionDeviceConfig.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this IPSecConnectionDeviceConfig.
        The IPsec connection's Oracle ID (OCID).

        :param id: The id of this IPSecConnectionDeviceConfig.
        :type: str
        """
        self._id = id

    @property
    def time_created(self):
        """
        Gets the time_created of this IPSecConnectionDeviceConfig.
        The date and time the IPsec connection was created.

        :return: The time_created of this IPSecConnectionDeviceConfig.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this IPSecConnectionDeviceConfig.
        The date and time the IPsec connection was created.

        :param time_created: The time_created of this IPSecConnectionDeviceConfig.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def tunnels(self):
        """
        Gets the tunnels of this IPSecConnectionDeviceConfig.
        Two [TunnelConfig](#/en/core/20160918/TunnelConfig/) objects.

        :return: The tunnels of this IPSecConnectionDeviceConfig.
        :rtype: list[TunnelConfig]
        """
        return self._tunnels

    @tunnels.setter
    def tunnels(self, tunnels):
        """
        Sets the tunnels of this IPSecConnectionDeviceConfig.
        Two [TunnelConfig](#/en/core/20160918/TunnelConfig/) objects.

        :param tunnels: The tunnels of this IPSecConnectionDeviceConfig.
        :type: list[TunnelConfig]
        """
        self._tunnels = tunnels

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
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if objects are not equal
        """
        return not self == other

