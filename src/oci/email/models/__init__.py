# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .change_sender_compartment_details import ChangeSenderCompartmentDetails
from .create_sender_details import CreateSenderDetails
from .create_suppression_details import CreateSuppressionDetails
from .sender import Sender
from .sender_summary import SenderSummary
from .suppression import Suppression
from .suppression_summary import SuppressionSummary
from .update_sender_details import UpdateSenderDetails

# Maps type names to classes for email services.
email_type_mapping = {
    "ChangeSenderCompartmentDetails": ChangeSenderCompartmentDetails,
    "CreateSenderDetails": CreateSenderDetails,
    "CreateSuppressionDetails": CreateSuppressionDetails,
    "Sender": Sender,
    "SenderSummary": SenderSummary,
    "Suppression": Suppression,
    "SuppressionSummary": SuppressionSummary,
    "UpdateSenderDetails": UpdateSenderDetails
}
