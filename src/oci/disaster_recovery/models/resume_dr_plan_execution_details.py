# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .dr_plan_execution_control_details import DrPlanExecutionControlDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResumeDrPlanExecutionDetails(DrPlanExecutionControlDetails):
    """
    The details for resuming a DR Plan Execution.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ResumeDrPlanExecutionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.disaster_recovery.models.ResumeDrPlanExecutionDetails.action_type` attribute
        of this class is ``RESUME`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action_type:
            The value to assign to the action_type property of this ResumeDrPlanExecutionDetails.
            Allowed values for this property are: "CANCEL", "PAUSE", "RESUME"
        :type action_type: str

        """
        self.swagger_types = {
            'action_type': 'str'
        }

        self.attribute_map = {
            'action_type': 'actionType'
        }

        self._action_type = None
        self._action_type = 'RESUME'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
