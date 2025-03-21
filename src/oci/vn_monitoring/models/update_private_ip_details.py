# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdatePrivateIpDetails(object):
    """
    UpdatePrivateIpDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdatePrivateIpDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdatePrivateIpDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this UpdatePrivateIpDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdatePrivateIpDetails.
        :type freeform_tags: dict(str, str)

        :param hostname_label:
            The value to assign to the hostname_label property of this UpdatePrivateIpDetails.
        :type hostname_label: str

        :param vnic_id:
            The value to assign to the vnic_id property of this UpdatePrivateIpDetails.
        :type vnic_id: str

        """
        self.swagger_types = {
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'hostname_label': 'str',
            'vnic_id': 'str'
        }
        self.attribute_map = {
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'hostname_label': 'hostnameLabel',
            'vnic_id': 'vnicId'
        }
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._hostname_label = None
        self._vnic_id = None

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdatePrivateIpDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdatePrivateIpDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdatePrivateIpDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdatePrivateIpDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdatePrivateIpDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this UpdatePrivateIpDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdatePrivateIpDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this UpdatePrivateIpDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdatePrivateIpDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdatePrivateIpDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdatePrivateIpDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdatePrivateIpDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def hostname_label(self):
        """
        Gets the hostname_label of this UpdatePrivateIpDetails.
        The hostname for the private IP. Used for DNS. The value
        is the hostname portion of the private IP's fully qualified domain name (FQDN)
        (for example, `bminstance1` in FQDN `bminstance1.subnet123.vcn1.oraclevcn.com`).
        Must be unique across all VNICs in the subnet and comply with
        `RFC 952`__ and
        `RFC 1123`__.

        For more information, see
        `DNS in Your Virtual Cloud Network`__.

        Example: `bminstance1`

        __ https://tools.ietf.org/html/rfc952
        __ https://tools.ietf.org/html/rfc1123
        __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/dns.htm


        :return: The hostname_label of this UpdatePrivateIpDetails.
        :rtype: str
        """
        return self._hostname_label

    @hostname_label.setter
    def hostname_label(self, hostname_label):
        """
        Sets the hostname_label of this UpdatePrivateIpDetails.
        The hostname for the private IP. Used for DNS. The value
        is the hostname portion of the private IP's fully qualified domain name (FQDN)
        (for example, `bminstance1` in FQDN `bminstance1.subnet123.vcn1.oraclevcn.com`).
        Must be unique across all VNICs in the subnet and comply with
        `RFC 952`__ and
        `RFC 1123`__.

        For more information, see
        `DNS in Your Virtual Cloud Network`__.

        Example: `bminstance1`

        __ https://tools.ietf.org/html/rfc952
        __ https://tools.ietf.org/html/rfc1123
        __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/dns.htm


        :param hostname_label: The hostname_label of this UpdatePrivateIpDetails.
        :type: str
        """
        self._hostname_label = hostname_label

    @property
    def vnic_id(self):
        """
        Gets the vnic_id of this UpdatePrivateIpDetails.
        The `OCID`__ of the VNIC to reassign the private IP to. The VNIC must
        be in the same subnet as the current VNIC.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The vnic_id of this UpdatePrivateIpDetails.
        :rtype: str
        """
        return self._vnic_id

    @vnic_id.setter
    def vnic_id(self, vnic_id):
        """
        Sets the vnic_id of this UpdatePrivateIpDetails.
        The `OCID`__ of the VNIC to reassign the private IP to. The VNIC must
        be in the same subnet as the current VNIC.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param vnic_id: The vnic_id of this UpdatePrivateIpDetails.
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
