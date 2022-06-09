# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResponseCompressionPolicy(object):
    """
    An object that specifies a compression policy for HTTP response from ENABLEMENT POINT to the client.

    This compression policy can be used to enable support for HTTP response compression algorithms like gzip and
    configure the conditions of when a compression algorithm will be used.

    HTTP responses will only be compressed if the client indicates support for one of the enabled compression
    algorithms via the \"Accept-Encoding\" request header.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ResponseCompressionPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param gzip_compression:
            The value to assign to the gzip_compression property of this ResponseCompressionPolicy.
        :type gzip_compression: oci.waa.models.GzipCompressionPolicy

        """
        self.swagger_types = {
            'gzip_compression': 'GzipCompressionPolicy'
        }

        self.attribute_map = {
            'gzip_compression': 'gzipCompression'
        }

        self._gzip_compression = None

    @property
    def gzip_compression(self):
        """
        Gets the gzip_compression of this ResponseCompressionPolicy.

        :return: The gzip_compression of this ResponseCompressionPolicy.
        :rtype: oci.waa.models.GzipCompressionPolicy
        """
        return self._gzip_compression

    @gzip_compression.setter
    def gzip_compression(self, gzip_compression):
        """
        Sets the gzip_compression of this ResponseCompressionPolicy.

        :param gzip_compression: The gzip_compression of this ResponseCompressionPolicy.
        :type: oci.waa.models.GzipCompressionPolicy
        """
        self._gzip_compression = gzip_compression

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
