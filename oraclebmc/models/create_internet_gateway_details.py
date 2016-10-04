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


class CreateInternetGatewayDetails(object):

    def __init__(self):

        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'is_enabled': 'bool',
            'vcn_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'is_enabled': 'isEnabled',
            'vcn_id': 'vcnId'
        }

        self._compartment_id = None
        self._display_name = None
        self._is_enabled = None
        self._vcn_id = None


    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CreateInternetGatewayDetails.
        The OCID of the compartment to contain the Internet Gateway.

        :return: The compartment_id of this CreateInternetGatewayDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateInternetGatewayDetails.
        The OCID of the compartment to contain the Internet Gateway.

        :param compartment_id: The compartment_id of this CreateInternetGatewayDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateInternetGatewayDetails.
        A user-friendly name. Does not have to be unique, and it's not changeable.\n

        :return: The display_name of this CreateInternetGatewayDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateInternetGatewayDetails.
        A user-friendly name. Does not have to be unique, and it's not changeable.\n

        :param display_name: The display_name of this CreateInternetGatewayDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this CreateInternetGatewayDetails.
        Whether the gateway is enabled upon creation.

        :return: The is_enabled of this CreateInternetGatewayDetails.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this CreateInternetGatewayDetails.
        Whether the gateway is enabled upon creation.

        :param is_enabled: The is_enabled of this CreateInternetGatewayDetails.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def vcn_id(self):
        """
        Gets the vcn_id of this CreateInternetGatewayDetails.
        The OCID of the VCN the Internet Gateway is attached to.

        :return: The vcn_id of this CreateInternetGatewayDetails.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this CreateInternetGatewayDetails.
        The OCID of the VCN the Internet Gateway is attached to.

        :param vcn_id: The vcn_id of this CreateInternetGatewayDetails.
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

