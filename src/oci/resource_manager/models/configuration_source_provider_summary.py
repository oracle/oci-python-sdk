# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConfigurationSourceProviderSummary(object):
    """
    Summary information for a configuration source provider.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ConfigurationSourceProviderSummary object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.resource_manager.models.GitlabAccessTokenConfigurationSourceProviderSummary`
        * :class:`~oci.resource_manager.models.GithubAccessTokenConfigurationSourceProviderSummary`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ConfigurationSourceProviderSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ConfigurationSourceProviderSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this ConfigurationSourceProviderSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this ConfigurationSourceProviderSummary.
        :type description: str

        :param time_created:
            The value to assign to the time_created property of this ConfigurationSourceProviderSummary.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ConfigurationSourceProviderSummary.
        :type lifecycle_state: str

        :param config_source_provider_type:
            The value to assign to the config_source_provider_type property of this ConfigurationSourceProviderSummary.
        :type config_source_provider_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ConfigurationSourceProviderSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ConfigurationSourceProviderSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'config_source_provider_type': 'str',
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
            'config_source_provider_type': 'configSourceProviderType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._time_created = None
        self._lifecycle_state = None
        self._config_source_provider_type = None
        self._freeform_tags = None
        self._defined_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['configSourceProviderType']

        if type == 'GITLAB_ACCESS_TOKEN':
            return 'GitlabAccessTokenConfigurationSourceProviderSummary'

        if type == 'GITHUB_ACCESS_TOKEN':
            return 'GithubAccessTokenConfigurationSourceProviderSummary'
        else:
            return 'ConfigurationSourceProviderSummary'

    @property
    def id(self):
        """
        Gets the id of this ConfigurationSourceProviderSummary.
        The `OCID`__ of the configuration source provider.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this ConfigurationSourceProviderSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ConfigurationSourceProviderSummary.
        The `OCID`__ of the configuration source provider.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this ConfigurationSourceProviderSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this ConfigurationSourceProviderSummary.
        The `OCID`__ of the compartment where the configuration source provider is located.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ConfigurationSourceProviderSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ConfigurationSourceProviderSummary.
        The `OCID`__ of the compartment where the configuration source provider is located.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ConfigurationSourceProviderSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this ConfigurationSourceProviderSummary.
        Human-readable display name for the configuration source provider.


        :return: The display_name of this ConfigurationSourceProviderSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ConfigurationSourceProviderSummary.
        Human-readable display name for the configuration source provider.


        :param display_name: The display_name of this ConfigurationSourceProviderSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this ConfigurationSourceProviderSummary.
        General description of the configuration source provider.


        :return: The description of this ConfigurationSourceProviderSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ConfigurationSourceProviderSummary.
        General description of the configuration source provider.


        :param description: The description of this ConfigurationSourceProviderSummary.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        Gets the time_created of this ConfigurationSourceProviderSummary.
        The date and time when the configuration source provider was created.
        Format is defined by RFC3339.
        Example: `2020-01-25T21:10:29.600Z`


        :return: The time_created of this ConfigurationSourceProviderSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ConfigurationSourceProviderSummary.
        The date and time when the configuration source provider was created.
        Format is defined by RFC3339.
        Example: `2020-01-25T21:10:29.600Z`


        :param time_created: The time_created of this ConfigurationSourceProviderSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this ConfigurationSourceProviderSummary.
        Current state of the specified configuration source provider.
        For more information about configuration source provider lifecycle states in Resource Manager, see
        `Key Concepts`__.

        Allowable values:
        - ACTIVE

        __ https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#CSPStates


        :return: The lifecycle_state of this ConfigurationSourceProviderSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ConfigurationSourceProviderSummary.
        Current state of the specified configuration source provider.
        For more information about configuration source provider lifecycle states in Resource Manager, see
        `Key Concepts`__.

        Allowable values:
        - ACTIVE

        __ https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#CSPStates


        :param lifecycle_state: The lifecycle_state of this ConfigurationSourceProviderSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def config_source_provider_type(self):
        """
        **[Required]** Gets the config_source_provider_type of this ConfigurationSourceProviderSummary.
        The type of configuration source provider. The `GITLAB_ACCESS_TOKEN` type corresponds to GitLab.
        The `GITHUB_ACCESS_TOKEN` type corresponds to GitHub.


        :return: The config_source_provider_type of this ConfigurationSourceProviderSummary.
        :rtype: str
        """
        return self._config_source_provider_type

    @config_source_provider_type.setter
    def config_source_provider_type(self, config_source_provider_type):
        """
        Sets the config_source_provider_type of this ConfigurationSourceProviderSummary.
        The type of configuration source provider. The `GITLAB_ACCESS_TOKEN` type corresponds to GitLab.
        The `GITHUB_ACCESS_TOKEN` type corresponds to GitHub.


        :param config_source_provider_type: The config_source_provider_type of this ConfigurationSourceProviderSummary.
        :type: str
        """
        self._config_source_provider_type = config_source_provider_type

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ConfigurationSourceProviderSummary.
        Free-form tags associated with this resource. Each tag is a key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ConfigurationSourceProviderSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ConfigurationSourceProviderSummary.
        Free-form tags associated with this resource. Each tag is a key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ConfigurationSourceProviderSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ConfigurationSourceProviderSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ConfigurationSourceProviderSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ConfigurationSourceProviderSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ConfigurationSourceProviderSummary.
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
