# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HistoricalMetric(object):
    """
    Metric details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HistoricalMetric object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this HistoricalMetric.
        :type name: str

        :param aggregation:
            The value to assign to the aggregation property of this HistoricalMetric.
        :type aggregation: str

        :param value:
            The value to assign to the value property of this HistoricalMetric.
        :type value: float

        """
        self.swagger_types = {
            'name': 'str',
            'aggregation': 'str',
            'value': 'float'
        }

        self.attribute_map = {
            'name': 'name',
            'aggregation': 'aggregation',
            'value': 'value'
        }

        self._name = None
        self._aggregation = None
        self._value = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this HistoricalMetric.
        Metric name.


        :return: The name of this HistoricalMetric.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this HistoricalMetric.
        Metric name.


        :param name: The name of this HistoricalMetric.
        :type: str
        """
        self._name = name

    @property
    def aggregation(self):
        """
        **[Required]** Gets the aggregation of this HistoricalMetric.
        Aggregation time interval.


        :return: The aggregation of this HistoricalMetric.
        :rtype: str
        """
        return self._aggregation

    @aggregation.setter
    def aggregation(self, aggregation):
        """
        Sets the aggregation of this HistoricalMetric.
        Aggregation time interval.


        :param aggregation: The aggregation of this HistoricalMetric.
        :type: str
        """
        self._aggregation = aggregation

    @property
    def value(self):
        """
        **[Required]** Gets the value of this HistoricalMetric.
        Aggregation value.


        :return: The value of this HistoricalMetric.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this HistoricalMetric.
        Aggregation value.


        :param value: The value of this HistoricalMetric.
        :type: float
        """
        self._value = value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
