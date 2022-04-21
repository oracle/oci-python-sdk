# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TimeAndHorizontalScalingConfig(object):
    """
    Time of day and horizontal scaling configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TimeAndHorizontalScalingConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_recurrence:
            The value to assign to the time_recurrence property of this TimeAndHorizontalScalingConfig.
        :type time_recurrence: str

        :param target_node_count:
            The value to assign to the target_node_count property of this TimeAndHorizontalScalingConfig.
        :type target_node_count: int

        """
        self.swagger_types = {
            'time_recurrence': 'str',
            'target_node_count': 'int'
        }

        self.attribute_map = {
            'time_recurrence': 'timeRecurrence',
            'target_node_count': 'targetNodeCount'
        }

        self._time_recurrence = None
        self._target_node_count = None

    @property
    def time_recurrence(self):
        """
        Gets the time_recurrence of this TimeAndHorizontalScalingConfig.
        Day/time recurrence (specified following RFC 5545) at which to trigger autoscaling action. Currently only WEEKLY frequency is supported. Days of the week are specified using BYDAY field. Time of the day is specified using BYHOUR and BYMINUTE fields. Other fields are not supported.


        :return: The time_recurrence of this TimeAndHorizontalScalingConfig.
        :rtype: str
        """
        return self._time_recurrence

    @time_recurrence.setter
    def time_recurrence(self, time_recurrence):
        """
        Sets the time_recurrence of this TimeAndHorizontalScalingConfig.
        Day/time recurrence (specified following RFC 5545) at which to trigger autoscaling action. Currently only WEEKLY frequency is supported. Days of the week are specified using BYDAY field. Time of the day is specified using BYHOUR and BYMINUTE fields. Other fields are not supported.


        :param time_recurrence: The time_recurrence of this TimeAndHorizontalScalingConfig.
        :type: str
        """
        self._time_recurrence = time_recurrence

    @property
    def target_node_count(self):
        """
        Gets the target_node_count of this TimeAndHorizontalScalingConfig.
        This value is the desired number of nodes in the cluster.


        :return: The target_node_count of this TimeAndHorizontalScalingConfig.
        :rtype: int
        """
        return self._target_node_count

    @target_node_count.setter
    def target_node_count(self, target_node_count):
        """
        Sets the target_node_count of this TimeAndHorizontalScalingConfig.
        This value is the desired number of nodes in the cluster.


        :param target_node_count: The target_node_count of this TimeAndHorizontalScalingConfig.
        :type: int
        """
        self._target_node_count = target_node_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
