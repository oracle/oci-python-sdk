# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Metric(object):
    """
    A metric is a quantitative measurement of an entity.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Metric object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this Metric.
        :type name: str

        :param value_source:
            The value to assign to the value_source property of this Metric.
        :type value_source: str

        :param unit:
            The value to assign to the unit property of this Metric.
        :type unit: str

        :param description:
            The value to assign to the description property of this Metric.
        :type description: str

        """
        self.swagger_types = {
            'name': 'str',
            'value_source': 'str',
            'unit': 'str',
            'description': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'value_source': 'valueSource',
            'unit': 'unit',
            'description': 'description'
        }

        self._name = None
        self._value_source = None
        self._unit = None
        self._description = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this Metric.
        The name of the metric. This must be a known metric name.


        :return: The name of this Metric.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Metric.
        The name of the metric. This must be a known metric name.


        :param name: The name of this Metric.
        :type: str
        """
        self._name = name

    @property
    def value_source(self):
        """
        Gets the value_source of this Metric.
        This must not be set.


        :return: The value_source of this Metric.
        :rtype: str
        """
        return self._value_source

    @value_source.setter
    def value_source(self, value_source):
        """
        Sets the value_source of this Metric.
        This must not be set.


        :param value_source: The value_source of this Metric.
        :type: str
        """
        self._value_source = value_source

    @property
    def unit(self):
        """
        Gets the unit of this Metric.
        The unit of the metric.


        :return: The unit of this Metric.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        Sets the unit of this Metric.
        The unit of the metric.


        :param unit: The unit of this Metric.
        :type: str
        """
        self._unit = unit

    @property
    def description(self):
        """
        Gets the description of this Metric.
        A description of the metric.


        :return: The description of this Metric.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Metric.
        A description of the metric.


        :param description: The description of this Metric.
        :type: str
        """
        self._description = description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
