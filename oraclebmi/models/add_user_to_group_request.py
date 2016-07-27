# coding: utf-8

"""
This is a modified version of the same template from swagger-codegen.
The original can be found at https://github.com/swagger-api/swagger-codegen.
The original license is below.

    Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems

class AddUserToGroupRequest(object):

    def __init__(self):
        """
        AddUserToGroupRequest - a model defined in Swagger
        """
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
        Gets the user_id of this AddUserToGroupRequest.
        The OCID of the user.

        :return: The user_id of this AddUserToGroupRequest.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this AddUserToGroupRequest.
        The OCID of the user.

        :param user_id: The user_id of this AddUserToGroupRequest.
        :type: str
        """
        self._user_id = user_id

    @property
    def group_id(self):
        """
        Gets the group_id of this AddUserToGroupRequest.
        The OCID of the group.

        :return: The group_id of this AddUserToGroupRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this AddUserToGroupRequest.
        The OCID of the group.

        :param group_id: The group_id of this AddUserToGroupRequest.
        :type: str
        """
        self._group_id = group_id

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if objects are not equal
        """
        return not self == other

