# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20211101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateMediaWorkflowDetails(object):
    """
    The information about new MediaWorkflow.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateMediaWorkflowDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateMediaWorkflowDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateMediaWorkflowDetails.
        :type compartment_id: str

        :param tasks:
            The value to assign to the tasks property of this CreateMediaWorkflowDetails.
        :type tasks: list[oci.media_services.models.MediaWorkflowTask]

        :param media_workflow_configuration_ids:
            The value to assign to the media_workflow_configuration_ids property of this CreateMediaWorkflowDetails.
        :type media_workflow_configuration_ids: list[str]

        :param parameters:
            The value to assign to the parameters property of this CreateMediaWorkflowDetails.
        :type parameters: dict(str, object)

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateMediaWorkflowDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateMediaWorkflowDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'tasks': 'list[MediaWorkflowTask]',
            'media_workflow_configuration_ids': 'list[str]',
            'parameters': 'dict(str, object)',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'tasks': 'tasks',
            'media_workflow_configuration_ids': 'mediaWorkflowConfigurationIds',
            'parameters': 'parameters',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._compartment_id = None
        self._tasks = None
        self._media_workflow_configuration_ids = None
        self._parameters = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateMediaWorkflowDetails.
        Name for the MediaWorkflow. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this CreateMediaWorkflowDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateMediaWorkflowDetails.
        Name for the MediaWorkflow. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this CreateMediaWorkflowDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateMediaWorkflowDetails.
        Compartment Identifier.


        :return: The compartment_id of this CreateMediaWorkflowDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateMediaWorkflowDetails.
        Compartment Identifier.


        :param compartment_id: The compartment_id of this CreateMediaWorkflowDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def tasks(self):
        """
        Gets the tasks of this CreateMediaWorkflowDetails.
        The processing to be done in this workflow. Each key of the MediaWorkflowTasks in this array must be unique
        within the array. The order of tasks given here will be preserved.


        :return: The tasks of this CreateMediaWorkflowDetails.
        :rtype: list[oci.media_services.models.MediaWorkflowTask]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """
        Sets the tasks of this CreateMediaWorkflowDetails.
        The processing to be done in this workflow. Each key of the MediaWorkflowTasks in this array must be unique
        within the array. The order of tasks given here will be preserved.


        :param tasks: The tasks of this CreateMediaWorkflowDetails.
        :type: list[oci.media_services.models.MediaWorkflowTask]
        """
        self._tasks = tasks

    @property
    def media_workflow_configuration_ids(self):
        """
        Gets the media_workflow_configuration_ids of this CreateMediaWorkflowDetails.
        Configurations to be applied to all the jobs for this workflow. Parameters in these configurations are
        overridden by parameters in the MediaWorkflowConfigurations of the MediaWorkflowJob and the
        parameters of the MediaWorkflowJob.


        :return: The media_workflow_configuration_ids of this CreateMediaWorkflowDetails.
        :rtype: list[str]
        """
        return self._media_workflow_configuration_ids

    @media_workflow_configuration_ids.setter
    def media_workflow_configuration_ids(self, media_workflow_configuration_ids):
        """
        Sets the media_workflow_configuration_ids of this CreateMediaWorkflowDetails.
        Configurations to be applied to all the jobs for this workflow. Parameters in these configurations are
        overridden by parameters in the MediaWorkflowConfigurations of the MediaWorkflowJob and the
        parameters of the MediaWorkflowJob.


        :param media_workflow_configuration_ids: The media_workflow_configuration_ids of this CreateMediaWorkflowDetails.
        :type: list[str]
        """
        self._media_workflow_configuration_ids = media_workflow_configuration_ids

    @property
    def parameters(self):
        """
        Gets the parameters of this CreateMediaWorkflowDetails.
        JSON object representing named parameters and their default values that can be referenced throughout this workflow.
        The values declared here can be overridden by the MediaWorkflowConfigurations or parameters supplied when creating
        MediaWorkflowJobs from this MediaWorkflow.


        :return: The parameters of this CreateMediaWorkflowDetails.
        :rtype: dict(str, object)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this CreateMediaWorkflowDetails.
        JSON object representing named parameters and their default values that can be referenced throughout this workflow.
        The values declared here can be overridden by the MediaWorkflowConfigurations or parameters supplied when creating
        MediaWorkflowJobs from this MediaWorkflow.


        :param parameters: The parameters of this CreateMediaWorkflowDetails.
        :type: dict(str, object)
        """
        self._parameters = parameters

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateMediaWorkflowDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateMediaWorkflowDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateMediaWorkflowDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateMediaWorkflowDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateMediaWorkflowDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateMediaWorkflowDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateMediaWorkflowDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateMediaWorkflowDetails.
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
