# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .deploy_artifact_source import DeployArtifactSource
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InlineDeployArtifactSource(DeployArtifactSource):
    """
    Specifies the inline deployment artifact source details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InlineDeployArtifactSource object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.InlineDeployArtifactSource.deploy_artifact_source_type` attribute
        of this class is ``INLINE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param deploy_artifact_source_type:
            The value to assign to the deploy_artifact_source_type property of this InlineDeployArtifactSource.
            Allowed values for this property are: "INLINE", "OCIR", "GENERIC_ARTIFACT", "HELM_CHART"
        :type deploy_artifact_source_type: str

        :param base64_encoded_content:
            The value to assign to the base64_encoded_content property of this InlineDeployArtifactSource.
        :type base64_encoded_content: str

        """
        self.swagger_types = {
            'deploy_artifact_source_type': 'str',
            'base64_encoded_content': 'str'
        }

        self.attribute_map = {
            'deploy_artifact_source_type': 'deployArtifactSourceType',
            'base64_encoded_content': 'base64EncodedContent'
        }

        self._deploy_artifact_source_type = None
        self._base64_encoded_content = None
        self._deploy_artifact_source_type = 'INLINE'

    @property
    def base64_encoded_content(self):
        """
        **[Required]** Gets the base64_encoded_content of this InlineDeployArtifactSource.
        base64 Encoded String


        :return: The base64_encoded_content of this InlineDeployArtifactSource.
        :rtype: str
        """
        return self._base64_encoded_content

    @base64_encoded_content.setter
    def base64_encoded_content(self, base64_encoded_content):
        """
        Sets the base64_encoded_content of this InlineDeployArtifactSource.
        base64 Encoded String


        :param base64_encoded_content: The base64_encoded_content of this InlineDeployArtifactSource.
        :type: str
        """
        self._base64_encoded_content = base64_encoded_content

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
