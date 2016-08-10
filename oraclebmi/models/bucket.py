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

class Bucket(object):

    def __init__(self):

        self.swagger_types = {
            'namespace': 'str',
            'name': 'str',
            'compartment': 'str',
            'metadata': 'dict(str, str)',
            'created_by': 'str',
            'created_on': 'datetime',
            'etag': 'str'
        }

        self.attribute_map = {
            'namespace': 'namespace',
            'name': 'name',
            'compartment': 'compartment',
            'metadata': 'metadata',
            'created_by': 'createdBy',
            'created_on': 'createdOn',
            'etag': 'etag'
        }

        self._namespace = None
        self._name = None
        self._compartment = None
        self._metadata = None
        self._created_by = None
        self._created_on = None
        self._etag = None


    @property
    def namespace(self):
        """
        Gets the namespace of this Bucket.
        the namespace in which the bucket lives.

        :return: The namespace of this Bucket.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this Bucket.
        the namespace in which the bucket lives.

        :param namespace: The namespace of this Bucket.
        :type: str
        """
        self._namespace = namespace

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
    def compartment(self):
        """
        Gets the compartment of this Bucket.
        the compartment in which the bucket is authorized.

        :return: The compartment of this Bucket.
        :rtype: str
        """
        return self._compartment

    @compartment.setter
    def compartment(self, compartment):
        """
        Sets the compartment of this Bucket.
        the compartment in which the bucket is authorized.

        :param compartment: The compartment of this Bucket.
        :type: str
        """
        self._compartment = compartment

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
    def created_by(self):
        """
        Gets the created_by of this Bucket.
        the OCID of the user who created the bucket.

        :return: The created_by of this Bucket.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this Bucket.
        the OCID of the user who created the bucket.

        :param created_by: The created_by of this Bucket.
        :type: str
        """
        self._created_by = created_by

    @property
    def created_on(self):
        """
        Gets the created_on of this Bucket.
        The date and time at which the bucket was created.

        :return: The created_on of this Bucket.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """
        Sets the created_on of this Bucket.
        The date and time at which the bucket was created.

        :param created_on: The created_on of this Bucket.
        :type: datetime
        """
        self._created_on = created_on

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

