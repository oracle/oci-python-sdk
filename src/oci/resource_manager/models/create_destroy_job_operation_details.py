# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_job_operation_details import CreateJobOperationDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDestroyJobOperationDetails(CreateJobOperationDetails):
    """
    Job details that are specific to destroy operations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDestroyJobOperationDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.resource_manager.models.CreateDestroyJobOperationDetails.operation` attribute
        of this class is ``DESTROY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation:
            The value to assign to the operation property of this CreateDestroyJobOperationDetails.
        :type operation: str

        :param execution_plan_strategy:
            The value to assign to the execution_plan_strategy property of this CreateDestroyJobOperationDetails.
        :type execution_plan_strategy: str

        """
        self.swagger_types = {
            'operation': 'str',
            'execution_plan_strategy': 'str'
        }

        self.attribute_map = {
            'operation': 'operation',
            'execution_plan_strategy': 'executionPlanStrategy'
        }

        self._operation = None
        self._execution_plan_strategy = None
        self._operation = 'DESTROY'

    @property
    def execution_plan_strategy(self):
        """
        **[Required]** Gets the execution_plan_strategy of this CreateDestroyJobOperationDetails.
        Specifies the source of the execution plan to apply.
        Currently, only `AUTO_APPROVED` is allowed, which indicates that the job
        will be run without an execution plan.


        :return: The execution_plan_strategy of this CreateDestroyJobOperationDetails.
        :rtype: str
        """
        return self._execution_plan_strategy

    @execution_plan_strategy.setter
    def execution_plan_strategy(self, execution_plan_strategy):
        """
        Sets the execution_plan_strategy of this CreateDestroyJobOperationDetails.
        Specifies the source of the execution plan to apply.
        Currently, only `AUTO_APPROVED` is allowed, which indicates that the job
        will be run without an execution plan.


        :param execution_plan_strategy: The execution_plan_strategy of this CreateDestroyJobOperationDetails.
        :type: str
        """
        self._execution_plan_strategy = execution_plan_strategy

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
