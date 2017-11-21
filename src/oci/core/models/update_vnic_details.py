# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateVnicDetails(object):

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateVnicDetails object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateVnicDetails.
        :type display_name: str

        :param hostname_label:
            The value to assign to the hostname_label property of this UpdateVnicDetails.
        :type hostname_label: str

        :param skip_source_dest_check:
            The value to assign to the skip_source_dest_check property of this UpdateVnicDetails.
        :type skip_source_dest_check: bool

        """
        self.swagger_types = {
            'display_name': 'str',
            'hostname_label': 'str',
            'skip_source_dest_check': 'bool'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'hostname_label': 'hostnameLabel',
            'skip_source_dest_check': 'skipSourceDestCheck'
        }

        self._display_name = None
        self._hostname_label = None
        self._skip_source_dest_check = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateVnicDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :return: The display_name of this UpdateVnicDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateVnicDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :param display_name: The display_name of this UpdateVnicDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def hostname_label(self):
        """
        Gets the hostname_label of this UpdateVnicDetails.
        The hostname for the VNIC's primary private IP. Used for DNS. The value is the hostname
        portion of the primary private IP's fully qualified domain name (FQDN)
        (for example, `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`).
        Must be unique across all VNICs in the subnet and comply with
        `RFC 952`__ and
        `RFC 1123`__.
        The value appears in the :class:`Vnic` object and also the
        :class:`PrivateIp` object returned by
        :func:`list_private_ips` and
        :func:`get_private_ip`.

        For more information, see
        `DNS in Your Virtual Cloud Network`__.

        __ https://tools.ietf.org/html/rfc952
        __ https://tools.ietf.org/html/rfc1123
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/dns.htm


        :return: The hostname_label of this UpdateVnicDetails.
        :rtype: str
        """
        return self._hostname_label

    @hostname_label.setter
    def hostname_label(self, hostname_label):
        """
        Sets the hostname_label of this UpdateVnicDetails.
        The hostname for the VNIC's primary private IP. Used for DNS. The value is the hostname
        portion of the primary private IP's fully qualified domain name (FQDN)
        (for example, `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`).
        Must be unique across all VNICs in the subnet and comply with
        `RFC 952`__ and
        `RFC 1123`__.
        The value appears in the :class:`Vnic` object and also the
        :class:`PrivateIp` object returned by
        :func:`list_private_ips` and
        :func:`get_private_ip`.

        For more information, see
        `DNS in Your Virtual Cloud Network`__.

        __ https://tools.ietf.org/html/rfc952
        __ https://tools.ietf.org/html/rfc1123
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/dns.htm


        :param hostname_label: The hostname_label of this UpdateVnicDetails.
        :type: str
        """
        self._hostname_label = hostname_label

    @property
    def skip_source_dest_check(self):
        """
        Gets the skip_source_dest_check of this UpdateVnicDetails.
        Whether the source/destination check is disabled on the VNIC.
        Defaults to `false`, which means the check is performed. For information
        about why you would skip the source/destination check, see
        `Using a Private IP as a Route Target`__.

        Example: `true`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Tasks/managingroutetables.htm#privateip


        :return: The skip_source_dest_check of this UpdateVnicDetails.
        :rtype: bool
        """
        return self._skip_source_dest_check

    @skip_source_dest_check.setter
    def skip_source_dest_check(self, skip_source_dest_check):
        """
        Sets the skip_source_dest_check of this UpdateVnicDetails.
        Whether the source/destination check is disabled on the VNIC.
        Defaults to `false`, which means the check is performed. For information
        about why you would skip the source/destination check, see
        `Using a Private IP as a Route Target`__.

        Example: `true`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Tasks/managingroutetables.htm#privateip


        :param skip_source_dest_check: The skip_source_dest_check of this UpdateVnicDetails.
        :type: bool
        """
        self._skip_source_dest_check = skip_source_dest_check

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
