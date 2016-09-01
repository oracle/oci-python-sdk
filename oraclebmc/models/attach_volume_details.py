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

class AttachVolumeDetails(object):

    def __init__(self):

        self.swagger_types = {
            'display_name': 'str',
            'instance_id': 'str',
            'type': 'str',
            'volume_id': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'instance_id': 'instanceId',
            'type': 'type',
            'volume_id': 'volumeId'
        }

        self._display_name = None
        self._instance_id = None
        self._type = None
        self._volume_id = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'iscsi':
               return 'AttachIScsiVolumeDetails'

        raise ValueError('Could not resolve subtype type based on the object dictionary.')

    @property
    def display_name(self):
        """
        Gets the display_name of this AttachVolumeDetails.
        A user-friendly name. Does not have to be unique, and it's not changeable.\n

        :return: The display_name of this AttachVolumeDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AttachVolumeDetails.
        A user-friendly name. Does not have to be unique, and it's not changeable.\n

        :param display_name: The display_name of this AttachVolumeDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def instance_id(self):
        """
        Gets the instance_id of this AttachVolumeDetails.
        The OCID of the instance.

        :return: The instance_id of this AttachVolumeDetails.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this AttachVolumeDetails.
        The OCID of the instance.

        :param instance_id: The instance_id of this AttachVolumeDetails.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def type(self):
        """
        Gets the type of this AttachVolumeDetails.
        The type of volume. The only supported value is \"iscsi\".

        :return: The type of this AttachVolumeDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AttachVolumeDetails.
        The type of volume. The only supported value is \"iscsi\".

        :param type: The type of this AttachVolumeDetails.
        :type: str
        """
        self._type = type

    @property
    def volume_id(self):
        """
        Gets the volume_id of this AttachVolumeDetails.
        The OCID of the volume.

        :return: The volume_id of this AttachVolumeDetails.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """
        Sets the volume_id of this AttachVolumeDetails.
        The OCID of the volume.

        :param volume_id: The volume_id of this AttachVolumeDetails.
        :type: str
        """
        self._volume_id = volume_id

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

