# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateIPSecTunnelBgpSessionDetails(object):
    """
    Details to modify an IPSec Tunnel's BGP session paramaters.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateIPSecTunnelBgpSessionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param oracle_interface_ip:
            The value to assign to the oracle_interface_ip property of this UpdateIPSecTunnelBgpSessionDetails.
        :type oracle_interface_ip: str

        :param customer_interface_ip:
            The value to assign to the customer_interface_ip property of this UpdateIPSecTunnelBgpSessionDetails.
        :type customer_interface_ip: str

        :param customer_bgp_asn:
            The value to assign to the customer_bgp_asn property of this UpdateIPSecTunnelBgpSessionDetails.
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
        Gets the oracle_interface_ip of this UpdateIPSecTunnelBgpSessionDetails.
        The IPv4 Address used in the BGP peering session for the Oracle router. Example: 10.0.0.1/31.


        :return: The oracle_interface_ip of this UpdateIPSecTunnelBgpSessionDetails.
        :rtype: str
        """
        return self._oracle_interface_ip

    @oracle_interface_ip.setter
    def oracle_interface_ip(self, oracle_interface_ip):
        """
        Sets the oracle_interface_ip of this UpdateIPSecTunnelBgpSessionDetails.
        The IPv4 Address used in the BGP peering session for the Oracle router. Example: 10.0.0.1/31.


        :param oracle_interface_ip: The oracle_interface_ip of this UpdateIPSecTunnelBgpSessionDetails.
        :type: str
        """
        self._oracle_interface_ip = oracle_interface_ip

    @property
    def customer_interface_ip(self):
        """
        Gets the customer_interface_ip of this UpdateIPSecTunnelBgpSessionDetails.
        The IPv4 Address used in the BGP peering session for the non-Oracle router. Example: 10.0.0.2/31.


        :return: The customer_interface_ip of this UpdateIPSecTunnelBgpSessionDetails.
        :rtype: str
        """
        return self._customer_interface_ip

    @customer_interface_ip.setter
    def customer_interface_ip(self, customer_interface_ip):
        """
        Sets the customer_interface_ip of this UpdateIPSecTunnelBgpSessionDetails.
        The IPv4 Address used in the BGP peering session for the non-Oracle router. Example: 10.0.0.2/31.


        :param customer_interface_ip: The customer_interface_ip of this UpdateIPSecTunnelBgpSessionDetails.
        :type: str
        """
        self._customer_interface_ip = customer_interface_ip

    @property
    def customer_bgp_asn(self):
        """
        Gets the customer_bgp_asn of this UpdateIPSecTunnelBgpSessionDetails.
        The value of the remote BGP ASN in asplain format, as a string. Example: 1587232876 (4 byte ASN) or 12345 (2 byte ASN).


        :return: The customer_bgp_asn of this UpdateIPSecTunnelBgpSessionDetails.
        :rtype: str
        """
        return self._customer_bgp_asn

    @customer_bgp_asn.setter
    def customer_bgp_asn(self, customer_bgp_asn):
        """
        Sets the customer_bgp_asn of this UpdateIPSecTunnelBgpSessionDetails.
        The value of the remote BGP ASN in asplain format, as a string. Example: 1587232876 (4 byte ASN) or 12345 (2 byte ASN).


        :param customer_bgp_asn: The customer_bgp_asn of this UpdateIPSecTunnelBgpSessionDetails.
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
