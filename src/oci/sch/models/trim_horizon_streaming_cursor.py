# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .streaming_cursor_details import StreamingCursorDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TrimHorizonStreamingCursor(StreamingCursorDetails):
    """
    `TRIM_HORIZON` cursor type. Sets the starting point for consuming the stream at the oldest available message in the stream. For more information about Streaming cursors, see `Using Cursors`__.

    __ https://docs.cloud.oracle.com/iaas/Content/Streaming/Tasks/using_a_single_consumer.htm#usingcursors
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TrimHorizonStreamingCursor object with values from keyword arguments. The default value of the :py:attr:`~oci.sch.models.TrimHorizonStreamingCursor.kind` attribute
        of this class is ``TRIM_HORIZON`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kind:
            The value to assign to the kind property of this TrimHorizonStreamingCursor.
            Allowed values for this property are: "LATEST", "TRIM_HORIZON"
        :type kind: str

        """
        self.swagger_types = {
            'kind': 'str'
        }

        self.attribute_map = {
            'kind': 'kind'
        }

        self._kind = None
        self._kind = 'TRIM_HORIZON'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
