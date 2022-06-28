# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
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

        """
        self.swagger_types = {
            'defined_tags': 'dict(str, dict(str, object))',
            'dhcp_options_id': 'str',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'route_table_id': 'str',
            'security_list_ids': 'list[str]'
        }

        self.attribute_map = {
            'defined_tags': 'definedTags',
            'dhcp_options_id': 'dhcpOptionsId',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'route_table_id': 'routeTableId',
            'security_list_ids': 'securityListIds'
        }

        self._defined_tags = None
        self._dhcp_options_id = None
        self._display_name = None
        self._freeform_tags = None
        self._route_table_id = None
        self._security_list_ids = None

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateSubnetDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateSubnetDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateSubnetDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateSubnetDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def dhcp_options_id(self):
        """
        Gets the dhcp_options_id of this UpdateSubnetDetails.
        The `OCID`__ of the set of DHCP options the subnet will use.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The dhcp_options_id of this UpdateSubnetDetails.
        :rtype: str
        """
        return self._dhcp_options_id

    @dhcp_options_id.setter
    def dhcp_options_id(self, dhcp_options_id):
        """
        Sets the dhcp_options_id of this UpdateSubnetDetails.
        The `OCID`__ of the set of DHCP options the subnet will use.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


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
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateSubnetDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateSubnetDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateSubnetDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def route_table_id(self):
        """
        Gets the route_table_id of this UpdateSubnetDetails.
        The `OCID`__ of the route table the subnet will use.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The route_table_id of this UpdateSubnetDetails.
        :rtype: str
        """
        return self._route_table_id

    @route_table_id.setter
    def route_table_id(self, route_table_id):
        """
        Sets the route_table_id of this UpdateSubnetDetails.
        The `OCID`__ of the route table the subnet will use.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


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

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
