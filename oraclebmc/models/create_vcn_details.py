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


class CreateVcnDetails(object):

    def __init__(self):

        self.swagger_types = {
            'cidr_block': 'str',
            'compartment_id': 'str',
            'display_name': 'str'
        }

        self.attribute_map = {
            'cidr_block': 'cidrBlock',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName'
        }

        self._cidr_block = None
        self._compartment_id = None
        self._display_name = None

    @property
    def cidr_block(self):
        """
        Gets the cidr_block of this CreateVcnDetails.
        The CIDR IP address block of the VCN.

        :return: The cidr_block of this CreateVcnDetails.
        :rtype: str
        """
        return self._cidr_block

    @cidr_block.setter
    def cidr_block(self, cidr_block):
        """
        Sets the cidr_block of this CreateVcnDetails.
        The CIDR IP address block of the VCN.

        :param cidr_block: The cidr_block of this CreateVcnDetails.
        :type: str
        """
        self._cidr_block = cidr_block

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CreateVcnDetails.
        The OCID of the compartment to contain the VCN.

        :return: The compartment_id of this CreateVcnDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateVcnDetails.
        The OCID of the compartment to contain the VCN.

        :param compartment_id: The compartment_id of this CreateVcnDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateVcnDetails.
        A user-friendly name. Does not have to be unique, and it's not changeable.\n

        :return: The display_name of this CreateVcnDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateVcnDetails.
        A user-friendly name. Does not have to be unique, and it's not changeable.\n

        :param display_name: The display_name of this CreateVcnDetails.
        :type: str
        """
        self._display_name = display_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
