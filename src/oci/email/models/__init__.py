# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20170907

from __future__ import absolute_import

from .change_email_domain_compartment_details import ChangeEmailDomainCompartmentDetails
from .change_sender_compartment_details import ChangeSenderCompartmentDetails
from .configuration import Configuration
from .create_dkim_details import CreateDkimDetails
from .create_email_domain_details import CreateEmailDomainDetails
from .create_email_return_path_details import CreateEmailReturnPathDetails
from .create_sender_details import CreateSenderDetails
from .create_suppression_details import CreateSuppressionDetails
from .dkim import Dkim
from .dkim_collection import DkimCollection
from .dkim_summary import DkimSummary
from .email_domain import EmailDomain
from .email_domain_collection import EmailDomainCollection
from .email_domain_summary import EmailDomainSummary
from .email_return_path import EmailReturnPath
from .email_return_path_collection import EmailReturnPathCollection
from .email_return_path_summary import EmailReturnPathSummary
from .sender import Sender
from .sender_summary import SenderSummary
from .suppression import Suppression
from .suppression_summary import SuppressionSummary
from .update_dkim_details import UpdateDkimDetails
from .update_email_domain_details import UpdateEmailDomainDetails
from .update_email_return_path_details import UpdateEmailReturnPathDetails
from .update_sender_details import UpdateSenderDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary
from .work_request_summary_collection import WorkRequestSummaryCollection

# Maps type names to classes for email services.
email_type_mapping = {
    "ChangeEmailDomainCompartmentDetails": ChangeEmailDomainCompartmentDetails,
    "ChangeSenderCompartmentDetails": ChangeSenderCompartmentDetails,
    "Configuration": Configuration,
    "CreateDkimDetails": CreateDkimDetails,
    "CreateEmailDomainDetails": CreateEmailDomainDetails,
    "CreateEmailReturnPathDetails": CreateEmailReturnPathDetails,
    "CreateSenderDetails": CreateSenderDetails,
    "CreateSuppressionDetails": CreateSuppressionDetails,
    "Dkim": Dkim,
    "DkimCollection": DkimCollection,
    "DkimSummary": DkimSummary,
    "EmailDomain": EmailDomain,
    "EmailDomainCollection": EmailDomainCollection,
    "EmailDomainSummary": EmailDomainSummary,
    "EmailReturnPath": EmailReturnPath,
    "EmailReturnPathCollection": EmailReturnPathCollection,
    "EmailReturnPathSummary": EmailReturnPathSummary,
    "Sender": Sender,
    "SenderSummary": SenderSummary,
    "Suppression": Suppression,
    "SuppressionSummary": SuppressionSummary,
    "UpdateDkimDetails": UpdateDkimDetails,
    "UpdateEmailDomainDetails": UpdateEmailDomainDetails,
    "UpdateEmailReturnPathDetails": UpdateEmailReturnPathDetails,
    "UpdateSenderDetails": UpdateSenderDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary,
    "WorkRequestSummaryCollection": WorkRequestSummaryCollection
}
