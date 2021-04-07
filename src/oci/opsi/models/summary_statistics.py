# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SummaryStatistics(object):
    """
    Contains common summary statistics.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SummaryStatistics object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param minimum:
            The value to assign to the minimum property of this SummaryStatistics.
        :type minimum: float

        :param maximum:
            The value to assign to the maximum property of this SummaryStatistics.
        :type maximum: float

        :param average:
            The value to assign to the average property of this SummaryStatistics.
        :type average: float

        :param median:
            The value to assign to the median property of this SummaryStatistics.
        :type median: float

        :param lower_quartile:
            The value to assign to the lower_quartile property of this SummaryStatistics.
        :type lower_quartile: float

        :param upper_quartile:
            The value to assign to the upper_quartile property of this SummaryStatistics.
        :type upper_quartile: float

        """
        self.swagger_types = {
            'minimum': 'float',
            'maximum': 'float',
            'average': 'float',
            'median': 'float',
            'lower_quartile': 'float',
            'upper_quartile': 'float'
        }

        self.attribute_map = {
            'minimum': 'minimum',
            'maximum': 'maximum',
            'average': 'average',
            'median': 'median',
            'lower_quartile': 'lowerQuartile',
            'upper_quartile': 'upperQuartile'
        }

        self._minimum = None
        self._maximum = None
        self._average = None
        self._median = None
        self._lower_quartile = None
        self._upper_quartile = None

    @property
    def minimum(self):
        """
        **[Required]** Gets the minimum of this SummaryStatistics.
        The smallest number in the data set.


        :return: The minimum of this SummaryStatistics.
        :rtype: float
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        """
        Sets the minimum of this SummaryStatistics.
        The smallest number in the data set.


        :param minimum: The minimum of this SummaryStatistics.
        :type: float
        """
        self._minimum = minimum

    @property
    def maximum(self):
        """
        **[Required]** Gets the maximum of this SummaryStatistics.
        The largest number in the data set.


        :return: The maximum of this SummaryStatistics.
        :rtype: float
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        """
        Sets the maximum of this SummaryStatistics.
        The largest number in the data set.


        :param maximum: The maximum of this SummaryStatistics.
        :type: float
        """
        self._maximum = maximum

    @property
    def average(self):
        """
        **[Required]** Gets the average of this SummaryStatistics.
        The average number in the data set.


        :return: The average of this SummaryStatistics.
        :rtype: float
        """
        return self._average

    @average.setter
    def average(self, average):
        """
        Sets the average of this SummaryStatistics.
        The average number in the data set.


        :param average: The average of this SummaryStatistics.
        :type: float
        """
        self._average = average

    @property
    def median(self):
        """
        **[Required]** Gets the median of this SummaryStatistics.
        The middle number in the data set.


        :return: The median of this SummaryStatistics.
        :rtype: float
        """
        return self._median

    @median.setter
    def median(self, median):
        """
        Sets the median of this SummaryStatistics.
        The middle number in the data set.


        :param median: The median of this SummaryStatistics.
        :type: float
        """
        self._median = median

    @property
    def lower_quartile(self):
        """
        **[Required]** Gets the lower_quartile of this SummaryStatistics.
        The middle number between the smallest number and the median of the data set. It's also known as the 25th quartile.


        :return: The lower_quartile of this SummaryStatistics.
        :rtype: float
        """
        return self._lower_quartile

    @lower_quartile.setter
    def lower_quartile(self, lower_quartile):
        """
        Sets the lower_quartile of this SummaryStatistics.
        The middle number between the smallest number and the median of the data set. It's also known as the 25th quartile.


        :param lower_quartile: The lower_quartile of this SummaryStatistics.
        :type: float
        """
        self._lower_quartile = lower_quartile

    @property
    def upper_quartile(self):
        """
        **[Required]** Gets the upper_quartile of this SummaryStatistics.
        The middle number between the median and the largest number of the data set. It's also known as the 75th quartile.


        :return: The upper_quartile of this SummaryStatistics.
        :rtype: float
        """
        return self._upper_quartile

    @upper_quartile.setter
    def upper_quartile(self, upper_quartile):
        """
        Sets the upper_quartile of this SummaryStatistics.
        The middle number between the median and the largest number of the data set. It's also known as the 75th quartile.


        :param upper_quartile: The upper_quartile of this SummaryStatistics.
        :type: float
        """
        self._upper_quartile = upper_quartile

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
