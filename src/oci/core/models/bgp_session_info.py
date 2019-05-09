# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BgpSessionInfo(object):
    """
    Information needed to establish a BGP Session on an interface.
    """

    #: A constant which can be used with the bgp_state property of a BgpSessionInfo.
    #: This constant has a value of "UP"
    BGP_STATE_UP = "UP"

    #: A constant which can be used with the bgp_state property of a BgpSessionInfo.
    #: This constant has a value of "DOWN"
    BGP_STATE_DOWN = "DOWN"

    def __init__(self, **kwargs):
        """
        Initializes a new BgpSessionInfo object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param oracle_interface_ip:
            The value to assign to the oracle_interface_ip property of this BgpSessionInfo.
        :type oracle_interface_ip: str

        :param customer_interface_ip:
            The value to assign to the customer_interface_ip property of this BgpSessionInfo.
        :type customer_interface_ip: str

        :param oracle_bgp_asn:
            The value to assign to the oracle_bgp_asn property of this BgpSessionInfo.
        :type oracle_bgp_asn: str

        :param customer_bgp_asn:
            The value to assign to the customer_bgp_asn property of this BgpSessionInfo.
        :type customer_bgp_asn: str

        :param bgp_state:
            The value to assign to the bgp_state property of this BgpSessionInfo.
            Allowed values for this property are: "UP", "DOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type bgp_state: str

        """
        self.swagger_types = {
            'oracle_interface_ip': 'str',
            'customer_interface_ip': 'str',
            'oracle_bgp_asn': 'str',
            'customer_bgp_asn': 'str',
            'bgp_state': 'str'
        }

        self.attribute_map = {
            'oracle_interface_ip': 'oracleInterfaceIp',
            'customer_interface_ip': 'customerInterfaceIp',
            'oracle_bgp_asn': 'oracleBgpAsn',
            'customer_bgp_asn': 'customerBgpAsn',
            'bgp_state': 'bgpState'
        }

        self._oracle_interface_ip = None
        self._customer_interface_ip = None
        self._oracle_bgp_asn = None
        self._customer_bgp_asn = None
        self._bgp_state = None

    @property
    def oracle_interface_ip(self):
        """
        Gets the oracle_interface_ip of this BgpSessionInfo.
        This is the IPv4 Address used in the BGP peering session for the Oracle router. Example: 10.0.0.1/31


        :return: The oracle_interface_ip of this BgpSessionInfo.
        :rtype: str
        """
        return self._oracle_interface_ip

    @oracle_interface_ip.setter
    def oracle_interface_ip(self, oracle_interface_ip):
        """
        Sets the oracle_interface_ip of this BgpSessionInfo.
        This is the IPv4 Address used in the BGP peering session for the Oracle router. Example: 10.0.0.1/31


        :param oracle_interface_ip: The oracle_interface_ip of this BgpSessionInfo.
        :type: str
        """
        self._oracle_interface_ip = oracle_interface_ip

    @property
    def customer_interface_ip(self):
        """
        Gets the customer_interface_ip of this BgpSessionInfo.
        This is the IPv4 Address used in the BGP peering session for the non-Oracle router. Example: 10.0.0.2/31


        :return: The customer_interface_ip of this BgpSessionInfo.
        :rtype: str
        """
        return self._customer_interface_ip

    @customer_interface_ip.setter
    def customer_interface_ip(self, customer_interface_ip):
        """
        Sets the customer_interface_ip of this BgpSessionInfo.
        This is the IPv4 Address used in the BGP peering session for the non-Oracle router. Example: 10.0.0.2/31


        :param customer_interface_ip: The customer_interface_ip of this BgpSessionInfo.
        :type: str
        """
        self._customer_interface_ip = customer_interface_ip

    @property
    def oracle_bgp_asn(self):
        """
        Gets the oracle_bgp_asn of this BgpSessionInfo.
        This is the value of the Oracle Bgp ASN in asplain format, as a string. Example: 1587232876 (4 byte ASN) or 12345 (2 byte ASN)


        :return: The oracle_bgp_asn of this BgpSessionInfo.
        :rtype: str
        """
        return self._oracle_bgp_asn

    @oracle_bgp_asn.setter
    def oracle_bgp_asn(self, oracle_bgp_asn):
        """
        Sets the oracle_bgp_asn of this BgpSessionInfo.
        This is the value of the Oracle Bgp ASN in asplain format, as a string. Example: 1587232876 (4 byte ASN) or 12345 (2 byte ASN)


        :param oracle_bgp_asn: The oracle_bgp_asn of this BgpSessionInfo.
        :type: str
        """
        self._oracle_bgp_asn = oracle_bgp_asn

    @property
    def customer_bgp_asn(self):
        """
        Gets the customer_bgp_asn of this BgpSessionInfo.
        This is the value of the remote Bgp ASN in asplain format, as a string. Example: 1587232876 (4 byte ASN) or 12345 (2 byte ASN)


        :return: The customer_bgp_asn of this BgpSessionInfo.
        :rtype: str
        """
        return self._customer_bgp_asn

    @customer_bgp_asn.setter
    def customer_bgp_asn(self, customer_bgp_asn):
        """
        Sets the customer_bgp_asn of this BgpSessionInfo.
        This is the value of the remote Bgp ASN in asplain format, as a string. Example: 1587232876 (4 byte ASN) or 12345 (2 byte ASN)


        :param customer_bgp_asn: The customer_bgp_asn of this BgpSessionInfo.
        :type: str
        """
        self._customer_bgp_asn = customer_bgp_asn

    @property
    def bgp_state(self):
        """
        Gets the bgp_state of this BgpSessionInfo.
        the state of the BGP.

        Allowed values for this property are: "UP", "DOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The bgp_state of this BgpSessionInfo.
        :rtype: str
        """
        return self._bgp_state

    @bgp_state.setter
    def bgp_state(self, bgp_state):
        """
        Sets the bgp_state of this BgpSessionInfo.
        the state of the BGP.


        :param bgp_state: The bgp_state of this BgpSessionInfo.
        :type: str
        """
        allowed_values = ["UP", "DOWN"]
        if not value_allowed_none_or_none_sentinel(bgp_state, allowed_values):
            bgp_state = 'UNKNOWN_ENUM_VALUE'
        self._bgp_state = bgp_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
