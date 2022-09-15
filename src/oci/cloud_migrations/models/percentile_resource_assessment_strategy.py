# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .resource_assessment_strategy import ResourceAssessmentStrategy
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PercentileResourceAssessmentStrategy(ResourceAssessmentStrategy):
    """
    The strategy based on percentile usage.
    """

    #: A constant which can be used with the percentile property of a PercentileResourceAssessmentStrategy.
    #: This constant has a value of "P50"
    PERCENTILE_P50 = "P50"

    #: A constant which can be used with the percentile property of a PercentileResourceAssessmentStrategy.
    #: This constant has a value of "P90"
    PERCENTILE_P90 = "P90"

    #: A constant which can be used with the percentile property of a PercentileResourceAssessmentStrategy.
    #: This constant has a value of "P95"
    PERCENTILE_P95 = "P95"

    #: A constant which can be used with the percentile property of a PercentileResourceAssessmentStrategy.
    #: This constant has a value of "P99"
    PERCENTILE_P99 = "P99"

    #: A constant which can be used with the metric_time_window property of a PercentileResourceAssessmentStrategy.
    #: This constant has a value of "1d"
    METRIC_TIME_WINDOW_1D = "1d"

    #: A constant which can be used with the metric_time_window property of a PercentileResourceAssessmentStrategy.
    #: This constant has a value of "7d"
    METRIC_TIME_WINDOW_7D = "7d"

    #: A constant which can be used with the metric_time_window property of a PercentileResourceAssessmentStrategy.
    #: This constant has a value of "30d"
    METRIC_TIME_WINDOW_30D = "30d"

    def __init__(self, **kwargs):
        """
        Initializes a new PercentileResourceAssessmentStrategy object with values from keyword arguments. The default value of the :py:attr:`~oci.cloud_migrations.models.PercentileResourceAssessmentStrategy.strategy_type` attribute
        of this class is ``PERCENTILE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param resource_type:
            The value to assign to the resource_type property of this PercentileResourceAssessmentStrategy.
            Allowed values for this property are: "CPU", "MEMORY", "ALL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type resource_type: str

        :param strategy_type:
            The value to assign to the strategy_type property of this PercentileResourceAssessmentStrategy.
            Allowed values for this property are: "AS_IS", "AVERAGE", "PEAK", "PERCENTILE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type strategy_type: str

        :param percentile:
            The value to assign to the percentile property of this PercentileResourceAssessmentStrategy.
            Allowed values for this property are: "P50", "P90", "P95", "P99", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type percentile: str

        :param adjustment_multiplier:
            The value to assign to the adjustment_multiplier property of this PercentileResourceAssessmentStrategy.
        :type adjustment_multiplier: float

        :param metric_time_window:
            The value to assign to the metric_time_window property of this PercentileResourceAssessmentStrategy.
            Allowed values for this property are: "1d", "7d", "30d", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type metric_time_window: str

        """
        self.swagger_types = {
            'resource_type': 'str',
            'strategy_type': 'str',
            'percentile': 'str',
            'adjustment_multiplier': 'float',
            'metric_time_window': 'str'
        }

        self.attribute_map = {
            'resource_type': 'resourceType',
            'strategy_type': 'strategyType',
            'percentile': 'percentile',
            'adjustment_multiplier': 'adjustmentMultiplier',
            'metric_time_window': 'metricTimeWindow'
        }

        self._resource_type = None
        self._strategy_type = None
        self._percentile = None
        self._adjustment_multiplier = None
        self._metric_time_window = None
        self._strategy_type = 'PERCENTILE'

    @property
    def percentile(self):
        """
        **[Required]** Gets the percentile of this PercentileResourceAssessmentStrategy.
        Percentile value

        Allowed values for this property are: "P50", "P90", "P95", "P99", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The percentile of this PercentileResourceAssessmentStrategy.
        :rtype: str
        """
        return self._percentile

    @percentile.setter
    def percentile(self, percentile):
        """
        Sets the percentile of this PercentileResourceAssessmentStrategy.
        Percentile value


        :param percentile: The percentile of this PercentileResourceAssessmentStrategy.
        :type: str
        """
        allowed_values = ["P50", "P90", "P95", "P99"]
        if not value_allowed_none_or_none_sentinel(percentile, allowed_values):
            percentile = 'UNKNOWN_ENUM_VALUE'
        self._percentile = percentile

    @property
    def adjustment_multiplier(self):
        """
        Gets the adjustment_multiplier of this PercentileResourceAssessmentStrategy.
        The real resource usage is multiplied to this number before making any recommendation.


        :return: The adjustment_multiplier of this PercentileResourceAssessmentStrategy.
        :rtype: float
        """
        return self._adjustment_multiplier

    @adjustment_multiplier.setter
    def adjustment_multiplier(self, adjustment_multiplier):
        """
        Sets the adjustment_multiplier of this PercentileResourceAssessmentStrategy.
        The real resource usage is multiplied to this number before making any recommendation.


        :param adjustment_multiplier: The adjustment_multiplier of this PercentileResourceAssessmentStrategy.
        :type: float
        """
        self._adjustment_multiplier = adjustment_multiplier

    @property
    def metric_time_window(self):
        """
        Gets the metric_time_window of this PercentileResourceAssessmentStrategy.
        The current state of the migration plan.

        Allowed values for this property are: "1d", "7d", "30d", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The metric_time_window of this PercentileResourceAssessmentStrategy.
        :rtype: str
        """
        return self._metric_time_window

    @metric_time_window.setter
    def metric_time_window(self, metric_time_window):
        """
        Sets the metric_time_window of this PercentileResourceAssessmentStrategy.
        The current state of the migration plan.


        :param metric_time_window: The metric_time_window of this PercentileResourceAssessmentStrategy.
        :type: str
        """
        allowed_values = ["1d", "7d", "30d"]
        if not value_allowed_none_or_none_sentinel(metric_time_window, allowed_values):
            metric_time_window = 'UNKNOWN_ENUM_VALUE'
        self._metric_time_window = metric_time_window

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
