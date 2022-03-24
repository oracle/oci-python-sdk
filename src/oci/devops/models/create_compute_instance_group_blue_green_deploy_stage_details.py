# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_deploy_stage_details import CreateDeployStageDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateComputeInstanceGroupBlueGreenDeployStageDetails(CreateDeployStageDetails):
    """
    Specifies the Instance Group Blue-Green deployment stage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateComputeInstanceGroupBlueGreenDeployStageDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.CreateComputeInstanceGroupBlueGreenDeployStageDetails.deploy_stage_type` attribute
        of this class is ``COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        :type display_name: str

        :param deploy_stage_type:
            The value to assign to the deploy_stage_type property of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        :type deploy_stage_type: str

        :param deploy_pipeline_id:
            The value to assign to the deploy_pipeline_id property of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        :type deploy_pipeline_id: str

        :param deploy_stage_predecessor_collection:
            The value to assign to the deploy_stage_predecessor_collection property of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        :type deploy_stage_predecessor_collection: oci.devops.models.DeployStagePredecessorCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param deploy_environment_id_a:
            The value to assign to the deploy_environment_id_a property of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        :type deploy_environment_id_a: str

        :param deploy_environment_id_b:
            The value to assign to the deploy_environment_id_b property of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        :type deploy_environment_id_b: str

        :param deployment_spec_deploy_artifact_id:
            The value to assign to the deployment_spec_deploy_artifact_id property of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        :type deployment_spec_deploy_artifact_id: str

        :param deploy_artifact_ids:
            The value to assign to the deploy_artifact_ids property of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        :type deploy_artifact_ids: list[str]

        :param rollout_policy:
            The value to assign to the rollout_policy property of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        :type rollout_policy: oci.devops.models.ComputeInstanceGroupRolloutPolicy

        :param failure_policy:
            The value to assign to the failure_policy property of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        :type failure_policy: oci.devops.models.ComputeInstanceGroupFailurePolicy

        :param test_load_balancer_config:
            The value to assign to the test_load_balancer_config property of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        :type test_load_balancer_config: oci.devops.models.LoadBalancerConfig

        :param production_load_balancer_config:
            The value to assign to the production_load_balancer_config property of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        :type production_load_balancer_config: oci.devops.models.LoadBalancerConfig

        """
        self.swagger_types = {
            'description': 'str',
            'display_name': 'str',
            'deploy_stage_type': 'str',
            'deploy_pipeline_id': 'str',
            'deploy_stage_predecessor_collection': 'DeployStagePredecessorCollection',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'deploy_environment_id_a': 'str',
            'deploy_environment_id_b': 'str',
            'deployment_spec_deploy_artifact_id': 'str',
            'deploy_artifact_ids': 'list[str]',
            'rollout_policy': 'ComputeInstanceGroupRolloutPolicy',
            'failure_policy': 'ComputeInstanceGroupFailurePolicy',
            'test_load_balancer_config': 'LoadBalancerConfig',
            'production_load_balancer_config': 'LoadBalancerConfig'
        }

        self.attribute_map = {
            'description': 'description',
            'display_name': 'displayName',
            'deploy_stage_type': 'deployStageType',
            'deploy_pipeline_id': 'deployPipelineId',
            'deploy_stage_predecessor_collection': 'deployStagePredecessorCollection',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'deploy_environment_id_a': 'deployEnvironmentIdA',
            'deploy_environment_id_b': 'deployEnvironmentIdB',
            'deployment_spec_deploy_artifact_id': 'deploymentSpecDeployArtifactId',
            'deploy_artifact_ids': 'deployArtifactIds',
            'rollout_policy': 'rolloutPolicy',
            'failure_policy': 'failurePolicy',
            'test_load_balancer_config': 'testLoadBalancerConfig',
            'production_load_balancer_config': 'productionLoadBalancerConfig'
        }

        self._description = None
        self._display_name = None
        self._deploy_stage_type = None
        self._deploy_pipeline_id = None
        self._deploy_stage_predecessor_collection = None
        self._freeform_tags = None
        self._defined_tags = None
        self._deploy_environment_id_a = None
        self._deploy_environment_id_b = None
        self._deployment_spec_deploy_artifact_id = None
        self._deploy_artifact_ids = None
        self._rollout_policy = None
        self._failure_policy = None
        self._test_load_balancer_config = None
        self._production_load_balancer_config = None
        self._deploy_stage_type = 'COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT'

    @property
    def deploy_environment_id_a(self):
        """
        **[Required]** Gets the deploy_environment_id_a of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        First compute instance group environment OCID for deployment.


        :return: The deploy_environment_id_a of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        :rtype: str
        """
        return self._deploy_environment_id_a

    @deploy_environment_id_a.setter
    def deploy_environment_id_a(self, deploy_environment_id_a):
        """
        Sets the deploy_environment_id_a of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        First compute instance group environment OCID for deployment.


        :param deploy_environment_id_a: The deploy_environment_id_a of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        :type: str
        """
        self._deploy_environment_id_a = deploy_environment_id_a

    @property
    def deploy_environment_id_b(self):
        """
        **[Required]** Gets the deploy_environment_id_b of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        Second compute instance group environment OCID for deployment.


        :return: The deploy_environment_id_b of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        :rtype: str
        """
        return self._deploy_environment_id_b

    @deploy_environment_id_b.setter
    def deploy_environment_id_b(self, deploy_environment_id_b):
        """
        Sets the deploy_environment_id_b of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        Second compute instance group environment OCID for deployment.


        :param deploy_environment_id_b: The deploy_environment_id_b of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        :type: str
        """
        self._deploy_environment_id_b = deploy_environment_id_b

    @property
    def deployment_spec_deploy_artifact_id(self):
        """
        **[Required]** Gets the deployment_spec_deploy_artifact_id of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        The OCID of the artifact that contains the deployment specification.


        :return: The deployment_spec_deploy_artifact_id of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        :rtype: str
        """
        return self._deployment_spec_deploy_artifact_id

    @deployment_spec_deploy_artifact_id.setter
    def deployment_spec_deploy_artifact_id(self, deployment_spec_deploy_artifact_id):
        """
        Sets the deployment_spec_deploy_artifact_id of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        The OCID of the artifact that contains the deployment specification.


        :param deployment_spec_deploy_artifact_id: The deployment_spec_deploy_artifact_id of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        :type: str
        """
        self._deployment_spec_deploy_artifact_id = deployment_spec_deploy_artifact_id

    @property
    def deploy_artifact_ids(self):
        """
        Gets the deploy_artifact_ids of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        The list of file artifact OCIDs to deploy.


        :return: The deploy_artifact_ids of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        :rtype: list[str]
        """
        return self._deploy_artifact_ids

    @deploy_artifact_ids.setter
    def deploy_artifact_ids(self, deploy_artifact_ids):
        """
        Sets the deploy_artifact_ids of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        The list of file artifact OCIDs to deploy.


        :param deploy_artifact_ids: The deploy_artifact_ids of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        :type: list[str]
        """
        self._deploy_artifact_ids = deploy_artifact_ids

    @property
    def rollout_policy(self):
        """
        **[Required]** Gets the rollout_policy of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.

        :return: The rollout_policy of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        :rtype: oci.devops.models.ComputeInstanceGroupRolloutPolicy
        """
        return self._rollout_policy

    @rollout_policy.setter
    def rollout_policy(self, rollout_policy):
        """
        Sets the rollout_policy of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.

        :param rollout_policy: The rollout_policy of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        :type: oci.devops.models.ComputeInstanceGroupRolloutPolicy
        """
        self._rollout_policy = rollout_policy

    @property
    def failure_policy(self):
        """
        Gets the failure_policy of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.

        :return: The failure_policy of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        :rtype: oci.devops.models.ComputeInstanceGroupFailurePolicy
        """
        return self._failure_policy

    @failure_policy.setter
    def failure_policy(self, failure_policy):
        """
        Sets the failure_policy of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.

        :param failure_policy: The failure_policy of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        :type: oci.devops.models.ComputeInstanceGroupFailurePolicy
        """
        self._failure_policy = failure_policy

    @property
    def test_load_balancer_config(self):
        """
        Gets the test_load_balancer_config of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.

        :return: The test_load_balancer_config of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        :rtype: oci.devops.models.LoadBalancerConfig
        """
        return self._test_load_balancer_config

    @test_load_balancer_config.setter
    def test_load_balancer_config(self, test_load_balancer_config):
        """
        Sets the test_load_balancer_config of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.

        :param test_load_balancer_config: The test_load_balancer_config of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        :type: oci.devops.models.LoadBalancerConfig
        """
        self._test_load_balancer_config = test_load_balancer_config

    @property
    def production_load_balancer_config(self):
        """
        **[Required]** Gets the production_load_balancer_config of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.

        :return: The production_load_balancer_config of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        :rtype: oci.devops.models.LoadBalancerConfig
        """
        return self._production_load_balancer_config

    @production_load_balancer_config.setter
    def production_load_balancer_config(self, production_load_balancer_config):
        """
        Sets the production_load_balancer_config of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.

        :param production_load_balancer_config: The production_load_balancer_config of this CreateComputeInstanceGroupBlueGreenDeployStageDetails.
        :type: oci.devops.models.LoadBalancerConfig
        """
        self._production_load_balancer_config = production_load_balancer_config

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
