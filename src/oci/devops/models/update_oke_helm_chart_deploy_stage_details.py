# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_deploy_stage_details import UpdateDeployStageDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateOkeHelmChartDeployStageDetails(UpdateDeployStageDetails):
    """
    Specifies the Kubernetes cluster deployment stage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateOkeHelmChartDeployStageDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.UpdateOkeHelmChartDeployStageDetails.deploy_stage_type` attribute
        of this class is ``OKE_HELM_CHART_DEPLOYMENT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateOkeHelmChartDeployStageDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this UpdateOkeHelmChartDeployStageDetails.
        :type display_name: str

        :param deploy_stage_type:
            The value to assign to the deploy_stage_type property of this UpdateOkeHelmChartDeployStageDetails.
        :type deploy_stage_type: str

        :param deploy_stage_predecessor_collection:
            The value to assign to the deploy_stage_predecessor_collection property of this UpdateOkeHelmChartDeployStageDetails.
        :type deploy_stage_predecessor_collection: oci.devops.models.DeployStagePredecessorCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateOkeHelmChartDeployStageDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateOkeHelmChartDeployStageDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param oke_cluster_deploy_environment_id:
            The value to assign to the oke_cluster_deploy_environment_id property of this UpdateOkeHelmChartDeployStageDetails.
        :type oke_cluster_deploy_environment_id: str

        :param helm_chart_deploy_artifact_id:
            The value to assign to the helm_chart_deploy_artifact_id property of this UpdateOkeHelmChartDeployStageDetails.
        :type helm_chart_deploy_artifact_id: str

        :param values_artifact_ids:
            The value to assign to the values_artifact_ids property of this UpdateOkeHelmChartDeployStageDetails.
        :type values_artifact_ids: list[str]

        :param release_name:
            The value to assign to the release_name property of this UpdateOkeHelmChartDeployStageDetails.
        :type release_name: str

        :param namespace:
            The value to assign to the namespace property of this UpdateOkeHelmChartDeployStageDetails.
        :type namespace: str

        :param timeout_in_seconds:
            The value to assign to the timeout_in_seconds property of this UpdateOkeHelmChartDeployStageDetails.
        :type timeout_in_seconds: int

        :param rollback_policy:
            The value to assign to the rollback_policy property of this UpdateOkeHelmChartDeployStageDetails.
        :type rollback_policy: oci.devops.models.DeployStageRollbackPolicy

        """
        self.swagger_types = {
            'description': 'str',
            'display_name': 'str',
            'deploy_stage_type': 'str',
            'deploy_stage_predecessor_collection': 'DeployStagePredecessorCollection',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'oke_cluster_deploy_environment_id': 'str',
            'helm_chart_deploy_artifact_id': 'str',
            'values_artifact_ids': 'list[str]',
            'release_name': 'str',
            'namespace': 'str',
            'timeout_in_seconds': 'int',
            'rollback_policy': 'DeployStageRollbackPolicy'
        }

        self.attribute_map = {
            'description': 'description',
            'display_name': 'displayName',
            'deploy_stage_type': 'deployStageType',
            'deploy_stage_predecessor_collection': 'deployStagePredecessorCollection',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'oke_cluster_deploy_environment_id': 'okeClusterDeployEnvironmentId',
            'helm_chart_deploy_artifact_id': 'helmChartDeployArtifactId',
            'values_artifact_ids': 'valuesArtifactIds',
            'release_name': 'releaseName',
            'namespace': 'namespace',
            'timeout_in_seconds': 'timeoutInSeconds',
            'rollback_policy': 'rollbackPolicy'
        }

        self._description = None
        self._display_name = None
        self._deploy_stage_type = None
        self._deploy_stage_predecessor_collection = None
        self._freeform_tags = None
        self._defined_tags = None
        self._oke_cluster_deploy_environment_id = None
        self._helm_chart_deploy_artifact_id = None
        self._values_artifact_ids = None
        self._release_name = None
        self._namespace = None
        self._timeout_in_seconds = None
        self._rollback_policy = None
        self._deploy_stage_type = 'OKE_HELM_CHART_DEPLOYMENT'

    @property
    def oke_cluster_deploy_environment_id(self):
        """
        Gets the oke_cluster_deploy_environment_id of this UpdateOkeHelmChartDeployStageDetails.
        Kubernetes cluster environment OCID for deployment.


        :return: The oke_cluster_deploy_environment_id of this UpdateOkeHelmChartDeployStageDetails.
        :rtype: str
        """
        return self._oke_cluster_deploy_environment_id

    @oke_cluster_deploy_environment_id.setter
    def oke_cluster_deploy_environment_id(self, oke_cluster_deploy_environment_id):
        """
        Sets the oke_cluster_deploy_environment_id of this UpdateOkeHelmChartDeployStageDetails.
        Kubernetes cluster environment OCID for deployment.


        :param oke_cluster_deploy_environment_id: The oke_cluster_deploy_environment_id of this UpdateOkeHelmChartDeployStageDetails.
        :type: str
        """
        self._oke_cluster_deploy_environment_id = oke_cluster_deploy_environment_id

    @property
    def helm_chart_deploy_artifact_id(self):
        """
        Gets the helm_chart_deploy_artifact_id of this UpdateOkeHelmChartDeployStageDetails.
        Helm chart artifact OCID.


        :return: The helm_chart_deploy_artifact_id of this UpdateOkeHelmChartDeployStageDetails.
        :rtype: str
        """
        return self._helm_chart_deploy_artifact_id

    @helm_chart_deploy_artifact_id.setter
    def helm_chart_deploy_artifact_id(self, helm_chart_deploy_artifact_id):
        """
        Sets the helm_chart_deploy_artifact_id of this UpdateOkeHelmChartDeployStageDetails.
        Helm chart artifact OCID.


        :param helm_chart_deploy_artifact_id: The helm_chart_deploy_artifact_id of this UpdateOkeHelmChartDeployStageDetails.
        :type: str
        """
        self._helm_chart_deploy_artifact_id = helm_chart_deploy_artifact_id

    @property
    def values_artifact_ids(self):
        """
        Gets the values_artifact_ids of this UpdateOkeHelmChartDeployStageDetails.
        List of values.yaml file artifact OCIDs.


        :return: The values_artifact_ids of this UpdateOkeHelmChartDeployStageDetails.
        :rtype: list[str]
        """
        return self._values_artifact_ids

    @values_artifact_ids.setter
    def values_artifact_ids(self, values_artifact_ids):
        """
        Sets the values_artifact_ids of this UpdateOkeHelmChartDeployStageDetails.
        List of values.yaml file artifact OCIDs.


        :param values_artifact_ids: The values_artifact_ids of this UpdateOkeHelmChartDeployStageDetails.
        :type: list[str]
        """
        self._values_artifact_ids = values_artifact_ids

    @property
    def release_name(self):
        """
        Gets the release_name of this UpdateOkeHelmChartDeployStageDetails.
        Name of the Helm chart release.


        :return: The release_name of this UpdateOkeHelmChartDeployStageDetails.
        :rtype: str
        """
        return self._release_name

    @release_name.setter
    def release_name(self, release_name):
        """
        Sets the release_name of this UpdateOkeHelmChartDeployStageDetails.
        Name of the Helm chart release.


        :param release_name: The release_name of this UpdateOkeHelmChartDeployStageDetails.
        :type: str
        """
        self._release_name = release_name

    @property
    def namespace(self):
        """
        Gets the namespace of this UpdateOkeHelmChartDeployStageDetails.
        Default namespace to be used for Kubernetes deployment when not specified in the manifest.


        :return: The namespace of this UpdateOkeHelmChartDeployStageDetails.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this UpdateOkeHelmChartDeployStageDetails.
        Default namespace to be used for Kubernetes deployment when not specified in the manifest.


        :param namespace: The namespace of this UpdateOkeHelmChartDeployStageDetails.
        :type: str
        """
        self._namespace = namespace

    @property
    def timeout_in_seconds(self):
        """
        Gets the timeout_in_seconds of this UpdateOkeHelmChartDeployStageDetails.
        Time to wait for execution of a helm stage. Defaults to 300 seconds.


        :return: The timeout_in_seconds of this UpdateOkeHelmChartDeployStageDetails.
        :rtype: int
        """
        return self._timeout_in_seconds

    @timeout_in_seconds.setter
    def timeout_in_seconds(self, timeout_in_seconds):
        """
        Sets the timeout_in_seconds of this UpdateOkeHelmChartDeployStageDetails.
        Time to wait for execution of a helm stage. Defaults to 300 seconds.


        :param timeout_in_seconds: The timeout_in_seconds of this UpdateOkeHelmChartDeployStageDetails.
        :type: int
        """
        self._timeout_in_seconds = timeout_in_seconds

    @property
    def rollback_policy(self):
        """
        Gets the rollback_policy of this UpdateOkeHelmChartDeployStageDetails.

        :return: The rollback_policy of this UpdateOkeHelmChartDeployStageDetails.
        :rtype: oci.devops.models.DeployStageRollbackPolicy
        """
        return self._rollback_policy

    @rollback_policy.setter
    def rollback_policy(self, rollback_policy):
        """
        Sets the rollback_policy of this UpdateOkeHelmChartDeployStageDetails.

        :param rollback_policy: The rollback_policy of this UpdateOkeHelmChartDeployStageDetails.
        :type: oci.devops.models.DeployStageRollbackPolicy
        """
        self._rollback_policy = rollback_policy

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
