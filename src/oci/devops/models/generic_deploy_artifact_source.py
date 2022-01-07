# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .deploy_artifact_source import DeployArtifactSource
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GenericDeployArtifactSource(DeployArtifactSource):
    """
    Specifies the Artifact Registry source details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GenericDeployArtifactSource object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.GenericDeployArtifactSource.deploy_artifact_source_type` attribute
        of this class is ``GENERIC_ARTIFACT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param deploy_artifact_source_type:
            The value to assign to the deploy_artifact_source_type property of this GenericDeployArtifactSource.
            Allowed values for this property are: "INLINE", "OCIR", "GENERIC_ARTIFACT"
        :type deploy_artifact_source_type: str

        :param repository_id:
            The value to assign to the repository_id property of this GenericDeployArtifactSource.
        :type repository_id: str

        :param deploy_artifact_path:
            The value to assign to the deploy_artifact_path property of this GenericDeployArtifactSource.
        :type deploy_artifact_path: str

        :param deploy_artifact_version:
            The value to assign to the deploy_artifact_version property of this GenericDeployArtifactSource.
        :type deploy_artifact_version: str

        """
        self.swagger_types = {
            'deploy_artifact_source_type': 'str',
            'repository_id': 'str',
            'deploy_artifact_path': 'str',
            'deploy_artifact_version': 'str'
        }

        self.attribute_map = {
            'deploy_artifact_source_type': 'deployArtifactSourceType',
            'repository_id': 'repositoryId',
            'deploy_artifact_path': 'deployArtifactPath',
            'deploy_artifact_version': 'deployArtifactVersion'
        }

        self._deploy_artifact_source_type = None
        self._repository_id = None
        self._deploy_artifact_path = None
        self._deploy_artifact_version = None
        self._deploy_artifact_source_type = 'GENERIC_ARTIFACT'

    @property
    def repository_id(self):
        """
        **[Required]** Gets the repository_id of this GenericDeployArtifactSource.
        The OCID of a repository


        :return: The repository_id of this GenericDeployArtifactSource.
        :rtype: str
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        """
        Sets the repository_id of this GenericDeployArtifactSource.
        The OCID of a repository


        :param repository_id: The repository_id of this GenericDeployArtifactSource.
        :type: str
        """
        self._repository_id = repository_id

    @property
    def deploy_artifact_path(self):
        """
        **[Required]** Gets the deploy_artifact_path of this GenericDeployArtifactSource.
        Specifies the artifact path in the repository.


        :return: The deploy_artifact_path of this GenericDeployArtifactSource.
        :rtype: str
        """
        return self._deploy_artifact_path

    @deploy_artifact_path.setter
    def deploy_artifact_path(self, deploy_artifact_path):
        """
        Sets the deploy_artifact_path of this GenericDeployArtifactSource.
        Specifies the artifact path in the repository.


        :param deploy_artifact_path: The deploy_artifact_path of this GenericDeployArtifactSource.
        :type: str
        """
        self._deploy_artifact_path = deploy_artifact_path

    @property
    def deploy_artifact_version(self):
        """
        **[Required]** Gets the deploy_artifact_version of this GenericDeployArtifactSource.
        Users can set this as a placeholder value that refers to a pipeline parameter, for example, ${appVersion}.


        :return: The deploy_artifact_version of this GenericDeployArtifactSource.
        :rtype: str
        """
        return self._deploy_artifact_version

    @deploy_artifact_version.setter
    def deploy_artifact_version(self, deploy_artifact_version):
        """
        Sets the deploy_artifact_version of this GenericDeployArtifactSource.
        Users can set this as a placeholder value that refers to a pipeline parameter, for example, ${appVersion}.


        :param deploy_artifact_version: The deploy_artifact_version of this GenericDeployArtifactSource.
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
