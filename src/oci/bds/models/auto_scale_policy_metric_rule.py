# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutoScalePolicyMetricRule(object):
    """
    Metric and threshold details for triggering an autoscaling action
    """

    #: A constant which can be used with the metric_type property of a AutoScalePolicyMetricRule.
    #: This constant has a value of "CPU_UTILIZATION"
    METRIC_TYPE_CPU_UTILIZATION = "CPU_UTILIZATION"

    def __init__(self, **kwargs):
        """
        Initializes a new AutoScalePolicyMetricRule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric_type:
            The value to assign to the metric_type property of this AutoScalePolicyMetricRule.
            Allowed values for this property are: "CPU_UTILIZATION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type metric_type: str

        :param threshold:
            The value to assign to the threshold property of this AutoScalePolicyMetricRule.
        :type threshold: oci.bds.models.MetricThresholdRule

        """
        self.swagger_types = {
            'metric_type': 'str',
            'threshold': 'MetricThresholdRule'
        }

        self.attribute_map = {
            'metric_type': 'metricType',
            'threshold': 'threshold'
        }

        self._metric_type = None
        self._threshold = None

    @property
    def metric_type(self):
        """
        **[Required]** Gets the metric_type of this AutoScalePolicyMetricRule.
        Allowed value is CPU_UTILIZATION currently

        Allowed values for this property are: "CPU_UTILIZATION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The metric_type of this AutoScalePolicyMetricRule.
        :rtype: str
        """
        return self._metric_type

    @metric_type.setter
    def metric_type(self, metric_type):
        """
        Sets the metric_type of this AutoScalePolicyMetricRule.
        Allowed value is CPU_UTILIZATION currently


        :param metric_type: The metric_type of this AutoScalePolicyMetricRule.
        :type: str
        """
        allowed_values = ["CPU_UTILIZATION"]
        if not value_allowed_none_or_none_sentinel(metric_type, allowed_values):
            metric_type = 'UNKNOWN_ENUM_VALUE'
        self._metric_type = metric_type

    @property
    def threshold(self):
        """
        **[Required]** Gets the threshold of this AutoScalePolicyMetricRule.

        :return: The threshold of this AutoScalePolicyMetricRule.
        :rtype: oci.bds.models.MetricThresholdRule
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """
        Sets the threshold of this AutoScalePolicyMetricRule.

        :param threshold: The threshold of this AutoScalePolicyMetricRule.
        :type: oci.bds.models.MetricThresholdRule
        """
        self._threshold = threshold

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
