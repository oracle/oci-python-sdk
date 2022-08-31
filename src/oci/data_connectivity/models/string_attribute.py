# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .attribute_profile_result import AttributeProfileResult
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StringAttribute(AttributeProfileResult):
    """
    A summary of profiling results of a specefic attribute.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new StringAttribute object with values from keyword arguments. The default value of the :py:attr:`~oci.data_connectivity.models.StringAttribute.type` attribute
        of this class is ``STRING`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this StringAttribute.
        :type type: object

        :param name:
            The value to assign to the name property of this StringAttribute.
        :type name: str

        :param min:
            The value to assign to the min property of this StringAttribute.
        :type min: oci.data_connectivity.models.ProfileStat

        :param max:
            The value to assign to the max property of this StringAttribute.
        :type max: oci.data_connectivity.models.ProfileStat

        :param null_count:
            The value to assign to the null_count property of this StringAttribute.
        :type null_count: oci.data_connectivity.models.ProfileStat

        :param distinct_count:
            The value to assign to the distinct_count property of this StringAttribute.
        :type distinct_count: oci.data_connectivity.models.ProfileStat

        :param unique_count:
            The value to assign to the unique_count property of this StringAttribute.
        :type unique_count: oci.data_connectivity.models.ProfileStat

        :param duplicate_count:
            The value to assign to the duplicate_count property of this StringAttribute.
        :type duplicate_count: oci.data_connectivity.models.ProfileStat

        :param value_frequencies:
            The value to assign to the value_frequencies property of this StringAttribute.
        :type value_frequencies: list[oci.data_connectivity.models.ObjectFreqStat]

        :param min_length:
            The value to assign to the min_length property of this StringAttribute.
        :type min_length: oci.data_connectivity.models.ProfileStat

        :param max_length:
            The value to assign to the max_length property of this StringAttribute.
        :type max_length: oci.data_connectivity.models.ProfileStat

        :param mean_length:
            The value to assign to the mean_length property of this StringAttribute.
        :type mean_length: oci.data_connectivity.models.ProfileStat

        :param pattern_frequencies:
            The value to assign to the pattern_frequencies property of this StringAttribute.
        :type pattern_frequencies: list[oci.data_connectivity.models.ObjectFreqStat]

        :param inferred_data_types:
            The value to assign to the inferred_data_types property of this StringAttribute.
        :type inferred_data_types: list[oci.data_connectivity.models.DataTypeStat]

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
            'min_length': 'ProfileStat',
            'max_length': 'ProfileStat',
            'mean_length': 'ProfileStat',
            'pattern_frequencies': 'list[ObjectFreqStat]',
            'inferred_data_types': 'list[DataTypeStat]'
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
            'min_length': 'minLength',
            'max_length': 'maxLength',
            'mean_length': 'meanLength',
            'pattern_frequencies': 'patternFrequencies',
            'inferred_data_types': 'inferredDataTypes'
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
        self._min_length = None
        self._max_length = None
        self._mean_length = None
        self._pattern_frequencies = None
        self._inferred_data_types = None
        self._type = 'STRING'

    @property
    def min_length(self):
        """
        Gets the min_length of this StringAttribute.

        :return: The min_length of this StringAttribute.
        :rtype: oci.data_connectivity.models.ProfileStat
        """
        return self._min_length

    @min_length.setter
    def min_length(self, min_length):
        """
        Sets the min_length of this StringAttribute.

        :param min_length: The min_length of this StringAttribute.
        :type: oci.data_connectivity.models.ProfileStat
        """
        self._min_length = min_length

    @property
    def max_length(self):
        """
        Gets the max_length of this StringAttribute.

        :return: The max_length of this StringAttribute.
        :rtype: oci.data_connectivity.models.ProfileStat
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """
        Sets the max_length of this StringAttribute.

        :param max_length: The max_length of this StringAttribute.
        :type: oci.data_connectivity.models.ProfileStat
        """
        self._max_length = max_length

    @property
    def mean_length(self):
        """
        Gets the mean_length of this StringAttribute.

        :return: The mean_length of this StringAttribute.
        :rtype: oci.data_connectivity.models.ProfileStat
        """
        return self._mean_length

    @mean_length.setter
    def mean_length(self, mean_length):
        """
        Sets the mean_length of this StringAttribute.

        :param mean_length: The mean_length of this StringAttribute.
        :type: oci.data_connectivity.models.ProfileStat
        """
        self._mean_length = mean_length

    @property
    def pattern_frequencies(self):
        """
        Gets the pattern_frequencies of this StringAttribute.
        Pattern frequencies for the column as described in the profile config.


        :return: The pattern_frequencies of this StringAttribute.
        :rtype: list[oci.data_connectivity.models.ObjectFreqStat]
        """
        return self._pattern_frequencies

    @pattern_frequencies.setter
    def pattern_frequencies(self, pattern_frequencies):
        """
        Sets the pattern_frequencies of this StringAttribute.
        Pattern frequencies for the column as described in the profile config.


        :param pattern_frequencies: The pattern_frequencies of this StringAttribute.
        :type: list[oci.data_connectivity.models.ObjectFreqStat]
        """
        self._pattern_frequencies = pattern_frequencies

    @property
    def inferred_data_types(self):
        """
        Gets the inferred_data_types of this StringAttribute.
        Inferred DataType for the column.


        :return: The inferred_data_types of this StringAttribute.
        :rtype: list[oci.data_connectivity.models.DataTypeStat]
        """
        return self._inferred_data_types

    @inferred_data_types.setter
    def inferred_data_types(self, inferred_data_types):
        """
        Sets the inferred_data_types of this StringAttribute.
        Inferred DataType for the column.


        :param inferred_data_types: The inferred_data_types of this StringAttribute.
        :type: list[oci.data_connectivity.models.DataTypeStat]
        """
        self._inferred_data_types = inferred_data_types

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
