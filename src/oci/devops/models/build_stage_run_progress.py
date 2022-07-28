# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .build_pipeline_stage_run_progress import BuildPipelineStageRunProgress
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BuildStageRunProgress(BuildPipelineStageRunProgress):
    """
    Specifies the run details for Build stage.
    """

    #: A constant which can be used with the image property of a BuildStageRunProgress.
    #: This constant has a value of "OL7_X86_64_STANDARD_10"
    IMAGE_OL7_X86_64_STANDARD_10 = "OL7_X86_64_STANDARD_10"

    def __init__(self, **kwargs):
        """
        Initializes a new BuildStageRunProgress object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.BuildStageRunProgress.build_pipeline_stage_type` attribute
        of this class is ``BUILD`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param stage_display_name:
            The value to assign to the stage_display_name property of this BuildStageRunProgress.
        :type stage_display_name: str

        :param build_pipeline_stage_type:
            The value to assign to the build_pipeline_stage_type property of this BuildStageRunProgress.
        :type build_pipeline_stage_type: str

        :param build_pipeline_stage_id:
            The value to assign to the build_pipeline_stage_id property of this BuildStageRunProgress.
        :type build_pipeline_stage_id: str

        :param time_started:
            The value to assign to the time_started property of this BuildStageRunProgress.
        :type time_started: datetime

        :param time_finished:
            The value to assign to the time_finished property of this BuildStageRunProgress.
        :type time_finished: datetime

        :param status:
            The value to assign to the status property of this BuildStageRunProgress.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param build_pipeline_stage_predecessors:
            The value to assign to the build_pipeline_stage_predecessors property of this BuildStageRunProgress.
        :type build_pipeline_stage_predecessors: oci.devops.models.BuildPipelineStagePredecessorCollection

        :param actual_build_runner_shape:
            The value to assign to the actual_build_runner_shape property of this BuildStageRunProgress.
        :type actual_build_runner_shape: str

        :param actual_build_runner_shape_config:
            The value to assign to the actual_build_runner_shape_config property of this BuildStageRunProgress.
        :type actual_build_runner_shape_config: oci.devops.models.ActualBuildRunnerShapeConfig

        :param image:
            The value to assign to the image property of this BuildStageRunProgress.
            Allowed values for this property are: "OL7_X86_64_STANDARD_10", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type image: str

        :param build_spec_file:
            The value to assign to the build_spec_file property of this BuildStageRunProgress.
        :type build_spec_file: str

        :param stage_execution_timeout_in_seconds:
            The value to assign to the stage_execution_timeout_in_seconds property of this BuildStageRunProgress.
        :type stage_execution_timeout_in_seconds: int

        :param build_source_collection:
            The value to assign to the build_source_collection property of this BuildStageRunProgress.
        :type build_source_collection: oci.devops.models.BuildSourceCollection

        :param primary_build_source:
            The value to assign to the primary_build_source property of this BuildStageRunProgress.
        :type primary_build_source: str

        :param steps:
            The value to assign to the steps property of this BuildStageRunProgress.
        :type steps: list[oci.devops.models.BuildStageRunStep]

        :param exported_variables:
            The value to assign to the exported_variables property of this BuildStageRunProgress.
        :type exported_variables: oci.devops.models.ExportedVariableCollection

        :param private_access_config:
            The value to assign to the private_access_config property of this BuildStageRunProgress.
        :type private_access_config: oci.devops.models.NetworkChannel

        """
        self.swagger_types = {
            'stage_display_name': 'str',
            'build_pipeline_stage_type': 'str',
            'build_pipeline_stage_id': 'str',
            'time_started': 'datetime',
            'time_finished': 'datetime',
            'status': 'str',
            'build_pipeline_stage_predecessors': 'BuildPipelineStagePredecessorCollection',
            'actual_build_runner_shape': 'str',
            'actual_build_runner_shape_config': 'ActualBuildRunnerShapeConfig',
            'image': 'str',
            'build_spec_file': 'str',
            'stage_execution_timeout_in_seconds': 'int',
            'build_source_collection': 'BuildSourceCollection',
            'primary_build_source': 'str',
            'steps': 'list[BuildStageRunStep]',
            'exported_variables': 'ExportedVariableCollection',
            'private_access_config': 'NetworkChannel'
        }

        self.attribute_map = {
            'stage_display_name': 'stageDisplayName',
            'build_pipeline_stage_type': 'buildPipelineStageType',
            'build_pipeline_stage_id': 'buildPipelineStageId',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished',
            'status': 'status',
            'build_pipeline_stage_predecessors': 'buildPipelineStagePredecessors',
            'actual_build_runner_shape': 'actualBuildRunnerShape',
            'actual_build_runner_shape_config': 'actualBuildRunnerShapeConfig',
            'image': 'image',
            'build_spec_file': 'buildSpecFile',
            'stage_execution_timeout_in_seconds': 'stageExecutionTimeoutInSeconds',
            'build_source_collection': 'buildSourceCollection',
            'primary_build_source': 'primaryBuildSource',
            'steps': 'steps',
            'exported_variables': 'exportedVariables',
            'private_access_config': 'privateAccessConfig'
        }

        self._stage_display_name = None
        self._build_pipeline_stage_type = None
        self._build_pipeline_stage_id = None
        self._time_started = None
        self._time_finished = None
        self._status = None
        self._build_pipeline_stage_predecessors = None
        self._actual_build_runner_shape = None
        self._actual_build_runner_shape_config = None
        self._image = None
        self._build_spec_file = None
        self._stage_execution_timeout_in_seconds = None
        self._build_source_collection = None
        self._primary_build_source = None
        self._steps = None
        self._exported_variables = None
        self._private_access_config = None
        self._build_pipeline_stage_type = 'BUILD'

    @property
    def actual_build_runner_shape(self):
        """
        Gets the actual_build_runner_shape of this BuildStageRunProgress.
        Name of Build Runner shape where this Build Stage is running.


        :return: The actual_build_runner_shape of this BuildStageRunProgress.
        :rtype: str
        """
        return self._actual_build_runner_shape

    @actual_build_runner_shape.setter
    def actual_build_runner_shape(self, actual_build_runner_shape):
        """
        Sets the actual_build_runner_shape of this BuildStageRunProgress.
        Name of Build Runner shape where this Build Stage is running.


        :param actual_build_runner_shape: The actual_build_runner_shape of this BuildStageRunProgress.
        :type: str
        """
        self._actual_build_runner_shape = actual_build_runner_shape

    @property
    def actual_build_runner_shape_config(self):
        """
        Gets the actual_build_runner_shape_config of this BuildStageRunProgress.

        :return: The actual_build_runner_shape_config of this BuildStageRunProgress.
        :rtype: oci.devops.models.ActualBuildRunnerShapeConfig
        """
        return self._actual_build_runner_shape_config

    @actual_build_runner_shape_config.setter
    def actual_build_runner_shape_config(self, actual_build_runner_shape_config):
        """
        Sets the actual_build_runner_shape_config of this BuildStageRunProgress.

        :param actual_build_runner_shape_config: The actual_build_runner_shape_config of this BuildStageRunProgress.
        :type: oci.devops.models.ActualBuildRunnerShapeConfig
        """
        self._actual_build_runner_shape_config = actual_build_runner_shape_config

    @property
    def image(self):
        """
        **[Required]** Gets the image of this BuildStageRunProgress.
        Image name for the Build Environment

        Allowed values for this property are: "OL7_X86_64_STANDARD_10", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The image of this BuildStageRunProgress.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this BuildStageRunProgress.
        Image name for the Build Environment


        :param image: The image of this BuildStageRunProgress.
        :type: str
        """
        allowed_values = ["OL7_X86_64_STANDARD_10"]
        if not value_allowed_none_or_none_sentinel(image, allowed_values):
            image = 'UNKNOWN_ENUM_VALUE'
        self._image = image

    @property
    def build_spec_file(self):
        """
        Gets the build_spec_file of this BuildStageRunProgress.
        The path to the build specification file for this Environment. The default location if not specified is build_spec.yaml


        :return: The build_spec_file of this BuildStageRunProgress.
        :rtype: str
        """
        return self._build_spec_file

    @build_spec_file.setter
    def build_spec_file(self, build_spec_file):
        """
        Sets the build_spec_file of this BuildStageRunProgress.
        The path to the build specification file for this Environment. The default location if not specified is build_spec.yaml


        :param build_spec_file: The build_spec_file of this BuildStageRunProgress.
        :type: str
        """
        self._build_spec_file = build_spec_file

    @property
    def stage_execution_timeout_in_seconds(self):
        """
        Gets the stage_execution_timeout_in_seconds of this BuildStageRunProgress.
        Timeout for the Build Stage Execution. Value in seconds.


        :return: The stage_execution_timeout_in_seconds of this BuildStageRunProgress.
        :rtype: int
        """
        return self._stage_execution_timeout_in_seconds

    @stage_execution_timeout_in_seconds.setter
    def stage_execution_timeout_in_seconds(self, stage_execution_timeout_in_seconds):
        """
        Sets the stage_execution_timeout_in_seconds of this BuildStageRunProgress.
        Timeout for the Build Stage Execution. Value in seconds.


        :param stage_execution_timeout_in_seconds: The stage_execution_timeout_in_seconds of this BuildStageRunProgress.
        :type: int
        """
        self._stage_execution_timeout_in_seconds = stage_execution_timeout_in_seconds

    @property
    def build_source_collection(self):
        """
        **[Required]** Gets the build_source_collection of this BuildStageRunProgress.

        :return: The build_source_collection of this BuildStageRunProgress.
        :rtype: oci.devops.models.BuildSourceCollection
        """
        return self._build_source_collection

    @build_source_collection.setter
    def build_source_collection(self, build_source_collection):
        """
        Sets the build_source_collection of this BuildStageRunProgress.

        :param build_source_collection: The build_source_collection of this BuildStageRunProgress.
        :type: oci.devops.models.BuildSourceCollection
        """
        self._build_source_collection = build_source_collection

    @property
    def primary_build_source(self):
        """
        Gets the primary_build_source of this BuildStageRunProgress.
        Name of the BuildSource in which the build_spec.yml file need to be located. If not specified, the 1st entry in the BuildSource collection will be chosen as Primary.


        :return: The primary_build_source of this BuildStageRunProgress.
        :rtype: str
        """
        return self._primary_build_source

    @primary_build_source.setter
    def primary_build_source(self, primary_build_source):
        """
        Sets the primary_build_source of this BuildStageRunProgress.
        Name of the BuildSource in which the build_spec.yml file need to be located. If not specified, the 1st entry in the BuildSource collection will be chosen as Primary.


        :param primary_build_source: The primary_build_source of this BuildStageRunProgress.
        :type: str
        """
        self._primary_build_source = primary_build_source

    @property
    def steps(self):
        """
        Gets the steps of this BuildStageRunProgress.
        The details about all the steps in a Build stage


        :return: The steps of this BuildStageRunProgress.
        :rtype: list[oci.devops.models.BuildStageRunStep]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """
        Sets the steps of this BuildStageRunProgress.
        The details about all the steps in a Build stage


        :param steps: The steps of this BuildStageRunProgress.
        :type: list[oci.devops.models.BuildStageRunStep]
        """
        self._steps = steps

    @property
    def exported_variables(self):
        """
        Gets the exported_variables of this BuildStageRunProgress.

        :return: The exported_variables of this BuildStageRunProgress.
        :rtype: oci.devops.models.ExportedVariableCollection
        """
        return self._exported_variables

    @exported_variables.setter
    def exported_variables(self, exported_variables):
        """
        Sets the exported_variables of this BuildStageRunProgress.

        :param exported_variables: The exported_variables of this BuildStageRunProgress.
        :type: oci.devops.models.ExportedVariableCollection
        """
        self._exported_variables = exported_variables

    @property
    def private_access_config(self):
        """
        Gets the private_access_config of this BuildStageRunProgress.

        :return: The private_access_config of this BuildStageRunProgress.
        :rtype: oci.devops.models.NetworkChannel
        """
        return self._private_access_config

    @private_access_config.setter
    def private_access_config(self, private_access_config):
        """
        Sets the private_access_config of this BuildStageRunProgress.

        :param private_access_config: The private_access_config of this BuildStageRunProgress.
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
