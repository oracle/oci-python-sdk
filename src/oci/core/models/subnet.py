# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Subnet(object):
    """
    A logical subdivision of a VCN. Each subnet
    consists of a contiguous range of IP addresses that do not overlap with
    other subnets in the VCN. Example: 172.16.1.0/24. For more information, see
    `Overview of the Networking Service`__ and
    `VCNs and Subnets`__.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator. If you're an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/overview.htm
    __ https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm
    __ https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the lifecycle_state property of a Subnet.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a Subnet.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a Subnet.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a Subnet.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a Subnet.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    def __init__(self, **kwargs):
        """
        Initializes a new Subnet object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this Subnet.
        :type availability_domain: str

        :param cidr_block:
            The value to assign to the cidr_block property of this Subnet.
        :type cidr_block: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Subnet.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this Subnet.
        :type defined_tags: dict(str, dict(str, object))

        :param dhcp_options_id:
            The value to assign to the dhcp_options_id property of this Subnet.
        :type dhcp_options_id: str

        :param display_name:
            The value to assign to the display_name property of this Subnet.
        :type display_name: str

        :param dns_label:
            The value to assign to the dns_label property of this Subnet.
        :type dns_label: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Subnet.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this Subnet.
        :type id: str

        :param ipv6_cidr_block:
            The value to assign to the ipv6_cidr_block property of this Subnet.
        :type ipv6_cidr_block: str

        :param ipv6_virtual_router_ip:
            The value to assign to the ipv6_virtual_router_ip property of this Subnet.
        :type ipv6_virtual_router_ip: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Subnet.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param prohibit_internet_ingress:
            The value to assign to the prohibit_internet_ingress property of this Subnet.
        :type prohibit_internet_ingress: bool

        :param prohibit_public_ip_on_vnic:
            The value to assign to the prohibit_public_ip_on_vnic property of this Subnet.
        :type prohibit_public_ip_on_vnic: bool

        :param route_table_id:
            The value to assign to the route_table_id property of this Subnet.
        :type route_table_id: str

        :param security_list_ids:
            The value to assign to the security_list_ids property of this Subnet.
        :type security_list_ids: list[str]

        :param subnet_domain_name:
            The value to assign to the subnet_domain_name property of this Subnet.
        :type subnet_domain_name: str

        :param time_created:
            The value to assign to the time_created property of this Subnet.
        :type time_created: datetime

        :param vcn_id:
            The value to assign to the vcn_id property of this Subnet.
        :type vcn_id: str

        :param virtual_router_ip:
            The value to assign to the virtual_router_ip property of this Subnet.
        :type virtual_router_ip: str

        :param virtual_router_mac:
            The value to assign to the virtual_router_mac property of this Subnet.
        :type virtual_router_mac: str

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'cidr_block': 'str',
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'dhcp_options_id': 'str',
            'display_name': 'str',
            'dns_label': 'str',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'ipv6_cidr_block': 'str',
            'ipv6_virtual_router_ip': 'str',
            'lifecycle_state': 'str',
            'prohibit_internet_ingress': 'bool',
            'prohibit_public_ip_on_vnic': 'bool',
            'route_table_id': 'str',
            'security_list_ids': 'list[str]',
            'subnet_domain_name': 'str',
            'time_created': 'datetime',
            'vcn_id': 'str',
            'virtual_router_ip': 'str',
            'virtual_router_mac': 'str'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'cidr_block': 'cidrBlock',
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'dhcp_options_id': 'dhcpOptionsId',
            'display_name': 'displayName',
            'dns_label': 'dnsLabel',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'ipv6_cidr_block': 'ipv6CidrBlock',
            'ipv6_virtual_router_ip': 'ipv6VirtualRouterIp',
            'lifecycle_state': 'lifecycleState',
            'prohibit_internet_ingress': 'prohibitInternetIngress',
            'prohibit_public_ip_on_vnic': 'prohibitPublicIpOnVnic',
            'route_table_id': 'routeTableId',
            'security_list_ids': 'securityListIds',
            'subnet_domain_name': 'subnetDomainName',
            'time_created': 'timeCreated',
            'vcn_id': 'vcnId',
            'virtual_router_ip': 'virtualRouterIp',
            'virtual_router_mac': 'virtualRouterMac'
        }

        self._availability_domain = None
        self._cidr_block = None
        self._compartment_id = None
        self._defined_tags = None
        self._dhcp_options_id = None
        self._display_name = None
        self._dns_label = None
        self._freeform_tags = None
        self._id = None
        self._ipv6_cidr_block = None
        self._ipv6_virtual_router_ip = None
        self._lifecycle_state = None
        self._prohibit_internet_ingress = None
        self._prohibit_public_ip_on_vnic = None
        self._route_table_id = None
        self._security_list_ids = None
        self._subnet_domain_name = None
        self._time_created = None
        self._vcn_id = None
        self._virtual_router_ip = None
        self._virtual_router_mac = None

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this Subnet.
        The subnet's availability domain. This attribute will be null if this is a regional subnet
        instead of an AD-specific subnet. Oracle recommends creating regional subnets.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this Subnet.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this Subnet.
        The subnet's availability domain. This attribute will be null if this is a regional subnet
        instead of an AD-specific subnet. Oracle recommends creating regional subnets.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this Subnet.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def cidr_block(self):
        """
        **[Required]** Gets the cidr_block of this Subnet.
        The subnet's CIDR block.

        Example: `10.0.1.0/24`


        :return: The cidr_block of this Subnet.
        :rtype: str
        """
        return self._cidr_block

    @cidr_block.setter
    def cidr_block(self, cidr_block):
        """
        Sets the cidr_block of this Subnet.
        The subnet's CIDR block.

        Example: `10.0.1.0/24`


        :param cidr_block: The cidr_block of this Subnet.
        :type: str
        """
        self._cidr_block = cidr_block

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Subnet.
        The OCID of the compartment containing the subnet.


        :return: The compartment_id of this Subnet.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Subnet.
        The OCID of the compartment containing the subnet.


        :param compartment_id: The compartment_id of this Subnet.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Subnet.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Subnet.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Subnet.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Subnet.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def dhcp_options_id(self):
        """
        Gets the dhcp_options_id of this Subnet.
        The OCID of the set of DHCP options that the subnet uses.


        :return: The dhcp_options_id of this Subnet.
        :rtype: str
        """
        return self._dhcp_options_id

    @dhcp_options_id.setter
    def dhcp_options_id(self, dhcp_options_id):
        """
        Sets the dhcp_options_id of this Subnet.
        The OCID of the set of DHCP options that the subnet uses.


        :param dhcp_options_id: The dhcp_options_id of this Subnet.
        :type: str
        """
        self._dhcp_options_id = dhcp_options_id

    @property
    def display_name(self):
        """
        Gets the display_name of this Subnet.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this Subnet.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Subnet.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this Subnet.
        :type: str
        """
        self._display_name = display_name

    @property
    def dns_label(self):
        """
        Gets the dns_label of this Subnet.
        A DNS label for the subnet, used in conjunction with the VNIC's hostname and
        VCN's DNS label to form a fully qualified domain name (FQDN) for each VNIC
        within this subnet (for example, `bminstance-1.subnet123.vcn1.oraclevcn.com`).
        Must be an alphanumeric string that begins with a letter and is unique within the VCN.
        The value cannot be changed.

        The absence of this parameter means the Internet and VCN Resolver
        will not resolve hostnames of instances in this subnet.

        For more information, see
        `DNS in Your Virtual Cloud Network`__.

        Example: `subnet123`

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/dns.htm


        :return: The dns_label of this Subnet.
        :rtype: str
        """
        return self._dns_label

    @dns_label.setter
    def dns_label(self, dns_label):
        """
        Sets the dns_label of this Subnet.
        A DNS label for the subnet, used in conjunction with the VNIC's hostname and
        VCN's DNS label to form a fully qualified domain name (FQDN) for each VNIC
        within this subnet (for example, `bminstance-1.subnet123.vcn1.oraclevcn.com`).
        Must be an alphanumeric string that begins with a letter and is unique within the VCN.
        The value cannot be changed.

        The absence of this parameter means the Internet and VCN Resolver
        will not resolve hostnames of instances in this subnet.

        For more information, see
        `DNS in Your Virtual Cloud Network`__.

        Example: `subnet123`

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/dns.htm


        :param dns_label: The dns_label of this Subnet.
        :type: str
        """
        self._dns_label = dns_label

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Subnet.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Subnet.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Subnet.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Subnet.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Subnet.
        The subnet's Oracle ID (OCID).


        :return: The id of this Subnet.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Subnet.
        The subnet's Oracle ID (OCID).


        :param id: The id of this Subnet.
        :type: str
        """
        self._id = id

    @property
    def ipv6_cidr_block(self):
        """
        Gets the ipv6_cidr_block of this Subnet.
        For an IPv6-enabled subnet, this is the IPv6 CIDR block for the subnet's IP address space.
        The subnet size is always /64. See `IPv6 Addresses`__.

        Example: `2001:0db8:0123:1111::/64`

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/ipv6.htm


        :return: The ipv6_cidr_block of this Subnet.
        :rtype: str
        """
        return self._ipv6_cidr_block

    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, ipv6_cidr_block):
        """
        Sets the ipv6_cidr_block of this Subnet.
        For an IPv6-enabled subnet, this is the IPv6 CIDR block for the subnet's IP address space.
        The subnet size is always /64. See `IPv6 Addresses`__.

        Example: `2001:0db8:0123:1111::/64`

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/ipv6.htm


        :param ipv6_cidr_block: The ipv6_cidr_block of this Subnet.
        :type: str
        """
        self._ipv6_cidr_block = ipv6_cidr_block

    @property
    def ipv6_virtual_router_ip(self):
        """
        Gets the ipv6_virtual_router_ip of this Subnet.
        For an IPv6-enabled subnet, this is the IPv6 address of the virtual router.

        Example: `2001:0db8:0123:1111:89ab:cdef:1234:5678`


        :return: The ipv6_virtual_router_ip of this Subnet.
        :rtype: str
        """
        return self._ipv6_virtual_router_ip

    @ipv6_virtual_router_ip.setter
    def ipv6_virtual_router_ip(self, ipv6_virtual_router_ip):
        """
        Sets the ipv6_virtual_router_ip of this Subnet.
        For an IPv6-enabled subnet, this is the IPv6 address of the virtual router.

        Example: `2001:0db8:0123:1111:89ab:cdef:1234:5678`


        :param ipv6_virtual_router_ip: The ipv6_virtual_router_ip of this Subnet.
        :type: str
        """
        self._ipv6_virtual_router_ip = ipv6_virtual_router_ip

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Subnet.
        The subnet's current state.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Subnet.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Subnet.
        The subnet's current state.


        :param lifecycle_state: The lifecycle_state of this Subnet.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "UPDATING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def prohibit_internet_ingress(self):
        """
        Gets the prohibit_internet_ingress of this Subnet.
        Whether to disallow ingress internet traffic to VNICs within this subnet. Defaults to false.

        For IPV4, `prohibitInternetIngress` behaves similarly to `prohibitPublicIpOnVnic`.
        If it is set to false, VNICs created in this subnet will automatically be assigned public IP
        addresses unless specified otherwise during instance launch or VNIC creation (with the `assignPublicIp`
        flag in :class:`CreateVnicDetails`).
        If `prohibitInternetIngress` is set to true, VNICs created in this subnet cannot have public IP addresses
        (that is, it's a privatesubnet).

        For IPv6, if `prohibitInternetIngress` is set to `true`, internet access is not allowed for any
        IPv6s assigned to VNICs in the subnet. Otherwise, ingress internet traffic is allowed by default.

        Example: `true`


        :return: The prohibit_internet_ingress of this Subnet.
        :rtype: bool
        """
        return self._prohibit_internet_ingress

    @prohibit_internet_ingress.setter
    def prohibit_internet_ingress(self, prohibit_internet_ingress):
        """
        Sets the prohibit_internet_ingress of this Subnet.
        Whether to disallow ingress internet traffic to VNICs within this subnet. Defaults to false.

        For IPV4, `prohibitInternetIngress` behaves similarly to `prohibitPublicIpOnVnic`.
        If it is set to false, VNICs created in this subnet will automatically be assigned public IP
        addresses unless specified otherwise during instance launch or VNIC creation (with the `assignPublicIp`
        flag in :class:`CreateVnicDetails`).
        If `prohibitInternetIngress` is set to true, VNICs created in this subnet cannot have public IP addresses
        (that is, it's a privatesubnet).

        For IPv6, if `prohibitInternetIngress` is set to `true`, internet access is not allowed for any
        IPv6s assigned to VNICs in the subnet. Otherwise, ingress internet traffic is allowed by default.

        Example: `true`


        :param prohibit_internet_ingress: The prohibit_internet_ingress of this Subnet.
        :type: bool
        """
        self._prohibit_internet_ingress = prohibit_internet_ingress

    @property
    def prohibit_public_ip_on_vnic(self):
        """
        Gets the prohibit_public_ip_on_vnic of this Subnet.
        Whether VNICs within this subnet can have public IP addresses.
        Defaults to false, which means VNICs created in this subnet will
        automatically be assigned public IP addresses unless specified
        otherwise during instance launch or VNIC creation (with the
        `assignPublicIp` flag in
        :class:`CreateVnicDetails`).
        If `prohibitPublicIpOnVnic` is set to true, VNICs created in this
        subnet cannot have public IP addresses (that is, it's a private
        subnet).

        Example: `true`


        :return: The prohibit_public_ip_on_vnic of this Subnet.
        :rtype: bool
        """
        return self._prohibit_public_ip_on_vnic

    @prohibit_public_ip_on_vnic.setter
    def prohibit_public_ip_on_vnic(self, prohibit_public_ip_on_vnic):
        """
        Sets the prohibit_public_ip_on_vnic of this Subnet.
        Whether VNICs within this subnet can have public IP addresses.
        Defaults to false, which means VNICs created in this subnet will
        automatically be assigned public IP addresses unless specified
        otherwise during instance launch or VNIC creation (with the
        `assignPublicIp` flag in
        :class:`CreateVnicDetails`).
        If `prohibitPublicIpOnVnic` is set to true, VNICs created in this
        subnet cannot have public IP addresses (that is, it's a private
        subnet).

        Example: `true`


        :param prohibit_public_ip_on_vnic: The prohibit_public_ip_on_vnic of this Subnet.
        :type: bool
        """
        self._prohibit_public_ip_on_vnic = prohibit_public_ip_on_vnic

    @property
    def route_table_id(self):
        """
        **[Required]** Gets the route_table_id of this Subnet.
        The OCID of the route table that the subnet uses.


        :return: The route_table_id of this Subnet.
        :rtype: str
        """
        return self._route_table_id

    @route_table_id.setter
    def route_table_id(self, route_table_id):
        """
        Sets the route_table_id of this Subnet.
        The OCID of the route table that the subnet uses.


        :param route_table_id: The route_table_id of this Subnet.
        :type: str
        """
        self._route_table_id = route_table_id

    @property
    def security_list_ids(self):
        """
        Gets the security_list_ids of this Subnet.
        The OCIDs of the security list or lists that the subnet uses. Remember
        that security lists are associated *with the subnet*, but the
        rules are applied to the individual VNICs in the subnet.


        :return: The security_list_ids of this Subnet.
        :rtype: list[str]
        """
        return self._security_list_ids

    @security_list_ids.setter
    def security_list_ids(self, security_list_ids):
        """
        Sets the security_list_ids of this Subnet.
        The OCIDs of the security list or lists that the subnet uses. Remember
        that security lists are associated *with the subnet*, but the
        rules are applied to the individual VNICs in the subnet.


        :param security_list_ids: The security_list_ids of this Subnet.
        :type: list[str]
        """
        self._security_list_ids = security_list_ids

    @property
    def subnet_domain_name(self):
        """
        Gets the subnet_domain_name of this Subnet.
        The subnet's domain name, which consists of the subnet's DNS label,
        the VCN's DNS label, and the `oraclevcn.com` domain.

        For more information, see
        `DNS in Your Virtual Cloud Network`__.

        Example: `subnet123.vcn1.oraclevcn.com`

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/dns.htm


        :return: The subnet_domain_name of this Subnet.
        :rtype: str
        """
        return self._subnet_domain_name

    @subnet_domain_name.setter
    def subnet_domain_name(self, subnet_domain_name):
        """
        Sets the subnet_domain_name of this Subnet.
        The subnet's domain name, which consists of the subnet's DNS label,
        the VCN's DNS label, and the `oraclevcn.com` domain.

        For more information, see
        `DNS in Your Virtual Cloud Network`__.

        Example: `subnet123.vcn1.oraclevcn.com`

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/dns.htm


        :param subnet_domain_name: The subnet_domain_name of this Subnet.
        :type: str
        """
        self._subnet_domain_name = subnet_domain_name

    @property
    def time_created(self):
        """
        Gets the time_created of this Subnet.
        The date and time the subnet was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Subnet.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Subnet.
        The date and time the subnet was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Subnet.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this Subnet.
        The OCID of the VCN the subnet is in.


        :return: The vcn_id of this Subnet.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this Subnet.
        The OCID of the VCN the subnet is in.


        :param vcn_id: The vcn_id of this Subnet.
        :type: str
        """
        self._vcn_id = vcn_id

    @property
    def virtual_router_ip(self):
        """
        **[Required]** Gets the virtual_router_ip of this Subnet.
        The IP address of the virtual router.

        Example: `10.0.14.1`


        :return: The virtual_router_ip of this Subnet.
        :rtype: str
        """
        return self._virtual_router_ip

    @virtual_router_ip.setter
    def virtual_router_ip(self, virtual_router_ip):
        """
        Sets the virtual_router_ip of this Subnet.
        The IP address of the virtual router.

        Example: `10.0.14.1`


        :param virtual_router_ip: The virtual_router_ip of this Subnet.
        :type: str
        """
        self._virtual_router_ip = virtual_router_ip

    @property
    def virtual_router_mac(self):
        """
        **[Required]** Gets the virtual_router_mac of this Subnet.
        The MAC address of the virtual router.

        Example: `00:00:00:00:00:01`


        :return: The virtual_router_mac of this Subnet.
        :rtype: str
        """
        return self._virtual_router_mac

    @virtual_router_mac.setter
    def virtual_router_mac(self, virtual_router_mac):
        """
        Sets the virtual_router_mac of this Subnet.
        The MAC address of the virtual router.

        Example: `00:00:00:00:00:01`


        :param virtual_router_mac: The virtual_router_mac of this Subnet.
        :type: str
        """
        self._virtual_router_mac = virtual_router_mac

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
