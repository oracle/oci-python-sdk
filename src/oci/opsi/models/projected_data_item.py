# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProjectedDataItem(object):
    """
    The timestamp of the projected event and their corresponding resource value.
    `highValue` and `lowValue` are the uncertainty bounds of the corresponding value.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ProjectedDataItem object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param end_timestamp:
            The value to assign to the end_timestamp property of this ProjectedDataItem.
        :type end_timestamp: datetime

        :param usage:
            The value to assign to the usage property of this ProjectedDataItem.
        :type usage: float

        :param high_value:
            The value to assign to the high_value property of this ProjectedDataItem.
        :type high_value: float

        :param low_value:
            The value to assign to the low_value property of this ProjectedDataItem.
        :type low_value: float

        """
        self.swagger_types = {
            'end_timestamp': 'datetime',
            'usage': 'float',
            'high_value': 'float',
            'low_value': 'float'
        }

        self.attribute_map = {
            'end_timestamp': 'endTimestamp',
            'usage': 'usage',
            'high_value': 'highValue',
            'low_value': 'lowValue'
        }

        self._end_timestamp = None
        self._usage = None
        self._high_value = None
        self._low_value = None

    @property
    def end_timestamp(self):
        """
        **[Required]** Gets the end_timestamp of this ProjectedDataItem.
        The timestamp in which the current sampling period ends in RFC 3339 format.


        :return: The end_timestamp of this ProjectedDataItem.
        :rtype: datetime
        """
        return self._end_timestamp

    @end_timestamp.setter
    def end_timestamp(self, end_timestamp):
        """
        Sets the end_timestamp of this ProjectedDataItem.
        The timestamp in which the current sampling period ends in RFC 3339 format.


        :param end_timestamp: The end_timestamp of this ProjectedDataItem.
        :type: datetime
        """
        self._end_timestamp = end_timestamp

    @property
    def usage(self):
        """
        **[Required]** Gets the usage of this ProjectedDataItem.
        Total amount used of the resource metric type (CPU, STORAGE).


        :return: The usage of this ProjectedDataItem.
        :rtype: float
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """
        Sets the usage of this ProjectedDataItem.
        Total amount used of the resource metric type (CPU, STORAGE).


        :param usage: The usage of this ProjectedDataItem.
        :type: float
        """
        self._usage = usage

    @property
    def high_value(self):
        """
        **[Required]** Gets the high_value of this ProjectedDataItem.
        Upper uncertainty bound of the current usage value.


        :return: The high_value of this ProjectedDataItem.
        :rtype: float
        """
        return self._high_value

    @high_value.setter
    def high_value(self, high_value):
        """
        Sets the high_value of this ProjectedDataItem.
        Upper uncertainty bound of the current usage value.


        :param high_value: The high_value of this ProjectedDataItem.
        :type: float
        """
        self._high_value = high_value

    @property
    def low_value(self):
        """
        **[Required]** Gets the low_value of this ProjectedDataItem.
        Lower uncertainty bound of the current usage value.


        :return: The low_value of this ProjectedDataItem.
        :rtype: float
        """
        return self._low_value

    @low_value.setter
    def low_value(self, low_value):
        """
        Sets the low_value of this ProjectedDataItem.
        Lower uncertainty bound of the current usage value.


        :param low_value: The low_value of this ProjectedDataItem.
        :type: float
        """
        self._low_value = low_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
