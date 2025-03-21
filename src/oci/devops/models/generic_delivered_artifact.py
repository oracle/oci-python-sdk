# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210630

from .delivered_artifact import DeliveredArtifact
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GenericDeliveredArtifact(DeliveredArtifact):
    """
    Details of the generic artifacts delivered through the Deliver Artifacts stage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GenericDeliveredArtifact object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.GenericDeliveredArtifact.artifact_type` attribute
        of this class is ``GENERIC_ARTIFACT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param deploy_artifact_id:
            The value to assign to the deploy_artifact_id property of this GenericDeliveredArtifact.
        :type deploy_artifact_id: str

        :param output_artifact_name:
            The value to assign to the output_artifact_name property of this GenericDeliveredArtifact.
        :type output_artifact_name: str

        :param artifact_type:
            The value to assign to the artifact_type property of this GenericDeliveredArtifact.
            Allowed values for this property are: "GENERIC_ARTIFACT", "OCIR"
        :type artifact_type: str

        :param artifact_repository_id:
            The value to assign to the artifact_repository_id property of this GenericDeliveredArtifact.
        :type artifact_repository_id: str

        :param delivered_artifact_id:
            The value to assign to the delivered_artifact_id property of this GenericDeliveredArtifact.
        :type delivered_artifact_id: str

        :param path:
            The value to assign to the path property of this GenericDeliveredArtifact.
        :type path: str

        :param version:
            The value to assign to the version property of this GenericDeliveredArtifact.
        :type version: str

        """
        self.swagger_types = {
            'deploy_artifact_id': 'str',
            'output_artifact_name': 'str',
            'artifact_type': 'str',
            'artifact_repository_id': 'str',
            'delivered_artifact_id': 'str',
            'path': 'str',
            'version': 'str'
        }
        self.attribute_map = {
            'deploy_artifact_id': 'deployArtifactId',
            'output_artifact_name': 'outputArtifactName',
            'artifact_type': 'artifactType',
            'artifact_repository_id': 'artifactRepositoryId',
            'delivered_artifact_id': 'deliveredArtifactId',
            'path': 'path',
            'version': 'version'
        }
        self._deploy_artifact_id = None
        self._output_artifact_name = None
        self._artifact_type = None
        self._artifact_repository_id = None
        self._delivered_artifact_id = None
        self._path = None
        self._version = None
        self._artifact_type = 'GENERIC_ARTIFACT'

    @property
    def artifact_repository_id(self):
        """
        Gets the artifact_repository_id of this GenericDeliveredArtifact.
        The OCID of the artifact registry repository used by the DeliverArtifactStage


        :return: The artifact_repository_id of this GenericDeliveredArtifact.
        :rtype: str
        """
        return self._artifact_repository_id

    @artifact_repository_id.setter
    def artifact_repository_id(self, artifact_repository_id):
        """
        Sets the artifact_repository_id of this GenericDeliveredArtifact.
        The OCID of the artifact registry repository used by the DeliverArtifactStage


        :param artifact_repository_id: The artifact_repository_id of this GenericDeliveredArtifact.
        :type: str
        """
        self._artifact_repository_id = artifact_repository_id

    @property
    def delivered_artifact_id(self):
        """
        **[Required]** Gets the delivered_artifact_id of this GenericDeliveredArtifact.
        The OCID of the artifact pushed by the Deliver Artifacts stage.


        :return: The delivered_artifact_id of this GenericDeliveredArtifact.
        :rtype: str
        """
        return self._delivered_artifact_id

    @delivered_artifact_id.setter
    def delivered_artifact_id(self, delivered_artifact_id):
        """
        Sets the delivered_artifact_id of this GenericDeliveredArtifact.
        The OCID of the artifact pushed by the Deliver Artifacts stage.


        :param delivered_artifact_id: The delivered_artifact_id of this GenericDeliveredArtifact.
        :type: str
        """
        self._delivered_artifact_id = delivered_artifact_id

    @property
    def path(self):
        """
        Gets the path of this GenericDeliveredArtifact.
        Path of the repository where artifact was pushed


        :return: The path of this GenericDeliveredArtifact.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this GenericDeliveredArtifact.
        Path of the repository where artifact was pushed


        :param path: The path of this GenericDeliveredArtifact.
        :type: str
        """
        self._path = path

    @property
    def version(self):
        """
        Gets the version of this GenericDeliveredArtifact.
        Version of the artifact pushed


        :return: The version of this GenericDeliveredArtifact.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this GenericDeliveredArtifact.
        Version of the artifact pushed


        :param version: The version of this GenericDeliveredArtifact.
        :type: str
        """
        self._version = version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
