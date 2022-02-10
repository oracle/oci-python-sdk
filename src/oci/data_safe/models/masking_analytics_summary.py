# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MaskingAnalyticsSummary(object):
    """
    Summary of masking analytics data.
    """

    #: A constant which can be used with the metric_name property of a MaskingAnalyticsSummary.
    #: This constant has a value of "MASKING_POLICY"
    METRIC_NAME_MASKING_POLICY = "MASKING_POLICY"

    #: A constant which can be used with the metric_name property of a MaskingAnalyticsSummary.
    #: This constant has a value of "MASKING_DATABASE"
    METRIC_NAME_MASKING_DATABASE = "MASKING_DATABASE"

    #: A constant which can be used with the metric_name property of a MaskingAnalyticsSummary.
    #: This constant has a value of "MASKING_WORK_REQUEST"
    METRIC_NAME_MASKING_WORK_REQUEST = "MASKING_WORK_REQUEST"

    #: A constant which can be used with the metric_name property of a MaskingAnalyticsSummary.
    #: This constant has a value of "MASKED_SENSITIVE_TYPE"
    METRIC_NAME_MASKED_SENSITIVE_TYPE = "MASKED_SENSITIVE_TYPE"

    #: A constant which can be used with the metric_name property of a MaskingAnalyticsSummary.
    #: This constant has a value of "MASKED_SCHEMA"
    METRIC_NAME_MASKED_SCHEMA = "MASKED_SCHEMA"

    #: A constant which can be used with the metric_name property of a MaskingAnalyticsSummary.
    #: This constant has a value of "MASKED_TABLE"
    METRIC_NAME_MASKED_TABLE = "MASKED_TABLE"

    #: A constant which can be used with the metric_name property of a MaskingAnalyticsSummary.
    #: This constant has a value of "MASKED_COLUMN"
    METRIC_NAME_MASKED_COLUMN = "MASKED_COLUMN"

    #: A constant which can be used with the metric_name property of a MaskingAnalyticsSummary.
    #: This constant has a value of "MASKED_DATA_VALUE"
    METRIC_NAME_MASKED_DATA_VALUE = "MASKED_DATA_VALUE"

    def __init__(self, **kwargs):
        """
        Initializes a new MaskingAnalyticsSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric_name:
            The value to assign to the metric_name property of this MaskingAnalyticsSummary.
            Allowed values for this property are: "MASKING_POLICY", "MASKING_DATABASE", "MASKING_WORK_REQUEST", "MASKED_SENSITIVE_TYPE", "MASKED_SCHEMA", "MASKED_TABLE", "MASKED_COLUMN", "MASKED_DATA_VALUE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type metric_name: str

        :param dimensions:
            The value to assign to the dimensions property of this MaskingAnalyticsSummary.
        :type dimensions: oci.data_safe.models.MaskingAnalyticsDimensions

        :param count:
            The value to assign to the count property of this MaskingAnalyticsSummary.
        :type count: int

        """
        self.swagger_types = {
            'metric_name': 'str',
            'dimensions': 'MaskingAnalyticsDimensions',
            'count': 'int'
        }

        self.attribute_map = {
            'metric_name': 'metricName',
            'dimensions': 'dimensions',
            'count': 'count'
        }

        self._metric_name = None
        self._dimensions = None
        self._count = None

    @property
    def metric_name(self):
        """
        **[Required]** Gets the metric_name of this MaskingAnalyticsSummary.
        The name of the aggregation metric.

        Allowed values for this property are: "MASKING_POLICY", "MASKING_DATABASE", "MASKING_WORK_REQUEST", "MASKED_SENSITIVE_TYPE", "MASKED_SCHEMA", "MASKED_TABLE", "MASKED_COLUMN", "MASKED_DATA_VALUE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The metric_name of this MaskingAnalyticsSummary.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """
        Sets the metric_name of this MaskingAnalyticsSummary.
        The name of the aggregation metric.


        :param metric_name: The metric_name of this MaskingAnalyticsSummary.
        :type: str
        """
        allowed_values = ["MASKING_POLICY", "MASKING_DATABASE", "MASKING_WORK_REQUEST", "MASKED_SENSITIVE_TYPE", "MASKED_SCHEMA", "MASKED_TABLE", "MASKED_COLUMN", "MASKED_DATA_VALUE"]
        if not value_allowed_none_or_none_sentinel(metric_name, allowed_values):
            metric_name = 'UNKNOWN_ENUM_VALUE'
        self._metric_name = metric_name

    @property
    def dimensions(self):
        """
        Gets the dimensions of this MaskingAnalyticsSummary.

        :return: The dimensions of this MaskingAnalyticsSummary.
        :rtype: oci.data_safe.models.MaskingAnalyticsDimensions
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """
        Sets the dimensions of this MaskingAnalyticsSummary.

        :param dimensions: The dimensions of this MaskingAnalyticsSummary.
        :type: oci.data_safe.models.MaskingAnalyticsDimensions
        """
        self._dimensions = dimensions

    @property
    def count(self):
        """
        **[Required]** Gets the count of this MaskingAnalyticsSummary.
        The total count for the aggregation metric.


        :return: The count of this MaskingAnalyticsSummary.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this MaskingAnalyticsSummary.
        The total count for the aggregation metric.


        :param count: The count of this MaskingAnalyticsSummary.
        :type: int
        """
        self._count = count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
