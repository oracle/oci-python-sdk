# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .deployment_summary import DeploymentSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeployPipelineRedeploymentSummary(DeploymentSummary):
    """
    Summary of a full pipeline redeployment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DeployPipelineRedeploymentSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.DeployPipelineRedeploymentSummary.deployment_type` attribute
        of this class is ``PIPELINE_REDEPLOYMENT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param deployment_type:
            The value to assign to the deployment_type property of this DeployPipelineRedeploymentSummary.
        :type deployment_type: str

        :param id:
            The value to assign to the id property of this DeployPipelineRedeploymentSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this DeployPipelineRedeploymentSummary.
        :type display_name: str

        :param project_id:
            The value to assign to the project_id property of this DeployPipelineRedeploymentSummary.
        :type project_id: str

        :param deploy_pipeline_id:
            The value to assign to the deploy_pipeline_id property of this DeployPipelineRedeploymentSummary.
        :type deploy_pipeline_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DeployPipelineRedeploymentSummary.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this DeployPipelineRedeploymentSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DeployPipelineRedeploymentSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DeployPipelineRedeploymentSummary.
        :type lifecycle_state: str

        :param deployment_arguments:
            The value to assign to the deployment_arguments property of this DeployPipelineRedeploymentSummary.
        :type deployment_arguments: oci.devops.models.DeploymentArgumentCollection

        :param deploy_stage_override_arguments:
            The value to assign to the deploy_stage_override_arguments property of this DeployPipelineRedeploymentSummary.
        :type deploy_stage_override_arguments: oci.devops.models.DeployStageOverrideArgumentCollection

        :param deploy_artifact_override_arguments:
            The value to assign to the deploy_artifact_override_arguments property of this DeployPipelineRedeploymentSummary.
        :type deploy_artifact_override_arguments: oci.devops.models.DeployArtifactOverrideArgumentCollection

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this DeployPipelineRedeploymentSummary.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DeployPipelineRedeploymentSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DeployPipelineRedeploymentSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this DeployPipelineRedeploymentSummary.
        :type system_tags: dict(str, dict(str, object))

        :param previous_deployment_id:
            The value to assign to the previous_deployment_id property of this DeployPipelineRedeploymentSummary.
        :type previous_deployment_id: str

        """
        self.swagger_types = {
            'deployment_type': 'str',
            'id': 'str',
            'display_name': 'str',
            'project_id': 'str',
            'deploy_pipeline_id': 'str',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'deployment_arguments': 'DeploymentArgumentCollection',
            'deploy_stage_override_arguments': 'DeployStageOverrideArgumentCollection',
            'deploy_artifact_override_arguments': 'DeployArtifactOverrideArgumentCollection',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'previous_deployment_id': 'str'
        }

        self.attribute_map = {
            'deployment_type': 'deploymentType',
            'id': 'id',
            'display_name': 'displayName',
            'project_id': 'projectId',
            'deploy_pipeline_id': 'deployPipelineId',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'deployment_arguments': 'deploymentArguments',
            'deploy_stage_override_arguments': 'deployStageOverrideArguments',
            'deploy_artifact_override_arguments': 'deployArtifactOverrideArguments',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'previous_deployment_id': 'previousDeploymentId'
        }

        self._deployment_type = None
        self._id = None
        self._display_name = None
        self._project_id = None
        self._deploy_pipeline_id = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._deployment_arguments = None
        self._deploy_stage_override_arguments = None
        self._deploy_artifact_override_arguments = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._previous_deployment_id = None
        self._deployment_type = 'PIPELINE_REDEPLOYMENT'

    @property
    def previous_deployment_id(self):
        """
        **[Required]** Gets the previous_deployment_id of this DeployPipelineRedeploymentSummary.
        Specifies the OCID of the previous deployment to be redeployed.


        :return: The previous_deployment_id of this DeployPipelineRedeploymentSummary.
        :rtype: str
        """
        return self._previous_deployment_id

    @previous_deployment_id.setter
    def previous_deployment_id(self, previous_deployment_id):
        """
        Sets the previous_deployment_id of this DeployPipelineRedeploymentSummary.
        Specifies the OCID of the previous deployment to be redeployed.


        :param previous_deployment_id: The previous_deployment_id of this DeployPipelineRedeploymentSummary.
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
