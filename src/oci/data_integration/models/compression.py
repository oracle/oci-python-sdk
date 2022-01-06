# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Compression(object):
    """
    The optional compression configuration.
    """

    #: A constant which can be used with the codec property of a Compression.
    #: This constant has a value of "NONE"
    CODEC_NONE = "NONE"

    #: A constant which can be used with the codec property of a Compression.
    #: This constant has a value of "AUTO"
    CODEC_AUTO = "AUTO"

    #: A constant which can be used with the codec property of a Compression.
    #: This constant has a value of "GZIP"
    CODEC_GZIP = "GZIP"

    #: A constant which can be used with the codec property of a Compression.
    #: This constant has a value of "BZIP2"
    CODEC_BZIP2 = "BZIP2"

    #: A constant which can be used with the codec property of a Compression.
    #: This constant has a value of "DEFLATE"
    CODEC_DEFLATE = "DEFLATE"

    #: A constant which can be used with the codec property of a Compression.
    #: This constant has a value of "LZ4"
    CODEC_LZ4 = "LZ4"

    #: A constant which can be used with the codec property of a Compression.
    #: This constant has a value of "SNAPPY"
    CODEC_SNAPPY = "SNAPPY"

    def __init__(self, **kwargs):
        """
        Initializes a new Compression object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param codec:
            The value to assign to the codec property of this Compression.
            Allowed values for this property are: "NONE", "AUTO", "GZIP", "BZIP2", "DEFLATE", "LZ4", "SNAPPY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type codec: str

        """
        self.swagger_types = {
            'codec': 'str'
        }

        self.attribute_map = {
            'codec': 'codec'
        }

        self._codec = None

    @property
    def codec(self):
        """
        Gets the codec of this Compression.
        Compression algorithm

        Allowed values for this property are: "NONE", "AUTO", "GZIP", "BZIP2", "DEFLATE", "LZ4", "SNAPPY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The codec of this Compression.
        :rtype: str
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        """
        Sets the codec of this Compression.
        Compression algorithm


        :param codec: The codec of this Compression.
        :type: str
        """
        allowed_values = ["NONE", "AUTO", "GZIP", "BZIP2", "DEFLATE", "LZ4", "SNAPPY"]
        if not value_allowed_none_or_none_sentinel(codec, allowed_values):
            codec = 'UNKNOWN_ENUM_VALUE'
        self._codec = codec

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
