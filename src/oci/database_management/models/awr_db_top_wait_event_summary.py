# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AwrDbTopWaitEventSummary(object):
    """
    A summary of the AWR top wait event data for one event.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AwrDbTopWaitEventSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this AwrDbTopWaitEventSummary.
        :type name: str

        :param waits_per_sec:
            The value to assign to the waits_per_sec property of this AwrDbTopWaitEventSummary.
        :type waits_per_sec: float

        :param avg_wait_time_per_sec:
            The value to assign to the avg_wait_time_per_sec property of this AwrDbTopWaitEventSummary.
        :type avg_wait_time_per_sec: float

        """
        self.swagger_types = {
            'name': 'str',
            'waits_per_sec': 'float',
            'avg_wait_time_per_sec': 'float'
        }

        self.attribute_map = {
            'name': 'name',
            'waits_per_sec': 'waitsPerSec',
            'avg_wait_time_per_sec': 'avgWaitTimePerSec'
        }

        self._name = None
        self._waits_per_sec = None
        self._avg_wait_time_per_sec = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this AwrDbTopWaitEventSummary.
        The name of the event.


        :return: The name of this AwrDbTopWaitEventSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AwrDbTopWaitEventSummary.
        The name of the event.


        :param name: The name of this AwrDbTopWaitEventSummary.
        :type: str
        """
        self._name = name

    @property
    def waits_per_sec(self):
        """
        Gets the waits_per_sec of this AwrDbTopWaitEventSummary.
        The wait count per second.


        :return: The waits_per_sec of this AwrDbTopWaitEventSummary.
        :rtype: float
        """
        return self._waits_per_sec

    @waits_per_sec.setter
    def waits_per_sec(self, waits_per_sec):
        """
        Sets the waits_per_sec of this AwrDbTopWaitEventSummary.
        The wait count per second.


        :param waits_per_sec: The waits_per_sec of this AwrDbTopWaitEventSummary.
        :type: float
        """
        self._waits_per_sec = waits_per_sec

    @property
    def avg_wait_time_per_sec(self):
        """
        Gets the avg_wait_time_per_sec of this AwrDbTopWaitEventSummary.
        The average wait time per second.


        :return: The avg_wait_time_per_sec of this AwrDbTopWaitEventSummary.
        :rtype: float
        """
        return self._avg_wait_time_per_sec

    @avg_wait_time_per_sec.setter
    def avg_wait_time_per_sec(self, avg_wait_time_per_sec):
        """
        Sets the avg_wait_time_per_sec of this AwrDbTopWaitEventSummary.
        The average wait time per second.


        :param avg_wait_time_per_sec: The avg_wait_time_per_sec of this AwrDbTopWaitEventSummary.
        :type: float
        """
        self._avg_wait_time_per_sec = avg_wait_time_per_sec

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
