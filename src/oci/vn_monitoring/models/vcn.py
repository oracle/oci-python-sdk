# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Vcn(object):
    """
    A virtual cloud network (VCN). For more information, see
    `Overview of the Networking Service`__.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator. If you're an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/overview.htm
    __ https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the lifecycle_state property of a Vcn.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a Vcn.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a Vcn.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a Vcn.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    def __init__(self, **kwargs):
        """
        Initializes a new Vcn object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cidr_block:
            The value to assign to the cidr_block property of this Vcn.
        :type cidr_block: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Vcn.
        :type compartment_id: str

        :param default_dhcp_options_id:
            The value to assign to the default_dhcp_options_id property of this Vcn.
        :type default_dhcp_options_id: str

        :param default_route_table_id:
            The value to assign to the default_route_table_id property of this Vcn.
        :type default_route_table_id: str

        :param default_security_list_id:
            The value to assign to the default_security_list_id property of this Vcn.
        :type default_security_list_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this Vcn.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this Vcn.
        :type display_name: str

        :param dns_label:
            The value to assign to the dns_label property of this Vcn.
        :type dns_label: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Vcn.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this Vcn.
        :type id: str

        :param ipv6_cidr_block:
            The value to assign to the ipv6_cidr_block property of this Vcn.
        :type ipv6_cidr_block: str

        :param ipv6_public_cidr_block:
            The value to assign to the ipv6_public_cidr_block property of this Vcn.
        :type ipv6_public_cidr_block: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Vcn.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this Vcn.
        :type time_created: datetime

        :param vcn_domain_name:
            The value to assign to the vcn_domain_name property of this Vcn.
        :type vcn_domain_name: str

        """
        self.swagger_types = {
            'cidr_block': 'str',
            'compartment_id': 'str',
            'default_dhcp_options_id': 'str',
            'default_route_table_id': 'str',
            'default_security_list_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'dns_label': 'str',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'ipv6_cidr_block': 'str',
            'ipv6_public_cidr_block': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'vcn_domain_name': 'str'
        }

        self.attribute_map = {
            'cidr_block': 'cidrBlock',
            'compartment_id': 'compartmentId',
            'default_dhcp_options_id': 'defaultDhcpOptionsId',
            'default_route_table_id': 'defaultRouteTableId',
            'default_security_list_id': 'defaultSecurityListId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'dns_label': 'dnsLabel',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'ipv6_cidr_block': 'ipv6CidrBlock',
            'ipv6_public_cidr_block': 'ipv6PublicCidrBlock',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'vcn_domain_name': 'vcnDomainName'
        }

        self._cidr_block = None
        self._compartment_id = None
        self._default_dhcp_options_id = None
        self._default_route_table_id = None
        self._default_security_list_id = None
        self._defined_tags = None
        self._display_name = None
        self._dns_label = None
        self._freeform_tags = None
        self._id = None
        self._ipv6_cidr_block = None
        self._ipv6_public_cidr_block = None
        self._lifecycle_state = None
        self._time_created = None
        self._vcn_domain_name = None

    @property
    def cidr_block(self):
        """
        **[Required]** Gets the cidr_block of this Vcn.
        The CIDR block IP address of the VCN.

        Example: `172.16.0.0/16`


        :return: The cidr_block of this Vcn.
        :rtype: str
        """
        return self._cidr_block

    @cidr_block.setter
    def cidr_block(self, cidr_block):
        """
        Sets the cidr_block of this Vcn.
        The CIDR block IP address of the VCN.

        Example: `172.16.0.0/16`


        :param cidr_block: The cidr_block of this Vcn.
        :type: str
        """
        self._cidr_block = cidr_block

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Vcn.
        The `OCID`__ of the compartment containing the VCN.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this Vcn.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Vcn.
        The `OCID`__ of the compartment containing the VCN.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this Vcn.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def default_dhcp_options_id(self):
        """
        Gets the default_dhcp_options_id of this Vcn.
        The `OCID`__ for the VCN's default set of DHCP options.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The default_dhcp_options_id of this Vcn.
        :rtype: str
        """
        return self._default_dhcp_options_id

    @default_dhcp_options_id.setter
    def default_dhcp_options_id(self, default_dhcp_options_id):
        """
        Sets the default_dhcp_options_id of this Vcn.
        The `OCID`__ for the VCN's default set of DHCP options.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param default_dhcp_options_id: The default_dhcp_options_id of this Vcn.
        :type: str
        """
        self._default_dhcp_options_id = default_dhcp_options_id

    @property
    def default_route_table_id(self):
        """
        Gets the default_route_table_id of this Vcn.
        The `OCID`__ for the VCN's default route table.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The default_route_table_id of this Vcn.
        :rtype: str
        """
        return self._default_route_table_id

    @default_route_table_id.setter
    def default_route_table_id(self, default_route_table_id):
        """
        Sets the default_route_table_id of this Vcn.
        The `OCID`__ for the VCN's default route table.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param default_route_table_id: The default_route_table_id of this Vcn.
        :type: str
        """
        self._default_route_table_id = default_route_table_id

    @property
    def default_security_list_id(self):
        """
        Gets the default_security_list_id of this Vcn.
        The `OCID`__ for the VCN's default security list.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The default_security_list_id of this Vcn.
        :rtype: str
        """
        return self._default_security_list_id

    @default_security_list_id.setter
    def default_security_list_id(self, default_security_list_id):
        """
        Sets the default_security_list_id of this Vcn.
        The `OCID`__ for the VCN's default security list.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param default_security_list_id: The default_security_list_id of this Vcn.
        :type: str
        """
        self._default_security_list_id = default_security_list_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Vcn.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this Vcn.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Vcn.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this Vcn.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this Vcn.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this Vcn.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Vcn.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this Vcn.
        :type: str
        """
        self._display_name = display_name

    @property
    def dns_label(self):
        """
        Gets the dns_label of this Vcn.
        A DNS label for the VCN, used in conjunction with the VNIC's hostname and
        subnet's DNS label to form a fully qualified domain name (FQDN) for each VNIC
        within this subnet (for example, `bminstance-1.subnet123.vcn1.oraclevcn.com`).
        Must be an alphanumeric string that begins with a letter.
        The value cannot be changed.

        The absence of this parameter means the Internet and VCN Resolver will
        not work for this VCN.

        For more information, see
        `DNS in Your Virtual Cloud Network`__.

        Example: `vcn1`

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/dns.htm


        :return: The dns_label of this Vcn.
        :rtype: str
        """
        return self._dns_label

    @dns_label.setter
    def dns_label(self, dns_label):
        """
        Sets the dns_label of this Vcn.
        A DNS label for the VCN, used in conjunction with the VNIC's hostname and
        subnet's DNS label to form a fully qualified domain name (FQDN) for each VNIC
        within this subnet (for example, `bminstance-1.subnet123.vcn1.oraclevcn.com`).
        Must be an alphanumeric string that begins with a letter.
        The value cannot be changed.

        The absence of this parameter means the Internet and VCN Resolver will
        not work for this VCN.

        For more information, see
        `DNS in Your Virtual Cloud Network`__.

        Example: `vcn1`

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/dns.htm


        :param dns_label: The dns_label of this Vcn.
        :type: str
        """
        self._dns_label = dns_label

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Vcn.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this Vcn.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Vcn.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this Vcn.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Vcn.
        The VCN's Oracle ID (`OCID`__).

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this Vcn.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Vcn.
        The VCN's Oracle ID (`OCID`__).

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this Vcn.
        :type: str
        """
        self._id = id

    @property
    def ipv6_cidr_block(self):
        """
        Gets the ipv6_cidr_block of this Vcn.
        For an IPv6-enabled VCN, this is the IPv6 CIDR block for the VCN's private IP address space.
        The VCN size is always /56. Oracle
        provides the IPv6 CIDR block to use as the *same* CIDR for the `ipv6PublicCidrBlock`.
        When creating a subnet, specify the last 8 bits, 00 to FF.
        See `IPv6 Addresses`__.
        Example: `2001:0db8:0123::/56`

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/ipv6.htm


        :return: The ipv6_cidr_block of this Vcn.
        :rtype: str
        """
        return self._ipv6_cidr_block

    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, ipv6_cidr_block):
        """
        Sets the ipv6_cidr_block of this Vcn.
        For an IPv6-enabled VCN, this is the IPv6 CIDR block for the VCN's private IP address space.
        The VCN size is always /56. Oracle
        provides the IPv6 CIDR block to use as the *same* CIDR for the `ipv6PublicCidrBlock`.
        When creating a subnet, specify the last 8 bits, 00 to FF.
        See `IPv6 Addresses`__.
        Example: `2001:0db8:0123::/56`

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/ipv6.htm


        :param ipv6_cidr_block: The ipv6_cidr_block of this Vcn.
        :type: str
        """
        self._ipv6_cidr_block = ipv6_cidr_block

    @property
    def ipv6_public_cidr_block(self):
        """
        Gets the ipv6_public_cidr_block of this Vcn.
        For an IPv6-enabled VCN, this is the IPv6 CIDR block for the VCN's public IP address space.
        The VCN size is always /56. This CIDR is always provided by Oracle. If you don't provide a
        custom CIDR for the `ipv6CidrBlock` when creating the VCN, Oracle assigns that value and also
        uses it for `ipv6PublicCidrBlock`. Oracle uses addresses from this block for the `publicIpAddress`
        attribute of an :class:`Ipv6` that has internet access allowed.

        Example: `2001:0db8:0123::/48`


        :return: The ipv6_public_cidr_block of this Vcn.
        :rtype: str
        """
        return self._ipv6_public_cidr_block

    @ipv6_public_cidr_block.setter
    def ipv6_public_cidr_block(self, ipv6_public_cidr_block):
        """
        Sets the ipv6_public_cidr_block of this Vcn.
        For an IPv6-enabled VCN, this is the IPv6 CIDR block for the VCN's public IP address space.
        The VCN size is always /56. This CIDR is always provided by Oracle. If you don't provide a
        custom CIDR for the `ipv6CidrBlock` when creating the VCN, Oracle assigns that value and also
        uses it for `ipv6PublicCidrBlock`. Oracle uses addresses from this block for the `publicIpAddress`
        attribute of an :class:`Ipv6` that has internet access allowed.

        Example: `2001:0db8:0123::/48`


        :param ipv6_public_cidr_block: The ipv6_public_cidr_block of this Vcn.
        :type: str
        """
        self._ipv6_public_cidr_block = ipv6_public_cidr_block

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Vcn.
        The VCN's current state.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"


        :return: The lifecycle_state of this Vcn.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Vcn.
        The VCN's current state.


        :param lifecycle_state: The lifecycle_state of this Vcn.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            raise ValueError(
                "Invalid value for `lifecycle_state`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this Vcn.
        The date and time the VCN was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Vcn.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Vcn.
        The date and time the VCN was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Vcn.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def vcn_domain_name(self):
        """
        Gets the vcn_domain_name of this Vcn.
        The VCN's domain name, which consists of the VCN's DNS label, and the
        `oraclevcn.com` domain.

        For more information, see
        `DNS in Your Virtual Cloud Network`__.

        Example: `vcn1.oraclevcn.com`

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/dns.htm


        :return: The vcn_domain_name of this Vcn.
        :rtype: str
        """
        return self._vcn_domain_name

    @vcn_domain_name.setter
    def vcn_domain_name(self, vcn_domain_name):
        """
        Sets the vcn_domain_name of this Vcn.
        The VCN's domain name, which consists of the VCN's DNS label, and the
        `oraclevcn.com` domain.

        For more information, see
        `DNS in Your Virtual Cloud Network`__.

        Example: `vcn1.oraclevcn.com`

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/dns.htm


        :param vcn_domain_name: The vcn_domain_name of this Vcn.
        :type: str
        """
        self._vcn_domain_name = vcn_domain_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
