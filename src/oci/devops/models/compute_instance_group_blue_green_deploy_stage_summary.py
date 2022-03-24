# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .deploy_stage_summary import DeployStageSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ComputeInstanceGroupBlueGreenDeployStageSummary(DeployStageSummary):
    """
    Specifies the Instance Group Blue-Green deployment stage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ComputeInstanceGroupBlueGreenDeployStageSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.ComputeInstanceGroupBlueGreenDeployStageSummary.deploy_stage_type` attribute
        of this class is ``COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :type id: str

        :param description:
            The value to assign to the description property of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :type display_name: str

        :param project_id:
            The value to assign to the project_id property of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :type project_id: str

        :param deploy_pipeline_id:
            The value to assign to the deploy_pipeline_id property of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :type deploy_pipeline_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :type compartment_id: str

        :param deploy_stage_type:
            The value to assign to the deploy_stage_type property of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :type deploy_stage_type: str

        :param time_created:
            The value to assign to the time_created property of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :type lifecycle_details: str

        :param deploy_stage_predecessor_collection:
            The value to assign to the deploy_stage_predecessor_collection property of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :type deploy_stage_predecessor_collection: oci.devops.models.DeployStagePredecessorCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :type system_tags: dict(str, dict(str, object))

        :param deploy_environment_id_a:
            The value to assign to the deploy_environment_id_a property of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :type deploy_environment_id_a: str

        :param deploy_environment_id_b:
            The value to assign to the deploy_environment_id_b property of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :type deploy_environment_id_b: str

        :param deployment_spec_deploy_artifact_id:
            The value to assign to the deployment_spec_deploy_artifact_id property of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :type deployment_spec_deploy_artifact_id: str

        :param deploy_artifact_ids:
            The value to assign to the deploy_artifact_ids property of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :type deploy_artifact_ids: list[str]

        :param rollout_policy:
            The value to assign to the rollout_policy property of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :type rollout_policy: oci.devops.models.ComputeInstanceGroupRolloutPolicy

        :param failure_policy:
            The value to assign to the failure_policy property of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :type failure_policy: oci.devops.models.ComputeInstanceGroupFailurePolicy

        :param test_load_balancer_config:
            The value to assign to the test_load_balancer_config property of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :type test_load_balancer_config: oci.devops.models.LoadBalancerConfig

        :param production_load_balancer_config:
            The value to assign to the production_load_balancer_config property of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :type production_load_balancer_config: oci.devops.models.LoadBalancerConfig

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
            'deploy_environment_id_a': 'deployEnvironmentIdA',
            'deploy_environment_id_b': 'deployEnvironmentIdB',
            'deployment_spec_deploy_artifact_id': 'deploymentSpecDeployArtifactId',
            'deploy_artifact_ids': 'deployArtifactIds',
            'rollout_policy': 'rolloutPolicy',
            'failure_policy': 'failurePolicy',
            'test_load_balancer_config': 'testLoadBalancerConfig',
            'production_load_balancer_config': 'productionLoadBalancerConfig'
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
        **[Required]** Gets the deploy_environment_id_a of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        First compute instance group environment OCID for deployment.


        :return: The deploy_environment_id_a of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :rtype: str
        """
        return self._deploy_environment_id_a

    @deploy_environment_id_a.setter
    def deploy_environment_id_a(self, deploy_environment_id_a):
        """
        Sets the deploy_environment_id_a of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        First compute instance group environment OCID for deployment.


        :param deploy_environment_id_a: The deploy_environment_id_a of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :type: str
        """
        self._deploy_environment_id_a = deploy_environment_id_a

    @property
    def deploy_environment_id_b(self):
        """
        **[Required]** Gets the deploy_environment_id_b of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        Second compute instance group environment OCID for deployment.


        :return: The deploy_environment_id_b of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :rtype: str
        """
        return self._deploy_environment_id_b

    @deploy_environment_id_b.setter
    def deploy_environment_id_b(self, deploy_environment_id_b):
        """
        Sets the deploy_environment_id_b of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        Second compute instance group environment OCID for deployment.


        :param deploy_environment_id_b: The deploy_environment_id_b of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :type: str
        """
        self._deploy_environment_id_b = deploy_environment_id_b

    @property
    def deployment_spec_deploy_artifact_id(self):
        """
        **[Required]** Gets the deployment_spec_deploy_artifact_id of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        The OCID of the artifact that contains the deployment specification.


        :return: The deployment_spec_deploy_artifact_id of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :rtype: str
        """
        return self._deployment_spec_deploy_artifact_id

    @deployment_spec_deploy_artifact_id.setter
    def deployment_spec_deploy_artifact_id(self, deployment_spec_deploy_artifact_id):
        """
        Sets the deployment_spec_deploy_artifact_id of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        The OCID of the artifact that contains the deployment specification.


        :param deployment_spec_deploy_artifact_id: The deployment_spec_deploy_artifact_id of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :type: str
        """
        self._deployment_spec_deploy_artifact_id = deployment_spec_deploy_artifact_id

    @property
    def deploy_artifact_ids(self):
        """
        Gets the deploy_artifact_ids of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        The list of file artifact OCIDs to deploy.


        :return: The deploy_artifact_ids of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :rtype: list[str]
        """
        return self._deploy_artifact_ids

    @deploy_artifact_ids.setter
    def deploy_artifact_ids(self, deploy_artifact_ids):
        """
        Sets the deploy_artifact_ids of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        The list of file artifact OCIDs to deploy.


        :param deploy_artifact_ids: The deploy_artifact_ids of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :type: list[str]
        """
        self._deploy_artifact_ids = deploy_artifact_ids

    @property
    def rollout_policy(self):
        """
        **[Required]** Gets the rollout_policy of this ComputeInstanceGroupBlueGreenDeployStageSummary.

        :return: The rollout_policy of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :rtype: oci.devops.models.ComputeInstanceGroupRolloutPolicy
        """
        return self._rollout_policy

    @rollout_policy.setter
    def rollout_policy(self, rollout_policy):
        """
        Sets the rollout_policy of this ComputeInstanceGroupBlueGreenDeployStageSummary.

        :param rollout_policy: The rollout_policy of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :type: oci.devops.models.ComputeInstanceGroupRolloutPolicy
        """
        self._rollout_policy = rollout_policy

    @property
    def failure_policy(self):
        """
        Gets the failure_policy of this ComputeInstanceGroupBlueGreenDeployStageSummary.

        :return: The failure_policy of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :rtype: oci.devops.models.ComputeInstanceGroupFailurePolicy
        """
        return self._failure_policy

    @failure_policy.setter
    def failure_policy(self, failure_policy):
        """
        Sets the failure_policy of this ComputeInstanceGroupBlueGreenDeployStageSummary.

        :param failure_policy: The failure_policy of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :type: oci.devops.models.ComputeInstanceGroupFailurePolicy
        """
        self._failure_policy = failure_policy

    @property
    def test_load_balancer_config(self):
        """
        Gets the test_load_balancer_config of this ComputeInstanceGroupBlueGreenDeployStageSummary.

        :return: The test_load_balancer_config of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :rtype: oci.devops.models.LoadBalancerConfig
        """
        return self._test_load_balancer_config

    @test_load_balancer_config.setter
    def test_load_balancer_config(self, test_load_balancer_config):
        """
        Sets the test_load_balancer_config of this ComputeInstanceGroupBlueGreenDeployStageSummary.

        :param test_load_balancer_config: The test_load_balancer_config of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :type: oci.devops.models.LoadBalancerConfig
        """
        self._test_load_balancer_config = test_load_balancer_config

    @property
    def production_load_balancer_config(self):
        """
        **[Required]** Gets the production_load_balancer_config of this ComputeInstanceGroupBlueGreenDeployStageSummary.

        :return: The production_load_balancer_config of this ComputeInstanceGroupBlueGreenDeployStageSummary.
        :rtype: oci.devops.models.LoadBalancerConfig
        """
        return self._production_load_balancer_config

    @production_load_balancer_config.setter
    def production_load_balancer_config(self, production_load_balancer_config):
        """
        Sets the production_load_balancer_config of this ComputeInstanceGroupBlueGreenDeployStageSummary.

        :param production_load_balancer_config: The production_load_balancer_config of this ComputeInstanceGroupBlueGreenDeployStageSummary.
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
