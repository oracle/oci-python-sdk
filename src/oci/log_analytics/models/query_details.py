# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class QueryDetails(object):
    """
    Input arguments for running a log anlaytics query. If the request is set to run in asynchronous mode
    then shouldIncludeColumns and shouldIncludeFields can be overwritten when retrieving the results.
    """

    #: A constant which can be used with the sub_system property of a QueryDetails.
    #: This constant has a value of "LOG"
    SUB_SYSTEM_LOG = "LOG"

    #: A constant which can be used with the async_mode property of a QueryDetails.
    #: This constant has a value of "FOREGROUND"
    ASYNC_MODE_FOREGROUND = "FOREGROUND"

    #: A constant which can be used with the async_mode property of a QueryDetails.
    #: This constant has a value of "BACKGROUND"
    ASYNC_MODE_BACKGROUND = "BACKGROUND"

    def __init__(self, **kwargs):
        """
        Initializes a new QueryDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this QueryDetails.
        :type compartment_id: str

        :param compartment_id_in_subtree:
            The value to assign to the compartment_id_in_subtree property of this QueryDetails.
        :type compartment_id_in_subtree: bool

        :param saved_search_id:
            The value to assign to the saved_search_id property of this QueryDetails.
        :type saved_search_id: str

        :param query_string:
            The value to assign to the query_string property of this QueryDetails.
        :type query_string: str

        :param sub_system:
            The value to assign to the sub_system property of this QueryDetails.
            Allowed values for this property are: "LOG"
        :type sub_system: str

        :param max_total_count:
            The value to assign to the max_total_count property of this QueryDetails.
        :type max_total_count: int

        :param time_filter:
            The value to assign to the time_filter property of this QueryDetails.
        :type time_filter: oci.log_analytics.models.TimeRange

        :param scope_filters:
            The value to assign to the scope_filters property of this QueryDetails.
        :type scope_filters: list[oci.log_analytics.models.ScopeFilter]

        :param query_timeout_in_seconds:
            The value to assign to the query_timeout_in_seconds property of this QueryDetails.
        :type query_timeout_in_seconds: int

        :param should_run_async:
            The value to assign to the should_run_async property of this QueryDetails.
        :type should_run_async: bool

        :param async_mode:
            The value to assign to the async_mode property of this QueryDetails.
            Allowed values for this property are: "FOREGROUND", "BACKGROUND"
        :type async_mode: str

        :param should_include_total_count:
            The value to assign to the should_include_total_count property of this QueryDetails.
        :type should_include_total_count: bool

        :param should_include_columns:
            The value to assign to the should_include_columns property of this QueryDetails.
        :type should_include_columns: bool

        :param should_include_fields:
            The value to assign to the should_include_fields property of this QueryDetails.
        :type should_include_fields: bool

        :param should_use_acceleration:
            The value to assign to the should_use_acceleration property of this QueryDetails.
        :type should_use_acceleration: bool

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'compartment_id_in_subtree': 'bool',
            'saved_search_id': 'str',
            'query_string': 'str',
            'sub_system': 'str',
            'max_total_count': 'int',
            'time_filter': 'TimeRange',
            'scope_filters': 'list[ScopeFilter]',
            'query_timeout_in_seconds': 'int',
            'should_run_async': 'bool',
            'async_mode': 'str',
            'should_include_total_count': 'bool',
            'should_include_columns': 'bool',
            'should_include_fields': 'bool',
            'should_use_acceleration': 'bool'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'compartment_id_in_subtree': 'compartmentIdInSubtree',
            'saved_search_id': 'savedSearchId',
            'query_string': 'queryString',
            'sub_system': 'subSystem',
            'max_total_count': 'maxTotalCount',
            'time_filter': 'timeFilter',
            'scope_filters': 'scopeFilters',
            'query_timeout_in_seconds': 'queryTimeoutInSeconds',
            'should_run_async': 'shouldRunAsync',
            'async_mode': 'asyncMode',
            'should_include_total_count': 'shouldIncludeTotalCount',
            'should_include_columns': 'shouldIncludeColumns',
            'should_include_fields': 'shouldIncludeFields',
            'should_use_acceleration': 'shouldUseAcceleration'
        }

        self._compartment_id = None
        self._compartment_id_in_subtree = None
        self._saved_search_id = None
        self._query_string = None
        self._sub_system = None
        self._max_total_count = None
        self._time_filter = None
        self._scope_filters = None
        self._query_timeout_in_seconds = None
        self._should_run_async = None
        self._async_mode = None
        self._should_include_total_count = None
        self._should_include_columns = None
        self._should_include_fields = None
        self._should_use_acceleration = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this QueryDetails.
        Compartment Identifier `OCID]`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this QueryDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this QueryDetails.
        Compartment Identifier `OCID]`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this QueryDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def compartment_id_in_subtree(self):
        """
        Gets the compartment_id_in_subtree of this QueryDetails.
        Flag to search all child compartments of the compartment Id specified in the compartmentId query parameter.


        :return: The compartment_id_in_subtree of this QueryDetails.
        :rtype: bool
        """
        return self._compartment_id_in_subtree

    @compartment_id_in_subtree.setter
    def compartment_id_in_subtree(self, compartment_id_in_subtree):
        """
        Sets the compartment_id_in_subtree of this QueryDetails.
        Flag to search all child compartments of the compartment Id specified in the compartmentId query parameter.


        :param compartment_id_in_subtree: The compartment_id_in_subtree of this QueryDetails.
        :type: bool
        """
        self._compartment_id_in_subtree = compartment_id_in_subtree

    @property
    def saved_search_id(self):
        """
        Gets the saved_search_id of this QueryDetails.
        Saved search OCID for this query if known.


        :return: The saved_search_id of this QueryDetails.
        :rtype: str
        """
        return self._saved_search_id

    @saved_search_id.setter
    def saved_search_id(self, saved_search_id):
        """
        Sets the saved_search_id of this QueryDetails.
        Saved search OCID for this query if known.


        :param saved_search_id: The saved_search_id of this QueryDetails.
        :type: str
        """
        self._saved_search_id = saved_search_id

    @property
    def query_string(self):
        """
        **[Required]** Gets the query_string of this QueryDetails.
        Query to perform. Must conform to logging analytic querylanguage syntax. Syntax errors will be returned if present.


        :return: The query_string of this QueryDetails.
        :rtype: str
        """
        return self._query_string

    @query_string.setter
    def query_string(self, query_string):
        """
        Sets the query_string of this QueryDetails.
        Query to perform. Must conform to logging analytic querylanguage syntax. Syntax errors will be returned if present.


        :param query_string: The query_string of this QueryDetails.
        :type: str
        """
        self._query_string = query_string

    @property
    def sub_system(self):
        """
        **[Required]** Gets the sub_system of this QueryDetails.
        Default subsystem to qualify fields with in the queryString if not specified.

        Allowed values for this property are: "LOG"


        :return: The sub_system of this QueryDetails.
        :rtype: str
        """
        return self._sub_system

    @sub_system.setter
    def sub_system(self, sub_system):
        """
        Sets the sub_system of this QueryDetails.
        Default subsystem to qualify fields with in the queryString if not specified.


        :param sub_system: The sub_system of this QueryDetails.
        :type: str
        """
        allowed_values = ["LOG"]
        if not value_allowed_none_or_none_sentinel(sub_system, allowed_values):
            raise ValueError(
                "Invalid value for `sub_system`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._sub_system = sub_system

    @property
    def max_total_count(self):
        """
        Gets the max_total_count of this QueryDetails.
        Maximum number of results to count.  Note a maximum of 2001 will be enforced; that is, actualMaxTotalCountUsed = Math.min(maxTotalCount, 2001).


        :return: The max_total_count of this QueryDetails.
        :rtype: int
        """
        return self._max_total_count

    @max_total_count.setter
    def max_total_count(self, max_total_count):
        """
        Sets the max_total_count of this QueryDetails.
        Maximum number of results to count.  Note a maximum of 2001 will be enforced; that is, actualMaxTotalCountUsed = Math.min(maxTotalCount, 2001).


        :param max_total_count: The max_total_count of this QueryDetails.
        :type: int
        """
        self._max_total_count = max_total_count

    @property
    def time_filter(self):
        """
        Gets the time_filter of this QueryDetails.

        :return: The time_filter of this QueryDetails.
        :rtype: oci.log_analytics.models.TimeRange
        """
        return self._time_filter

    @time_filter.setter
    def time_filter(self, time_filter):
        """
        Sets the time_filter of this QueryDetails.

        :param time_filter: The time_filter of this QueryDetails.
        :type: oci.log_analytics.models.TimeRange
        """
        self._time_filter = time_filter

    @property
    def scope_filters(self):
        """
        Gets the scope_filters of this QueryDetails.
        List of filters to be applied when the query executes. More than one filter per field is not permitted.


        :return: The scope_filters of this QueryDetails.
        :rtype: list[oci.log_analytics.models.ScopeFilter]
        """
        return self._scope_filters

    @scope_filters.setter
    def scope_filters(self, scope_filters):
        """
        Sets the scope_filters of this QueryDetails.
        List of filters to be applied when the query executes. More than one filter per field is not permitted.


        :param scope_filters: The scope_filters of this QueryDetails.
        :type: list[oci.log_analytics.models.ScopeFilter]
        """
        self._scope_filters = scope_filters

    @property
    def query_timeout_in_seconds(self):
        """
        Gets the query_timeout_in_seconds of this QueryDetails.
        Amount of time, in seconds, allowed for a query to execute. If this time expires before the query is complete, any partial results will be returned.


        :return: The query_timeout_in_seconds of this QueryDetails.
        :rtype: int
        """
        return self._query_timeout_in_seconds

    @query_timeout_in_seconds.setter
    def query_timeout_in_seconds(self, query_timeout_in_seconds):
        """
        Sets the query_timeout_in_seconds of this QueryDetails.
        Amount of time, in seconds, allowed for a query to execute. If this time expires before the query is complete, any partial results will be returned.


        :param query_timeout_in_seconds: The query_timeout_in_seconds of this QueryDetails.
        :type: int
        """
        self._query_timeout_in_seconds = query_timeout_in_seconds

    @property
    def should_run_async(self):
        """
        Gets the should_run_async of this QueryDetails.
        Option to run the query asynchronously. This will lead to a LogAnalyticsQueryJobWorkRequest being submitted and the {workRequestId} will be returned to use for fetching the results.


        :return: The should_run_async of this QueryDetails.
        :rtype: bool
        """
        return self._should_run_async

    @should_run_async.setter
    def should_run_async(self, should_run_async):
        """
        Sets the should_run_async of this QueryDetails.
        Option to run the query asynchronously. This will lead to a LogAnalyticsQueryJobWorkRequest being submitted and the {workRequestId} will be returned to use for fetching the results.


        :param should_run_async: The should_run_async of this QueryDetails.
        :type: bool
        """
        self._should_run_async = should_run_async

    @property
    def async_mode(self):
        """
        Gets the async_mode of this QueryDetails.
        Execution mode for the query if running asynchronously i.e (shouldRunAsync is set to true).

        Allowed values for this property are: "FOREGROUND", "BACKGROUND"


        :return: The async_mode of this QueryDetails.
        :rtype: str
        """
        return self._async_mode

    @async_mode.setter
    def async_mode(self, async_mode):
        """
        Sets the async_mode of this QueryDetails.
        Execution mode for the query if running asynchronously i.e (shouldRunAsync is set to true).


        :param async_mode: The async_mode of this QueryDetails.
        :type: str
        """
        allowed_values = ["FOREGROUND", "BACKGROUND"]
        if not value_allowed_none_or_none_sentinel(async_mode, allowed_values):
            raise ValueError(
                "Invalid value for `async_mode`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._async_mode = async_mode

    @property
    def should_include_total_count(self):
        """
        Gets the should_include_total_count of this QueryDetails.
        Include the total number of results from the query. Note, this value will always be equal to or less than maxTotalCount.


        :return: The should_include_total_count of this QueryDetails.
        :rtype: bool
        """
        return self._should_include_total_count

    @should_include_total_count.setter
    def should_include_total_count(self, should_include_total_count):
        """
        Sets the should_include_total_count of this QueryDetails.
        Include the total number of results from the query. Note, this value will always be equal to or less than maxTotalCount.


        :param should_include_total_count: The should_include_total_count of this QueryDetails.
        :type: bool
        """
        self._should_include_total_count = should_include_total_count

    @property
    def should_include_columns(self):
        """
        Gets the should_include_columns of this QueryDetails.
        Include columns in response


        :return: The should_include_columns of this QueryDetails.
        :rtype: bool
        """
        return self._should_include_columns

    @should_include_columns.setter
    def should_include_columns(self, should_include_columns):
        """
        Sets the should_include_columns of this QueryDetails.
        Include columns in response


        :param should_include_columns: The should_include_columns of this QueryDetails.
        :type: bool
        """
        self._should_include_columns = should_include_columns

    @property
    def should_include_fields(self):
        """
        Gets the should_include_fields of this QueryDetails.
        Include fields in response


        :return: The should_include_fields of this QueryDetails.
        :rtype: bool
        """
        return self._should_include_fields

    @should_include_fields.setter
    def should_include_fields(self, should_include_fields):
        """
        Sets the should_include_fields of this QueryDetails.
        Include fields in response


        :param should_include_fields: The should_include_fields of this QueryDetails.
        :type: bool
        """
        self._should_include_fields = should_include_fields

    @property
    def should_use_acceleration(self):
        """
        Gets the should_use_acceleration of this QueryDetails.
        Controls if query should ignore pre-calculated results if available and only use raw data. If set and no acceleration data is found it will fallback to raw data.


        :return: The should_use_acceleration of this QueryDetails.
        :rtype: bool
        """
        return self._should_use_acceleration

    @should_use_acceleration.setter
    def should_use_acceleration(self, should_use_acceleration):
        """
        Sets the should_use_acceleration of this QueryDetails.
        Controls if query should ignore pre-calculated results if available and only use raw data. If set and no acceleration data is found it will fallback to raw data.


        :param should_use_acceleration: The should_use_acceleration of this QueryDetails.
        :type: bool
        """
        self._should_use_acceleration = should_use_acceleration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
