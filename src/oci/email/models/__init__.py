# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from .create_sender_details import CreateSenderDetails
from .create_suppression_details import CreateSuppressionDetails
from .sender import Sender
from .sender_summary import SenderSummary
from .suppression import Suppression
from .suppression_summary import SuppressionSummary

# Maps type names to classes for email services.
email_type_mapping = {
    "CreateSenderDetails": CreateSenderDetails,
    "CreateSuppressionDetails": CreateSuppressionDetails,
    "Sender": Sender,
    "SenderSummary": SenderSummary,
    "Suppression": Suppression,
    "SuppressionSummary": SuppressionSummary
}
