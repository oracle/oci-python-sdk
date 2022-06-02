# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateConfigurationSourceProviderDetails(object):
    """
    The details for updating a configuration source provider.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateConfigurationSourceProviderDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.resource_manager.models.UpdateGitlabAccessTokenConfigurationSourceProviderDetails`
        * :class:`~oci.resource_manager.models.UpdateGithubAccessTokenConfigurationSourceProviderDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateConfigurationSourceProviderDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateConfigurationSourceProviderDetails.
        :type description: str

        :param config_source_provider_type:
            The value to assign to the config_source_provider_type property of this UpdateConfigurationSourceProviderDetails.
        :type config_source_provider_type: str

        :param private_server_config_details:
            The value to assign to the private_server_config_details property of this UpdateConfigurationSourceProviderDetails.
        :type private_server_config_details: oci.resource_manager.models.PrivateServerConfigDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateConfigurationSourceProviderDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateConfigurationSourceProviderDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'config_source_provider_type': 'str',
            'private_server_config_details': 'PrivateServerConfigDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'config_source_provider_type': 'configSourceProviderType',
            'private_server_config_details': 'privateServerConfigDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._config_source_provider_type = None
        self._private_server_config_details = None
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
            return 'UpdateGitlabAccessTokenConfigurationSourceProviderDetails'

        if type == 'GITHUB_ACCESS_TOKEN':
            return 'UpdateGithubAccessTokenConfigurationSourceProviderDetails'
        else:
            return 'UpdateConfigurationSourceProviderDetails'

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateConfigurationSourceProviderDetails.
        Human-readable name of the configuration source provider. Avoid entering confidential information.


        :return: The display_name of this UpdateConfigurationSourceProviderDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateConfigurationSourceProviderDetails.
        Human-readable name of the configuration source provider. Avoid entering confidential information.


        :param display_name: The display_name of this UpdateConfigurationSourceProviderDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateConfigurationSourceProviderDetails.
        Description of the configuration source provider. Avoid entering confidential information.


        :return: The description of this UpdateConfigurationSourceProviderDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateConfigurationSourceProviderDetails.
        Description of the configuration source provider. Avoid entering confidential information.


        :param description: The description of this UpdateConfigurationSourceProviderDetails.
        :type: str
        """
        self._description = description

    @property
    def config_source_provider_type(self):
        """
        Gets the config_source_provider_type of this UpdateConfigurationSourceProviderDetails.
        The type of configuration source provider.
        The `GITLAB_ACCESS_TOKEN` type corresponds to GitLab.
        The `GITHUB_ACCESS_TOKEN` type corresponds to GitHub.


        :return: The config_source_provider_type of this UpdateConfigurationSourceProviderDetails.
        :rtype: str
        """
        return self._config_source_provider_type

    @config_source_provider_type.setter
    def config_source_provider_type(self, config_source_provider_type):
        """
        Sets the config_source_provider_type of this UpdateConfigurationSourceProviderDetails.
        The type of configuration source provider.
        The `GITLAB_ACCESS_TOKEN` type corresponds to GitLab.
        The `GITHUB_ACCESS_TOKEN` type corresponds to GitHub.


        :param config_source_provider_type: The config_source_provider_type of this UpdateConfigurationSourceProviderDetails.
        :type: str
        """
        self._config_source_provider_type = config_source_provider_type

    @property
    def private_server_config_details(self):
        """
        Gets the private_server_config_details of this UpdateConfigurationSourceProviderDetails.

        :return: The private_server_config_details of this UpdateConfigurationSourceProviderDetails.
        :rtype: oci.resource_manager.models.PrivateServerConfigDetails
        """
        return self._private_server_config_details

    @private_server_config_details.setter
    def private_server_config_details(self, private_server_config_details):
        """
        Sets the private_server_config_details of this UpdateConfigurationSourceProviderDetails.

        :param private_server_config_details: The private_server_config_details of this UpdateConfigurationSourceProviderDetails.
        :type: oci.resource_manager.models.PrivateServerConfigDetails
        """
        self._private_server_config_details = private_server_config_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateConfigurationSourceProviderDetails.
        Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateConfigurationSourceProviderDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateConfigurationSourceProviderDetails.
        Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateConfigurationSourceProviderDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateConfigurationSourceProviderDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateConfigurationSourceProviderDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateConfigurationSourceProviderDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateConfigurationSourceProviderDetails.
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
