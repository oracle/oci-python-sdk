# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WafRequest(object):
    """
    A time series of request counts handled by the Web Application Firewall, including blocked requests.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new WafRequest object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_observed:
            The value to assign to the time_observed property of this WafRequest.
        :type time_observed: datetime

        :param time_range_in_seconds:
            The value to assign to the time_range_in_seconds property of this WafRequest.
        :type time_range_in_seconds: int

        :param count:
            The value to assign to the count property of this WafRequest.
        :type count: int

        """
        self.swagger_types = {
            'time_observed': 'datetime',
            'time_range_in_seconds': 'int',
            'count': 'int'
        }

        self.attribute_map = {
            'time_observed': 'timeObserved',
            'time_range_in_seconds': 'timeRangeInSeconds',
            'count': 'count'
        }

        self._time_observed = None
        self._time_range_in_seconds = None
        self._count = None

    @property
    def time_observed(self):
        """
        Gets the time_observed of this WafRequest.
        The date and time the traffic was observed, rounded down to the start of a range, and expressed in RFC 3339 timestamp format.


        :return: The time_observed of this WafRequest.
        :rtype: datetime
        """
        return self._time_observed

    @time_observed.setter
    def time_observed(self, time_observed):
        """
        Sets the time_observed of this WafRequest.
        The date and time the traffic was observed, rounded down to the start of a range, and expressed in RFC 3339 timestamp format.


        :param time_observed: The time_observed of this WafRequest.
        :type: datetime
        """
        self._time_observed = time_observed

    @property
    def time_range_in_seconds(self):
        """
        Gets the time_range_in_seconds of this WafRequest.
        The number of seconds this data covers.


        :return: The time_range_in_seconds of this WafRequest.
        :rtype: int
        """
        return self._time_range_in_seconds

    @time_range_in_seconds.setter
    def time_range_in_seconds(self, time_range_in_seconds):
        """
        Sets the time_range_in_seconds of this WafRequest.
        The number of seconds this data covers.


        :param time_range_in_seconds: The time_range_in_seconds of this WafRequest.
        :type: int
        """
        self._time_range_in_seconds = time_range_in_seconds

    @property
    def count(self):
        """
        Gets the count of this WafRequest.
        The total number of requests received in this time period.


        :return: The count of this WafRequest.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this WafRequest.
        The total number of requests received in this time period.


        :param count: The count of this WafRequest.
        :type: int
        """
        self._count = count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
