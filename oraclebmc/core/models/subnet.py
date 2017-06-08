# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class Subnet(object):

    def __init__(self):

        self.swagger_types = {
            'availability_domain': 'str',
            'cidr_block': 'str',
            'compartment_id': 'str',
            'dhcp_options_id': 'str',
            'display_name': 'str',
            'dns_label': 'str',
            'id': 'str',
            'lifecycle_state': 'str',
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
            'dhcp_options_id': 'dhcpOptionsId',
            'display_name': 'displayName',
            'dns_label': 'dnsLabel',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
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
        self._dhcp_options_id = None
        self._display_name = None
        self._dns_label = None
        self._id = None
        self._lifecycle_state = None
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
        The subnet's Availability Domain.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this Subnet.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this Subnet.
        The subnet's Availability Domain.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this Subnet.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def cidr_block(self):
        """
        Gets the cidr_block of this Subnet.
        The subnet's CIDR block.

        Example: `172.16.1.0/24`


        :return: The cidr_block of this Subnet.
        :rtype: str
        """
        return self._cidr_block

    @cidr_block.setter
    def cidr_block(self, cidr_block):
        """
        Sets the cidr_block of this Subnet.
        The subnet's CIDR block.

        Example: `172.16.1.0/24`


        :param cidr_block: The cidr_block of this Subnet.
        :type: str
        """
        self._cidr_block = cidr_block

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this Subnet.
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
    def dhcp_options_id(self):
        """
        Gets the dhcp_options_id of this Subnet.
        The OCID of the set of DHCP options associated with the subnet.


        :return: The dhcp_options_id of this Subnet.
        :rtype: str
        """
        return self._dhcp_options_id

    @dhcp_options_id.setter
    def dhcp_options_id(self, dhcp_options_id):
        """
        Sets the dhcp_options_id of this Subnet.
        The OCID of the set of DHCP options associated with the subnet.


        :param dhcp_options_id: The dhcp_options_id of this Subnet.
        :type: str
        """
        self._dhcp_options_id = dhcp_options_id

    @property
    def display_name(self):
        """
        Gets the display_name of this Subnet.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :return: The display_name of this Subnet.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Subnet.
        A user-friendly name. Does not have to be unique, and it's changeable.


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
        within this subnet (e.g., `bminstance-1.subnet123.vcn1.oraclevcn.com`).
        Must be an alphanumeric string that begins with a letter and is unique within the VCN.
        The value cannot be changed.

        The absence of this parameter means the Internet and VCN Resolver
        will not resolve hostnames of instances in this subnet.

        For more information, see
        `DNS in Your Virtual Cloud Network`__.

        Example: `subnet123`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/dns.htm


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
        within this subnet (e.g., `bminstance-1.subnet123.vcn1.oraclevcn.com`).
        Must be an alphanumeric string that begins with a letter and is unique within the VCN.
        The value cannot be changed.

        The absence of this parameter means the Internet and VCN Resolver
        will not resolve hostnames of instances in this subnet.

        For more information, see
        `DNS in Your Virtual Cloud Network`__.

        Example: `subnet123`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/dns.htm


        :param dns_label: The dns_label of this Subnet.
        :type: str
        """
        self._dns_label = dns_label

    @property
    def id(self):
        """
        Gets the id of this Subnet.
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
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Subnet.
        The subnet's current state.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
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
        allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]
        if lifecycle_state not in allowed_values:
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def prohibit_public_ip_on_vnic(self):
        """
        Gets the prohibit_public_ip_on_vnic of this Subnet.
        Whether VNICs within this subnet can have public IP addresses.
        Defaults to false, which means VNICs created in this subnet will
        automatically be assigned public IP addresses unless specified
        otherwise during instance launch (with the `assignPublicIp` flag in
        :class:`CreateVnicDetails`).
        If `prohibitPublicIpOnVnic` is set to true, VNICs created in this
        subnet cannot have public IP addresses (i.e., it's a private
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
        otherwise during instance launch (with the `assignPublicIp` flag in
        :class:`CreateVnicDetails`).
        If `prohibitPublicIpOnVnic` is set to true, VNICs created in this
        subnet cannot have public IP addresses (i.e., it's a private
        subnet).

        Example: `true`


        :param prohibit_public_ip_on_vnic: The prohibit_public_ip_on_vnic of this Subnet.
        :type: bool
        """
        self._prohibit_public_ip_on_vnic = prohibit_public_ip_on_vnic

    @property
    def route_table_id(self):
        """
        Gets the route_table_id of this Subnet.
        The OCID of the route table the subnet is using.


        :return: The route_table_id of this Subnet.
        :rtype: str
        """
        return self._route_table_id

    @route_table_id.setter
    def route_table_id(self, route_table_id):
        """
        Sets the route_table_id of this Subnet.
        The OCID of the route table the subnet is using.


        :param route_table_id: The route_table_id of this Subnet.
        :type: str
        """
        self._route_table_id = route_table_id

    @property
    def security_list_ids(self):
        """
        Gets the security_list_ids of this Subnet.
        OCIDs for the security lists to use for VNICs in this subnet.


        :return: The security_list_ids of this Subnet.
        :rtype: list[str]
        """
        return self._security_list_ids

    @security_list_ids.setter
    def security_list_ids(self, security_list_ids):
        """
        Sets the security_list_ids of this Subnet.
        OCIDs for the security lists to use for VNICs in this subnet.


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

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/dns.htm


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

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/dns.htm


        :param subnet_domain_name: The subnet_domain_name of this Subnet.
        :type: str
        """
        self._subnet_domain_name = subnet_domain_name

    @property
    def time_created(self):
        """
        Gets the time_created of this Subnet.
        The date and time the subnet was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this Subnet.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Subnet.
        The date and time the subnet was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this Subnet.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def vcn_id(self):
        """
        Gets the vcn_id of this Subnet.
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
        Gets the virtual_router_ip of this Subnet.
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
        Gets the virtual_router_mac of this Subnet.
        The MAC address of the virtual router.

        Example: `00:00:17:B6:4D:DD`


        :return: The virtual_router_mac of this Subnet.
        :rtype: str
        """
        return self._virtual_router_mac

    @virtual_router_mac.setter
    def virtual_router_mac(self, virtual_router_mac):
        """
        Sets the virtual_router_mac of this Subnet.
        The MAC address of the virtual router.

        Example: `00:00:17:B6:4D:DD`


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
