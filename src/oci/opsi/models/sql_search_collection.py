# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlSearchCollection(object):
    """
    Search SQL response.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlSearchCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sql_identifier:
            The value to assign to the sql_identifier property of this SqlSearchCollection.
        :type sql_identifier: str

        :param sql_text:
            The value to assign to the sql_text property of this SqlSearchCollection.
        :type sql_text: str

        :param time_interval_start:
            The value to assign to the time_interval_start property of this SqlSearchCollection.
        :type time_interval_start: datetime

        :param time_interval_end:
            The value to assign to the time_interval_end property of this SqlSearchCollection.
        :type time_interval_end: datetime

        :param items:
            The value to assign to the items property of this SqlSearchCollection.
        :type items: list[oci.opsi.models.SqlSearchSummary]

        """
        self.swagger_types = {
            'sql_identifier': 'str',
            'sql_text': 'str',
            'time_interval_start': 'datetime',
            'time_interval_end': 'datetime',
            'items': 'list[SqlSearchSummary]'
        }

        self.attribute_map = {
            'sql_identifier': 'sqlIdentifier',
            'sql_text': 'sqlText',
            'time_interval_start': 'timeIntervalStart',
            'time_interval_end': 'timeIntervalEnd',
            'items': 'items'
        }

        self._sql_identifier = None
        self._sql_text = None
        self._time_interval_start = None
        self._time_interval_end = None
        self._items = None

    @property
    def sql_identifier(self):
        """
        Gets the sql_identifier of this SqlSearchCollection.
        Unique SQL_ID for a SQL Statement.


        :return: The sql_identifier of this SqlSearchCollection.
        :rtype: str
        """
        return self._sql_identifier

    @sql_identifier.setter
    def sql_identifier(self, sql_identifier):
        """
        Sets the sql_identifier of this SqlSearchCollection.
        Unique SQL_ID for a SQL Statement.


        :param sql_identifier: The sql_identifier of this SqlSearchCollection.
        :type: str
        """
        self._sql_identifier = sql_identifier

    @property
    def sql_text(self):
        """
        Gets the sql_text of this SqlSearchCollection.
        SQL Statement Text


        :return: The sql_text of this SqlSearchCollection.
        :rtype: str
        """
        return self._sql_text

    @sql_text.setter
    def sql_text(self, sql_text):
        """
        Sets the sql_text of this SqlSearchCollection.
        SQL Statement Text


        :param sql_text: The sql_text of this SqlSearchCollection.
        :type: str
        """
        self._sql_text = sql_text

    @property
    def time_interval_start(self):
        """
        **[Required]** Gets the time_interval_start of this SqlSearchCollection.
        The start timestamp that was passed into the request.


        :return: The time_interval_start of this SqlSearchCollection.
        :rtype: datetime
        """
        return self._time_interval_start

    @time_interval_start.setter
    def time_interval_start(self, time_interval_start):
        """
        Sets the time_interval_start of this SqlSearchCollection.
        The start timestamp that was passed into the request.


        :param time_interval_start: The time_interval_start of this SqlSearchCollection.
        :type: datetime
        """
        self._time_interval_start = time_interval_start

    @property
    def time_interval_end(self):
        """
        **[Required]** Gets the time_interval_end of this SqlSearchCollection.
        The end timestamp that was passed into the request.


        :return: The time_interval_end of this SqlSearchCollection.
        :rtype: datetime
        """
        return self._time_interval_end

    @time_interval_end.setter
    def time_interval_end(self, time_interval_end):
        """
        Sets the time_interval_end of this SqlSearchCollection.
        The end timestamp that was passed into the request.


        :param time_interval_end: The time_interval_end of this SqlSearchCollection.
        :type: datetime
        """
        self._time_interval_end = time_interval_end

    @property
    def items(self):
        """
        **[Required]** Gets the items of this SqlSearchCollection.
        List of Databases executing the sql.


        :return: The items of this SqlSearchCollection.
        :rtype: list[oci.opsi.models.SqlSearchSummary]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this SqlSearchCollection.
        List of Databases executing the sql.


        :param items: The items of this SqlSearchCollection.
        :type: list[oci.opsi.models.SqlSearchSummary]
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
