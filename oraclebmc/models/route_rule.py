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

