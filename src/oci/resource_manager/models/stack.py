# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180917


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Stack(object):
    """
    The properties that define a stack.
    A stack is the collection of Oracle Cloud Infrastructure resources corresponding to a given Terraform configuration.
    For instructions on managing stacks, see
    `Managing Stacks`__.
    For more information about stacks, see
    `Key Concepts`__.

    __ https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Tasks/stacks.htm
    __ https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#concepts__stackdefinition
    """

    #: A constant which can be used with the lifecycle_state property of a Stack.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Stack.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Stack.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Stack.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Stack.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the stack_drift_status property of a Stack.
    #: This constant has a value of "NOT_CHECKED"
    STACK_DRIFT_STATUS_NOT_CHECKED = "NOT_CHECKED"

    #: A constant which can be used with the stack_drift_status property of a Stack.
    #: This constant has a value of "IN_SYNC"
    STACK_DRIFT_STATUS_IN_SYNC = "IN_SYNC"

    #: A constant which can be used with the stack_drift_status property of a Stack.
    #: This constant has a value of "DRIFTED"
    STACK_DRIFT_STATUS_DRIFTED = "DRIFTED"

    def __init__(self, **kwargs):
        """
        Initializes a new Stack object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Stack.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Stack.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this Stack.
        :type display_name: str

        :param description:
            The value to assign to the description property of this Stack.
        :type description: str

        :param time_created:
            The value to assign to the time_created property of this Stack.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Stack.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param config_source:
            The value to assign to the config_source property of this Stack.
        :type config_source: oci.resource_manager.models.ConfigSource

        :param custom_terraform_provider:
            The value to assign to the custom_terraform_provider property of this Stack.
        :type custom_terraform_provider: oci.resource_manager.models.CustomTerraformProvider

        :param is_third_party_provider_experience_enabled:
            The value to assign to the is_third_party_provider_experience_enabled property of this Stack.
        :type is_third_party_provider_experience_enabled: bool

        :param variables:
            The value to assign to the variables property of this Stack.
        :type variables: dict(str, str)

        :param terraform_version:
            The value to assign to the terraform_version property of this Stack.
        :type terraform_version: str

        :param stack_drift_status:
            The value to assign to the stack_drift_status property of this Stack.
            Allowed values for this property are: "NOT_CHECKED", "IN_SYNC", "DRIFTED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type stack_drift_status: str

        :param time_drift_last_checked:
            The value to assign to the time_drift_last_checked property of this Stack.
        :type time_drift_last_checked: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Stack.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Stack.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'config_source': 'ConfigSource',
            'custom_terraform_provider': 'CustomTerraformProvider',
            'is_third_party_provider_experience_enabled': 'bool',
            'variables': 'dict(str, str)',
            'terraform_version': 'str',
            'stack_drift_status': 'str',
            'time_drift_last_checked': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'config_source': 'configSource',
            'custom_terraform_provider': 'customTerraformProvider',
            'is_third_party_provider_experience_enabled': 'isThirdPartyProviderExperienceEnabled',
            'variables': 'variables',
            'terraform_version': 'terraformVersion',
            'stack_drift_status': 'stackDriftStatus',
            'time_drift_last_checked': 'timeDriftLastChecked',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._time_created = None
        self._lifecycle_state = None
        self._config_source = None
        self._custom_terraform_provider = None
        self._is_third_party_provider_experience_enabled = None
        self._variables = None
        self._terraform_version = None
        self._stack_drift_status = None
        self._time_drift_last_checked = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        Gets the id of this Stack.
        Unique identifier (`OCID`__) for the stack.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this Stack.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Stack.
        Unique identifier (`OCID`__) for the stack.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this Stack.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this Stack.
        Unique identifier (`OCID`__) for the compartment where the stack is located.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this Stack.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Stack.
        Unique identifier (`OCID`__) for the compartment where the stack is located.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this Stack.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this Stack.
        Human-readable name of the stack.


        :return: The display_name of this Stack.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Stack.
        Human-readable name of the stack.


        :param display_name: The display_name of this Stack.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this Stack.
        Description of the stack.


        :return: The description of this Stack.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Stack.
        Description of the stack.


        :param description: The description of this Stack.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        Gets the time_created of this Stack.
        The date and time at which the stack was created.
        Format is defined by RFC3339.
        Example: `2020-01-25T21:10:29.600Z`


        :return: The time_created of this Stack.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Stack.
        The date and time at which the stack was created.
        Format is defined by RFC3339.
        Example: `2020-01-25T21:10:29.600Z`


        :param time_created: The time_created of this Stack.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Stack.
        The current lifecycle state of the stack.
        For more information about stack lifecycle states in Resource Manager, see
        `Key Concepts`__.

        __ https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#concepts__StackStates

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Stack.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Stack.
        The current lifecycle state of the stack.
        For more information about stack lifecycle states in Resource Manager, see
        `Key Concepts`__.

        __ https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#concepts__StackStates


        :param lifecycle_state: The lifecycle_state of this Stack.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def config_source(self):
        """
        Gets the config_source of this Stack.

        :return: The config_source of this Stack.
        :rtype: oci.resource_manager.models.ConfigSource
        """
        return self._config_source

    @config_source.setter
    def config_source(self, config_source):
        """
        Sets the config_source of this Stack.

        :param config_source: The config_source of this Stack.
        :type: oci.resource_manager.models.ConfigSource
        """
        self._config_source = config_source

    @property
    def custom_terraform_provider(self):
        """
        Gets the custom_terraform_provider of this Stack.

        :return: The custom_terraform_provider of this Stack.
        :rtype: oci.resource_manager.models.CustomTerraformProvider
        """
        return self._custom_terraform_provider

    @custom_terraform_provider.setter
    def custom_terraform_provider(self, custom_terraform_provider):
        """
        Sets the custom_terraform_provider of this Stack.

        :param custom_terraform_provider: The custom_terraform_provider of this Stack.
        :type: oci.resource_manager.models.CustomTerraformProvider
        """
        self._custom_terraform_provider = custom_terraform_provider

    @property
    def is_third_party_provider_experience_enabled(self):
        """
        Gets the is_third_party_provider_experience_enabled of this Stack.
        When `true`, the stack sources third-party Terraform providers from
        `Terraform Registry`__ and allows
        :func:`custom_terraform_provider`.
        For more information about stack sourcing of third-party Terraform providers, see
        `Third-party Provider Configuration`__.

        __ https://registry.terraform.io/browse/providers
        __ https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#third-party-providers


        :return: The is_third_party_provider_experience_enabled of this Stack.
        :rtype: bool
        """
        return self._is_third_party_provider_experience_enabled

    @is_third_party_provider_experience_enabled.setter
    def is_third_party_provider_experience_enabled(self, is_third_party_provider_experience_enabled):
        """
        Sets the is_third_party_provider_experience_enabled of this Stack.
        When `true`, the stack sources third-party Terraform providers from
        `Terraform Registry`__ and allows
        :func:`custom_terraform_provider`.
        For more information about stack sourcing of third-party Terraform providers, see
        `Third-party Provider Configuration`__.

        __ https://registry.terraform.io/browse/providers
        __ https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#third-party-providers


        :param is_third_party_provider_experience_enabled: The is_third_party_provider_experience_enabled of this Stack.
        :type: bool
        """
        self._is_third_party_provider_experience_enabled = is_third_party_provider_experience_enabled

    @property
    def variables(self):
        """
        Gets the variables of this Stack.
        Terraform variables associated with this resource.
        Maximum number of variables supported is 250.
        The maximum size of each variable, including both name and value, is 8192 bytes.
        Example: `{\"CompartmentId\": \"compartment-id-value\"}`


        :return: The variables of this Stack.
        :rtype: dict(str, str)
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """
        Sets the variables of this Stack.
        Terraform variables associated with this resource.
        Maximum number of variables supported is 250.
        The maximum size of each variable, including both name and value, is 8192 bytes.
        Example: `{\"CompartmentId\": \"compartment-id-value\"}`


        :param variables: The variables of this Stack.
        :type: dict(str, str)
        """
        self._variables = variables

    @property
    def terraform_version(self):
        """
        Gets the terraform_version of this Stack.
        The version of Terraform specified for the stack. Example: `0.12.x`


        :return: The terraform_version of this Stack.
        :rtype: str
        """
        return self._terraform_version

    @terraform_version.setter
    def terraform_version(self, terraform_version):
        """
        Sets the terraform_version of this Stack.
        The version of Terraform specified for the stack. Example: `0.12.x`


        :param terraform_version: The terraform_version of this Stack.
        :type: str
        """
        self._terraform_version = terraform_version

    @property
    def stack_drift_status(self):
        """
        Gets the stack_drift_status of this Stack.
        Drift status of the stack.
        Drift refers to differences between the actual (current) state of the stack and the expected (defined) state of the stack.

        Allowed values for this property are: "NOT_CHECKED", "IN_SYNC", "DRIFTED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The stack_drift_status of this Stack.
        :rtype: str
        """
        return self._stack_drift_status

    @stack_drift_status.setter
    def stack_drift_status(self, stack_drift_status):
        """
        Sets the stack_drift_status of this Stack.
        Drift status of the stack.
        Drift refers to differences between the actual (current) state of the stack and the expected (defined) state of the stack.


        :param stack_drift_status: The stack_drift_status of this Stack.
        :type: str
        """
        allowed_values = ["NOT_CHECKED", "IN_SYNC", "DRIFTED"]
        if not value_allowed_none_or_none_sentinel(stack_drift_status, allowed_values):
            stack_drift_status = 'UNKNOWN_ENUM_VALUE'
        self._stack_drift_status = stack_drift_status

    @property
    def time_drift_last_checked(self):
        """
        Gets the time_drift_last_checked of this Stack.
        The date and time when the drift detection was last executed.
        Format is defined by RFC3339.
        Example: `2020-01-25T21:10:29.600Z`


        :return: The time_drift_last_checked of this Stack.
        :rtype: datetime
        """
        return self._time_drift_last_checked

    @time_drift_last_checked.setter
    def time_drift_last_checked(self, time_drift_last_checked):
        """
        Sets the time_drift_last_checked of this Stack.
        The date and time when the drift detection was last executed.
        Format is defined by RFC3339.
        Example: `2020-01-25T21:10:29.600Z`


        :param time_drift_last_checked: The time_drift_last_checked of this Stack.
        :type: datetime
        """
        self._time_drift_last_checked = time_drift_last_checked

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Stack.
        Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Stack.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Stack.
        Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Stack.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Stack.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Stack.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Stack.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Stack.
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
