# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SubmitHistoricalMetricsDetails(object):
    """
    Post historical metric details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SubmitHistoricalMetricsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param historical_metrics:
            The value to assign to the historical_metrics property of this SubmitHistoricalMetricsDetails.
        :type historical_metrics: list[oci.cloud_bridge.models.HistoricalMetric]

        """
        self.swagger_types = {
            'historical_metrics': 'list[HistoricalMetric]'
        }

        self.attribute_map = {
            'historical_metrics': 'historicalMetrics'
        }

        self._historical_metrics = None

    @property
    def historical_metrics(self):
        """
        **[Required]** Gets the historical_metrics of this SubmitHistoricalMetricsDetails.
        List of asset historical metrics.


        :return: The historical_metrics of this SubmitHistoricalMetricsDetails.
        :rtype: list[oci.cloud_bridge.models.HistoricalMetric]
        """
        return self._historical_metrics

    @historical_metrics.setter
    def historical_metrics(self, historical_metrics):
        """
        Sets the historical_metrics of this SubmitHistoricalMetricsDetails.
        List of asset historical metrics.


        :param historical_metrics: The historical_metrics of this SubmitHistoricalMetricsDetails.
        :type: list[oci.cloud_bridge.models.HistoricalMetric]
        """
        self._historical_metrics = historical_metrics

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
