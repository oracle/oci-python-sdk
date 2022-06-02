# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_configuration_source_provider_details import UpdateConfigurationSourceProviderDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateGitlabAccessTokenConfigurationSourceProviderDetails(UpdateConfigurationSourceProviderDetails):
    """
    The details for updating a configuration source provider of the type `GITLAB_ACCESS_TOKEN`.
    This type corresponds to a configuration source provider in GitLab that is authenticated with a personal access token.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateGitlabAccessTokenConfigurationSourceProviderDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.resource_manager.models.UpdateGitlabAccessTokenConfigurationSourceProviderDetails.config_source_provider_type` attribute
        of this class is ``GITLAB_ACCESS_TOKEN`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateGitlabAccessTokenConfigurationSourceProviderDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateGitlabAccessTokenConfigurationSourceProviderDetails.
        :type description: str

        :param config_source_provider_type:
            The value to assign to the config_source_provider_type property of this UpdateGitlabAccessTokenConfigurationSourceProviderDetails.
        :type config_source_provider_type: str

        :param private_server_config_details:
            The value to assign to the private_server_config_details property of this UpdateGitlabAccessTokenConfigurationSourceProviderDetails.
        :type private_server_config_details: oci.resource_manager.models.PrivateServerConfigDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateGitlabAccessTokenConfigurationSourceProviderDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateGitlabAccessTokenConfigurationSourceProviderDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param api_endpoint:
            The value to assign to the api_endpoint property of this UpdateGitlabAccessTokenConfigurationSourceProviderDetails.
        :type api_endpoint: str

        :param access_token:
            The value to assign to the access_token property of this UpdateGitlabAccessTokenConfigurationSourceProviderDetails.
        :type access_token: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'config_source_provider_type': 'str',
            'private_server_config_details': 'PrivateServerConfigDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'api_endpoint': 'str',
            'access_token': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'config_source_provider_type': 'configSourceProviderType',
            'private_server_config_details': 'privateServerConfigDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'api_endpoint': 'apiEndpoint',
            'access_token': 'accessToken'
        }

        self._display_name = None
        self._description = None
        self._config_source_provider_type = None
        self._private_server_config_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._api_endpoint = None
        self._access_token = None
        self._config_source_provider_type = 'GITLAB_ACCESS_TOKEN'

    @property
    def api_endpoint(self):
        """
        Gets the api_endpoint of this UpdateGitlabAccessTokenConfigurationSourceProviderDetails.
        The Git service endpoint.
        Example: `https://gitlab.com`


        :return: The api_endpoint of this UpdateGitlabAccessTokenConfigurationSourceProviderDetails.
        :rtype: str
        """
        return self._api_endpoint

    @api_endpoint.setter
    def api_endpoint(self, api_endpoint):
        """
        Sets the api_endpoint of this UpdateGitlabAccessTokenConfigurationSourceProviderDetails.
        The Git service endpoint.
        Example: `https://gitlab.com`


        :param api_endpoint: The api_endpoint of this UpdateGitlabAccessTokenConfigurationSourceProviderDetails.
        :type: str
        """
        self._api_endpoint = api_endpoint

    @property
    def access_token(self):
        """
        Gets the access_token of this UpdateGitlabAccessTokenConfigurationSourceProviderDetails.
        The personal access token to be configured on the GitLab repository.


        :return: The access_token of this UpdateGitlabAccessTokenConfigurationSourceProviderDetails.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """
        Sets the access_token of this UpdateGitlabAccessTokenConfigurationSourceProviderDetails.
        The personal access token to be configured on the GitLab repository.


        :param access_token: The access_token of this UpdateGitlabAccessTokenConfigurationSourceProviderDetails.
        :type: str
        """
        self._access_token = access_token

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
