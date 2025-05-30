# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HeatWaveFleetByCategory(object):
    """
    The number of HeatWave clusters in the fleet, grouped by shape and Lakehouse-enabled status.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HeatWaveFleetByCategory object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this HeatWaveFleetByCategory.
        :type name: str

        :param value:
            The value to assign to the value property of this HeatWaveFleetByCategory.
        :type value: str

        :param count:
            The value to assign to the count property of this HeatWaveFleetByCategory.
        :type count: int

        """
        self.swagger_types = {
            'name': 'str',
            'value': 'str',
            'count': 'int'
        }
        self.attribute_map = {
            'name': 'name',
            'value': 'value',
            'count': 'count'
        }
        self._name = None
        self._value = None
        self._count = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this HeatWaveFleetByCategory.
        The name of the HeatWave fleet category.


        :return: The name of this HeatWaveFleetByCategory.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this HeatWaveFleetByCategory.
        The name of the HeatWave fleet category.


        :param name: The name of this HeatWaveFleetByCategory.
        :type: str
        """
        self._name = name

    @property
    def value(self):
        """
        **[Required]** Gets the value of this HeatWaveFleetByCategory.
        The value of the HeatWave fleet category.


        :return: The value of this HeatWaveFleetByCategory.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this HeatWaveFleetByCategory.
        The value of the HeatWave fleet category.


        :param value: The value of this HeatWaveFleetByCategory.
        :type: str
        """
        self._value = value

    @property
    def count(self):
        """
        **[Required]** Gets the count of this HeatWaveFleetByCategory.
        The number of matching HeatWave clusters.


        :return: The count of this HeatWaveFleetByCategory.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this HeatWaveFleetByCategory.
        The number of matching HeatWave clusters.


        :param count: The count of this HeatWaveFleetByCategory.
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
