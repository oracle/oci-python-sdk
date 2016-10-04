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


class RouteRule(object):

    def __init__(self):

        self.swagger_types = {
            'cidr_block': 'str',
            'network_entity_id': 'str'
        }

        self.attribute_map = {
            'cidr_block': 'cidrBlock',
            'network_entity_id': 'networkEntityId'
        }

        self._cidr_block = None
        self._network_entity_id = None


    @property
    def cidr_block(self):
        """
        Gets the cidr_block of this RouteRule.
        A destination IP address range in CIDR notation. Matching packets will\nbe routed to the indicated network entity (the target).\n

        :return: The cidr_block of this RouteRule.
        :rtype: str
        """
        return self._cidr_block

    @cidr_block.setter
    def cidr_block(self, cidr_block):
        """
        Sets the cidr_block of this RouteRule.
        A destination IP address range in CIDR notation. Matching packets will\nbe routed to the indicated network entity (the target).\n

        :param cidr_block: The cidr_block of this RouteRule.
        :type: str
        """
        self._cidr_block = cidr_block

    @property
    def network_entity_id(self):
        """
        Gets the network_entity_id of this RouteRule.
        The OCID for the route rule's target.

        :return: The network_entity_id of this RouteRule.
        :rtype: str
        """
        return self._network_entity_id

    @network_entity_id.setter
    def network_entity_id(self, network_entity_id):
        """
        Sets the network_entity_id of this RouteRule.
        The OCID for the route rule's target.

        :param network_entity_id: The network_entity_id of this RouteRule.
        :type: str
        """
        self._network_entity_id = network_entity_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

