# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateSubnetDetails(object):
    """
    CreateSubnetDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateSubnetDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this CreateSubnetDetails.
        :type availability_domain: str

        :param cidr_block:
            The value to assign to the cidr_block property of this CreateSubnetDetails.
        :type cidr_block: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateSubnetDetails.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateSubnetDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param dhcp_options_id:
            The value to assign to the dhcp_options_id property of this CreateSubnetDetails.
        :type dhcp_options_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateSubnetDetails.
        :type display_name: str

        :param dns_label:
            The value to assign to the dns_label property of this CreateSubnetDetails.
        :type dns_label: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateSubnetDetails.
        :type freeform_tags: dict(str, str)

        :param prohibit_public_ip_on_vnic:
            The value to assign to the prohibit_public_ip_on_vnic property of this CreateSubnetDetails.
        :type prohibit_public_ip_on_vnic: bool

        :param route_table_id:
            The value to assign to the route_table_id property of this CreateSubnetDetails.
        :type route_table_id: str

        :param security_list_ids:
            The value to assign to the security_list_ids property of this CreateSubnetDetails.
        :type security_list_ids: list[str]

        :param vcn_id:
            The value to assign to the vcn_id property of this CreateSubnetDetails.
        :type vcn_id: str

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
            'prohibit_public_ip_on_vnic': 'bool',
            'route_table_id': 'str',
            'security_list_ids': 'list[str]',
            'vcn_id': 'str'
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
            'prohibit_public_ip_on_vnic': 'prohibitPublicIpOnVnic',
            'route_table_id': 'routeTableId',
            'security_list_ids': 'securityListIds',
            'vcn_id': 'vcnId'
        }

        self._availability_domain = None
        self._cidr_block = None
        self._compartment_id = None
        self._defined_tags = None
        self._dhcp_options_id = None
        self._display_name = None
        self._dns_label = None
        self._freeform_tags = None
        self._prohibit_public_ip_on_vnic = None
        self._route_table_id = None
        self._security_list_ids = None
        self._vcn_id = None

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this CreateSubnetDetails.
        The Availability Domain to contain the subnet.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this CreateSubnetDetails.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this CreateSubnetDetails.
        The Availability Domain to contain the subnet.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this CreateSubnetDetails.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def cidr_block(self):
        """
        **[Required]** Gets the cidr_block of this CreateSubnetDetails.
        The CIDR IP address range of the subnet.

        Example: `172.16.1.0/24`


        :return: The cidr_block of this CreateSubnetDetails.
        :rtype: str
        """
        return self._cidr_block

    @cidr_block.setter
    def cidr_block(self, cidr_block):
        """
        Sets the cidr_block of this CreateSubnetDetails.
        The CIDR IP address range of the subnet.

        Example: `172.16.1.0/24`


        :param cidr_block: The cidr_block of this CreateSubnetDetails.
        :type: str
        """
        self._cidr_block = cidr_block

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateSubnetDetails.
        The OCID of the compartment to contain the subnet.


        :return: The compartment_id of this CreateSubnetDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateSubnetDetails.
        The OCID of the compartment to contain the subnet.


        :param compartment_id: The compartment_id of this CreateSubnetDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateSubnetDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateSubnetDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateSubnetDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateSubnetDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def dhcp_options_id(self):
        """
        Gets the dhcp_options_id of this CreateSubnetDetails.
        The OCID of the set of DHCP options the subnet will use. If you don't
        provide a value, the subnet will use the VCN's default set of DHCP options.


        :return: The dhcp_options_id of this CreateSubnetDetails.
        :rtype: str
        """
        return self._dhcp_options_id

    @dhcp_options_id.setter
    def dhcp_options_id(self, dhcp_options_id):
        """
        Sets the dhcp_options_id of this CreateSubnetDetails.
        The OCID of the set of DHCP options the subnet will use. If you don't
        provide a value, the subnet will use the VCN's default set of DHCP options.


        :param dhcp_options_id: The dhcp_options_id of this CreateSubnetDetails.
        :type: str
        """
        self._dhcp_options_id = dhcp_options_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateSubnetDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this CreateSubnetDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateSubnetDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this CreateSubnetDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def dns_label(self):
        """
        Gets the dns_label of this CreateSubnetDetails.
        A DNS label for the subnet, used in conjunction with the VNIC's hostname and
        VCN's DNS label to form a fully qualified domain name (FQDN) for each VNIC
        within this subnet (for example, `bminstance-1.subnet123.vcn1.oraclevcn.com`).
        Must be an alphanumeric string that begins with a letter and is unique within the VCN.
        The value cannot be changed.

        This value must be set if you want to use the Internet and VCN Resolver to resolve the
        hostnames of instances in the subnet. It can only be set if the VCN itself
        was created with a DNS label.

        For more information, see
        `DNS in Your Virtual Cloud Network`__.

        Example: `subnet123`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/dns.htm


        :return: The dns_label of this CreateSubnetDetails.
        :rtype: str
        """
        return self._dns_label

    @dns_label.setter
    def dns_label(self, dns_label):
        """
        Sets the dns_label of this CreateSubnetDetails.
        A DNS label for the subnet, used in conjunction with the VNIC's hostname and
        VCN's DNS label to form a fully qualified domain name (FQDN) for each VNIC
        within this subnet (for example, `bminstance-1.subnet123.vcn1.oraclevcn.com`).
        Must be an alphanumeric string that begins with a letter and is unique within the VCN.
        The value cannot be changed.

        This value must be set if you want to use the Internet and VCN Resolver to resolve the
        hostnames of instances in the subnet. It can only be set if the VCN itself
        was created with a DNS label.

        For more information, see
        `DNS in Your Virtual Cloud Network`__.

        Example: `subnet123`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/dns.htm


        :param dns_label: The dns_label of this CreateSubnetDetails.
        :type: str
        """
        self._dns_label = dns_label

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateSubnetDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateSubnetDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateSubnetDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateSubnetDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def prohibit_public_ip_on_vnic(self):
        """
        Gets the prohibit_public_ip_on_vnic of this CreateSubnetDetails.
        Whether VNICs within this subnet can have public IP addresses.
        Defaults to false, which means VNICs created in this subnet will
        automatically be assigned public IP addresses unless specified
        otherwise during instance launch or VNIC creation (with the
        `assignPublicIp` flag in :class:`CreateVnicDetails`).
        If `prohibitPublicIpOnVnic` is set to true, VNICs created in this
        subnet cannot have public IP addresses (that is, it's a private
        subnet).

        Example: `true`


        :return: The prohibit_public_ip_on_vnic of this CreateSubnetDetails.
        :rtype: bool
        """
        return self._prohibit_public_ip_on_vnic

    @prohibit_public_ip_on_vnic.setter
    def prohibit_public_ip_on_vnic(self, prohibit_public_ip_on_vnic):
        """
        Sets the prohibit_public_ip_on_vnic of this CreateSubnetDetails.
        Whether VNICs within this subnet can have public IP addresses.
        Defaults to false, which means VNICs created in this subnet will
        automatically be assigned public IP addresses unless specified
        otherwise during instance launch or VNIC creation (with the
        `assignPublicIp` flag in :class:`CreateVnicDetails`).
        If `prohibitPublicIpOnVnic` is set to true, VNICs created in this
        subnet cannot have public IP addresses (that is, it's a private
        subnet).

        Example: `true`


        :param prohibit_public_ip_on_vnic: The prohibit_public_ip_on_vnic of this CreateSubnetDetails.
        :type: bool
        """
        self._prohibit_public_ip_on_vnic = prohibit_public_ip_on_vnic

    @property
    def route_table_id(self):
        """
        Gets the route_table_id of this CreateSubnetDetails.
        The OCID of the route table the subnet will use. If you don't provide a value,
        the subnet will use the VCN's default route table.


        :return: The route_table_id of this CreateSubnetDetails.
        :rtype: str
        """
        return self._route_table_id

    @route_table_id.setter
    def route_table_id(self, route_table_id):
        """
        Sets the route_table_id of this CreateSubnetDetails.
        The OCID of the route table the subnet will use. If you don't provide a value,
        the subnet will use the VCN's default route table.


        :param route_table_id: The route_table_id of this CreateSubnetDetails.
        :type: str
        """
        self._route_table_id = route_table_id

    @property
    def security_list_ids(self):
        """
        Gets the security_list_ids of this CreateSubnetDetails.
        OCIDs for the security lists to associate with the subnet. If you don't
        provide a value, the VCN's default security list will be associated with
        the subnet. Remember that security lists are associated at the subnet
        level, but the rules are applied to the individual VNICs in the subnet.


        :return: The security_list_ids of this CreateSubnetDetails.
        :rtype: list[str]
        """
        return self._security_list_ids

    @security_list_ids.setter
    def security_list_ids(self, security_list_ids):
        """
        Sets the security_list_ids of this CreateSubnetDetails.
        OCIDs for the security lists to associate with the subnet. If you don't
        provide a value, the VCN's default security list will be associated with
        the subnet. Remember that security lists are associated at the subnet
        level, but the rules are applied to the individual VNICs in the subnet.


        :param security_list_ids: The security_list_ids of this CreateSubnetDetails.
        :type: list[str]
        """
        self._security_list_ids = security_list_ids

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this CreateSubnetDetails.
        The OCID of the VCN to contain the subnet.


        :return: The vcn_id of this CreateSubnetDetails.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this CreateSubnetDetails.
        The OCID of the VCN to contain the subnet.


        :param vcn_id: The vcn_id of this CreateSubnetDetails.
        :type: str
        """
        self._vcn_id = vcn_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
