# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeployPipelineArtifact(object):
    """
    Artifact used in the pipeline.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DeployPipelineArtifact object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param deploy_artifact_id:
            The value to assign to the deploy_artifact_id property of this DeployPipelineArtifact.
        :type deploy_artifact_id: str

        :param display_name:
            The value to assign to the display_name property of this DeployPipelineArtifact.
        :type display_name: str

        :param deploy_pipeline_stages:
            The value to assign to the deploy_pipeline_stages property of this DeployPipelineArtifact.
        :type deploy_pipeline_stages: oci.devops.models.DeployPipelineStageCollection

        """
        self.swagger_types = {
            'deploy_artifact_id': 'str',
            'display_name': 'str',
            'deploy_pipeline_stages': 'DeployPipelineStageCollection'
        }

        self.attribute_map = {
            'deploy_artifact_id': 'deployArtifactId',
            'display_name': 'displayName',
            'deploy_pipeline_stages': 'deployPipelineStages'
        }

        self._deploy_artifact_id = None
        self._display_name = None
        self._deploy_pipeline_stages = None

    @property
    def deploy_artifact_id(self):
        """
        **[Required]** Gets the deploy_artifact_id of this DeployPipelineArtifact.
        The OCID of an artifact


        :return: The deploy_artifact_id of this DeployPipelineArtifact.
        :rtype: str
        """
        return self._deploy_artifact_id

    @deploy_artifact_id.setter
    def deploy_artifact_id(self, deploy_artifact_id):
        """
        Sets the deploy_artifact_id of this DeployPipelineArtifact.
        The OCID of an artifact


        :param deploy_artifact_id: The deploy_artifact_id of this DeployPipelineArtifact.
        :type: str
        """
        self._deploy_artifact_id = deploy_artifact_id

    @property
    def display_name(self):
        """
        Gets the display_name of this DeployPipelineArtifact.
        Display name of the artifact. Avoid entering confidential information.


        :return: The display_name of this DeployPipelineArtifact.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DeployPipelineArtifact.
        Display name of the artifact. Avoid entering confidential information.


        :param display_name: The display_name of this DeployPipelineArtifact.
        :type: str
        """
        self._display_name = display_name

    @property
    def deploy_pipeline_stages(self):
        """
        **[Required]** Gets the deploy_pipeline_stages of this DeployPipelineArtifact.

        :return: The deploy_pipeline_stages of this DeployPipelineArtifact.
        :rtype: oci.devops.models.DeployPipelineStageCollection
        """
        return self._deploy_pipeline_stages

    @deploy_pipeline_stages.setter
    def deploy_pipeline_stages(self, deploy_pipeline_stages):
        """
        Sets the deploy_pipeline_stages of this DeployPipelineArtifact.

        :param deploy_pipeline_stages: The deploy_pipeline_stages of this DeployPipelineArtifact.
        :type: oci.devops.models.DeployPipelineStageCollection
        """
        self._deploy_pipeline_stages = deploy_pipeline_stages

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
