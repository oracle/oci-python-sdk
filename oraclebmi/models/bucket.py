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

class Bucket(object):

    def __init__(self):
        """
        Bucket - a model defined in Swagger
        """

        self.swagger_types = {
            'name': 'str',
            'metadata': 'dict(str, str)',
            'time_created': 'datetime',
            'time_modified': 'datetime',
            'etag': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'metadata': 'metadata',
            'time_created': 'timeCreated',
            'time_modified': 'timeModified',
            'etag': 'etag'
        }

        self._name = None
        self._metadata = None
        self._time_created = None
        self._time_modified = None
        self._etag = None


    @property
    def name(self):
        """
        Gets the name of this Bucket.
        The name of the bucket.

        :return: The name of this Bucket.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Bucket.
        The name of the bucket.

        :param name: The name of this Bucket.
        :type: str
        """
        self._name = name

    @property
    def metadata(self):
        """
        Gets the metadata of this Bucket.
        Arbitrary string keys and values for the user-defined metadata.

        :return: The metadata of this Bucket.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this Bucket.
        Arbitrary string keys and values for the user-defined metadata.

        :param metadata: The metadata of this Bucket.
        :type: dict(str, str)
        """
        self._metadata = metadata

    @property
    def time_created(self):
        """
        Gets the time_created of this Bucket.
        The date and time at which the bucket was created.

        :return: The time_created of this Bucket.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Bucket.
        The date and time at which the bucket was created.

        :param time_created: The time_created of this Bucket.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_modified(self):
        """
        Gets the time_modified of this Bucket.
        The date and time at which the bucket was last modified.

        :return: The time_modified of this Bucket.
        :rtype: datetime
        """
        return self._time_modified

    @time_modified.setter
    def time_modified(self, time_modified):
        """
        Sets the time_modified of this Bucket.
        The date and time at which the bucket was last modified.

        :param time_modified: The time_modified of this Bucket.
        :type: datetime
        """
        self._time_modified = time_modified

    @property
    def etag(self):
        """
        Gets the etag of this Bucket.
        The entity tag for the bucket.

        :return: The etag of this Bucket.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this Bucket.
        The entity tag for the bucket.

        :param etag: The etag of this Bucket.
        :type: str
        """
        self._etag = etag

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

