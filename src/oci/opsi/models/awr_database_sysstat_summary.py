# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AwrDatabaseSysstatSummary(object):
    """
    The summary of the AWR SYSSTAT data.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AwrDatabaseSysstatSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this AwrDatabaseSysstatSummary.
        :type name: str

        :param category:
            The value to assign to the category property of this AwrDatabaseSysstatSummary.
        :type category: str

        :param time_begin:
            The value to assign to the time_begin property of this AwrDatabaseSysstatSummary.
        :type time_begin: datetime

        :param time_end:
            The value to assign to the time_end property of this AwrDatabaseSysstatSummary.
        :type time_end: datetime

        :param avg_value:
            The value to assign to the avg_value property of this AwrDatabaseSysstatSummary.
        :type avg_value: float

        :param current_value:
            The value to assign to the current_value property of this AwrDatabaseSysstatSummary.
        :type current_value: float

        """
        self.swagger_types = {
            'name': 'str',
            'category': 'str',
            'time_begin': 'datetime',
            'time_end': 'datetime',
            'avg_value': 'float',
            'current_value': 'float'
        }

        self.attribute_map = {
            'name': 'name',
            'category': 'category',
            'time_begin': 'timeBegin',
            'time_end': 'timeEnd',
            'avg_value': 'avgValue',
            'current_value': 'currentValue'
        }

        self._name = None
        self._category = None
        self._time_begin = None
        self._time_end = None
        self._avg_value = None
        self._current_value = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this AwrDatabaseSysstatSummary.
        The name of the SYSSTAT.


        :return: The name of this AwrDatabaseSysstatSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AwrDatabaseSysstatSummary.
        The name of the SYSSTAT.


        :param name: The name of this AwrDatabaseSysstatSummary.
        :type: str
        """
        self._name = name

    @property
    def category(self):
        """
        Gets the category of this AwrDatabaseSysstatSummary.
        The name of the SYSSTAT category.


        :return: The category of this AwrDatabaseSysstatSummary.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this AwrDatabaseSysstatSummary.
        The name of the SYSSTAT category.


        :param category: The category of this AwrDatabaseSysstatSummary.
        :type: str
        """
        self._category = category

    @property
    def time_begin(self):
        """
        Gets the time_begin of this AwrDatabaseSysstatSummary.
        The start time of the SYSSTAT.


        :return: The time_begin of this AwrDatabaseSysstatSummary.
        :rtype: datetime
        """
        return self._time_begin

    @time_begin.setter
    def time_begin(self, time_begin):
        """
        Sets the time_begin of this AwrDatabaseSysstatSummary.
        The start time of the SYSSTAT.


        :param time_begin: The time_begin of this AwrDatabaseSysstatSummary.
        :type: datetime
        """
        self._time_begin = time_begin

    @property
    def time_end(self):
        """
        Gets the time_end of this AwrDatabaseSysstatSummary.
        The end time of the SYSSTAT.


        :return: The time_end of this AwrDatabaseSysstatSummary.
        :rtype: datetime
        """
        return self._time_end

    @time_end.setter
    def time_end(self, time_end):
        """
        Sets the time_end of this AwrDatabaseSysstatSummary.
        The end time of the SYSSTAT.


        :param time_end: The time_end of this AwrDatabaseSysstatSummary.
        :type: datetime
        """
        self._time_end = time_end

    @property
    def avg_value(self):
        """
        Gets the avg_value of this AwrDatabaseSysstatSummary.
        The average value of the SYSSTAT. The units are stats name/val per the time period {timeBegin - timeEnd}.


        :return: The avg_value of this AwrDatabaseSysstatSummary.
        :rtype: float
        """
        return self._avg_value

    @avg_value.setter
    def avg_value(self, avg_value):
        """
        Sets the avg_value of this AwrDatabaseSysstatSummary.
        The average value of the SYSSTAT. The units are stats name/val per the time period {timeBegin - timeEnd}.


        :param avg_value: The avg_value of this AwrDatabaseSysstatSummary.
        :type: float
        """
        self._avg_value = avg_value

    @property
    def current_value(self):
        """
        Gets the current_value of this AwrDatabaseSysstatSummary.
        The last value of the SYSSTAT. The units are stats name/val per the time period {timeBegin - timeEnd}.


        :return: The current_value of this AwrDatabaseSysstatSummary.
        :rtype: float
        """
        return self._current_value

    @current_value.setter
    def current_value(self, current_value):
        """
        Sets the current_value of this AwrDatabaseSysstatSummary.
        The last value of the SYSSTAT. The units are stats name/val per the time period {timeBegin - timeEnd}.


        :param current_value: The current_value of this AwrDatabaseSysstatSummary.
        :type: float
        """
        self._current_value = current_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
