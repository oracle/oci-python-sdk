# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_build_pipeline_stage_details import CreateBuildPipelineStageDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateBuildStageDetails(CreateBuildPipelineStageDetails):
    """
    Specifies the build stage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateBuildStageDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.CreateBuildStageDetails.build_pipeline_stage_type` attribute
        of this class is ``BUILD`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateBuildStageDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateBuildStageDetails.
        :type description: str

        :param build_pipeline_stage_type:
            The value to assign to the build_pipeline_stage_type property of this CreateBuildStageDetails.
        :type build_pipeline_stage_type: str

        :param build_pipeline_id:
            The value to assign to the build_pipeline_id property of this CreateBuildStageDetails.
        :type build_pipeline_id: str

        :param build_pipeline_stage_predecessor_collection:
            The value to assign to the build_pipeline_stage_predecessor_collection property of this CreateBuildStageDetails.
        :type build_pipeline_stage_predecessor_collection: oci.devops.models.BuildPipelineStagePredecessorCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateBuildStageDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateBuildStageDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param image:
            The value to assign to the image property of this CreateBuildStageDetails.
        :type image: str

        :param build_spec_file:
            The value to assign to the build_spec_file property of this CreateBuildStageDetails.
        :type build_spec_file: str

        :param stage_execution_timeout_in_seconds:
            The value to assign to the stage_execution_timeout_in_seconds property of this CreateBuildStageDetails.
        :type stage_execution_timeout_in_seconds: int

        :param build_source_collection:
            The value to assign to the build_source_collection property of this CreateBuildStageDetails.
        :type build_source_collection: oci.devops.models.BuildSourceCollection

        :param primary_build_source:
            The value to assign to the primary_build_source property of this CreateBuildStageDetails.
        :type primary_build_source: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'build_pipeline_stage_type': 'str',
            'build_pipeline_id': 'str',
            'build_pipeline_stage_predecessor_collection': 'BuildPipelineStagePredecessorCollection',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'image': 'str',
            'build_spec_file': 'str',
            'stage_execution_timeout_in_seconds': 'int',
            'build_source_collection': 'BuildSourceCollection',
            'primary_build_source': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'build_pipeline_stage_type': 'buildPipelineStageType',
            'build_pipeline_id': 'buildPipelineId',
            'build_pipeline_stage_predecessor_collection': 'buildPipelineStagePredecessorCollection',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'image': 'image',
            'build_spec_file': 'buildSpecFile',
            'stage_execution_timeout_in_seconds': 'stageExecutionTimeoutInSeconds',
            'build_source_collection': 'buildSourceCollection',
            'primary_build_source': 'primaryBuildSource'
        }

        self._display_name = None
        self._description = None
        self._build_pipeline_stage_type = None
        self._build_pipeline_id = None
        self._build_pipeline_stage_predecessor_collection = None
        self._freeform_tags = None
        self._defined_tags = None
        self._image = None
        self._build_spec_file = None
        self._stage_execution_timeout_in_seconds = None
        self._build_source_collection = None
        self._primary_build_source = None
        self._build_pipeline_stage_type = 'BUILD'

    @property
    def image(self):
        """
        **[Required]** Gets the image of this CreateBuildStageDetails.
        Image name for the build environment


        :return: The image of this CreateBuildStageDetails.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this CreateBuildStageDetails.
        Image name for the build environment


        :param image: The image of this CreateBuildStageDetails.
        :type: str
        """
        self._image = image

    @property
    def build_spec_file(self):
        """
        Gets the build_spec_file of this CreateBuildStageDetails.
        The path to the build specification file for this environment. The default location of the file if not specified is build_spec.yaml.


        :return: The build_spec_file of this CreateBuildStageDetails.
        :rtype: str
        """
        return self._build_spec_file

    @build_spec_file.setter
    def build_spec_file(self, build_spec_file):
        """
        Sets the build_spec_file of this CreateBuildStageDetails.
        The path to the build specification file for this environment. The default location of the file if not specified is build_spec.yaml.


        :param build_spec_file: The build_spec_file of this CreateBuildStageDetails.
        :type: str
        """
        self._build_spec_file = build_spec_file

    @property
    def stage_execution_timeout_in_seconds(self):
        """
        Gets the stage_execution_timeout_in_seconds of this CreateBuildStageDetails.
        Timeout for the build stage execution. Specify value in seconds.


        :return: The stage_execution_timeout_in_seconds of this CreateBuildStageDetails.
        :rtype: int
        """
        return self._stage_execution_timeout_in_seconds

    @stage_execution_timeout_in_seconds.setter
    def stage_execution_timeout_in_seconds(self, stage_execution_timeout_in_seconds):
        """
        Sets the stage_execution_timeout_in_seconds of this CreateBuildStageDetails.
        Timeout for the build stage execution. Specify value in seconds.


        :param stage_execution_timeout_in_seconds: The stage_execution_timeout_in_seconds of this CreateBuildStageDetails.
        :type: int
        """
        self._stage_execution_timeout_in_seconds = stage_execution_timeout_in_seconds

    @property
    def build_source_collection(self):
        """
        **[Required]** Gets the build_source_collection of this CreateBuildStageDetails.

        :return: The build_source_collection of this CreateBuildStageDetails.
        :rtype: oci.devops.models.BuildSourceCollection
        """
        return self._build_source_collection

    @build_source_collection.setter
    def build_source_collection(self, build_source_collection):
        """
        Sets the build_source_collection of this CreateBuildStageDetails.

        :param build_source_collection: The build_source_collection of this CreateBuildStageDetails.
        :type: oci.devops.models.BuildSourceCollection
        """
        self._build_source_collection = build_source_collection

    @property
    def primary_build_source(self):
        """
        Gets the primary_build_source of this CreateBuildStageDetails.
        Name of the build source where the build_spec.yml file is located. If not specified, the first entry in the build source collection is chosen as primary build source.


        :return: The primary_build_source of this CreateBuildStageDetails.
        :rtype: str
        """
        return self._primary_build_source

    @primary_build_source.setter
    def primary_build_source(self, primary_build_source):
        """
        Sets the primary_build_source of this CreateBuildStageDetails.
        Name of the build source where the build_spec.yml file is located. If not specified, the first entry in the build source collection is chosen as primary build source.


        :param primary_build_source: The primary_build_source of this CreateBuildStageDetails.
        :type: str
        """
        self._primary_build_source = primary_build_source

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
