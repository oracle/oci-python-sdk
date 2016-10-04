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


class UpdatePolicyDetails(object):

    def __init__(self):

        self.swagger_types = {
            'description': 'str',
            'statements': 'list[str]',
            'version_date': 'datetime'
        }

        self.attribute_map = {
            'description': 'description',
            'statements': 'statements',
            'version_date': 'versionDate'
        }

        self._description = None
        self._statements = None
        self._version_date = None


    @property
    def description(self):
        """
        Gets the description of this UpdatePolicyDetails.
        The non-unique, changeable description you assign to the policy.

        :return: The description of this UpdatePolicyDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdatePolicyDetails.
        The non-unique, changeable description you assign to the policy.

        :param description: The description of this UpdatePolicyDetails.
        :type: str
        """
        self._description = description

    @property
    def statements(self):
        """
        Gets the statements of this UpdatePolicyDetails.
        An array of policy statements written in the policy language. See\n[Policies](/Content/Identity/Concepts/policies.htm).\n

        :return: The statements of this UpdatePolicyDetails.
        :rtype: list[str]
        """
        return self._statements

    @statements.setter
    def statements(self, statements):
        """
        Sets the statements of this UpdatePolicyDetails.
        An array of policy statements written in the policy language. See\n[Policies](/Content/Identity/Concepts/policies.htm).\n

        :param statements: The statements of this UpdatePolicyDetails.
        :type: list[str]
        """
        self._statements = statements

    @property
    def version_date(self):
        """
        Gets the version_date of this UpdatePolicyDetails.
        The version of the policy. If null or set to an empty string, when a request comes in for authorization, the\npolicy will be evaluated according to the current behavior of the services at that moment. If set to a particular\ndate (YYYY-MM-DD), the policy will be evaluated according to the behavior of the services on that date.\n

        :return: The version_date of this UpdatePolicyDetails.
        :rtype: datetime
        """
        return self._version_date

    @version_date.setter
    def version_date(self, version_date):
        """
        Sets the version_date of this UpdatePolicyDetails.
        The version of the policy. If null or set to an empty string, when a request comes in for authorization, the\npolicy will be evaluated according to the current behavior of the services at that moment. If set to a particular\ndate (YYYY-MM-DD), the policy will be evaluated according to the behavior of the services on that date.\n

        :param version_date: The version_date of this UpdatePolicyDetails.
        :type: datetime
        """
        self._version_date = version_date

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

