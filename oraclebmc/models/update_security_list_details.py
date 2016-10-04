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


class UpdateSecurityListDetails(object):

    def __init__(self):

        self.swagger_types = {
            'egress_security_rules': 'list[EgressSecurityRule]',
            'ingress_security_rules': 'list[IngressSecurityRule]'
        }

        self.attribute_map = {
            'egress_security_rules': 'egressSecurityRules',
            'ingress_security_rules': 'ingressSecurityRules'
        }

        self._egress_security_rules = None
        self._ingress_security_rules = None


    @property
    def egress_security_rules(self):
        """
        Gets the egress_security_rules of this UpdateSecurityListDetails.
        Rules for allowing egress IP packets.

        :return: The egress_security_rules of this UpdateSecurityListDetails.
        :rtype: list[EgressSecurityRule]
        """
        return self._egress_security_rules

    @egress_security_rules.setter
    def egress_security_rules(self, egress_security_rules):
        """
        Sets the egress_security_rules of this UpdateSecurityListDetails.
        Rules for allowing egress IP packets.

        :param egress_security_rules: The egress_security_rules of this UpdateSecurityListDetails.
        :type: list[EgressSecurityRule]
        """
        self._egress_security_rules = egress_security_rules

    @property
    def ingress_security_rules(self):
        """
        Gets the ingress_security_rules of this UpdateSecurityListDetails.
        Rules for allowing ingress IP packets.

        :return: The ingress_security_rules of this UpdateSecurityListDetails.
        :rtype: list[IngressSecurityRule]
        """
        return self._ingress_security_rules

    @ingress_security_rules.setter
    def ingress_security_rules(self, ingress_security_rules):
        """
        Sets the ingress_security_rules of this UpdateSecurityListDetails.
        Rules for allowing ingress IP packets.

        :param ingress_security_rules: The ingress_security_rules of this UpdateSecurityListDetails.
        :type: list[IngressSecurityRule]
        """
        self._ingress_security_rules = ingress_security_rules

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

