# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsSourceMetric(object):
    """
    LogAnalyticsSourceMetric
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsSourceMetric object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_metric_source_enabled:
            The value to assign to the is_metric_source_enabled property of this LogAnalyticsSourceMetric.
        :type is_metric_source_enabled: bool

        :param metric_name:
            The value to assign to the metric_name property of this LogAnalyticsSourceMetric.
        :type metric_name: str

        :param source_name:
            The value to assign to the source_name property of this LogAnalyticsSourceMetric.
        :type source_name: str

        :param entity_type:
            The value to assign to the entity_type property of this LogAnalyticsSourceMetric.
        :type entity_type: str

        """
        self.swagger_types = {
            'is_metric_source_enabled': 'bool',
            'metric_name': 'str',
            'source_name': 'str',
            'entity_type': 'str'
        }

        self.attribute_map = {
            'is_metric_source_enabled': 'isMetricSourceEnabled',
            'metric_name': 'metricName',
            'source_name': 'sourceName',
            'entity_type': 'entityType'
        }

        self._is_metric_source_enabled = None
        self._metric_name = None
        self._source_name = None
        self._entity_type = None

    @property
    def is_metric_source_enabled(self):
        """
        Gets the is_metric_source_enabled of this LogAnalyticsSourceMetric.
        A flag specifying whether or not the metric source is enabled.


        :return: The is_metric_source_enabled of this LogAnalyticsSourceMetric.
        :rtype: bool
        """
        return self._is_metric_source_enabled

    @is_metric_source_enabled.setter
    def is_metric_source_enabled(self, is_metric_source_enabled):
        """
        Sets the is_metric_source_enabled of this LogAnalyticsSourceMetric.
        A flag specifying whether or not the metric source is enabled.


        :param is_metric_source_enabled: The is_metric_source_enabled of this LogAnalyticsSourceMetric.
        :type: bool
        """
        self._is_metric_source_enabled = is_metric_source_enabled

    @property
    def metric_name(self):
        """
        Gets the metric_name of this LogAnalyticsSourceMetric.
        The metric name.


        :return: The metric_name of this LogAnalyticsSourceMetric.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """
        Sets the metric_name of this LogAnalyticsSourceMetric.
        The metric name.


        :param metric_name: The metric_name of this LogAnalyticsSourceMetric.
        :type: str
        """
        self._metric_name = metric_name

    @property
    def source_name(self):
        """
        Gets the source_name of this LogAnalyticsSourceMetric.
        The source internal name.


        :return: The source_name of this LogAnalyticsSourceMetric.
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        """
        Sets the source_name of this LogAnalyticsSourceMetric.
        The source internal name.


        :param source_name: The source_name of this LogAnalyticsSourceMetric.
        :type: str
        """
        self._source_name = source_name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this LogAnalyticsSourceMetric.
        The entity type.


        :return: The entity_type of this LogAnalyticsSourceMetric.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this LogAnalyticsSourceMetric.
        The entity type.


        :param entity_type: The entity_type of this LogAnalyticsSourceMetric.
        :type: str
        """
        self._entity_type = entity_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
