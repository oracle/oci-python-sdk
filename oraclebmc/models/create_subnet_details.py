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


class CreateSubnetDetails(object):

    def __init__(self):

        self.swagger_types = {
            'availability_domain': 'str',
            'cidr_block': 'str',
            'compartment_id': 'str',
            'dhcp_options_id': 'str',
            'display_name': 'str',
            'route_table_id': 'str',
            'security_list_ids': 'list[str]',
            'vcn_id': 'str'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'cidr_block': 'cidrBlock',
            'compartment_id': 'compartmentId',
            'dhcp_options_id': 'dhcpOptionsId',
            'display_name': 'displayName',
            'route_table_id': 'routeTableId',
            'security_list_ids': 'securityListIds',
            'vcn_id': 'vcnId'
        }

        self._availability_domain = None
        self._cidr_block = None
        self._compartment_id = None
        self._dhcp_options_id = None
        self._display_name = None
        self._route_table_id = None
        self._security_list_ids = None
        self._vcn_id = None


    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this CreateSubnetDetails.
        The Availability Domain to contain the subnet.

        :return: The availability_domain of this CreateSubnetDetails.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this CreateSubnetDetails.
        The Availability Domain to contain the subnet.

        :param availability_domain: The availability_domain of this CreateSubnetDetails.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def cidr_block(self):
        """
        Gets the cidr_block of this CreateSubnetDetails.
        The CIDR IP address range of the subnet.

        :return: The cidr_block of this CreateSubnetDetails.
        :rtype: str
        """
        return self._cidr_block

    @cidr_block.setter
    def cidr_block(self, cidr_block):
        """
        Sets the cidr_block of this CreateSubnetDetails.
        The CIDR IP address range of the subnet.

        :param cidr_block: The cidr_block of this CreateSubnetDetails.
        :type: str
        """
        self._cidr_block = cidr_block

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CreateSubnetDetails.
        The OCID of the compartment to contain the subnet.

        :return: The compartment_id of this CreateSubnetDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateSubnetDetails.
        The OCID of the compartment to contain the subnet.

        :param compartment_id: The compartment_id of this CreateSubnetDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def dhcp_options_id(self):
        """
        Gets the dhcp_options_id of this CreateSubnetDetails.
        The OCID of the set of DHCP options the subnet will use. If you don't\nprovide a value, the subnet will use the VCN's default set of DHCP options.\n

        :return: The dhcp_options_id of this CreateSubnetDetails.
        :rtype: str
        """
        return self._dhcp_options_id

    @dhcp_options_id.setter
    def dhcp_options_id(self, dhcp_options_id):
        """
        Sets the dhcp_options_id of this CreateSubnetDetails.
        The OCID of the set of DHCP options the subnet will use. If you don't\nprovide a value, the subnet will use the VCN's default set of DHCP options.\n

        :param dhcp_options_id: The dhcp_options_id of this CreateSubnetDetails.
        :type: str
        """
        self._dhcp_options_id = dhcp_options_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateSubnetDetails.
        A user-friendly name. Does not have to be unique, and it's not changeable.\n

        :return: The display_name of this CreateSubnetDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateSubnetDetails.
        A user-friendly name. Does not have to be unique, and it's not changeable.\n

        :param display_name: The display_name of this CreateSubnetDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def route_table_id(self):
        """
        Gets the route_table_id of this CreateSubnetDetails.
        The OCID of the route table the subnet will use. If you don't provide a value,\nthe subnet will use the VCN's default route table.\n

        :return: The route_table_id of this CreateSubnetDetails.
        :rtype: str
        """
        return self._route_table_id

    @route_table_id.setter
    def route_table_id(self, route_table_id):
        """
        Sets the route_table_id of this CreateSubnetDetails.
        The OCID of the route table the subnet will use. If you don't provide a value,\nthe subnet will use the VCN's default route table.\n

        :param route_table_id: The route_table_id of this CreateSubnetDetails.
        :type: str
        """
        self._route_table_id = route_table_id

    @property
    def security_list_ids(self):
        """
        Gets the security_list_ids of this CreateSubnetDetails.
        OCIDs for the security lists to associate with the subnet. If you don't\nprovide a value, the VCN's default security list will be associated with\nthe subnet. Remember that security lists are associated at the subnet\nlevel, but the rules are applied to the individual VNICs in the subnet.\n

        :return: The security_list_ids of this CreateSubnetDetails.
        :rtype: list[str]
        """
        return self._security_list_ids

    @security_list_ids.setter
    def security_list_ids(self, security_list_ids):
        """
        Sets the security_list_ids of this CreateSubnetDetails.
        OCIDs for the security lists to associate with the subnet. If you don't\nprovide a value, the VCN's default security list will be associated with\nthe subnet. Remember that security lists are associated at the subnet\nlevel, but the rules are applied to the individual VNICs in the subnet.\n

        :param security_list_ids: The security_list_ids of this CreateSubnetDetails.
        :type: list[str]
        """
        self._security_list_ids = security_list_ids

    @property
    def vcn_id(self):
        """
        Gets the vcn_id of this CreateSubnetDetails.
        The OCID of the VCN to contain the subnet.

        :return: The vcn_id of this CreateSubnetDetails.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this CreateSubnetDetails.
        The OCID of the VCN to contain the subnet.

        :param vcn_id: The vcn_id of this CreateSubnetDetails.
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

