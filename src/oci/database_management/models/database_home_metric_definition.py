# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseHomeMetricDefinition(object):
    """
    The response containing the CPU, Storage, Wait, DB Time, and Memory metrics for a specific database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseHomeMetricDefinition object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param activity_time_series_metrics:
            The value to assign to the activity_time_series_metrics property of this DatabaseHomeMetricDefinition.
        :type activity_time_series_metrics: list[oci.database_management.models.ActivityTimeSeriesMetrics]

        :param db_time_aggregate_metrics:
            The value to assign to the db_time_aggregate_metrics property of this DatabaseHomeMetricDefinition.
        :type db_time_aggregate_metrics: oci.database_management.models.DatabaseTimeAggregateMetrics

        :param io_aggregate_metrics:
            The value to assign to the io_aggregate_metrics property of this DatabaseHomeMetricDefinition.
        :type io_aggregate_metrics: oci.database_management.models.DatabaseIOAggregateMetrics

        :param memory_aggregate_metrics:
            The value to assign to the memory_aggregate_metrics property of this DatabaseHomeMetricDefinition.
        :type memory_aggregate_metrics: oci.database_management.models.MemoryAggregateMetrics

        :param db_storage_aggregate_metrics:
            The value to assign to the db_storage_aggregate_metrics property of this DatabaseHomeMetricDefinition.
        :type db_storage_aggregate_metrics: oci.database_management.models.DatabaseStorageAggregateMetrics

        """
        self.swagger_types = {
            'activity_time_series_metrics': 'list[ActivityTimeSeriesMetrics]',
            'db_time_aggregate_metrics': 'DatabaseTimeAggregateMetrics',
            'io_aggregate_metrics': 'DatabaseIOAggregateMetrics',
            'memory_aggregate_metrics': 'MemoryAggregateMetrics',
            'db_storage_aggregate_metrics': 'DatabaseStorageAggregateMetrics'
        }

        self.attribute_map = {
            'activity_time_series_metrics': 'activityTimeSeriesMetrics',
            'db_time_aggregate_metrics': 'dbTimeAggregateMetrics',
            'io_aggregate_metrics': 'ioAggregateMetrics',
            'memory_aggregate_metrics': 'memoryAggregateMetrics',
            'db_storage_aggregate_metrics': 'dbStorageAggregateMetrics'
        }

        self._activity_time_series_metrics = None
        self._db_time_aggregate_metrics = None
        self._io_aggregate_metrics = None
        self._memory_aggregate_metrics = None
        self._db_storage_aggregate_metrics = None

    @property
    def activity_time_series_metrics(self):
        """
        **[Required]** Gets the activity_time_series_metrics of this DatabaseHomeMetricDefinition.
        A list of the active session metrics for CPU and Wait time for a specific database.


        :return: The activity_time_series_metrics of this DatabaseHomeMetricDefinition.
        :rtype: list[oci.database_management.models.ActivityTimeSeriesMetrics]
        """
        return self._activity_time_series_metrics

    @activity_time_series_metrics.setter
    def activity_time_series_metrics(self, activity_time_series_metrics):
        """
        Sets the activity_time_series_metrics of this DatabaseHomeMetricDefinition.
        A list of the active session metrics for CPU and Wait time for a specific database.


        :param activity_time_series_metrics: The activity_time_series_metrics of this DatabaseHomeMetricDefinition.
        :type: list[oci.database_management.models.ActivityTimeSeriesMetrics]
        """
        self._activity_time_series_metrics = activity_time_series_metrics

    @property
    def db_time_aggregate_metrics(self):
        """
        **[Required]** Gets the db_time_aggregate_metrics of this DatabaseHomeMetricDefinition.

        :return: The db_time_aggregate_metrics of this DatabaseHomeMetricDefinition.
        :rtype: oci.database_management.models.DatabaseTimeAggregateMetrics
        """
        return self._db_time_aggregate_metrics

    @db_time_aggregate_metrics.setter
    def db_time_aggregate_metrics(self, db_time_aggregate_metrics):
        """
        Sets the db_time_aggregate_metrics of this DatabaseHomeMetricDefinition.

        :param db_time_aggregate_metrics: The db_time_aggregate_metrics of this DatabaseHomeMetricDefinition.
        :type: oci.database_management.models.DatabaseTimeAggregateMetrics
        """
        self._db_time_aggregate_metrics = db_time_aggregate_metrics

    @property
    def io_aggregate_metrics(self):
        """
        **[Required]** Gets the io_aggregate_metrics of this DatabaseHomeMetricDefinition.

        :return: The io_aggregate_metrics of this DatabaseHomeMetricDefinition.
        :rtype: oci.database_management.models.DatabaseIOAggregateMetrics
        """
        return self._io_aggregate_metrics

    @io_aggregate_metrics.setter
    def io_aggregate_metrics(self, io_aggregate_metrics):
        """
        Sets the io_aggregate_metrics of this DatabaseHomeMetricDefinition.

        :param io_aggregate_metrics: The io_aggregate_metrics of this DatabaseHomeMetricDefinition.
        :type: oci.database_management.models.DatabaseIOAggregateMetrics
        """
        self._io_aggregate_metrics = io_aggregate_metrics

    @property
    def memory_aggregate_metrics(self):
        """
        **[Required]** Gets the memory_aggregate_metrics of this DatabaseHomeMetricDefinition.

        :return: The memory_aggregate_metrics of this DatabaseHomeMetricDefinition.
        :rtype: oci.database_management.models.MemoryAggregateMetrics
        """
        return self._memory_aggregate_metrics

    @memory_aggregate_metrics.setter
    def memory_aggregate_metrics(self, memory_aggregate_metrics):
        """
        Sets the memory_aggregate_metrics of this DatabaseHomeMetricDefinition.

        :param memory_aggregate_metrics: The memory_aggregate_metrics of this DatabaseHomeMetricDefinition.
        :type: oci.database_management.models.MemoryAggregateMetrics
        """
        self._memory_aggregate_metrics = memory_aggregate_metrics

    @property
    def db_storage_aggregate_metrics(self):
        """
        **[Required]** Gets the db_storage_aggregate_metrics of this DatabaseHomeMetricDefinition.

        :return: The db_storage_aggregate_metrics of this DatabaseHomeMetricDefinition.
        :rtype: oci.database_management.models.DatabaseStorageAggregateMetrics
        """
        return self._db_storage_aggregate_metrics

    @db_storage_aggregate_metrics.setter
    def db_storage_aggregate_metrics(self, db_storage_aggregate_metrics):
        """
        Sets the db_storage_aggregate_metrics of this DatabaseHomeMetricDefinition.

        :param db_storage_aggregate_metrics: The db_storage_aggregate_metrics of this DatabaseHomeMetricDefinition.
        :type: oci.database_management.models.DatabaseStorageAggregateMetrics
        """
        self._db_storage_aggregate_metrics = db_storage_aggregate_metrics

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
