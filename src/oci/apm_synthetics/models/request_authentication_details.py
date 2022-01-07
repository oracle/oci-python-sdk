# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RequestAuthenticationDetails(object):
    """
    Details for request HTTP authentication.
    """

    #: A constant which can be used with the oauth_scheme property of a RequestAuthenticationDetails.
    #: This constant has a value of "NONE"
    OAUTH_SCHEME_NONE = "NONE"

    #: A constant which can be used with the oauth_scheme property of a RequestAuthenticationDetails.
    #: This constant has a value of "BASIC"
    OAUTH_SCHEME_BASIC = "BASIC"

    #: A constant which can be used with the auth_request_method property of a RequestAuthenticationDetails.
    #: This constant has a value of "GET"
    AUTH_REQUEST_METHOD_GET = "GET"

    #: A constant which can be used with the auth_request_method property of a RequestAuthenticationDetails.
    #: This constant has a value of "POST"
    AUTH_REQUEST_METHOD_POST = "POST"

    def __init__(self, **kwargs):
        """
        Initializes a new RequestAuthenticationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param oauth_scheme:
            The value to assign to the oauth_scheme property of this RequestAuthenticationDetails.
            Allowed values for this property are: "NONE", "BASIC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type oauth_scheme: str

        :param auth_user_name:
            The value to assign to the auth_user_name property of this RequestAuthenticationDetails.
        :type auth_user_name: str

        :param auth_user_password:
            The value to assign to the auth_user_password property of this RequestAuthenticationDetails.
        :type auth_user_password: str

        :param auth_token:
            The value to assign to the auth_token property of this RequestAuthenticationDetails.
        :type auth_token: str

        :param auth_url:
            The value to assign to the auth_url property of this RequestAuthenticationDetails.
        :type auth_url: str

        :param auth_headers:
            The value to assign to the auth_headers property of this RequestAuthenticationDetails.
        :type auth_headers: list[oci.apm_synthetics.models.Header]

        :param auth_request_method:
            The value to assign to the auth_request_method property of this RequestAuthenticationDetails.
            Allowed values for this property are: "GET", "POST", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type auth_request_method: str

        :param auth_request_post_body:
            The value to assign to the auth_request_post_body property of this RequestAuthenticationDetails.
        :type auth_request_post_body: str

        """
        self.swagger_types = {
            'oauth_scheme': 'str',
            'auth_user_name': 'str',
            'auth_user_password': 'str',
            'auth_token': 'str',
            'auth_url': 'str',
            'auth_headers': 'list[Header]',
            'auth_request_method': 'str',
            'auth_request_post_body': 'str'
        }

        self.attribute_map = {
            'oauth_scheme': 'oauthScheme',
            'auth_user_name': 'authUserName',
            'auth_user_password': 'authUserPassword',
            'auth_token': 'authToken',
            'auth_url': 'authUrl',
            'auth_headers': 'authHeaders',
            'auth_request_method': 'authRequestMethod',
            'auth_request_post_body': 'authRequestPostBody'
        }

        self._oauth_scheme = None
        self._auth_user_name = None
        self._auth_user_password = None
        self._auth_token = None
        self._auth_url = None
        self._auth_headers = None
        self._auth_request_method = None
        self._auth_request_post_body = None

    @property
    def oauth_scheme(self):
        """
        Gets the oauth_scheme of this RequestAuthenticationDetails.
        Request http oauth scheme.

        Allowed values for this property are: "NONE", "BASIC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The oauth_scheme of this RequestAuthenticationDetails.
        :rtype: str
        """
        return self._oauth_scheme

    @oauth_scheme.setter
    def oauth_scheme(self, oauth_scheme):
        """
        Sets the oauth_scheme of this RequestAuthenticationDetails.
        Request http oauth scheme.


        :param oauth_scheme: The oauth_scheme of this RequestAuthenticationDetails.
        :type: str
        """
        allowed_values = ["NONE", "BASIC"]
        if not value_allowed_none_or_none_sentinel(oauth_scheme, allowed_values):
            oauth_scheme = 'UNKNOWN_ENUM_VALUE'
        self._oauth_scheme = oauth_scheme

    @property
    def auth_user_name(self):
        """
        Gets the auth_user_name of this RequestAuthenticationDetails.
        Username for authentication.


        :return: The auth_user_name of this RequestAuthenticationDetails.
        :rtype: str
        """
        return self._auth_user_name

    @auth_user_name.setter
    def auth_user_name(self, auth_user_name):
        """
        Sets the auth_user_name of this RequestAuthenticationDetails.
        Username for authentication.


        :param auth_user_name: The auth_user_name of this RequestAuthenticationDetails.
        :type: str
        """
        self._auth_user_name = auth_user_name

    @property
    def auth_user_password(self):
        """
        Gets the auth_user_password of this RequestAuthenticationDetails.
        User password for authentication.


        :return: The auth_user_password of this RequestAuthenticationDetails.
        :rtype: str
        """
        return self._auth_user_password

    @auth_user_password.setter
    def auth_user_password(self, auth_user_password):
        """
        Sets the auth_user_password of this RequestAuthenticationDetails.
        User password for authentication.


        :param auth_user_password: The auth_user_password of this RequestAuthenticationDetails.
        :type: str
        """
        self._auth_user_password = auth_user_password

    @property
    def auth_token(self):
        """
        Gets the auth_token of this RequestAuthenticationDetails.
        Authentication token.


        :return: The auth_token of this RequestAuthenticationDetails.
        :rtype: str
        """
        return self._auth_token

    @auth_token.setter
    def auth_token(self, auth_token):
        """
        Sets the auth_token of this RequestAuthenticationDetails.
        Authentication token.


        :param auth_token: The auth_token of this RequestAuthenticationDetails.
        :type: str
        """
        self._auth_token = auth_token

    @property
    def auth_url(self):
        """
        Gets the auth_url of this RequestAuthenticationDetails.
        URL to get authetication token.


        :return: The auth_url of this RequestAuthenticationDetails.
        :rtype: str
        """
        return self._auth_url

    @auth_url.setter
    def auth_url(self, auth_url):
        """
        Sets the auth_url of this RequestAuthenticationDetails.
        URL to get authetication token.


        :param auth_url: The auth_url of this RequestAuthenticationDetails.
        :type: str
        """
        self._auth_url = auth_url

    @property
    def auth_headers(self):
        """
        Gets the auth_headers of this RequestAuthenticationDetails.
        List of authentication headers. Example: `[{\"headerName\": \"content-type\", \"headerValue\":\"json\"}]`


        :return: The auth_headers of this RequestAuthenticationDetails.
        :rtype: list[oci.apm_synthetics.models.Header]
        """
        return self._auth_headers

    @auth_headers.setter
    def auth_headers(self, auth_headers):
        """
        Sets the auth_headers of this RequestAuthenticationDetails.
        List of authentication headers. Example: `[{\"headerName\": \"content-type\", \"headerValue\":\"json\"}]`


        :param auth_headers: The auth_headers of this RequestAuthenticationDetails.
        :type: list[oci.apm_synthetics.models.Header]
        """
        self._auth_headers = auth_headers

    @property
    def auth_request_method(self):
        """
        Gets the auth_request_method of this RequestAuthenticationDetails.
        Request method.

        Allowed values for this property are: "GET", "POST", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The auth_request_method of this RequestAuthenticationDetails.
        :rtype: str
        """
        return self._auth_request_method

    @auth_request_method.setter
    def auth_request_method(self, auth_request_method):
        """
        Sets the auth_request_method of this RequestAuthenticationDetails.
        Request method.


        :param auth_request_method: The auth_request_method of this RequestAuthenticationDetails.
        :type: str
        """
        allowed_values = ["GET", "POST"]
        if not value_allowed_none_or_none_sentinel(auth_request_method, allowed_values):
            auth_request_method = 'UNKNOWN_ENUM_VALUE'
        self._auth_request_method = auth_request_method

    @property
    def auth_request_post_body(self):
        """
        Gets the auth_request_post_body of this RequestAuthenticationDetails.
        Request post body.


        :return: The auth_request_post_body of this RequestAuthenticationDetails.
        :rtype: str
        """
        return self._auth_request_post_body

    @auth_request_post_body.setter
    def auth_request_post_body(self, auth_request_post_body):
        """
        Sets the auth_request_post_body of this RequestAuthenticationDetails.
        Request post body.


        :param auth_request_post_body: The auth_request_post_body of this RequestAuthenticationDetails.
        :type: str
        """
        self._auth_request_post_body = auth_request_post_body

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
