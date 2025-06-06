# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IpInventoryVcnOverlapCollection(object):
    """
    The details of the overlapping VCNs and compartments.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new IpInventoryVcnOverlapCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param last_updated_timestamp:
            The value to assign to the last_updated_timestamp property of this IpInventoryVcnOverlapCollection.
        :type last_updated_timestamp: datetime

        :param ip_inventory_vcn_overlap_summary:
            The value to assign to the ip_inventory_vcn_overlap_summary property of this IpInventoryVcnOverlapCollection.
        :type ip_inventory_vcn_overlap_summary: list[oci.core.models.IpInventoryVcnOverlapSummary]

        :param message:
            The value to assign to the message property of this IpInventoryVcnOverlapCollection.
        :type message: str

        :param overlap_count:
            The value to assign to the overlap_count property of this IpInventoryVcnOverlapCollection.
        :type overlap_count: int

        """
        self.swagger_types = {
            'last_updated_timestamp': 'datetime',
            'ip_inventory_vcn_overlap_summary': 'list[IpInventoryVcnOverlapSummary]',
            'message': 'str',
            'overlap_count': 'int'
        }
        self.attribute_map = {
            'last_updated_timestamp': 'lastUpdatedTimestamp',
            'ip_inventory_vcn_overlap_summary': 'ipInventoryVcnOverlapSummary',
            'message': 'message',
            'overlap_count': 'overlapCount'
        }
        self._last_updated_timestamp = None
        self._ip_inventory_vcn_overlap_summary = None
        self._message = None
        self._overlap_count = None

    @property
    def last_updated_timestamp(self):
        """
        Gets the last_updated_timestamp of this IpInventoryVcnOverlapCollection.
        The timestamp of the latest update from the database in the format defined by `RFC3339`__.
        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The last_updated_timestamp of this IpInventoryVcnOverlapCollection.
        :rtype: datetime
        """
        return self._last_updated_timestamp

    @last_updated_timestamp.setter
    def last_updated_timestamp(self, last_updated_timestamp):
        """
        Sets the last_updated_timestamp of this IpInventoryVcnOverlapCollection.
        The timestamp of the latest update from the database in the format defined by `RFC3339`__.
        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param last_updated_timestamp: The last_updated_timestamp of this IpInventoryVcnOverlapCollection.
        :type: datetime
        """
        self._last_updated_timestamp = last_updated_timestamp

    @property
    def ip_inventory_vcn_overlap_summary(self):
        """
        Gets the ip_inventory_vcn_overlap_summary of this IpInventoryVcnOverlapCollection.
        Lists `IpInventoryVcnOverlapSummary` object.


        :return: The ip_inventory_vcn_overlap_summary of this IpInventoryVcnOverlapCollection.
        :rtype: list[oci.core.models.IpInventoryVcnOverlapSummary]
        """
        return self._ip_inventory_vcn_overlap_summary

    @ip_inventory_vcn_overlap_summary.setter
    def ip_inventory_vcn_overlap_summary(self, ip_inventory_vcn_overlap_summary):
        """
        Sets the ip_inventory_vcn_overlap_summary of this IpInventoryVcnOverlapCollection.
        Lists `IpInventoryVcnOverlapSummary` object.


        :param ip_inventory_vcn_overlap_summary: The ip_inventory_vcn_overlap_summary of this IpInventoryVcnOverlapCollection.
        :type: list[oci.core.models.IpInventoryVcnOverlapSummary]
        """
        self._ip_inventory_vcn_overlap_summary = ip_inventory_vcn_overlap_summary

    @property
    def message(self):
        """
        Gets the message of this IpInventoryVcnOverlapCollection.
        Indicates the status of the data.


        :return: The message of this IpInventoryVcnOverlapCollection.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this IpInventoryVcnOverlapCollection.
        Indicates the status of the data.


        :param message: The message of this IpInventoryVcnOverlapCollection.
        :type: str
        """
        self._message = message

    @property
    def overlap_count(self):
        """
        Gets the overlap_count of this IpInventoryVcnOverlapCollection.
        The overlap count for the given VCN and compartments.


        :return: The overlap_count of this IpInventoryVcnOverlapCollection.
        :rtype: int
        """
        return self._overlap_count

    @overlap_count.setter
    def overlap_count(self, overlap_count):
        """
        Sets the overlap_count of this IpInventoryVcnOverlapCollection.
        The overlap count for the given VCN and compartments.


        :param overlap_count: The overlap_count of this IpInventoryVcnOverlapCollection.
        :type: int
        """
        self._overlap_count = overlap_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
