# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .allowed_regions_template import AllowedRegionsTemplate
from .association import Association
from .base_tag_definition_validator import BaseTagDefinitionValidator
from .create_governance_rule_details import CreateGovernanceRuleDetails
from .create_inclusion_criterion_details import CreateInclusionCriterionDetails
from .default_tag_definition_validator import DefaultTagDefinitionValidator
from .enforced_governance_rule import EnforcedGovernanceRule
from .enforced_governance_rule_collection import EnforcedGovernanceRuleCollection
from .enforced_governance_rule_summary import EnforcedGovernanceRuleSummary
from .enum_tag_definition_validator import EnumTagDefinitionValidator
from .governance_rule import GovernanceRule
from .governance_rule_collection import GovernanceRuleCollection
from .governance_rule_summary import GovernanceRuleSummary
from .inclusion_criterion import InclusionCriterion
from .inclusion_criterion_collection import InclusionCriterionCollection
from .inclusion_criterion_summary import InclusionCriterionSummary
from .quota_template import QuotaTemplate
from .tag import Tag
from .tag_default import TagDefault
from .tag_template import TagTemplate
from .template import Template
from .tenancy_association import TenancyAssociation
from .tenancy_attachment import TenancyAttachment
from .tenancy_attachment_collection import TenancyAttachmentCollection
from .tenancy_attachment_summary import TenancyAttachmentSummary
from .update_governance_rule_details import UpdateGovernanceRuleDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary
from .work_request_summary_collection import WorkRequestSummaryCollection

# Maps type names to classes for governance_rules_control_plane services.
governance_rules_control_plane_type_mapping = {
    "AllowedRegionsTemplate": AllowedRegionsTemplate,
    "Association": Association,
    "BaseTagDefinitionValidator": BaseTagDefinitionValidator,
    "CreateGovernanceRuleDetails": CreateGovernanceRuleDetails,
    "CreateInclusionCriterionDetails": CreateInclusionCriterionDetails,
    "DefaultTagDefinitionValidator": DefaultTagDefinitionValidator,
    "EnforcedGovernanceRule": EnforcedGovernanceRule,
    "EnforcedGovernanceRuleCollection": EnforcedGovernanceRuleCollection,
    "EnforcedGovernanceRuleSummary": EnforcedGovernanceRuleSummary,
    "EnumTagDefinitionValidator": EnumTagDefinitionValidator,
    "GovernanceRule": GovernanceRule,
    "GovernanceRuleCollection": GovernanceRuleCollection,
    "GovernanceRuleSummary": GovernanceRuleSummary,
    "InclusionCriterion": InclusionCriterion,
    "InclusionCriterionCollection": InclusionCriterionCollection,
    "InclusionCriterionSummary": InclusionCriterionSummary,
    "QuotaTemplate": QuotaTemplate,
    "Tag": Tag,
    "TagDefault": TagDefault,
    "TagTemplate": TagTemplate,
    "Template": Template,
    "TenancyAssociation": TenancyAssociation,
    "TenancyAttachment": TenancyAttachment,
    "TenancyAttachmentCollection": TenancyAttachmentCollection,
    "TenancyAttachmentSummary": TenancyAttachmentSummary,
    "UpdateGovernanceRuleDetails": UpdateGovernanceRuleDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary,
    "WorkRequestSummaryCollection": WorkRequestSummaryCollection
}
