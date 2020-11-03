# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .create_sender_invitation_details import CreateSenderInvitationDetails
from .link import Link
from .link_collection import LinkCollection
from .link_summary import LinkSummary
from .recipient_invitation import RecipientInvitation
from .recipient_invitation_collection import RecipientInvitationCollection
from .recipient_invitation_summary import RecipientInvitationSummary
from .sender_invitation import SenderInvitation
from .sender_invitation_collection import SenderInvitationCollection
from .sender_invitation_summary import SenderInvitationSummary
from .update_recipient_invitation_details import UpdateRecipientInvitationDetails
from .update_sender_invitation_details import UpdateSenderInvitationDetails
from .work_request import WorkRequest
from .work_request_collection import WorkRequestCollection
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary

# Maps type names to classes for tenant_manager_control_plane services.
tenant_manager_control_plane_type_mapping = {
    "CreateSenderInvitationDetails": CreateSenderInvitationDetails,
    "Link": Link,
    "LinkCollection": LinkCollection,
    "LinkSummary": LinkSummary,
    "RecipientInvitation": RecipientInvitation,
    "RecipientInvitationCollection": RecipientInvitationCollection,
    "RecipientInvitationSummary": RecipientInvitationSummary,
    "SenderInvitation": SenderInvitation,
    "SenderInvitationCollection": SenderInvitationCollection,
    "SenderInvitationSummary": SenderInvitationSummary,
    "UpdateRecipientInvitationDetails": UpdateRecipientInvitationDetails,
    "UpdateSenderInvitationDetails": UpdateSenderInvitationDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestCollection": WorkRequestCollection,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}
