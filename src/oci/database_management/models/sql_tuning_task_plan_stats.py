# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlTuningTaskPlanStats(object):
    """
    The statistics of a SQL execution plan.
    """

    #: A constant which can be used with the plan_status property of a SqlTuningTaskPlanStats.
    #: This constant has a value of "COMPLETE"
    PLAN_STATUS_COMPLETE = "COMPLETE"

    #: A constant which can be used with the plan_status property of a SqlTuningTaskPlanStats.
    #: This constant has a value of "PARTIAL"
    PLAN_STATUS_PARTIAL = "PARTIAL"

    def __init__(self, **kwargs):
        """
        Initializes a new SqlTuningTaskPlanStats object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param plan_type:
            The value to assign to the plan_type property of this SqlTuningTaskPlanStats.
        :type plan_type: str

        :param plan_stats:
            The value to assign to the plan_stats property of this SqlTuningTaskPlanStats.
        :type plan_stats: dict(str, float)

        :param plan_status:
            The value to assign to the plan_status property of this SqlTuningTaskPlanStats.
            Allowed values for this property are: "COMPLETE", "PARTIAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type plan_status: str

        """
        self.swagger_types = {
            'plan_type': 'str',
            'plan_stats': 'dict(str, float)',
            'plan_status': 'str'
        }

        self.attribute_map = {
            'plan_type': 'planType',
            'plan_stats': 'planStats',
            'plan_status': 'planStatus'
        }

        self._plan_type = None
        self._plan_stats = None
        self._plan_status = None

    @property
    def plan_type(self):
        """
        **[Required]** Gets the plan_type of this SqlTuningTaskPlanStats.
        The type of the original or modified plan with profile, index, and so on.


        :return: The plan_type of this SqlTuningTaskPlanStats.
        :rtype: str
        """
        return self._plan_type

    @plan_type.setter
    def plan_type(self, plan_type):
        """
        Sets the plan_type of this SqlTuningTaskPlanStats.
        The type of the original or modified plan with profile, index, and so on.


        :param plan_type: The plan_type of this SqlTuningTaskPlanStats.
        :type: str
        """
        self._plan_type = plan_type

    @property
    def plan_stats(self):
        """
        **[Required]** Gets the plan_stats of this SqlTuningTaskPlanStats.
        A map contains the statistics for the SQL execution using the plan.
        The key of the map is the metric's name. The value of the map is the metric's value.


        :return: The plan_stats of this SqlTuningTaskPlanStats.
        :rtype: dict(str, float)
        """
        return self._plan_stats

    @plan_stats.setter
    def plan_stats(self, plan_stats):
        """
        Sets the plan_stats of this SqlTuningTaskPlanStats.
        A map contains the statistics for the SQL execution using the plan.
        The key of the map is the metric's name. The value of the map is the metric's value.


        :param plan_stats: The plan_stats of this SqlTuningTaskPlanStats.
        :type: dict(str, float)
        """
        self._plan_stats = plan_stats

    @property
    def plan_status(self):
        """
        **[Required]** Gets the plan_status of this SqlTuningTaskPlanStats.
        The status of the execution using the plan.

        Allowed values for this property are: "COMPLETE", "PARTIAL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The plan_status of this SqlTuningTaskPlanStats.
        :rtype: str
        """
        return self._plan_status

    @plan_status.setter
    def plan_status(self, plan_status):
        """
        Sets the plan_status of this SqlTuningTaskPlanStats.
        The status of the execution using the plan.


        :param plan_status: The plan_status of this SqlTuningTaskPlanStats.
        :type: str
        """
        allowed_values = ["COMPLETE", "PARTIAL"]
        if not value_allowed_none_or_none_sentinel(plan_status, allowed_values):
            plan_status = 'UNKNOWN_ENUM_VALUE'
        self._plan_status = plan_status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
