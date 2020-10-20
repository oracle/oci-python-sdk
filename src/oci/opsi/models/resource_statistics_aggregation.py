# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResourceStatisticsAggregation(object):
    """
    Contains database details and resource statistics
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ResourceStatisticsAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param database_details:
            The value to assign to the database_details property of this ResourceStatisticsAggregation.
        :type database_details: DatabaseDetails

        :param current_statistics:
            The value to assign to the current_statistics property of this ResourceStatisticsAggregation.
        :type current_statistics: ResourceStatistics

        """
        self.swagger_types = {
            'database_details': 'DatabaseDetails',
            'current_statistics': 'ResourceStatistics'
        }

        self.attribute_map = {
            'database_details': 'databaseDetails',
            'current_statistics': 'currentStatistics'
        }

        self._database_details = None
        self._current_statistics = None

    @property
    def database_details(self):
        """
        Gets the database_details of this ResourceStatisticsAggregation.

        :return: The database_details of this ResourceStatisticsAggregation.
        :rtype: DatabaseDetails
        """
        return self._database_details

    @database_details.setter
    def database_details(self, database_details):
        """
        Sets the database_details of this ResourceStatisticsAggregation.

        :param database_details: The database_details of this ResourceStatisticsAggregation.
        :type: DatabaseDetails
        """
        self._database_details = database_details

    @property
    def current_statistics(self):
        """
        Gets the current_statistics of this ResourceStatisticsAggregation.

        :return: The current_statistics of this ResourceStatisticsAggregation.
        :rtype: ResourceStatistics
        """
        return self._current_statistics

    @current_statistics.setter
    def current_statistics(self, current_statistics):
        """
        Sets the current_statistics of this ResourceStatisticsAggregation.

        :param current_statistics: The current_statistics of this ResourceStatisticsAggregation.
        :type: ResourceStatistics
        """
        self._current_statistics = current_statistics

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
