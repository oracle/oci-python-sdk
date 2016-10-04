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


class AddUserToGroupDetails(object):

    def __init__(self):

        self.swagger_types = {
            'user_id': 'str',
            'group_id': 'str'
        }

        self.attribute_map = {
            'user_id': 'userId',
            'group_id': 'groupId'
        }

        self._user_id = None
        self._group_id = None


    @property
    def user_id(self):
        """
        Gets the user_id of this AddUserToGroupDetails.
        The OCID of the user.

        :return: The user_id of this AddUserToGroupDetails.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this AddUserToGroupDetails.
        The OCID of the user.

        :param user_id: The user_id of this AddUserToGroupDetails.
        :type: str
        """
        self._user_id = user_id

    @property
    def group_id(self):
        """
        Gets the group_id of this AddUserToGroupDetails.
        The OCID of the group.

        :return: The group_id of this AddUserToGroupDetails.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this AddUserToGroupDetails.
        The OCID of the group.

        :param group_id: The group_id of this AddUserToGroupDetails.
        :type: str
        """
        self._group_id = group_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

