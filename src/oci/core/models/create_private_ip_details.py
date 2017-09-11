# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class CreatePrivateIpDetails(object):

    def __init__(self):

        self.swagger_types = {
            'display_name': 'str',
            'hostname_label': 'str',
            'ip_address': 'str',
            'vnic_id': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'hostname_label': 'hostnameLabel',
            'ip_address': 'ipAddress',
            'vnic_id': 'vnicId'
        }

        self._display_name = None
        self._hostname_label = None
        self._ip_address = None
        self._vnic_id = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreatePrivateIpDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid
        entering confidential information.


        :return: The display_name of this CreatePrivateIpDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreatePrivateIpDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid
        entering confidential information.


        :param display_name: The display_name of this CreatePrivateIpDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def hostname_label(self):
        """
        Gets the hostname_label of this CreatePrivateIpDetails.
        The hostname for the private IP. Used for DNS. The value
        is the hostname portion of the private IP's fully qualified domain name (FQDN)
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


        :return: The hostname_label of this CreatePrivateIpDetails.
        :rtype: str
        """
        return self._hostname_label

    @hostname_label.setter
    def hostname_label(self, hostname_label):
        """
        Sets the hostname_label of this CreatePrivateIpDetails.
        The hostname for the private IP. Used for DNS. The value
        is the hostname portion of the private IP's fully qualified domain name (FQDN)
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


        :param hostname_label: The hostname_label of this CreatePrivateIpDetails.
        :type: str
        """
        self._hostname_label = hostname_label

    @property
    def ip_address(self):
        """
        Gets the ip_address of this CreatePrivateIpDetails.
        A private IP address of your choice. Must be an available IP address within
        the subnet's CIDR. If you don't specify a value, Oracle automatically
        assigns a private IP address from the subnet.

        Example: `10.0.3.3`


        :return: The ip_address of this CreatePrivateIpDetails.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this CreatePrivateIpDetails.
        A private IP address of your choice. Must be an available IP address within
        the subnet's CIDR. If you don't specify a value, Oracle automatically
        assigns a private IP address from the subnet.

        Example: `10.0.3.3`


        :param ip_address: The ip_address of this CreatePrivateIpDetails.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def vnic_id(self):
        """
        Gets the vnic_id of this CreatePrivateIpDetails.
        The OCID of the VNIC to assign the private IP to. The VNIC and private IP
        must be in the same subnet.


        :return: The vnic_id of this CreatePrivateIpDetails.
        :rtype: str
        """
        return self._vnic_id

    @vnic_id.setter
    def vnic_id(self, vnic_id):
        """
        Sets the vnic_id of this CreatePrivateIpDetails.
        The OCID of the VNIC to assign the private IP to. The VNIC and private IP
        must be in the same subnet.


        :param vnic_id: The vnic_id of this CreatePrivateIpDetails.
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
