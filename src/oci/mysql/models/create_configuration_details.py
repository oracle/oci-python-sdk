# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateConfigurationDetails(object):
    """
    The details required to create a new Configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateConfigurationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateConfigurationDetails.
        :type compartment_id: str

        :param description:
            The value to assign to the description property of this CreateConfigurationDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this CreateConfigurationDetails.
        :type display_name: str

        :param shape_name:
            The value to assign to the shape_name property of this CreateConfigurationDetails.
        :type shape_name: str

        :param variables:
            The value to assign to the variables property of this CreateConfigurationDetails.
        :type variables: oci.mysql.models.ConfigurationVariables

        :param parent_configuration_id:
            The value to assign to the parent_configuration_id property of this CreateConfigurationDetails.
        :type parent_configuration_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateConfigurationDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateConfigurationDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'description': 'str',
            'display_name': 'str',
            'shape_name': 'str',
            'variables': 'ConfigurationVariables',
            'parent_configuration_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'description': 'description',
            'display_name': 'displayName',
            'shape_name': 'shapeName',
            'variables': 'variables',
            'parent_configuration_id': 'parentConfigurationId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._description = None
        self._display_name = None
        self._shape_name = None
        self._variables = None
        self._parent_configuration_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateConfigurationDetails.
        The OCID of the compartment.


        :return: The compartment_id of this CreateConfigurationDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateConfigurationDetails.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this CreateConfigurationDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def description(self):
        """
        Gets the description of this CreateConfigurationDetails.
        User-provided data about the Configuration.


        :return: The description of this CreateConfigurationDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateConfigurationDetails.
        User-provided data about the Configuration.


        :param description: The description of this CreateConfigurationDetails.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateConfigurationDetails.
        The display name of the Configuration.


        :return: The display_name of this CreateConfigurationDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateConfigurationDetails.
        The display name of the Configuration.


        :param display_name: The display_name of this CreateConfigurationDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def shape_name(self):
        """
        **[Required]** Gets the shape_name of this CreateConfigurationDetails.
        The name of the associated Shape.


        :return: The shape_name of this CreateConfigurationDetails.
        :rtype: str
        """
        return self._shape_name

    @shape_name.setter
    def shape_name(self, shape_name):
        """
        Sets the shape_name of this CreateConfigurationDetails.
        The name of the associated Shape.


        :param shape_name: The shape_name of this CreateConfigurationDetails.
        :type: str
        """
        self._shape_name = shape_name

    @property
    def variables(self):
        """
        Gets the variables of this CreateConfigurationDetails.

        :return: The variables of this CreateConfigurationDetails.
        :rtype: oci.mysql.models.ConfigurationVariables
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """
        Sets the variables of this CreateConfigurationDetails.

        :param variables: The variables of this CreateConfigurationDetails.
        :type: oci.mysql.models.ConfigurationVariables
        """
        self._variables = variables

    @property
    def parent_configuration_id(self):
        """
        Gets the parent_configuration_id of this CreateConfigurationDetails.
        The OCID of the Configuration from which the new Configuration is derived. The values in CreateConfigurationDetails.variables supersede the variables of the parent Configuration.


        :return: The parent_configuration_id of this CreateConfigurationDetails.
        :rtype: str
        """
        return self._parent_configuration_id

    @parent_configuration_id.setter
    def parent_configuration_id(self, parent_configuration_id):
        """
        Sets the parent_configuration_id of this CreateConfigurationDetails.
        The OCID of the Configuration from which the new Configuration is derived. The values in CreateConfigurationDetails.variables supersede the variables of the parent Configuration.


        :param parent_configuration_id: The parent_configuration_id of this CreateConfigurationDetails.
        :type: str
        """
        self._parent_configuration_id = parent_configuration_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateConfigurationDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateConfigurationDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateConfigurationDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateConfigurationDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateConfigurationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateConfigurationDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateConfigurationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateConfigurationDetails.
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
