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


class CreateDhcpDetails(object):

    def __init__(self):

        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'options': 'list[DhcpOption]',
            'vcn_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'options': 'options',
            'vcn_id': 'vcnId'
        }

        self._compartment_id = None
        self._display_name = None
        self._options = None
        self._vcn_id = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CreateDhcpDetails.
        The OCID of the compartment to contain the set of DHCP options.

        :return: The compartment_id of this CreateDhcpDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateDhcpDetails.
        The OCID of the compartment to contain the set of DHCP options.

        :param compartment_id: The compartment_id of this CreateDhcpDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateDhcpDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.

        :return: The display_name of this CreateDhcpDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDhcpDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.

        :param display_name: The display_name of this CreateDhcpDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def options(self):
        """
        Gets the options of this CreateDhcpDetails.
        A set of DHCP options.

        :return: The options of this CreateDhcpDetails.
        :rtype: list[DhcpOption]
        """
        return self._options

    @options.setter
    def options(self, options):
        """
        Sets the options of this CreateDhcpDetails.
        A set of DHCP options.

        :param options: The options of this CreateDhcpDetails.
        :type: list[DhcpOption]
        """
        self._options = options

    @property
    def vcn_id(self):
        """
        Gets the vcn_id of this CreateDhcpDetails.
        The OCID of the VCN the set of DHCP options belongs to.

        :return: The vcn_id of this CreateDhcpDetails.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this CreateDhcpDetails.
        The OCID of the VCN the set of DHCP options belongs to.

        :param vcn_id: The vcn_id of this CreateDhcpDetails.
        :type: str
        """
        self._vcn_id = vcn_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
