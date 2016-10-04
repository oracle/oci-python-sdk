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


class ObjectSummary(object):

    def __init__(self):

        self.swagger_types = {
            'name': 'str',
            'size': 'int',
            'md5': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'name': 'name',
            'size': 'size',
            'md5': 'md5',
            'time_created': 'timeCreated'
        }

        self._name = None
        self._size = None
        self._md5 = None
        self._time_created = None


    @property
    def name(self):
        """
        Gets the name of this ObjectSummary.
        The name of the object.

        :return: The name of this ObjectSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ObjectSummary.
        The name of the object.

        :param name: The name of this ObjectSummary.
        :type: str
        """
        self._name = name

    @property
    def size(self):
        """
        Gets the size of this ObjectSummary.
        Size of the object in bytes.

        :return: The size of this ObjectSummary.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this ObjectSummary.
        Size of the object in bytes.

        :param size: The size of this ObjectSummary.
        :type: int
        """
        self._size = size

    @property
    def md5(self):
        """
        Gets the md5 of this ObjectSummary.
        Base64 encoded MD5 hash of the object data.

        :return: The md5 of this ObjectSummary.
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """
        Sets the md5 of this ObjectSummary.
        Base64 encoded MD5 hash of the object data.

        :param md5: The md5 of this ObjectSummary.
        :type: str
        """
        self._md5 = md5

    @property
    def time_created(self):
        """
        Gets the time_created of this ObjectSummary.
        Date and time of object creation.

        :return: The time_created of this ObjectSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ObjectSummary.
        Date and time of object creation.

        :param time_created: The time_created of this ObjectSummary.
        :type: datetime
        """
        self._time_created = time_created


    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

