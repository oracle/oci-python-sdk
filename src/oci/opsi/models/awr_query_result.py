# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AwrQueryResult(object):
    """
    The AWR query result.
    """

    #: A constant which can be used with the awr_result_type property of a AwrQueryResult.
    #: This constant has a value of "AWRDB_SET"
    AWR_RESULT_TYPE_AWRDB_SET = "AWRDB_SET"

    #: A constant which can be used with the awr_result_type property of a AwrQueryResult.
    #: This constant has a value of "AWRDB_SNAPSHOT_RANGE_SET"
    AWR_RESULT_TYPE_AWRDB_SNAPSHOT_RANGE_SET = "AWRDB_SNAPSHOT_RANGE_SET"

    #: A constant which can be used with the awr_result_type property of a AwrQueryResult.
    #: This constant has a value of "AWRDB_SNAPSHOT_SET"
    AWR_RESULT_TYPE_AWRDB_SNAPSHOT_SET = "AWRDB_SNAPSHOT_SET"

    #: A constant which can be used with the awr_result_type property of a AwrQueryResult.
    #: This constant has a value of "AWRDB_METRICS_SET"
    AWR_RESULT_TYPE_AWRDB_METRICS_SET = "AWRDB_METRICS_SET"

    #: A constant which can be used with the awr_result_type property of a AwrQueryResult.
    #: This constant has a value of "AWRDB_SYSSTAT_SET"
    AWR_RESULT_TYPE_AWRDB_SYSSTAT_SET = "AWRDB_SYSSTAT_SET"

    #: A constant which can be used with the awr_result_type property of a AwrQueryResult.
    #: This constant has a value of "AWRDB_TOP_EVENT_SET"
    AWR_RESULT_TYPE_AWRDB_TOP_EVENT_SET = "AWRDB_TOP_EVENT_SET"

    #: A constant which can be used with the awr_result_type property of a AwrQueryResult.
    #: This constant has a value of "AWRDB_EVENT_SET"
    AWR_RESULT_TYPE_AWRDB_EVENT_SET = "AWRDB_EVENT_SET"

    #: A constant which can be used with the awr_result_type property of a AwrQueryResult.
    #: This constant has a value of "AWRDB_EVENT_HISTOGRAM"
    AWR_RESULT_TYPE_AWRDB_EVENT_HISTOGRAM = "AWRDB_EVENT_HISTOGRAM"

    #: A constant which can be used with the awr_result_type property of a AwrQueryResult.
    #: This constant has a value of "AWRDB_DB_PARAMETER_SET"
    AWR_RESULT_TYPE_AWRDB_DB_PARAMETER_SET = "AWRDB_DB_PARAMETER_SET"

    #: A constant which can be used with the awr_result_type property of a AwrQueryResult.
    #: This constant has a value of "AWRDB_DB_PARAMETER_CHANGE"
    AWR_RESULT_TYPE_AWRDB_DB_PARAMETER_CHANGE = "AWRDB_DB_PARAMETER_CHANGE"

    #: A constant which can be used with the awr_result_type property of a AwrQueryResult.
    #: This constant has a value of "AWRDB_ASH_CPU_USAGE_SET"
    AWR_RESULT_TYPE_AWRDB_ASH_CPU_USAGE_SET = "AWRDB_ASH_CPU_USAGE_SET"

    #: A constant which can be used with the awr_result_type property of a AwrQueryResult.
    #: This constant has a value of "AWRDB_DB_REPORT"
    AWR_RESULT_TYPE_AWRDB_DB_REPORT = "AWRDB_DB_REPORT"

    #: A constant which can be used with the awr_result_type property of a AwrQueryResult.
    #: This constant has a value of "AWRDB_SQL_REPORT"
    AWR_RESULT_TYPE_AWRDB_SQL_REPORT = "AWRDB_SQL_REPORT"

    def __init__(self, **kwargs):
        """
        Initializes a new AwrQueryResult object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.opsi.models.AwrDatabaseCpuUsageCollection`
        * :class:`~oci.opsi.models.AwrDatabaseParameterCollection`
        * :class:`~oci.opsi.models.AwrDatabaseWaitEventBucketCollection`
        * :class:`~oci.opsi.models.AwrDatabaseSnapshotRangeCollection`
        * :class:`~oci.opsi.models.AwrDatabaseSnapshotCollection`
        * :class:`~oci.opsi.models.AwrDatabaseSysstatCollection`
        * :class:`~oci.opsi.models.AwrDatabaseMetricCollection`
        * :class:`~oci.opsi.models.AwrDatabaseWaitEventCollection`
        * :class:`~oci.opsi.models.AwrDatabaseCollection`
        * :class:`~oci.opsi.models.AwrDatabaseTopWaitEventCollection`
        * :class:`~oci.opsi.models.AwrDatabaseParameterChangeCollection`
        * :class:`~oci.opsi.models.AwrDatabaseReport`
        * :class:`~oci.opsi.models.AwrDatabaseSqlReport`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this AwrQueryResult.
        :type name: str

        :param version:
            The value to assign to the version property of this AwrQueryResult.
        :type version: str

        :param db_query_time_in_secs:
            The value to assign to the db_query_time_in_secs property of this AwrQueryResult.
        :type db_query_time_in_secs: float

        :param awr_result_type:
            The value to assign to the awr_result_type property of this AwrQueryResult.
            Allowed values for this property are: "AWRDB_SET", "AWRDB_SNAPSHOT_RANGE_SET", "AWRDB_SNAPSHOT_SET", "AWRDB_METRICS_SET", "AWRDB_SYSSTAT_SET", "AWRDB_TOP_EVENT_SET", "AWRDB_EVENT_SET", "AWRDB_EVENT_HISTOGRAM", "AWRDB_DB_PARAMETER_SET", "AWRDB_DB_PARAMETER_CHANGE", "AWRDB_ASH_CPU_USAGE_SET", "AWRDB_DB_REPORT", "AWRDB_SQL_REPORT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type awr_result_type: str

        """
        self.swagger_types = {
            'name': 'str',
            'version': 'str',
            'db_query_time_in_secs': 'float',
            'awr_result_type': 'str'
        }
        self.attribute_map = {
            'name': 'name',
            'version': 'version',
            'db_query_time_in_secs': 'dbQueryTimeInSecs',
            'awr_result_type': 'awrResultType'
        }
        self._name = None
        self._version = None
        self._db_query_time_in_secs = None
        self._awr_result_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['awrResultType']

        if type == 'AWRDB_ASH_CPU_USAGE_SET':
            return 'AwrDatabaseCpuUsageCollection'

        if type == 'AWRDB_DB_PARAMETER_SET':
            return 'AwrDatabaseParameterCollection'

        if type == 'AWRDB_EVENT_HISTOGRAM_SET':
            return 'AwrDatabaseWaitEventBucketCollection'

        if type == 'AWRDB_SNAPSHOT_RANGE_SET':
            return 'AwrDatabaseSnapshotRangeCollection'

        if type == 'AWRDB_SNAPSHOT_SET':
            return 'AwrDatabaseSnapshotCollection'

        if type == 'AWRDB_SYSSTAT_SET':
            return 'AwrDatabaseSysstatCollection'

        if type == 'AWRDB_METRICS_SET':
            return 'AwrDatabaseMetricCollection'

        if type == 'AWRDB_EVENT_SET':
            return 'AwrDatabaseWaitEventCollection'

        if type == 'AWRDB_SET':
            return 'AwrDatabaseCollection'

        if type == 'AWRDB_TOP_EVENT_SET':
            return 'AwrDatabaseTopWaitEventCollection'

        if type == 'AWRDB_DB_PARAMETER_CHANGE':
            return 'AwrDatabaseParameterChangeCollection'

        if type == 'AWRDB_DB_REPORT':
            return 'AwrDatabaseReport'

        if type == 'AWRDB_SQL_REPORT':
            return 'AwrDatabaseSqlReport'
        else:
            return 'AwrQueryResult'

    @property
    def name(self):
        """
        **[Required]** Gets the name of this AwrQueryResult.
        The name of the query result.


        :return: The name of this AwrQueryResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AwrQueryResult.
        The name of the query result.


        :param name: The name of this AwrQueryResult.
        :type: str
        """
        self._name = name

    @property
    def version(self):
        """
        Gets the version of this AwrQueryResult.
        The version of the query result.


        :return: The version of this AwrQueryResult.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this AwrQueryResult.
        The version of the query result.


        :param version: The version of this AwrQueryResult.
        :type: str
        """
        self._version = version

    @property
    def db_query_time_in_secs(self):
        """
        Gets the db_query_time_in_secs of this AwrQueryResult.
        The time taken to query the database tier (in seconds).


        :return: The db_query_time_in_secs of this AwrQueryResult.
        :rtype: float
        """
        return self._db_query_time_in_secs

    @db_query_time_in_secs.setter
    def db_query_time_in_secs(self, db_query_time_in_secs):
        """
        Sets the db_query_time_in_secs of this AwrQueryResult.
        The time taken to query the database tier (in seconds).


        :param db_query_time_in_secs: The db_query_time_in_secs of this AwrQueryResult.
        :type: float
        """
        self._db_query_time_in_secs = db_query_time_in_secs

    @property
    def awr_result_type(self):
        """
        **[Required]** Gets the awr_result_type of this AwrQueryResult.
        The result type of AWR query.

        Allowed values for this property are: "AWRDB_SET", "AWRDB_SNAPSHOT_RANGE_SET", "AWRDB_SNAPSHOT_SET", "AWRDB_METRICS_SET", "AWRDB_SYSSTAT_SET", "AWRDB_TOP_EVENT_SET", "AWRDB_EVENT_SET", "AWRDB_EVENT_HISTOGRAM", "AWRDB_DB_PARAMETER_SET", "AWRDB_DB_PARAMETER_CHANGE", "AWRDB_ASH_CPU_USAGE_SET", "AWRDB_DB_REPORT", "AWRDB_SQL_REPORT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The awr_result_type of this AwrQueryResult.
        :rtype: str
        """
        return self._awr_result_type

    @awr_result_type.setter
    def awr_result_type(self, awr_result_type):
        """
        Sets the awr_result_type of this AwrQueryResult.
        The result type of AWR query.


        :param awr_result_type: The awr_result_type of this AwrQueryResult.
        :type: str
        """
        allowed_values = ["AWRDB_SET", "AWRDB_SNAPSHOT_RANGE_SET", "AWRDB_SNAPSHOT_SET", "AWRDB_METRICS_SET", "AWRDB_SYSSTAT_SET", "AWRDB_TOP_EVENT_SET", "AWRDB_EVENT_SET", "AWRDB_EVENT_HISTOGRAM", "AWRDB_DB_PARAMETER_SET", "AWRDB_DB_PARAMETER_CHANGE", "AWRDB_ASH_CPU_USAGE_SET", "AWRDB_DB_REPORT", "AWRDB_SQL_REPORT"]
        if not value_allowed_none_or_none_sentinel(awr_result_type, allowed_values):
            awr_result_type = 'UNKNOWN_ENUM_VALUE'
        self._awr_result_type = awr_result_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
