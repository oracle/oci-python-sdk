# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .build_pipeline_stage_run_progress import BuildPipelineStageRunProgress
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TriggerDeploymentPipelineStageRunProgress(BuildPipelineStageRunProgress):
    """
    Specifies Trigger Deployment Pipleline stage specific run details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TriggerDeploymentPipelineStageRunProgress object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.TriggerDeploymentPipelineStageRunProgress.build_pipeline_stage_type` attribute
        of this class is ``TRIGGER_DEPLOYMENT_PIPELINE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param stage_display_name:
            The value to assign to the stage_display_name property of this TriggerDeploymentPipelineStageRunProgress.
        :type stage_display_name: str

        :param build_pipeline_stage_type:
            The value to assign to the build_pipeline_stage_type property of this TriggerDeploymentPipelineStageRunProgress.
        :type build_pipeline_stage_type: str

        :param build_pipeline_stage_id:
            The value to assign to the build_pipeline_stage_id property of this TriggerDeploymentPipelineStageRunProgress.
        :type build_pipeline_stage_id: str

        :param time_started:
            The value to assign to the time_started property of this TriggerDeploymentPipelineStageRunProgress.
        :type time_started: datetime

        :param time_finished:
            The value to assign to the time_finished property of this TriggerDeploymentPipelineStageRunProgress.
        :type time_finished: datetime

        :param status:
            The value to assign to the status property of this TriggerDeploymentPipelineStageRunProgress.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"
        :type status: str

        :param build_pipeline_stage_predecessors:
            The value to assign to the build_pipeline_stage_predecessors property of this TriggerDeploymentPipelineStageRunProgress.
        :type build_pipeline_stage_predecessors: oci.devops.models.BuildPipelineStagePredecessorCollection

        :param exported_variables:
            The value to assign to the exported_variables property of this TriggerDeploymentPipelineStageRunProgress.
        :type exported_variables: oci.devops.models.ExportedVariableCollection

        :param artifact_override_parameters:
            The value to assign to the artifact_override_parameters property of this TriggerDeploymentPipelineStageRunProgress.
        :type artifact_override_parameters: oci.devops.models.DeployArtifactOverrideArgumentCollection

        :param deployment_id:
            The value to assign to the deployment_id property of this TriggerDeploymentPipelineStageRunProgress.
        :type deployment_id: str

        """
        self.swagger_types = {
            'stage_display_name': 'str',
            'build_pipeline_stage_type': 'str',
            'build_pipeline_stage_id': 'str',
            'time_started': 'datetime',
            'time_finished': 'datetime',
            'status': 'str',
            'build_pipeline_stage_predecessors': 'BuildPipelineStagePredecessorCollection',
            'exported_variables': 'ExportedVariableCollection',
            'artifact_override_parameters': 'DeployArtifactOverrideArgumentCollection',
            'deployment_id': 'str'
        }

        self.attribute_map = {
            'stage_display_name': 'stageDisplayName',
            'build_pipeline_stage_type': 'buildPipelineStageType',
            'build_pipeline_stage_id': 'buildPipelineStageId',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished',
            'status': 'status',
            'build_pipeline_stage_predecessors': 'buildPipelineStagePredecessors',
            'exported_variables': 'exportedVariables',
            'artifact_override_parameters': 'artifactOverrideParameters',
            'deployment_id': 'deploymentId'
        }

        self._stage_display_name = None
        self._build_pipeline_stage_type = None
        self._build_pipeline_stage_id = None
        self._time_started = None
        self._time_finished = None
        self._status = None
        self._build_pipeline_stage_predecessors = None
        self._exported_variables = None
        self._artifact_override_parameters = None
        self._deployment_id = None
        self._build_pipeline_stage_type = 'TRIGGER_DEPLOYMENT_PIPELINE'

    @property
    def exported_variables(self):
        """
        Gets the exported_variables of this TriggerDeploymentPipelineStageRunProgress.

        :return: The exported_variables of this TriggerDeploymentPipelineStageRunProgress.
        :rtype: oci.devops.models.ExportedVariableCollection
        """
        return self._exported_variables

    @exported_variables.setter
    def exported_variables(self, exported_variables):
        """
        Sets the exported_variables of this TriggerDeploymentPipelineStageRunProgress.

        :param exported_variables: The exported_variables of this TriggerDeploymentPipelineStageRunProgress.
        :type: oci.devops.models.ExportedVariableCollection
        """
        self._exported_variables = exported_variables

    @property
    def artifact_override_parameters(self):
        """
        Gets the artifact_override_parameters of this TriggerDeploymentPipelineStageRunProgress.

        :return: The artifact_override_parameters of this TriggerDeploymentPipelineStageRunProgress.
        :rtype: oci.devops.models.DeployArtifactOverrideArgumentCollection
        """
        return self._artifact_override_parameters

    @artifact_override_parameters.setter
    def artifact_override_parameters(self, artifact_override_parameters):
        """
        Sets the artifact_override_parameters of this TriggerDeploymentPipelineStageRunProgress.

        :param artifact_override_parameters: The artifact_override_parameters of this TriggerDeploymentPipelineStageRunProgress.
        :type: oci.devops.models.DeployArtifactOverrideArgumentCollection
        """
        self._artifact_override_parameters = artifact_override_parameters

    @property
    def deployment_id(self):
        """
        Gets the deployment_id of this TriggerDeploymentPipelineStageRunProgress.
        Identifier of the deployment triggered.


        :return: The deployment_id of this TriggerDeploymentPipelineStageRunProgress.
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        """
        Sets the deployment_id of this TriggerDeploymentPipelineStageRunProgress.
        Identifier of the deployment triggered.


        :param deployment_id: The deployment_id of this TriggerDeploymentPipelineStageRunProgress.
        :type: str
        """
        self._deployment_id = deployment_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
