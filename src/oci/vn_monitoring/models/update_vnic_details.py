# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateVnicDetails(object):
    """
    UpdateVnicDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateVnicDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateVnicDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this UpdateVnicDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateVnicDetails.
        :type freeform_tags: dict(str, str)

        :param hostname_label:
            The value to assign to the hostname_label property of this UpdateVnicDetails.
        :type hostname_label: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this UpdateVnicDetails.
        :type nsg_ids: list[str]

        :param skip_source_dest_check:
            The value to assign to the skip_source_dest_check property of this UpdateVnicDetails.
        :type skip_source_dest_check: bool

        """
        self.swagger_types = {
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'hostname_label': 'str',
            'nsg_ids': 'list[str]',
            'skip_source_dest_check': 'bool'
        }

        self.attribute_map = {
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'hostname_label': 'hostnameLabel',
            'nsg_ids': 'nsgIds',
            'skip_source_dest_check': 'skipSourceDestCheck'
        }

        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._hostname_label = None
        self._nsg_ids = None
        self._skip_source_dest_check = None

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateVnicDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateVnicDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateVnicDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateVnicDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateVnicDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this UpdateVnicDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateVnicDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this UpdateVnicDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateVnicDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateVnicDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateVnicDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateVnicDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def hostname_label(self):
        """
        Gets the hostname_label of this UpdateVnicDetails.
        The hostname for the VNIC's primary private IP. Used for DNS. The value is the hostname
        portion of the primary private IP's fully qualified domain name (FQDN)
        (for example, `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`).
        Must be unique across all VNICs in the subnet and comply with
        `RFC 952`__ and
        `RFC 1123`__.
        The value appears in the :class:`Vnic` object and also the
        :class:`PrivateIp` object returned by
        :func:`list_private_ips` and
        :func:`get_private_ip`.

        For more information, see
        `DNS in Your Virtual Cloud Network`__.

        __ https://tools.ietf.org/html/rfc952
        __ https://tools.ietf.org/html/rfc1123
        __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/dns.htm


        :return: The hostname_label of this UpdateVnicDetails.
        :rtype: str
        """
        return self._hostname_label

    @hostname_label.setter
    def hostname_label(self, hostname_label):
        """
        Sets the hostname_label of this UpdateVnicDetails.
        The hostname for the VNIC's primary private IP. Used for DNS. The value is the hostname
        portion of the primary private IP's fully qualified domain name (FQDN)
        (for example, `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`).
        Must be unique across all VNICs in the subnet and comply with
        `RFC 952`__ and
        `RFC 1123`__.
        The value appears in the :class:`Vnic` object and also the
        :class:`PrivateIp` object returned by
        :func:`list_private_ips` and
        :func:`get_private_ip`.

        For more information, see
        `DNS in Your Virtual Cloud Network`__.

        __ https://tools.ietf.org/html/rfc952
        __ https://tools.ietf.org/html/rfc1123
        __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/dns.htm


        :param hostname_label: The hostname_label of this UpdateVnicDetails.
        :type: str
        """
        self._hostname_label = hostname_label

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this UpdateVnicDetails.
        A list of the OCIDs of the network security groups (NSGs) to add the VNIC to. Setting this as
        an empty array removes the VNIC from all network security groups.

        For more information about NSGs, see
        :class:`NetworkSecurityGroup`.


        :return: The nsg_ids of this UpdateVnicDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this UpdateVnicDetails.
        A list of the OCIDs of the network security groups (NSGs) to add the VNIC to. Setting this as
        an empty array removes the VNIC from all network security groups.

        For more information about NSGs, see
        :class:`NetworkSecurityGroup`.


        :param nsg_ids: The nsg_ids of this UpdateVnicDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def skip_source_dest_check(self):
        """
        Gets the skip_source_dest_check of this UpdateVnicDetails.
        Whether the source/destination check is disabled on the VNIC.
        Defaults to `false`, which means the check is performed. For information about why you would
        skip the source/destination check, see
        `Using a Private IP as a Route Target`__.
        Example: `true`

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm#privateip


        :return: The skip_source_dest_check of this UpdateVnicDetails.
        :rtype: bool
        """
        return self._skip_source_dest_check

    @skip_source_dest_check.setter
    def skip_source_dest_check(self, skip_source_dest_check):
        """
        Sets the skip_source_dest_check of this UpdateVnicDetails.
        Whether the source/destination check is disabled on the VNIC.
        Defaults to `false`, which means the check is performed. For information about why you would
        skip the source/destination check, see
        `Using a Private IP as a Route Target`__.
        Example: `true`

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm#privateip


        :param skip_source_dest_check: The skip_source_dest_check of this UpdateVnicDetails.
        :type: bool
        """
        self._skip_source_dest_check = skip_source_dest_check

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
