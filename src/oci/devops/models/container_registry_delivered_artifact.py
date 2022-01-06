# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .delivered_artifact import DeliveredArtifact
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ContainerRegistryDeliveredArtifact(DeliveredArtifact):
    """
    Details of the container registry artifacts delivered through the Deliver Artifacts stage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ContainerRegistryDeliveredArtifact object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.ContainerRegistryDeliveredArtifact.artifact_type` attribute
        of this class is ``OCIR`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param deploy_artifact_id:
            The value to assign to the deploy_artifact_id property of this ContainerRegistryDeliveredArtifact.
        :type deploy_artifact_id: str

        :param output_artifact_name:
            The value to assign to the output_artifact_name property of this ContainerRegistryDeliveredArtifact.
        :type output_artifact_name: str

        :param artifact_type:
            The value to assign to the artifact_type property of this ContainerRegistryDeliveredArtifact.
            Allowed values for this property are: "GENERIC_ARTIFACT", "OCIR"
        :type artifact_type: str

        :param delivered_artifact_hash:
            The value to assign to the delivered_artifact_hash property of this ContainerRegistryDeliveredArtifact.
        :type delivered_artifact_hash: str

        :param image_uri:
            The value to assign to the image_uri property of this ContainerRegistryDeliveredArtifact.
        :type image_uri: str

        """
        self.swagger_types = {
            'deploy_artifact_id': 'str',
            'output_artifact_name': 'str',
            'artifact_type': 'str',
            'delivered_artifact_hash': 'str',
            'image_uri': 'str'
        }

        self.attribute_map = {
            'deploy_artifact_id': 'deployArtifactId',
            'output_artifact_name': 'outputArtifactName',
            'artifact_type': 'artifactType',
            'delivered_artifact_hash': 'deliveredArtifactHash',
            'image_uri': 'imageUri'
        }

        self._deploy_artifact_id = None
        self._output_artifact_name = None
        self._artifact_type = None
        self._delivered_artifact_hash = None
        self._image_uri = None
        self._artifact_type = 'OCIR'

    @property
    def delivered_artifact_hash(self):
        """
        **[Required]** Gets the delivered_artifact_hash of this ContainerRegistryDeliveredArtifact.
        The hash of the container registry artifact pushed by the Deliver Artifacts stage.


        :return: The delivered_artifact_hash of this ContainerRegistryDeliveredArtifact.
        :rtype: str
        """
        return self._delivered_artifact_hash

    @delivered_artifact_hash.setter
    def delivered_artifact_hash(self, delivered_artifact_hash):
        """
        Sets the delivered_artifact_hash of this ContainerRegistryDeliveredArtifact.
        The hash of the container registry artifact pushed by the Deliver Artifacts stage.


        :param delivered_artifact_hash: The delivered_artifact_hash of this ContainerRegistryDeliveredArtifact.
        :type: str
        """
        self._delivered_artifact_hash = delivered_artifact_hash

    @property
    def image_uri(self):
        """
        Gets the image_uri of this ContainerRegistryDeliveredArtifact.
        The imageUri of the OCIR artifact pushed by the DeliverArtifactStage


        :return: The image_uri of this ContainerRegistryDeliveredArtifact.
        :rtype: str
        """
        return self._image_uri

    @image_uri.setter
    def image_uri(self, image_uri):
        """
        Sets the image_uri of this ContainerRegistryDeliveredArtifact.
        The imageUri of the OCIR artifact pushed by the DeliverArtifactStage


        :param image_uri: The image_uri of this ContainerRegistryDeliveredArtifact.
        :type: str
        """
        self._image_uri = image_uri

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
