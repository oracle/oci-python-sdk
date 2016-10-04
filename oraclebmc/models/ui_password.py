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


class UIPassword(object):

    def __init__(self):

        self.swagger_types = {
            'password': 'str',
            'user_id': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'inactive_status': 'int'
        }

        self.attribute_map = {
            'password': 'password',
            'user_id': 'userId',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'inactive_status': 'inactiveStatus'
        }

        self._password = None
        self._user_id = None
        self._time_created = None
        self._lifecycle_state = None
        self._inactive_status = None


    @property
    def password(self):
        """
        Gets the password of this UIPassword.
        The user's password for the Console.

        :return: The password of this UIPassword.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this UIPassword.
        The user's password for the Console.

        :param password: The password of this UIPassword.
        :type: str
        """
        self._password = password

    @property
    def user_id(self):
        """
        Gets the user_id of this UIPassword.
        The OCID of the user.

        :return: The user_id of this UIPassword.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this UIPassword.
        The OCID of the user.

        :param user_id: The user_id of this UIPassword.
        :type: str
        """
        self._user_id = user_id

    @property
    def time_created(self):
        """
        Gets the time_created of this UIPassword.
        Date and time the password was created.

        :return: The time_created of this UIPassword.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this UIPassword.
        Date and time the password was created.

        :param time_created: The time_created of this UIPassword.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this UIPassword.
        The password's current state. After creating a password, make sure its `lifecycleState` changes from\nCREATING to ACTIVE before using it.\n

        :return: The lifecycle_state of this UIPassword.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this UIPassword.
        The password's current state. After creating a password, make sure its `lifecycleState` changes from\nCREATING to ACTIVE before using it.\n

        :param lifecycle_state: The lifecycle_state of this UIPassword.
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
        Gets the inactive_status of this UIPassword.
        The detailed status of INACTIVE lifecycleState.

        :return: The inactive_status of this UIPassword.
        :rtype: int
        """
        return self._inactive_status

    @inactive_status.setter
    def inactive_status(self, inactive_status):
        """
        Sets the inactive_status of this UIPassword.
        The detailed status of INACTIVE lifecycleState.

        :param inactive_status: The inactive_status of this UIPassword.
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

