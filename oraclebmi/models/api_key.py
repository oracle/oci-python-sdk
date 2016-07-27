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

class ApiKey(object):

    def __init__(self):
        """
        ApiKey - a model defined in Swagger
        """
        self.swagger_types = {
            'key_id': 'str',
            'key_value': 'str',
            'fingerprint': 'str',
            'user_id': 'str',
            'time_created': 'datetime',
            'time_modified': 'datetime',
            'state': 'str'
        }

        self.attribute_map = {
            'key_id': 'keyId',
            'key_value': 'keyValue',
            'fingerprint': 'fingerprint',
            'user_id': 'userId',
            'time_created': 'timeCreated',
            'time_modified': 'timeModified',
            'state': 'state'
        }

        self._key_id = None
        self._key_value = None
        self._fingerprint = None
        self._user_id = None
        self._time_created = None
        self._time_modified = None
        self._state = None

    @property
    def key_id(self):
        """
        Gets the key_id of this ApiKey.
        An Oracle-assigned identifier for the key, in this format:\nTENANCY_OCID/USER_OCID/KEY_FINGERPRINT.\n

        :return: The key_id of this ApiKey.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """
        Sets the key_id of this ApiKey.
        An Oracle-assigned identifier for the key, in this format:\nTENANCY_OCID/USER_OCID/KEY_FINGERPRINT.\n

        :param key_id: The key_id of this ApiKey.
        :type: str
        """
        self._key_id = key_id

    @property
    def key_value(self):
        """
        Gets the key_value of this ApiKey.
        The key's value.

        :return: The key_value of this ApiKey.
        :rtype: str
        """
        return self._key_value

    @key_value.setter
    def key_value(self, key_value):
        """
        Sets the key_value of this ApiKey.
        The key's value.

        :param key_value: The key_value of this ApiKey.
        :type: str
        """
        self._key_value = key_value

    @property
    def fingerprint(self):
        """
        Gets the fingerprint of this ApiKey.
        The key's fingerprint (e.g., 12:34:56:78:90:ab:cd:ef:12:34:56:78:90:ab:cd:ef).

        :return: The fingerprint of this ApiKey.
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """
        Sets the fingerprint of this ApiKey.
        The key's fingerprint (e.g., 12:34:56:78:90:ab:cd:ef:12:34:56:78:90:ab:cd:ef).

        :param fingerprint: The fingerprint of this ApiKey.
        :type: str
        """
        self._fingerprint = fingerprint

    @property
    def user_id(self):
        """
        Gets the user_id of this ApiKey.
        The OCID of the user the key belongs to.

        :return: The user_id of this ApiKey.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this ApiKey.
        The OCID of the user the key belongs to.

        :param user_id: The user_id of this ApiKey.
        :type: str
        """
        self._user_id = user_id

    @property
    def time_created(self):
        """
        Gets the time_created of this ApiKey.
        Date and time the `ApiKey` object was created.

        :return: The time_created of this ApiKey.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ApiKey.
        Date and time the `ApiKey` object was created.

        :param time_created: The time_created of this ApiKey.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_modified(self):
        """
        Gets the time_modified of this ApiKey.
        Date and time the `ApiKey` object was last modified (same as `TimeCreated` if not yet modified).

        :return: The time_modified of this ApiKey.
        :rtype: datetime
        """
        return self._time_modified

    @time_modified.setter
    def time_modified(self, time_modified):
        """
        Sets the time_modified of this ApiKey.
        Date and time the `ApiKey` object was last modified (same as `TimeCreated` if not yet modified).

        :param time_modified: The time_modified of this ApiKey.
        :type: datetime
        """
        self._time_modified = time_modified

    @property
    def state(self):
        """
        Gets the state of this ApiKey.
        The API key's state. After creating an `ApiKey` object, make sure its state changes from CREATING\nto CREATED before using it.\n

        :return: The state of this ApiKey.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this ApiKey.
        The API key's state. After creating an `ApiKey` object, make sure its state changes from CREATING\nto CREATED before using it.\n

        :param state: The state of this ApiKey.
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

