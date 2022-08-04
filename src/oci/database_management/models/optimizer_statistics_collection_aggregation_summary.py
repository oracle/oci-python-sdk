# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OptimizerStatisticsCollectionAggregationSummary(object):
    """
    The summary of the Optimizer Statistics Collection, which includes the aggregated number of tasks grouped by status.
    """

    #: A constant which can be used with the group_by property of a OptimizerStatisticsCollectionAggregationSummary.
    #: This constant has a value of "TASK_STATUS"
    GROUP_BY_TASK_STATUS = "TASK_STATUS"

    #: A constant which can be used with the group_by property of a OptimizerStatisticsCollectionAggregationSummary.
    #: This constant has a value of "TASK_OBJECTS_STATUS"
    GROUP_BY_TASK_OBJECTS_STATUS = "TASK_OBJECTS_STATUS"

    def __init__(self, **kwargs):
        """
        Initializes a new OptimizerStatisticsCollectionAggregationSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param group_by:
            The value to assign to the group_by property of this OptimizerStatisticsCollectionAggregationSummary.
            Allowed values for this property are: "TASK_STATUS", "TASK_OBJECTS_STATUS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type group_by: str

        :param time_start:
            The value to assign to the time_start property of this OptimizerStatisticsCollectionAggregationSummary.
        :type time_start: datetime

        :param time_end:
            The value to assign to the time_end property of this OptimizerStatisticsCollectionAggregationSummary.
        :type time_end: datetime

        :param pending:
            The value to assign to the pending property of this OptimizerStatisticsCollectionAggregationSummary.
        :type pending: int

        :param in_progress:
            The value to assign to the in_progress property of this OptimizerStatisticsCollectionAggregationSummary.
        :type in_progress: int

        :param completed:
            The value to assign to the completed property of this OptimizerStatisticsCollectionAggregationSummary.
        :type completed: int

        :param failed:
            The value to assign to the failed property of this OptimizerStatisticsCollectionAggregationSummary.
        :type failed: int

        :param skipped:
            The value to assign to the skipped property of this OptimizerStatisticsCollectionAggregationSummary.
        :type skipped: int

        :param timed_out:
            The value to assign to the timed_out property of this OptimizerStatisticsCollectionAggregationSummary.
        :type timed_out: int

        :param unknown:
            The value to assign to the unknown property of this OptimizerStatisticsCollectionAggregationSummary.
        :type unknown: int

        :param total:
            The value to assign to the total property of this OptimizerStatisticsCollectionAggregationSummary.
        :type total: int

        """
        self.swagger_types = {
            'group_by': 'str',
            'time_start': 'datetime',
            'time_end': 'datetime',
            'pending': 'int',
            'in_progress': 'int',
            'completed': 'int',
            'failed': 'int',
            'skipped': 'int',
            'timed_out': 'int',
            'unknown': 'int',
            'total': 'int'
        }

        self.attribute_map = {
            'group_by': 'groupBy',
            'time_start': 'timeStart',
            'time_end': 'timeEnd',
            'pending': 'pending',
            'in_progress': 'inProgress',
            'completed': 'completed',
            'failed': 'failed',
            'skipped': 'skipped',
            'timed_out': 'timedOut',
            'unknown': 'unknown',
            'total': 'total'
        }

        self._group_by = None
        self._time_start = None
        self._time_end = None
        self._pending = None
        self._in_progress = None
        self._completed = None
        self._failed = None
        self._skipped = None
        self._timed_out = None
        self._unknown = None
        self._total = None

    @property
    def group_by(self):
        """
        Gets the group_by of this OptimizerStatisticsCollectionAggregationSummary.
        The optimizer statistics tasks grouped by type.

        Allowed values for this property are: "TASK_STATUS", "TASK_OBJECTS_STATUS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The group_by of this OptimizerStatisticsCollectionAggregationSummary.
        :rtype: str
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        """
        Sets the group_by of this OptimizerStatisticsCollectionAggregationSummary.
        The optimizer statistics tasks grouped by type.


        :param group_by: The group_by of this OptimizerStatisticsCollectionAggregationSummary.
        :type: str
        """
        allowed_values = ["TASK_STATUS", "TASK_OBJECTS_STATUS"]
        if not value_allowed_none_or_none_sentinel(group_by, allowed_values):
            group_by = 'UNKNOWN_ENUM_VALUE'
        self._group_by = group_by

    @property
    def time_start(self):
        """
        **[Required]** Gets the time_start of this OptimizerStatisticsCollectionAggregationSummary.
        Indicates the start of the hour as the statistics are aggregated per hour.


        :return: The time_start of this OptimizerStatisticsCollectionAggregationSummary.
        :rtype: datetime
        """
        return self._time_start

    @time_start.setter
    def time_start(self, time_start):
        """
        Sets the time_start of this OptimizerStatisticsCollectionAggregationSummary.
        Indicates the start of the hour as the statistics are aggregated per hour.


        :param time_start: The time_start of this OptimizerStatisticsCollectionAggregationSummary.
        :type: datetime
        """
        self._time_start = time_start

    @property
    def time_end(self):
        """
        Gets the time_end of this OptimizerStatisticsCollectionAggregationSummary.
        Indicates the end of the hour as the statistics are aggregated per hour.


        :return: The time_end of this OptimizerStatisticsCollectionAggregationSummary.
        :rtype: datetime
        """
        return self._time_end

    @time_end.setter
    def time_end(self, time_end):
        """
        Sets the time_end of this OptimizerStatisticsCollectionAggregationSummary.
        Indicates the end of the hour as the statistics are aggregated per hour.


        :param time_end: The time_end of this OptimizerStatisticsCollectionAggregationSummary.
        :type: datetime
        """
        self._time_end = time_end

    @property
    def pending(self):
        """
        Gets the pending of this OptimizerStatisticsCollectionAggregationSummary.
        The number of tasks or objects for which statistics are yet to be gathered.


        :return: The pending of this OptimizerStatisticsCollectionAggregationSummary.
        :rtype: int
        """
        return self._pending

    @pending.setter
    def pending(self, pending):
        """
        Sets the pending of this OptimizerStatisticsCollectionAggregationSummary.
        The number of tasks or objects for which statistics are yet to be gathered.


        :param pending: The pending of this OptimizerStatisticsCollectionAggregationSummary.
        :type: int
        """
        self._pending = pending

    @property
    def in_progress(self):
        """
        Gets the in_progress of this OptimizerStatisticsCollectionAggregationSummary.
        The number of tasks or objects for which statistics gathering is in progress.


        :return: The in_progress of this OptimizerStatisticsCollectionAggregationSummary.
        :rtype: int
        """
        return self._in_progress

    @in_progress.setter
    def in_progress(self, in_progress):
        """
        Sets the in_progress of this OptimizerStatisticsCollectionAggregationSummary.
        The number of tasks or objects for which statistics gathering is in progress.


        :param in_progress: The in_progress of this OptimizerStatisticsCollectionAggregationSummary.
        :type: int
        """
        self._in_progress = in_progress

    @property
    def completed(self):
        """
        Gets the completed of this OptimizerStatisticsCollectionAggregationSummary.
        The number of tasks or objects for which statistics gathering is completed.


        :return: The completed of this OptimizerStatisticsCollectionAggregationSummary.
        :rtype: int
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """
        Sets the completed of this OptimizerStatisticsCollectionAggregationSummary.
        The number of tasks or objects for which statistics gathering is completed.


        :param completed: The completed of this OptimizerStatisticsCollectionAggregationSummary.
        :type: int
        """
        self._completed = completed

    @property
    def failed(self):
        """
        Gets the failed of this OptimizerStatisticsCollectionAggregationSummary.
        The number of tasks or objects for which statistics gathering failed.


        :return: The failed of this OptimizerStatisticsCollectionAggregationSummary.
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """
        Sets the failed of this OptimizerStatisticsCollectionAggregationSummary.
        The number of tasks or objects for which statistics gathering failed.


        :param failed: The failed of this OptimizerStatisticsCollectionAggregationSummary.
        :type: int
        """
        self._failed = failed

    @property
    def skipped(self):
        """
        Gets the skipped of this OptimizerStatisticsCollectionAggregationSummary.
        The number of tasks or objects for which statistics gathering was skipped.


        :return: The skipped of this OptimizerStatisticsCollectionAggregationSummary.
        :rtype: int
        """
        return self._skipped

    @skipped.setter
    def skipped(self, skipped):
        """
        Sets the skipped of this OptimizerStatisticsCollectionAggregationSummary.
        The number of tasks or objects for which statistics gathering was skipped.


        :param skipped: The skipped of this OptimizerStatisticsCollectionAggregationSummary.
        :type: int
        """
        self._skipped = skipped

    @property
    def timed_out(self):
        """
        Gets the timed_out of this OptimizerStatisticsCollectionAggregationSummary.
        The number of tasks or objects for which statistics gathering timed out.


        :return: The timed_out of this OptimizerStatisticsCollectionAggregationSummary.
        :rtype: int
        """
        return self._timed_out

    @timed_out.setter
    def timed_out(self, timed_out):
        """
        Sets the timed_out of this OptimizerStatisticsCollectionAggregationSummary.
        The number of tasks or objects for which statistics gathering timed out.


        :param timed_out: The timed_out of this OptimizerStatisticsCollectionAggregationSummary.
        :type: int
        """
        self._timed_out = timed_out

    @property
    def unknown(self):
        """
        Gets the unknown of this OptimizerStatisticsCollectionAggregationSummary.
        The number of tasks or objects for which the status of statistics gathering is unknown.


        :return: The unknown of this OptimizerStatisticsCollectionAggregationSummary.
        :rtype: int
        """
        return self._unknown

    @unknown.setter
    def unknown(self, unknown):
        """
        Sets the unknown of this OptimizerStatisticsCollectionAggregationSummary.
        The number of tasks or objects for which the status of statistics gathering is unknown.


        :param unknown: The unknown of this OptimizerStatisticsCollectionAggregationSummary.
        :type: int
        """
        self._unknown = unknown

    @property
    def total(self):
        """
        Gets the total of this OptimizerStatisticsCollectionAggregationSummary.
        The total number of tasks or objects for which statistics collection is finished. This number is the
        sum of all the tasks or objects with various statuses: pending, inProgress, completed, failed, skipped,
        timedOut, and unknown.


        :return: The total of this OptimizerStatisticsCollectionAggregationSummary.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this OptimizerStatisticsCollectionAggregationSummary.
        The total number of tasks or objects for which statistics collection is finished. This number is the
        sum of all the tasks or objects with various statuses: pending, inProgress, completed, failed, skipped,
        timedOut, and unknown.


        :param total: The total of this OptimizerStatisticsCollectionAggregationSummary.
        :type: int
        """
        self._total = total

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
