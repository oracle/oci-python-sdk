# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .authentication_policy import AuthenticationPolicy
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TokenAuthenticationPolicy(AuthenticationPolicy):
    """
    Validate a token present in the header or query parameter. A valid
    policy must specify either tokenHeader or tokenQueryParam.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TokenAuthenticationPolicy object with values from keyword arguments. The default value of the :py:attr:`~oci.apigateway.models.TokenAuthenticationPolicy.type` attribute
        of this class is ``TOKEN_AUTHENTICATION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_anonymous_access_allowed:
            The value to assign to the is_anonymous_access_allowed property of this TokenAuthenticationPolicy.
        :type is_anonymous_access_allowed: bool

        :param type:
            The value to assign to the type property of this TokenAuthenticationPolicy.
            Allowed values for this property are: "CUSTOM_AUTHENTICATION", "JWT_AUTHENTICATION", "TOKEN_AUTHENTICATION"
        :type type: str

        :param token_header:
            The value to assign to the token_header property of this TokenAuthenticationPolicy.
        :type token_header: str

        :param token_query_param:
            The value to assign to the token_query_param property of this TokenAuthenticationPolicy.
        :type token_query_param: str

        :param token_auth_scheme:
            The value to assign to the token_auth_scheme property of this TokenAuthenticationPolicy.
        :type token_auth_scheme: str

        :param max_clock_skew_in_seconds:
            The value to assign to the max_clock_skew_in_seconds property of this TokenAuthenticationPolicy.
        :type max_clock_skew_in_seconds: float

        :param validation_policy:
            The value to assign to the validation_policy property of this TokenAuthenticationPolicy.
        :type validation_policy: oci.apigateway.models.TokenAuthenticationValidationPolicy

        :param validation_failure_policy:
            The value to assign to the validation_failure_policy property of this TokenAuthenticationPolicy.
        :type validation_failure_policy: oci.apigateway.models.ValidationFailurePolicy

        """
        self.swagger_types = {
            'is_anonymous_access_allowed': 'bool',
            'type': 'str',
            'token_header': 'str',
            'token_query_param': 'str',
            'token_auth_scheme': 'str',
            'max_clock_skew_in_seconds': 'float',
            'validation_policy': 'TokenAuthenticationValidationPolicy',
            'validation_failure_policy': 'ValidationFailurePolicy'
        }

        self.attribute_map = {
            'is_anonymous_access_allowed': 'isAnonymousAccessAllowed',
            'type': 'type',
            'token_header': 'tokenHeader',
            'token_query_param': 'tokenQueryParam',
            'token_auth_scheme': 'tokenAuthScheme',
            'max_clock_skew_in_seconds': 'maxClockSkewInSeconds',
            'validation_policy': 'validationPolicy',
            'validation_failure_policy': 'validationFailurePolicy'
        }

        self._is_anonymous_access_allowed = None
        self._type = None
        self._token_header = None
        self._token_query_param = None
        self._token_auth_scheme = None
        self._max_clock_skew_in_seconds = None
        self._validation_policy = None
        self._validation_failure_policy = None
        self._type = 'TOKEN_AUTHENTICATION'

    @property
    def token_header(self):
        """
        Gets the token_header of this TokenAuthenticationPolicy.
        The name of the header containing the authentication token.


        :return: The token_header of this TokenAuthenticationPolicy.
        :rtype: str
        """
        return self._token_header

    @token_header.setter
    def token_header(self, token_header):
        """
        Sets the token_header of this TokenAuthenticationPolicy.
        The name of the header containing the authentication token.


        :param token_header: The token_header of this TokenAuthenticationPolicy.
        :type: str
        """
        self._token_header = token_header

    @property
    def token_query_param(self):
        """
        Gets the token_query_param of this TokenAuthenticationPolicy.
        The name of the query parameter containing the authentication token.


        :return: The token_query_param of this TokenAuthenticationPolicy.
        :rtype: str
        """
        return self._token_query_param

    @token_query_param.setter
    def token_query_param(self, token_query_param):
        """
        Sets the token_query_param of this TokenAuthenticationPolicy.
        The name of the query parameter containing the authentication token.


        :param token_query_param: The token_query_param of this TokenAuthenticationPolicy.
        :type: str
        """
        self._token_query_param = token_query_param

    @property
    def token_auth_scheme(self):
        """
        Gets the token_auth_scheme of this TokenAuthenticationPolicy.
        The authentication scheme that is to be used when authenticating
        the token. This must to be provided if \"tokenHeader\" is specified.


        :return: The token_auth_scheme of this TokenAuthenticationPolicy.
        :rtype: str
        """
        return self._token_auth_scheme

    @token_auth_scheme.setter
    def token_auth_scheme(self, token_auth_scheme):
        """
        Sets the token_auth_scheme of this TokenAuthenticationPolicy.
        The authentication scheme that is to be used when authenticating
        the token. This must to be provided if \"tokenHeader\" is specified.


        :param token_auth_scheme: The token_auth_scheme of this TokenAuthenticationPolicy.
        :type: str
        """
        self._token_auth_scheme = token_auth_scheme

    @property
    def max_clock_skew_in_seconds(self):
        """
        Gets the max_clock_skew_in_seconds of this TokenAuthenticationPolicy.
        The maximum expected time difference between the system clocks
        of the token issuer and the API Gateway.


        :return: The max_clock_skew_in_seconds of this TokenAuthenticationPolicy.
        :rtype: float
        """
        return self._max_clock_skew_in_seconds

    @max_clock_skew_in_seconds.setter
    def max_clock_skew_in_seconds(self, max_clock_skew_in_seconds):
        """
        Sets the max_clock_skew_in_seconds of this TokenAuthenticationPolicy.
        The maximum expected time difference between the system clocks
        of the token issuer and the API Gateway.


        :param max_clock_skew_in_seconds: The max_clock_skew_in_seconds of this TokenAuthenticationPolicy.
        :type: float
        """
        self._max_clock_skew_in_seconds = max_clock_skew_in_seconds

    @property
    def validation_policy(self):
        """
        **[Required]** Gets the validation_policy of this TokenAuthenticationPolicy.

        :return: The validation_policy of this TokenAuthenticationPolicy.
        :rtype: oci.apigateway.models.TokenAuthenticationValidationPolicy
        """
        return self._validation_policy

    @validation_policy.setter
    def validation_policy(self, validation_policy):
        """
        Sets the validation_policy of this TokenAuthenticationPolicy.

        :param validation_policy: The validation_policy of this TokenAuthenticationPolicy.
        :type: oci.apigateway.models.TokenAuthenticationValidationPolicy
        """
        self._validation_policy = validation_policy

    @property
    def validation_failure_policy(self):
        """
        Gets the validation_failure_policy of this TokenAuthenticationPolicy.

        :return: The validation_failure_policy of this TokenAuthenticationPolicy.
        :rtype: oci.apigateway.models.ValidationFailurePolicy
        """
        return self._validation_failure_policy

    @validation_failure_policy.setter
    def validation_failure_policy(self, validation_failure_policy):
        """
        Sets the validation_failure_policy of this TokenAuthenticationPolicy.

        :param validation_failure_policy: The validation_failure_policy of this TokenAuthenticationPolicy.
        :type: oci.apigateway.models.ValidationFailurePolicy
        """
        self._validation_failure_policy = validation_failure_policy

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
