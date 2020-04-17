# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LBCookieSessionPersistenceConfigurationDetails(object):
    """
    The configuration details for implementing load balancer cookie session persistence (LB cookie stickiness).

    Session persistence enables the Load Balancing service to direct all requests that originate from a single logical
    client to a single backend web server. For more information, see
    `Session Persistence`__.

    When you configure LB cookie stickiness, the load balancer inserts a cookie into the response. The parameters configured
    in the cookie enable session stickiness. This method is useful when you have applications and Web backend services
    that cannot generate their own cookies.

    Path route rules take precedence to determine the target backend server. The load balancer verifies that session stickiness
    is enabled for the backend server and that the cookie configuration (domain, path, and cookie hash) is valid for the
    target. The system ignores invalid cookies.

    To disable LB cookie stickiness on a running load balancer, use the
    :func:`update_backend_set` operation and specify `null` for the
    `LBCookieSessionPersistenceConfigurationDetails` object.

    Example: `LBCookieSessionPersistenceConfigurationDetails: null`

    **Note:** `SessionPersistenceConfigurationDetails` (application cookie stickiness) and `LBCookieSessionPersistenceConfigurationDetails`
    (LB cookie stickiness) are mutually exclusive. An error results if you try to enable both types of session persistence.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

    __ https://docs.cloud.oracle.com/Content/Balance/Reference/sessionpersistence.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LBCookieSessionPersistenceConfigurationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cookie_name:
            The value to assign to the cookie_name property of this LBCookieSessionPersistenceConfigurationDetails.
        :type cookie_name: str

        :param disable_fallback:
            The value to assign to the disable_fallback property of this LBCookieSessionPersistenceConfigurationDetails.
        :type disable_fallback: bool

        :param domain:
            The value to assign to the domain property of this LBCookieSessionPersistenceConfigurationDetails.
        :type domain: str

        :param path:
            The value to assign to the path property of this LBCookieSessionPersistenceConfigurationDetails.
        :type path: str

        :param max_age_in_seconds:
            The value to assign to the max_age_in_seconds property of this LBCookieSessionPersistenceConfigurationDetails.
        :type max_age_in_seconds: int

        :param is_secure:
            The value to assign to the is_secure property of this LBCookieSessionPersistenceConfigurationDetails.
        :type is_secure: bool

        :param is_http_only:
            The value to assign to the is_http_only property of this LBCookieSessionPersistenceConfigurationDetails.
        :type is_http_only: bool

        """
        self.swagger_types = {
            'cookie_name': 'str',
            'disable_fallback': 'bool',
            'domain': 'str',
            'path': 'str',
            'max_age_in_seconds': 'int',
            'is_secure': 'bool',
            'is_http_only': 'bool'
        }

        self.attribute_map = {
            'cookie_name': 'cookieName',
            'disable_fallback': 'disableFallback',
            'domain': 'domain',
            'path': 'path',
            'max_age_in_seconds': 'maxAgeInSeconds',
            'is_secure': 'isSecure',
            'is_http_only': 'isHttpOnly'
        }

        self._cookie_name = None
        self._disable_fallback = None
        self._domain = None
        self._path = None
        self._max_age_in_seconds = None
        self._is_secure = None
        self._is_http_only = None

    @property
    def cookie_name(self):
        """
        Gets the cookie_name of this LBCookieSessionPersistenceConfigurationDetails.
        The name of the cookie inserted by the load balancer. If this field is not configured, the cookie name defaults
        to \"X-Oracle-BMC-LBS-Route\".

        Example: `example_cookie`

        **Notes:**

        *  Ensure that the cookie name used at the backend application servers is different from the cookie name used
           at the load balancer. To minimize the chance of name collision, Oracle recommends that you use a prefix
           such as \"X-Oracle-OCI-\" for this field.

        *  If a backend server and the load balancer both insert cookies with the same name, the client or browser
           behavior can vary depending on the domain and path values associated with the cookie. If the name, domain,
           and path values of the `Set-cookie` generated by a backend server and the `Set-cookie` generated by the
           load balancer are all the same, the client or browser treats them as one cookie and returns only one of
           the cookie values in subsequent requests. If both `Set-cookie` names are the same, but the domain and path
           names are different, the client or browser treats them as two different cookies.


        :return: The cookie_name of this LBCookieSessionPersistenceConfigurationDetails.
        :rtype: str
        """
        return self._cookie_name

    @cookie_name.setter
    def cookie_name(self, cookie_name):
        """
        Sets the cookie_name of this LBCookieSessionPersistenceConfigurationDetails.
        The name of the cookie inserted by the load balancer. If this field is not configured, the cookie name defaults
        to \"X-Oracle-BMC-LBS-Route\".

        Example: `example_cookie`

        **Notes:**

        *  Ensure that the cookie name used at the backend application servers is different from the cookie name used
           at the load balancer. To minimize the chance of name collision, Oracle recommends that you use a prefix
           such as \"X-Oracle-OCI-\" for this field.

        *  If a backend server and the load balancer both insert cookies with the same name, the client or browser
           behavior can vary depending on the domain and path values associated with the cookie. If the name, domain,
           and path values of the `Set-cookie` generated by a backend server and the `Set-cookie` generated by the
           load balancer are all the same, the client or browser treats them as one cookie and returns only one of
           the cookie values in subsequent requests. If both `Set-cookie` names are the same, but the domain and path
           names are different, the client or browser treats them as two different cookies.


        :param cookie_name: The cookie_name of this LBCookieSessionPersistenceConfigurationDetails.
        :type: str
        """
        self._cookie_name = cookie_name

    @property
    def disable_fallback(self):
        """
        Gets the disable_fallback of this LBCookieSessionPersistenceConfigurationDetails.
        Whether the load balancer is prevented from directing traffic from a persistent session client to
        a different backend server if the original server is unavailable. Defaults to false.

        Example: `false`


        :return: The disable_fallback of this LBCookieSessionPersistenceConfigurationDetails.
        :rtype: bool
        """
        return self._disable_fallback

    @disable_fallback.setter
    def disable_fallback(self, disable_fallback):
        """
        Sets the disable_fallback of this LBCookieSessionPersistenceConfigurationDetails.
        Whether the load balancer is prevented from directing traffic from a persistent session client to
        a different backend server if the original server is unavailable. Defaults to false.

        Example: `false`


        :param disable_fallback: The disable_fallback of this LBCookieSessionPersistenceConfigurationDetails.
        :type: bool
        """
        self._disable_fallback = disable_fallback

    @property
    def domain(self):
        """
        Gets the domain of this LBCookieSessionPersistenceConfigurationDetails.
        The domain in which the cookie is valid. The `Set-cookie` header inserted by the load balancer contains a
        domain attribute with the specified value.

        This attribute has no default value. If you do not specify a value, the load balancer does not insert the domain
        attribute into the `Set-cookie` header.

        **Notes:**

        *  `RFC 6265 - HTTP State Management Mechanism`__ describes client and
           browser behavior when the domain attribute is present or not present in the `Set-cookie` header.

           If the value of the `Domain` attribute is `example.com` in the `Set-cookie` header, the client includes
           the same cookie in the `Cookie` header when making HTTP requests to `example.com`, `www.example.com`, and
           `www.abc.example.com`. If the `Domain` attribute is not present, the client returns the cookie only for
           the domain to which the original request was made.

        *  Ensure that this attribute specifies the correct domain value. If the `Domain` attribute in the `Set-cookie`
           header does not include the domain to which the original request was made, the client or browser might reject
           the cookie. As specified in RFC 6265, the client accepts a cookie with the `Domain` attribute value `example.com`
           or `www.example.com` sent from `www.example.com`. It does not accept a cookie with the `Domain` attribute
           `abc.example.com` or `www.abc.example.com` sent from `www.example.com`.

        Example: `example.com`

        __ https://www.ietf.org/rfc/rfc6265.txt


        :return: The domain of this LBCookieSessionPersistenceConfigurationDetails.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this LBCookieSessionPersistenceConfigurationDetails.
        The domain in which the cookie is valid. The `Set-cookie` header inserted by the load balancer contains a
        domain attribute with the specified value.

        This attribute has no default value. If you do not specify a value, the load balancer does not insert the domain
        attribute into the `Set-cookie` header.

        **Notes:**

        *  `RFC 6265 - HTTP State Management Mechanism`__ describes client and
           browser behavior when the domain attribute is present or not present in the `Set-cookie` header.

           If the value of the `Domain` attribute is `example.com` in the `Set-cookie` header, the client includes
           the same cookie in the `Cookie` header when making HTTP requests to `example.com`, `www.example.com`, and
           `www.abc.example.com`. If the `Domain` attribute is not present, the client returns the cookie only for
           the domain to which the original request was made.

        *  Ensure that this attribute specifies the correct domain value. If the `Domain` attribute in the `Set-cookie`
           header does not include the domain to which the original request was made, the client or browser might reject
           the cookie. As specified in RFC 6265, the client accepts a cookie with the `Domain` attribute value `example.com`
           or `www.example.com` sent from `www.example.com`. It does not accept a cookie with the `Domain` attribute
           `abc.example.com` or `www.abc.example.com` sent from `www.example.com`.

        Example: `example.com`

        __ https://www.ietf.org/rfc/rfc6265.txt


        :param domain: The domain of this LBCookieSessionPersistenceConfigurationDetails.
        :type: str
        """
        self._domain = domain

    @property
    def path(self):
        """
        Gets the path of this LBCookieSessionPersistenceConfigurationDetails.
        The path in which the cookie is valid. The `Set-cookie header` inserted by the load balancer contains a `Path`
        attribute with the specified value.

        Clients include the cookie in an HTTP request only if the path portion of the request-uri matches, or is a
        subdirectory of, the cookie's `Path` attribute.

        The default value is `/`.

        Example: `/example`


        :return: The path of this LBCookieSessionPersistenceConfigurationDetails.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this LBCookieSessionPersistenceConfigurationDetails.
        The path in which the cookie is valid. The `Set-cookie header` inserted by the load balancer contains a `Path`
        attribute with the specified value.

        Clients include the cookie in an HTTP request only if the path portion of the request-uri matches, or is a
        subdirectory of, the cookie's `Path` attribute.

        The default value is `/`.

        Example: `/example`


        :param path: The path of this LBCookieSessionPersistenceConfigurationDetails.
        :type: str
        """
        self._path = path

    @property
    def max_age_in_seconds(self):
        """
        Gets the max_age_in_seconds of this LBCookieSessionPersistenceConfigurationDetails.
        The amount of time the cookie remains valid. The `Set-cookie` header inserted by the load balancer contains
        a `Max-Age` attribute with the specified value.

        The specified value must be at least one second. There is no default value for this attribute. If you do not
        specify a value, the load balancer does not include the `Max-Age` attribute in the `Set-cookie` header. In
        most cases, the client or browser retains the cookie until the current session ends, as defined by the client.

        Example: `3600`


        :return: The max_age_in_seconds of this LBCookieSessionPersistenceConfigurationDetails.
        :rtype: int
        """
        return self._max_age_in_seconds

    @max_age_in_seconds.setter
    def max_age_in_seconds(self, max_age_in_seconds):
        """
        Sets the max_age_in_seconds of this LBCookieSessionPersistenceConfigurationDetails.
        The amount of time the cookie remains valid. The `Set-cookie` header inserted by the load balancer contains
        a `Max-Age` attribute with the specified value.

        The specified value must be at least one second. There is no default value for this attribute. If you do not
        specify a value, the load balancer does not include the `Max-Age` attribute in the `Set-cookie` header. In
        most cases, the client or browser retains the cookie until the current session ends, as defined by the client.

        Example: `3600`


        :param max_age_in_seconds: The max_age_in_seconds of this LBCookieSessionPersistenceConfigurationDetails.
        :type: int
        """
        self._max_age_in_seconds = max_age_in_seconds

    @property
    def is_secure(self):
        """
        Gets the is_secure of this LBCookieSessionPersistenceConfigurationDetails.
        Whether the `Set-cookie` header should contain the `Secure` attribute. If `true`, the `Set-cookie` header
        inserted by the load balancer contains the `Secure` attribute, which directs the client or browser to send the
        cookie only using a secure protocol.

        **Note:** If you set this field to `true`, you cannot associate the corresponding backend set with an HTTP
        listener.

        Example: `true`


        :return: The is_secure of this LBCookieSessionPersistenceConfigurationDetails.
        :rtype: bool
        """
        return self._is_secure

    @is_secure.setter
    def is_secure(self, is_secure):
        """
        Sets the is_secure of this LBCookieSessionPersistenceConfigurationDetails.
        Whether the `Set-cookie` header should contain the `Secure` attribute. If `true`, the `Set-cookie` header
        inserted by the load balancer contains the `Secure` attribute, which directs the client or browser to send the
        cookie only using a secure protocol.

        **Note:** If you set this field to `true`, you cannot associate the corresponding backend set with an HTTP
        listener.

        Example: `true`


        :param is_secure: The is_secure of this LBCookieSessionPersistenceConfigurationDetails.
        :type: bool
        """
        self._is_secure = is_secure

    @property
    def is_http_only(self):
        """
        Gets the is_http_only of this LBCookieSessionPersistenceConfigurationDetails.
        Whether the `Set-cookie` header should contain the `HttpOnly` attribute. If `true`, the `Set-cookie` header
        inserted by the load balancer contains the `HttpOnly` attribute, which limits the scope of the cookie to HTTP
        requests. This attribute directs the client or browser to omit the cookie when providing access to cookies
        through non-HTTP APIs. For example, it restricts the cookie from JavaScript channels.

        Example: `true`


        :return: The is_http_only of this LBCookieSessionPersistenceConfigurationDetails.
        :rtype: bool
        """
        return self._is_http_only

    @is_http_only.setter
    def is_http_only(self, is_http_only):
        """
        Sets the is_http_only of this LBCookieSessionPersistenceConfigurationDetails.
        Whether the `Set-cookie` header should contain the `HttpOnly` attribute. If `true`, the `Set-cookie` header
        inserted by the load balancer contains the `HttpOnly` attribute, which limits the scope of the cookie to HTTP
        requests. This attribute directs the client or browser to omit the cookie when providing access to cookies
        through non-HTTP APIs. For example, it restricts the cookie from JavaScript channels.

        Example: `true`


        :param is_http_only: The is_http_only of this LBCookieSessionPersistenceConfigurationDetails.
        :type: bool
        """
        self._is_http_only = is_http_only

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
