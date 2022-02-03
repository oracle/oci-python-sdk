# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExecutionPlanStatsComparision(object):
    """
    The comparison report of the SQL execution plan statistics in the original and modified plan.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExecutionPlanStatsComparision object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param original:
            The value to assign to the original property of this ExecutionPlanStatsComparision.
        :type original: oci.database_management.models.SqlTuningTaskPlanStats

        :param modified:
            The value to assign to the modified property of this ExecutionPlanStatsComparision.
        :type modified: oci.database_management.models.SqlTuningTaskPlanStats

        """
        self.swagger_types = {
            'original': 'SqlTuningTaskPlanStats',
            'modified': 'SqlTuningTaskPlanStats'
        }

        self.attribute_map = {
            'original': 'original',
            'modified': 'modified'
        }

        self._original = None
        self._modified = None

    @property
    def original(self):
        """
        **[Required]** Gets the original of this ExecutionPlanStatsComparision.

        :return: The original of this ExecutionPlanStatsComparision.
        :rtype: oci.database_management.models.SqlTuningTaskPlanStats
        """
        return self._original

    @original.setter
    def original(self, original):
        """
        Sets the original of this ExecutionPlanStatsComparision.

        :param original: The original of this ExecutionPlanStatsComparision.
        :type: oci.database_management.models.SqlTuningTaskPlanStats
        """
        self._original = original

    @property
    def modified(self):
        """
        **[Required]** Gets the modified of this ExecutionPlanStatsComparision.

        :return: The modified of this ExecutionPlanStatsComparision.
        :rtype: oci.database_management.models.SqlTuningTaskPlanStats
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this ExecutionPlanStatsComparision.

        :param modified: The modified of this ExecutionPlanStatsComparision.
        :type: oci.database_management.models.SqlTuningTaskPlanStats
        """
        self._modified = modified

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
