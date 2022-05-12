# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .deploy_stage import DeployStage
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FunctionDeployStage(DeployStage):
    """
    Specifies the Function stage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FunctionDeployStage object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.FunctionDeployStage.deploy_stage_type` attribute
        of this class is ``DEPLOY_FUNCTION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this FunctionDeployStage.
        :type id: str

        :param description:
            The value to assign to the description property of this FunctionDeployStage.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this FunctionDeployStage.
        :type display_name: str

        :param project_id:
            The value to assign to the project_id property of this FunctionDeployStage.
        :type project_id: str

        :param deploy_pipeline_id:
            The value to assign to the deploy_pipeline_id property of this FunctionDeployStage.
        :type deploy_pipeline_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this FunctionDeployStage.
        :type compartment_id: str

        :param deploy_stage_type:
            The value to assign to the deploy_stage_type property of this FunctionDeployStage.
            Allowed values for this property are: "WAIT", "COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT", "COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT", "COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT", "COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT", "COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT", "COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL", "OKE_BLUE_GREEN_DEPLOYMENT", "OKE_BLUE_GREEN_TRAFFIC_SHIFT", "OKE_CANARY_DEPLOYMENT", "OKE_CANARY_TRAFFIC_SHIFT", "OKE_CANARY_APPROVAL", "OKE_DEPLOYMENT", "DEPLOY_FUNCTION", "INVOKE_FUNCTION", "LOAD_BALANCER_TRAFFIC_SHIFT", "MANUAL_APPROVAL", "OKE_HELM_CHART_DEPLOYMENT"
        :type deploy_stage_type: str

        :param time_created:
            The value to assign to the time_created property of this FunctionDeployStage.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this FunctionDeployStage.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this FunctionDeployStage.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this FunctionDeployStage.
        :type lifecycle_details: str

        :param deploy_stage_predecessor_collection:
            The value to assign to the deploy_stage_predecessor_collection property of this FunctionDeployStage.
        :type deploy_stage_predecessor_collection: oci.devops.models.DeployStagePredecessorCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this FunctionDeployStage.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this FunctionDeployStage.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this FunctionDeployStage.
        :type system_tags: dict(str, dict(str, object))

        :param function_deploy_environment_id:
            The value to assign to the function_deploy_environment_id property of this FunctionDeployStage.
        :type function_deploy_environment_id: str

        :param docker_image_deploy_artifact_id:
            The value to assign to the docker_image_deploy_artifact_id property of this FunctionDeployStage.
        :type docker_image_deploy_artifact_id: str

        :param config:
            The value to assign to the config property of this FunctionDeployStage.
        :type config: dict(str, str)

        :param max_memory_in_mbs:
            The value to assign to the max_memory_in_mbs property of this FunctionDeployStage.
        :type max_memory_in_mbs: int

        :param function_timeout_in_seconds:
            The value to assign to the function_timeout_in_seconds property of this FunctionDeployStage.
        :type function_timeout_in_seconds: int

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
            'docker_image_deploy_artifact_id': 'str',
            'config': 'dict(str, str)',
            'max_memory_in_mbs': 'int',
            'function_timeout_in_seconds': 'int'
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
            'docker_image_deploy_artifact_id': 'dockerImageDeployArtifactId',
            'config': 'config',
            'max_memory_in_mbs': 'maxMemoryInMBs',
            'function_timeout_in_seconds': 'functionTimeoutInSeconds'
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
        self._docker_image_deploy_artifact_id = None
        self._config = None
        self._max_memory_in_mbs = None
        self._function_timeout_in_seconds = None
        self._deploy_stage_type = 'DEPLOY_FUNCTION'

    @property
    def function_deploy_environment_id(self):
        """
        **[Required]** Gets the function_deploy_environment_id of this FunctionDeployStage.
        Function environment OCID.


        :return: The function_deploy_environment_id of this FunctionDeployStage.
        :rtype: str
        """
        return self._function_deploy_environment_id

    @function_deploy_environment_id.setter
    def function_deploy_environment_id(self, function_deploy_environment_id):
        """
        Sets the function_deploy_environment_id of this FunctionDeployStage.
        Function environment OCID.


        :param function_deploy_environment_id: The function_deploy_environment_id of this FunctionDeployStage.
        :type: str
        """
        self._function_deploy_environment_id = function_deploy_environment_id

    @property
    def docker_image_deploy_artifact_id(self):
        """
        **[Required]** Gets the docker_image_deploy_artifact_id of this FunctionDeployStage.
        A Docker image artifact OCID.


        :return: The docker_image_deploy_artifact_id of this FunctionDeployStage.
        :rtype: str
        """
        return self._docker_image_deploy_artifact_id

    @docker_image_deploy_artifact_id.setter
    def docker_image_deploy_artifact_id(self, docker_image_deploy_artifact_id):
        """
        Sets the docker_image_deploy_artifact_id of this FunctionDeployStage.
        A Docker image artifact OCID.


        :param docker_image_deploy_artifact_id: The docker_image_deploy_artifact_id of this FunctionDeployStage.
        :type: str
        """
        self._docker_image_deploy_artifact_id = docker_image_deploy_artifact_id

    @property
    def config(self):
        """
        Gets the config of this FunctionDeployStage.
        User provided key and value pair configuration, which is assigned through constants or parameter.


        :return: The config of this FunctionDeployStage.
        :rtype: dict(str, str)
        """
        return self._config

    @config.setter
    def config(self, config):
        """
        Sets the config of this FunctionDeployStage.
        User provided key and value pair configuration, which is assigned through constants or parameter.


        :param config: The config of this FunctionDeployStage.
        :type: dict(str, str)
        """
        self._config = config

    @property
    def max_memory_in_mbs(self):
        """
        Gets the max_memory_in_mbs of this FunctionDeployStage.
        Maximum usable memory for the Function (in MB).


        :return: The max_memory_in_mbs of this FunctionDeployStage.
        :rtype: int
        """
        return self._max_memory_in_mbs

    @max_memory_in_mbs.setter
    def max_memory_in_mbs(self, max_memory_in_mbs):
        """
        Sets the max_memory_in_mbs of this FunctionDeployStage.
        Maximum usable memory for the Function (in MB).


        :param max_memory_in_mbs: The max_memory_in_mbs of this FunctionDeployStage.
        :type: int
        """
        self._max_memory_in_mbs = max_memory_in_mbs

    @property
    def function_timeout_in_seconds(self):
        """
        Gets the function_timeout_in_seconds of this FunctionDeployStage.
        Timeout for execution of the Function. Value in seconds.


        :return: The function_timeout_in_seconds of this FunctionDeployStage.
        :rtype: int
        """
        return self._function_timeout_in_seconds

    @function_timeout_in_seconds.setter
    def function_timeout_in_seconds(self, function_timeout_in_seconds):
        """
        Sets the function_timeout_in_seconds of this FunctionDeployStage.
        Timeout for execution of the Function. Value in seconds.


        :param function_timeout_in_seconds: The function_timeout_in_seconds of this FunctionDeployStage.
        :type: int
        """
        self._function_timeout_in_seconds = function_timeout_in_seconds

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
