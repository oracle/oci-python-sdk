# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResponseCachingPolicy(object):
    """
    An object that specifies an HTTP response caching policy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ResponseCachingPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_response_header_based_caching_enabled:
            The value to assign to the is_response_header_based_caching_enabled property of this ResponseCachingPolicy.
        :type is_response_header_based_caching_enabled: bool

        """
        self.swagger_types = {
            'is_response_header_based_caching_enabled': 'bool'
        }

        self.attribute_map = {
            'is_response_header_based_caching_enabled': 'isResponseHeaderBasedCachingEnabled'
        }

        self._is_response_header_based_caching_enabled = None

    @property
    def is_response_header_based_caching_enabled(self):
        """
        Gets the is_response_header_based_caching_enabled of this ResponseCachingPolicy.
        When false, responses will not be cached by the backend based on response headers.

        When true, responses that contain one of the supported cache control headers will be cached according to the
        values specified in the cache control headers.

        The \"X-Accel-Expires\" header field sets caching time of a response in seconds. The zero value disables
        caching for a response. If the value starts with the @ prefix, it sets an absolute time in seconds since
        Epoch, up to which the response may be cached.

        If the header does not include the \"X-Accel-Expires\" field, parameters of caching may be set in the header
        fields \"Expires\" or \"Cache-Control\".

        If the header includes the \"Set-Cookie\" field, such a response will not be cached.

        If the header includes the \"Vary\" field with the special value \"*\", such a response will not be cached. If the
        header includes the \"Vary\" field with another value, such a response will be cached taking into account the
        corresponding request header fields.


        :return: The is_response_header_based_caching_enabled of this ResponseCachingPolicy.
        :rtype: bool
        """
        return self._is_response_header_based_caching_enabled

    @is_response_header_based_caching_enabled.setter
    def is_response_header_based_caching_enabled(self, is_response_header_based_caching_enabled):
        """
        Sets the is_response_header_based_caching_enabled of this ResponseCachingPolicy.
        When false, responses will not be cached by the backend based on response headers.

        When true, responses that contain one of the supported cache control headers will be cached according to the
        values specified in the cache control headers.

        The \"X-Accel-Expires\" header field sets caching time of a response in seconds. The zero value disables
        caching for a response. If the value starts with the @ prefix, it sets an absolute time in seconds since
        Epoch, up to which the response may be cached.

        If the header does not include the \"X-Accel-Expires\" field, parameters of caching may be set in the header
        fields \"Expires\" or \"Cache-Control\".

        If the header includes the \"Set-Cookie\" field, such a response will not be cached.

        If the header includes the \"Vary\" field with the special value \"*\", such a response will not be cached. If the
        header includes the \"Vary\" field with another value, such a response will be cached taking into account the
        corresponding request header fields.


        :param is_response_header_based_caching_enabled: The is_response_header_based_caching_enabled of this ResponseCachingPolicy.
        :type: bool
        """
        self._is_response_header_based_caching_enabled = is_response_header_based_caching_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
