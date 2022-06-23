# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .activate_order_details import ActivateOrderDetails
from .assigned_subscription import AssignedSubscription
from .assigned_subscription_collection import AssignedSubscriptionCollection
from .assigned_subscription_summary import AssignedSubscriptionSummary
from .available_region_collection import AvailableRegionCollection
from .available_region_summary import AvailableRegionSummary
from .create_child_tenancy_details import CreateChildTenancyDetails
from .create_domain_details import CreateDomainDetails
from .create_domain_governance_details import CreateDomainGovernanceDetails
from .create_sender_invitation_details import CreateSenderInvitationDetails
from .create_subscription_mapping_details import CreateSubscriptionMappingDetails
from .domain import Domain
from .domain_collection import DomainCollection
from .domain_governance import DomainGovernance
from .domain_governance_collection import DomainGovernanceCollection
from .domain_governance_summary import DomainGovernanceSummary
from .domain_summary import DomainSummary
from .link import Link
from .link_collection import LinkCollection
from .link_summary import LinkSummary
from .order import Order
from .organization import Organization
from .organization_collection import OrganizationCollection
from .organization_summary import OrganizationSummary
from .organization_tenancy import OrganizationTenancy
from .organization_tenancy_collection import OrganizationTenancyCollection
from .organization_tenancy_summary import OrganizationTenancySummary
from .promotion import Promotion
from .recipient_invitation import RecipientInvitation
from .recipient_invitation_collection import RecipientInvitationCollection
from .recipient_invitation_summary import RecipientInvitationSummary
from .sender_invitation import SenderInvitation
from .sender_invitation_collection import SenderInvitationCollection
from .sender_invitation_summary import SenderInvitationSummary
from .sku import Sku
from .subscription import Subscription
from .subscription_collection import SubscriptionCollection
from .subscription_info import SubscriptionInfo
from .subscription_mapping import SubscriptionMapping
from .subscription_mapping_collection import SubscriptionMappingCollection
from .subscription_mapping_summary import SubscriptionMappingSummary
from .subscription_sku import SubscriptionSku
from .subscription_summary import SubscriptionSummary
from .update_domain_details import UpdateDomainDetails
from .update_domain_governance_details import UpdateDomainGovernanceDetails
from .update_organization_details import UpdateOrganizationDetails
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
    "ActivateOrderDetails": ActivateOrderDetails,
    "AssignedSubscription": AssignedSubscription,
    "AssignedSubscriptionCollection": AssignedSubscriptionCollection,
    "AssignedSubscriptionSummary": AssignedSubscriptionSummary,
    "AvailableRegionCollection": AvailableRegionCollection,
    "AvailableRegionSummary": AvailableRegionSummary,
    "CreateChildTenancyDetails": CreateChildTenancyDetails,
    "CreateDomainDetails": CreateDomainDetails,
    "CreateDomainGovernanceDetails": CreateDomainGovernanceDetails,
    "CreateSenderInvitationDetails": CreateSenderInvitationDetails,
    "CreateSubscriptionMappingDetails": CreateSubscriptionMappingDetails,
    "Domain": Domain,
    "DomainCollection": DomainCollection,
    "DomainGovernance": DomainGovernance,
    "DomainGovernanceCollection": DomainGovernanceCollection,
    "DomainGovernanceSummary": DomainGovernanceSummary,
    "DomainSummary": DomainSummary,
    "Link": Link,
    "LinkCollection": LinkCollection,
    "LinkSummary": LinkSummary,
    "Order": Order,
    "Organization": Organization,
    "OrganizationCollection": OrganizationCollection,
    "OrganizationSummary": OrganizationSummary,
    "OrganizationTenancy": OrganizationTenancy,
    "OrganizationTenancyCollection": OrganizationTenancyCollection,
    "OrganizationTenancySummary": OrganizationTenancySummary,
    "Promotion": Promotion,
    "RecipientInvitation": RecipientInvitation,
    "RecipientInvitationCollection": RecipientInvitationCollection,
    "RecipientInvitationSummary": RecipientInvitationSummary,
    "SenderInvitation": SenderInvitation,
    "SenderInvitationCollection": SenderInvitationCollection,
    "SenderInvitationSummary": SenderInvitationSummary,
    "Sku": Sku,
    "Subscription": Subscription,
    "SubscriptionCollection": SubscriptionCollection,
    "SubscriptionInfo": SubscriptionInfo,
    "SubscriptionMapping": SubscriptionMapping,
    "SubscriptionMappingCollection": SubscriptionMappingCollection,
    "SubscriptionMappingSummary": SubscriptionMappingSummary,
    "SubscriptionSku": SubscriptionSku,
    "SubscriptionSummary": SubscriptionSummary,
    "UpdateDomainDetails": UpdateDomainDetails,
    "UpdateDomainGovernanceDetails": UpdateDomainGovernanceDetails,
    "UpdateOrganizationDetails": UpdateOrganizationDetails,
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
