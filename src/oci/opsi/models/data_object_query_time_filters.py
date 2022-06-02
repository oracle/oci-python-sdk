# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataObjectQueryTimeFilters(object):
    """
    Time filters to be applied in the data object query.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DataObjectQueryTimeFilters object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_period:
            The value to assign to the time_period property of this DataObjectQueryTimeFilters.
        :type time_period: str

        :param time_start:
            The value to assign to the time_start property of this DataObjectQueryTimeFilters.
        :type time_start: datetime

        :param time_end:
            The value to assign to the time_end property of this DataObjectQueryTimeFilters.
        :type time_end: datetime

        """
        self.swagger_types = {
            'time_period': 'str',
            'time_start': 'datetime',
            'time_end': 'datetime'
        }

        self.attribute_map = {
            'time_period': 'timePeriod',
            'time_start': 'timeStart',
            'time_end': 'timeEnd'
        }

        self._time_period = None
        self._time_start = None
        self._time_end = None

    @property
    def time_period(self):
        """
        Gets the time_period of this DataObjectQueryTimeFilters.
        Specify time period in ISO 8601 format with respect to current time.
        Default is last 30 days represented by P30D.
        If timePeriod is specified, then timeStart and timeEnd will be ignored.
        Examples: P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months).


        :return: The time_period of this DataObjectQueryTimeFilters.
        :rtype: str
        """
        return self._time_period

    @time_period.setter
    def time_period(self, time_period):
        """
        Sets the time_period of this DataObjectQueryTimeFilters.
        Specify time period in ISO 8601 format with respect to current time.
        Default is last 30 days represented by P30D.
        If timePeriod is specified, then timeStart and timeEnd will be ignored.
        Examples: P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months).


        :param time_period: The time_period of this DataObjectQueryTimeFilters.
        :type: str
        """
        self._time_period = time_period

    @property
    def time_start(self):
        """
        Gets the time_start of this DataObjectQueryTimeFilters.
        Start time in UTC in RFC3339 formatted datetime string. Example: 2021-10-30T00:00:00.000Z.
        timeStart and timeEnd are used together. If timePeriod is specified, this parameter is ignored.


        :return: The time_start of this DataObjectQueryTimeFilters.
        :rtype: datetime
        """
        return self._time_start

    @time_start.setter
    def time_start(self, time_start):
        """
        Sets the time_start of this DataObjectQueryTimeFilters.
        Start time in UTC in RFC3339 formatted datetime string. Example: 2021-10-30T00:00:00.000Z.
        timeStart and timeEnd are used together. If timePeriod is specified, this parameter is ignored.


        :param time_start: The time_start of this DataObjectQueryTimeFilters.
        :type: datetime
        """
        self._time_start = time_start

    @property
    def time_end(self):
        """
        Gets the time_end of this DataObjectQueryTimeFilters.
        End time in UTC in RFC3339 formatted datetime string. Example: 2021-10-30T00:00:00.000Z.
        timeStart and timeEnd are used together. If timePeriod is specified, this parameter is ignored.
        If timeEnd is not specified, current time is used as timeEnd.


        :return: The time_end of this DataObjectQueryTimeFilters.
        :rtype: datetime
        """
        return self._time_end

    @time_end.setter
    def time_end(self, time_end):
        """
        Sets the time_end of this DataObjectQueryTimeFilters.
        End time in UTC in RFC3339 formatted datetime string. Example: 2021-10-30T00:00:00.000Z.
        timeStart and timeEnd are used together. If timePeriod is specified, this parameter is ignored.
        If timeEnd is not specified, current time is used as timeEnd.


        :param time_end: The time_end of this DataObjectQueryTimeFilters.
        :type: datetime
        """
        self._time_end = time_end

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
