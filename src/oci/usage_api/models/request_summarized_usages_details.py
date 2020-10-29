# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RequestSummarizedUsagesDetails(object):
    """
    Details for the '/usage' query.
    """

    #: A constant which can be used with the granularity property of a RequestSummarizedUsagesDetails.
    #: This constant has a value of "HOURLY"
    GRANULARITY_HOURLY = "HOURLY"

    #: A constant which can be used with the granularity property of a RequestSummarizedUsagesDetails.
    #: This constant has a value of "DAILY"
    GRANULARITY_DAILY = "DAILY"

    #: A constant which can be used with the granularity property of a RequestSummarizedUsagesDetails.
    #: This constant has a value of "MONTHLY"
    GRANULARITY_MONTHLY = "MONTHLY"

    #: A constant which can be used with the granularity property of a RequestSummarizedUsagesDetails.
    #: This constant has a value of "TOTAL"
    GRANULARITY_TOTAL = "TOTAL"

    #: A constant which can be used with the query_type property of a RequestSummarizedUsagesDetails.
    #: This constant has a value of "USAGE"
    QUERY_TYPE_USAGE = "USAGE"

    #: A constant which can be used with the query_type property of a RequestSummarizedUsagesDetails.
    #: This constant has a value of "COST"
    QUERY_TYPE_COST = "COST"

    def __init__(self, **kwargs):
        """
        Initializes a new RequestSummarizedUsagesDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param tenant_id:
            The value to assign to the tenant_id property of this RequestSummarizedUsagesDetails.
        :type tenant_id: str

        :param time_usage_started:
            The value to assign to the time_usage_started property of this RequestSummarizedUsagesDetails.
        :type time_usage_started: datetime

        :param time_usage_ended:
            The value to assign to the time_usage_ended property of this RequestSummarizedUsagesDetails.
        :type time_usage_ended: datetime

        :param granularity:
            The value to assign to the granularity property of this RequestSummarizedUsagesDetails.
            Allowed values for this property are: "HOURLY", "DAILY", "MONTHLY", "TOTAL"
        :type granularity: str

        :param query_type:
            The value to assign to the query_type property of this RequestSummarizedUsagesDetails.
            Allowed values for this property are: "USAGE", "COST"
        :type query_type: str

        :param group_by:
            The value to assign to the group_by property of this RequestSummarizedUsagesDetails.
        :type group_by: list[str]

        :param compartment_depth:
            The value to assign to the compartment_depth property of this RequestSummarizedUsagesDetails.
        :type compartment_depth: float

        :param filter:
            The value to assign to the filter property of this RequestSummarizedUsagesDetails.
        :type filter: Filter

        """
        self.swagger_types = {
            'tenant_id': 'str',
            'time_usage_started': 'datetime',
            'time_usage_ended': 'datetime',
            'granularity': 'str',
            'query_type': 'str',
            'group_by': 'list[str]',
            'compartment_depth': 'float',
            'filter': 'Filter'
        }

        self.attribute_map = {
            'tenant_id': 'tenantId',
            'time_usage_started': 'timeUsageStarted',
            'time_usage_ended': 'timeUsageEnded',
            'granularity': 'granularity',
            'query_type': 'queryType',
            'group_by': 'groupBy',
            'compartment_depth': 'compartmentDepth',
            'filter': 'filter'
        }

        self._tenant_id = None
        self._time_usage_started = None
        self._time_usage_ended = None
        self._granularity = None
        self._query_type = None
        self._group_by = None
        self._compartment_depth = None
        self._filter = None

    @property
    def tenant_id(self):
        """
        **[Required]** Gets the tenant_id of this RequestSummarizedUsagesDetails.
        Tenant ID


        :return: The tenant_id of this RequestSummarizedUsagesDetails.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """
        Sets the tenant_id of this RequestSummarizedUsagesDetails.
        Tenant ID


        :param tenant_id: The tenant_id of this RequestSummarizedUsagesDetails.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def time_usage_started(self):
        """
        **[Required]** Gets the time_usage_started of this RequestSummarizedUsagesDetails.
        The usage start time.


        :return: The time_usage_started of this RequestSummarizedUsagesDetails.
        :rtype: datetime
        """
        return self._time_usage_started

    @time_usage_started.setter
    def time_usage_started(self, time_usage_started):
        """
        Sets the time_usage_started of this RequestSummarizedUsagesDetails.
        The usage start time.


        :param time_usage_started: The time_usage_started of this RequestSummarizedUsagesDetails.
        :type: datetime
        """
        self._time_usage_started = time_usage_started

    @property
    def time_usage_ended(self):
        """
        **[Required]** Gets the time_usage_ended of this RequestSummarizedUsagesDetails.
        The usage end time.


        :return: The time_usage_ended of this RequestSummarizedUsagesDetails.
        :rtype: datetime
        """
        return self._time_usage_ended

    @time_usage_ended.setter
    def time_usage_ended(self, time_usage_ended):
        """
        Sets the time_usage_ended of this RequestSummarizedUsagesDetails.
        The usage end time.


        :param time_usage_ended: The time_usage_ended of this RequestSummarizedUsagesDetails.
        :type: datetime
        """
        self._time_usage_ended = time_usage_ended

    @property
    def granularity(self):
        """
        **[Required]** Gets the granularity of this RequestSummarizedUsagesDetails.
        The usage granularity.
        HOURLY - Hourly data aggregation.
        DAILY - Daily data aggregation.
        MONTHLY - Monthly data aggregation.
        TOTAL - Not yet supported.

        Allowed values for this property are: "HOURLY", "DAILY", "MONTHLY", "TOTAL"


        :return: The granularity of this RequestSummarizedUsagesDetails.
        :rtype: str
        """
        return self._granularity

    @granularity.setter
    def granularity(self, granularity):
        """
        Sets the granularity of this RequestSummarizedUsagesDetails.
        The usage granularity.
        HOURLY - Hourly data aggregation.
        DAILY - Daily data aggregation.
        MONTHLY - Monthly data aggregation.
        TOTAL - Not yet supported.


        :param granularity: The granularity of this RequestSummarizedUsagesDetails.
        :type: str
        """
        allowed_values = ["HOURLY", "DAILY", "MONTHLY", "TOTAL"]
        if not value_allowed_none_or_none_sentinel(granularity, allowed_values):
            raise ValueError(
                "Invalid value for `granularity`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._granularity = granularity

    @property
    def query_type(self):
        """
        Gets the query_type of this RequestSummarizedUsagesDetails.
        The query usage type.
        Usage - Query the usage data.
        Cost - Query the cost/billing data.

        Allowed values for this property are: "USAGE", "COST"


        :return: The query_type of this RequestSummarizedUsagesDetails.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        """
        Sets the query_type of this RequestSummarizedUsagesDetails.
        The query usage type.
        Usage - Query the usage data.
        Cost - Query the cost/billing data.


        :param query_type: The query_type of this RequestSummarizedUsagesDetails.
        :type: str
        """
        allowed_values = ["USAGE", "COST"]
        if not value_allowed_none_or_none_sentinel(query_type, allowed_values):
            raise ValueError(
                "Invalid value for `query_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._query_type = query_type

    @property
    def group_by(self):
        """
        Gets the group_by of this RequestSummarizedUsagesDetails.
        Aggregate the result by.
        example:
          `[\"service\"]`


        :return: The group_by of this RequestSummarizedUsagesDetails.
        :rtype: list[str]
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        """
        Sets the group_by of this RequestSummarizedUsagesDetails.
        Aggregate the result by.
        example:
          `[\"service\"]`


        :param group_by: The group_by of this RequestSummarizedUsagesDetails.
        :type: list[str]
        """
        self._group_by = group_by

    @property
    def compartment_depth(self):
        """
        Gets the compartment_depth of this RequestSummarizedUsagesDetails.
        The compartment depth level.


        :return: The compartment_depth of this RequestSummarizedUsagesDetails.
        :rtype: float
        """
        return self._compartment_depth

    @compartment_depth.setter
    def compartment_depth(self, compartment_depth):
        """
        Sets the compartment_depth of this RequestSummarizedUsagesDetails.
        The compartment depth level.


        :param compartment_depth: The compartment_depth of this RequestSummarizedUsagesDetails.
        :type: float
        """
        self._compartment_depth = compartment_depth

    @property
    def filter(self):
        """
        Gets the filter of this RequestSummarizedUsagesDetails.

        :return: The filter of this RequestSummarizedUsagesDetails.
        :rtype: Filter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """
        Sets the filter of this RequestSummarizedUsagesDetails.

        :param filter: The filter of this RequestSummarizedUsagesDetails.
        :type: Filter
        """
        self._filter = filter

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
