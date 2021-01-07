# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExportDetails(object):
    """
    Input arguments for running a query synchronosly and streaming the results as soon as they become available.
    """

    #: A constant which can be used with the sub_system property of a ExportDetails.
    #: This constant has a value of "LOG"
    SUB_SYSTEM_LOG = "LOG"

    #: A constant which can be used with the output_format property of a ExportDetails.
    #: This constant has a value of "CSV"
    OUTPUT_FORMAT_CSV = "CSV"

    #: A constant which can be used with the output_format property of a ExportDetails.
    #: This constant has a value of "JSON"
    OUTPUT_FORMAT_JSON = "JSON"

    def __init__(self, **kwargs):
        """
        Initializes a new ExportDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this ExportDetails.
        :type compartment_id: str

        :param compartment_id_in_subtree:
            The value to assign to the compartment_id_in_subtree property of this ExportDetails.
        :type compartment_id_in_subtree: bool

        :param query_string:
            The value to assign to the query_string property of this ExportDetails.
        :type query_string: str

        :param sub_system:
            The value to assign to the sub_system property of this ExportDetails.
            Allowed values for this property are: "LOG"
        :type sub_system: str

        :param scope_filters:
            The value to assign to the scope_filters property of this ExportDetails.
        :type scope_filters: list[oci.log_analytics.models.ScopeFilter]

        :param max_total_count:
            The value to assign to the max_total_count property of this ExportDetails.
        :type max_total_count: int

        :param time_filter:
            The value to assign to the time_filter property of this ExportDetails.
        :type time_filter: oci.log_analytics.models.TimeRange

        :param query_timeout_in_seconds:
            The value to assign to the query_timeout_in_seconds property of this ExportDetails.
        :type query_timeout_in_seconds: int

        :param should_include_columns:
            The value to assign to the should_include_columns property of this ExportDetails.
        :type should_include_columns: bool

        :param output_format:
            The value to assign to the output_format property of this ExportDetails.
            Allowed values for this property are: "CSV", "JSON"
        :type output_format: str

        :param should_localize:
            The value to assign to the should_localize property of this ExportDetails.
        :type should_localize: bool

        :param should_use_acceleration:
            The value to assign to the should_use_acceleration property of this ExportDetails.
        :type should_use_acceleration: bool

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'compartment_id_in_subtree': 'bool',
            'query_string': 'str',
            'sub_system': 'str',
            'scope_filters': 'list[ScopeFilter]',
            'max_total_count': 'int',
            'time_filter': 'TimeRange',
            'query_timeout_in_seconds': 'int',
            'should_include_columns': 'bool',
            'output_format': 'str',
            'should_localize': 'bool',
            'should_use_acceleration': 'bool'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'compartment_id_in_subtree': 'compartmentIdInSubtree',
            'query_string': 'queryString',
            'sub_system': 'subSystem',
            'scope_filters': 'scopeFilters',
            'max_total_count': 'maxTotalCount',
            'time_filter': 'timeFilter',
            'query_timeout_in_seconds': 'queryTimeoutInSeconds',
            'should_include_columns': 'shouldIncludeColumns',
            'output_format': 'outputFormat',
            'should_localize': 'shouldLocalize',
            'should_use_acceleration': 'shouldUseAcceleration'
        }

        self._compartment_id = None
        self._compartment_id_in_subtree = None
        self._query_string = None
        self._sub_system = None
        self._scope_filters = None
        self._max_total_count = None
        self._time_filter = None
        self._query_timeout_in_seconds = None
        self._should_include_columns = None
        self._output_format = None
        self._should_localize = None
        self._should_use_acceleration = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ExportDetails.
        Compartment Identifier `OCID]`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ExportDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ExportDetails.
        Compartment Identifier `OCID]`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ExportDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def compartment_id_in_subtree(self):
        """
        Gets the compartment_id_in_subtree of this ExportDetails.
        Flag to search all child compartments of the compartment Id specified in the compartmentId query parameter.


        :return: The compartment_id_in_subtree of this ExportDetails.
        :rtype: bool
        """
        return self._compartment_id_in_subtree

    @compartment_id_in_subtree.setter
    def compartment_id_in_subtree(self, compartment_id_in_subtree):
        """
        Sets the compartment_id_in_subtree of this ExportDetails.
        Flag to search all child compartments of the compartment Id specified in the compartmentId query parameter.


        :param compartment_id_in_subtree: The compartment_id_in_subtree of this ExportDetails.
        :type: bool
        """
        self._compartment_id_in_subtree = compartment_id_in_subtree

    @property
    def query_string(self):
        """
        **[Required]** Gets the query_string of this ExportDetails.
        Query to perform.


        :return: The query_string of this ExportDetails.
        :rtype: str
        """
        return self._query_string

    @query_string.setter
    def query_string(self, query_string):
        """
        Sets the query_string of this ExportDetails.
        Query to perform.


        :param query_string: The query_string of this ExportDetails.
        :type: str
        """
        self._query_string = query_string

    @property
    def sub_system(self):
        """
        **[Required]** Gets the sub_system of this ExportDetails.
        Default subsystem to qualify fields with in the queryString if not specified.

        Allowed values for this property are: "LOG"


        :return: The sub_system of this ExportDetails.
        :rtype: str
        """
        return self._sub_system

    @sub_system.setter
    def sub_system(self, sub_system):
        """
        Sets the sub_system of this ExportDetails.
        Default subsystem to qualify fields with in the queryString if not specified.


        :param sub_system: The sub_system of this ExportDetails.
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
    def scope_filters(self):
        """
        Gets the scope_filters of this ExportDetails.
        List of filters to be applied when the query executes. More than one filter per field is not permitted.


        :return: The scope_filters of this ExportDetails.
        :rtype: list[oci.log_analytics.models.ScopeFilter]
        """
        return self._scope_filters

    @scope_filters.setter
    def scope_filters(self, scope_filters):
        """
        Sets the scope_filters of this ExportDetails.
        List of filters to be applied when the query executes. More than one filter per field is not permitted.


        :param scope_filters: The scope_filters of this ExportDetails.
        :type: list[oci.log_analytics.models.ScopeFilter]
        """
        self._scope_filters = scope_filters

    @property
    def max_total_count(self):
        """
        Gets the max_total_count of this ExportDetails.
        Maximum number of results retrieved from data source.  Note a maximum value will be enforced; if the export results can be streamed, the maximum will be 50000000, otherwise 10000; that is, if not streamed, actualMaxTotalCountUsed = Math.min(maxTotalCount, 10000).


        Export will incrementally stream results depending on the queryString.

        Some commands including head/tail are not compatible with streaming result delivery and therefore enforce a reduced limit on overall maxtotalcount.
         no sort command or sort by id, e.g. ' | sort id ' - is streaming compatible
         sort by time and id, e.g. ' | sort -time, id ' - is streaming compatible
        all other cases, e.g. ' | sort -time, id, mtgtguid ' - is not streaming compatible due to the additional sort field


        :return: The max_total_count of this ExportDetails.
        :rtype: int
        """
        return self._max_total_count

    @max_total_count.setter
    def max_total_count(self, max_total_count):
        """
        Sets the max_total_count of this ExportDetails.
        Maximum number of results retrieved from data source.  Note a maximum value will be enforced; if the export results can be streamed, the maximum will be 50000000, otherwise 10000; that is, if not streamed, actualMaxTotalCountUsed = Math.min(maxTotalCount, 10000).


        Export will incrementally stream results depending on the queryString.

        Some commands including head/tail are not compatible with streaming result delivery and therefore enforce a reduced limit on overall maxtotalcount.
         no sort command or sort by id, e.g. ' | sort id ' - is streaming compatible
         sort by time and id, e.g. ' | sort -time, id ' - is streaming compatible
        all other cases, e.g. ' | sort -time, id, mtgtguid ' - is not streaming compatible due to the additional sort field


        :param max_total_count: The max_total_count of this ExportDetails.
        :type: int
        """
        self._max_total_count = max_total_count

    @property
    def time_filter(self):
        """
        Gets the time_filter of this ExportDetails.

        :return: The time_filter of this ExportDetails.
        :rtype: oci.log_analytics.models.TimeRange
        """
        return self._time_filter

    @time_filter.setter
    def time_filter(self, time_filter):
        """
        Sets the time_filter of this ExportDetails.

        :param time_filter: The time_filter of this ExportDetails.
        :type: oci.log_analytics.models.TimeRange
        """
        self._time_filter = time_filter

    @property
    def query_timeout_in_seconds(self):
        """
        Gets the query_timeout_in_seconds of this ExportDetails.
        Amount of time, in seconds, allowed for a query to execute. If this time expires before the query is complete, any partial results will be returned.


        :return: The query_timeout_in_seconds of this ExportDetails.
        :rtype: int
        """
        return self._query_timeout_in_seconds

    @query_timeout_in_seconds.setter
    def query_timeout_in_seconds(self, query_timeout_in_seconds):
        """
        Sets the query_timeout_in_seconds of this ExportDetails.
        Amount of time, in seconds, allowed for a query to execute. If this time expires before the query is complete, any partial results will be returned.


        :param query_timeout_in_seconds: The query_timeout_in_seconds of this ExportDetails.
        :type: int
        """
        self._query_timeout_in_seconds = query_timeout_in_seconds

    @property
    def should_include_columns(self):
        """
        Gets the should_include_columns of this ExportDetails.
        Include columns in response


        :return: The should_include_columns of this ExportDetails.
        :rtype: bool
        """
        return self._should_include_columns

    @should_include_columns.setter
    def should_include_columns(self, should_include_columns):
        """
        Sets the should_include_columns of this ExportDetails.
        Include columns in response


        :param should_include_columns: The should_include_columns of this ExportDetails.
        :type: bool
        """
        self._should_include_columns = should_include_columns

    @property
    def output_format(self):
        """
        Gets the output_format of this ExportDetails.
        Specifies the format for the returned results.

        Allowed values for this property are: "CSV", "JSON"


        :return: The output_format of this ExportDetails.
        :rtype: str
        """
        return self._output_format

    @output_format.setter
    def output_format(self, output_format):
        """
        Sets the output_format of this ExportDetails.
        Specifies the format for the returned results.


        :param output_format: The output_format of this ExportDetails.
        :type: str
        """
        allowed_values = ["CSV", "JSON"]
        if not value_allowed_none_or_none_sentinel(output_format, allowed_values):
            raise ValueError(
                "Invalid value for `output_format`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._output_format = output_format

    @property
    def should_localize(self):
        """
        Gets the should_localize of this ExportDetails.
        Localize results, including header columns, List-Of-Values and timestamp values.


        :return: The should_localize of this ExportDetails.
        :rtype: bool
        """
        return self._should_localize

    @should_localize.setter
    def should_localize(self, should_localize):
        """
        Sets the should_localize of this ExportDetails.
        Localize results, including header columns, List-Of-Values and timestamp values.


        :param should_localize: The should_localize of this ExportDetails.
        :type: bool
        """
        self._should_localize = should_localize

    @property
    def should_use_acceleration(self):
        """
        Gets the should_use_acceleration of this ExportDetails.
        Controls if query should ignore pre-calculated results if available and only use raw data.


        :return: The should_use_acceleration of this ExportDetails.
        :rtype: bool
        """
        return self._should_use_acceleration

    @should_use_acceleration.setter
    def should_use_acceleration(self, should_use_acceleration):
        """
        Sets the should_use_acceleration of this ExportDetails.
        Controls if query should ignore pre-calculated results if available and only use raw data.


        :param should_use_acceleration: The should_use_acceleration of this ExportDetails.
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
