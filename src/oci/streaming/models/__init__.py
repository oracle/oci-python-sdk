# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .change_connect_harness_compartment_details import ChangeConnectHarnessCompartmentDetails
from .change_stream_compartment_details import ChangeStreamCompartmentDetails
from .change_stream_pool_compartment_details import ChangeStreamPoolCompartmentDetails
from .connect_harness import ConnectHarness
from .connect_harness_summary import ConnectHarnessSummary
from .create_connect_harness_details import CreateConnectHarnessDetails
from .create_cursor_details import CreateCursorDetails
from .create_group_cursor_details import CreateGroupCursorDetails
from .create_stream_details import CreateStreamDetails
from .create_stream_pool_details import CreateStreamPoolDetails
from .cursor import Cursor
from .custom_encryption_key import CustomEncryptionKey
from .custom_encryption_key_details import CustomEncryptionKeyDetails
from .group import Group
from .kafka_settings import KafkaSettings
from .message import Message
from .partition_reservation import PartitionReservation
from .private_endpoint_details import PrivateEndpointDetails
from .private_endpoint_settings import PrivateEndpointSettings
from .put_messages_details import PutMessagesDetails
from .put_messages_details_entry import PutMessagesDetailsEntry
from .put_messages_result import PutMessagesResult
from .put_messages_result_entry import PutMessagesResultEntry
from .stream import Stream
from .stream_pool import StreamPool
from .stream_pool_summary import StreamPoolSummary
from .stream_summary import StreamSummary
from .update_connect_harness_details import UpdateConnectHarnessDetails
from .update_group_details import UpdateGroupDetails
from .update_stream_details import UpdateStreamDetails
from .update_stream_pool_details import UpdateStreamPoolDetails

# Maps type names to classes for streaming services.
streaming_type_mapping = {
    "ChangeConnectHarnessCompartmentDetails": ChangeConnectHarnessCompartmentDetails,
    "ChangeStreamCompartmentDetails": ChangeStreamCompartmentDetails,
    "ChangeStreamPoolCompartmentDetails": ChangeStreamPoolCompartmentDetails,
    "ConnectHarness": ConnectHarness,
    "ConnectHarnessSummary": ConnectHarnessSummary,
    "CreateConnectHarnessDetails": CreateConnectHarnessDetails,
    "CreateCursorDetails": CreateCursorDetails,
    "CreateGroupCursorDetails": CreateGroupCursorDetails,
    "CreateStreamDetails": CreateStreamDetails,
    "CreateStreamPoolDetails": CreateStreamPoolDetails,
    "Cursor": Cursor,
    "CustomEncryptionKey": CustomEncryptionKey,
    "CustomEncryptionKeyDetails": CustomEncryptionKeyDetails,
    "Group": Group,
    "KafkaSettings": KafkaSettings,
    "Message": Message,
    "PartitionReservation": PartitionReservation,
    "PrivateEndpointDetails": PrivateEndpointDetails,
    "PrivateEndpointSettings": PrivateEndpointSettings,
    "PutMessagesDetails": PutMessagesDetails,
    "PutMessagesDetailsEntry": PutMessagesDetailsEntry,
    "PutMessagesResult": PutMessagesResult,
    "PutMessagesResultEntry": PutMessagesResultEntry,
    "Stream": Stream,
    "StreamPool": StreamPool,
    "StreamPoolSummary": StreamPoolSummary,
    "StreamSummary": StreamSummary,
    "UpdateConnectHarnessDetails": UpdateConnectHarnessDetails,
    "UpdateGroupDetails": UpdateGroupDetails,
    "UpdateStreamDetails": UpdateStreamDetails,
    "UpdateStreamPoolDetails": UpdateStreamPoolDetails
}
