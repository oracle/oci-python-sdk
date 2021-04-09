# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateSubnetDetails(object):
    """
    UpdateSubnetDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateSubnetDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateSubnetDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param dhcp_options_id:
            The value to assign to the dhcp_options_id property of this UpdateSubnetDetails.
        :type dhcp_options_id: str

        :param display_name:
            The value to assign to the display_name property of this UpdateSubnetDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateSubnetDetails.
        :type freeform_tags: dict(str, str)

        :param route_table_id:
            The value to assign to the route_table_id property of this UpdateSubnetDetails.
        :type route_table_id: str

        :param security_list_ids:
            The value to assign to the security_list_ids property of this UpdateSubnetDetails.
        :type security_list_ids: list[str]

        :param cidr_block:
            The value to assign to the cidr_block property of this UpdateSubnetDetails.
        :type cidr_block: str

        :param ipv6_cidr_block:
            The value to assign to the ipv6_cidr_block property of this UpdateSubnetDetails.
        :type ipv6_cidr_block: str

        """
        self.swagger_types = {
            'defined_tags': 'dict(str, dict(str, object))',
            'dhcp_options_id': 'str',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'route_table_id': 'str',
            'security_list_ids': 'list[str]',
            'cidr_block': 'str',
            'ipv6_cidr_block': 'str'
        }

        self.attribute_map = {
            'defined_tags': 'definedTags',
            'dhcp_options_id': 'dhcpOptionsId',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'route_table_id': 'routeTableId',
            'security_list_ids': 'securityListIds',
            'cidr_block': 'cidrBlock',
            'ipv6_cidr_block': 'ipv6CidrBlock'
        }

        self._defined_tags = None
        self._dhcp_options_id = None
        self._display_name = None
        self._freeform_tags = None
        self._route_table_id = None
        self._security_list_ids = None
        self._cidr_block = None
        self._ipv6_cidr_block = None

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateSubnetDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateSubnetDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateSubnetDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateSubnetDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def dhcp_options_id(self):
        """
        Gets the dhcp_options_id of this UpdateSubnetDetails.
        The OCID of the set of DHCP options the subnet will use.


        :return: The dhcp_options_id of this UpdateSubnetDetails.
        :rtype: str
        """
        return self._dhcp_options_id

    @dhcp_options_id.setter
    def dhcp_options_id(self, dhcp_options_id):
        """
        Sets the dhcp_options_id of this UpdateSubnetDetails.
        The OCID of the set of DHCP options the subnet will use.


        :param dhcp_options_id: The dhcp_options_id of this UpdateSubnetDetails.
        :type: str
        """
        self._dhcp_options_id = dhcp_options_id

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateSubnetDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this UpdateSubnetDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateSubnetDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this UpdateSubnetDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateSubnetDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateSubnetDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateSubnetDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateSubnetDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def route_table_id(self):
        """
        Gets the route_table_id of this UpdateSubnetDetails.
        The OCID of the route table the subnet will use.


        :return: The route_table_id of this UpdateSubnetDetails.
        :rtype: str
        """
        return self._route_table_id

    @route_table_id.setter
    def route_table_id(self, route_table_id):
        """
        Sets the route_table_id of this UpdateSubnetDetails.
        The OCID of the route table the subnet will use.


        :param route_table_id: The route_table_id of this UpdateSubnetDetails.
        :type: str
        """
        self._route_table_id = route_table_id

    @property
    def security_list_ids(self):
        """
        Gets the security_list_ids of this UpdateSubnetDetails.
        The OCIDs of the security list or lists the subnet will use. This
        replaces the entire current set of security lists. Remember that
        security lists are associated *with the subnet*, but the rules are
        applied to the individual VNICs in the subnet.


        :return: The security_list_ids of this UpdateSubnetDetails.
        :rtype: list[str]
        """
        return self._security_list_ids

    @security_list_ids.setter
    def security_list_ids(self, security_list_ids):
        """
        Sets the security_list_ids of this UpdateSubnetDetails.
        The OCIDs of the security list or lists the subnet will use. This
        replaces the entire current set of security lists. Remember that
        security lists are associated *with the subnet*, but the rules are
        applied to the individual VNICs in the subnet.


        :param security_list_ids: The security_list_ids of this UpdateSubnetDetails.
        :type: list[str]
        """
        self._security_list_ids = security_list_ids

    @property
    def cidr_block(self):
        """
        Gets the cidr_block of this UpdateSubnetDetails.
        The CIDR block of the subnet. The new CIDR block must meet the following criteria:

        - Must be valid.
        - The CIDR block's IP range must be completely within one of the VCN's CIDR block ranges.
        - The old and new CIDR block ranges must use the same network address. Example: `10.0.0.0/25` and `10.0.0.0/24`.
        - Must contain all IP addresses in use in the old CIDR range.
        - The new CIDR range's broadcast address (last IP address of CIDR range) must not be an IP address in use in the old CIDR range.

        **Note:** If you are changing the CIDR block, you cannot create VNICs or private IPs for this resource while the update is in progress.

        Example: `172.16.0.0/16`


        :return: The cidr_block of this UpdateSubnetDetails.
        :rtype: str
        """
        return self._cidr_block

    @cidr_block.setter
    def cidr_block(self, cidr_block):
        """
        Sets the cidr_block of this UpdateSubnetDetails.
        The CIDR block of the subnet. The new CIDR block must meet the following criteria:

        - Must be valid.
        - The CIDR block's IP range must be completely within one of the VCN's CIDR block ranges.
        - The old and new CIDR block ranges must use the same network address. Example: `10.0.0.0/25` and `10.0.0.0/24`.
        - Must contain all IP addresses in use in the old CIDR range.
        - The new CIDR range's broadcast address (last IP address of CIDR range) must not be an IP address in use in the old CIDR range.

        **Note:** If you are changing the CIDR block, you cannot create VNICs or private IPs for this resource while the update is in progress.

        Example: `172.16.0.0/16`


        :param cidr_block: The cidr_block of this UpdateSubnetDetails.
        :type: str
        """
        self._cidr_block = cidr_block

    @property
    def ipv6_cidr_block(self):
        """
        Gets the ipv6_cidr_block of this UpdateSubnetDetails.
        This is the IPv6 CIDR block for the subnet's IP address space.
        The subnet size is always /64.
        See `IPv6 Addresses`__.
        The provided CIDR must maintain the following rules -

        a. The IPv6 CIDR block is valid and correctly formatted.
        b. The IPv6 CIDR is within the parent VCN IPv6 range.

        Example: `2001:0db8:0123:1111::/64`

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/ipv6.htm


        :return: The ipv6_cidr_block of this UpdateSubnetDetails.
        :rtype: str
        """
        return self._ipv6_cidr_block

    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, ipv6_cidr_block):
        """
        Sets the ipv6_cidr_block of this UpdateSubnetDetails.
        This is the IPv6 CIDR block for the subnet's IP address space.
        The subnet size is always /64.
        See `IPv6 Addresses`__.
        The provided CIDR must maintain the following rules -

        a. The IPv6 CIDR block is valid and correctly formatted.
        b. The IPv6 CIDR is within the parent VCN IPv6 range.

        Example: `2001:0db8:0123:1111::/64`

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/ipv6.htm


        :param ipv6_cidr_block: The ipv6_cidr_block of this UpdateSubnetDetails.
        :type: str
        """
        self._ipv6_cidr_block = ipv6_cidr_block

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
