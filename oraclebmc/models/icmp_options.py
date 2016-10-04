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


class IcmpOptions(object):

    def __init__(self):

        self.swagger_types = {
            'code': 'int',
            'type': 'int'
        }

        self.attribute_map = {
            'code': 'code',
            'type': 'type'
        }

        self._code = None
        self._type = None


    @property
    def code(self):
        """
        Gets the code of this IcmpOptions.
        The ICMP code (optional).

        :return: The code of this IcmpOptions.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this IcmpOptions.
        The ICMP code (optional).

        :param code: The code of this IcmpOptions.
        :type: int
        """
        self._code = code

    @property
    def type(self):
        """
        Gets the type of this IcmpOptions.
        The ICMP type.

        :return: The type of this IcmpOptions.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this IcmpOptions.
        The ICMP type.

        :param type: The type of this IcmpOptions.
        :type: int
        """
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

