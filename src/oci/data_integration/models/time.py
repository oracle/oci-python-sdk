# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Time(object):
    """
    A model to hold time in hour:minute:second format.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Time object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param hour:
            The value to assign to the hour property of this Time.
        :type hour: int

        :param minute:
            The value to assign to the minute property of this Time.
        :type minute: int

        :param second:
            The value to assign to the second property of this Time.
        :type second: int

        """
        self.swagger_types = {
            'hour': 'int',
            'minute': 'int',
            'second': 'int'
        }

        self.attribute_map = {
            'hour': 'hour',
            'minute': 'minute',
            'second': 'second'
        }

        self._hour = None
        self._minute = None
        self._second = None

    @property
    def hour(self):
        """
        Gets the hour of this Time.
        The hour value.


        :return: The hour of this Time.
        :rtype: int
        """
        return self._hour

    @hour.setter
    def hour(self, hour):
        """
        Sets the hour of this Time.
        The hour value.


        :param hour: The hour of this Time.
        :type: int
        """
        self._hour = hour

    @property
    def minute(self):
        """
        Gets the minute of this Time.
        The minute value.


        :return: The minute of this Time.
        :rtype: int
        """
        return self._minute

    @minute.setter
    def minute(self, minute):
        """
        Sets the minute of this Time.
        The minute value.


        :param minute: The minute of this Time.
        :type: int
        """
        self._minute = minute

    @property
    def second(self):
        """
        Gets the second of this Time.
        The second value.


        :return: The second of this Time.
        :rtype: int
        """
        return self._second

    @second.setter
    def second(self, second):
        """
        Sets the second of this Time.
        The second value.


        :param second: The second of this Time.
        :type: int
        """
        self._second = second

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
