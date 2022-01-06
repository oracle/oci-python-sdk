# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PrivateAccessChannel(object):
    """
    Analytics Instance Private Access Channel model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PrivateAccessChannel object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this PrivateAccessChannel.
        :type key: str

        :param display_name:
            The value to assign to the display_name property of this PrivateAccessChannel.
        :type display_name: str

        :param vcn_id:
            The value to assign to the vcn_id property of this PrivateAccessChannel.
        :type vcn_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this PrivateAccessChannel.
        :type subnet_id: str

        :param ip_address:
            The value to assign to the ip_address property of this PrivateAccessChannel.
        :type ip_address: str

        :param egress_source_ip_addresses:
            The value to assign to the egress_source_ip_addresses property of this PrivateAccessChannel.
        :type egress_source_ip_addresses: list[str]

        :param private_source_dns_zones:
            The value to assign to the private_source_dns_zones property of this PrivateAccessChannel.
        :type private_source_dns_zones: list[oci.analytics.models.PrivateSourceDnsZone]

        """
        self.swagger_types = {
            'key': 'str',
            'display_name': 'str',
            'vcn_id': 'str',
            'subnet_id': 'str',
            'ip_address': 'str',
            'egress_source_ip_addresses': 'list[str]',
            'private_source_dns_zones': 'list[PrivateSourceDnsZone]'
        }

        self.attribute_map = {
            'key': 'key',
            'display_name': 'displayName',
            'vcn_id': 'vcnId',
            'subnet_id': 'subnetId',
            'ip_address': 'ipAddress',
            'egress_source_ip_addresses': 'egressSourceIpAddresses',
            'private_source_dns_zones': 'privateSourceDnsZones'
        }

        self._key = None
        self._display_name = None
        self._vcn_id = None
        self._subnet_id = None
        self._ip_address = None
        self._egress_source_ip_addresses = None
        self._private_source_dns_zones = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this PrivateAccessChannel.
        Private Access Channel unique identifier key.


        :return: The key of this PrivateAccessChannel.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this PrivateAccessChannel.
        Private Access Channel unique identifier key.


        :param key: The key of this PrivateAccessChannel.
        :type: str
        """
        self._key = key

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this PrivateAccessChannel.
        Display Name of the Private Access Channel.


        :return: The display_name of this PrivateAccessChannel.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this PrivateAccessChannel.
        Display Name of the Private Access Channel.


        :param display_name: The display_name of this PrivateAccessChannel.
        :type: str
        """
        self._display_name = display_name

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this PrivateAccessChannel.
        OCID of the customer VCN peered with private access channel.


        :return: The vcn_id of this PrivateAccessChannel.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this PrivateAccessChannel.
        OCID of the customer VCN peered with private access channel.


        :param vcn_id: The vcn_id of this PrivateAccessChannel.
        :type: str
        """
        self._vcn_id = vcn_id

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this PrivateAccessChannel.
        OCID of the customer subnet connected to private access channel.


        :return: The subnet_id of this PrivateAccessChannel.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this PrivateAccessChannel.
        OCID of the customer subnet connected to private access channel.


        :param subnet_id: The subnet_id of this PrivateAccessChannel.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def ip_address(self):
        """
        **[Required]** Gets the ip_address of this PrivateAccessChannel.
        IP Address of the Private Access channel.


        :return: The ip_address of this PrivateAccessChannel.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this PrivateAccessChannel.
        IP Address of the Private Access channel.


        :param ip_address: The ip_address of this PrivateAccessChannel.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def egress_source_ip_addresses(self):
        """
        **[Required]** Gets the egress_source_ip_addresses of this PrivateAccessChannel.
        The list of IP addresses from the customer subnet connected to private access channel, used as a source Ip by Private Access Channel
        for network traffic from the AnalyticsInstance to Private Sources.


        :return: The egress_source_ip_addresses of this PrivateAccessChannel.
        :rtype: list[str]
        """
        return self._egress_source_ip_addresses

    @egress_source_ip_addresses.setter
    def egress_source_ip_addresses(self, egress_source_ip_addresses):
        """
        Sets the egress_source_ip_addresses of this PrivateAccessChannel.
        The list of IP addresses from the customer subnet connected to private access channel, used as a source Ip by Private Access Channel
        for network traffic from the AnalyticsInstance to Private Sources.


        :param egress_source_ip_addresses: The egress_source_ip_addresses of this PrivateAccessChannel.
        :type: list[str]
        """
        self._egress_source_ip_addresses = egress_source_ip_addresses

    @property
    def private_source_dns_zones(self):
        """
        Gets the private_source_dns_zones of this PrivateAccessChannel.
        List of Private Source DNS zones registered with Private Access Channel,
        where datasource hostnames from these dns zones / domains will be resolved in the peered VCN for access from Analytics Instance.
        Min of 1 is required and Max of 30 Private Source DNS zones can be registered.


        :return: The private_source_dns_zones of this PrivateAccessChannel.
        :rtype: list[oci.analytics.models.PrivateSourceDnsZone]
        """
        return self._private_source_dns_zones

    @private_source_dns_zones.setter
    def private_source_dns_zones(self, private_source_dns_zones):
        """
        Sets the private_source_dns_zones of this PrivateAccessChannel.
        List of Private Source DNS zones registered with Private Access Channel,
        where datasource hostnames from these dns zones / domains will be resolved in the peered VCN for access from Analytics Instance.
        Min of 1 is required and Max of 30 Private Source DNS zones can be registered.


        :param private_source_dns_zones: The private_source_dns_zones of this PrivateAccessChannel.
        :type: list[oci.analytics.models.PrivateSourceDnsZone]
        """
        self._private_source_dns_zones = private_source_dns_zones

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
