# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .attribute_profile_result import AttributeProfileResult
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NumericAttribute(AttributeProfileResult):
    """
    A summary of profiling results of a specefic attribute.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NumericAttribute object with values from keyword arguments. The default value of the :py:attr:`~oci.data_connectivity.models.NumericAttribute.type` attribute
        of this class is ``NUMERIC`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this NumericAttribute.
        :type type: object

        :param name:
            The value to assign to the name property of this NumericAttribute.
        :type name: str

        :param min:
            The value to assign to the min property of this NumericAttribute.
        :type min: oci.data_connectivity.models.ProfileStat

        :param max:
            The value to assign to the max property of this NumericAttribute.
        :type max: oci.data_connectivity.models.ProfileStat

        :param null_count:
            The value to assign to the null_count property of this NumericAttribute.
        :type null_count: oci.data_connectivity.models.ProfileStat

        :param distinct_count:
            The value to assign to the distinct_count property of this NumericAttribute.
        :type distinct_count: oci.data_connectivity.models.ProfileStat

        :param unique_count:
            The value to assign to the unique_count property of this NumericAttribute.
        :type unique_count: oci.data_connectivity.models.ProfileStat

        :param duplicate_count:
            The value to assign to the duplicate_count property of this NumericAttribute.
        :type duplicate_count: oci.data_connectivity.models.ProfileStat

        :param value_frequencies:
            The value to assign to the value_frequencies property of this NumericAttribute.
        :type value_frequencies: list[oci.data_connectivity.models.ObjectFreqStat]

        :param mean:
            The value to assign to the mean property of this NumericAttribute.
        :type mean: oci.data_connectivity.models.ProfileStat

        :param median:
            The value to assign to the median property of this NumericAttribute.
        :type median: oci.data_connectivity.models.ProfileStat

        :param standard_deviation:
            The value to assign to the standard_deviation property of this NumericAttribute.
        :type standard_deviation: oci.data_connectivity.models.ProfileStat

        :param variance:
            The value to assign to the variance property of this NumericAttribute.
        :type variance: oci.data_connectivity.models.ProfileStat

        :param outlier:
            The value to assign to the outlier property of this NumericAttribute.
        :type outlier: oci.data_connectivity.models.Outlier

        :param histogram:
            The value to assign to the histogram property of this NumericAttribute.
        :type histogram: oci.data_connectivity.models.Histogram

        :param pattern_frequencies:
            The value to assign to the pattern_frequencies property of this NumericAttribute.
        :type pattern_frequencies: list[oci.data_connectivity.models.ObjectFreqStat]

        """
        self.swagger_types = {
            'type': 'object',
            'name': 'str',
            'min': 'ProfileStat',
            'max': 'ProfileStat',
            'null_count': 'ProfileStat',
            'distinct_count': 'ProfileStat',
            'unique_count': 'ProfileStat',
            'duplicate_count': 'ProfileStat',
            'value_frequencies': 'list[ObjectFreqStat]',
            'mean': 'ProfileStat',
            'median': 'ProfileStat',
            'standard_deviation': 'ProfileStat',
            'variance': 'ProfileStat',
            'outlier': 'Outlier',
            'histogram': 'Histogram',
            'pattern_frequencies': 'list[ObjectFreqStat]'
        }

        self.attribute_map = {
            'type': 'type',
            'name': 'name',
            'min': 'min',
            'max': 'max',
            'null_count': 'nullCount',
            'distinct_count': 'distinctCount',
            'unique_count': 'uniqueCount',
            'duplicate_count': 'duplicateCount',
            'value_frequencies': 'valueFrequencies',
            'mean': 'mean',
            'median': 'median',
            'standard_deviation': 'standardDeviation',
            'variance': 'variance',
            'outlier': 'outlier',
            'histogram': 'histogram',
            'pattern_frequencies': 'patternFrequencies'
        }

        self._type = None
        self._name = None
        self._min = None
        self._max = None
        self._null_count = None
        self._distinct_count = None
        self._unique_count = None
        self._duplicate_count = None
        self._value_frequencies = None
        self._mean = None
        self._median = None
        self._standard_deviation = None
        self._variance = None
        self._outlier = None
        self._histogram = None
        self._pattern_frequencies = None
        self._type = 'NUMERIC'

    @property
    def mean(self):
        """
        Gets the mean of this NumericAttribute.

        :return: The mean of this NumericAttribute.
        :rtype: oci.data_connectivity.models.ProfileStat
        """
        return self._mean

    @mean.setter
    def mean(self, mean):
        """
        Sets the mean of this NumericAttribute.

        :param mean: The mean of this NumericAttribute.
        :type: oci.data_connectivity.models.ProfileStat
        """
        self._mean = mean

    @property
    def median(self):
        """
        Gets the median of this NumericAttribute.

        :return: The median of this NumericAttribute.
        :rtype: oci.data_connectivity.models.ProfileStat
        """
        return self._median

    @median.setter
    def median(self, median):
        """
        Sets the median of this NumericAttribute.

        :param median: The median of this NumericAttribute.
        :type: oci.data_connectivity.models.ProfileStat
        """
        self._median = median

    @property
    def standard_deviation(self):
        """
        Gets the standard_deviation of this NumericAttribute.

        :return: The standard_deviation of this NumericAttribute.
        :rtype: oci.data_connectivity.models.ProfileStat
        """
        return self._standard_deviation

    @standard_deviation.setter
    def standard_deviation(self, standard_deviation):
        """
        Sets the standard_deviation of this NumericAttribute.

        :param standard_deviation: The standard_deviation of this NumericAttribute.
        :type: oci.data_connectivity.models.ProfileStat
        """
        self._standard_deviation = standard_deviation

    @property
    def variance(self):
        """
        Gets the variance of this NumericAttribute.

        :return: The variance of this NumericAttribute.
        :rtype: oci.data_connectivity.models.ProfileStat
        """
        return self._variance

    @variance.setter
    def variance(self, variance):
        """
        Sets the variance of this NumericAttribute.

        :param variance: The variance of this NumericAttribute.
        :type: oci.data_connectivity.models.ProfileStat
        """
        self._variance = variance

    @property
    def outlier(self):
        """
        Gets the outlier of this NumericAttribute.

        :return: The outlier of this NumericAttribute.
        :rtype: oci.data_connectivity.models.Outlier
        """
        return self._outlier

    @outlier.setter
    def outlier(self, outlier):
        """
        Sets the outlier of this NumericAttribute.

        :param outlier: The outlier of this NumericAttribute.
        :type: oci.data_connectivity.models.Outlier
        """
        self._outlier = outlier

    @property
    def histogram(self):
        """
        Gets the histogram of this NumericAttribute.

        :return: The histogram of this NumericAttribute.
        :rtype: oci.data_connectivity.models.Histogram
        """
        return self._histogram

    @histogram.setter
    def histogram(self, histogram):
        """
        Sets the histogram of this NumericAttribute.

        :param histogram: The histogram of this NumericAttribute.
        :type: oci.data_connectivity.models.Histogram
        """
        self._histogram = histogram

    @property
    def pattern_frequencies(self):
        """
        Gets the pattern_frequencies of this NumericAttribute.
        Pattern frequencies for the column as described already in profile config.


        :return: The pattern_frequencies of this NumericAttribute.
        :rtype: list[oci.data_connectivity.models.ObjectFreqStat]
        """
        return self._pattern_frequencies

    @pattern_frequencies.setter
    def pattern_frequencies(self, pattern_frequencies):
        """
        Sets the pattern_frequencies of this NumericAttribute.
        Pattern frequencies for the column as described already in profile config.


        :param pattern_frequencies: The pattern_frequencies of this NumericAttribute.
        :type: list[oci.data_connectivity.models.ObjectFreqStat]
        """
        self._pattern_frequencies = pattern_frequencies

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
