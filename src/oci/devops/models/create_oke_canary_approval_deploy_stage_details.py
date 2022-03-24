# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_deploy_stage_details import CreateDeployStageDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateOkeCanaryApprovalDeployStageDetails(CreateDeployStageDetails):
    """
    Specifies the Container Engine for Kubernetes (OKE) cluster canary deployment approval stage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateOkeCanaryApprovalDeployStageDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.CreateOkeCanaryApprovalDeployStageDetails.deploy_stage_type` attribute
        of this class is ``OKE_CANARY_APPROVAL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this CreateOkeCanaryApprovalDeployStageDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this CreateOkeCanaryApprovalDeployStageDetails.
        :type display_name: str

        :param deploy_stage_type:
            The value to assign to the deploy_stage_type property of this CreateOkeCanaryApprovalDeployStageDetails.
        :type deploy_stage_type: str

        :param deploy_pipeline_id:
            The value to assign to the deploy_pipeline_id property of this CreateOkeCanaryApprovalDeployStageDetails.
        :type deploy_pipeline_id: str

        :param deploy_stage_predecessor_collection:
            The value to assign to the deploy_stage_predecessor_collection property of this CreateOkeCanaryApprovalDeployStageDetails.
        :type deploy_stage_predecessor_collection: oci.devops.models.DeployStagePredecessorCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateOkeCanaryApprovalDeployStageDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateOkeCanaryApprovalDeployStageDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param oke_canary_traffic_shift_deploy_stage_id:
            The value to assign to the oke_canary_traffic_shift_deploy_stage_id property of this CreateOkeCanaryApprovalDeployStageDetails.
        :type oke_canary_traffic_shift_deploy_stage_id: str

        :param approval_policy:
            The value to assign to the approval_policy property of this CreateOkeCanaryApprovalDeployStageDetails.
        :type approval_policy: oci.devops.models.ApprovalPolicy

        """
        self.swagger_types = {
            'description': 'str',
            'display_name': 'str',
            'deploy_stage_type': 'str',
            'deploy_pipeline_id': 'str',
            'deploy_stage_predecessor_collection': 'DeployStagePredecessorCollection',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'oke_canary_traffic_shift_deploy_stage_id': 'str',
            'approval_policy': 'ApprovalPolicy'
        }

        self.attribute_map = {
            'description': 'description',
            'display_name': 'displayName',
            'deploy_stage_type': 'deployStageType',
            'deploy_pipeline_id': 'deployPipelineId',
            'deploy_stage_predecessor_collection': 'deployStagePredecessorCollection',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'oke_canary_traffic_shift_deploy_stage_id': 'okeCanaryTrafficShiftDeployStageId',
            'approval_policy': 'approvalPolicy'
        }

        self._description = None
        self._display_name = None
        self._deploy_stage_type = None
        self._deploy_pipeline_id = None
        self._deploy_stage_predecessor_collection = None
        self._freeform_tags = None
        self._defined_tags = None
        self._oke_canary_traffic_shift_deploy_stage_id = None
        self._approval_policy = None
        self._deploy_stage_type = 'OKE_CANARY_APPROVAL'

    @property
    def oke_canary_traffic_shift_deploy_stage_id(self):
        """
        **[Required]** Gets the oke_canary_traffic_shift_deploy_stage_id of this CreateOkeCanaryApprovalDeployStageDetails.
        The OCID of an upstream OKE canary deployment traffic shift stage in this pipeline.


        :return: The oke_canary_traffic_shift_deploy_stage_id of this CreateOkeCanaryApprovalDeployStageDetails.
        :rtype: str
        """
        return self._oke_canary_traffic_shift_deploy_stage_id

    @oke_canary_traffic_shift_deploy_stage_id.setter
    def oke_canary_traffic_shift_deploy_stage_id(self, oke_canary_traffic_shift_deploy_stage_id):
        """
        Sets the oke_canary_traffic_shift_deploy_stage_id of this CreateOkeCanaryApprovalDeployStageDetails.
        The OCID of an upstream OKE canary deployment traffic shift stage in this pipeline.


        :param oke_canary_traffic_shift_deploy_stage_id: The oke_canary_traffic_shift_deploy_stage_id of this CreateOkeCanaryApprovalDeployStageDetails.
        :type: str
        """
        self._oke_canary_traffic_shift_deploy_stage_id = oke_canary_traffic_shift_deploy_stage_id

    @property
    def approval_policy(self):
        """
        **[Required]** Gets the approval_policy of this CreateOkeCanaryApprovalDeployStageDetails.

        :return: The approval_policy of this CreateOkeCanaryApprovalDeployStageDetails.
        :rtype: oci.devops.models.ApprovalPolicy
        """
        return self._approval_policy

    @approval_policy.setter
    def approval_policy(self, approval_policy):
        """
        Sets the approval_policy of this CreateOkeCanaryApprovalDeployStageDetails.

        :param approval_policy: The approval_policy of this CreateOkeCanaryApprovalDeployStageDetails.
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
