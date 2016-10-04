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


class UserGroupMembership(object):

    def __init__(self):

        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'group_id': 'str',
            'user_id': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'inactive_status': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'group_id': 'groupId',
            'user_id': 'userId',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'inactive_status': 'inactiveStatus'
        }

        self._id = None
        self._compartment_id = None
        self._group_id = None
        self._user_id = None
        self._time_created = None
        self._lifecycle_state = None
        self._inactive_status = None


    @property
    def id(self):
        """
        Gets the id of this UserGroupMembership.
        The membership's Oracle ID (OCID).

        :return: The id of this UserGroupMembership.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UserGroupMembership.
        The membership's Oracle ID (OCID).

        :param id: The id of this UserGroupMembership.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this UserGroupMembership.
        The OCID of the tenancy containing the user, group, and membership object.

        :return: The compartment_id of this UserGroupMembership.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this UserGroupMembership.
        The OCID of the tenancy containing the user, group, and membership object.

        :param compartment_id: The compartment_id of this UserGroupMembership.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def group_id(self):
        """
        Gets the group_id of this UserGroupMembership.
        The OCID of the group.

        :return: The group_id of this UserGroupMembership.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this UserGroupMembership.
        The OCID of the group.

        :param group_id: The group_id of this UserGroupMembership.
        :type: str
        """
        self._group_id = group_id

    @property
    def user_id(self):
        """
        Gets the user_id of this UserGroupMembership.
        The OCID of the user.

        :return: The user_id of this UserGroupMembership.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this UserGroupMembership.
        The OCID of the user.

        :param user_id: The user_id of this UserGroupMembership.
        :type: str
        """
        self._user_id = user_id

    @property
    def time_created(self):
        """
        Gets the time_created of this UserGroupMembership.
        Date and time the membership was created.

        :return: The time_created of this UserGroupMembership.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this UserGroupMembership.
        Date and time the membership was created.

        :param time_created: The time_created of this UserGroupMembership.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this UserGroupMembership.
        The membership's current state.  After creating a membership object, make sure its `lifecycleState` changes\nfrom CREATING to ACTIVE before using it.\n

        :return: The lifecycle_state of this UserGroupMembership.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this UserGroupMembership.
        The membership's current state.  After creating a membership object, make sure its `lifecycleState` changes\nfrom CREATING to ACTIVE before using it.\n

        :param lifecycle_state: The lifecycle_state of this UserGroupMembership.
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
        Gets the inactive_status of this UserGroupMembership.
        The detailed status of INACTIVE lifecycleState.

        :return: The inactive_status of this UserGroupMembership.
        :rtype: int
        """
        return self._inactive_status

    @inactive_status.setter
    def inactive_status(self, inactive_status):
        """
        Sets the inactive_status of this UserGroupMembership.
        The detailed status of INACTIVE lifecycleState.

        :param inactive_status: The inactive_status of this UserGroupMembership.
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

