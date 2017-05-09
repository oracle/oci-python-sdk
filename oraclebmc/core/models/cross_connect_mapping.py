# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class CrossConnectMapping(object):

    def __init__(self):

        self.swagger_types = {
            'bgp_md5_auth_key': 'str',
            'cross_connect_or_cross_connect_group_id': 'str',
            'customer_bgp_peering_ip': 'str',
            'oracle_bgp_peering_ip': 'str',
            'vlan': 'int'
        }

        self.attribute_map = {
            'bgp_md5_auth_key': 'bgpMd5AuthKey',
            'cross_connect_or_cross_connect_group_id': 'crossConnectOrCrossConnectGroupId',
            'customer_bgp_peering_ip': 'customerBgpPeeringIp',
            'oracle_bgp_peering_ip': 'oracleBgpPeeringIp',
            'vlan': 'vlan'
        }

        self._bgp_md5_auth_key = None
        self._cross_connect_or_cross_connect_group_id = None
        self._customer_bgp_peering_ip = None
        self._oracle_bgp_peering_ip = None
        self._vlan = None

    @property
    def bgp_md5_auth_key(self):
        """
        Gets the bgp_md5_auth_key of this CrossConnectMapping.
        The key for BGP MD5 authentication. Only applicable if your system
        requires MD5 authentication. If empty or not set (null), that
        means you don't use BGP MD5 authentication.


        :return: The bgp_md5_auth_key of this CrossConnectMapping.
        :rtype: str
        """
        return self._bgp_md5_auth_key

    @bgp_md5_auth_key.setter
    def bgp_md5_auth_key(self, bgp_md5_auth_key):
        """
        Sets the bgp_md5_auth_key of this CrossConnectMapping.
        The key for BGP MD5 authentication. Only applicable if your system
        requires MD5 authentication. If empty or not set (null), that
        means you don't use BGP MD5 authentication.


        :param bgp_md5_auth_key: The bgp_md5_auth_key of this CrossConnectMapping.
        :type: str
        """
        self._bgp_md5_auth_key = bgp_md5_auth_key

    @property
    def cross_connect_or_cross_connect_group_id(self):
        """
        Gets the cross_connect_or_cross_connect_group_id of this CrossConnectMapping.
        The OCID of the cross-connect or cross-connect group for this mapping.
        Specified by the owner of the cross-connect or cross-connect group (the
        customer if the customer is colocated with Oracle; the provider if the
        customer is connecting via provider).


        :return: The cross_connect_or_cross_connect_group_id of this CrossConnectMapping.
        :rtype: str
        """
        return self._cross_connect_or_cross_connect_group_id

    @cross_connect_or_cross_connect_group_id.setter
    def cross_connect_or_cross_connect_group_id(self, cross_connect_or_cross_connect_group_id):
        """
        Sets the cross_connect_or_cross_connect_group_id of this CrossConnectMapping.
        The OCID of the cross-connect or cross-connect group for this mapping.
        Specified by the owner of the cross-connect or cross-connect group (the
        customer if the customer is colocated with Oracle; the provider if the
        customer is connecting via provider).


        :param cross_connect_or_cross_connect_group_id: The cross_connect_or_cross_connect_group_id of this CrossConnectMapping.
        :type: str
        """
        self._cross_connect_or_cross_connect_group_id = cross_connect_or_cross_connect_group_id

    @property
    def customer_bgp_peering_ip(self):
        """
        Gets the customer_bgp_peering_ip of this CrossConnectMapping.
        The BGP IP address for the router on the other end of the BGP session from
        Oracle. Specified by the owner of that router. If the session goes from Oracle
        to a customer, this is the BGP IP address of the customer's edge router. If the
        session goes from Oracle to a provider, this is the BGP IP address of the
        provider's edge router. Must use a /30 or /31 subnet mask.

        Example: `10.0.0.18/31`


        :return: The customer_bgp_peering_ip of this CrossConnectMapping.
        :rtype: str
        """
        return self._customer_bgp_peering_ip

    @customer_bgp_peering_ip.setter
    def customer_bgp_peering_ip(self, customer_bgp_peering_ip):
        """
        Sets the customer_bgp_peering_ip of this CrossConnectMapping.
        The BGP IP address for the router on the other end of the BGP session from
        Oracle. Specified by the owner of that router. If the session goes from Oracle
        to a customer, this is the BGP IP address of the customer's edge router. If the
        session goes from Oracle to a provider, this is the BGP IP address of the
        provider's edge router. Must use a /30 or /31 subnet mask.

        Example: `10.0.0.18/31`


        :param customer_bgp_peering_ip: The customer_bgp_peering_ip of this CrossConnectMapping.
        :type: str
        """
        self._customer_bgp_peering_ip = customer_bgp_peering_ip

    @property
    def oracle_bgp_peering_ip(self):
        """
        Gets the oracle_bgp_peering_ip of this CrossConnectMapping.
        The IP address for Oracle's end of the BPG session. Must use a /30 or /31
        subnet mask. If the session goes from Oracle to a customer's edge router,
        the customer specifies this information. If the session goes from Oracle to
        a provider's edge router, the provider specifies this.

        Example: `10.0.0.19/31`


        :return: The oracle_bgp_peering_ip of this CrossConnectMapping.
        :rtype: str
        """
        return self._oracle_bgp_peering_ip

    @oracle_bgp_peering_ip.setter
    def oracle_bgp_peering_ip(self, oracle_bgp_peering_ip):
        """
        Sets the oracle_bgp_peering_ip of this CrossConnectMapping.
        The IP address for Oracle's end of the BPG session. Must use a /30 or /31
        subnet mask. If the session goes from Oracle to a customer's edge router,
        the customer specifies this information. If the session goes from Oracle to
        a provider's edge router, the provider specifies this.

        Example: `10.0.0.19/31`


        :param oracle_bgp_peering_ip: The oracle_bgp_peering_ip of this CrossConnectMapping.
        :type: str
        """
        self._oracle_bgp_peering_ip = oracle_bgp_peering_ip

    @property
    def vlan(self):
        """
        Gets the vlan of this CrossConnectMapping.
        The number of the specific VLAN (on the cross-connect or cross-connect group)
        that is assigned to this virtual circuit. Specified by the owner of the cross-connect
        or cross-connect group (the customer if the customer is colocated with Oracle, or
        the provider if the customer is connecting via provider).

        Example: `200`


        :return: The vlan of this CrossConnectMapping.
        :rtype: int
        """
        return self._vlan

    @vlan.setter
    def vlan(self, vlan):
        """
        Sets the vlan of this CrossConnectMapping.
        The number of the specific VLAN (on the cross-connect or cross-connect group)
        that is assigned to this virtual circuit. Specified by the owner of the cross-connect
        or cross-connect group (the customer if the customer is colocated with Oracle, or
        the provider if the customer is connecting via provider).

        Example: `200`


        :param vlan: The vlan of this CrossConnectMapping.
        :type: int
        """
        self._vlan = vlan

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
