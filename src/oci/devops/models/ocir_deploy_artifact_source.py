# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .deploy_artifact_source import DeployArtifactSource
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OcirDeployArtifactSource(DeployArtifactSource):
    """
    Specifies the OCIR details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OcirDeployArtifactSource object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.OcirDeployArtifactSource.deploy_artifact_source_type` attribute
        of this class is ``OCIR`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param deploy_artifact_source_type:
            The value to assign to the deploy_artifact_source_type property of this OcirDeployArtifactSource.
            Allowed values for this property are: "INLINE", "OCIR", "GENERIC_ARTIFACT", "HELM_CHART"
        :type deploy_artifact_source_type: str

        :param image_uri:
            The value to assign to the image_uri property of this OcirDeployArtifactSource.
        :type image_uri: str

        :param image_digest:
            The value to assign to the image_digest property of this OcirDeployArtifactSource.
        :type image_digest: str

        """
        self.swagger_types = {
            'deploy_artifact_source_type': 'str',
            'image_uri': 'str',
            'image_digest': 'str'
        }

        self.attribute_map = {
            'deploy_artifact_source_type': 'deployArtifactSourceType',
            'image_uri': 'imageUri',
            'image_digest': 'imageDigest'
        }

        self._deploy_artifact_source_type = None
        self._image_uri = None
        self._image_digest = None
        self._deploy_artifact_source_type = 'OCIR'

    @property
    def image_uri(self):
        """
        **[Required]** Gets the image_uri of this OcirDeployArtifactSource.
        Specifies OCIR image path - optionally include tag.


        :return: The image_uri of this OcirDeployArtifactSource.
        :rtype: str
        """
        return self._image_uri

    @image_uri.setter
    def image_uri(self, image_uri):
        """
        Sets the image_uri of this OcirDeployArtifactSource.
        Specifies OCIR image path - optionally include tag.


        :param image_uri: The image_uri of this OcirDeployArtifactSource.
        :type: str
        """
        self._image_uri = image_uri

    @property
    def image_digest(self):
        """
        Gets the image_digest of this OcirDeployArtifactSource.
        Specifies image digest for the version of the image.


        :return: The image_digest of this OcirDeployArtifactSource.
        :rtype: str
        """
        return self._image_digest

    @image_digest.setter
    def image_digest(self, image_digest):
        """
        Sets the image_digest of this OcirDeployArtifactSource.
        Specifies image digest for the version of the image.


        :param image_digest: The image_digest of this OcirDeployArtifactSource.
        :type: str
        """
        self._image_digest = image_digest

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
