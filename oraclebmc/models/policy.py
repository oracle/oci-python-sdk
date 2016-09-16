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

class Policy(object):

    def __init__(self):

        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'name': 'str',
            'statements': 'list[str]',
            'description': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'inactive_status': 'int',
            'version_date': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'name': 'name',
            'statements': 'statements',
            'description': 'description',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'inactive_status': 'inactiveStatus',
            'version_date': 'versionDate'
        }

        self._id = None
        self._compartment_id = None
        self._name = None
        self._statements = None
        self._description = None
        self._time_created = None
        self._lifecycle_state = None
        self._inactive_status = None
        self._version_date = None


    @property
    def id(self):
        """
        Gets the id of this Policy.
        The policy's Oracle ID (OCID).

        :return: The id of this Policy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Policy.
        The policy's Oracle ID (OCID).

        :param id: The id of this Policy.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this Policy.
        The OCID of the tenancy containing the policy.

        :return: The compartment_id of this Policy.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Policy.
        The OCID of the tenancy containing the policy.

        :param compartment_id: The compartment_id of this Policy.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        Gets the name of this Policy.
        The unique, unchangeable name you assign to the policy during creation. Must be unique across all\npolicies in the tenancy.\n

        :return: The name of this Policy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Policy.
        The unique, unchangeable name you assign to the policy during creation. Must be unique across all\npolicies in the tenancy.\n

        :param name: The name of this Policy.
        :type: str
        """
        self._name = name

    @property
    def statements(self):
        """
        Gets the statements of this Policy.
        An array of one or more policy statements written in the policy language.

        :return: The statements of this Policy.
        :rtype: list[str]
        """
        return self._statements

    @statements.setter
    def statements(self, statements):
        """
        Sets the statements of this Policy.
        An array of one or more policy statements written in the policy language.

        :param statements: The statements of this Policy.
        :type: list[str]
        """
        self._statements = statements

    @property
    def description(self):
        """
        Gets the description of this Policy.
        The non-unique, changeable description you assign to the policy during creation.

        :return: The description of this Policy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Policy.
        The non-unique, changeable description you assign to the policy during creation.

        :param description: The description of this Policy.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        Gets the time_created of this Policy.
        Date and time the policy was created.

        :return: The time_created of this Policy.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Policy.
        Date and time the policy was created.

        :param time_created: The time_created of this Policy.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Policy.
        The policy's current state. After creating a policy, make sure its `lifecycleState` changes from CREATING to\nACTIVE before using it.\n

        :return: The lifecycle_state of this Policy.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Policy.
        The policy's current state. After creating a policy, make sure its `lifecycleState` changes from CREATING to\nACTIVE before using it.\n

        :param lifecycle_state: The lifecycle_state of this Policy.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]
        if lifecycle_state not in allowed_values:
            raise ValueError(
                "Invalid value for `lifecycle_state`, must be one of {0}"
                .format(allowed_values)
            )
        self._lifecycle_state = lifecycle_state

    @property
    def inactive_status(self):
        """
        Gets the inactive_status of this Policy.
        The detailed status of INACTIVE lifecycleState.

        :return: The inactive_status of this Policy.
        :rtype: int
        """
        return self._inactive_status

    @inactive_status.setter
    def inactive_status(self, inactive_status):
        """
        Sets the inactive_status of this Policy.
        The detailed status of INACTIVE lifecycleState.

        :param inactive_status: The inactive_status of this Policy.
        :type: int
        """
        self._inactive_status = inactive_status

    @property
    def version_date(self):
        """
        Gets the version_date of this Policy.
        The version of the policy. If null or set to an empty string, when a request comes in for authorization, the\npolicy will be evaluated according to the current behavior of the services at that moment. If set to a particular\ndate (YYYY-MM-DD), the policy will be evaluated according to the behavior of the services on that date.\n

        :return: The version_date of this Policy.
        :rtype: datetime
        """
        return self._version_date

    @version_date.setter
    def version_date(self, version_date):
        """
        Sets the version_date of this Policy.
        The version of the policy. If null or set to an empty string, when a request comes in for authorization, the\npolicy will be evaluated according to the current behavior of the services at that moment. If set to a particular\ndate (YYYY-MM-DD), the policy will be evaluated according to the behavior of the services on that date.\n

        :param version_date: The version_date of this Policy.
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

