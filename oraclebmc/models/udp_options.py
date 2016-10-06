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


class UdpOptions(object):

    def __init__(self):

        self.swagger_types = {
            'destination_port_range': 'PortRange'
        }

        self.attribute_map = {
            'destination_port_range': 'destinationPortRange'
        }

        self._destination_port_range = None

    @property
    def destination_port_range(self):
        """
        Gets the destination_port_range of this UdpOptions.
        A single destination port or a range.

        :return: The destination_port_range of this UdpOptions.
        :rtype: PortRange
        """
        return self._destination_port_range

    @destination_port_range.setter
    def destination_port_range(self, destination_port_range):
        """
        Sets the destination_port_range of this UdpOptions.
        A single destination port or a range.

        :param destination_port_range: The destination_port_range of this UdpOptions.
        :type: PortRange
        """
        self._destination_port_range = destination_port_range

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
