# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CorsPolicy(object):
    """
    Enable CORS (Cross-Origin-Resource-Sharing) request handling.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CorsPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param allowed_origins:
            The value to assign to the allowed_origins property of this CorsPolicy.
        :type allowed_origins: list[str]

        :param allowed_methods:
            The value to assign to the allowed_methods property of this CorsPolicy.
        :type allowed_methods: list[str]

        :param allowed_headers:
            The value to assign to the allowed_headers property of this CorsPolicy.
        :type allowed_headers: list[str]

        :param exposed_headers:
            The value to assign to the exposed_headers property of this CorsPolicy.
        :type exposed_headers: list[str]

        :param is_allow_credentials_enabled:
            The value to assign to the is_allow_credentials_enabled property of this CorsPolicy.
        :type is_allow_credentials_enabled: bool

        :param max_age_in_seconds:
            The value to assign to the max_age_in_seconds property of this CorsPolicy.
        :type max_age_in_seconds: int

        """
        self.swagger_types = {
            'allowed_origins': 'list[str]',
            'allowed_methods': 'list[str]',
            'allowed_headers': 'list[str]',
            'exposed_headers': 'list[str]',
            'is_allow_credentials_enabled': 'bool',
            'max_age_in_seconds': 'int'
        }

        self.attribute_map = {
            'allowed_origins': 'allowedOrigins',
            'allowed_methods': 'allowedMethods',
            'allowed_headers': 'allowedHeaders',
            'exposed_headers': 'exposedHeaders',
            'is_allow_credentials_enabled': 'isAllowCredentialsEnabled',
            'max_age_in_seconds': 'maxAgeInSeconds'
        }

        self._allowed_origins = None
        self._allowed_methods = None
        self._allowed_headers = None
        self._exposed_headers = None
        self._is_allow_credentials_enabled = None
        self._max_age_in_seconds = None

    @property
    def allowed_origins(self):
        """
        **[Required]** Gets the allowed_origins of this CorsPolicy.
        The list of allowed origins that the CORS handler will use to respond to CORS requests. The gateway will
        send the Access-Control-Allow-Origin header with the best origin match for the circumstances. '*' will match
        any origins, and 'null' will match queries from 'file:' origins. All other origins must be qualified with the
        scheme, full hostname, and port if necessary.


        :return: The allowed_origins of this CorsPolicy.
        :rtype: list[str]
        """
        return self._allowed_origins

    @allowed_origins.setter
    def allowed_origins(self, allowed_origins):
        """
        Sets the allowed_origins of this CorsPolicy.
        The list of allowed origins that the CORS handler will use to respond to CORS requests. The gateway will
        send the Access-Control-Allow-Origin header with the best origin match for the circumstances. '*' will match
        any origins, and 'null' will match queries from 'file:' origins. All other origins must be qualified with the
        scheme, full hostname, and port if necessary.


        :param allowed_origins: The allowed_origins of this CorsPolicy.
        :type: list[str]
        """
        self._allowed_origins = allowed_origins

    @property
    def allowed_methods(self):
        """
        Gets the allowed_methods of this CorsPolicy.
        The list of allowed HTTP methods that will be returned for the preflight OPTIONS request in the
        Access-Control-Allow-Methods header. '*' will allow all methods.


        :return: The allowed_methods of this CorsPolicy.
        :rtype: list[str]
        """
        return self._allowed_methods

    @allowed_methods.setter
    def allowed_methods(self, allowed_methods):
        """
        Sets the allowed_methods of this CorsPolicy.
        The list of allowed HTTP methods that will be returned for the preflight OPTIONS request in the
        Access-Control-Allow-Methods header. '*' will allow all methods.


        :param allowed_methods: The allowed_methods of this CorsPolicy.
        :type: list[str]
        """
        self._allowed_methods = allowed_methods

    @property
    def allowed_headers(self):
        """
        Gets the allowed_headers of this CorsPolicy.
        The list of headers that will be allowed from the client via the Access-Control-Allow-Headers header.
        '*' will allow all headers.


        :return: The allowed_headers of this CorsPolicy.
        :rtype: list[str]
        """
        return self._allowed_headers

    @allowed_headers.setter
    def allowed_headers(self, allowed_headers):
        """
        Sets the allowed_headers of this CorsPolicy.
        The list of headers that will be allowed from the client via the Access-Control-Allow-Headers header.
        '*' will allow all headers.


        :param allowed_headers: The allowed_headers of this CorsPolicy.
        :type: list[str]
        """
        self._allowed_headers = allowed_headers

    @property
    def exposed_headers(self):
        """
        Gets the exposed_headers of this CorsPolicy.
        The list of headers that the client will be allowed to see from the response as indicated by the
        Access-Control-Expose-Headers header. '*' will expose all headers.


        :return: The exposed_headers of this CorsPolicy.
        :rtype: list[str]
        """
        return self._exposed_headers

    @exposed_headers.setter
    def exposed_headers(self, exposed_headers):
        """
        Sets the exposed_headers of this CorsPolicy.
        The list of headers that the client will be allowed to see from the response as indicated by the
        Access-Control-Expose-Headers header. '*' will expose all headers.


        :param exposed_headers: The exposed_headers of this CorsPolicy.
        :type: list[str]
        """
        self._exposed_headers = exposed_headers

    @property
    def is_allow_credentials_enabled(self):
        """
        Gets the is_allow_credentials_enabled of this CorsPolicy.
        Whether to send the Access-Control-Allow-Credentials header to allow CORS requests with cookies.


        :return: The is_allow_credentials_enabled of this CorsPolicy.
        :rtype: bool
        """
        return self._is_allow_credentials_enabled

    @is_allow_credentials_enabled.setter
    def is_allow_credentials_enabled(self, is_allow_credentials_enabled):
        """
        Sets the is_allow_credentials_enabled of this CorsPolicy.
        Whether to send the Access-Control-Allow-Credentials header to allow CORS requests with cookies.


        :param is_allow_credentials_enabled: The is_allow_credentials_enabled of this CorsPolicy.
        :type: bool
        """
        self._is_allow_credentials_enabled = is_allow_credentials_enabled

    @property
    def max_age_in_seconds(self):
        """
        Gets the max_age_in_seconds of this CorsPolicy.
        The time in seconds for the client to cache preflight responses. This is sent as the Access-Control-Max-Age
        if greater than 0.


        :return: The max_age_in_seconds of this CorsPolicy.
        :rtype: int
        """
        return self._max_age_in_seconds

    @max_age_in_seconds.setter
    def max_age_in_seconds(self, max_age_in_seconds):
        """
        Sets the max_age_in_seconds of this CorsPolicy.
        The time in seconds for the client to cache preflight responses. This is sent as the Access-Control-Max-Age
        if greater than 0.


        :param max_age_in_seconds: The max_age_in_seconds of this CorsPolicy.
        :type: int
        """
        self._max_age_in_seconds = max_age_in_seconds

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
