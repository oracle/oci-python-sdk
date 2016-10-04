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


class UpdateRouteTableDetails(object):

    def __init__(self):

        self.swagger_types = {
            'route_rules': 'list[RouteRule]'
        }

        self.attribute_map = {
            'route_rules': 'routeRules'
        }

        self._route_rules = None


    @property
    def route_rules(self):
        """
        Gets the route_rules of this UpdateRouteTableDetails.
        The collection of rules used for routing destination IPs to network devices.

        :return: The route_rules of this UpdateRouteTableDetails.
        :rtype: list[RouteRule]
        """
        return self._route_rules

    @route_rules.setter
    def route_rules(self, route_rules):
        """
        Sets the route_rules of this UpdateRouteTableDetails.
        The collection of rules used for routing destination IPs to network devices.

        :param route_rules: The route_rules of this UpdateRouteTableDetails.
        :type: list[RouteRule]
        """
        self._route_rules = route_rules

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

