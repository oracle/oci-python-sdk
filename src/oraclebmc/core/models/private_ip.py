# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class PrivateIp(object):

    def __init__(self):

        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
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
            'display_name': 'displayName',
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
        self._display_name = None
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
