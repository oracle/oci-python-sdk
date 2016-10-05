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

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
