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


class User(object):

    def __init__(self):

        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'name': 'str',
            'description': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'inactive_status': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'name': 'name',
            'description': 'description',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'inactive_status': 'inactiveStatus'
        }

        self._id = None
        self._compartment_id = None
        self._name = None
        self._description = None
        self._time_created = None
        self._lifecycle_state = None
        self._inactive_status = None


    @property
    def id(self):
        """
        Gets the id of this User.
        The user's Oracle ID (OCID).

        :return: The id of this User.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this User.
        The user's Oracle ID (OCID).

        :param id: The id of this User.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this User.
        The OCID of the tenancy containing the user.

        :return: The compartment_id of this User.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this User.
        The OCID of the tenancy containing the user.

        :param compartment_id: The compartment_id of this User.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        Gets the name of this User.
        The unique, unchangeable name you assign to the user during creation. This is the user's login for\nthe Console. Must be unique across all users in the tenancy.\n

        :return: The name of this User.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this User.
        The unique, unchangeable name you assign to the user during creation. This is the user's login for\nthe Console. Must be unique across all users in the tenancy.\n

        :param name: The name of this User.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this User.
        The non-unique, changeable description you assign to the user during creation.

        :return: The description of this User.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this User.
        The non-unique, changeable description you assign to the user during creation.

        :param description: The description of this User.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        Gets the time_created of this User.
        Date and time the user was created.

        :return: The time_created of this User.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this User.
        Date and time the user was created.

        :param time_created: The time_created of this User.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this User.
        The user's current state. After creating a user, make sure its `lifecycleState` changes from CREATING to\nACTIVE before using it.\n

        :return: The lifecycle_state of this User.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this User.
        The user's current state. After creating a user, make sure its `lifecycleState` changes from CREATING to\nACTIVE before using it.\n

        :param lifecycle_state: The lifecycle_state of this User.
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
        Gets the inactive_status of this User.
        Returned only if the user's `lifecycleState` is INACTIVE. A 16-bit value showing the reason why the user\nis inactive:\n\n- bit 0: SUSPENDED (reserved for future use)\n- bit 1: DISABLED (reserved for future use)\n- bit 2: BLOCKED (the user has exceeded the maximum number of failed login attempts for the Console)\n

        :return: The inactive_status of this User.
        :rtype: int
        """
        return self._inactive_status

    @inactive_status.setter
    def inactive_status(self, inactive_status):
        """
        Sets the inactive_status of this User.
        Returned only if the user's `lifecycleState` is INACTIVE. A 16-bit value showing the reason why the user\nis inactive:\n\n- bit 0: SUSPENDED (reserved for future use)\n- bit 1: DISABLED (reserved for future use)\n- bit 2: BLOCKED (the user has exceeded the maximum number of failed login attempts for the Console)\n

        :param inactive_status: The inactive_status of this User.
        :type: int
        """
        self._inactive_status = inactive_status


    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

