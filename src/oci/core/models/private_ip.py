# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PrivateIp(object):

    def __init__(self, **kwargs):
        """
        Initializes a new PrivateIp object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this PrivateIp.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this PrivateIp.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this PrivateIp.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this PrivateIp.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this PrivateIp.
        :type freeform_tags: dict(str, str)

        :param hostname_label:
            The value to assign to the hostname_label property of this PrivateIp.
        :type hostname_label: str

        :param id:
            The value to assign to the id property of this PrivateIp.
        :type id: str

        :param ip_address:
            The value to assign to the ip_address property of this PrivateIp.
        :type ip_address: str

        :param is_primary:
            The value to assign to the is_primary property of this PrivateIp.
        :type is_primary: bool

        :param subnet_id:
            The value to assign to the subnet_id property of this PrivateIp.
        :type subnet_id: str

        :param time_created:
            The value to assign to the time_created property of this PrivateIp.
        :type time_created: datetime

        :param vnic_id:
            The value to assign to the vnic_id property of this PrivateIp.
        :type vnic_id: str

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'hostname_label': 'str',
            'id': 'str',
            'ip_address': 'str',
            'is_primary': 'bool',
            'subnet_id': 'str',
            'time_created': 'datetime',
            'vnic_id': 'str'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'hostname_label': 'hostnameLabel',
            'id': 'id',
            'ip_address': 'ipAddress',
            'is_primary': 'isPrimary',
            'subnet_id': 'subnetId',
            'time_created': 'timeCreated',
            'vnic_id': 'vnicId'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._hostname_label = None
        self._id = None
        self._ip_address = None
        self._is_primary = None
        self._subnet_id = None
        self._time_created = None
        self._vnic_id = None

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this PrivateIp.
        The private IP's Availability Domain.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this PrivateIp.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this PrivateIp.
        The private IP's Availability Domain.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this PrivateIp.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this PrivateIp.
        The OCID of the compartment containing the private IP.


        :return: The compartment_id of this PrivateIp.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this PrivateIp.
        The OCID of the compartment containing the private IP.


        :param compartment_id: The compartment_id of this PrivateIp.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this PrivateIp.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this PrivateIp.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this PrivateIp.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this PrivateIp.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this PrivateIp.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid
        entering confidential information.


        :return: The display_name of this PrivateIp.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this PrivateIp.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid
        entering confidential information.


        :param display_name: The display_name of this PrivateIp.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this PrivateIp.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this PrivateIp.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this PrivateIp.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this PrivateIp.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def hostname_label(self):
        """
        Gets the hostname_label of this PrivateIp.
        The hostname for the private IP. Used for DNS. The value is the hostname
        portion of the private IP's fully qualified domain name (FQDN)
        (for example, `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`).
        Must be unique across all VNICs in the subnet and comply with
        `RFC 952`__ and
        `RFC 1123`__.

        For more information, see
        `DNS in Your Virtual Cloud Network`__.

        Example: `bminstance-1`

        __ https://tools.ietf.org/html/rfc952
        __ https://tools.ietf.org/html/rfc1123
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/dns.htm


        :return: The hostname_label of this PrivateIp.
        :rtype: str
        """
        return self._hostname_label

    @hostname_label.setter
    def hostname_label(self, hostname_label):
        """
        Sets the hostname_label of this PrivateIp.
        The hostname for the private IP. Used for DNS. The value is the hostname
        portion of the private IP's fully qualified domain name (FQDN)
        (for example, `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`).
        Must be unique across all VNICs in the subnet and comply with
        `RFC 952`__ and
        `RFC 1123`__.

        For more information, see
        `DNS in Your Virtual Cloud Network`__.

        Example: `bminstance-1`

        __ https://tools.ietf.org/html/rfc952
        __ https://tools.ietf.org/html/rfc1123
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/dns.htm


        :param hostname_label: The hostname_label of this PrivateIp.
        :type: str
        """
        self._hostname_label = hostname_label

    @property
    def id(self):
        """
        Gets the id of this PrivateIp.
        The private IP's Oracle ID (OCID).


        :return: The id of this PrivateIp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PrivateIp.
        The private IP's Oracle ID (OCID).


        :param id: The id of this PrivateIp.
        :type: str
        """
        self._id = id

    @property
    def ip_address(self):
        """
        Gets the ip_address of this PrivateIp.
        The private IP address of the `privateIp` object. The address is within the CIDR
        of the VNIC's subnet.

        Example: `10.0.3.3`


        :return: The ip_address of this PrivateIp.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this PrivateIp.
        The private IP address of the `privateIp` object. The address is within the CIDR
        of the VNIC's subnet.

        Example: `10.0.3.3`


        :param ip_address: The ip_address of this PrivateIp.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def is_primary(self):
        """
        Gets the is_primary of this PrivateIp.
        Whether this private IP is the primary one on the VNIC. Primary private IPs
        are unassigned and deleted automatically when the VNIC is terminated.

        Example: `true`


        :return: The is_primary of this PrivateIp.
        :rtype: bool
        """
        return self._is_primary

    @is_primary.setter
    def is_primary(self, is_primary):
        """
        Sets the is_primary of this PrivateIp.
        Whether this private IP is the primary one on the VNIC. Primary private IPs
        are unassigned and deleted automatically when the VNIC is terminated.

        Example: `true`


        :param is_primary: The is_primary of this PrivateIp.
        :type: bool
        """
        self._is_primary = is_primary

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this PrivateIp.
        The OCID of the subnet the VNIC is in.


        :return: The subnet_id of this PrivateIp.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this PrivateIp.
        The OCID of the subnet the VNIC is in.


        :param subnet_id: The subnet_id of this PrivateIp.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def time_created(self):
        """
        Gets the time_created of this PrivateIp.
        The date and time the private IP was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this PrivateIp.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this PrivateIp.
        The date and time the private IP was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this PrivateIp.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def vnic_id(self):
        """
        Gets the vnic_id of this PrivateIp.
        The OCID of the VNIC the private IP is assigned to. The VNIC and private IP
        must be in the same subnet.


        :return: The vnic_id of this PrivateIp.
        :rtype: str
        """
        return self._vnic_id

    @vnic_id.setter
    def vnic_id(self, vnic_id):
        """
        Sets the vnic_id of this PrivateIp.
        The OCID of the VNIC the private IP is assigned to. The VNIC and private IP
        must be in the same subnet.


        :param vnic_id: The vnic_id of this PrivateIp.
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
