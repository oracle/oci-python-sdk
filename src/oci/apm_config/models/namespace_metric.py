# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NamespaceMetric(object):
    """
    Metric associated with a namespace.
    """

    #: A constant which can be used with the type property of a NamespaceMetric.
    #: This constant has a value of "COUNTER"
    TYPE_COUNTER = "COUNTER"

    #: A constant which can be used with the type property of a NamespaceMetric.
    #: This constant has a value of "GAUGE"
    TYPE_GAUGE = "GAUGE"

    def __init__(self, **kwargs):
        """
        Initializes a new NamespaceMetric object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this NamespaceMetric.
        :type name: str

        :param type:
            The value to assign to the type property of this NamespaceMetric.
            Allowed values for this property are: "COUNTER", "GAUGE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param unit:
            The value to assign to the unit property of this NamespaceMetric.
        :type unit: str

        """
        self.swagger_types = {
            'name': 'str',
            'type': 'str',
            'unit': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'type': 'type',
            'unit': 'unit'
        }

        self._name = None
        self._type = None
        self._unit = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this NamespaceMetric.
        Name of the metric.


        :return: The name of this NamespaceMetric.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this NamespaceMetric.
        Name of the metric.


        :param name: The name of this NamespaceMetric.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this NamespaceMetric.
        Type of metric.

        Allowed values for this property are: "COUNTER", "GAUGE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this NamespaceMetric.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this NamespaceMetric.
        Type of metric.


        :param type: The type of this NamespaceMetric.
        :type: str
        """
        allowed_values = ["COUNTER", "GAUGE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def unit(self):
        """
        Gets the unit of this NamespaceMetric.
        Unit of the metric.


        :return: The unit of this NamespaceMetric.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        Sets the unit of this NamespaceMetric.
        Unit of the metric.


        :param unit: The unit of this NamespaceMetric.
        :type: str
        """
        self._unit = unit

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
