# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .deploy_stage import DeployStage
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InvokeFunctionDeployStage(DeployStage):
    """
    Specifies Invoke Function stage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InvokeFunctionDeployStage object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.InvokeFunctionDeployStage.deploy_stage_type` attribute
        of this class is ``INVOKE_FUNCTION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this InvokeFunctionDeployStage.
        :type id: str

        :param description:
            The value to assign to the description property of this InvokeFunctionDeployStage.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this InvokeFunctionDeployStage.
        :type display_name: str

        :param project_id:
            The value to assign to the project_id property of this InvokeFunctionDeployStage.
        :type project_id: str

        :param deploy_pipeline_id:
            The value to assign to the deploy_pipeline_id property of this InvokeFunctionDeployStage.
        :type deploy_pipeline_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this InvokeFunctionDeployStage.
        :type compartment_id: str

        :param deploy_stage_type:
            The value to assign to the deploy_stage_type property of this InvokeFunctionDeployStage.
            Allowed values for this property are: "WAIT", "COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT", "COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT", "COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT", "COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT", "COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT", "COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL", "OKE_BLUE_GREEN_DEPLOYMENT", "OKE_BLUE_GREEN_TRAFFIC_SHIFT", "OKE_CANARY_DEPLOYMENT", "OKE_CANARY_TRAFFIC_SHIFT", "OKE_CANARY_APPROVAL", "OKE_DEPLOYMENT", "DEPLOY_FUNCTION", "INVOKE_FUNCTION", "LOAD_BALANCER_TRAFFIC_SHIFT", "MANUAL_APPROVAL", "OKE_HELM_CHART_DEPLOYMENT"
        :type deploy_stage_type: str

        :param time_created:
            The value to assign to the time_created property of this InvokeFunctionDeployStage.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this InvokeFunctionDeployStage.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this InvokeFunctionDeployStage.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this InvokeFunctionDeployStage.
        :type lifecycle_details: str

        :param deploy_stage_predecessor_collection:
            The value to assign to the deploy_stage_predecessor_collection property of this InvokeFunctionDeployStage.
        :type deploy_stage_predecessor_collection: oci.devops.models.DeployStagePredecessorCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this InvokeFunctionDeployStage.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this InvokeFunctionDeployStage.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this InvokeFunctionDeployStage.
        :type system_tags: dict(str, dict(str, object))

        :param function_deploy_environment_id:
            The value to assign to the function_deploy_environment_id property of this InvokeFunctionDeployStage.
        :type function_deploy_environment_id: str

        :param deploy_artifact_id:
            The value to assign to the deploy_artifact_id property of this InvokeFunctionDeployStage.
        :type deploy_artifact_id: str

        :param is_async:
            The value to assign to the is_async property of this InvokeFunctionDeployStage.
        :type is_async: bool

        :param is_validation_enabled:
            The value to assign to the is_validation_enabled property of this InvokeFunctionDeployStage.
        :type is_validation_enabled: bool

        """
        self.swagger_types = {
            'id': 'str',
            'description': 'str',
            'display_name': 'str',
            'project_id': 'str',
            'deploy_pipeline_id': 'str',
            'compartment_id': 'str',
            'deploy_stage_type': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'deploy_stage_predecessor_collection': 'DeployStagePredecessorCollection',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'function_deploy_environment_id': 'str',
            'deploy_artifact_id': 'str',
            'is_async': 'bool',
            'is_validation_enabled': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'description': 'description',
            'display_name': 'displayName',
            'project_id': 'projectId',
            'deploy_pipeline_id': 'deployPipelineId',
            'compartment_id': 'compartmentId',
            'deploy_stage_type': 'deployStageType',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'deploy_stage_predecessor_collection': 'deployStagePredecessorCollection',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'function_deploy_environment_id': 'functionDeployEnvironmentId',
            'deploy_artifact_id': 'deployArtifactId',
            'is_async': 'isAsync',
            'is_validation_enabled': 'isValidationEnabled'
        }

        self._id = None
        self._description = None
        self._display_name = None
        self._project_id = None
        self._deploy_pipeline_id = None
        self._compartment_id = None
        self._deploy_stage_type = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._deploy_stage_predecessor_collection = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._function_deploy_environment_id = None
        self._deploy_artifact_id = None
        self._is_async = None
        self._is_validation_enabled = None
        self._deploy_stage_type = 'INVOKE_FUNCTION'

    @property
    def function_deploy_environment_id(self):
        """
        **[Required]** Gets the function_deploy_environment_id of this InvokeFunctionDeployStage.
        Function environment OCID.


        :return: The function_deploy_environment_id of this InvokeFunctionDeployStage.
        :rtype: str
        """
        return self._function_deploy_environment_id

    @function_deploy_environment_id.setter
    def function_deploy_environment_id(self, function_deploy_environment_id):
        """
        Sets the function_deploy_environment_id of this InvokeFunctionDeployStage.
        Function environment OCID.


        :param function_deploy_environment_id: The function_deploy_environment_id of this InvokeFunctionDeployStage.
        :type: str
        """
        self._function_deploy_environment_id = function_deploy_environment_id

    @property
    def deploy_artifact_id(self):
        """
        Gets the deploy_artifact_id of this InvokeFunctionDeployStage.
        Optional binary artifact OCID user may provide to this stage.


        :return: The deploy_artifact_id of this InvokeFunctionDeployStage.
        :rtype: str
        """
        return self._deploy_artifact_id

    @deploy_artifact_id.setter
    def deploy_artifact_id(self, deploy_artifact_id):
        """
        Sets the deploy_artifact_id of this InvokeFunctionDeployStage.
        Optional binary artifact OCID user may provide to this stage.


        :param deploy_artifact_id: The deploy_artifact_id of this InvokeFunctionDeployStage.
        :type: str
        """
        self._deploy_artifact_id = deploy_artifact_id

    @property
    def is_async(self):
        """
        **[Required]** Gets the is_async of this InvokeFunctionDeployStage.
        A boolean flag specifies whether this stage executes asynchronously.


        :return: The is_async of this InvokeFunctionDeployStage.
        :rtype: bool
        """
        return self._is_async

    @is_async.setter
    def is_async(self, is_async):
        """
        Sets the is_async of this InvokeFunctionDeployStage.
        A boolean flag specifies whether this stage executes asynchronously.


        :param is_async: The is_async of this InvokeFunctionDeployStage.
        :type: bool
        """
        self._is_async = is_async

    @property
    def is_validation_enabled(self):
        """
        **[Required]** Gets the is_validation_enabled of this InvokeFunctionDeployStage.
        A boolean flag specifies whether the invoked function must be validated.


        :return: The is_validation_enabled of this InvokeFunctionDeployStage.
        :rtype: bool
        """
        return self._is_validation_enabled

    @is_validation_enabled.setter
    def is_validation_enabled(self, is_validation_enabled):
        """
        Sets the is_validation_enabled of this InvokeFunctionDeployStage.
        A boolean flag specifies whether the invoked function must be validated.


        :param is_validation_enabled: The is_validation_enabled of this InvokeFunctionDeployStage.
        :type: bool
        """
        self._is_validation_enabled = is_validation_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
