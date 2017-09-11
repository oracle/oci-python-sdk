# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class UpdatePrivateIpDetails(object):

    def __init__(self):

        self.swagger_types = {
            'display_name': 'str',
            'hostname_label': 'str',
            'vnic_id': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'hostname_label': 'hostnameLabel',
            'vnic_id': 'vnicId'
        }

        self._display_name = None
        self._hostname_label = None
        self._vnic_id = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdatePrivateIpDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid
        entering confidential information.


        :return: The display_name of this UpdatePrivateIpDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdatePrivateIpDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid
        entering confidential information.


        :param display_name: The display_name of this UpdatePrivateIpDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def hostname_label(self):
        """
        Gets the hostname_label of this UpdatePrivateIpDetails.
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


        :return: The hostname_label of this UpdatePrivateIpDetails.
        :rtype: str
        """
        return self._hostname_label

    @hostname_label.setter
    def hostname_label(self, hostname_label):
        """
        Sets the hostname_label of this UpdatePrivateIpDetails.
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


        :param hostname_label: The hostname_label of this UpdatePrivateIpDetails.
        :type: str
        """
        self._hostname_label = hostname_label

    @property
    def vnic_id(self):
        """
        Gets the vnic_id of this UpdatePrivateIpDetails.
        The OCID of the VNIC to reassign the private IP to. The VNIC must
        be in the same subnet as the current VNIC.


        :return: The vnic_id of this UpdatePrivateIpDetails.
        :rtype: str
        """
        return self._vnic_id

    @vnic_id.setter
    def vnic_id(self, vnic_id):
        """
        Sets the vnic_id of this UpdatePrivateIpDetails.
        The OCID of the VNIC to reassign the private IP to. The VNIC must
        be in the same subnet as the current VNIC.


        :param vnic_id: The vnic_id of this UpdatePrivateIpDetails.
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
