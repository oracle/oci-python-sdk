# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseInstanceHomeMetricsDefinition(object):
    """
    The response containing the CPU, Wait, DB Time, and Memory metrics
    for a specific Oracle Real Application Clusters (Oracle RAC) database
    instance.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseInstanceHomeMetricsDefinition object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param instance_name:
            The value to assign to the instance_name property of this DatabaseInstanceHomeMetricsDefinition.
        :type instance_name: str

        :param instance_number:
            The value to assign to the instance_number property of this DatabaseInstanceHomeMetricsDefinition.
        :type instance_number: int

        :param activity_time_series_metrics:
            The value to assign to the activity_time_series_metrics property of this DatabaseInstanceHomeMetricsDefinition.
        :type activity_time_series_metrics: list[oci.database_management.models.ActivityTimeSeriesMetrics]

        :param db_time_aggregate_metrics:
            The value to assign to the db_time_aggregate_metrics property of this DatabaseInstanceHomeMetricsDefinition.
        :type db_time_aggregate_metrics: oci.database_management.models.DatabaseTimeAggregateMetrics

        :param io_aggregate_metrics:
            The value to assign to the io_aggregate_metrics property of this DatabaseInstanceHomeMetricsDefinition.
        :type io_aggregate_metrics: oci.database_management.models.DatabaseIOAggregateMetrics

        :param memory_aggregate_metrics:
            The value to assign to the memory_aggregate_metrics property of this DatabaseInstanceHomeMetricsDefinition.
        :type memory_aggregate_metrics: oci.database_management.models.MemoryAggregateMetrics

        :param cpu_utilization_aggregate_metrics:
            The value to assign to the cpu_utilization_aggregate_metrics property of this DatabaseInstanceHomeMetricsDefinition.
        :type cpu_utilization_aggregate_metrics: oci.database_management.models.CpuUtilizationAggregateMetrics

        """
        self.swagger_types = {
            'instance_name': 'str',
            'instance_number': 'int',
            'activity_time_series_metrics': 'list[ActivityTimeSeriesMetrics]',
            'db_time_aggregate_metrics': 'DatabaseTimeAggregateMetrics',
            'io_aggregate_metrics': 'DatabaseIOAggregateMetrics',
            'memory_aggregate_metrics': 'MemoryAggregateMetrics',
            'cpu_utilization_aggregate_metrics': 'CpuUtilizationAggregateMetrics'
        }

        self.attribute_map = {
            'instance_name': 'instanceName',
            'instance_number': 'instanceNumber',
            'activity_time_series_metrics': 'activityTimeSeriesMetrics',
            'db_time_aggregate_metrics': 'dbTimeAggregateMetrics',
            'io_aggregate_metrics': 'ioAggregateMetrics',
            'memory_aggregate_metrics': 'memoryAggregateMetrics',
            'cpu_utilization_aggregate_metrics': 'cpuUtilizationAggregateMetrics'
        }

        self._instance_name = None
        self._instance_number = None
        self._activity_time_series_metrics = None
        self._db_time_aggregate_metrics = None
        self._io_aggregate_metrics = None
        self._memory_aggregate_metrics = None
        self._cpu_utilization_aggregate_metrics = None

    @property
    def instance_name(self):
        """
        **[Required]** Gets the instance_name of this DatabaseInstanceHomeMetricsDefinition.
        The name of the Oracle Real Application Clusters (Oracle RAC)
        database instance to which the corresponding metrics belong.


        :return: The instance_name of this DatabaseInstanceHomeMetricsDefinition.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """
        Sets the instance_name of this DatabaseInstanceHomeMetricsDefinition.
        The name of the Oracle Real Application Clusters (Oracle RAC)
        database instance to which the corresponding metrics belong.


        :param instance_name: The instance_name of this DatabaseInstanceHomeMetricsDefinition.
        :type: str
        """
        self._instance_name = instance_name

    @property
    def instance_number(self):
        """
        **[Required]** Gets the instance_number of this DatabaseInstanceHomeMetricsDefinition.
        The number of Oracle Real Application Clusters (Oracle RAC)
        database instance to which the corresponding metrics belong.


        :return: The instance_number of this DatabaseInstanceHomeMetricsDefinition.
        :rtype: int
        """
        return self._instance_number

    @instance_number.setter
    def instance_number(self, instance_number):
        """
        Sets the instance_number of this DatabaseInstanceHomeMetricsDefinition.
        The number of Oracle Real Application Clusters (Oracle RAC)
        database instance to which the corresponding metrics belong.


        :param instance_number: The instance_number of this DatabaseInstanceHomeMetricsDefinition.
        :type: int
        """
        self._instance_number = instance_number

    @property
    def activity_time_series_metrics(self):
        """
        **[Required]** Gets the activity_time_series_metrics of this DatabaseInstanceHomeMetricsDefinition.
        A list of the active session metrics for CPU and Wait time for
        a specific Oracle Real Application Clusters (Oracle RAC)
        database instance.


        :return: The activity_time_series_metrics of this DatabaseInstanceHomeMetricsDefinition.
        :rtype: list[oci.database_management.models.ActivityTimeSeriesMetrics]
        """
        return self._activity_time_series_metrics

    @activity_time_series_metrics.setter
    def activity_time_series_metrics(self, activity_time_series_metrics):
        """
        Sets the activity_time_series_metrics of this DatabaseInstanceHomeMetricsDefinition.
        A list of the active session metrics for CPU and Wait time for
        a specific Oracle Real Application Clusters (Oracle RAC)
        database instance.


        :param activity_time_series_metrics: The activity_time_series_metrics of this DatabaseInstanceHomeMetricsDefinition.
        :type: list[oci.database_management.models.ActivityTimeSeriesMetrics]
        """
        self._activity_time_series_metrics = activity_time_series_metrics

    @property
    def db_time_aggregate_metrics(self):
        """
        **[Required]** Gets the db_time_aggregate_metrics of this DatabaseInstanceHomeMetricsDefinition.

        :return: The db_time_aggregate_metrics of this DatabaseInstanceHomeMetricsDefinition.
        :rtype: oci.database_management.models.DatabaseTimeAggregateMetrics
        """
        return self._db_time_aggregate_metrics

    @db_time_aggregate_metrics.setter
    def db_time_aggregate_metrics(self, db_time_aggregate_metrics):
        """
        Sets the db_time_aggregate_metrics of this DatabaseInstanceHomeMetricsDefinition.

        :param db_time_aggregate_metrics: The db_time_aggregate_metrics of this DatabaseInstanceHomeMetricsDefinition.
        :type: oci.database_management.models.DatabaseTimeAggregateMetrics
        """
        self._db_time_aggregate_metrics = db_time_aggregate_metrics

    @property
    def io_aggregate_metrics(self):
        """
        **[Required]** Gets the io_aggregate_metrics of this DatabaseInstanceHomeMetricsDefinition.

        :return: The io_aggregate_metrics of this DatabaseInstanceHomeMetricsDefinition.
        :rtype: oci.database_management.models.DatabaseIOAggregateMetrics
        """
        return self._io_aggregate_metrics

    @io_aggregate_metrics.setter
    def io_aggregate_metrics(self, io_aggregate_metrics):
        """
        Sets the io_aggregate_metrics of this DatabaseInstanceHomeMetricsDefinition.

        :param io_aggregate_metrics: The io_aggregate_metrics of this DatabaseInstanceHomeMetricsDefinition.
        :type: oci.database_management.models.DatabaseIOAggregateMetrics
        """
        self._io_aggregate_metrics = io_aggregate_metrics

    @property
    def memory_aggregate_metrics(self):
        """
        **[Required]** Gets the memory_aggregate_metrics of this DatabaseInstanceHomeMetricsDefinition.

        :return: The memory_aggregate_metrics of this DatabaseInstanceHomeMetricsDefinition.
        :rtype: oci.database_management.models.MemoryAggregateMetrics
        """
        return self._memory_aggregate_metrics

    @memory_aggregate_metrics.setter
    def memory_aggregate_metrics(self, memory_aggregate_metrics):
        """
        Sets the memory_aggregate_metrics of this DatabaseInstanceHomeMetricsDefinition.

        :param memory_aggregate_metrics: The memory_aggregate_metrics of this DatabaseInstanceHomeMetricsDefinition.
        :type: oci.database_management.models.MemoryAggregateMetrics
        """
        self._memory_aggregate_metrics = memory_aggregate_metrics

    @property
    def cpu_utilization_aggregate_metrics(self):
        """
        Gets the cpu_utilization_aggregate_metrics of this DatabaseInstanceHomeMetricsDefinition.

        :return: The cpu_utilization_aggregate_metrics of this DatabaseInstanceHomeMetricsDefinition.
        :rtype: oci.database_management.models.CpuUtilizationAggregateMetrics
        """
        return self._cpu_utilization_aggregate_metrics

    @cpu_utilization_aggregate_metrics.setter
    def cpu_utilization_aggregate_metrics(self, cpu_utilization_aggregate_metrics):
        """
        Sets the cpu_utilization_aggregate_metrics of this DatabaseInstanceHomeMetricsDefinition.

        :param cpu_utilization_aggregate_metrics: The cpu_utilization_aggregate_metrics of this DatabaseInstanceHomeMetricsDefinition.
        :type: oci.database_management.models.CpuUtilizationAggregateMetrics
        """
        self._cpu_utilization_aggregate_metrics = cpu_utilization_aggregate_metrics

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
