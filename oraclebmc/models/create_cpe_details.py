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


class CreateCpeDetails(object):

    def __init__(self):

        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'ip_address': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'ip_address': 'ipAddress'
        }

        self._compartment_id = None
        self._display_name = None
        self._ip_address = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CreateCpeDetails.
        The OCID of the compartment to contain the CPE.

        :return: The compartment_id of this CreateCpeDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateCpeDetails.
        The OCID of the compartment to contain the CPE.

        :param compartment_id: The compartment_id of this CreateCpeDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateCpeDetails.
        A user-friendly name. Does not have to be unique, and it's not changeable.\n

        :return: The display_name of this CreateCpeDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateCpeDetails.
        A user-friendly name. Does not have to be unique, and it's not changeable.\n

        :param display_name: The display_name of this CreateCpeDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def ip_address(self):
        """
        Gets the ip_address of this CreateCpeDetails.
        The public IP address of the on-premise router.

        :return: The ip_address of this CreateCpeDetails.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this CreateCpeDetails.
        The public IP address of the on-premise router.

        :param ip_address: The ip_address of this CreateCpeDetails.
        :type: str
        """
        self._ip_address = ip_address

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
