# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateIPSecTunnelEncryptionDomainDetails(object):
    """
    Request to update a multi-encryption domain policy on the VPNaaS tunnel.
    There can't be more than 50 security associations in use at one time. See `Encryption domain for policy-based
    tunnels`__ for more.

    __ https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/ipsecencryptiondomains.htm#spi_policy_based_tunnel
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateIPSecTunnelEncryptionDomainDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param oracle_traffic_selector:
            The value to assign to the oracle_traffic_selector property of this UpdateIPSecTunnelEncryptionDomainDetails.
        :type oracle_traffic_selector: list[str]

        :param cpe_traffic_selector:
            The value to assign to the cpe_traffic_selector property of this UpdateIPSecTunnelEncryptionDomainDetails.
        :type cpe_traffic_selector: list[str]

        """
        self.swagger_types = {
            'oracle_traffic_selector': 'list[str]',
            'cpe_traffic_selector': 'list[str]'
        }

        self.attribute_map = {
            'oracle_traffic_selector': 'oracleTrafficSelector',
            'cpe_traffic_selector': 'cpeTrafficSelector'
        }

        self._oracle_traffic_selector = None
        self._cpe_traffic_selector = None

    @property
    def oracle_traffic_selector(self):
        """
        Gets the oracle_traffic_selector of this UpdateIPSecTunnelEncryptionDomainDetails.
        Lists IPv4 or IPv6-enabled subnets in your Oracle tenancy.


        :return: The oracle_traffic_selector of this UpdateIPSecTunnelEncryptionDomainDetails.
        :rtype: list[str]
        """
        return self._oracle_traffic_selector

    @oracle_traffic_selector.setter
    def oracle_traffic_selector(self, oracle_traffic_selector):
        """
        Sets the oracle_traffic_selector of this UpdateIPSecTunnelEncryptionDomainDetails.
        Lists IPv4 or IPv6-enabled subnets in your Oracle tenancy.


        :param oracle_traffic_selector: The oracle_traffic_selector of this UpdateIPSecTunnelEncryptionDomainDetails.
        :type: list[str]
        """
        self._oracle_traffic_selector = oracle_traffic_selector

    @property
    def cpe_traffic_selector(self):
        """
        Gets the cpe_traffic_selector of this UpdateIPSecTunnelEncryptionDomainDetails.
        Lists IPv4 or IPv6-enabled subnets in your on-premises network.


        :return: The cpe_traffic_selector of this UpdateIPSecTunnelEncryptionDomainDetails.
        :rtype: list[str]
        """
        return self._cpe_traffic_selector

    @cpe_traffic_selector.setter
    def cpe_traffic_selector(self, cpe_traffic_selector):
        """
        Sets the cpe_traffic_selector of this UpdateIPSecTunnelEncryptionDomainDetails.
        Lists IPv4 or IPv6-enabled subnets in your on-premises network.


        :param cpe_traffic_selector: The cpe_traffic_selector of this UpdateIPSecTunnelEncryptionDomainDetails.
        :type: list[str]
        """
        self._cpe_traffic_selector = cpe_traffic_selector

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
