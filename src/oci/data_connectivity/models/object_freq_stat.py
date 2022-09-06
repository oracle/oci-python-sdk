# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ObjectFreqStat(object):
    """
    One specific element. Its meaning changes according to the context. For example, for ValueFrequency, the value represents a column value. For Patterns the value represents a pattern. For DataType the value represents a data type. For DataType formats (pertaining to date time) the value represents a format.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ObjectFreqStat object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this ObjectFreqStat.
        :type value: str

        :param confidence:
            The value to assign to the confidence property of this ObjectFreqStat.
        :type confidence: int

        :param freq:
            The value to assign to the freq property of this ObjectFreqStat.
        :type freq: int

        :param freq_percentage:
            The value to assign to the freq_percentage property of this ObjectFreqStat.
        :type freq_percentage: float

        """
        self.swagger_types = {
            'value': 'str',
            'confidence': 'int',
            'freq': 'int',
            'freq_percentage': 'float'
        }

        self.attribute_map = {
            'value': 'value',
            'confidence': 'confidence',
            'freq': 'freq',
            'freq_percentage': 'freqPercentage'
        }

        self._value = None
        self._confidence = None
        self._freq = None
        self._freq_percentage = None

    @property
    def value(self):
        """
        Gets the value of this ObjectFreqStat.
        Value of the confidence of the profile result.


        :return: The value of this ObjectFreqStat.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this ObjectFreqStat.
        Value of the confidence of the profile result.


        :param value: The value of this ObjectFreqStat.
        :type: str
        """
        self._value = value

    @property
    def confidence(self):
        """
        Gets the confidence of this ObjectFreqStat.
        Placeholder for now, in future we will return the confidence of the profile result (because we are using sampled data and not whole data)


        :return: The confidence of this ObjectFreqStat.
        :rtype: int
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """
        Sets the confidence of this ObjectFreqStat.
        Placeholder for now, in future we will return the confidence of the profile result (because we are using sampled data and not whole data)


        :param confidence: The confidence of this ObjectFreqStat.
        :type: int
        """
        self._confidence = confidence

    @property
    def freq(self):
        """
        Gets the freq of this ObjectFreqStat.
        The number of times the value appeared.


        :return: The freq of this ObjectFreqStat.
        :rtype: int
        """
        return self._freq

    @freq.setter
    def freq(self, freq):
        """
        Sets the freq of this ObjectFreqStat.
        The number of times the value appeared.


        :param freq: The freq of this ObjectFreqStat.
        :type: int
        """
        self._freq = freq

    @property
    def freq_percentage(self):
        """
        Gets the freq_percentage of this ObjectFreqStat.
        Frequency percentage across the sampled row counts (excluding nulls).


        :return: The freq_percentage of this ObjectFreqStat.
        :rtype: float
        """
        return self._freq_percentage

    @freq_percentage.setter
    def freq_percentage(self, freq_percentage):
        """
        Sets the freq_percentage of this ObjectFreqStat.
        Frequency percentage across the sampled row counts (excluding nulls).


        :param freq_percentage: The freq_percentage of this ObjectFreqStat.
        :type: float
        """
        self._freq_percentage = freq_percentage

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
