# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlPlanInsightAggregationCollection(object):
    """
    SQL plan insights response.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlPlanInsightAggregationCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sql_identifier:
            The value to assign to the sql_identifier property of this SqlPlanInsightAggregationCollection.
        :type sql_identifier: str

        :param database_id:
            The value to assign to the database_id property of this SqlPlanInsightAggregationCollection.
        :type database_id: str

        :param time_interval_start:
            The value to assign to the time_interval_start property of this SqlPlanInsightAggregationCollection.
        :type time_interval_start: datetime

        :param time_interval_end:
            The value to assign to the time_interval_end property of this SqlPlanInsightAggregationCollection.
        :type time_interval_end: datetime

        :param insights:
            The value to assign to the insights property of this SqlPlanInsightAggregationCollection.
        :type insights: list[oci.opsi.models.SqlPlanInsights]

        :param items:
            The value to assign to the items property of this SqlPlanInsightAggregationCollection.
        :type items: list[oci.opsi.models.SqlPlanInsightAggregation]

        """
        self.swagger_types = {
            'sql_identifier': 'str',
            'database_id': 'str',
            'time_interval_start': 'datetime',
            'time_interval_end': 'datetime',
            'insights': 'list[SqlPlanInsights]',
            'items': 'list[SqlPlanInsightAggregation]'
        }

        self.attribute_map = {
            'sql_identifier': 'sqlIdentifier',
            'database_id': 'databaseId',
            'time_interval_start': 'timeIntervalStart',
            'time_interval_end': 'timeIntervalEnd',
            'insights': 'insights',
            'items': 'items'
        }

        self._sql_identifier = None
        self._database_id = None
        self._time_interval_start = None
        self._time_interval_end = None
        self._insights = None
        self._items = None

    @property
    def sql_identifier(self):
        """
        **[Required]** Gets the sql_identifier of this SqlPlanInsightAggregationCollection.
        Unique SQL_ID for a SQL Statement.


        :return: The sql_identifier of this SqlPlanInsightAggregationCollection.
        :rtype: str
        """
        return self._sql_identifier

    @sql_identifier.setter
    def sql_identifier(self, sql_identifier):
        """
        Sets the sql_identifier of this SqlPlanInsightAggregationCollection.
        Unique SQL_ID for a SQL Statement.


        :param sql_identifier: The sql_identifier of this SqlPlanInsightAggregationCollection.
        :type: str
        """
        self._sql_identifier = sql_identifier

    @property
    def database_id(self):
        """
        **[Required]** Gets the database_id of this SqlPlanInsightAggregationCollection.
        The `OCID`__ of the database.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The database_id of this SqlPlanInsightAggregationCollection.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        """
        Sets the database_id of this SqlPlanInsightAggregationCollection.
        The `OCID`__ of the database.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param database_id: The database_id of this SqlPlanInsightAggregationCollection.
        :type: str
        """
        self._database_id = database_id

    @property
    def time_interval_start(self):
        """
        **[Required]** Gets the time_interval_start of this SqlPlanInsightAggregationCollection.
        The start timestamp that was passed into the request.


        :return: The time_interval_start of this SqlPlanInsightAggregationCollection.
        :rtype: datetime
        """
        return self._time_interval_start

    @time_interval_start.setter
    def time_interval_start(self, time_interval_start):
        """
        Sets the time_interval_start of this SqlPlanInsightAggregationCollection.
        The start timestamp that was passed into the request.


        :param time_interval_start: The time_interval_start of this SqlPlanInsightAggregationCollection.
        :type: datetime
        """
        self._time_interval_start = time_interval_start

    @property
    def time_interval_end(self):
        """
        **[Required]** Gets the time_interval_end of this SqlPlanInsightAggregationCollection.
        The end timestamp that was passed into the request.


        :return: The time_interval_end of this SqlPlanInsightAggregationCollection.
        :rtype: datetime
        """
        return self._time_interval_end

    @time_interval_end.setter
    def time_interval_end(self, time_interval_end):
        """
        Sets the time_interval_end of this SqlPlanInsightAggregationCollection.
        The end timestamp that was passed into the request.


        :param time_interval_end: The time_interval_end of this SqlPlanInsightAggregationCollection.
        :type: datetime
        """
        self._time_interval_end = time_interval_end

    @property
    def insights(self):
        """
        **[Required]** Gets the insights of this SqlPlanInsightAggregationCollection.
        List of SQL plan insights.


        :return: The insights of this SqlPlanInsightAggregationCollection.
        :rtype: list[oci.opsi.models.SqlPlanInsights]
        """
        return self._insights

    @insights.setter
    def insights(self, insights):
        """
        Sets the insights of this SqlPlanInsightAggregationCollection.
        List of SQL plan insights.


        :param insights: The insights of this SqlPlanInsightAggregationCollection.
        :type: list[oci.opsi.models.SqlPlanInsights]
        """
        self._insights = insights

    @property
    def items(self):
        """
        **[Required]** Gets the items of this SqlPlanInsightAggregationCollection.
        List of SQL plan statistics.


        :return: The items of this SqlPlanInsightAggregationCollection.
        :rtype: list[oci.opsi.models.SqlPlanInsightAggregation]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this SqlPlanInsightAggregationCollection.
        List of SQL plan statistics.


        :param items: The items of this SqlPlanInsightAggregationCollection.
        :type: list[oci.opsi.models.SqlPlanInsightAggregation]
        """
        self._items = items

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
