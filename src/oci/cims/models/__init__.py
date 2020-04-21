# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .activity_item import ActivityItem
from .category import Category
from .classifier import Classifier
from .contact import Contact
from .contact_list import ContactList
from .create_category_details import CreateCategoryDetails
from .create_incident import CreateIncident
from .create_issue_type_details import CreateIssueTypeDetails
from .create_item_details import CreateItemDetails
from .create_limit_item_details import CreateLimitItemDetails
from .create_resource_details import CreateResourceDetails
from .create_sub_category_details import CreateSubCategoryDetails
from .create_tech_support_item_details import CreateTechSupportItemDetails
from .create_ticket_details import CreateTicketDetails
from .incident import Incident
from .incident_resource_type import IncidentResourceType
from .incident_summary import IncidentSummary
from .incident_type import IncidentType
from .issue_type import IssueType
from .item import Item
from .limit_item import LimitItem
from .resource import Resource
from .service_category import ServiceCategory
from .status import Status
from .sub_category import SubCategory
from .tech_support_item import TechSupportItem
from .tenancy_information import TenancyInformation
from .ticket import Ticket
from .update_activity_item_details import UpdateActivityItemDetails
from .update_incident import UpdateIncident
from .update_item_details import UpdateItemDetails
from .update_resource_details import UpdateResourceDetails
from .update_ticket_details import UpdateTicketDetails
from .validation_response import ValidationResponse

# Maps type names to classes for cims services.
cims_type_mapping = {
    "ActivityItem": ActivityItem,
    "Category": Category,
    "Classifier": Classifier,
    "Contact": Contact,
    "ContactList": ContactList,
    "CreateCategoryDetails": CreateCategoryDetails,
    "CreateIncident": CreateIncident,
    "CreateIssueTypeDetails": CreateIssueTypeDetails,
    "CreateItemDetails": CreateItemDetails,
    "CreateLimitItemDetails": CreateLimitItemDetails,
    "CreateResourceDetails": CreateResourceDetails,
    "CreateSubCategoryDetails": CreateSubCategoryDetails,
    "CreateTechSupportItemDetails": CreateTechSupportItemDetails,
    "CreateTicketDetails": CreateTicketDetails,
    "Incident": Incident,
    "IncidentResourceType": IncidentResourceType,
    "IncidentSummary": IncidentSummary,
    "IncidentType": IncidentType,
    "IssueType": IssueType,
    "Item": Item,
    "LimitItem": LimitItem,
    "Resource": Resource,
    "ServiceCategory": ServiceCategory,
    "Status": Status,
    "SubCategory": SubCategory,
    "TechSupportItem": TechSupportItem,
    "TenancyInformation": TenancyInformation,
    "Ticket": Ticket,
    "UpdateActivityItemDetails": UpdateActivityItemDetails,
    "UpdateIncident": UpdateIncident,
    "UpdateItemDetails": UpdateItemDetails,
    "UpdateResourceDetails": UpdateResourceDetails,
    "UpdateTicketDetails": UpdateTicketDetails,
    "ValidationResponse": ValidationResponse
}
