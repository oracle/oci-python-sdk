# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SummarizeMetricsDataDetails(object):
    """
    The request details for retrieving aggregated data.
    Use the query and optional properties to filter the returned results.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SummarizeMetricsDataDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param namespace:
            The value to assign to the namespace property of this SummarizeMetricsDataDetails.
        :type namespace: str

        :param resource_group:
            The value to assign to the resource_group property of this SummarizeMetricsDataDetails.
        :type resource_group: str

        :param query:
            The value to assign to the query property of this SummarizeMetricsDataDetails.
        :type query: str

        :param start_time:
            The value to assign to the start_time property of this SummarizeMetricsDataDetails.
        :type start_time: datetime

        :param end_time:
            The value to assign to the end_time property of this SummarizeMetricsDataDetails.
        :type end_time: datetime

        :param resolution:
            The value to assign to the resolution property of this SummarizeMetricsDataDetails.
        :type resolution: str

        """
        self.swagger_types = {
            'namespace': 'str',
            'resource_group': 'str',
            'query': 'str',
            'start_time': 'datetime',
            'end_time': 'datetime',
            'resolution': 'str'
        }

        self.attribute_map = {
            'namespace': 'namespace',
            'resource_group': 'resourceGroup',
            'query': 'query',
            'start_time': 'startTime',
            'end_time': 'endTime',
            'resolution': 'resolution'
        }

        self._namespace = None
        self._resource_group = None
        self._query = None
        self._start_time = None
        self._end_time = None
        self._resolution = None

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this SummarizeMetricsDataDetails.
        The source service or application to use when searching for metric data points to aggregate.

        Example: `oci_computeagent`


        :return: The namespace of this SummarizeMetricsDataDetails.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this SummarizeMetricsDataDetails.
        The source service or application to use when searching for metric data points to aggregate.

        Example: `oci_computeagent`


        :param namespace: The namespace of this SummarizeMetricsDataDetails.
        :type: str
        """
        self._namespace = namespace

    @property
    def resource_group(self):
        """
        Gets the resource_group of this SummarizeMetricsDataDetails.
        Resource group that you want to use as a filter. The specified resource group must exist in the definition of the posted metric. Only one resource group can be applied per metric.
        A valid resourceGroup value starts with an alphabetical character and includes only alphanumeric characters, periods (.), underscores (_), hyphens (-), and dollar signs ($).
        Avoid entering confidential information.

        Example: `frontend-fleet`


        :return: The resource_group of this SummarizeMetricsDataDetails.
        :rtype: str
        """
        return self._resource_group

    @resource_group.setter
    def resource_group(self, resource_group):
        """
        Sets the resource_group of this SummarizeMetricsDataDetails.
        Resource group that you want to use as a filter. The specified resource group must exist in the definition of the posted metric. Only one resource group can be applied per metric.
        A valid resourceGroup value starts with an alphabetical character and includes only alphanumeric characters, periods (.), underscores (_), hyphens (-), and dollar signs ($).
        Avoid entering confidential information.

        Example: `frontend-fleet`


        :param resource_group: The resource_group of this SummarizeMetricsDataDetails.
        :type: str
        """
        self._resource_group = resource_group

    @property
    def query(self):
        """
        **[Required]** Gets the query of this SummarizeMetricsDataDetails.
        The Monitoring Query Language (MQL) expression to use when searching for metric data points to
        aggregate. The query must specify a metric, statistic, and interval. Supported values for
        interval: `1m`-`60m` (also `1h`). You can optionally specify dimensions and grouping functions.
        Supported grouping functions: `grouping()`, `groupBy()`.

        Construct your query to avoid exceeding limits on returned data. See :class:`MetricData`.

        For details about Monitoring Query Language (MQL), see
        `Monitoring Query Language (MQL) Reference`__.
        For available dimensions, review the metric definition for the supported service.
        See `Supported Services`__.

        Example: `CpuUtilization[1m].sum()`

        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Reference/mql.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#SupportedServices


        :return: The query of this SummarizeMetricsDataDetails.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this SummarizeMetricsDataDetails.
        The Monitoring Query Language (MQL) expression to use when searching for metric data points to
        aggregate. The query must specify a metric, statistic, and interval. Supported values for
        interval: `1m`-`60m` (also `1h`). You can optionally specify dimensions and grouping functions.
        Supported grouping functions: `grouping()`, `groupBy()`.

        Construct your query to avoid exceeding limits on returned data. See :class:`MetricData`.

        For details about Monitoring Query Language (MQL), see
        `Monitoring Query Language (MQL) Reference`__.
        For available dimensions, review the metric definition for the supported service.
        See `Supported Services`__.

        Example: `CpuUtilization[1m].sum()`

        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Reference/mql.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#SupportedServices


        :param query: The query of this SummarizeMetricsDataDetails.
        :type: str
        """
        self._query = query

    @property
    def start_time(self):
        """
        Gets the start_time of this SummarizeMetricsDataDetails.
        The beginning of the time range to use when searching for metric data points.
        Format is defined by RFC3339. The response includes metric data points for the startTime.
        Default value: the timestamp 3 hours before the call was sent.

        Example: `2019-02-01T01:02:29.600Z`


        :return: The start_time of this SummarizeMetricsDataDetails.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this SummarizeMetricsDataDetails.
        The beginning of the time range to use when searching for metric data points.
        Format is defined by RFC3339. The response includes metric data points for the startTime.
        Default value: the timestamp 3 hours before the call was sent.

        Example: `2019-02-01T01:02:29.600Z`


        :param start_time: The start_time of this SummarizeMetricsDataDetails.
        :type: datetime
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """
        Gets the end_time of this SummarizeMetricsDataDetails.
        The end of the time range to use when searching for metric data points.
        Format is defined by RFC3339. The response excludes metric data points for the endTime.
        Default value: the timestamp representing when the call was sent.

        Example: `2019-02-01T02:02:29.600Z`


        :return: The end_time of this SummarizeMetricsDataDetails.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this SummarizeMetricsDataDetails.
        The end of the time range to use when searching for metric data points.
        Format is defined by RFC3339. The response excludes metric data points for the endTime.
        Default value: the timestamp representing when the call was sent.

        Example: `2019-02-01T02:02:29.600Z`


        :param end_time: The end_time of this SummarizeMetricsDataDetails.
        :type: datetime
        """
        self._end_time = end_time

    @property
    def resolution(self):
        """
        Gets the resolution of this SummarizeMetricsDataDetails.
        The time between calculated aggregation windows. Use with the query interval to vary the
        frequency at which aggregated data points are returned. For example, use a query interval of
        5 minutes with a resolution of 1 minute to retrieve five-minute aggregations at a one-minute
        frequency. The resolution must be equal or less than the interval in the query. The default
        resolution is 1m (one minute). Supported values: `1m`-`60m` (also `1h`).

        Example: `5m`


        :return: The resolution of this SummarizeMetricsDataDetails.
        :rtype: str
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """
        Sets the resolution of this SummarizeMetricsDataDetails.
        The time between calculated aggregation windows. Use with the query interval to vary the
        frequency at which aggregated data points are returned. For example, use a query interval of
        5 minutes with a resolution of 1 minute to retrieve five-minute aggregations at a one-minute
        frequency. The resolution must be equal or less than the interval in the query. The default
        resolution is 1m (one minute). Supported values: `1m`-`60m` (also `1h`).

        Example: `5m`


        :param resolution: The resolution of this SummarizeMetricsDataDetails.
        :type: str
        """
        self._resolution = resolution

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
