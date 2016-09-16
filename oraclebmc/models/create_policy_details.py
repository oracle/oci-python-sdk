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

class CreatePolicyDetails(object):

    def __init__(self):

        self.swagger_types = {
            'compartment_id': 'str',
            'name': 'str',
            'statements': 'list[str]',
            'description': 'str',
            'version_date': 'datetime'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'name': 'name',
            'statements': 'statements',
            'description': 'description',
            'version_date': 'versionDate'
        }

        self._compartment_id = None
        self._name = None
        self._statements = None
        self._description = None
        self._version_date = None


    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CreatePolicyDetails.
        The OCID of the tenancy containing the policy.

        :return: The compartment_id of this CreatePolicyDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreatePolicyDetails.
        The OCID of the tenancy containing the policy.

        :param compartment_id: The compartment_id of this CreatePolicyDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        Gets the name of this CreatePolicyDetails.
        A unique, unchangeable name you assign to the policy during creation. Must be unique across all policies\nin the tenancy.\n

        :return: The name of this CreatePolicyDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreatePolicyDetails.
        A unique, unchangeable name you assign to the policy during creation. Must be unique across all policies\nin the tenancy.\n

        :param name: The name of this CreatePolicyDetails.
        :type: str
        """
        self._name = name

    @property
    def statements(self):
        """
        Gets the statements of this CreatePolicyDetails.
        An array of policy statements written in the policy language. See\n[Policies](/Content/Identity/Concepts/policies.htm).\n

        :return: The statements of this CreatePolicyDetails.
        :rtype: list[str]
        """
        return self._statements

    @statements.setter
    def statements(self, statements):
        """
        Sets the statements of this CreatePolicyDetails.
        An array of policy statements written in the policy language. See\n[Policies](/Content/Identity/Concepts/policies.htm).\n

        :param statements: The statements of this CreatePolicyDetails.
        :type: list[str]
        """
        self._statements = statements

    @property
    def description(self):
        """
        Gets the description of this CreatePolicyDetails.
        The non-unique, changeable description you assign to the policy during creation.

        :return: The description of this CreatePolicyDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreatePolicyDetails.
        The non-unique, changeable description you assign to the policy during creation.

        :param description: The description of this CreatePolicyDetails.
        :type: str
        """
        self._description = description

    @property
    def version_date(self):
        """
        Gets the version_date of this CreatePolicyDetails.
        The version of the policy. If null or set to an empty string, when a request comes in for authorization, the\npolicy will be evaluated according to the current behavior of the services at that moment. If set to a particular\ndate (YYYY-MM-DD), the policy will be evaluated according to the behavior of the services on that date.\n

        :return: The version_date of this CreatePolicyDetails.
        :rtype: datetime
        """
        return self._version_date

    @version_date.setter
    def version_date(self, version_date):
        """
        Sets the version_date of this CreatePolicyDetails.
        The version of the policy. If null or set to an empty string, when a request comes in for authorization, the\npolicy will be evaluated according to the current behavior of the services at that moment. If set to a particular\ndate (YYYY-MM-DD), the policy will be evaluated according to the behavior of the services on that date.\n

        :param version_date: The version_date of this CreatePolicyDetails.
        :type: datetime
        """
        self._version_date = version_date

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

