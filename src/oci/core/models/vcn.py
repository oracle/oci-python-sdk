# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Vcn(object):

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

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Vcn.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
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
        self._lifecycle_state = None
        self._time_created = None
        self._vcn_domain_name = None

    @property
    def cidr_block(self):
        """
        **[Required]** Gets the cidr_block of this Vcn.
        The CIDR IP address block of the VCN.

        Example: `172.16.0.0/16`


        :return: The cidr_block of this Vcn.
        :rtype: str
        """
        return self._cidr_block

    @cidr_block.setter
    def cidr_block(self, cidr_block):
        """
        Sets the cidr_block of this Vcn.
        The CIDR IP address block of the VCN.

        Example: `172.16.0.0/16`


        :param cidr_block: The cidr_block of this Vcn.
        :type: str
        """
        self._cidr_block = cidr_block

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Vcn.
        The OCID of the compartment containing the VCN.


        :return: The compartment_id of this Vcn.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Vcn.
        The OCID of the compartment containing the VCN.


        :param compartment_id: The compartment_id of this Vcn.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def default_dhcp_options_id(self):
        """
        Gets the default_dhcp_options_id of this Vcn.
        The OCID for the VCN's default set of DHCP options.


        :return: The default_dhcp_options_id of this Vcn.
        :rtype: str
        """
        return self._default_dhcp_options_id

    @default_dhcp_options_id.setter
    def default_dhcp_options_id(self, default_dhcp_options_id):
        """
        Sets the default_dhcp_options_id of this Vcn.
        The OCID for the VCN's default set of DHCP options.


        :param default_dhcp_options_id: The default_dhcp_options_id of this Vcn.
        :type: str
        """
        self._default_dhcp_options_id = default_dhcp_options_id

    @property
    def default_route_table_id(self):
        """
        Gets the default_route_table_id of this Vcn.
        The OCID for the VCN's default route table.


        :return: The default_route_table_id of this Vcn.
        :rtype: str
        """
        return self._default_route_table_id

    @default_route_table_id.setter
    def default_route_table_id(self, default_route_table_id):
        """
        Sets the default_route_table_id of this Vcn.
        The OCID for the VCN's default route table.


        :param default_route_table_id: The default_route_table_id of this Vcn.
        :type: str
        """
        self._default_route_table_id = default_route_table_id

    @property
    def default_security_list_id(self):
        """
        Gets the default_security_list_id of this Vcn.
        The OCID for the VCN's default security list.


        :return: The default_security_list_id of this Vcn.
        :rtype: str
        """
        return self._default_security_list_id

    @default_security_list_id.setter
    def default_security_list_id(self, default_security_list_id):
        """
        Sets the default_security_list_id of this Vcn.
        The OCID for the VCN's default security list.


        :param default_security_list_id: The default_security_list_id of this Vcn.
        :type: str
        """
        self._default_security_list_id = default_security_list_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Vcn.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Vcn.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Vcn.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


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

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/dns.htm


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

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/dns.htm


        :param dns_label: The dns_label of this Vcn.
        :type: str
        """
        self._dns_label = dns_label

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Vcn.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Vcn.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Vcn.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Vcn.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Vcn.
        The VCN's Oracle ID (OCID).


        :return: The id of this Vcn.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Vcn.
        The VCN's Oracle ID (OCID).


        :param id: The id of this Vcn.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Vcn.
        The VCN's current state.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


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
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this Vcn.
        The date and time the VCN was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this Vcn.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Vcn.
        The date and time the VCN was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


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

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/dns.htm


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

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/dns.htm


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
