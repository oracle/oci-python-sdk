# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HistoricalMetricSummary(object):
    """
    Metric details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HistoricalMetricSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this HistoricalMetricSummary.
        :type name: str

        :param aggregation:
            The value to assign to the aggregation property of this HistoricalMetricSummary.
        :type aggregation: str

        :param value:
            The value to assign to the value property of this HistoricalMetricSummary.
        :type value: float

        :param time_created:
            The value to assign to the time_created property of this HistoricalMetricSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this HistoricalMetricSummary.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'name': 'str',
            'aggregation': 'str',
            'value': 'float',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'name': 'name',
            'aggregation': 'aggregation',
            'value': 'value',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._name = None
        self._aggregation = None
        self._value = None
        self._time_created = None
        self._time_updated = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this HistoricalMetricSummary.
        Metric name.


        :return: The name of this HistoricalMetricSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this HistoricalMetricSummary.
        Metric name.


        :param name: The name of this HistoricalMetricSummary.
        :type: str
        """
        self._name = name

    @property
    def aggregation(self):
        """
        **[Required]** Gets the aggregation of this HistoricalMetricSummary.
        Aggregation time interval.


        :return: The aggregation of this HistoricalMetricSummary.
        :rtype: str
        """
        return self._aggregation

    @aggregation.setter
    def aggregation(self, aggregation):
        """
        Sets the aggregation of this HistoricalMetricSummary.
        Aggregation time interval.


        :param aggregation: The aggregation of this HistoricalMetricSummary.
        :type: str
        """
        self._aggregation = aggregation

    @property
    def value(self):
        """
        **[Required]** Gets the value of this HistoricalMetricSummary.
        Aggregation value.


        :return: The value of this HistoricalMetricSummary.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this HistoricalMetricSummary.
        Aggregation value.


        :param value: The value of this HistoricalMetricSummary.
        :type: float
        """
        self._value = value

    @property
    def time_created(self):
        """
        Gets the time_created of this HistoricalMetricSummary.
        The time the HistoricalMetric was created. An RFC3339 formatted datetime string.


        :return: The time_created of this HistoricalMetricSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this HistoricalMetricSummary.
        The time the HistoricalMetric was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this HistoricalMetricSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this HistoricalMetricSummary.
        The time the HistoricalMetric was updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this HistoricalMetricSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this HistoricalMetricSummary.
        The time the HistoricalMetric was updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this HistoricalMetricSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
