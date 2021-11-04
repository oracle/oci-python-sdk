# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateBuildPipelineStageDetails(object):
    """
    The information to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateBuildPipelineStageDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.devops.models.UpdateWaitStageDetails`
        * :class:`~oci.devops.models.UpdateBuildStageDetails`
        * :class:`~oci.devops.models.UpdateTriggerDeploymentStageDetails`
        * :class:`~oci.devops.models.UpdateDeliverArtifactStageDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateBuildPipelineStageDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateBuildPipelineStageDetails.
        :type description: str

        :param build_pipeline_stage_type:
            The value to assign to the build_pipeline_stage_type property of this UpdateBuildPipelineStageDetails.
        :type build_pipeline_stage_type: str

        :param build_pipeline_stage_predecessor_collection:
            The value to assign to the build_pipeline_stage_predecessor_collection property of this UpdateBuildPipelineStageDetails.
        :type build_pipeline_stage_predecessor_collection: oci.devops.models.BuildPipelineStagePredecessorCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateBuildPipelineStageDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateBuildPipelineStageDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'build_pipeline_stage_type': 'str',
            'build_pipeline_stage_predecessor_collection': 'BuildPipelineStagePredecessorCollection',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'build_pipeline_stage_type': 'buildPipelineStageType',
            'build_pipeline_stage_predecessor_collection': 'buildPipelineStagePredecessorCollection',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._build_pipeline_stage_type = None
        self._build_pipeline_stage_predecessor_collection = None
        self._freeform_tags = None
        self._defined_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['buildPipelineStageType']

        if type == 'WAIT':
            return 'UpdateWaitStageDetails'

        if type == 'BUILD':
            return 'UpdateBuildStageDetails'

        if type == 'TRIGGER_DEPLOYMENT_PIPELINE':
            return 'UpdateTriggerDeploymentStageDetails'

        if type == 'DELIVER_ARTIFACT':
            return 'UpdateDeliverArtifactStageDetails'
        else:
            return 'UpdateBuildPipelineStageDetails'

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateBuildPipelineStageDetails.
        Stage identifier which can be renamed and is not necessarily unique


        :return: The display_name of this UpdateBuildPipelineStageDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateBuildPipelineStageDetails.
        Stage identifier which can be renamed and is not necessarily unique


        :param display_name: The display_name of this UpdateBuildPipelineStageDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateBuildPipelineStageDetails.
        Optional description about the BuildStage


        :return: The description of this UpdateBuildPipelineStageDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateBuildPipelineStageDetails.
        Optional description about the BuildStage


        :param description: The description of this UpdateBuildPipelineStageDetails.
        :type: str
        """
        self._description = description

    @property
    def build_pipeline_stage_type(self):
        """
        **[Required]** Gets the build_pipeline_stage_type of this UpdateBuildPipelineStageDetails.
        Stage sub types.


        :return: The build_pipeline_stage_type of this UpdateBuildPipelineStageDetails.
        :rtype: str
        """
        return self._build_pipeline_stage_type

    @build_pipeline_stage_type.setter
    def build_pipeline_stage_type(self, build_pipeline_stage_type):
        """
        Sets the build_pipeline_stage_type of this UpdateBuildPipelineStageDetails.
        Stage sub types.


        :param build_pipeline_stage_type: The build_pipeline_stage_type of this UpdateBuildPipelineStageDetails.
        :type: str
        """
        self._build_pipeline_stage_type = build_pipeline_stage_type

    @property
    def build_pipeline_stage_predecessor_collection(self):
        """
        Gets the build_pipeline_stage_predecessor_collection of this UpdateBuildPipelineStageDetails.

        :return: The build_pipeline_stage_predecessor_collection of this UpdateBuildPipelineStageDetails.
        :rtype: oci.devops.models.BuildPipelineStagePredecessorCollection
        """
        return self._build_pipeline_stage_predecessor_collection

    @build_pipeline_stage_predecessor_collection.setter
    def build_pipeline_stage_predecessor_collection(self, build_pipeline_stage_predecessor_collection):
        """
        Sets the build_pipeline_stage_predecessor_collection of this UpdateBuildPipelineStageDetails.

        :param build_pipeline_stage_predecessor_collection: The build_pipeline_stage_predecessor_collection of this UpdateBuildPipelineStageDetails.
        :type: oci.devops.models.BuildPipelineStagePredecessorCollection
        """
        self._build_pipeline_stage_predecessor_collection = build_pipeline_stage_predecessor_collection

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateBuildPipelineStageDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateBuildPipelineStageDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateBuildPipelineStageDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateBuildPipelineStageDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateBuildPipelineStageDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateBuildPipelineStageDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateBuildPipelineStageDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateBuildPipelineStageDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other