# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RowReductionDetails(object):
    """
    Information regarding how/what row reduction methods will be applied. If this property is not present or is null, then it means row reduction is not applied.
    """

    #: A constant which can be used with the reduction_method property of a RowReductionDetails.
    #: This constant has a value of "DELETE_ROW"
    REDUCTION_METHOD_DELETE_ROW = "DELETE_ROW"

    #: A constant which can be used with the reduction_method property of a RowReductionDetails.
    #: This constant has a value of "AVERAGE_ROW"
    REDUCTION_METHOD_AVERAGE_ROW = "AVERAGE_ROW"

    def __init__(self, **kwargs):
        """
        Initializes a new RowReductionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_reduction_enabled:
            The value to assign to the is_reduction_enabled property of this RowReductionDetails.
        :type is_reduction_enabled: bool

        :param reduction_percentage:
            The value to assign to the reduction_percentage property of this RowReductionDetails.
        :type reduction_percentage: float

        :param reduction_method:
            The value to assign to the reduction_method property of this RowReductionDetails.
            Allowed values for this property are: "DELETE_ROW", "AVERAGE_ROW", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type reduction_method: str

        """
        self.swagger_types = {
            'is_reduction_enabled': 'bool',
            'reduction_percentage': 'float',
            'reduction_method': 'str'
        }

        self.attribute_map = {
            'is_reduction_enabled': 'isReductionEnabled',
            'reduction_percentage': 'reductionPercentage',
            'reduction_method': 'reductionMethod'
        }

        self._is_reduction_enabled = None
        self._reduction_percentage = None
        self._reduction_method = None

    @property
    def is_reduction_enabled(self):
        """
        **[Required]** Gets the is_reduction_enabled of this RowReductionDetails.
        A boolean value to indicate if row reduction is applied


        :return: The is_reduction_enabled of this RowReductionDetails.
        :rtype: bool
        """
        return self._is_reduction_enabled

    @is_reduction_enabled.setter
    def is_reduction_enabled(self, is_reduction_enabled):
        """
        Sets the is_reduction_enabled of this RowReductionDetails.
        A boolean value to indicate if row reduction is applied


        :param is_reduction_enabled: The is_reduction_enabled of this RowReductionDetails.
        :type: bool
        """
        self._is_reduction_enabled = is_reduction_enabled

    @property
    def reduction_percentage(self):
        """
        **[Required]** Gets the reduction_percentage of this RowReductionDetails.
        A percentage to reduce data size down to on top of original data


        :return: The reduction_percentage of this RowReductionDetails.
        :rtype: float
        """
        return self._reduction_percentage

    @reduction_percentage.setter
    def reduction_percentage(self, reduction_percentage):
        """
        Sets the reduction_percentage of this RowReductionDetails.
        A percentage to reduce data size down to on top of original data


        :param reduction_percentage: The reduction_percentage of this RowReductionDetails.
        :type: float
        """
        self._reduction_percentage = reduction_percentage

    @property
    def reduction_method(self):
        """
        **[Required]** Gets the reduction_method of this RowReductionDetails.
        Method for row reduction:
          * DELETE_ROW - delete rows with equal intervals
          * AVERAGE_ROW - average multiple rows to one row

        Allowed values for this property are: "DELETE_ROW", "AVERAGE_ROW", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The reduction_method of this RowReductionDetails.
        :rtype: str
        """
        return self._reduction_method

    @reduction_method.setter
    def reduction_method(self, reduction_method):
        """
        Sets the reduction_method of this RowReductionDetails.
        Method for row reduction:
          * DELETE_ROW - delete rows with equal intervals
          * AVERAGE_ROW - average multiple rows to one row


        :param reduction_method: The reduction_method of this RowReductionDetails.
        :type: str
        """
        allowed_values = ["DELETE_ROW", "AVERAGE_ROW"]
        if not value_allowed_none_or_none_sentinel(reduction_method, allowed_values):
            reduction_method = 'UNKNOWN_ENUM_VALUE'
        self._reduction_method = reduction_method

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
