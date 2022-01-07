# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StatementsAggregateMetrics(object):
    """
    The queued and running statement metrics for Autonomous Databases.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new StatementsAggregateMetrics object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param queued_statements:
            The value to assign to the queued_statements property of this StatementsAggregateMetrics.
        :type queued_statements: oci.database_management.models.MetricDataPoint

        :param running_statements:
            The value to assign to the running_statements property of this StatementsAggregateMetrics.
        :type running_statements: oci.database_management.models.MetricDataPoint

        """
        self.swagger_types = {
            'queued_statements': 'MetricDataPoint',
            'running_statements': 'MetricDataPoint'
        }

        self.attribute_map = {
            'queued_statements': 'queuedStatements',
            'running_statements': 'runningStatements'
        }

        self._queued_statements = None
        self._running_statements = None

    @property
    def queued_statements(self):
        """
        Gets the queued_statements of this StatementsAggregateMetrics.

        :return: The queued_statements of this StatementsAggregateMetrics.
        :rtype: oci.database_management.models.MetricDataPoint
        """
        return self._queued_statements

    @queued_statements.setter
    def queued_statements(self, queued_statements):
        """
        Sets the queued_statements of this StatementsAggregateMetrics.

        :param queued_statements: The queued_statements of this StatementsAggregateMetrics.
        :type: oci.database_management.models.MetricDataPoint
        """
        self._queued_statements = queued_statements

    @property
    def running_statements(self):
        """
        Gets the running_statements of this StatementsAggregateMetrics.

        :return: The running_statements of this StatementsAggregateMetrics.
        :rtype: oci.database_management.models.MetricDataPoint
        """
        return self._running_statements

    @running_statements.setter
    def running_statements(self, running_statements):
        """
        Sets the running_statements of this StatementsAggregateMetrics.

        :param running_statements: The running_statements of this StatementsAggregateMetrics.
        :type: oci.database_management.models.MetricDataPoint
        """
        self._running_statements = running_statements

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
