# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .build_pipeline_stage import BuildPipelineStage
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BuildStage(BuildPipelineStage):
    """
    Specifies the build stage.
    """

    #: A constant which can be used with the image property of a BuildStage.
    #: This constant has a value of "OL7_X86_64_STANDARD_10"
    IMAGE_OL7_X86_64_STANDARD_10 = "OL7_X86_64_STANDARD_10"

    def __init__(self, **kwargs):
        """
        Initializes a new BuildStage object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.BuildStage.build_pipeline_stage_type` attribute
        of this class is ``BUILD`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this BuildStage.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this BuildStage.
        :type display_name: str

        :param description:
            The value to assign to the description property of this BuildStage.
        :type description: str

        :param project_id:
            The value to assign to the project_id property of this BuildStage.
        :type project_id: str

        :param build_pipeline_id:
            The value to assign to the build_pipeline_id property of this BuildStage.
        :type build_pipeline_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this BuildStage.
        :type compartment_id: str

        :param build_pipeline_stage_type:
            The value to assign to the build_pipeline_stage_type property of this BuildStage.
            Allowed values for this property are: "WAIT", "BUILD", "DELIVER_ARTIFACT", "TRIGGER_DEPLOYMENT_PIPELINE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type build_pipeline_stage_type: str

        :param time_created:
            The value to assign to the time_created property of this BuildStage.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this BuildStage.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this BuildStage.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this BuildStage.
        :type lifecycle_details: str

        :param build_pipeline_stage_predecessor_collection:
            The value to assign to the build_pipeline_stage_predecessor_collection property of this BuildStage.
        :type build_pipeline_stage_predecessor_collection: oci.devops.models.BuildPipelineStagePredecessorCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this BuildStage.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this BuildStage.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this BuildStage.
        :type system_tags: dict(str, dict(str, object))

        :param image:
            The value to assign to the image property of this BuildStage.
            Allowed values for this property are: "OL7_X86_64_STANDARD_10", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type image: str

        :param build_spec_file:
            The value to assign to the build_spec_file property of this BuildStage.
        :type build_spec_file: str

        :param stage_execution_timeout_in_seconds:
            The value to assign to the stage_execution_timeout_in_seconds property of this BuildStage.
        :type stage_execution_timeout_in_seconds: int

        :param build_source_collection:
            The value to assign to the build_source_collection property of this BuildStage.
        :type build_source_collection: oci.devops.models.BuildSourceCollection

        :param primary_build_source:
            The value to assign to the primary_build_source property of this BuildStage.
        :type primary_build_source: str

        :param private_access_config:
            The value to assign to the private_access_config property of this BuildStage.
        :type private_access_config: oci.devops.models.NetworkChannel

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'project_id': 'str',
            'build_pipeline_id': 'str',
            'compartment_id': 'str',
            'build_pipeline_stage_type': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'build_pipeline_stage_predecessor_collection': 'BuildPipelineStagePredecessorCollection',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'image': 'str',
            'build_spec_file': 'str',
            'stage_execution_timeout_in_seconds': 'int',
            'build_source_collection': 'BuildSourceCollection',
            'primary_build_source': 'str',
            'private_access_config': 'NetworkChannel'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'project_id': 'projectId',
            'build_pipeline_id': 'buildPipelineId',
            'compartment_id': 'compartmentId',
            'build_pipeline_stage_type': 'buildPipelineStageType',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'build_pipeline_stage_predecessor_collection': 'buildPipelineStagePredecessorCollection',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'image': 'image',
            'build_spec_file': 'buildSpecFile',
            'stage_execution_timeout_in_seconds': 'stageExecutionTimeoutInSeconds',
            'build_source_collection': 'buildSourceCollection',
            'primary_build_source': 'primaryBuildSource',
            'private_access_config': 'privateAccessConfig'
        }

        self._id = None
        self._display_name = None
        self._description = None
        self._project_id = None
        self._build_pipeline_id = None
        self._compartment_id = None
        self._build_pipeline_stage_type = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._build_pipeline_stage_predecessor_collection = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._image = None
        self._build_spec_file = None
        self._stage_execution_timeout_in_seconds = None
        self._build_source_collection = None
        self._primary_build_source = None
        self._private_access_config = None
        self._build_pipeline_stage_type = 'BUILD'

    @property
    def image(self):
        """
        **[Required]** Gets the image of this BuildStage.
        Image name for the build environment.

        Allowed values for this property are: "OL7_X86_64_STANDARD_10", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The image of this BuildStage.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this BuildStage.
        Image name for the build environment.


        :param image: The image of this BuildStage.
        :type: str
        """
        allowed_values = ["OL7_X86_64_STANDARD_10"]
        if not value_allowed_none_or_none_sentinel(image, allowed_values):
            image = 'UNKNOWN_ENUM_VALUE'
        self._image = image

    @property
    def build_spec_file(self):
        """
        Gets the build_spec_file of this BuildStage.
        The path to the build specification file for this environment. The default location of the file if not specified is build_spec.yaml.


        :return: The build_spec_file of this BuildStage.
        :rtype: str
        """
        return self._build_spec_file

    @build_spec_file.setter
    def build_spec_file(self, build_spec_file):
        """
        Sets the build_spec_file of this BuildStage.
        The path to the build specification file for this environment. The default location of the file if not specified is build_spec.yaml.


        :param build_spec_file: The build_spec_file of this BuildStage.
        :type: str
        """
        self._build_spec_file = build_spec_file

    @property
    def stage_execution_timeout_in_seconds(self):
        """
        Gets the stage_execution_timeout_in_seconds of this BuildStage.
        Timeout for the build stage execution. Specify value in seconds.


        :return: The stage_execution_timeout_in_seconds of this BuildStage.
        :rtype: int
        """
        return self._stage_execution_timeout_in_seconds

    @stage_execution_timeout_in_seconds.setter
    def stage_execution_timeout_in_seconds(self, stage_execution_timeout_in_seconds):
        """
        Sets the stage_execution_timeout_in_seconds of this BuildStage.
        Timeout for the build stage execution. Specify value in seconds.


        :param stage_execution_timeout_in_seconds: The stage_execution_timeout_in_seconds of this BuildStage.
        :type: int
        """
        self._stage_execution_timeout_in_seconds = stage_execution_timeout_in_seconds

    @property
    def build_source_collection(self):
        """
        **[Required]** Gets the build_source_collection of this BuildStage.

        :return: The build_source_collection of this BuildStage.
        :rtype: oci.devops.models.BuildSourceCollection
        """
        return self._build_source_collection

    @build_source_collection.setter
    def build_source_collection(self, build_source_collection):
        """
        Sets the build_source_collection of this BuildStage.

        :param build_source_collection: The build_source_collection of this BuildStage.
        :type: oci.devops.models.BuildSourceCollection
        """
        self._build_source_collection = build_source_collection

    @property
    def primary_build_source(self):
        """
        Gets the primary_build_source of this BuildStage.
        Name of the build source where the build_spec.yml file is located. If not specified, then the first entry in the build source collection is chosen as primary build source.


        :return: The primary_build_source of this BuildStage.
        :rtype: str
        """
        return self._primary_build_source

    @primary_build_source.setter
    def primary_build_source(self, primary_build_source):
        """
        Sets the primary_build_source of this BuildStage.
        Name of the build source where the build_spec.yml file is located. If not specified, then the first entry in the build source collection is chosen as primary build source.


        :param primary_build_source: The primary_build_source of this BuildStage.
        :type: str
        """
        self._primary_build_source = primary_build_source

    @property
    def private_access_config(self):
        """
        Gets the private_access_config of this BuildStage.

        :return: The private_access_config of this BuildStage.
        :rtype: oci.devops.models.NetworkChannel
        """
        return self._private_access_config

    @private_access_config.setter
    def private_access_config(self, private_access_config):
        """
        Sets the private_access_config of this BuildStage.

        :param private_access_config: The private_access_config of this BuildStage.
        :type: oci.devops.models.NetworkChannel
        """
        self._private_access_config = private_access_config

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
