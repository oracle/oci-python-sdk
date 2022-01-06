# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_network_address_list_details import UpdateNetworkAddressListDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateNetworkAddressListVcnAddressesDetails(UpdateNetworkAddressListDetails):
    """
    The information to be updated for NetworkAddressListVcnAddresses.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateNetworkAddressListVcnAddressesDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.waf.models.UpdateNetworkAddressListVcnAddressesDetails.type` attribute
        of this class is ``VCN_ADDRESSES`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateNetworkAddressListVcnAddressesDetails.
        :type display_name: str

        :param type:
            The value to assign to the type property of this UpdateNetworkAddressListVcnAddressesDetails.
            Allowed values for this property are: "ADDRESSES", "VCN_ADDRESSES"
        :type type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateNetworkAddressListVcnAddressesDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateNetworkAddressListVcnAddressesDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this UpdateNetworkAddressListVcnAddressesDetails.
        :type system_tags: dict(str, dict(str, object))

        :param vcn_addresses:
            The value to assign to the vcn_addresses property of this UpdateNetworkAddressListVcnAddressesDetails.
        :type vcn_addresses: list[oci.waf.models.PrivateAddresses]

        """
        self.swagger_types = {
            'display_name': 'str',
            'type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'vcn_addresses': 'list[PrivateAddresses]'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'type': 'type',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'vcn_addresses': 'vcnAddresses'
        }

        self._display_name = None
        self._type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._vcn_addresses = None
        self._type = 'VCN_ADDRESSES'

    @property
    def vcn_addresses(self):
        """
        Gets the vcn_addresses of this UpdateNetworkAddressListVcnAddressesDetails.
        A list of private address prefixes, each associated with a particular VCN.
        To specify all addresses in a VCN, use \"0.0.0.0/0\" for IPv4 and \"::/0\" for IPv6.


        :return: The vcn_addresses of this UpdateNetworkAddressListVcnAddressesDetails.
        :rtype: list[oci.waf.models.PrivateAddresses]
        """
        return self._vcn_addresses

    @vcn_addresses.setter
    def vcn_addresses(self, vcn_addresses):
        """
        Sets the vcn_addresses of this UpdateNetworkAddressListVcnAddressesDetails.
        A list of private address prefixes, each associated with a particular VCN.
        To specify all addresses in a VCN, use \"0.0.0.0/0\" for IPv4 and \"::/0\" for IPv6.


        :param vcn_addresses: The vcn_addresses of this UpdateNetworkAddressListVcnAddressesDetails.
        :type: list[oci.waf.models.PrivateAddresses]
        """
        self._vcn_addresses = vcn_addresses

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
