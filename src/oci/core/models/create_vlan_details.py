# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateVlanDetails(object):
    """
    CreateVlanDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateVlanDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this CreateVlanDetails.
        :type availability_domain: str

        :param cidr_block:
            The value to assign to the cidr_block property of this CreateVlanDetails.
        :type cidr_block: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateVlanDetails.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateVlanDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CreateVlanDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateVlanDetails.
        :type freeform_tags: dict(str, str)

        :param nsg_ids:
            The value to assign to the nsg_ids property of this CreateVlanDetails.
        :type nsg_ids: list[str]

        :param route_table_id:
            The value to assign to the route_table_id property of this CreateVlanDetails.
        :type route_table_id: str

        :param vcn_id:
            The value to assign to the vcn_id property of this CreateVlanDetails.
        :type vcn_id: str

        :param vlan_tag:
            The value to assign to the vlan_tag property of this CreateVlanDetails.
        :type vlan_tag: int

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'cidr_block': 'str',
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'nsg_ids': 'list[str]',
            'route_table_id': 'str',
            'vcn_id': 'str',
            'vlan_tag': 'int'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'cidr_block': 'cidrBlock',
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'nsg_ids': 'nsgIds',
            'route_table_id': 'routeTableId',
            'vcn_id': 'vcnId',
            'vlan_tag': 'vlanTag'
        }

        self._availability_domain = None
        self._cidr_block = None
        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._nsg_ids = None
        self._route_table_id = None
        self._vcn_id = None
        self._vlan_tag = None

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this CreateVlanDetails.
        The availability domain of the VLAN.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this CreateVlanDetails.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this CreateVlanDetails.
        The availability domain of the VLAN.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this CreateVlanDetails.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def cidr_block(self):
        """
        **[Required]** Gets the cidr_block of this CreateVlanDetails.
        The range of IPv4 addresses that will be used for layer 3 communication with
        hosts outside the VLAN. The CIDR must maintain the following rules -

        a. The CIDR block is valid and correctly formatted.
        b. The new range is within one of the parent VCN ranges.

        Example: `192.0.2.0/24`


        :return: The cidr_block of this CreateVlanDetails.
        :rtype: str
        """
        return self._cidr_block

    @cidr_block.setter
    def cidr_block(self, cidr_block):
        """
        Sets the cidr_block of this CreateVlanDetails.
        The range of IPv4 addresses that will be used for layer 3 communication with
        hosts outside the VLAN. The CIDR must maintain the following rules -

        a. The CIDR block is valid and correctly formatted.
        b. The new range is within one of the parent VCN ranges.

        Example: `192.0.2.0/24`


        :param cidr_block: The cidr_block of this CreateVlanDetails.
        :type: str
        """
        self._cidr_block = cidr_block

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateVlanDetails.
        The OCID of the compartment to contain the VLAN.


        :return: The compartment_id of this CreateVlanDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateVlanDetails.
        The OCID of the compartment to contain the VLAN.


        :param compartment_id: The compartment_id of this CreateVlanDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateVlanDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateVlanDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateVlanDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateVlanDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateVlanDetails.
        A descriptive name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this CreateVlanDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateVlanDetails.
        A descriptive name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreateVlanDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateVlanDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateVlanDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateVlanDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateVlanDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this CreateVlanDetails.
        A list of the OCIDs of the network security groups (NSGs) to add all VNICs in the VLAN to. For more
        information about NSGs, see
        :class:`NetworkSecurityGroup`.


        :return: The nsg_ids of this CreateVlanDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this CreateVlanDetails.
        A list of the OCIDs of the network security groups (NSGs) to add all VNICs in the VLAN to. For more
        information about NSGs, see
        :class:`NetworkSecurityGroup`.


        :param nsg_ids: The nsg_ids of this CreateVlanDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def route_table_id(self):
        """
        Gets the route_table_id of this CreateVlanDetails.
        The OCID of the route table the VLAN will use. If you don't provide a value,
        the VLAN uses the VCN's default route table.


        :return: The route_table_id of this CreateVlanDetails.
        :rtype: str
        """
        return self._route_table_id

    @route_table_id.setter
    def route_table_id(self, route_table_id):
        """
        Sets the route_table_id of this CreateVlanDetails.
        The OCID of the route table the VLAN will use. If you don't provide a value,
        the VLAN uses the VCN's default route table.


        :param route_table_id: The route_table_id of this CreateVlanDetails.
        :type: str
        """
        self._route_table_id = route_table_id

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this CreateVlanDetails.
        The OCID of the VCN to contain the VLAN.


        :return: The vcn_id of this CreateVlanDetails.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this CreateVlanDetails.
        The OCID of the VCN to contain the VLAN.


        :param vcn_id: The vcn_id of this CreateVlanDetails.
        :type: str
        """
        self._vcn_id = vcn_id

    @property
    def vlan_tag(self):
        """
        Gets the vlan_tag of this CreateVlanDetails.
        The IEEE 802.1Q VLAN tag for this VLAN. The value must be unique across all
        VLANs in the VCN. If you don't provide a value, Oracle assigns one.
        You cannot change the value later. VLAN tag 0 is reserved for use by Oracle.


        :return: The vlan_tag of this CreateVlanDetails.
        :rtype: int
        """
        return self._vlan_tag

    @vlan_tag.setter
    def vlan_tag(self, vlan_tag):
        """
        Sets the vlan_tag of this CreateVlanDetails.
        The IEEE 802.1Q VLAN tag for this VLAN. The value must be unique across all
        VLANs in the VCN. If you don't provide a value, Oracle assigns one.
        You cannot change the value later. VLAN tag 0 is reserved for use by Oracle.


        :param vlan_tag: The vlan_tag of this CreateVlanDetails.
        :type: int
        """
        self._vlan_tag = vlan_tag

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
