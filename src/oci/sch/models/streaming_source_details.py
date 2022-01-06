# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .source_details import SourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StreamingSourceDetails(SourceDetails):
    """
    The Streaming source.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new StreamingSourceDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.sch.models.StreamingSourceDetails.kind` attribute
        of this class is ``streaming`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kind:
            The value to assign to the kind property of this StreamingSourceDetails.
            Allowed values for this property are: "logging", "streaming"
        :type kind: str

        :param stream_id:
            The value to assign to the stream_id property of this StreamingSourceDetails.
        :type stream_id: str

        :param cursor:
            The value to assign to the cursor property of this StreamingSourceDetails.
        :type cursor: oci.sch.models.StreamingCursorDetails

        """
        self.swagger_types = {
            'kind': 'str',
            'stream_id': 'str',
            'cursor': 'StreamingCursorDetails'
        }

        self.attribute_map = {
            'kind': 'kind',
            'stream_id': 'streamId',
            'cursor': 'cursor'
        }

        self._kind = None
        self._stream_id = None
        self._cursor = None
        self._kind = 'streaming'

    @property
    def stream_id(self):
        """
        **[Required]** Gets the stream_id of this StreamingSourceDetails.
        The `OCID`__ of the stream.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The stream_id of this StreamingSourceDetails.
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        """
        Sets the stream_id of this StreamingSourceDetails.
        The `OCID`__ of the stream.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param stream_id: The stream_id of this StreamingSourceDetails.
        :type: str
        """
        self._stream_id = stream_id

    @property
    def cursor(self):
        """
        Gets the cursor of this StreamingSourceDetails.

        :return: The cursor of this StreamingSourceDetails.
        :rtype: oci.sch.models.StreamingCursorDetails
        """
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        """
        Sets the cursor of this StreamingSourceDetails.

        :param cursor: The cursor of this StreamingSourceDetails.
        :type: oci.sch.models.StreamingCursorDetails
        """
        self._cursor = cursor

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
