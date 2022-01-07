# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlStatisticsTimeSeriesAggregation(object):
    """
    Database details and SQL performance statistics for a given database
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlStatisticsTimeSeriesAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param database_details:
            The value to assign to the database_details property of this SqlStatisticsTimeSeriesAggregation.
        :type database_details: oci.opsi.models.DatabaseDetails

        :param statistics:
            The value to assign to the statistics property of this SqlStatisticsTimeSeriesAggregation.
        :type statistics: list[oci.opsi.models.SqlStatisticsTimeSeries]

        """
        self.swagger_types = {
            'database_details': 'DatabaseDetails',
            'statistics': 'list[SqlStatisticsTimeSeries]'
        }

        self.attribute_map = {
            'database_details': 'databaseDetails',
            'statistics': 'statistics'
        }

        self._database_details = None
        self._statistics = None

    @property
    def database_details(self):
        """
        **[Required]** Gets the database_details of this SqlStatisticsTimeSeriesAggregation.

        :return: The database_details of this SqlStatisticsTimeSeriesAggregation.
        :rtype: oci.opsi.models.DatabaseDetails
        """
        return self._database_details

    @database_details.setter
    def database_details(self, database_details):
        """
        Sets the database_details of this SqlStatisticsTimeSeriesAggregation.

        :param database_details: The database_details of this SqlStatisticsTimeSeriesAggregation.
        :type: oci.opsi.models.DatabaseDetails
        """
        self._database_details = database_details

    @property
    def statistics(self):
        """
        **[Required]** Gets the statistics of this SqlStatisticsTimeSeriesAggregation.
        SQL performance statistics for a given database


        :return: The statistics of this SqlStatisticsTimeSeriesAggregation.
        :rtype: list[oci.opsi.models.SqlStatisticsTimeSeries]
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        """
        Sets the statistics of this SqlStatisticsTimeSeriesAggregation.
        SQL performance statistics for a given database


        :param statistics: The statistics of this SqlStatisticsTimeSeriesAggregation.
        :type: list[oci.opsi.models.SqlStatisticsTimeSeries]
        """
        self._statistics = statistics

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
