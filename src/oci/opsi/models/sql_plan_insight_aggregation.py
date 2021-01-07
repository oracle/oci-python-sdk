# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlPlanInsightAggregation(object):
    """
    SQL execution plan Performance statistics.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlPlanInsightAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param plan_hash:
            The value to assign to the plan_hash property of this SqlPlanInsightAggregation.
        :type plan_hash: int

        :param io_time_in_sec:
            The value to assign to the io_time_in_sec property of this SqlPlanInsightAggregation.
        :type io_time_in_sec: float

        :param cpu_time_in_sec:
            The value to assign to the cpu_time_in_sec property of this SqlPlanInsightAggregation.
        :type cpu_time_in_sec: float

        :param inefficient_wait_time_in_sec:
            The value to assign to the inefficient_wait_time_in_sec property of this SqlPlanInsightAggregation.
        :type inefficient_wait_time_in_sec: float

        :param executions_count:
            The value to assign to the executions_count property of this SqlPlanInsightAggregation.
        :type executions_count: int

        """
        self.swagger_types = {
            'plan_hash': 'int',
            'io_time_in_sec': 'float',
            'cpu_time_in_sec': 'float',
            'inefficient_wait_time_in_sec': 'float',
            'executions_count': 'int'
        }

        self.attribute_map = {
            'plan_hash': 'planHash',
            'io_time_in_sec': 'ioTimeInSec',
            'cpu_time_in_sec': 'cpuTimeInSec',
            'inefficient_wait_time_in_sec': 'inefficientWaitTimeInSec',
            'executions_count': 'executionsCount'
        }

        self._plan_hash = None
        self._io_time_in_sec = None
        self._cpu_time_in_sec = None
        self._inefficient_wait_time_in_sec = None
        self._executions_count = None

    @property
    def plan_hash(self):
        """
        **[Required]** Gets the plan_hash of this SqlPlanInsightAggregation.
        Plan hash value for the SQL Execution Plan


        :return: The plan_hash of this SqlPlanInsightAggregation.
        :rtype: int
        """
        return self._plan_hash

    @plan_hash.setter
    def plan_hash(self, plan_hash):
        """
        Sets the plan_hash of this SqlPlanInsightAggregation.
        Plan hash value for the SQL Execution Plan


        :param plan_hash: The plan_hash of this SqlPlanInsightAggregation.
        :type: int
        """
        self._plan_hash = plan_hash

    @property
    def io_time_in_sec(self):
        """
        **[Required]** Gets the io_time_in_sec of this SqlPlanInsightAggregation.
        IO Time in seconds


        :return: The io_time_in_sec of this SqlPlanInsightAggregation.
        :rtype: float
        """
        return self._io_time_in_sec

    @io_time_in_sec.setter
    def io_time_in_sec(self, io_time_in_sec):
        """
        Sets the io_time_in_sec of this SqlPlanInsightAggregation.
        IO Time in seconds


        :param io_time_in_sec: The io_time_in_sec of this SqlPlanInsightAggregation.
        :type: float
        """
        self._io_time_in_sec = io_time_in_sec

    @property
    def cpu_time_in_sec(self):
        """
        **[Required]** Gets the cpu_time_in_sec of this SqlPlanInsightAggregation.
        CPU Time in seconds


        :return: The cpu_time_in_sec of this SqlPlanInsightAggregation.
        :rtype: float
        """
        return self._cpu_time_in_sec

    @cpu_time_in_sec.setter
    def cpu_time_in_sec(self, cpu_time_in_sec):
        """
        Sets the cpu_time_in_sec of this SqlPlanInsightAggregation.
        CPU Time in seconds


        :param cpu_time_in_sec: The cpu_time_in_sec of this SqlPlanInsightAggregation.
        :type: float
        """
        self._cpu_time_in_sec = cpu_time_in_sec

    @property
    def inefficient_wait_time_in_sec(self):
        """
        **[Required]** Gets the inefficient_wait_time_in_sec of this SqlPlanInsightAggregation.
        Inefficient Wait Time in seconds


        :return: The inefficient_wait_time_in_sec of this SqlPlanInsightAggregation.
        :rtype: float
        """
        return self._inefficient_wait_time_in_sec

    @inefficient_wait_time_in_sec.setter
    def inefficient_wait_time_in_sec(self, inefficient_wait_time_in_sec):
        """
        Sets the inefficient_wait_time_in_sec of this SqlPlanInsightAggregation.
        Inefficient Wait Time in seconds


        :param inefficient_wait_time_in_sec: The inefficient_wait_time_in_sec of this SqlPlanInsightAggregation.
        :type: float
        """
        self._inefficient_wait_time_in_sec = inefficient_wait_time_in_sec

    @property
    def executions_count(self):
        """
        **[Required]** Gets the executions_count of this SqlPlanInsightAggregation.
        Total number of executions


        :return: The executions_count of this SqlPlanInsightAggregation.
        :rtype: int
        """
        return self._executions_count

    @executions_count.setter
    def executions_count(self, executions_count):
        """
        Sets the executions_count of this SqlPlanInsightAggregation.
        Total number of executions


        :param executions_count: The executions_count of this SqlPlanInsightAggregation.
        :type: int
        """
        self._executions_count = executions_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
