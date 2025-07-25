# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Streaming(object):
    """
    Definition of the Stream.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Streaming object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param stream_id:
            The value to assign to the stream_id property of this Streaming.
        :type stream_id: str

        """
        self.swagger_types = {
            'stream_id': 'str'
        }
        self.attribute_map = {
            'stream_id': 'streamId'
        }
        self._stream_id = None

    @property
    def stream_id(self):
        """
        Gets the stream_id of this Streaming.
        Stream Id.


        :return: The stream_id of this Streaming.
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        """
        Sets the stream_id of this Streaming.
        Stream Id.


        :param stream_id: The stream_id of this Streaming.
        :type: str
        """
        self._stream_id = stream_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
