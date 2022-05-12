# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .deploy_artifact_source import DeployArtifactSource
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HelmRepositoryDeployArtifactSource(DeployArtifactSource):
    """
    Specifies Helm chart source details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HelmRepositoryDeployArtifactSource object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.HelmRepositoryDeployArtifactSource.deploy_artifact_source_type` attribute
        of this class is ``HELM_CHART`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param deploy_artifact_source_type:
            The value to assign to the deploy_artifact_source_type property of this HelmRepositoryDeployArtifactSource.
            Allowed values for this property are: "INLINE", "OCIR", "GENERIC_ARTIFACT", "HELM_CHART"
        :type deploy_artifact_source_type: str

        :param chart_url:
            The value to assign to the chart_url property of this HelmRepositoryDeployArtifactSource.
        :type chart_url: str

        :param deploy_artifact_version:
            The value to assign to the deploy_artifact_version property of this HelmRepositoryDeployArtifactSource.
        :type deploy_artifact_version: str

        """
        self.swagger_types = {
            'deploy_artifact_source_type': 'str',
            'chart_url': 'str',
            'deploy_artifact_version': 'str'
        }

        self.attribute_map = {
            'deploy_artifact_source_type': 'deployArtifactSourceType',
            'chart_url': 'chartUrl',
            'deploy_artifact_version': 'deployArtifactVersion'
        }

        self._deploy_artifact_source_type = None
        self._chart_url = None
        self._deploy_artifact_version = None
        self._deploy_artifact_source_type = 'HELM_CHART'

    @property
    def chart_url(self):
        """
        **[Required]** Gets the chart_url of this HelmRepositoryDeployArtifactSource.
        The URL of an OCIR repository.


        :return: The chart_url of this HelmRepositoryDeployArtifactSource.
        :rtype: str
        """
        return self._chart_url

    @chart_url.setter
    def chart_url(self, chart_url):
        """
        Sets the chart_url of this HelmRepositoryDeployArtifactSource.
        The URL of an OCIR repository.


        :param chart_url: The chart_url of this HelmRepositoryDeployArtifactSource.
        :type: str
        """
        self._chart_url = chart_url

    @property
    def deploy_artifact_version(self):
        """
        **[Required]** Gets the deploy_artifact_version of this HelmRepositoryDeployArtifactSource.
        Users can set this as a placeholder value that refers to a pipeline parameter, for example, ${appVersion}.


        :return: The deploy_artifact_version of this HelmRepositoryDeployArtifactSource.
        :rtype: str
        """
        return self._deploy_artifact_version

    @deploy_artifact_version.setter
    def deploy_artifact_version(self, deploy_artifact_version):
        """
        Sets the deploy_artifact_version of this HelmRepositoryDeployArtifactSource.
        Users can set this as a placeholder value that refers to a pipeline parameter, for example, ${appVersion}.


        :param deploy_artifact_version: The deploy_artifact_version of this HelmRepositoryDeployArtifactSource.
        :type: str
        """
        self._deploy_artifact_version = deploy_artifact_version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
