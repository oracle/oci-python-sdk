# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210930

from .network_address_list_summary import NetworkAddressListSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NetworkAddressListAddressesSummary(NetworkAddressListSummary):
    """
    Summary of NetworkAddressListAddresses.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NetworkAddressListAddressesSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.waf.models.NetworkAddressListAddressesSummary.type` attribute
        of this class is ``ADDRESSES`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this NetworkAddressListAddressesSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this NetworkAddressListAddressesSummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this NetworkAddressListAddressesSummary.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this NetworkAddressListAddressesSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this NetworkAddressListAddressesSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this NetworkAddressListAddressesSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this NetworkAddressListAddressesSummary.
        :type lifecycle_details: str

        :param type:
            The value to assign to the type property of this NetworkAddressListAddressesSummary.
            Allowed values for this property are: "ADDRESSES", "VCN_ADDRESSES"
        :type type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this NetworkAddressListAddressesSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this NetworkAddressListAddressesSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this NetworkAddressListAddressesSummary.
        :type system_tags: dict(str, dict(str, object))

        :param addresses:
            The value to assign to the addresses property of this NetworkAddressListAddressesSummary.
        :type addresses: list[str]

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'addresses': 'list[str]'
        }
        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'type': 'type',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'addresses': 'addresses'
        }
        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._addresses = None
        self._type = 'ADDRESSES'

    @property
    def addresses(self):
        """
        **[Required]** Gets the addresses of this NetworkAddressListAddressesSummary.
        A list of IP address prefixes in CIDR notation.
        To specify all addresses, use \"0.0.0.0/0\" for IPv4 and \"::/0\" for IPv6.


        :return: The addresses of this NetworkAddressListAddressesSummary.
        :rtype: list[str]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """
        Sets the addresses of this NetworkAddressListAddressesSummary.
        A list of IP address prefixes in CIDR notation.
        To specify all addresses, use \"0.0.0.0/0\" for IPv4 and \"::/0\" for IPv6.


        :param addresses: The addresses of this NetworkAddressListAddressesSummary.
        :type: list[str]
        """
        self._addresses = addresses

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
