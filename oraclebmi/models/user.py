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

class User(object):

    def __init__(self):
        """
        User - a model defined in Swagger
        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'name': 'str',
            'description': 'str',
            'time_created': 'datetime',
            'time_modified': 'datetime',
            'state': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'name': 'name',
            'description': 'description',
            'time_created': 'timeCreated',
            'time_modified': 'timeModified',
            'state': 'state'
        }

        self._id = None
        self._compartment_id = None
        self._name = None
        self._description = None
        self._time_created = None
        self._time_modified = None
        self._state = None

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
    def time_modified(self):
        """
        Gets the time_modified of this User.
        Date and time the user was last modified (same as `TimeCreated` if not yet modified).

        :return: The time_modified of this User.
        :rtype: datetime
        """
        return self._time_modified

    @time_modified.setter
    def time_modified(self, time_modified):
        """
        Sets the time_modified of this User.
        Date and time the user was last modified (same as `TimeCreated` if not yet modified).

        :param time_modified: The time_modified of this User.
        :type: datetime
        """
        self._time_modified = time_modified

    @property
    def state(self):
        """
        Gets the state of this User.
        The user's state. After creating a user, make sure its state changes from CREATING to CREATED\nbefore using it.\n

        :return: The state of this User.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this User.
        The user's state. After creating a user, make sure its state changes from CREATING to CREATED\nbefore using it.\n

        :param state: The state of this User.
        :type: str
        """
        self._state = state

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

