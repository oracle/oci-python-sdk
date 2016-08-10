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
            'display_name': 'str',
            'network_entity_id': 'str',
            'network_entity_type': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'cidr_block': 'cidrBlock',
            'display_name': 'displayName',
            'network_entity_id': 'networkEntityId',
            'network_entity_type': 'networkEntityType',
            'time_created': 'timeCreated'
        }

        self._cidr_block = None
        self._display_name = None
        self._network_entity_id = None
        self._network_entity_type = None
        self._time_created = None


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
    def display_name(self):
        """
        Gets the display_name of this RouteRule.
        A user-friendly name. Does not have to be unique, and it's unchangeable.\n

        :return: The display_name of this RouteRule.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this RouteRule.
        A user-friendly name. Does not have to be unique, and it's unchangeable.\n

        :param display_name: The display_name of this RouteRule.
        :type: str
        """
        self._display_name = display_name

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

    @property
    def network_entity_type(self):
        """
        Gets the network_entity_type of this RouteRule.
        The type of target.

        :return: The network_entity_type of this RouteRule.
        :rtype: str
        """
        return self._network_entity_type

    @network_entity_type.setter
    def network_entity_type(self, network_entity_type):
        """
        Sets the network_entity_type of this RouteRule.
        The type of target.

        :param network_entity_type: The network_entity_type of this RouteRule.
        :type: str
        """
        allowed_values = ["VNIC", "INTERNET_GATEWAY", "DYNAMICALLY_ROUTING_GATEWAY"]
        if network_entity_type not in allowed_values:
            raise ValueError(
                "Invalid value for `network_entity_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._network_entity_type = network_entity_type

    @property
    def time_created(self):
        """
        Gets the time_created of this RouteRule.
        Date and time the route rule was created.

        :return: The time_created of this RouteRule.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this RouteRule.
        Date and time the route rule was created.

        :param time_created: The time_created of this RouteRule.
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
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if objects are not equal
        """
        return not self == other

