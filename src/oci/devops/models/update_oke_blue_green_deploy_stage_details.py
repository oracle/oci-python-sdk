# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_deploy_stage_details import UpdateDeployStageDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateOkeBlueGreenDeployStageDetails(UpdateDeployStageDetails):
    """
    Specifies the Container Engine for Kubernetes (OKE) cluster Blue-Green deployment stage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateOkeBlueGreenDeployStageDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.UpdateOkeBlueGreenDeployStageDetails.deploy_stage_type` attribute
        of this class is ``OKE_BLUE_GREEN_DEPLOYMENT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateOkeBlueGreenDeployStageDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this UpdateOkeBlueGreenDeployStageDetails.
        :type display_name: str

        :param deploy_stage_type:
            The value to assign to the deploy_stage_type property of this UpdateOkeBlueGreenDeployStageDetails.
        :type deploy_stage_type: str

        :param deploy_stage_predecessor_collection:
            The value to assign to the deploy_stage_predecessor_collection property of this UpdateOkeBlueGreenDeployStageDetails.
        :type deploy_stage_predecessor_collection: oci.devops.models.DeployStagePredecessorCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateOkeBlueGreenDeployStageDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateOkeBlueGreenDeployStageDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param kubernetes_manifest_deploy_artifact_ids:
            The value to assign to the kubernetes_manifest_deploy_artifact_ids property of this UpdateOkeBlueGreenDeployStageDetails.
        :type kubernetes_manifest_deploy_artifact_ids: list[str]

        """
        self.swagger_types = {
            'description': 'str',
            'display_name': 'str',
            'deploy_stage_type': 'str',
            'deploy_stage_predecessor_collection': 'DeployStagePredecessorCollection',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'kubernetes_manifest_deploy_artifact_ids': 'list[str]'
        }

        self.attribute_map = {
            'description': 'description',
            'display_name': 'displayName',
            'deploy_stage_type': 'deployStageType',
            'deploy_stage_predecessor_collection': 'deployStagePredecessorCollection',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'kubernetes_manifest_deploy_artifact_ids': 'kubernetesManifestDeployArtifactIds'
        }

        self._description = None
        self._display_name = None
        self._deploy_stage_type = None
        self._deploy_stage_predecessor_collection = None
        self._freeform_tags = None
        self._defined_tags = None
        self._kubernetes_manifest_deploy_artifact_ids = None
        self._deploy_stage_type = 'OKE_BLUE_GREEN_DEPLOYMENT'

    @property
    def kubernetes_manifest_deploy_artifact_ids(self):
        """
        Gets the kubernetes_manifest_deploy_artifact_ids of this UpdateOkeBlueGreenDeployStageDetails.
        List of Kubernetes manifest artifact OCIDs, the manifests should not include any job resource.


        :return: The kubernetes_manifest_deploy_artifact_ids of this UpdateOkeBlueGreenDeployStageDetails.
        :rtype: list[str]
        """
        return self._kubernetes_manifest_deploy_artifact_ids

    @kubernetes_manifest_deploy_artifact_ids.setter
    def kubernetes_manifest_deploy_artifact_ids(self, kubernetes_manifest_deploy_artifact_ids):
        """
        Sets the kubernetes_manifest_deploy_artifact_ids of this UpdateOkeBlueGreenDeployStageDetails.
        List of Kubernetes manifest artifact OCIDs, the manifests should not include any job resource.


        :param kubernetes_manifest_deploy_artifact_ids: The kubernetes_manifest_deploy_artifact_ids of this UpdateOkeBlueGreenDeployStageDetails.
        :type: list[str]
        """
        self._kubernetes_manifest_deploy_artifact_ids = kubernetes_manifest_deploy_artifact_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
