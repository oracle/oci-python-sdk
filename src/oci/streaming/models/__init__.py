# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from .change_stream_compartment_details import ChangeStreamCompartmentDetails
from .create_cursor_details import CreateCursorDetails
from .create_group_cursor_details import CreateGroupCursorDetails
from .create_stream_details import CreateStreamDetails
from .cursor import Cursor
from .group import Group
from .message import Message
from .partition_reservation import PartitionReservation
from .put_messages_details import PutMessagesDetails
from .put_messages_details_entry import PutMessagesDetailsEntry
from .put_messages_result import PutMessagesResult
from .put_messages_result_entry import PutMessagesResultEntry
from .stream import Stream
from .stream_summary import StreamSummary
from .update_group_details import UpdateGroupDetails
from .update_stream_details import UpdateStreamDetails

# Maps type names to classes for streaming services.
streaming_type_mapping = {
    "ChangeStreamCompartmentDetails": ChangeStreamCompartmentDetails,
    "CreateCursorDetails": CreateCursorDetails,
    "CreateGroupCursorDetails": CreateGroupCursorDetails,
    "CreateStreamDetails": CreateStreamDetails,
    "Cursor": Cursor,
    "Group": Group,
    "Message": Message,
    "PartitionReservation": PartitionReservation,
    "PutMessagesDetails": PutMessagesDetails,
    "PutMessagesDetailsEntry": PutMessagesDetailsEntry,
    "PutMessagesResult": PutMessagesResult,
    "PutMessagesResultEntry": PutMessagesResultEntry,
    "Stream": Stream,
    "StreamSummary": StreamSummary,
    "UpdateGroupDetails": UpdateGroupDetails,
    "UpdateStreamDetails": UpdateStreamDetails
}
