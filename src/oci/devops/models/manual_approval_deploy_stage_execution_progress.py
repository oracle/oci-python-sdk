# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .deploy_stage_execution_progress import DeployStageExecutionProgress
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManualApprovalDeployStageExecutionProgress(DeployStageExecutionProgress):
    """
    Specifies the manual approval stage specific execution details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ManualApprovalDeployStageExecutionProgress object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.ManualApprovalDeployStageExecutionProgress.deploy_stage_type` attribute
        of this class is ``MANUAL_APPROVAL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param deploy_stage_display_name:
            The value to assign to the deploy_stage_display_name property of this ManualApprovalDeployStageExecutionProgress.
        :type deploy_stage_display_name: str

        :param deploy_stage_type:
            The value to assign to the deploy_stage_type property of this ManualApprovalDeployStageExecutionProgress.
        :type deploy_stage_type: str

        :param deploy_stage_id:
            The value to assign to the deploy_stage_id property of this ManualApprovalDeployStageExecutionProgress.
        :type deploy_stage_id: str

        :param time_started:
            The value to assign to the time_started property of this ManualApprovalDeployStageExecutionProgress.
        :type time_started: datetime

        :param time_finished:
            The value to assign to the time_finished property of this ManualApprovalDeployStageExecutionProgress.
        :type time_finished: datetime

        :param status:
            The value to assign to the status property of this ManualApprovalDeployStageExecutionProgress.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "ROLLBACK_IN_PROGRESS", "ROLLBACK_SUCCEEDED", "ROLLBACK_FAILED"
        :type status: str

        :param deploy_stage_predecessors:
            The value to assign to the deploy_stage_predecessors property of this ManualApprovalDeployStageExecutionProgress.
        :type deploy_stage_predecessors: oci.devops.models.DeployStagePredecessorCollection

        :param deploy_stage_execution_progress_details:
            The value to assign to the deploy_stage_execution_progress_details property of this ManualApprovalDeployStageExecutionProgress.
        :type deploy_stage_execution_progress_details: list[oci.devops.models.DeployStageExecutionProgressDetails]

        :param approval_actions:
            The value to assign to the approval_actions property of this ManualApprovalDeployStageExecutionProgress.
        :type approval_actions: list[oci.devops.models.ApprovalAction]

        """
        self.swagger_types = {
            'deploy_stage_display_name': 'str',
            'deploy_stage_type': 'str',
            'deploy_stage_id': 'str',
            'time_started': 'datetime',
            'time_finished': 'datetime',
            'status': 'str',
            'deploy_stage_predecessors': 'DeployStagePredecessorCollection',
            'deploy_stage_execution_progress_details': 'list[DeployStageExecutionProgressDetails]',
            'approval_actions': 'list[ApprovalAction]'
        }

        self.attribute_map = {
            'deploy_stage_display_name': 'deployStageDisplayName',
            'deploy_stage_type': 'deployStageType',
            'deploy_stage_id': 'deployStageId',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished',
            'status': 'status',
            'deploy_stage_predecessors': 'deployStagePredecessors',
            'deploy_stage_execution_progress_details': 'deployStageExecutionProgressDetails',
            'approval_actions': 'approvalActions'
        }

        self._deploy_stage_display_name = None
        self._deploy_stage_type = None
        self._deploy_stage_id = None
        self._time_started = None
        self._time_finished = None
        self._status = None
        self._deploy_stage_predecessors = None
        self._deploy_stage_execution_progress_details = None
        self._approval_actions = None
        self._deploy_stage_type = 'MANUAL_APPROVAL'

    @property
    def approval_actions(self):
        """
        Gets the approval_actions of this ManualApprovalDeployStageExecutionProgress.

        :return: The approval_actions of this ManualApprovalDeployStageExecutionProgress.
        :rtype: list[oci.devops.models.ApprovalAction]
        """
        return self._approval_actions

    @approval_actions.setter
    def approval_actions(self, approval_actions):
        """
        Sets the approval_actions of this ManualApprovalDeployStageExecutionProgress.

        :param approval_actions: The approval_actions of this ManualApprovalDeployStageExecutionProgress.
        :type: list[oci.devops.models.ApprovalAction]
        """
        self._approval_actions = approval_actions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
