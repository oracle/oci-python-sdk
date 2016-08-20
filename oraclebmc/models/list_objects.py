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

class ListObjects(object):

    def __init__(self):

        self.swagger_types = {
            'objects': 'list[ObjectSummary]',
            'prefixes': 'list[str]',
            'next_start_with': 'str'
        }

        self.attribute_map = {
            'objects': 'objects',
            'prefixes': 'prefixes',
            'next_start_with': 'nextStartWith'
        }

        self._objects = None
        self._prefixes = None
        self._next_start_with = None


    @property
    def objects(self):
        """
        Gets the objects of this ListObjects.


        :return: The objects of this ListObjects.
        :rtype: list[ObjectSummary]
        """
        return self._objects

    @objects.setter
    def objects(self, objects):
        """
        Sets the objects of this ListObjects.


        :param objects: The objects of this ListObjects.
        :type: list[ObjectSummary]
        """
        self._objects = objects

    @property
    def prefixes(self):
        """
        Gets the prefixes of this ListObjects.


        :return: The prefixes of this ListObjects.
        :rtype: list[str]
        """
        return self._prefixes

    @prefixes.setter
    def prefixes(self, prefixes):
        """
        Sets the prefixes of this ListObjects.


        :param prefixes: The prefixes of this ListObjects.
        :type: list[str]
        """
        self._prefixes = prefixes

    @property
    def next_start_with(self):
        """
        Gets the next_start_with of this ListObjects.
        The name of the object to be used in startWith parameter to obtain next page of a truncated list objects response.

        :return: The next_start_with of this ListObjects.
        :rtype: str
        """
        return self._next_start_with

    @next_start_with.setter
    def next_start_with(self, next_start_with):
        """
        Sets the next_start_with of this ListObjects.
        The name of the object to be used in startWith parameter to obtain next page of a truncated list objects response.

        :param next_start_with: The next_start_with of this ListObjects.
        :type: str
        """
        self._next_start_with = next_start_with

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

