# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FailedConnectionsAggregateMetrics(object):
    """
    The failed connection metrics for Autonomous Databases on Shared Exadata Infrastructure.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FailedConnectionsAggregateMetrics object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param failed_connections:
            The value to assign to the failed_connections property of this FailedConnectionsAggregateMetrics.
        :type failed_connections: oci.database_management.models.MetricDataPoint

        """
        self.swagger_types = {
            'failed_connections': 'MetricDataPoint'
        }

        self.attribute_map = {
            'failed_connections': 'failedConnections'
        }

        self._failed_connections = None

    @property
    def failed_connections(self):
        """
        Gets the failed_connections of this FailedConnectionsAggregateMetrics.

        :return: The failed_connections of this FailedConnectionsAggregateMetrics.
        :rtype: oci.database_management.models.MetricDataPoint
        """
        return self._failed_connections

    @failed_connections.setter
    def failed_connections(self, failed_connections):
        """
        Sets the failed_connections of this FailedConnectionsAggregateMetrics.

        :param failed_connections: The failed_connections of this FailedConnectionsAggregateMetrics.
        :type: oci.database_management.models.MetricDataPoint
        """
        self._failed_connections = failed_connections

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
