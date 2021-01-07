# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UserCapabilities(object):
    """
    Properties indicating how the user is allowed to authenticate.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UserCapabilities object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param can_use_console_password:
            The value to assign to the can_use_console_password property of this UserCapabilities.
        :type can_use_console_password: bool

        :param can_use_api_keys:
            The value to assign to the can_use_api_keys property of this UserCapabilities.
        :type can_use_api_keys: bool

        :param can_use_auth_tokens:
            The value to assign to the can_use_auth_tokens property of this UserCapabilities.
        :type can_use_auth_tokens: bool

        :param can_use_smtp_credentials:
            The value to assign to the can_use_smtp_credentials property of this UserCapabilities.
        :type can_use_smtp_credentials: bool

        :param can_use_customer_secret_keys:
            The value to assign to the can_use_customer_secret_keys property of this UserCapabilities.
        :type can_use_customer_secret_keys: bool

        :param can_use_o_auth2_client_credentials:
            The value to assign to the can_use_o_auth2_client_credentials property of this UserCapabilities.
        :type can_use_o_auth2_client_credentials: bool

        """
        self.swagger_types = {
            'can_use_console_password': 'bool',
            'can_use_api_keys': 'bool',
            'can_use_auth_tokens': 'bool',
            'can_use_smtp_credentials': 'bool',
            'can_use_customer_secret_keys': 'bool',
            'can_use_o_auth2_client_credentials': 'bool'
        }

        self.attribute_map = {
            'can_use_console_password': 'canUseConsolePassword',
            'can_use_api_keys': 'canUseApiKeys',
            'can_use_auth_tokens': 'canUseAuthTokens',
            'can_use_smtp_credentials': 'canUseSmtpCredentials',
            'can_use_customer_secret_keys': 'canUseCustomerSecretKeys',
            'can_use_o_auth2_client_credentials': 'canUseOAuth2ClientCredentials'
        }

        self._can_use_console_password = None
        self._can_use_api_keys = None
        self._can_use_auth_tokens = None
        self._can_use_smtp_credentials = None
        self._can_use_customer_secret_keys = None
        self._can_use_o_auth2_client_credentials = None

    @property
    def can_use_console_password(self):
        """
        Gets the can_use_console_password of this UserCapabilities.
        Indicates if the user can log in to the console.


        :return: The can_use_console_password of this UserCapabilities.
        :rtype: bool
        """
        return self._can_use_console_password

    @can_use_console_password.setter
    def can_use_console_password(self, can_use_console_password):
        """
        Sets the can_use_console_password of this UserCapabilities.
        Indicates if the user can log in to the console.


        :param can_use_console_password: The can_use_console_password of this UserCapabilities.
        :type: bool
        """
        self._can_use_console_password = can_use_console_password

    @property
    def can_use_api_keys(self):
        """
        Gets the can_use_api_keys of this UserCapabilities.
        Indicates if the user can use API keys.


        :return: The can_use_api_keys of this UserCapabilities.
        :rtype: bool
        """
        return self._can_use_api_keys

    @can_use_api_keys.setter
    def can_use_api_keys(self, can_use_api_keys):
        """
        Sets the can_use_api_keys of this UserCapabilities.
        Indicates if the user can use API keys.


        :param can_use_api_keys: The can_use_api_keys of this UserCapabilities.
        :type: bool
        """
        self._can_use_api_keys = can_use_api_keys

    @property
    def can_use_auth_tokens(self):
        """
        Gets the can_use_auth_tokens of this UserCapabilities.
        Indicates if the user can use SWIFT passwords / auth tokens.


        :return: The can_use_auth_tokens of this UserCapabilities.
        :rtype: bool
        """
        return self._can_use_auth_tokens

    @can_use_auth_tokens.setter
    def can_use_auth_tokens(self, can_use_auth_tokens):
        """
        Sets the can_use_auth_tokens of this UserCapabilities.
        Indicates if the user can use SWIFT passwords / auth tokens.


        :param can_use_auth_tokens: The can_use_auth_tokens of this UserCapabilities.
        :type: bool
        """
        self._can_use_auth_tokens = can_use_auth_tokens

    @property
    def can_use_smtp_credentials(self):
        """
        Gets the can_use_smtp_credentials of this UserCapabilities.
        Indicates if the user can use SMTP passwords.


        :return: The can_use_smtp_credentials of this UserCapabilities.
        :rtype: bool
        """
        return self._can_use_smtp_credentials

    @can_use_smtp_credentials.setter
    def can_use_smtp_credentials(self, can_use_smtp_credentials):
        """
        Sets the can_use_smtp_credentials of this UserCapabilities.
        Indicates if the user can use SMTP passwords.


        :param can_use_smtp_credentials: The can_use_smtp_credentials of this UserCapabilities.
        :type: bool
        """
        self._can_use_smtp_credentials = can_use_smtp_credentials

    @property
    def can_use_customer_secret_keys(self):
        """
        Gets the can_use_customer_secret_keys of this UserCapabilities.
        Indicates if the user can use SigV4 symmetric keys.


        :return: The can_use_customer_secret_keys of this UserCapabilities.
        :rtype: bool
        """
        return self._can_use_customer_secret_keys

    @can_use_customer_secret_keys.setter
    def can_use_customer_secret_keys(self, can_use_customer_secret_keys):
        """
        Sets the can_use_customer_secret_keys of this UserCapabilities.
        Indicates if the user can use SigV4 symmetric keys.


        :param can_use_customer_secret_keys: The can_use_customer_secret_keys of this UserCapabilities.
        :type: bool
        """
        self._can_use_customer_secret_keys = can_use_customer_secret_keys

    @property
    def can_use_o_auth2_client_credentials(self):
        """
        Gets the can_use_o_auth2_client_credentials of this UserCapabilities.
        Indicates if the user can use OAuth2 credentials and tokens.


        :return: The can_use_o_auth2_client_credentials of this UserCapabilities.
        :rtype: bool
        """
        return self._can_use_o_auth2_client_credentials

    @can_use_o_auth2_client_credentials.setter
    def can_use_o_auth2_client_credentials(self, can_use_o_auth2_client_credentials):
        """
        Sets the can_use_o_auth2_client_credentials of this UserCapabilities.
        Indicates if the user can use OAuth2 credentials and tokens.


        :param can_use_o_auth2_client_credentials: The can_use_o_auth2_client_credentials of this UserCapabilities.
        :type: bool
        """
        self._can_use_o_auth2_client_credentials = can_use_o_auth2_client_credentials

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
