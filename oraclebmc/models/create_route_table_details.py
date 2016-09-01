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

class CreateRouteTableDetails(object):

    def __init__(self):

        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'route_rules': 'list[RouteRule]',
            'vcn_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'route_rules': 'routeRules',
            'vcn_id': 'vcnId'
        }

        self._compartment_id = None
        self._display_name = None
        self._route_rules = None
        self._vcn_id = None


    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CreateRouteTableDetails.
        The OCID of the compartment to contain the route table.

        :return: The compartment_id of this CreateRouteTableDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateRouteTableDetails.
        The OCID of the compartment to contain the route table.

        :param compartment_id: The compartment_id of this CreateRouteTableDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateRouteTableDetails.
        A user-friendly name. Does not have to be unique, and it's not changeable.\n

        :return: The display_name of this CreateRouteTableDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateRouteTableDetails.
        A user-friendly name. Does not have to be unique, and it's not changeable.\n

        :param display_name: The display_name of this CreateRouteTableDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def route_rules(self):
        """
        Gets the route_rules of this CreateRouteTableDetails.
        The collection of rules used for routing destination IPs to network devices.

        :return: The route_rules of this CreateRouteTableDetails.
        :rtype: list[RouteRule]
        """
        return self._route_rules

    @route_rules.setter
    def route_rules(self, route_rules):
        """
        Sets the route_rules of this CreateRouteTableDetails.
        The collection of rules used for routing destination IPs to network devices.

        :param route_rules: The route_rules of this CreateRouteTableDetails.
        :type: list[RouteRule]
        """
        self._route_rules = route_rules

    @property
    def vcn_id(self):
        """
        Gets the vcn_id of this CreateRouteTableDetails.
        The OCID of the VCN the route table belongs to.

        :return: The vcn_id of this CreateRouteTableDetails.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this CreateRouteTableDetails.
        The OCID of the VCN the route table belongs to.

        :param vcn_id: The vcn_id of this CreateRouteTableDetails.
        :type: str
        """
        self._vcn_id = vcn_id

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

