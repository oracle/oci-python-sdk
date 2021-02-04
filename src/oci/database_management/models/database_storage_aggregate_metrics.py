# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseStorageAggregateMetrics(object):
    """
    The database storage metric values.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseStorageAggregateMetrics object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param storage_allocated:
            The value to assign to the storage_allocated property of this DatabaseStorageAggregateMetrics.
        :type storage_allocated: oci.database_management.models.MetricDataPoint

        :param storage_used:
            The value to assign to the storage_used property of this DatabaseStorageAggregateMetrics.
        :type storage_used: oci.database_management.models.MetricDataPoint

        :param storage_used_by_table_space:
            The value to assign to the storage_used_by_table_space property of this DatabaseStorageAggregateMetrics.
        :type storage_used_by_table_space: list[oci.database_management.models.MetricDataPoint]

        """
        self.swagger_types = {
            'storage_allocated': 'MetricDataPoint',
            'storage_used': 'MetricDataPoint',
            'storage_used_by_table_space': 'list[MetricDataPoint]'
        }

        self.attribute_map = {
            'storage_allocated': 'storageAllocated',
            'storage_used': 'storageUsed',
            'storage_used_by_table_space': 'storageUsedByTableSpace'
        }

        self._storage_allocated = None
        self._storage_used = None
        self._storage_used_by_table_space = None

    @property
    def storage_allocated(self):
        """
        Gets the storage_allocated of this DatabaseStorageAggregateMetrics.

        :return: The storage_allocated of this DatabaseStorageAggregateMetrics.
        :rtype: oci.database_management.models.MetricDataPoint
        """
        return self._storage_allocated

    @storage_allocated.setter
    def storage_allocated(self, storage_allocated):
        """
        Sets the storage_allocated of this DatabaseStorageAggregateMetrics.

        :param storage_allocated: The storage_allocated of this DatabaseStorageAggregateMetrics.
        :type: oci.database_management.models.MetricDataPoint
        """
        self._storage_allocated = storage_allocated

    @property
    def storage_used(self):
        """
        Gets the storage_used of this DatabaseStorageAggregateMetrics.

        :return: The storage_used of this DatabaseStorageAggregateMetrics.
        :rtype: oci.database_management.models.MetricDataPoint
        """
        return self._storage_used

    @storage_used.setter
    def storage_used(self, storage_used):
        """
        Sets the storage_used of this DatabaseStorageAggregateMetrics.

        :param storage_used: The storage_used of this DatabaseStorageAggregateMetrics.
        :type: oci.database_management.models.MetricDataPoint
        """
        self._storage_used = storage_used

    @property
    def storage_used_by_table_space(self):
        """
        Gets the storage_used_by_table_space of this DatabaseStorageAggregateMetrics.
        A list of the storage metrics grouped by TableSpace for a specific database.


        :return: The storage_used_by_table_space of this DatabaseStorageAggregateMetrics.
        :rtype: list[oci.database_management.models.MetricDataPoint]
        """
        return self._storage_used_by_table_space

    @storage_used_by_table_space.setter
    def storage_used_by_table_space(self, storage_used_by_table_space):
        """
        Sets the storage_used_by_table_space of this DatabaseStorageAggregateMetrics.
        A list of the storage metrics grouped by TableSpace for a specific database.


        :param storage_used_by_table_space: The storage_used_by_table_space of this DatabaseStorageAggregateMetrics.
        :type: list[oci.database_management.models.MetricDataPoint]
        """
        self._storage_used_by_table_space = storage_used_by_table_space

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
