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

class TunnelConfig(object):

    def __init__(self):
        """
        TunnelConfig - a model defined in Swagger
        """
        self.swagger_types = {
            'ip_address': 'str',
            'shared_secret': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'ip_address': 'ipAddress',
            'shared_secret': 'sharedSecret',
            'time_created': 'timeCreated'
        }

        self._ip_address = None
        self._shared_secret = None
        self._time_created = None

    @property
    def ip_address(self):
        """
        Gets the ip_address of this TunnelConfig.
        The IP address of Oracle's VPN headend.

        :return: The ip_address of this TunnelConfig.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this TunnelConfig.
        The IP address of Oracle's VPN headend.

        :param ip_address: The ip_address of this TunnelConfig.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def shared_secret(self):
        """
        Gets the shared_secret of this TunnelConfig.
        The shared secret of the IPsec tunnel.

        :return: The shared_secret of this TunnelConfig.
        :rtype: str
        """
        return self._shared_secret

    @shared_secret.setter
    def shared_secret(self, shared_secret):
        """
        Sets the shared_secret of this TunnelConfig.
        The shared secret of the IPsec tunnel.

        :param shared_secret: The shared_secret of this TunnelConfig.
        :type: str
        """
        self._shared_secret = shared_secret

    @property
    def time_created(self):
        """
        Gets the time_created of this TunnelConfig.
        Date and time the IPsec connection was created.

        :return: The time_created of this TunnelConfig.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this TunnelConfig.
        Date and time the IPsec connection was created.

        :param time_created: The time_created of this TunnelConfig.
        :type: datetime
        """
        self._time_created = time_created

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

