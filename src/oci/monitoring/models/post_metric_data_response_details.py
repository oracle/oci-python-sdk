# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PostMetricDataResponseDetails(object):
    """
    The response object returned from a PostMetricData operation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PostMetricDataResponseDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param failed_metrics_count:
            The value to assign to the failed_metrics_count property of this PostMetricDataResponseDetails.
        :type failed_metrics_count: int

        :param failed_metrics:
            The value to assign to the failed_metrics property of this PostMetricDataResponseDetails.
        :type failed_metrics: list[oci.monitoring.models.FailedMetricRecord]

        """
        self.swagger_types = {
            'failed_metrics_count': 'int',
            'failed_metrics': 'list[FailedMetricRecord]'
        }

        self.attribute_map = {
            'failed_metrics_count': 'failedMetricsCount',
            'failed_metrics': 'failedMetrics'
        }

        self._failed_metrics_count = None
        self._failed_metrics = None

    @property
    def failed_metrics_count(self):
        """
        **[Required]** Gets the failed_metrics_count of this PostMetricDataResponseDetails.
        The number of metric objects that failed input validation.


        :return: The failed_metrics_count of this PostMetricDataResponseDetails.
        :rtype: int
        """
        return self._failed_metrics_count

    @failed_metrics_count.setter
    def failed_metrics_count(self, failed_metrics_count):
        """
        Sets the failed_metrics_count of this PostMetricDataResponseDetails.
        The number of metric objects that failed input validation.


        :param failed_metrics_count: The failed_metrics_count of this PostMetricDataResponseDetails.
        :type: int
        """
        self._failed_metrics_count = failed_metrics_count

    @property
    def failed_metrics(self):
        """
        Gets the failed_metrics of this PostMetricDataResponseDetails.
        A list of records identifying metric objects that failed input validation
        and the reasons for the failures.


        :return: The failed_metrics of this PostMetricDataResponseDetails.
        :rtype: list[oci.monitoring.models.FailedMetricRecord]
        """
        return self._failed_metrics

    @failed_metrics.setter
    def failed_metrics(self, failed_metrics):
        """
        Sets the failed_metrics of this PostMetricDataResponseDetails.
        A list of records identifying metric objects that failed input validation
        and the reasons for the failures.


        :param failed_metrics: The failed_metrics of this PostMetricDataResponseDetails.
        :type: list[oci.monitoring.models.FailedMetricRecord]
        """
        self._failed_metrics = failed_metrics

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
