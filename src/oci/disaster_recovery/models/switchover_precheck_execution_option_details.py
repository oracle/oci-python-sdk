# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .dr_plan_execution_option_details import DrPlanExecutionOptionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SwitchoverPrecheckExecutionOptionDetails(DrPlanExecutionOptionDetails):
    """
    Options for switchover precheck execution.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SwitchoverPrecheckExecutionOptionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.disaster_recovery.models.SwitchoverPrecheckExecutionOptionDetails.plan_execution_type` attribute
        of this class is ``SWITCHOVER_PRECHECK`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param plan_execution_type:
            The value to assign to the plan_execution_type property of this SwitchoverPrecheckExecutionOptionDetails.
            Allowed values for this property are: "SWITCHOVER", "SWITCHOVER_PRECHECK", "FAILOVER", "FAILOVER_PRECHECK"
        :type plan_execution_type: str

        :param are_warnings_ignored:
            The value to assign to the are_warnings_ignored property of this SwitchoverPrecheckExecutionOptionDetails.
        :type are_warnings_ignored: bool

        """
        self.swagger_types = {
            'plan_execution_type': 'str',
            'are_warnings_ignored': 'bool'
        }

        self.attribute_map = {
            'plan_execution_type': 'planExecutionType',
            'are_warnings_ignored': 'areWarningsIgnored'
        }

        self._plan_execution_type = None
        self._are_warnings_ignored = None
        self._plan_execution_type = 'SWITCHOVER_PRECHECK'

    @property
    def are_warnings_ignored(self):
        """
        Gets the are_warnings_ignored of this SwitchoverPrecheckExecutionOptionDetails.
        A flag indicating whether warnigs should be ignored during the switchover.

        Example: `true`


        :return: The are_warnings_ignored of this SwitchoverPrecheckExecutionOptionDetails.
        :rtype: bool
        """
        return self._are_warnings_ignored

    @are_warnings_ignored.setter
    def are_warnings_ignored(self, are_warnings_ignored):
        """
        Sets the are_warnings_ignored of this SwitchoverPrecheckExecutionOptionDetails.
        A flag indicating whether warnigs should be ignored during the switchover.

        Example: `true`


        :param are_warnings_ignored: The are_warnings_ignored of this SwitchoverPrecheckExecutionOptionDetails.
        :type: bool
        """
        self._are_warnings_ignored = are_warnings_ignored

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
