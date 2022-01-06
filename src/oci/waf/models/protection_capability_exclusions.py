# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProtectionCapabilityExclusions(object):
    """
    Identifies specific HTTP message parameters to exclude from inspection by a protection capability.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ProtectionCapabilityExclusions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param request_cookies:
            The value to assign to the request_cookies property of this ProtectionCapabilityExclusions.
        :type request_cookies: list[str]

        :param args:
            The value to assign to the args property of this ProtectionCapabilityExclusions.
        :type args: list[str]

        """
        self.swagger_types = {
            'request_cookies': 'list[str]',
            'args': 'list[str]'
        }

        self.attribute_map = {
            'request_cookies': 'requestCookies',
            'args': 'args'
        }

        self._request_cookies = None
        self._args = None

    @property
    def request_cookies(self):
        """
        Gets the request_cookies of this ProtectionCapabilityExclusions.
        List of HTTP request cookie values (by cookie name) to exclude from inspecting.
        Example: If we have cookie 'cookieName=cookieValue' and requestCookies=['cookieName'], both 'cookieName' and 'cookieValue' will not be inspected.


        :return: The request_cookies of this ProtectionCapabilityExclusions.
        :rtype: list[str]
        """
        return self._request_cookies

    @request_cookies.setter
    def request_cookies(self, request_cookies):
        """
        Sets the request_cookies of this ProtectionCapabilityExclusions.
        List of HTTP request cookie values (by cookie name) to exclude from inspecting.
        Example: If we have cookie 'cookieName=cookieValue' and requestCookies=['cookieName'], both 'cookieName' and 'cookieValue' will not be inspected.


        :param request_cookies: The request_cookies of this ProtectionCapabilityExclusions.
        :type: list[str]
        """
        self._request_cookies = request_cookies

    @property
    def args(self):
        """
        Gets the args of this ProtectionCapabilityExclusions.
        List of URL query parameter values from form-urlencoded XML, JSON, AMP, or POST payloads to exclude from inspecting.
        Example: If we have query parameter 'argumentName=argumentValue' and args=['argumentName'], both 'argumentName' and 'argumentValue' will not be inspected.


        :return: The args of this ProtectionCapabilityExclusions.
        :rtype: list[str]
        """
        return self._args

    @args.setter
    def args(self, args):
        """
        Sets the args of this ProtectionCapabilityExclusions.
        List of URL query parameter values from form-urlencoded XML, JSON, AMP, or POST payloads to exclude from inspecting.
        Example: If we have query parameter 'argumentName=argumentValue' and args=['argumentName'], both 'argumentName' and 'argumentValue' will not be inspected.


        :param args: The args of this ProtectionCapabilityExclusions.
        :type: list[str]
        """
        self._args = args

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
