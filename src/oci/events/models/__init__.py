# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .action import Action
from .action_details import ActionDetails
from .action_details_list import ActionDetailsList
from .action_list import ActionList
from .change_rule_compartment_details import ChangeRuleCompartmentDetails
from .create_faa_s_action_details import CreateFaaSActionDetails
from .create_notification_service_action_details import CreateNotificationServiceActionDetails
from .create_rule_details import CreateRuleDetails
from .create_streaming_service_action_details import CreateStreamingServiceActionDetails
from .faa_s_action import FaaSAction
from .notification_service_action import NotificationServiceAction
from .rule import Rule
from .rule_summary import RuleSummary
from .streaming_service_action import StreamingServiceAction
from .update_rule_details import UpdateRuleDetails

# Maps type names to classes for events services.
events_type_mapping = {
    "Action": Action,
    "ActionDetails": ActionDetails,
    "ActionDetailsList": ActionDetailsList,
    "ActionList": ActionList,
    "ChangeRuleCompartmentDetails": ChangeRuleCompartmentDetails,
    "CreateFaaSActionDetails": CreateFaaSActionDetails,
    "CreateNotificationServiceActionDetails": CreateNotificationServiceActionDetails,
    "CreateRuleDetails": CreateRuleDetails,
    "CreateStreamingServiceActionDetails": CreateStreamingServiceActionDetails,
    "FaaSAction": FaaSAction,
    "NotificationServiceAction": NotificationServiceAction,
    "Rule": Rule,
    "RuleSummary": RuleSummary,
    "StreamingServiceAction": StreamingServiceAction,
    "UpdateRuleDetails": UpdateRuleDetails
}
