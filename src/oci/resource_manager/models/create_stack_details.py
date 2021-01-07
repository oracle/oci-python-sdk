# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateStackDetails(object):
    """
    The configuration details for creating a stack.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateStackDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateStackDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateStackDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateStackDetails.
        :type description: str

        :param config_source:
            The value to assign to the config_source property of this CreateStackDetails.
        :type config_source: oci.resource_manager.models.CreateConfigSourceDetails

        :param variables:
            The value to assign to the variables property of this CreateStackDetails.
        :type variables: dict(str, str)

        :param terraform_version:
            The value to assign to the terraform_version property of this CreateStackDetails.
        :type terraform_version: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateStackDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateStackDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'config_source': 'CreateConfigSourceDetails',
            'variables': 'dict(str, str)',
            'terraform_version': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'config_source': 'configSource',
            'variables': 'variables',
            'terraform_version': 'terraformVersion',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._config_source = None
        self._variables = None
        self._terraform_version = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateStackDetails.
        Unique identifier (`OCID`__) of the compartment in which the stack resides.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateStackDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateStackDetails.
        Unique identifier (`OCID`__) of the compartment in which the stack resides.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateStackDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateStackDetails.
        The stack's display name.


        :return: The display_name of this CreateStackDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateStackDetails.
        The stack's display name.


        :param display_name: The display_name of this CreateStackDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateStackDetails.
        Description of the stack.


        :return: The description of this CreateStackDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateStackDetails.
        Description of the stack.


        :param description: The description of this CreateStackDetails.
        :type: str
        """
        self._description = description

    @property
    def config_source(self):
        """
        **[Required]** Gets the config_source of this CreateStackDetails.

        :return: The config_source of this CreateStackDetails.
        :rtype: oci.resource_manager.models.CreateConfigSourceDetails
        """
        return self._config_source

    @config_source.setter
    def config_source(self, config_source):
        """
        Sets the config_source of this CreateStackDetails.

        :param config_source: The config_source of this CreateStackDetails.
        :type: oci.resource_manager.models.CreateConfigSourceDetails
        """
        self._config_source = config_source

    @property
    def variables(self):
        """
        Gets the variables of this CreateStackDetails.
        Terraform variables associated with this resource.
        Maximum number of variables supported is 250.
        The maximum size of each variable, including both name and value, is 4096 bytes.
        Example: `{\"CompartmentId\": \"compartment-id-value\"}`


        :return: The variables of this CreateStackDetails.
        :rtype: dict(str, str)
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """
        Sets the variables of this CreateStackDetails.
        Terraform variables associated with this resource.
        Maximum number of variables supported is 250.
        The maximum size of each variable, including both name and value, is 4096 bytes.
        Example: `{\"CompartmentId\": \"compartment-id-value\"}`


        :param variables: The variables of this CreateStackDetails.
        :type: dict(str, str)
        """
        self._variables = variables

    @property
    def terraform_version(self):
        """
        Gets the terraform_version of this CreateStackDetails.
        The version of Terraform to use with the stack. Example: `0.12.x`


        :return: The terraform_version of this CreateStackDetails.
        :rtype: str
        """
        return self._terraform_version

    @terraform_version.setter
    def terraform_version(self, terraform_version):
        """
        Sets the terraform_version of this CreateStackDetails.
        The version of Terraform to use with the stack. Example: `0.12.x`


        :param terraform_version: The terraform_version of this CreateStackDetails.
        :type: str
        """
        self._terraform_version = terraform_version

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateStackDetails.
        Free-form tags associated with this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateStackDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateStackDetails.
        Free-form tags associated with this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateStackDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateStackDetails.
        Defined tags associated with this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateStackDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateStackDetails.
        Defined tags associated with this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateStackDetails.
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
