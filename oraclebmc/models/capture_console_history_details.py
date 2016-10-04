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


class CaptureConsoleHistoryDetails(object):

    def __init__(self):

        self.swagger_types = {
            'instance_id': 'str'
        }

        self.attribute_map = {
            'instance_id': 'instanceId'
        }

        self._instance_id = None


    @property
    def instance_id(self):
        """
        Gets the instance_id of this CaptureConsoleHistoryDetails.
        The OCID of the instance to get the console history from.

        :return: The instance_id of this CaptureConsoleHistoryDetails.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this CaptureConsoleHistoryDetails.
        The OCID of the instance to get the console history from.

        :param instance_id: The instance_id of this CaptureConsoleHistoryDetails.
        :type: str
        """
        self._instance_id = instance_id


    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

