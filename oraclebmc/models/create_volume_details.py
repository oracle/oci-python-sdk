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

class CreateVolumeDetails(object):

    def __init__(self):

        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'volume_backup_id': 'str'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'volume_backup_id': 'volumeBackupId'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._display_name = None
        self._volume_backup_id = None


    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this CreateVolumeDetails.
        The Availability Domain of the volume.

        :return: The availability_domain of this CreateVolumeDetails.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this CreateVolumeDetails.
        The Availability Domain of the volume.

        :param availability_domain: The availability_domain of this CreateVolumeDetails.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CreateVolumeDetails.
        The OCID of the compartment that contains the volume.

        :return: The compartment_id of this CreateVolumeDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateVolumeDetails.
        The OCID of the compartment that contains the volume.

        :param compartment_id: The compartment_id of this CreateVolumeDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateVolumeDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.\n

        :return: The display_name of this CreateVolumeDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateVolumeDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.\n

        :param display_name: The display_name of this CreateVolumeDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def volume_backup_id(self):
        """
        Gets the volume_backup_id of this CreateVolumeDetails.
        The ID of the volume backup from which the data should be restored on the newly created volume.\n

        :return: The volume_backup_id of this CreateVolumeDetails.
        :rtype: str
        """
        return self._volume_backup_id

    @volume_backup_id.setter
    def volume_backup_id(self, volume_backup_id):
        """
        Sets the volume_backup_id of this CreateVolumeDetails.
        The ID of the volume backup from which the data should be restored on the newly created volume.\n

        :param volume_backup_id: The volume_backup_id of this CreateVolumeDetails.
        :type: str
        """
        self._volume_backup_id = volume_backup_id

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

