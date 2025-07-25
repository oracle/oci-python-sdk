# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MySqlReplicationApplierFilter(object):
    """
    Filter configured for a replication channel.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MySqlReplicationApplierFilter object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param filter_name:
            The value to assign to the filter_name property of this MySqlReplicationApplierFilter.
        :type filter_name: str

        :param filter_rule:
            The value to assign to the filter_rule property of this MySqlReplicationApplierFilter.
        :type filter_rule: str

        """
        self.swagger_types = {
            'filter_name': 'str',
            'filter_rule': 'str'
        }
        self.attribute_map = {
            'filter_name': 'filterName',
            'filter_rule': 'filterRule'
        }
        self._filter_name = None
        self._filter_rule = None

    @property
    def filter_name(self):
        """
        **[Required]** Gets the filter_name of this MySqlReplicationApplierFilter.
        The type of replication filter that has been configured for the replication channel.


        :return: The filter_name of this MySqlReplicationApplierFilter.
        :rtype: str
        """
        return self._filter_name

    @filter_name.setter
    def filter_name(self, filter_name):
        """
        Sets the filter_name of this MySqlReplicationApplierFilter.
        The type of replication filter that has been configured for the replication channel.


        :param filter_name: The filter_name of this MySqlReplicationApplierFilter.
        :type: str
        """
        self._filter_name = filter_name

    @property
    def filter_rule(self):
        """
        Gets the filter_rule of this MySqlReplicationApplierFilter.
        The rules configured for the replication filter type.


        :return: The filter_rule of this MySqlReplicationApplierFilter.
        :rtype: str
        """
        return self._filter_rule

    @filter_rule.setter
    def filter_rule(self, filter_rule):
        """
        Sets the filter_rule of this MySqlReplicationApplierFilter.
        The rules configured for the replication filter type.


        :param filter_rule: The filter_rule of this MySqlReplicationApplierFilter.
        :type: str
        """
        self._filter_rule = filter_rule

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
