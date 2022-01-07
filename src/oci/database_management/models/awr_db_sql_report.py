# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .awr_query_result import AwrQueryResult
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AwrDbSqlReport(AwrQueryResult):
    """
    The result of the AWR SQL report.
    """

    #: A constant which can be used with the format property of a AwrDbSqlReport.
    #: This constant has a value of "HTML"
    FORMAT_HTML = "HTML"

    #: A constant which can be used with the format property of a AwrDbSqlReport.
    #: This constant has a value of "TEXT"
    FORMAT_TEXT = "TEXT"

    def __init__(self, **kwargs):
        """
        Initializes a new AwrDbSqlReport object with values from keyword arguments. The default value of the :py:attr:`~oci.database_management.models.AwrDbSqlReport.awr_result_type` attribute
        of this class is ``AWRDB_SQL_REPORT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this AwrDbSqlReport.
        :type name: str

        :param version:
            The value to assign to the version property of this AwrDbSqlReport.
        :type version: str

        :param query_key:
            The value to assign to the query_key property of this AwrDbSqlReport.
        :type query_key: str

        :param db_query_time_in_secs:
            The value to assign to the db_query_time_in_secs property of this AwrDbSqlReport.
        :type db_query_time_in_secs: float

        :param awr_result_type:
            The value to assign to the awr_result_type property of this AwrDbSqlReport.
            Allowed values for this property are: "AWRDB_SET", "AWRDB_SNAPSHOT_RANGE_SET", "AWRDB_SNAPSHOT_SET", "AWRDB_METRICS_SET", "AWRDB_SYSSTAT_SET", "AWRDB_TOP_EVENT_SET", "AWRDB_EVENT_SET", "AWRDB_EVENT_HISTOGRAM", "AWRDB_DB_PARAMETER_SET", "AWRDB_DB_PARAMETER_CHANGE", "AWRDB_ASH_CPU_USAGE_SET", "AWRDB_DB_REPORT", "AWRDB_SQL_REPORT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type awr_result_type: str

        :param content:
            The value to assign to the content property of this AwrDbSqlReport.
        :type content: str

        :param format:
            The value to assign to the format property of this AwrDbSqlReport.
            Allowed values for this property are: "HTML", "TEXT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type format: str

        """
        self.swagger_types = {
            'name': 'str',
            'version': 'str',
            'query_key': 'str',
            'db_query_time_in_secs': 'float',
            'awr_result_type': 'str',
            'content': 'str',
            'format': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'version': 'version',
            'query_key': 'queryKey',
            'db_query_time_in_secs': 'dbQueryTimeInSecs',
            'awr_result_type': 'awrResultType',
            'content': 'content',
            'format': 'format'
        }

        self._name = None
        self._version = None
        self._query_key = None
        self._db_query_time_in_secs = None
        self._awr_result_type = None
        self._content = None
        self._format = None
        self._awr_result_type = 'AWRDB_SQL_REPORT'

    @property
    def content(self):
        """
        Gets the content of this AwrDbSqlReport.
        The content of the report.


        :return: The content of this AwrDbSqlReport.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this AwrDbSqlReport.
        The content of the report.


        :param content: The content of this AwrDbSqlReport.
        :type: str
        """
        self._content = content

    @property
    def format(self):
        """
        Gets the format of this AwrDbSqlReport.
        The format of the report.

        Allowed values for this property are: "HTML", "TEXT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The format of this AwrDbSqlReport.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """
        Sets the format of this AwrDbSqlReport.
        The format of the report.


        :param format: The format of this AwrDbSqlReport.
        :type: str
        """
        allowed_values = ["HTML", "TEXT"]
        if not value_allowed_none_or_none_sentinel(format, allowed_values):
            format = 'UNKNOWN_ENUM_VALUE'
        self._format = format

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
