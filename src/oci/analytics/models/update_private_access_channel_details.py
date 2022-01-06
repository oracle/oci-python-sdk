# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdatePrivateAccessChannelDetails(object):
    """
    Input payload to update a Private Access Channel.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdatePrivateAccessChannelDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdatePrivateAccessChannelDetails.
        :type display_name: str

        :param vcn_id:
            The value to assign to the vcn_id property of this UpdatePrivateAccessChannelDetails.
        :type vcn_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this UpdatePrivateAccessChannelDetails.
        :type subnet_id: str

        :param private_source_dns_zones:
            The value to assign to the private_source_dns_zones property of this UpdatePrivateAccessChannelDetails.
        :type private_source_dns_zones: list[oci.analytics.models.PrivateSourceDnsZone]

        """
        self.swagger_types = {
            'display_name': 'str',
            'vcn_id': 'str',
            'subnet_id': 'str',
            'private_source_dns_zones': 'list[PrivateSourceDnsZone]'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'vcn_id': 'vcnId',
            'subnet_id': 'subnetId',
            'private_source_dns_zones': 'privateSourceDnsZones'
        }

        self._display_name = None
        self._vcn_id = None
        self._subnet_id = None
        self._private_source_dns_zones = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdatePrivateAccessChannelDetails.
        Display Name of the Private Access Channel.


        :return: The display_name of this UpdatePrivateAccessChannelDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdatePrivateAccessChannelDetails.
        Display Name of the Private Access Channel.


        :param display_name: The display_name of this UpdatePrivateAccessChannelDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def vcn_id(self):
        """
        Gets the vcn_id of this UpdatePrivateAccessChannelDetails.
        OCID of the customer VCN peered with private access channel.


        :return: The vcn_id of this UpdatePrivateAccessChannelDetails.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this UpdatePrivateAccessChannelDetails.
        OCID of the customer VCN peered with private access channel.


        :param vcn_id: The vcn_id of this UpdatePrivateAccessChannelDetails.
        :type: str
        """
        self._vcn_id = vcn_id

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this UpdatePrivateAccessChannelDetails.
        OCID of the customer subnet connected to private access channel.


        :return: The subnet_id of this UpdatePrivateAccessChannelDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this UpdatePrivateAccessChannelDetails.
        OCID of the customer subnet connected to private access channel.


        :param subnet_id: The subnet_id of this UpdatePrivateAccessChannelDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def private_source_dns_zones(self):
        """
        Gets the private_source_dns_zones of this UpdatePrivateAccessChannelDetails.
        List of Private Source DNS zones registered with Private Access Channel,
        where datasource hostnames from these dns zones / domains will be resolved in the peered VCN for access from Analytics Instance.
        Min of 1 is required and Max of 30 Private Source DNS zones can be registered.


        :return: The private_source_dns_zones of this UpdatePrivateAccessChannelDetails.
        :rtype: list[oci.analytics.models.PrivateSourceDnsZone]
        """
        return self._private_source_dns_zones

    @private_source_dns_zones.setter
    def private_source_dns_zones(self, private_source_dns_zones):
        """
        Sets the private_source_dns_zones of this UpdatePrivateAccessChannelDetails.
        List of Private Source DNS zones registered with Private Access Channel,
        where datasource hostnames from these dns zones / domains will be resolved in the peered VCN for access from Analytics Instance.
        Min of 1 is required and Max of 30 Private Source DNS zones can be registered.


        :param private_source_dns_zones: The private_source_dns_zones of this UpdatePrivateAccessChannelDetails.
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
