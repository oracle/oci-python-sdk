# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateVlanDetails(object):
    """
    UpdateVlanDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateVlanDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateVlanDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this UpdateVlanDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateVlanDetails.
        :type freeform_tags: dict(str, str)

        :param nsg_ids:
            The value to assign to the nsg_ids property of this UpdateVlanDetails.
        :type nsg_ids: list[str]

        :param route_table_id:
            The value to assign to the route_table_id property of this UpdateVlanDetails.
        :type route_table_id: str

        :param cidr_block:
            The value to assign to the cidr_block property of this UpdateVlanDetails.
        :type cidr_block: str

        """
        self.swagger_types = {
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'nsg_ids': 'list[str]',
            'route_table_id': 'str',
            'cidr_block': 'str'
        }

        self.attribute_map = {
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'nsg_ids': 'nsgIds',
            'route_table_id': 'routeTableId',
            'cidr_block': 'cidrBlock'
        }

        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._nsg_ids = None
        self._route_table_id = None
        self._cidr_block = None

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateVlanDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateVlanDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateVlanDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateVlanDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateVlanDetails.
        A descriptive name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this UpdateVlanDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateVlanDetails.
        A descriptive name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this UpdateVlanDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateVlanDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateVlanDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateVlanDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateVlanDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this UpdateVlanDetails.
        A list of the OCIDs of the network security groups (NSGs) to use with
        this VLAN. All VNICs in the VLAN will belong to these NSGs. For more
        information about NSGs, see
        :class:`NetworkSecurityGroup`.


        :return: The nsg_ids of this UpdateVlanDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this UpdateVlanDetails.
        A list of the OCIDs of the network security groups (NSGs) to use with
        this VLAN. All VNICs in the VLAN will belong to these NSGs. For more
        information about NSGs, see
        :class:`NetworkSecurityGroup`.


        :param nsg_ids: The nsg_ids of this UpdateVlanDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def route_table_id(self):
        """
        Gets the route_table_id of this UpdateVlanDetails.
        The OCID of the route table the VLAN will use.


        :return: The route_table_id of this UpdateVlanDetails.
        :rtype: str
        """
        return self._route_table_id

    @route_table_id.setter
    def route_table_id(self, route_table_id):
        """
        Sets the route_table_id of this UpdateVlanDetails.
        The OCID of the route table the VLAN will use.


        :param route_table_id: The route_table_id of this UpdateVlanDetails.
        :type: str
        """
        self._route_table_id = route_table_id

    @property
    def cidr_block(self):
        """
        Gets the cidr_block of this UpdateVlanDetails.
        The CIDR block of the VLAN. The new CIDR block must meet the following criteria:

        - Must be valid.
        - The CIDR block's IP range must be completely within one of the VCN's CIDR block ranges.
        - The old and new CIDR block ranges must use the same network address. Example: `10.0.0.0/25` and `10.0.0.0/24`.
        - Must contain all IP addresses in use in the old CIDR range.
        - The new CIDR range's broadcast address (last IP address of CIDR range) must not be an IP address in use in the old CIDR range.

        **Note:** If you are changing the CIDR block, you cannot create VNICs or private IPs for this resource while the update is in progress.


        :return: The cidr_block of this UpdateVlanDetails.
        :rtype: str
        """
        return self._cidr_block

    @cidr_block.setter
    def cidr_block(self, cidr_block):
        """
        Sets the cidr_block of this UpdateVlanDetails.
        The CIDR block of the VLAN. The new CIDR block must meet the following criteria:

        - Must be valid.
        - The CIDR block's IP range must be completely within one of the VCN's CIDR block ranges.
        - The old and new CIDR block ranges must use the same network address. Example: `10.0.0.0/25` and `10.0.0.0/24`.
        - Must contain all IP addresses in use in the old CIDR range.
        - The new CIDR range's broadcast address (last IP address of CIDR range) must not be an IP address in use in the old CIDR range.

        **Note:** If you are changing the CIDR block, you cannot create VNICs or private IPs for this resource while the update is in progress.


        :param cidr_block: The cidr_block of this UpdateVlanDetails.
        :type: str
        """
        self._cidr_block = cidr_block

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
