# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateBuildPipelineDetails(object):
    """
    Information about the new build pipeline to be created.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateBuildPipelineDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this CreateBuildPipelineDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this CreateBuildPipelineDetails.
        :type display_name: str

        :param project_id:
            The value to assign to the project_id property of this CreateBuildPipelineDetails.
        :type project_id: str

        :param build_pipeline_parameters:
            The value to assign to the build_pipeline_parameters property of this CreateBuildPipelineDetails.
        :type build_pipeline_parameters: oci.devops.models.BuildPipelineParameterCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateBuildPipelineDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateBuildPipelineDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'description': 'str',
            'display_name': 'str',
            'project_id': 'str',
            'build_pipeline_parameters': 'BuildPipelineParameterCollection',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'description': 'description',
            'display_name': 'displayName',
            'project_id': 'projectId',
            'build_pipeline_parameters': 'buildPipelineParameters',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._description = None
        self._display_name = None
        self._project_id = None
        self._build_pipeline_parameters = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def description(self):
        """
        Gets the description of this CreateBuildPipelineDetails.
        Optional description about the build pipeline.


        :return: The description of this CreateBuildPipelineDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateBuildPipelineDetails.
        Optional description about the build pipeline.


        :param description: The description of this CreateBuildPipelineDetails.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateBuildPipelineDetails.
        Build pipeline display name. Avoid entering confidential information.


        :return: The display_name of this CreateBuildPipelineDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateBuildPipelineDetails.
        Build pipeline display name. Avoid entering confidential information.


        :param display_name: The display_name of this CreateBuildPipelineDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def project_id(self):
        """
        **[Required]** Gets the project_id of this CreateBuildPipelineDetails.
        The OCID of the DevOps project.


        :return: The project_id of this CreateBuildPipelineDetails.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this CreateBuildPipelineDetails.
        The OCID of the DevOps project.


        :param project_id: The project_id of this CreateBuildPipelineDetails.
        :type: str
        """
        self._project_id = project_id

    @property
    def build_pipeline_parameters(self):
        """
        Gets the build_pipeline_parameters of this CreateBuildPipelineDetails.

        :return: The build_pipeline_parameters of this CreateBuildPipelineDetails.
        :rtype: oci.devops.models.BuildPipelineParameterCollection
        """
        return self._build_pipeline_parameters

    @build_pipeline_parameters.setter
    def build_pipeline_parameters(self, build_pipeline_parameters):
        """
        Sets the build_pipeline_parameters of this CreateBuildPipelineDetails.

        :param build_pipeline_parameters: The build_pipeline_parameters of this CreateBuildPipelineDetails.
        :type: oci.devops.models.BuildPipelineParameterCollection
        """
        self._build_pipeline_parameters = build_pipeline_parameters

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateBuildPipelineDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateBuildPipelineDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateBuildPipelineDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateBuildPipelineDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateBuildPipelineDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateBuildPipelineDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateBuildPipelineDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateBuildPipelineDetails.
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
