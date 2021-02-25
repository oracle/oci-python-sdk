# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateMountTargetDetails(object):
    """
    Details for creating the mount target.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateMountTargetDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this CreateMountTargetDetails.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateMountTargetDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateMountTargetDetails.
        :type display_name: str

        :param hostname_label:
            The value to assign to the hostname_label property of this CreateMountTargetDetails.
        :type hostname_label: str

        :param ip_address:
            The value to assign to the ip_address property of this CreateMountTargetDetails.
        :type ip_address: str

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateMountTargetDetails.
        :type subnet_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this CreateMountTargetDetails.
        :type nsg_ids: list[str]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateMountTargetDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateMountTargetDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'hostname_label': 'str',
            'ip_address': 'str',
            'subnet_id': 'str',
            'nsg_ids': 'list[str]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'hostname_label': 'hostnameLabel',
            'ip_address': 'ipAddress',
            'subnet_id': 'subnetId',
            'nsg_ids': 'nsgIds',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._display_name = None
        self._hostname_label = None
        self._ip_address = None
        self._subnet_id = None
        self._nsg_ids = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this CreateMountTargetDetails.
        The availability domain in which to create the mount target.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this CreateMountTargetDetails.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this CreateMountTargetDetails.
        The availability domain in which to create the mount target.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this CreateMountTargetDetails.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateMountTargetDetails.
        The `OCID`__ of the compartment in which to create the mount target.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateMountTargetDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateMountTargetDetails.
        The `OCID`__ of the compartment in which to create the mount target.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateMountTargetDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateMountTargetDetails.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.

        Example: `My mount target`


        :return: The display_name of this CreateMountTargetDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateMountTargetDetails.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.

        Example: `My mount target`


        :param display_name: The display_name of this CreateMountTargetDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def hostname_label(self):
        """
        Gets the hostname_label of this CreateMountTargetDetails.
        The hostname for the mount target's IP address, used for
        DNS resolution. The value is the hostname portion of the private IP
        address's fully qualified domain name (FQDN). For example,
        `files-1` in the FQDN `files-1.subnet123.vcn1.oraclevcn.com`.
        Must be unique across all VNICs in the subnet and comply
        with `RFC 952`__
        and `RFC 1123`__.

        For more information, see
        `DNS in Your Virtual Cloud Network`__.

        Example: `files-1`

        __ https://tools.ietf.org/html/rfc952
        __ https://tools.ietf.org/html/rfc1123
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/dns.htm


        :return: The hostname_label of this CreateMountTargetDetails.
        :rtype: str
        """
        return self._hostname_label

    @hostname_label.setter
    def hostname_label(self, hostname_label):
        """
        Sets the hostname_label of this CreateMountTargetDetails.
        The hostname for the mount target's IP address, used for
        DNS resolution. The value is the hostname portion of the private IP
        address's fully qualified domain name (FQDN). For example,
        `files-1` in the FQDN `files-1.subnet123.vcn1.oraclevcn.com`.
        Must be unique across all VNICs in the subnet and comply
        with `RFC 952`__
        and `RFC 1123`__.

        For more information, see
        `DNS in Your Virtual Cloud Network`__.

        Example: `files-1`

        __ https://tools.ietf.org/html/rfc952
        __ https://tools.ietf.org/html/rfc1123
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/dns.htm


        :param hostname_label: The hostname_label of this CreateMountTargetDetails.
        :type: str
        """
        self._hostname_label = hostname_label

    @property
    def ip_address(self):
        """
        Gets the ip_address of this CreateMountTargetDetails.
        A private IP address of your choice. Must be an available IP address within
        the subnet's CIDR. If you don't specify a value, Oracle automatically
        assigns a private IP address from the subnet.

        Example: `10.0.3.3`


        :return: The ip_address of this CreateMountTargetDetails.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this CreateMountTargetDetails.
        A private IP address of your choice. Must be an available IP address within
        the subnet's CIDR. If you don't specify a value, Oracle automatically
        assigns a private IP address from the subnet.

        Example: `10.0.3.3`


        :param ip_address: The ip_address of this CreateMountTargetDetails.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this CreateMountTargetDetails.
        The `OCID`__ of the subnet in which to create the mount target.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this CreateMountTargetDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this CreateMountTargetDetails.
        The `OCID`__ of the subnet in which to create the mount target.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this CreateMountTargetDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this CreateMountTargetDetails.
        A list of Network Security Group `OCIDs`__ associated with this mount target.
        A maximum of 5 is allowed.
        Setting this to an empty array after the list is created removes the mount target from all NSGs.
        For more information about NSGs, see `Security Rules`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :return: The nsg_ids of this CreateMountTargetDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this CreateMountTargetDetails.
        A list of Network Security Group `OCIDs`__ associated with this mount target.
        A maximum of 5 is allowed.
        Setting this to an empty array after the list is created removes the mount target from all NSGs.
        For more information about NSGs, see `Security Rules`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :param nsg_ids: The nsg_ids of this CreateMountTargetDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateMountTargetDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair
         with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateMountTargetDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateMountTargetDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair
         with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateMountTargetDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateMountTargetDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateMountTargetDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateMountTargetDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateMountTargetDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
