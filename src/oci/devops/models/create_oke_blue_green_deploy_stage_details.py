# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_deploy_stage_details import CreateDeployStageDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateOkeBlueGreenDeployStageDetails(CreateDeployStageDetails):
    """
    Specifies the Container Engine for Kubernetes (OKE) cluster Blue-Green deployment stage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateOkeBlueGreenDeployStageDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.CreateOkeBlueGreenDeployStageDetails.deploy_stage_type` attribute
        of this class is ``OKE_BLUE_GREEN_DEPLOYMENT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this CreateOkeBlueGreenDeployStageDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this CreateOkeBlueGreenDeployStageDetails.
        :type display_name: str

        :param deploy_stage_type:
            The value to assign to the deploy_stage_type property of this CreateOkeBlueGreenDeployStageDetails.
        :type deploy_stage_type: str

        :param deploy_pipeline_id:
            The value to assign to the deploy_pipeline_id property of this CreateOkeBlueGreenDeployStageDetails.
        :type deploy_pipeline_id: str

        :param deploy_stage_predecessor_collection:
            The value to assign to the deploy_stage_predecessor_collection property of this CreateOkeBlueGreenDeployStageDetails.
        :type deploy_stage_predecessor_collection: oci.devops.models.DeployStagePredecessorCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateOkeBlueGreenDeployStageDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateOkeBlueGreenDeployStageDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param oke_cluster_deploy_environment_id:
            The value to assign to the oke_cluster_deploy_environment_id property of this CreateOkeBlueGreenDeployStageDetails.
        :type oke_cluster_deploy_environment_id: str

        :param kubernetes_manifest_deploy_artifact_ids:
            The value to assign to the kubernetes_manifest_deploy_artifact_ids property of this CreateOkeBlueGreenDeployStageDetails.
        :type kubernetes_manifest_deploy_artifact_ids: list[str]

        :param blue_green_strategy:
            The value to assign to the blue_green_strategy property of this CreateOkeBlueGreenDeployStageDetails.
        :type blue_green_strategy: oci.devops.models.OkeBlueGreenStrategy

        """
        self.swagger_types = {
            'description': 'str',
            'display_name': 'str',
            'deploy_stage_type': 'str',
            'deploy_pipeline_id': 'str',
            'deploy_stage_predecessor_collection': 'DeployStagePredecessorCollection',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'oke_cluster_deploy_environment_id': 'str',
            'kubernetes_manifest_deploy_artifact_ids': 'list[str]',
            'blue_green_strategy': 'OkeBlueGreenStrategy'
        }

        self.attribute_map = {
            'description': 'description',
            'display_name': 'displayName',
            'deploy_stage_type': 'deployStageType',
            'deploy_pipeline_id': 'deployPipelineId',
            'deploy_stage_predecessor_collection': 'deployStagePredecessorCollection',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'oke_cluster_deploy_environment_id': 'okeClusterDeployEnvironmentId',
            'kubernetes_manifest_deploy_artifact_ids': 'kubernetesManifestDeployArtifactIds',
            'blue_green_strategy': 'blueGreenStrategy'
        }

        self._description = None
        self._display_name = None
        self._deploy_stage_type = None
        self._deploy_pipeline_id = None
        self._deploy_stage_predecessor_collection = None
        self._freeform_tags = None
        self._defined_tags = None
        self._oke_cluster_deploy_environment_id = None
        self._kubernetes_manifest_deploy_artifact_ids = None
        self._blue_green_strategy = None
        self._deploy_stage_type = 'OKE_BLUE_GREEN_DEPLOYMENT'

    @property
    def oke_cluster_deploy_environment_id(self):
        """
        **[Required]** Gets the oke_cluster_deploy_environment_id of this CreateOkeBlueGreenDeployStageDetails.
        Kubernetes cluster environment OCID for deployment.


        :return: The oke_cluster_deploy_environment_id of this CreateOkeBlueGreenDeployStageDetails.
        :rtype: str
        """
        return self._oke_cluster_deploy_environment_id

    @oke_cluster_deploy_environment_id.setter
    def oke_cluster_deploy_environment_id(self, oke_cluster_deploy_environment_id):
        """
        Sets the oke_cluster_deploy_environment_id of this CreateOkeBlueGreenDeployStageDetails.
        Kubernetes cluster environment OCID for deployment.


        :param oke_cluster_deploy_environment_id: The oke_cluster_deploy_environment_id of this CreateOkeBlueGreenDeployStageDetails.
        :type: str
        """
        self._oke_cluster_deploy_environment_id = oke_cluster_deploy_environment_id

    @property
    def kubernetes_manifest_deploy_artifact_ids(self):
        """
        **[Required]** Gets the kubernetes_manifest_deploy_artifact_ids of this CreateOkeBlueGreenDeployStageDetails.
        List of Kubernetes manifest artifact OCIDs.


        :return: The kubernetes_manifest_deploy_artifact_ids of this CreateOkeBlueGreenDeployStageDetails.
        :rtype: list[str]
        """
        return self._kubernetes_manifest_deploy_artifact_ids

    @kubernetes_manifest_deploy_artifact_ids.setter
    def kubernetes_manifest_deploy_artifact_ids(self, kubernetes_manifest_deploy_artifact_ids):
        """
        Sets the kubernetes_manifest_deploy_artifact_ids of this CreateOkeBlueGreenDeployStageDetails.
        List of Kubernetes manifest artifact OCIDs.


        :param kubernetes_manifest_deploy_artifact_ids: The kubernetes_manifest_deploy_artifact_ids of this CreateOkeBlueGreenDeployStageDetails.
        :type: list[str]
        """
        self._kubernetes_manifest_deploy_artifact_ids = kubernetes_manifest_deploy_artifact_ids

    @property
    def blue_green_strategy(self):
        """
        **[Required]** Gets the blue_green_strategy of this CreateOkeBlueGreenDeployStageDetails.

        :return: The blue_green_strategy of this CreateOkeBlueGreenDeployStageDetails.
        :rtype: oci.devops.models.OkeBlueGreenStrategy
        """
        return self._blue_green_strategy

    @blue_green_strategy.setter
    def blue_green_strategy(self, blue_green_strategy):
        """
        Sets the blue_green_strategy of this CreateOkeBlueGreenDeployStageDetails.

        :param blue_green_strategy: The blue_green_strategy of this CreateOkeBlueGreenDeployStageDetails.
        :type: oci.devops.models.OkeBlueGreenStrategy
        """
        self._blue_green_strategy = blue_green_strategy

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
