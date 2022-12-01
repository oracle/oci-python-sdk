# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_configuration_source_provider_details import CreateConfigurationSourceProviderDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateBitbucketCloudUsernameAppPasswordConfigurationSourceProviderDetails(CreateConfigurationSourceProviderDetails):
    """
    Creation details for a configuration source provider of the type `BITBUCKET_CLOUD_USERNAME_appPASSWORD`.
    This type corresponds to a configuration source provider in Bitbucket that is authenticated with a username and app password.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateBitbucketCloudUsernameAppPasswordConfigurationSourceProviderDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.resource_manager.models.CreateBitbucketCloudUsernameAppPasswordConfigurationSourceProviderDetails.config_source_provider_type` attribute
        of this class is ``BITBUCKET_CLOUD_USERNAME_APPPASSWORD`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateBitbucketCloudUsernameAppPasswordConfigurationSourceProviderDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateBitbucketCloudUsernameAppPasswordConfigurationSourceProviderDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateBitbucketCloudUsernameAppPasswordConfigurationSourceProviderDetails.
        :type description: str

        :param config_source_provider_type:
            The value to assign to the config_source_provider_type property of this CreateBitbucketCloudUsernameAppPasswordConfigurationSourceProviderDetails.
        :type config_source_provider_type: str

        :param private_server_config_details:
            The value to assign to the private_server_config_details property of this CreateBitbucketCloudUsernameAppPasswordConfigurationSourceProviderDetails.
        :type private_server_config_details: oci.resource_manager.models.PrivateServerConfigDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateBitbucketCloudUsernameAppPasswordConfigurationSourceProviderDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateBitbucketCloudUsernameAppPasswordConfigurationSourceProviderDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param api_endpoint:
            The value to assign to the api_endpoint property of this CreateBitbucketCloudUsernameAppPasswordConfigurationSourceProviderDetails.
        :type api_endpoint: str

        :param username:
            The value to assign to the username property of this CreateBitbucketCloudUsernameAppPasswordConfigurationSourceProviderDetails.
        :type username: str

        :param secret_id:
            The value to assign to the secret_id property of this CreateBitbucketCloudUsernameAppPasswordConfigurationSourceProviderDetails.
        :type secret_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'config_source_provider_type': 'str',
            'private_server_config_details': 'PrivateServerConfigDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'api_endpoint': 'str',
            'username': 'str',
            'secret_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'config_source_provider_type': 'configSourceProviderType',
            'private_server_config_details': 'privateServerConfigDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'api_endpoint': 'apiEndpoint',
            'username': 'username',
            'secret_id': 'secretId'
        }

        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._config_source_provider_type = None
        self._private_server_config_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._api_endpoint = None
        self._username = None
        self._secret_id = None
        self._config_source_provider_type = 'BITBUCKET_CLOUD_USERNAME_APPPASSWORD'

    @property
    def api_endpoint(self):
        """
        **[Required]** Gets the api_endpoint of this CreateBitbucketCloudUsernameAppPasswordConfigurationSourceProviderDetails.
        The Bitbucket cloud service endpoint.
        Example: `https://bitbucket.org/`


        :return: The api_endpoint of this CreateBitbucketCloudUsernameAppPasswordConfigurationSourceProviderDetails.
        :rtype: str
        """
        return self._api_endpoint

    @api_endpoint.setter
    def api_endpoint(self, api_endpoint):
        """
        Sets the api_endpoint of this CreateBitbucketCloudUsernameAppPasswordConfigurationSourceProviderDetails.
        The Bitbucket cloud service endpoint.
        Example: `https://bitbucket.org/`


        :param api_endpoint: The api_endpoint of this CreateBitbucketCloudUsernameAppPasswordConfigurationSourceProviderDetails.
        :type: str
        """
        self._api_endpoint = api_endpoint

    @property
    def username(self):
        """
        **[Required]** Gets the username of this CreateBitbucketCloudUsernameAppPasswordConfigurationSourceProviderDetails.
        The username for the user of the Bitbucket cloud repository.


        :return: The username of this CreateBitbucketCloudUsernameAppPasswordConfigurationSourceProviderDetails.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this CreateBitbucketCloudUsernameAppPasswordConfigurationSourceProviderDetails.
        The username for the user of the Bitbucket cloud repository.


        :param username: The username of this CreateBitbucketCloudUsernameAppPasswordConfigurationSourceProviderDetails.
        :type: str
        """
        self._username = username

    @property
    def secret_id(self):
        """
        **[Required]** Gets the secret_id of this CreateBitbucketCloudUsernameAppPasswordConfigurationSourceProviderDetails.
        The secret ocid which is used to authorize the user.


        :return: The secret_id of this CreateBitbucketCloudUsernameAppPasswordConfigurationSourceProviderDetails.
        :rtype: str
        """
        return self._secret_id

    @secret_id.setter
    def secret_id(self, secret_id):
        """
        Sets the secret_id of this CreateBitbucketCloudUsernameAppPasswordConfigurationSourceProviderDetails.
        The secret ocid which is used to authorize the user.


        :param secret_id: The secret_id of this CreateBitbucketCloudUsernameAppPasswordConfigurationSourceProviderDetails.
        :type: str
        """
        self._secret_id = secret_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
