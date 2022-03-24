# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .deploy_stage_execution_progress import DeployStageExecutionProgress
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OkeCanaryDeployStageExecutionProgress(DeployStageExecutionProgress):
    """
    Specifies the Container Engine for Kubernetes (OKE) cluster Canary deployment stage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OkeCanaryDeployStageExecutionProgress object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.OkeCanaryDeployStageExecutionProgress.deploy_stage_type` attribute
        of this class is ``OKE_CANARY_DEPLOYMENT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param deploy_stage_display_name:
            The value to assign to the deploy_stage_display_name property of this OkeCanaryDeployStageExecutionProgress.
        :type deploy_stage_display_name: str

        :param deploy_stage_type:
            The value to assign to the deploy_stage_type property of this OkeCanaryDeployStageExecutionProgress.
        :type deploy_stage_type: str

        :param deploy_stage_id:
            The value to assign to the deploy_stage_id property of this OkeCanaryDeployStageExecutionProgress.
        :type deploy_stage_id: str

        :param time_started:
            The value to assign to the time_started property of this OkeCanaryDeployStageExecutionProgress.
        :type time_started: datetime

        :param time_finished:
            The value to assign to the time_finished property of this OkeCanaryDeployStageExecutionProgress.
        :type time_finished: datetime

        :param status:
            The value to assign to the status property of this OkeCanaryDeployStageExecutionProgress.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "ROLLBACK_IN_PROGRESS", "ROLLBACK_SUCCEEDED", "ROLLBACK_FAILED"
        :type status: str

        :param deploy_stage_predecessors:
            The value to assign to the deploy_stage_predecessors property of this OkeCanaryDeployStageExecutionProgress.
        :type deploy_stage_predecessors: oci.devops.models.DeployStagePredecessorCollection

        :param deploy_stage_execution_progress_details:
            The value to assign to the deploy_stage_execution_progress_details property of this OkeCanaryDeployStageExecutionProgress.
        :type deploy_stage_execution_progress_details: list[oci.devops.models.DeployStageExecutionProgressDetails]

        """
        self.swagger_types = {
            'deploy_stage_display_name': 'str',
            'deploy_stage_type': 'str',
            'deploy_stage_id': 'str',
            'time_started': 'datetime',
            'time_finished': 'datetime',
            'status': 'str',
            'deploy_stage_predecessors': 'DeployStagePredecessorCollection',
            'deploy_stage_execution_progress_details': 'list[DeployStageExecutionProgressDetails]'
        }

        self.attribute_map = {
            'deploy_stage_display_name': 'deployStageDisplayName',
            'deploy_stage_type': 'deployStageType',
            'deploy_stage_id': 'deployStageId',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished',
            'status': 'status',
            'deploy_stage_predecessors': 'deployStagePredecessors',
            'deploy_stage_execution_progress_details': 'deployStageExecutionProgressDetails'
        }

        self._deploy_stage_display_name = None
        self._deploy_stage_type = None
        self._deploy_stage_id = None
        self._time_started = None
        self._time_finished = None
        self._status = None
        self._deploy_stage_predecessors = None
        self._deploy_stage_execution_progress_details = None
        self._deploy_stage_type = 'OKE_CANARY_DEPLOYMENT'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
