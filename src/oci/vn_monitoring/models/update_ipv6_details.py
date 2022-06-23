# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateIpv6Details(object):
    """
    UpdateIpv6Details model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateIpv6Details object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateIpv6Details.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this UpdateIpv6Details.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateIpv6Details.
        :type freeform_tags: dict(str, str)

        :param is_internet_access_allowed:
            The value to assign to the is_internet_access_allowed property of this UpdateIpv6Details.
        :type is_internet_access_allowed: bool

        :param vnic_id:
            The value to assign to the vnic_id property of this UpdateIpv6Details.
        :type vnic_id: str

        """
        self.swagger_types = {
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'is_internet_access_allowed': 'bool',
            'vnic_id': 'str'
        }

        self.attribute_map = {
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'is_internet_access_allowed': 'isInternetAccessAllowed',
            'vnic_id': 'vnicId'
        }

        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._is_internet_access_allowed = None
        self._vnic_id = None

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateIpv6Details.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateIpv6Details.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateIpv6Details.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateIpv6Details.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateIpv6Details.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this UpdateIpv6Details.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateIpv6Details.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this UpdateIpv6Details.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateIpv6Details.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateIpv6Details.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateIpv6Details.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateIpv6Details.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def is_internet_access_allowed(self):
        """
        Gets the is_internet_access_allowed of this UpdateIpv6Details.
        Whether the IPv6 can be used for internet communication. Allowed by default for an IPv6 in
        a public subnet. Never allowed for an IPv6 in a private subnet. If the value is `true`, the
        IPv6 uses its public IP address for internet communication.

        If you switch this from `true` to `false`, the `publicIpAddress` attribute for the IPv6
        becomes null.

        Example: `false`


        :return: The is_internet_access_allowed of this UpdateIpv6Details.
        :rtype: bool
        """
        return self._is_internet_access_allowed

    @is_internet_access_allowed.setter
    def is_internet_access_allowed(self, is_internet_access_allowed):
        """
        Sets the is_internet_access_allowed of this UpdateIpv6Details.
        Whether the IPv6 can be used for internet communication. Allowed by default for an IPv6 in
        a public subnet. Never allowed for an IPv6 in a private subnet. If the value is `true`, the
        IPv6 uses its public IP address for internet communication.

        If you switch this from `true` to `false`, the `publicIpAddress` attribute for the IPv6
        becomes null.

        Example: `false`


        :param is_internet_access_allowed: The is_internet_access_allowed of this UpdateIpv6Details.
        :type: bool
        """
        self._is_internet_access_allowed = is_internet_access_allowed

    @property
    def vnic_id(self):
        """
        Gets the vnic_id of this UpdateIpv6Details.
        The `OCID`__ of the VNIC to reassign the IPv6 to.
        The VNIC must be in the same subnet as the current VNIC.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The vnic_id of this UpdateIpv6Details.
        :rtype: str
        """
        return self._vnic_id

    @vnic_id.setter
    def vnic_id(self, vnic_id):
        """
        Sets the vnic_id of this UpdateIpv6Details.
        The `OCID`__ of the VNIC to reassign the IPv6 to.
        The VNIC must be in the same subnet as the current VNIC.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param vnic_id: The vnic_id of this UpdateIpv6Details.
        :type: str
        """
        self._vnic_id = vnic_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
