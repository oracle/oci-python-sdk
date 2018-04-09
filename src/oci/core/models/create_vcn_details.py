# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateVcnDetails(object):
    """
    CreateVcnDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateVcnDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cidr_block:
            The value to assign to the cidr_block property of this CreateVcnDetails.
        :type cidr_block: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateVcnDetails.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateVcnDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CreateVcnDetails.
        :type display_name: str

        :param dns_label:
            The value to assign to the dns_label property of this CreateVcnDetails.
        :type dns_label: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateVcnDetails.
        :type freeform_tags: dict(str, str)

        """
        self.swagger_types = {
            'cidr_block': 'str',
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'dns_label': 'str',
            'freeform_tags': 'dict(str, str)'
        }

        self.attribute_map = {
            'cidr_block': 'cidrBlock',
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'dns_label': 'dnsLabel',
            'freeform_tags': 'freeformTags'
        }

        self._cidr_block = None
        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._dns_label = None
        self._freeform_tags = None

    @property
    def cidr_block(self):
        """
        **[Required]** Gets the cidr_block of this CreateVcnDetails.
        The CIDR IP address block of the VCN.

        Example: `172.16.0.0/16`


        :return: The cidr_block of this CreateVcnDetails.
        :rtype: str
        """
        return self._cidr_block

    @cidr_block.setter
    def cidr_block(self, cidr_block):
        """
        Sets the cidr_block of this CreateVcnDetails.
        The CIDR IP address block of the VCN.

        Example: `172.16.0.0/16`


        :param cidr_block: The cidr_block of this CreateVcnDetails.
        :type: str
        """
        self._cidr_block = cidr_block

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateVcnDetails.
        The OCID of the compartment to contain the VCN.


        :return: The compartment_id of this CreateVcnDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateVcnDetails.
        The OCID of the compartment to contain the VCN.


        :param compartment_id: The compartment_id of this CreateVcnDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateVcnDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateVcnDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateVcnDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateVcnDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateVcnDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this CreateVcnDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateVcnDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this CreateVcnDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def dns_label(self):
        """
        Gets the dns_label of this CreateVcnDetails.
        A DNS label for the VCN, used in conjunction with the VNIC's hostname and
        subnet's DNS label to form a fully qualified domain name (FQDN) for each VNIC
        within this subnet (for example, `bminstance-1.subnet123.vcn1.oraclevcn.com`).
        Not required to be unique, but it's a best practice to set unique DNS labels
        for VCNs in your tenancy. Must be an alphanumeric string that begins with a letter.
        The value cannot be changed.

        You must set this value if you want instances to be able to use hostnames to
        resolve other instances in the VCN. Otherwise the Internet and VCN Resolver
        will not work.

        For more information, see
        `DNS in Your Virtual Cloud Network`__.

        Example: `vcn1`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/dns.htm


        :return: The dns_label of this CreateVcnDetails.
        :rtype: str
        """
        return self._dns_label

    @dns_label.setter
    def dns_label(self, dns_label):
        """
        Sets the dns_label of this CreateVcnDetails.
        A DNS label for the VCN, used in conjunction with the VNIC's hostname and
        subnet's DNS label to form a fully qualified domain name (FQDN) for each VNIC
        within this subnet (for example, `bminstance-1.subnet123.vcn1.oraclevcn.com`).
        Not required to be unique, but it's a best practice to set unique DNS labels
        for VCNs in your tenancy. Must be an alphanumeric string that begins with a letter.
        The value cannot be changed.

        You must set this value if you want instances to be able to use hostnames to
        resolve other instances in the VCN. Otherwise the Internet and VCN Resolver
        will not work.

        For more information, see
        `DNS in Your Virtual Cloud Network`__.

        Example: `vcn1`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/dns.htm


        :param dns_label: The dns_label of this CreateVcnDetails.
        :type: str
        """
        self._dns_label = dns_label

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateVcnDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateVcnDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateVcnDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateVcnDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
