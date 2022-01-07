# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .deployment_summary import DeploymentSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SingleDeployStageDeploymentSummary(DeploymentSummary):
    """
    Summary of single stage deployment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SingleDeployStageDeploymentSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.SingleDeployStageDeploymentSummary.deployment_type` attribute
        of this class is ``SINGLE_STAGE_DEPLOYMENT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param deployment_type:
            The value to assign to the deployment_type property of this SingleDeployStageDeploymentSummary.
        :type deployment_type: str

        :param id:
            The value to assign to the id property of this SingleDeployStageDeploymentSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this SingleDeployStageDeploymentSummary.
        :type display_name: str

        :param project_id:
            The value to assign to the project_id property of this SingleDeployStageDeploymentSummary.
        :type project_id: str

        :param deploy_pipeline_id:
            The value to assign to the deploy_pipeline_id property of this SingleDeployStageDeploymentSummary.
        :type deploy_pipeline_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this SingleDeployStageDeploymentSummary.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this SingleDeployStageDeploymentSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this SingleDeployStageDeploymentSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SingleDeployStageDeploymentSummary.
        :type lifecycle_state: str

        :param deployment_arguments:
            The value to assign to the deployment_arguments property of this SingleDeployStageDeploymentSummary.
        :type deployment_arguments: oci.devops.models.DeploymentArgumentCollection

        :param deploy_artifact_override_arguments:
            The value to assign to the deploy_artifact_override_arguments property of this SingleDeployStageDeploymentSummary.
        :type deploy_artifact_override_arguments: oci.devops.models.DeployArtifactOverrideArgumentCollection

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this SingleDeployStageDeploymentSummary.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this SingleDeployStageDeploymentSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this SingleDeployStageDeploymentSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this SingleDeployStageDeploymentSummary.
        :type system_tags: dict(str, dict(str, object))

        :param deploy_stage_id:
            The value to assign to the deploy_stage_id property of this SingleDeployStageDeploymentSummary.
        :type deploy_stage_id: str

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
            'deploy_artifact_override_arguments': 'DeployArtifactOverrideArgumentCollection',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'deploy_stage_id': 'str'
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
            'deploy_artifact_override_arguments': 'deployArtifactOverrideArguments',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'deploy_stage_id': 'deployStageId'
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
        self._deploy_artifact_override_arguments = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._deploy_stage_id = None
        self._deployment_type = 'SINGLE_STAGE_DEPLOYMENT'

    @property
    def deploy_stage_id(self):
        """
        Gets the deploy_stage_id of this SingleDeployStageDeploymentSummary.
        Specifies the OCID of the stage to be deployed.


        :return: The deploy_stage_id of this SingleDeployStageDeploymentSummary.
        :rtype: str
        """
        return self._deploy_stage_id

    @deploy_stage_id.setter
    def deploy_stage_id(self, deploy_stage_id):
        """
        Sets the deploy_stage_id of this SingleDeployStageDeploymentSummary.
        Specifies the OCID of the stage to be deployed.


        :param deploy_stage_id: The deploy_stage_id of this SingleDeployStageDeploymentSummary.
        :type: str
        """
        self._deploy_stage_id = deploy_stage_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
