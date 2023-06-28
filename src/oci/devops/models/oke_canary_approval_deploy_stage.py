# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210630

from .deploy_stage import DeployStage
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OkeCanaryApprovalDeployStage(DeployStage):
    """
    Specifies the Container Engine for Kubernetes (OKE) cluster canary deployment approval stage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OkeCanaryApprovalDeployStage object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.OkeCanaryApprovalDeployStage.deploy_stage_type` attribute
        of this class is ``OKE_CANARY_APPROVAL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OkeCanaryApprovalDeployStage.
        :type id: str

        :param description:
            The value to assign to the description property of this OkeCanaryApprovalDeployStage.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this OkeCanaryApprovalDeployStage.
        :type display_name: str

        :param project_id:
            The value to assign to the project_id property of this OkeCanaryApprovalDeployStage.
        :type project_id: str

        :param deploy_pipeline_id:
            The value to assign to the deploy_pipeline_id property of this OkeCanaryApprovalDeployStage.
        :type deploy_pipeline_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this OkeCanaryApprovalDeployStage.
        :type compartment_id: str

        :param deploy_stage_type:
            The value to assign to the deploy_stage_type property of this OkeCanaryApprovalDeployStage.
            Allowed values for this property are: "WAIT", "COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT", "COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT", "COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT", "COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT", "COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT", "COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL", "OKE_BLUE_GREEN_DEPLOYMENT", "OKE_BLUE_GREEN_TRAFFIC_SHIFT", "OKE_CANARY_DEPLOYMENT", "OKE_CANARY_TRAFFIC_SHIFT", "OKE_CANARY_APPROVAL", "OKE_DEPLOYMENT", "DEPLOY_FUNCTION", "INVOKE_FUNCTION", "LOAD_BALANCER_TRAFFIC_SHIFT", "MANUAL_APPROVAL", "OKE_HELM_CHART_DEPLOYMENT", "SHELL"
        :type deploy_stage_type: str

        :param time_created:
            The value to assign to the time_created property of this OkeCanaryApprovalDeployStage.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this OkeCanaryApprovalDeployStage.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OkeCanaryApprovalDeployStage.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this OkeCanaryApprovalDeployStage.
        :type lifecycle_details: str

        :param deploy_stage_predecessor_collection:
            The value to assign to the deploy_stage_predecessor_collection property of this OkeCanaryApprovalDeployStage.
        :type deploy_stage_predecessor_collection: oci.devops.models.DeployStagePredecessorCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this OkeCanaryApprovalDeployStage.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this OkeCanaryApprovalDeployStage.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this OkeCanaryApprovalDeployStage.
        :type system_tags: dict(str, dict(str, object))

        :param oke_canary_traffic_shift_deploy_stage_id:
            The value to assign to the oke_canary_traffic_shift_deploy_stage_id property of this OkeCanaryApprovalDeployStage.
        :type oke_canary_traffic_shift_deploy_stage_id: str

        :param approval_policy:
            The value to assign to the approval_policy property of this OkeCanaryApprovalDeployStage.
        :type approval_policy: oci.devops.models.ApprovalPolicy

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
            'oke_canary_traffic_shift_deploy_stage_id': 'str',
            'approval_policy': 'ApprovalPolicy'
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
            'oke_canary_traffic_shift_deploy_stage_id': 'okeCanaryTrafficShiftDeployStageId',
            'approval_policy': 'approvalPolicy'
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
        self._oke_canary_traffic_shift_deploy_stage_id = None
        self._approval_policy = None
        self._deploy_stage_type = 'OKE_CANARY_APPROVAL'

    @property
    def oke_canary_traffic_shift_deploy_stage_id(self):
        """
        **[Required]** Gets the oke_canary_traffic_shift_deploy_stage_id of this OkeCanaryApprovalDeployStage.
        The OCID of an upstream OKE canary deployment traffic shift stage in this pipeline.


        :return: The oke_canary_traffic_shift_deploy_stage_id of this OkeCanaryApprovalDeployStage.
        :rtype: str
        """
        return self._oke_canary_traffic_shift_deploy_stage_id

    @oke_canary_traffic_shift_deploy_stage_id.setter
    def oke_canary_traffic_shift_deploy_stage_id(self, oke_canary_traffic_shift_deploy_stage_id):
        """
        Sets the oke_canary_traffic_shift_deploy_stage_id of this OkeCanaryApprovalDeployStage.
        The OCID of an upstream OKE canary deployment traffic shift stage in this pipeline.


        :param oke_canary_traffic_shift_deploy_stage_id: The oke_canary_traffic_shift_deploy_stage_id of this OkeCanaryApprovalDeployStage.
        :type: str
        """
        self._oke_canary_traffic_shift_deploy_stage_id = oke_canary_traffic_shift_deploy_stage_id

    @property
    def approval_policy(self):
        """
        **[Required]** Gets the approval_policy of this OkeCanaryApprovalDeployStage.

        :return: The approval_policy of this OkeCanaryApprovalDeployStage.
        :rtype: oci.devops.models.ApprovalPolicy
        """
        return self._approval_policy

    @approval_policy.setter
    def approval_policy(self, approval_policy):
        """
        Sets the approval_policy of this OkeCanaryApprovalDeployStage.

        :param approval_policy: The approval_policy of this OkeCanaryApprovalDeployStage.
        :type: oci.devops.models.ApprovalPolicy
        """
        self._approval_policy = approval_policy

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
