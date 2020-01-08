# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from .archiver import Archiver
from .archiver_error import ArchiverError
from .change_connect_harness_compartment_details import ChangeConnectHarnessCompartmentDetails
from .change_stream_compartment_details import ChangeStreamCompartmentDetails
from .change_stream_pool_compartment_details import ChangeStreamPoolCompartmentDetails
from .connect_harness import ConnectHarness
from .connect_harness_summary import ConnectHarnessSummary
from .create_archiver_details import CreateArchiverDetails
from .create_connect_harness_details import CreateConnectHarnessDetails
from .create_cursor_details import CreateCursorDetails
from .create_group_cursor_details import CreateGroupCursorDetails
from .create_stream_details import CreateStreamDetails
from .create_stream_pool_details import CreateStreamPoolDetails
from .cursor import Cursor
from .group import Group
from .kafka_settings import KafkaSettings
from .message import Message
from .partition_reservation import PartitionReservation
from .put_messages_details import PutMessagesDetails
from .put_messages_details_entry import PutMessagesDetailsEntry
from .put_messages_result import PutMessagesResult
from .put_messages_result_entry import PutMessagesResultEntry
from .stream import Stream
from .stream_pool import StreamPool
from .stream_pool_summary import StreamPoolSummary
from .stream_summary import StreamSummary
from .update_archiver_details import UpdateArchiverDetails
from .update_connect_harness_details import UpdateConnectHarnessDetails
from .update_group_details import UpdateGroupDetails
from .update_stream_details import UpdateStreamDetails
from .update_stream_pool_details import UpdateStreamPoolDetails

# Maps type names to classes for streaming services.
streaming_type_mapping = {
    "Archiver": Archiver,
    "ArchiverError": ArchiverError,
    "ChangeConnectHarnessCompartmentDetails": ChangeConnectHarnessCompartmentDetails,
    "ChangeStreamCompartmentDetails": ChangeStreamCompartmentDetails,
    "ChangeStreamPoolCompartmentDetails": ChangeStreamPoolCompartmentDetails,
    "ConnectHarness": ConnectHarness,
    "ConnectHarnessSummary": ConnectHarnessSummary,
    "CreateArchiverDetails": CreateArchiverDetails,
    "CreateConnectHarnessDetails": CreateConnectHarnessDetails,
    "CreateCursorDetails": CreateCursorDetails,
    "CreateGroupCursorDetails": CreateGroupCursorDetails,
    "CreateStreamDetails": CreateStreamDetails,
    "CreateStreamPoolDetails": CreateStreamPoolDetails,
    "Cursor": Cursor,
    "Group": Group,
    "KafkaSettings": KafkaSettings,
    "Message": Message,
    "PartitionReservation": PartitionReservation,
    "PutMessagesDetails": PutMessagesDetails,
    "PutMessagesDetailsEntry": PutMessagesDetailsEntry,
    "PutMessagesResult": PutMessagesResult,
    "PutMessagesResultEntry": PutMessagesResultEntry,
    "Stream": Stream,
    "StreamPool": StreamPool,
    "StreamPoolSummary": StreamPoolSummary,
    "StreamSummary": StreamSummary,
    "UpdateArchiverDetails": UpdateArchiverDetails,
    "UpdateConnectHarnessDetails": UpdateConnectHarnessDetails,
    "UpdateGroupDetails": UpdateGroupDetails,
    "UpdateStreamDetails": UpdateStreamDetails,
    "UpdateStreamPoolDetails": UpdateStreamPoolDetails
}
