# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateIPSecTunnelBgpSessionDetails(object):
    """
    CreateIPSecTunnelBgpSessionDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateIPSecTunnelBgpSessionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param oracle_interface_ip:
            The value to assign to the oracle_interface_ip property of this CreateIPSecTunnelBgpSessionDetails.
        :type oracle_interface_ip: str

        :param customer_interface_ip:
            The value to assign to the customer_interface_ip property of this CreateIPSecTunnelBgpSessionDetails.
        :type customer_interface_ip: str

        :param customer_bgp_asn:
            The value to assign to the customer_bgp_asn property of this CreateIPSecTunnelBgpSessionDetails.
        :type customer_bgp_asn: str

        """
        self.swagger_types = {
            'oracle_interface_ip': 'str',
            'customer_interface_ip': 'str',
            'customer_bgp_asn': 'str'
        }

        self.attribute_map = {
            'oracle_interface_ip': 'oracleInterfaceIp',
            'customer_interface_ip': 'customerInterfaceIp',
            'customer_bgp_asn': 'customerBgpAsn'
        }

        self._oracle_interface_ip = None
        self._customer_interface_ip = None
        self._customer_bgp_asn = None

    @property
    def oracle_interface_ip(self):
        """
        Gets the oracle_interface_ip of this CreateIPSecTunnelBgpSessionDetails.
        The IP address for the Oracle end of the inside tunnel interface.

        If the tunnel's `routing` attribute is set to `BGP`
        (see :class:`IPSecConnectionTunnel`), this IP address
        is required and used for the tunnel's BGP session.

        If `routing` is instead set to `STATIC`, this IP address is optional. You can set this IP
        address to troubleshoot or monitor the tunnel.

        The value must be a /30 or /31.

        Example: `10.0.0.4/31`


        :return: The oracle_interface_ip of this CreateIPSecTunnelBgpSessionDetails.
        :rtype: str
        """
        return self._oracle_interface_ip

    @oracle_interface_ip.setter
    def oracle_interface_ip(self, oracle_interface_ip):
        """
        Sets the oracle_interface_ip of this CreateIPSecTunnelBgpSessionDetails.
        The IP address for the Oracle end of the inside tunnel interface.

        If the tunnel's `routing` attribute is set to `BGP`
        (see :class:`IPSecConnectionTunnel`), this IP address
        is required and used for the tunnel's BGP session.

        If `routing` is instead set to `STATIC`, this IP address is optional. You can set this IP
        address to troubleshoot or monitor the tunnel.

        The value must be a /30 or /31.

        Example: `10.0.0.4/31`


        :param oracle_interface_ip: The oracle_interface_ip of this CreateIPSecTunnelBgpSessionDetails.
        :type: str
        """
        self._oracle_interface_ip = oracle_interface_ip

    @property
    def customer_interface_ip(self):
        """
        Gets the customer_interface_ip of this CreateIPSecTunnelBgpSessionDetails.
        The IP address for the CPE end of the inside tunnel interface.

        If the tunnel's `routing` attribute is set to `BGP`
        (see :class:`IPSecConnectionTunnel`), this IP address
        is required and used for the tunnel's BGP session.

        If `routing` is instead set to `STATIC`, this IP address is optional. You can set this IP
        address to troubleshoot or monitor the tunnel.

        The value must be a /30 or /31.

        Example: `10.0.0.5/31`


        :return: The customer_interface_ip of this CreateIPSecTunnelBgpSessionDetails.
        :rtype: str
        """
        return self._customer_interface_ip

    @customer_interface_ip.setter
    def customer_interface_ip(self, customer_interface_ip):
        """
        Sets the customer_interface_ip of this CreateIPSecTunnelBgpSessionDetails.
        The IP address for the CPE end of the inside tunnel interface.

        If the tunnel's `routing` attribute is set to `BGP`
        (see :class:`IPSecConnectionTunnel`), this IP address
        is required and used for the tunnel's BGP session.

        If `routing` is instead set to `STATIC`, this IP address is optional. You can set this IP
        address to troubleshoot or monitor the tunnel.

        The value must be a /30 or /31.

        Example: `10.0.0.5/31`


        :param customer_interface_ip: The customer_interface_ip of this CreateIPSecTunnelBgpSessionDetails.
        :type: str
        """
        self._customer_interface_ip = customer_interface_ip

    @property
    def customer_bgp_asn(self):
        """
        Gets the customer_bgp_asn of this CreateIPSecTunnelBgpSessionDetails.
        If the tunnel's `routing` attribute is set to `BGP`
        (see :class:`IPSecConnectionTunnel`), this ASN
        is required and used for the tunnel's BGP session. This is the ASN of the network on the
        CPE end of the BGP session. Can be a 2-byte or 4-byte ASN. Uses \"asplain\" format.

        If the tunnel's `routing` attribute is set to `STATIC`, the `customerBgpAsn` must be null.

        Example: `12345` (2-byte) or `1587232876` (4-byte)


        :return: The customer_bgp_asn of this CreateIPSecTunnelBgpSessionDetails.
        :rtype: str
        """
        return self._customer_bgp_asn

    @customer_bgp_asn.setter
    def customer_bgp_asn(self, customer_bgp_asn):
        """
        Sets the customer_bgp_asn of this CreateIPSecTunnelBgpSessionDetails.
        If the tunnel's `routing` attribute is set to `BGP`
        (see :class:`IPSecConnectionTunnel`), this ASN
        is required and used for the tunnel's BGP session. This is the ASN of the network on the
        CPE end of the BGP session. Can be a 2-byte or 4-byte ASN. Uses \"asplain\" format.

        If the tunnel's `routing` attribute is set to `STATIC`, the `customerBgpAsn` must be null.

        Example: `12345` (2-byte) or `1587232876` (4-byte)


        :param customer_bgp_asn: The customer_bgp_asn of this CreateIPSecTunnelBgpSessionDetails.
        :type: str
        """
        self._customer_bgp_asn = customer_bgp_asn

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
