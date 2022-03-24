# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .deployment import Deployment
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeployPipelineRedeployment(Deployment):
    """
    Redeployment of the full pipeline of a previous deployment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DeployPipelineRedeployment object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.DeployPipelineRedeployment.deployment_type` attribute
        of this class is ``PIPELINE_REDEPLOYMENT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param deploy_pipeline_artifacts:
            The value to assign to the deploy_pipeline_artifacts property of this DeployPipelineRedeployment.
        :type deploy_pipeline_artifacts: oci.devops.models.DeployPipelineArtifactCollection

        :param deploy_pipeline_environments:
            The value to assign to the deploy_pipeline_environments property of this DeployPipelineRedeployment.
        :type deploy_pipeline_environments: oci.devops.models.DeployPipelineEnvironmentCollection

        :param deployment_type:
            The value to assign to the deployment_type property of this DeployPipelineRedeployment.
            Allowed values for this property are: "PIPELINE_DEPLOYMENT", "PIPELINE_REDEPLOYMENT", "SINGLE_STAGE_DEPLOYMENT", "SINGLE_STAGE_REDEPLOYMENT"
        :type deployment_type: str

        :param id:
            The value to assign to the id property of this DeployPipelineRedeployment.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this DeployPipelineRedeployment.
        :type display_name: str

        :param project_id:
            The value to assign to the project_id property of this DeployPipelineRedeployment.
        :type project_id: str

        :param deploy_pipeline_id:
            The value to assign to the deploy_pipeline_id property of this DeployPipelineRedeployment.
        :type deploy_pipeline_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DeployPipelineRedeployment.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this DeployPipelineRedeployment.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DeployPipelineRedeployment.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DeployPipelineRedeployment.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this DeployPipelineRedeployment.
        :type lifecycle_details: str

        :param deployment_arguments:
            The value to assign to the deployment_arguments property of this DeployPipelineRedeployment.
        :type deployment_arguments: oci.devops.models.DeploymentArgumentCollection

        :param deploy_artifact_override_arguments:
            The value to assign to the deploy_artifact_override_arguments property of this DeployPipelineRedeployment.
        :type deploy_artifact_override_arguments: oci.devops.models.DeployArtifactOverrideArgumentCollection

        :param deployment_execution_progress:
            The value to assign to the deployment_execution_progress property of this DeployPipelineRedeployment.
        :type deployment_execution_progress: oci.devops.models.DeploymentExecutionProgress

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DeployPipelineRedeployment.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DeployPipelineRedeployment.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this DeployPipelineRedeployment.
        :type system_tags: dict(str, dict(str, object))

        :param previous_deployment_id:
            The value to assign to the previous_deployment_id property of this DeployPipelineRedeployment.
        :type previous_deployment_id: str

        """
        self.swagger_types = {
            'deploy_pipeline_artifacts': 'DeployPipelineArtifactCollection',
            'deploy_pipeline_environments': 'DeployPipelineEnvironmentCollection',
            'deployment_type': 'str',
            'id': 'str',
            'display_name': 'str',
            'project_id': 'str',
            'deploy_pipeline_id': 'str',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'deployment_arguments': 'DeploymentArgumentCollection',
            'deploy_artifact_override_arguments': 'DeployArtifactOverrideArgumentCollection',
            'deployment_execution_progress': 'DeploymentExecutionProgress',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'previous_deployment_id': 'str'
        }

        self.attribute_map = {
            'deploy_pipeline_artifacts': 'deployPipelineArtifacts',
            'deploy_pipeline_environments': 'deployPipelineEnvironments',
            'deployment_type': 'deploymentType',
            'id': 'id',
            'display_name': 'displayName',
            'project_id': 'projectId',
            'deploy_pipeline_id': 'deployPipelineId',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'deployment_arguments': 'deploymentArguments',
            'deploy_artifact_override_arguments': 'deployArtifactOverrideArguments',
            'deployment_execution_progress': 'deploymentExecutionProgress',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'previous_deployment_id': 'previousDeploymentId'
        }

        self._deploy_pipeline_artifacts = None
        self._deploy_pipeline_environments = None
        self._deployment_type = None
        self._id = None
        self._display_name = None
        self._project_id = None
        self._deploy_pipeline_id = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._deployment_arguments = None
        self._deploy_artifact_override_arguments = None
        self._deployment_execution_progress = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._previous_deployment_id = None
        self._deployment_type = 'PIPELINE_REDEPLOYMENT'

    @property
    def previous_deployment_id(self):
        """
        Gets the previous_deployment_id of this DeployPipelineRedeployment.
        Specifies the OCID of the previous deployment to be redeployed.


        :return: The previous_deployment_id of this DeployPipelineRedeployment.
        :rtype: str
        """
        return self._previous_deployment_id

    @previous_deployment_id.setter
    def previous_deployment_id(self, previous_deployment_id):
        """
        Sets the previous_deployment_id of this DeployPipelineRedeployment.
        Specifies the OCID of the previous deployment to be redeployed.


        :param previous_deployment_id: The previous_deployment_id of this DeployPipelineRedeployment.
        :type: str
        """
        self._previous_deployment_id = previous_deployment_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
