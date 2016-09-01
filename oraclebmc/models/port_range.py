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

class PortRange(object):

    def __init__(self):

        self.swagger_types = {
            'max': 'int',
            'min': 'int'
        }

        self.attribute_map = {
            'max': 'max',
            'min': 'min'
        }

        self._max = None
        self._min = None


    @property
    def max(self):
        """
        Gets the max of this PortRange.
        The maximum port number. Must not be lower than the minimum port number. To specify\na single port number, set both the min and max to the same value.\n

        :return: The max of this PortRange.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """
        Sets the max of this PortRange.
        The maximum port number. Must not be lower than the minimum port number. To specify\na single port number, set both the min and max to the same value.\n

        :param max: The max of this PortRange.
        :type: int
        """
        self._max = max

    @property
    def min(self):
        """
        Gets the min of this PortRange.
        The minimum port number. Must not be greater than the maximum port number.

        :return: The min of this PortRange.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """
        Sets the min of this PortRange.
        The minimum port number. Must not be greater than the maximum port number.

        :param min: The min of this PortRange.
        :type: int
        """
        self._min = min

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

