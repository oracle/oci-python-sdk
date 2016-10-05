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


class CreateImageDetails(object):

    def __init__(self):

        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'instance_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'instance_id': 'instanceId'
        }

        self._compartment_id = None
        self._display_name = None
        self._instance_id = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CreateImageDetails.
        The OCID of the compartment containing the instance you want to use as the basis for the image.

        :return: The compartment_id of this CreateImageDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateImageDetails.
        The OCID of the compartment containing the instance you want to use as the basis for the image.

        :param compartment_id: The compartment_id of this CreateImageDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateImageDetails.
        A user-friendly name for the image. It does not have to be unique, and it's changeable. You cannot use an\nOracle-provided image name as a custom image name.\n\nExample: `My Oracle Linux image`\n

        :return: The display_name of this CreateImageDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateImageDetails.
        A user-friendly name for the image. It does not have to be unique, and it's changeable. You cannot use an\nOracle-provided image name as a custom image name.\n\nExample: `My Oracle Linux image`\n

        :param display_name: The display_name of this CreateImageDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def instance_id(self):
        """
        Gets the instance_id of this CreateImageDetails.
        The OCID of the instance you want to use as the basis for the image.

        :return: The instance_id of this CreateImageDetails.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this CreateImageDetails.
        The OCID of the instance you want to use as the basis for the image.

        :param instance_id: The instance_id of this CreateImageDetails.
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
