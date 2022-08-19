# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateMediaWorkflowConfigurationDetails(object):
    """
    The information needed to create a new MediaWorkflowConfiguration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateMediaWorkflowConfigurationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateMediaWorkflowConfigurationDetails.
        :type display_name: str

        :param parameters:
            The value to assign to the parameters property of this CreateMediaWorkflowConfigurationDetails.
        :type parameters: dict(str, object)

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateMediaWorkflowConfigurationDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateMediaWorkflowConfigurationDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateMediaWorkflowConfigurationDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'parameters': 'dict(str, object)',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'parameters': 'parameters',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._parameters = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateMediaWorkflowConfigurationDetails.
        MediaWorkflowConfiguration identifier. Avoid entering confidential information.


        :return: The display_name of this CreateMediaWorkflowConfigurationDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateMediaWorkflowConfigurationDetails.
        MediaWorkflowConfiguration identifier. Avoid entering confidential information.


        :param display_name: The display_name of this CreateMediaWorkflowConfigurationDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def parameters(self):
        """
        **[Required]** Gets the parameters of this CreateMediaWorkflowConfigurationDetails.
        Reuseable parameter values encoded as a JSON; the top and second level JSON elements are
        objects. Each key of the top level object refers to a task key that is unqiue to the
        workflow, each of the second level objects' keys refer to the name of a parameter that is
        unique to the task. taskKey -> parameterName -> parameterValue


        :return: The parameters of this CreateMediaWorkflowConfigurationDetails.
        :rtype: dict(str, object)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this CreateMediaWorkflowConfigurationDetails.
        Reuseable parameter values encoded as a JSON; the top and second level JSON elements are
        objects. Each key of the top level object refers to a task key that is unqiue to the
        workflow, each of the second level objects' keys refer to the name of a parameter that is
        unique to the task. taskKey -> parameterName -> parameterValue


        :param parameters: The parameters of this CreateMediaWorkflowConfigurationDetails.
        :type: dict(str, object)
        """
        self._parameters = parameters

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateMediaWorkflowConfigurationDetails.
        Compartment Identifier.


        :return: The compartment_id of this CreateMediaWorkflowConfigurationDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateMediaWorkflowConfigurationDetails.
        Compartment Identifier.


        :param compartment_id: The compartment_id of this CreateMediaWorkflowConfigurationDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateMediaWorkflowConfigurationDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateMediaWorkflowConfigurationDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateMediaWorkflowConfigurationDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateMediaWorkflowConfigurationDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateMediaWorkflowConfigurationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateMediaWorkflowConfigurationDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateMediaWorkflowConfigurationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateMediaWorkflowConfigurationDetails.
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
