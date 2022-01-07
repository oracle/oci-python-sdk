# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_build_pipeline_stage_details import CreateBuildPipelineStageDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDeliverArtifactStageDetails(CreateBuildPipelineStageDetails):
    """
    Specifies the Deliver Artifacts stage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDeliverArtifactStageDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.CreateDeliverArtifactStageDetails.build_pipeline_stage_type` attribute
        of this class is ``DELIVER_ARTIFACT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateDeliverArtifactStageDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateDeliverArtifactStageDetails.
        :type description: str

        :param build_pipeline_stage_type:
            The value to assign to the build_pipeline_stage_type property of this CreateDeliverArtifactStageDetails.
        :type build_pipeline_stage_type: str

        :param build_pipeline_id:
            The value to assign to the build_pipeline_id property of this CreateDeliverArtifactStageDetails.
        :type build_pipeline_id: str

        :param build_pipeline_stage_predecessor_collection:
            The value to assign to the build_pipeline_stage_predecessor_collection property of this CreateDeliverArtifactStageDetails.
        :type build_pipeline_stage_predecessor_collection: oci.devops.models.BuildPipelineStagePredecessorCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDeliverArtifactStageDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDeliverArtifactStageDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param deliver_artifact_collection:
            The value to assign to the deliver_artifact_collection property of this CreateDeliverArtifactStageDetails.
        :type deliver_artifact_collection: oci.devops.models.DeliverArtifactCollection

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'build_pipeline_stage_type': 'str',
            'build_pipeline_id': 'str',
            'build_pipeline_stage_predecessor_collection': 'BuildPipelineStagePredecessorCollection',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'deliver_artifact_collection': 'DeliverArtifactCollection'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'build_pipeline_stage_type': 'buildPipelineStageType',
            'build_pipeline_id': 'buildPipelineId',
            'build_pipeline_stage_predecessor_collection': 'buildPipelineStagePredecessorCollection',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'deliver_artifact_collection': 'deliverArtifactCollection'
        }

        self._display_name = None
        self._description = None
        self._build_pipeline_stage_type = None
        self._build_pipeline_id = None
        self._build_pipeline_stage_predecessor_collection = None
        self._freeform_tags = None
        self._defined_tags = None
        self._deliver_artifact_collection = None
        self._build_pipeline_stage_type = 'DELIVER_ARTIFACT'

    @property
    def deliver_artifact_collection(self):
        """
        **[Required]** Gets the deliver_artifact_collection of this CreateDeliverArtifactStageDetails.

        :return: The deliver_artifact_collection of this CreateDeliverArtifactStageDetails.
        :rtype: oci.devops.models.DeliverArtifactCollection
        """
        return self._deliver_artifact_collection

    @deliver_artifact_collection.setter
    def deliver_artifact_collection(self, deliver_artifact_collection):
        """
        Sets the deliver_artifact_collection of this CreateDeliverArtifactStageDetails.

        :param deliver_artifact_collection: The deliver_artifact_collection of this CreateDeliverArtifactStageDetails.
        :type: oci.devops.models.DeliverArtifactCollection
        """
        self._deliver_artifact_collection = deliver_artifact_collection

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
