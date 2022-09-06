# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProfileConfig(object):
    """
    Profiling configuration.
    """

    #: A constant which can be used with the functions property of a ProfileConfig.
    #: This constant has a value of "ATTRIBUTE_COUNT"
    FUNCTIONS_ATTRIBUTE_COUNT = "ATTRIBUTE_COUNT"

    #: A constant which can be used with the functions property of a ProfileConfig.
    #: This constant has a value of "ROW_COUNT"
    FUNCTIONS_ROW_COUNT = "ROW_COUNT"

    #: A constant which can be used with the functions property of a ProfileConfig.
    #: This constant has a value of "DATA_TYPE"
    FUNCTIONS_DATA_TYPE = "DATA_TYPE"

    #: A constant which can be used with the functions property of a ProfileConfig.
    #: This constant has a value of "DISTINCT_COUNT"
    FUNCTIONS_DISTINCT_COUNT = "DISTINCT_COUNT"

    #: A constant which can be used with the functions property of a ProfileConfig.
    #: This constant has a value of "DUPLICATE_COUNT"
    FUNCTIONS_DUPLICATE_COUNT = "DUPLICATE_COUNT"

    #: A constant which can be used with the functions property of a ProfileConfig.
    #: This constant has a value of "HISTOGRAM"
    FUNCTIONS_HISTOGRAM = "HISTOGRAM"

    #: A constant which can be used with the functions property of a ProfileConfig.
    #: This constant has a value of "MAX"
    FUNCTIONS_MAX = "MAX"

    #: A constant which can be used with the functions property of a ProfileConfig.
    #: This constant has a value of "MAX_LENGTH"
    FUNCTIONS_MAX_LENGTH = "MAX_LENGTH"

    #: A constant which can be used with the functions property of a ProfileConfig.
    #: This constant has a value of "MEAN"
    FUNCTIONS_MEAN = "MEAN"

    #: A constant which can be used with the functions property of a ProfileConfig.
    #: This constant has a value of "MEAN_LENGTH"
    FUNCTIONS_MEAN_LENGTH = "MEAN_LENGTH"

    #: A constant which can be used with the functions property of a ProfileConfig.
    #: This constant has a value of "MEDIAN"
    FUNCTIONS_MEDIAN = "MEDIAN"

    #: A constant which can be used with the functions property of a ProfileConfig.
    #: This constant has a value of "MIN"
    FUNCTIONS_MIN = "MIN"

    #: A constant which can be used with the functions property of a ProfileConfig.
    #: This constant has a value of "MIN_LENGTH"
    FUNCTIONS_MIN_LENGTH = "MIN_LENGTH"

    #: A constant which can be used with the functions property of a ProfileConfig.
    #: This constant has a value of "NULL_COUNT"
    FUNCTIONS_NULL_COUNT = "NULL_COUNT"

    #: A constant which can be used with the functions property of a ProfileConfig.
    #: This constant has a value of "OUTLIER"
    FUNCTIONS_OUTLIER = "OUTLIER"

    #: A constant which can be used with the functions property of a ProfileConfig.
    #: This constant has a value of "PATTERN"
    FUNCTIONS_PATTERN = "PATTERN"

    #: A constant which can be used with the functions property of a ProfileConfig.
    #: This constant has a value of "STANDARD_DEVIATION"
    FUNCTIONS_STANDARD_DEVIATION = "STANDARD_DEVIATION"

    #: A constant which can be used with the functions property of a ProfileConfig.
    #: This constant has a value of "UNIQUE_COUNT"
    FUNCTIONS_UNIQUE_COUNT = "UNIQUE_COUNT"

    #: A constant which can be used with the functions property of a ProfileConfig.
    #: This constant has a value of "VARIANCE"
    FUNCTIONS_VARIANCE = "VARIANCE"

    #: A constant which can be used with the functions property of a ProfileConfig.
    #: This constant has a value of "VALUE_FREQUENCY"
    FUNCTIONS_VALUE_FREQUENCY = "VALUE_FREQUENCY"

    def __init__(self, **kwargs):
        """
        Initializes a new ProfileConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param attributes:
            The value to assign to the attributes property of this ProfileConfig.
        :type attributes: list[str]

        :param functions:
            The value to assign to the functions property of this ProfileConfig.
            Allowed values for items in this list are: "ATTRIBUTE_COUNT", "ROW_COUNT", "DATA_TYPE", "DISTINCT_COUNT", "DUPLICATE_COUNT", "HISTOGRAM", "MAX", "MAX_LENGTH", "MEAN", "MEAN_LENGTH", "MEDIAN", "MIN", "MIN_LENGTH", "NULL_COUNT", "OUTLIER", "PATTERN", "STANDARD_DEVIATION", "UNIQUE_COUNT", "VARIANCE", "VALUE_FREQUENCY"
        :type functions: list[str]

        :param top_n_val_freq:
            The value to assign to the top_n_val_freq property of this ProfileConfig.
        :type top_n_val_freq: int

        :param pattern_threshold:
            The value to assign to the pattern_threshold property of this ProfileConfig.
        :type pattern_threshold: int

        :param data_type_threshold:
            The value to assign to the data_type_threshold property of this ProfileConfig.
        :type data_type_threshold: int

        """
        self.swagger_types = {
            'attributes': 'list[str]',
            'functions': 'list[str]',
            'top_n_val_freq': 'int',
            'pattern_threshold': 'int',
            'data_type_threshold': 'int'
        }

        self.attribute_map = {
            'attributes': 'attributes',
            'functions': 'functions',
            'top_n_val_freq': 'topNValFreq',
            'pattern_threshold': 'patternThreshold',
            'data_type_threshold': 'dataTypeThreshold'
        }

        self._attributes = None
        self._functions = None
        self._top_n_val_freq = None
        self._pattern_threshold = None
        self._data_type_threshold = None

    @property
    def attributes(self):
        """
        Gets the attributes of this ProfileConfig.
        Array of column names to profile. If empty, all the columns in the entity are profiled.


        :return: The attributes of this ProfileConfig.
        :rtype: list[str]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """
        Sets the attributes of this ProfileConfig.
        Array of column names to profile. If empty, all the columns in the entity are profiled.


        :param attributes: The attributes of this ProfileConfig.
        :type: list[str]
        """
        self._attributes = attributes

    @property
    def functions(self):
        """
        Gets the functions of this ProfileConfig.
        Array of enum strings to decide which profile functions to run. If empty, all the supported functions are run.

        Allowed values for items in this list are: "ATTRIBUTE_COUNT", "ROW_COUNT", "DATA_TYPE", "DISTINCT_COUNT", "DUPLICATE_COUNT", "HISTOGRAM", "MAX", "MAX_LENGTH", "MEAN", "MEAN_LENGTH", "MEDIAN", "MIN", "MIN_LENGTH", "NULL_COUNT", "OUTLIER", "PATTERN", "STANDARD_DEVIATION", "UNIQUE_COUNT", "VARIANCE", "VALUE_FREQUENCY"


        :return: The functions of this ProfileConfig.
        :rtype: list[str]
        """
        return self._functions

    @functions.setter
    def functions(self, functions):
        """
        Sets the functions of this ProfileConfig.
        Array of enum strings to decide which profile functions to run. If empty, all the supported functions are run.


        :param functions: The functions of this ProfileConfig.
        :type: list[str]
        """
        allowed_values = ["ATTRIBUTE_COUNT", "ROW_COUNT", "DATA_TYPE", "DISTINCT_COUNT", "DUPLICATE_COUNT", "HISTOGRAM", "MAX", "MAX_LENGTH", "MEAN", "MEAN_LENGTH", "MEDIAN", "MIN", "MIN_LENGTH", "NULL_COUNT", "OUTLIER", "PATTERN", "STANDARD_DEVIATION", "UNIQUE_COUNT", "VARIANCE", "VALUE_FREQUENCY"]

        if functions and functions is not NONE_SENTINEL:
            for value in functions:
                if not value_allowed_none_or_none_sentinel(value, allowed_values):
                    raise ValueError(
                        "Invalid value for `functions`, must be None or one of {0}"
                        .format(allowed_values)
                    )
        self._functions = functions

    @property
    def top_n_val_freq(self):
        """
        Gets the top_n_val_freq of this ProfileConfig.
        The maximum number of value frequencies to return per column. The VFs are sorted descending on frequency, and ascending on value, and then topN are returned and rest discarded.


        :return: The top_n_val_freq of this ProfileConfig.
        :rtype: int
        """
        return self._top_n_val_freq

    @top_n_val_freq.setter
    def top_n_val_freq(self, top_n_val_freq):
        """
        Sets the top_n_val_freq of this ProfileConfig.
        The maximum number of value frequencies to return per column. The VFs are sorted descending on frequency, and ascending on value, and then topN are returned and rest discarded.


        :param top_n_val_freq: The top_n_val_freq of this ProfileConfig.
        :type: int
        """
        self._top_n_val_freq = top_n_val_freq

    @property
    def pattern_threshold(self):
        """
        Gets the pattern_threshold of this ProfileConfig.
        A pattern has to qualify at least this percentage threshold to be considered a pattern on its own. Patterns that do not qualify are clubbed together into 'Others' pattern.


        :return: The pattern_threshold of this ProfileConfig.
        :rtype: int
        """
        return self._pattern_threshold

    @pattern_threshold.setter
    def pattern_threshold(self, pattern_threshold):
        """
        Sets the pattern_threshold of this ProfileConfig.
        A pattern has to qualify at least this percentage threshold to be considered a pattern on its own. Patterns that do not qualify are clubbed together into 'Others' pattern.


        :param pattern_threshold: The pattern_threshold of this ProfileConfig.
        :type: int
        """
        self._pattern_threshold = pattern_threshold

    @property
    def data_type_threshold(self):
        """
        Gets the data_type_threshold of this ProfileConfig.
        A data type has to qualify at least this percentage threshold to be considered an inferred data type for a column.


        :return: The data_type_threshold of this ProfileConfig.
        :rtype: int
        """
        return self._data_type_threshold

    @data_type_threshold.setter
    def data_type_threshold(self, data_type_threshold):
        """
        Sets the data_type_threshold of this ProfileConfig.
        A data type has to qualify at least this percentage threshold to be considered an inferred data type for a column.


        :param data_type_threshold: The data_type_threshold of this ProfileConfig.
        :type: int
        """
        self._data_type_threshold = data_type_threshold

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
