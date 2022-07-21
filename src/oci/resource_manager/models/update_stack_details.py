# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateStackDetails(object):
    """
    Specifies which fields and the data for each to update on the specified stack.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateStackDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateStackDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateStackDetails.
        :type description: str

        :param config_source:
            The value to assign to the config_source property of this UpdateStackDetails.
        :type config_source: oci.resource_manager.models.UpdateConfigSourceDetails

        :param custom_terraform_provider:
            The value to assign to the custom_terraform_provider property of this UpdateStackDetails.
        :type custom_terraform_provider: oci.resource_manager.models.CustomTerraformProvider

        :param is_third_party_provider_experience_enabled:
            The value to assign to the is_third_party_provider_experience_enabled property of this UpdateStackDetails.
        :type is_third_party_provider_experience_enabled: bool

        :param variables:
            The value to assign to the variables property of this UpdateStackDetails.
        :type variables: dict(str, str)

        :param terraform_version:
            The value to assign to the terraform_version property of this UpdateStackDetails.
        :type terraform_version: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateStackDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateStackDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'config_source': 'UpdateConfigSourceDetails',
            'custom_terraform_provider': 'CustomTerraformProvider',
            'is_third_party_provider_experience_enabled': 'bool',
            'variables': 'dict(str, str)',
            'terraform_version': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'config_source': 'configSource',
            'custom_terraform_provider': 'customTerraformProvider',
            'is_third_party_provider_experience_enabled': 'isThirdPartyProviderExperienceEnabled',
            'variables': 'variables',
            'terraform_version': 'terraformVersion',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._config_source = None
        self._custom_terraform_provider = None
        self._is_third_party_provider_experience_enabled = None
        self._variables = None
        self._terraform_version = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateStackDetails.
        The name of the stack.


        :return: The display_name of this UpdateStackDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateStackDetails.
        The name of the stack.


        :param display_name: The display_name of this UpdateStackDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateStackDetails.
        Description of the stack.


        :return: The description of this UpdateStackDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateStackDetails.
        Description of the stack.


        :param description: The description of this UpdateStackDetails.
        :type: str
        """
        self._description = description

    @property
    def config_source(self):
        """
        Gets the config_source of this UpdateStackDetails.

        :return: The config_source of this UpdateStackDetails.
        :rtype: oci.resource_manager.models.UpdateConfigSourceDetails
        """
        return self._config_source

    @config_source.setter
    def config_source(self, config_source):
        """
        Sets the config_source of this UpdateStackDetails.

        :param config_source: The config_source of this UpdateStackDetails.
        :type: oci.resource_manager.models.UpdateConfigSourceDetails
        """
        self._config_source = config_source

    @property
    def custom_terraform_provider(self):
        """
        Gets the custom_terraform_provider of this UpdateStackDetails.

        :return: The custom_terraform_provider of this UpdateStackDetails.
        :rtype: oci.resource_manager.models.CustomTerraformProvider
        """
        return self._custom_terraform_provider

    @custom_terraform_provider.setter
    def custom_terraform_provider(self, custom_terraform_provider):
        """
        Sets the custom_terraform_provider of this UpdateStackDetails.

        :param custom_terraform_provider: The custom_terraform_provider of this UpdateStackDetails.
        :type: oci.resource_manager.models.CustomTerraformProvider
        """
        self._custom_terraform_provider = custom_terraform_provider

    @property
    def is_third_party_provider_experience_enabled(self):
        """
        Gets the is_third_party_provider_experience_enabled of this UpdateStackDetails.
        When `true`, changes the stack's sourcing of third-party Terraform providers to
        `Terraform Registry`__ and allows
        :func:`custom_terraform_provider`.
        Applies to older stacks that use Terraform version 0.12.x and 0.13.x only.
        (Older stacks that use other Terraform versions are automatically updated.)
        Once set to `true`, cannot be reverted.
        For more information about stack sourcing of third-party Terraform providers, see
        `Third-party Provider Configuration`__.

        __ https://registry.terraform.io/browse/providers
        __ https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#third-party-providers


        :return: The is_third_party_provider_experience_enabled of this UpdateStackDetails.
        :rtype: bool
        """
        return self._is_third_party_provider_experience_enabled

    @is_third_party_provider_experience_enabled.setter
    def is_third_party_provider_experience_enabled(self, is_third_party_provider_experience_enabled):
        """
        Sets the is_third_party_provider_experience_enabled of this UpdateStackDetails.
        When `true`, changes the stack's sourcing of third-party Terraform providers to
        `Terraform Registry`__ and allows
        :func:`custom_terraform_provider`.
        Applies to older stacks that use Terraform version 0.12.x and 0.13.x only.
        (Older stacks that use other Terraform versions are automatically updated.)
        Once set to `true`, cannot be reverted.
        For more information about stack sourcing of third-party Terraform providers, see
        `Third-party Provider Configuration`__.

        __ https://registry.terraform.io/browse/providers
        __ https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#third-party-providers


        :param is_third_party_provider_experience_enabled: The is_third_party_provider_experience_enabled of this UpdateStackDetails.
        :type: bool
        """
        self._is_third_party_provider_experience_enabled = is_third_party_provider_experience_enabled

    @property
    def variables(self):
        """
        Gets the variables of this UpdateStackDetails.
        Terraform variables associated with this resource.
        The maximum number of variables supported is 250.
        The maximum size of each variable, including both name and value, is 8192 bytes.
        Example: `{\"CompartmentId\": \"compartment-id-value\"}`


        :return: The variables of this UpdateStackDetails.
        :rtype: dict(str, str)
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """
        Sets the variables of this UpdateStackDetails.
        Terraform variables associated with this resource.
        The maximum number of variables supported is 250.
        The maximum size of each variable, including both name and value, is 8192 bytes.
        Example: `{\"CompartmentId\": \"compartment-id-value\"}`


        :param variables: The variables of this UpdateStackDetails.
        :type: dict(str, str)
        """
        self._variables = variables

    @property
    def terraform_version(self):
        """
        Gets the terraform_version of this UpdateStackDetails.
        The version of Terraform to use with the stack. Example: `0.12.x`


        :return: The terraform_version of this UpdateStackDetails.
        :rtype: str
        """
        return self._terraform_version

    @terraform_version.setter
    def terraform_version(self, terraform_version):
        """
        Sets the terraform_version of this UpdateStackDetails.
        The version of Terraform to use with the stack. Example: `0.12.x`


        :param terraform_version: The terraform_version of this UpdateStackDetails.
        :type: str
        """
        self._terraform_version = terraform_version

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateStackDetails.
        Free-form tags associated with this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateStackDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateStackDetails.
        Free-form tags associated with this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateStackDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateStackDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateStackDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateStackDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateStackDetails.
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
