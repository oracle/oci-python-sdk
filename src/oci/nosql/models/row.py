# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Row(object):
    """
    The result of GetRow.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Row object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this Row.
        :type value: dict(str, object)

        :param time_of_expiration:
            The value to assign to the time_of_expiration property of this Row.
        :type time_of_expiration: datetime

        :param usage:
            The value to assign to the usage property of this Row.
        :type usage: RequestUsage

        """
        self.swagger_types = {
            'value': 'dict(str, object)',
            'time_of_expiration': 'datetime',
            'usage': 'RequestUsage'
        }

        self.attribute_map = {
            'value': 'value',
            'time_of_expiration': 'timeOfExpiration',
            'usage': 'usage'
        }

        self._value = None
        self._time_of_expiration = None
        self._usage = None

    @property
    def value(self):
        """
        Gets the value of this Row.
        The map of values from a row.


        :return: The value of this Row.
        :rtype: dict(str, object)
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this Row.
        The map of values from a row.


        :param value: The value of this Row.
        :type: dict(str, object)
        """
        self._value = value

    @property
    def time_of_expiration(self):
        """
        Gets the time_of_expiration of this Row.
        The expiration time of the row. A zero value indicates that
        the row does not expire. An RFC3339 formatted datetime
        string.


        :return: The time_of_expiration of this Row.
        :rtype: datetime
        """
        return self._time_of_expiration

    @time_of_expiration.setter
    def time_of_expiration(self, time_of_expiration):
        """
        Sets the time_of_expiration of this Row.
        The expiration time of the row. A zero value indicates that
        the row does not expire. An RFC3339 formatted datetime
        string.


        :param time_of_expiration: The time_of_expiration of this Row.
        :type: datetime
        """
        self._time_of_expiration = time_of_expiration

    @property
    def usage(self):
        """
        Gets the usage of this Row.

        :return: The usage of this Row.
        :rtype: RequestUsage
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """
        Sets the usage of this Row.

        :param usage: The usage of this Row.
        :type: RequestUsage
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
