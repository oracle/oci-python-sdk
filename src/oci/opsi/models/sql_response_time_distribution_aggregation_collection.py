# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlResponseTimeDistributionAggregationCollection(object):
    """
    SQL response time distribution over the selected time window.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlResponseTimeDistributionAggregationCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sql_identifier:
            The value to assign to the sql_identifier property of this SqlResponseTimeDistributionAggregationCollection.
        :type sql_identifier: str

        :param database_id:
            The value to assign to the database_id property of this SqlResponseTimeDistributionAggregationCollection.
        :type database_id: str

        :param time_interval_start:
            The value to assign to the time_interval_start property of this SqlResponseTimeDistributionAggregationCollection.
        :type time_interval_start: datetime

        :param time_interval_end:
            The value to assign to the time_interval_end property of this SqlResponseTimeDistributionAggregationCollection.
        :type time_interval_end: datetime

        :param items:
            The value to assign to the items property of this SqlResponseTimeDistributionAggregationCollection.
        :type items: list[oci.opsi.models.SqlResponseTimeDistributionAggregation]

        """
        self.swagger_types = {
            'sql_identifier': 'str',
            'database_id': 'str',
            'time_interval_start': 'datetime',
            'time_interval_end': 'datetime',
            'items': 'list[SqlResponseTimeDistributionAggregation]'
        }

        self.attribute_map = {
            'sql_identifier': 'sqlIdentifier',
            'database_id': 'databaseId',
            'time_interval_start': 'timeIntervalStart',
            'time_interval_end': 'timeIntervalEnd',
            'items': 'items'
        }

        self._sql_identifier = None
        self._database_id = None
        self._time_interval_start = None
        self._time_interval_end = None
        self._items = None

    @property
    def sql_identifier(self):
        """
        **[Required]** Gets the sql_identifier of this SqlResponseTimeDistributionAggregationCollection.
        Unique SQL_ID for a SQL Statement.


        :return: The sql_identifier of this SqlResponseTimeDistributionAggregationCollection.
        :rtype: str
        """
        return self._sql_identifier

    @sql_identifier.setter
    def sql_identifier(self, sql_identifier):
        """
        Sets the sql_identifier of this SqlResponseTimeDistributionAggregationCollection.
        Unique SQL_ID for a SQL Statement.


        :param sql_identifier: The sql_identifier of this SqlResponseTimeDistributionAggregationCollection.
        :type: str
        """
        self._sql_identifier = sql_identifier

    @property
    def database_id(self):
        """
        **[Required]** Gets the database_id of this SqlResponseTimeDistributionAggregationCollection.
        The `OCID`__ of the database.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The database_id of this SqlResponseTimeDistributionAggregationCollection.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        """
        Sets the database_id of this SqlResponseTimeDistributionAggregationCollection.
        The `OCID`__ of the database.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param database_id: The database_id of this SqlResponseTimeDistributionAggregationCollection.
        :type: str
        """
        self._database_id = database_id

    @property
    def time_interval_start(self):
        """
        **[Required]** Gets the time_interval_start of this SqlResponseTimeDistributionAggregationCollection.
        The start timestamp that was passed into the request.


        :return: The time_interval_start of this SqlResponseTimeDistributionAggregationCollection.
        :rtype: datetime
        """
        return self._time_interval_start

    @time_interval_start.setter
    def time_interval_start(self, time_interval_start):
        """
        Sets the time_interval_start of this SqlResponseTimeDistributionAggregationCollection.
        The start timestamp that was passed into the request.


        :param time_interval_start: The time_interval_start of this SqlResponseTimeDistributionAggregationCollection.
        :type: datetime
        """
        self._time_interval_start = time_interval_start

    @property
    def time_interval_end(self):
        """
        **[Required]** Gets the time_interval_end of this SqlResponseTimeDistributionAggregationCollection.
        The end timestamp that was passed into the request.


        :return: The time_interval_end of this SqlResponseTimeDistributionAggregationCollection.
        :rtype: datetime
        """
        return self._time_interval_end

    @time_interval_end.setter
    def time_interval_end(self, time_interval_end):
        """
        Sets the time_interval_end of this SqlResponseTimeDistributionAggregationCollection.
        The end timestamp that was passed into the request.


        :param time_interval_end: The time_interval_end of this SqlResponseTimeDistributionAggregationCollection.
        :type: datetime
        """
        self._time_interval_end = time_interval_end

    @property
    def items(self):
        """
        **[Required]** Gets the items of this SqlResponseTimeDistributionAggregationCollection.
        Array of pre defined SQL response time bucket id and SQL executions count.


        :return: The items of this SqlResponseTimeDistributionAggregationCollection.
        :rtype: list[oci.opsi.models.SqlResponseTimeDistributionAggregation]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this SqlResponseTimeDistributionAggregationCollection.
        Array of pre defined SQL response time bucket id and SQL executions count.


        :param items: The items of this SqlResponseTimeDistributionAggregationCollection.
        :type: list[oci.opsi.models.SqlResponseTimeDistributionAggregation]
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
