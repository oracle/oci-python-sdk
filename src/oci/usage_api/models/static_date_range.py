# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .date_range import DateRange
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StaticDateRange(DateRange):
    """
    The saved static date range (Required when dynamicDateRange is missing).
    """

    def __init__(self, **kwargs):
        """
        Initializes a new StaticDateRange object with values from keyword arguments. The default value of the :py:attr:`~oci.usage_api.models.StaticDateRange.date_range_type` attribute
        of this class is ``STATIC`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param date_range_type:
            The value to assign to the date_range_type property of this StaticDateRange.
            Allowed values for this property are: "STATIC", "DYNAMIC"
        :type date_range_type: str

        :param time_usage_started:
            The value to assign to the time_usage_started property of this StaticDateRange.
        :type time_usage_started: datetime

        :param time_usage_ended:
            The value to assign to the time_usage_ended property of this StaticDateRange.
        :type time_usage_ended: datetime

        """
        self.swagger_types = {
            'date_range_type': 'str',
            'time_usage_started': 'datetime',
            'time_usage_ended': 'datetime'
        }

        self.attribute_map = {
            'date_range_type': 'dateRangeType',
            'time_usage_started': 'timeUsageStarted',
            'time_usage_ended': 'timeUsageEnded'
        }

        self._date_range_type = None
        self._time_usage_started = None
        self._time_usage_ended = None
        self._date_range_type = 'STATIC'

    @property
    def time_usage_started(self):
        """
        **[Required]** Gets the time_usage_started of this StaticDateRange.
        The usage start time.


        :return: The time_usage_started of this StaticDateRange.
        :rtype: datetime
        """
        return self._time_usage_started

    @time_usage_started.setter
    def time_usage_started(self, time_usage_started):
        """
        Sets the time_usage_started of this StaticDateRange.
        The usage start time.


        :param time_usage_started: The time_usage_started of this StaticDateRange.
        :type: datetime
        """
        self._time_usage_started = time_usage_started

    @property
    def time_usage_ended(self):
        """
        **[Required]** Gets the time_usage_ended of this StaticDateRange.
        The usage end time.


        :return: The time_usage_ended of this StaticDateRange.
        :rtype: datetime
        """
        return self._time_usage_ended

    @time_usage_ended.setter
    def time_usage_ended(self, time_usage_ended):
        """
        Sets the time_usage_ended of this StaticDateRange.
        The usage end time.


        :param time_usage_ended: The time_usage_ended of this StaticDateRange.
        :type: datetime
        """
        self._time_usage_ended = time_usage_ended

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
