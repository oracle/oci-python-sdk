# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HistoricalDataItem(object):
    """
    The historical timestamp and the corresponding resource value.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HistoricalDataItem object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param end_timestamp:
            The value to assign to the end_timestamp property of this HistoricalDataItem.
        :type end_timestamp: datetime

        :param usage:
            The value to assign to the usage property of this HistoricalDataItem.
        :type usage: float

        """
        self.swagger_types = {
            'end_timestamp': 'datetime',
            'usage': 'float'
        }

        self.attribute_map = {
            'end_timestamp': 'endTimestamp',
            'usage': 'usage'
        }

        self._end_timestamp = None
        self._usage = None

    @property
    def end_timestamp(self):
        """
        **[Required]** Gets the end_timestamp of this HistoricalDataItem.
        The timestamp in which the current sampling period ends in RFC 3339 format.


        :return: The end_timestamp of this HistoricalDataItem.
        :rtype: datetime
        """
        return self._end_timestamp

    @end_timestamp.setter
    def end_timestamp(self, end_timestamp):
        """
        Sets the end_timestamp of this HistoricalDataItem.
        The timestamp in which the current sampling period ends in RFC 3339 format.


        :param end_timestamp: The end_timestamp of this HistoricalDataItem.
        :type: datetime
        """
        self._end_timestamp = end_timestamp

    @property
    def usage(self):
        """
        **[Required]** Gets the usage of this HistoricalDataItem.
        Total amount used of the resource metric type (CPU, STORAGE).


        :return: The usage of this HistoricalDataItem.
        :rtype: float
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """
        Sets the usage of this HistoricalDataItem.
        Total amount used of the resource metric type (CPU, STORAGE).


        :param usage: The usage of this HistoricalDataItem.
        :type: float
        """
        self._usage = usage

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
