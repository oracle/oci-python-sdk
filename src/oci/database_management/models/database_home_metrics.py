# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseHomeMetrics(object):
    """
    The response containing the metric collection for a specific database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseHomeMetrics object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param database_home_metrics:
            The value to assign to the database_home_metrics property of this DatabaseHomeMetrics.
        :type database_home_metrics: oci.database_management.models.DatabaseHomeMetricDefinition

        :param database_instance_home_metrics:
            The value to assign to the database_instance_home_metrics property of this DatabaseHomeMetrics.
        :type database_instance_home_metrics: list[oci.database_management.models.DatabaseInstanceHomeMetricsDefinition]

        """
        self.swagger_types = {
            'database_home_metrics': 'DatabaseHomeMetricDefinition',
            'database_instance_home_metrics': 'list[DatabaseInstanceHomeMetricsDefinition]'
        }

        self.attribute_map = {
            'database_home_metrics': 'databaseHomeMetrics',
            'database_instance_home_metrics': 'databaseInstanceHomeMetrics'
        }

        self._database_home_metrics = None
        self._database_instance_home_metrics = None

    @property
    def database_home_metrics(self):
        """
        **[Required]** Gets the database_home_metrics of this DatabaseHomeMetrics.

        :return: The database_home_metrics of this DatabaseHomeMetrics.
        :rtype: oci.database_management.models.DatabaseHomeMetricDefinition
        """
        return self._database_home_metrics

    @database_home_metrics.setter
    def database_home_metrics(self, database_home_metrics):
        """
        Sets the database_home_metrics of this DatabaseHomeMetrics.

        :param database_home_metrics: The database_home_metrics of this DatabaseHomeMetrics.
        :type: oci.database_management.models.DatabaseHomeMetricDefinition
        """
        self._database_home_metrics = database_home_metrics

    @property
    def database_instance_home_metrics(self):
        """
        Gets the database_instance_home_metrics of this DatabaseHomeMetrics.
        The metrics for the RAC database instances.


        :return: The database_instance_home_metrics of this DatabaseHomeMetrics.
        :rtype: list[oci.database_management.models.DatabaseInstanceHomeMetricsDefinition]
        """
        return self._database_instance_home_metrics

    @database_instance_home_metrics.setter
    def database_instance_home_metrics(self, database_instance_home_metrics):
        """
        Sets the database_instance_home_metrics of this DatabaseHomeMetrics.
        The metrics for the RAC database instances.


        :param database_instance_home_metrics: The database_instance_home_metrics of this DatabaseHomeMetrics.
        :type: list[oci.database_management.models.DatabaseInstanceHomeMetricsDefinition]
        """
        self._database_instance_home_metrics = database_instance_home_metrics

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
