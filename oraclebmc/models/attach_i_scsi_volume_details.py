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

from .attach_volume_details import AttachVolumeDetails
from ..util import formatted_flat_dict


class AttachIScsiVolumeDetails(AttachVolumeDetails):

    def __init__(self):

        self.swagger_types = {
            'display_name': 'str',
            'instance_id': 'str',
            'type': 'str',
            'volume_id': 'str',
            'use_chap': 'bool'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'instance_id': 'instanceId',
            'type': 'type',
            'volume_id': 'volumeId',
            'use_chap': 'useChap'
        }

        self._display_name = None
        self._instance_id = None
        self._type = None
        self._volume_id = None
        self._use_chap = None

        self._type = 'iscsi'

    @property
    def use_chap(self):
        """
        Gets the use_chap of this AttachIScsiVolumeDetails.
        Whether to use CHAP authentication for the volume attachment. Defaults to false.

        :return: The use_chap of this AttachIScsiVolumeDetails.
        :rtype: bool
        """
        return self._use_chap

    @use_chap.setter
    def use_chap(self, use_chap):
        """
        Sets the use_chap of this AttachIScsiVolumeDetails.
        Whether to use CHAP authentication for the volume attachment. Defaults to false.

        :param use_chap: The use_chap of this AttachIScsiVolumeDetails.
        :type: bool
        """
        self._use_chap = use_chap

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

