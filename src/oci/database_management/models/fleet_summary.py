# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FleetSummary(object):
    """
    A summary of the inventory count grouped by database type and subtype, and the metrics that
    describe the aggregated usage of CPU, storage, and so on of all the databases in the fleet.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FleetSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param aggregated_metrics:
            The value to assign to the aggregated_metrics property of this FleetSummary.
        :type aggregated_metrics: list[oci.database_management.models.FleetMetricSummaryDefinition]

        :param inventory:
            The value to assign to the inventory property of this FleetSummary.
        :type inventory: list[oci.database_management.models.FleetStatusByCategory]

        """
        self.swagger_types = {
            'aggregated_metrics': 'list[FleetMetricSummaryDefinition]',
            'inventory': 'list[FleetStatusByCategory]'
        }

        self.attribute_map = {
            'aggregated_metrics': 'aggregatedMetrics',
            'inventory': 'inventory'
        }

        self._aggregated_metrics = None
        self._inventory = None

    @property
    def aggregated_metrics(self):
        """
        Gets the aggregated_metrics of this FleetSummary.
        A list of databases present in the fleet and their usage metrics.


        :return: The aggregated_metrics of this FleetSummary.
        :rtype: list[oci.database_management.models.FleetMetricSummaryDefinition]
        """
        return self._aggregated_metrics

    @aggregated_metrics.setter
    def aggregated_metrics(self, aggregated_metrics):
        """
        Sets the aggregated_metrics of this FleetSummary.
        A list of databases present in the fleet and their usage metrics.


        :param aggregated_metrics: The aggregated_metrics of this FleetSummary.
        :type: list[oci.database_management.models.FleetMetricSummaryDefinition]
        """
        self._aggregated_metrics = aggregated_metrics

    @property
    def inventory(self):
        """
        Gets the inventory of this FleetSummary.
        A list of the databases in the fleet, grouped by database type and subtype.


        :return: The inventory of this FleetSummary.
        :rtype: list[oci.database_management.models.FleetStatusByCategory]
        """
        return self._inventory

    @inventory.setter
    def inventory(self, inventory):
        """
        Sets the inventory of this FleetSummary.
        A list of the databases in the fleet, grouped by database type and subtype.


        :param inventory: The inventory of this FleetSummary.
        :type: list[oci.database_management.models.FleetStatusByCategory]
        """
        self._inventory = inventory

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
