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

class UpdatePolicyRequest(object):

    def __init__(self):

        self.swagger_types = {
            'description': 'str',
            'statements': 'list[str]'
        }

        self.attribute_map = {
            'description': 'description',
            'statements': 'statements'
        }

        self._description = None
        self._statements = None


    @property
    def description(self):
        """
        Gets the description of this UpdatePolicyRequest.
        The non-unique, changeable description you assign to the policy.

        :return: The description of this UpdatePolicyRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdatePolicyRequest.
        The non-unique, changeable description you assign to the policy.

        :param description: The description of this UpdatePolicyRequest.
        :type: str
        """
        self._description = description

    @property
    def statements(self):
        """
        Gets the statements of this UpdatePolicyRequest.
        An array of policy statements written in the policy language. See\n[Policies](../../../#Identity/Concepts/policies.htm).\n

        :return: The statements of this UpdatePolicyRequest.
        :rtype: list[str]
        """
        return self._statements

    @statements.setter
    def statements(self, statements):
        """
        Sets the statements of this UpdatePolicyRequest.
        An array of policy statements written in the policy language. See\n[Policies](../../../#Identity/Concepts/policies.htm).\n

        :param statements: The statements of this UpdatePolicyRequest.
        :type: list[str]
        """
        self._statements = statements

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

