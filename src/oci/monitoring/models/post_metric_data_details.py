# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PostMetricDataDetails(object):
    """
    An array of metric objects containing raw metric data points to be posted to the Monitoring service.
    """

    #: A constant which can be used with the batch_atomicity property of a PostMetricDataDetails.
    #: This constant has a value of "ATOMIC"
    BATCH_ATOMICITY_ATOMIC = "ATOMIC"

    #: A constant which can be used with the batch_atomicity property of a PostMetricDataDetails.
    #: This constant has a value of "NON_ATOMIC"
    BATCH_ATOMICITY_NON_ATOMIC = "NON_ATOMIC"

    def __init__(self, **kwargs):
        """
        Initializes a new PostMetricDataDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric_data:
            The value to assign to the metric_data property of this PostMetricDataDetails.
        :type metric_data: list[MetricDataDetails]

        :param batch_atomicity:
            The value to assign to the batch_atomicity property of this PostMetricDataDetails.
            Allowed values for this property are: "ATOMIC", "NON_ATOMIC"
        :type batch_atomicity: str

        """
        self.swagger_types = {
            'metric_data': 'list[MetricDataDetails]',
            'batch_atomicity': 'str'
        }

        self.attribute_map = {
            'metric_data': 'metricData',
            'batch_atomicity': 'batchAtomicity'
        }

        self._metric_data = None
        self._batch_atomicity = None

    @property
    def metric_data(self):
        """
        **[Required]** Gets the metric_data of this PostMetricDataDetails.
        A metric object containing raw metric data points to be posted to the Monitoring service.


        :return: The metric_data of this PostMetricDataDetails.
        :rtype: list[MetricDataDetails]
        """
        return self._metric_data

    @metric_data.setter
    def metric_data(self, metric_data):
        """
        Sets the metric_data of this PostMetricDataDetails.
        A metric object containing raw metric data points to be posted to the Monitoring service.


        :param metric_data: The metric_data of this PostMetricDataDetails.
        :type: list[MetricDataDetails]
        """
        self._metric_data = metric_data

    @property
    def batch_atomicity(self):
        """
        Gets the batch_atomicity of this PostMetricDataDetails.
        Batch atomicity behavior. Requires either partial or full pass of input validation for
        metric objects in PostMetricData requests. The default value of NON_ATOMIC requires a
        partial pass: at least one metric object in the request must pass input validation, and
        any objects that failed validation are identified in the returned summary, along with
        their error messages. A value of ATOMIC requires a full pass: all metric objects in
        the request must pass input validation.

        Example: `NON_ATOMIC`

        Allowed values for this property are: "ATOMIC", "NON_ATOMIC"


        :return: The batch_atomicity of this PostMetricDataDetails.
        :rtype: str
        """
        return self._batch_atomicity

    @batch_atomicity.setter
    def batch_atomicity(self, batch_atomicity):
        """
        Sets the batch_atomicity of this PostMetricDataDetails.
        Batch atomicity behavior. Requires either partial or full pass of input validation for
        metric objects in PostMetricData requests. The default value of NON_ATOMIC requires a
        partial pass: at least one metric object in the request must pass input validation, and
        any objects that failed validation are identified in the returned summary, along with
        their error messages. A value of ATOMIC requires a full pass: all metric objects in
        the request must pass input validation.

        Example: `NON_ATOMIC`


        :param batch_atomicity: The batch_atomicity of this PostMetricDataDetails.
        :type: str
        """
        allowed_values = ["ATOMIC", "NON_ATOMIC"]
        if not value_allowed_none_or_none_sentinel(batch_atomicity, allowed_values):
            raise ValueError(
                "Invalid value for `batch_atomicity`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._batch_atomicity = batch_atomicity

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
