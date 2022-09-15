# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AssetAggregation(object):
    """
    The result of an analytics aggregation on a set of assets.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AssetAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param dimensions:
            The value to assign to the dimensions property of this AssetAggregation.
        :type dimensions: dict(str, str)

        :param count:
            The value to assign to the count property of this AssetAggregation.
        :type count: int

        :param max:
            The value to assign to the max property of this AssetAggregation.
        :type max: float

        :param mean:
            The value to assign to the mean property of this AssetAggregation.
        :type mean: float

        :param min:
            The value to assign to the min property of this AssetAggregation.
        :type min: float

        :param sum:
            The value to assign to the sum property of this AssetAggregation.
        :type sum: float

        :param aggregated_property:
            The value to assign to the aggregated_property property of this AssetAggregation.
        :type aggregated_property: str

        """
        self.swagger_types = {
            'dimensions': 'dict(str, str)',
            'count': 'int',
            'max': 'float',
            'mean': 'float',
            'min': 'float',
            'sum': 'float',
            'aggregated_property': 'str'
        }

        self.attribute_map = {
            'dimensions': 'dimensions',
            'count': 'count',
            'max': 'max',
            'mean': 'mean',
            'min': 'min',
            'sum': 'sum',
            'aggregated_property': 'aggregatedProperty'
        }

        self._dimensions = None
        self._count = None
        self._max = None
        self._mean = None
        self._min = None
        self._sum = None
        self._aggregated_property = None

    @property
    def dimensions(self):
        """
        Gets the dimensions of this AssetAggregation.
        The dimensions along which assets can be aggregated for analytics.


        :return: The dimensions of this AssetAggregation.
        :rtype: dict(str, str)
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """
        Sets the dimensions of this AssetAggregation.
        The dimensions along which assets can be aggregated for analytics.


        :param dimensions: The dimensions of this AssetAggregation.
        :type: dict(str, str)
        """
        self._dimensions = dimensions

    @property
    def count(self):
        """
        Gets the count of this AssetAggregation.
        Returns the total number of observations from the group of assets.


        :return: The count of this AssetAggregation.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this AssetAggregation.
        Returns the total number of observations from the group of assets.


        :param count: The count of this AssetAggregation.
        :type: int
        """
        self._count = count

    @property
    def max(self):
        """
        Gets the max of this AssetAggregation.
        Returns the highest value from all the assets.


        :return: The max of this AssetAggregation.
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """
        Sets the max of this AssetAggregation.
        Returns the highest value from all the assets.


        :param max: The max of this AssetAggregation.
        :type: float
        """
        self._max = max

    @property
    def mean(self):
        """
        Gets the mean of this AssetAggregation.
        Returns the value of sum divided by count from the group of assets.


        :return: The mean of this AssetAggregation.
        :rtype: float
        """
        return self._mean

    @mean.setter
    def mean(self, mean):
        """
        Sets the mean of this AssetAggregation.
        Returns the value of sum divided by count from the group of assets.


        :param mean: The mean of this AssetAggregation.
        :type: float
        """
        self._mean = mean

    @property
    def min(self):
        """
        Gets the min of this AssetAggregation.
        Returns the lowest value from the group of assets.


        :return: The min of this AssetAggregation.
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """
        Sets the min of this AssetAggregation.
        Returns the lowest value from the group of assets.


        :param min: The min of this AssetAggregation.
        :type: float
        """
        self._min = min

    @property
    def sum(self):
        """
        Gets the sum of this AssetAggregation.
        Returns all values added together from the group of assets.


        :return: The sum of this AssetAggregation.
        :rtype: float
        """
        return self._sum

    @sum.setter
    def sum(self, sum):
        """
        Sets the sum of this AssetAggregation.
        Returns all values added together from the group of assets.


        :param sum: The sum of this AssetAggregation.
        :type: float
        """
        self._sum = sum

    @property
    def aggregated_property(self):
        """
        **[Required]** Gets the aggregated_property of this AssetAggregation.
        Aggregated property.


        :return: The aggregated_property of this AssetAggregation.
        :rtype: str
        """
        return self._aggregated_property

    @aggregated_property.setter
    def aggregated_property(self, aggregated_property):
        """
        Sets the aggregated_property of this AssetAggregation.
        Aggregated property.


        :param aggregated_property: The aggregated_property of this AssetAggregation.
        :type: str
        """
        self._aggregated_property = aggregated_property

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
