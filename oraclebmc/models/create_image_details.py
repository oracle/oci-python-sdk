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

