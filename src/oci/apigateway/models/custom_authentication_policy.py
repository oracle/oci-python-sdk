# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .authentication_policy import AuthenticationPolicy
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CustomAuthenticationPolicy(AuthenticationPolicy):
    """
    Use a function to validate a custom header or query parameter sent with the request authentication.
    A valid policy must specify either tokenHeader or tokenQueryParam.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CustomAuthenticationPolicy object with values from keyword arguments. The default value of the :py:attr:`~oci.apigateway.models.CustomAuthenticationPolicy.type` attribute
        of this class is ``CUSTOM_AUTHENTICATION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_anonymous_access_allowed:
            The value to assign to the is_anonymous_access_allowed property of this CustomAuthenticationPolicy.
        :type is_anonymous_access_allowed: bool

        :param type:
            The value to assign to the type property of this CustomAuthenticationPolicy.
            Allowed values for this property are: "CUSTOM_AUTHENTICATION", "JWT_AUTHENTICATION", "TOKEN_AUTHENTICATION"
        :type type: str

        :param function_id:
            The value to assign to the function_id property of this CustomAuthenticationPolicy.
        :type function_id: str

        :param token_header:
            The value to assign to the token_header property of this CustomAuthenticationPolicy.
        :type token_header: str

        :param token_query_param:
            The value to assign to the token_query_param property of this CustomAuthenticationPolicy.
        :type token_query_param: str

        :param parameters:
            The value to assign to the parameters property of this CustomAuthenticationPolicy.
        :type parameters: dict(str, str)

        :param cache_key:
            The value to assign to the cache_key property of this CustomAuthenticationPolicy.
        :type cache_key: list[str]

        :param validation_failure_policy:
            The value to assign to the validation_failure_policy property of this CustomAuthenticationPolicy.
        :type validation_failure_policy: oci.apigateway.models.ValidationFailurePolicy

        """
        self.swagger_types = {
            'is_anonymous_access_allowed': 'bool',
            'type': 'str',
            'function_id': 'str',
            'token_header': 'str',
            'token_query_param': 'str',
            'parameters': 'dict(str, str)',
            'cache_key': 'list[str]',
            'validation_failure_policy': 'ValidationFailurePolicy'
        }

        self.attribute_map = {
            'is_anonymous_access_allowed': 'isAnonymousAccessAllowed',
            'type': 'type',
            'function_id': 'functionId',
            'token_header': 'tokenHeader',
            'token_query_param': 'tokenQueryParam',
            'parameters': 'parameters',
            'cache_key': 'cacheKey',
            'validation_failure_policy': 'validationFailurePolicy'
        }

        self._is_anonymous_access_allowed = None
        self._type = None
        self._function_id = None
        self._token_header = None
        self._token_query_param = None
        self._parameters = None
        self._cache_key = None
        self._validation_failure_policy = None
        self._type = 'CUSTOM_AUTHENTICATION'

    @property
    def function_id(self):
        """
        **[Required]** Gets the function_id of this CustomAuthenticationPolicy.
        The `OCID`__ of the Oracle Functions function resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The function_id of this CustomAuthenticationPolicy.
        :rtype: str
        """
        return self._function_id

    @function_id.setter
    def function_id(self, function_id):
        """
        Sets the function_id of this CustomAuthenticationPolicy.
        The `OCID`__ of the Oracle Functions function resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param function_id: The function_id of this CustomAuthenticationPolicy.
        :type: str
        """
        self._function_id = function_id

    @property
    def token_header(self):
        """
        Gets the token_header of this CustomAuthenticationPolicy.
        The name of the header containing the authentication token.


        :return: The token_header of this CustomAuthenticationPolicy.
        :rtype: str
        """
        return self._token_header

    @token_header.setter
    def token_header(self, token_header):
        """
        Sets the token_header of this CustomAuthenticationPolicy.
        The name of the header containing the authentication token.


        :param token_header: The token_header of this CustomAuthenticationPolicy.
        :type: str
        """
        self._token_header = token_header

    @property
    def token_query_param(self):
        """
        Gets the token_query_param of this CustomAuthenticationPolicy.
        The name of the query parameter containing the authentication token.


        :return: The token_query_param of this CustomAuthenticationPolicy.
        :rtype: str
        """
        return self._token_query_param

    @token_query_param.setter
    def token_query_param(self, token_query_param):
        """
        Sets the token_query_param of this CustomAuthenticationPolicy.
        The name of the query parameter containing the authentication token.


        :param token_query_param: The token_query_param of this CustomAuthenticationPolicy.
        :type: str
        """
        self._token_query_param = token_query_param

    @property
    def parameters(self):
        """
        Gets the parameters of this CustomAuthenticationPolicy.
        A map where key is a user defined string and value is a context expressions whose values will be sent to the custom auth function. Values should contain an expression.
        Example: `{\"foo\": \"request.header[abc]\"}`


        :return: The parameters of this CustomAuthenticationPolicy.
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this CustomAuthenticationPolicy.
        A map where key is a user defined string and value is a context expressions whose values will be sent to the custom auth function. Values should contain an expression.
        Example: `{\"foo\": \"request.header[abc]\"}`


        :param parameters: The parameters of this CustomAuthenticationPolicy.
        :type: dict(str, str)
        """
        self._parameters = parameters

    @property
    def cache_key(self):
        """
        Gets the cache_key of this CustomAuthenticationPolicy.
        A list of keys from \"parameters\" attribute value whose values will be added to the cache key.


        :return: The cache_key of this CustomAuthenticationPolicy.
        :rtype: list[str]
        """
        return self._cache_key

    @cache_key.setter
    def cache_key(self, cache_key):
        """
        Sets the cache_key of this CustomAuthenticationPolicy.
        A list of keys from \"parameters\" attribute value whose values will be added to the cache key.


        :param cache_key: The cache_key of this CustomAuthenticationPolicy.
        :type: list[str]
        """
        self._cache_key = cache_key

    @property
    def validation_failure_policy(self):
        """
        Gets the validation_failure_policy of this CustomAuthenticationPolicy.

        :return: The validation_failure_policy of this CustomAuthenticationPolicy.
        :rtype: oci.apigateway.models.ValidationFailurePolicy
        """
        return self._validation_failure_policy

    @validation_failure_policy.setter
    def validation_failure_policy(self, validation_failure_policy):
        """
        Sets the validation_failure_policy of this CustomAuthenticationPolicy.

        :param validation_failure_policy: The validation_failure_policy of this CustomAuthenticationPolicy.
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
