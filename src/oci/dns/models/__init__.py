# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .change_steering_policy_compartment_details import ChangeSteeringPolicyCompartmentDetails
from .change_tsig_key_compartment_details import ChangeTsigKeyCompartmentDetails
from .change_zone_compartment_details import ChangeZoneCompartmentDetails
from .create_migrated_dynect_zone_details import CreateMigratedDynectZoneDetails
from .create_steering_policy_attachment_details import CreateSteeringPolicyAttachmentDetails
from .create_steering_policy_details import CreateSteeringPolicyDetails
from .create_tsig_key_details import CreateTsigKeyDetails
from .create_zone_base_details import CreateZoneBaseDetails
from .create_zone_details import CreateZoneDetails
from .dynect_migration_details import DynectMigrationDetails
from .external_master import ExternalMaster
from .migration_replacement import MigrationReplacement
from .nameserver import Nameserver
from .patch_domain_records_details import PatchDomainRecordsDetails
from .patch_rr_set_details import PatchRRSetDetails
from .patch_zone_records_details import PatchZoneRecordsDetails
from .rr_set import RRSet
from .record import Record
from .record_collection import RecordCollection
from .record_details import RecordDetails
from .record_operation import RecordOperation
from .steering_policy import SteeringPolicy
from .steering_policy_answer import SteeringPolicyAnswer
from .steering_policy_attachment import SteeringPolicyAttachment
from .steering_policy_attachment_summary import SteeringPolicyAttachmentSummary
from .steering_policy_filter_answer_data import SteeringPolicyFilterAnswerData
from .steering_policy_filter_rule import SteeringPolicyFilterRule
from .steering_policy_filter_rule_case import SteeringPolicyFilterRuleCase
from .steering_policy_health_rule import SteeringPolicyHealthRule
from .steering_policy_health_rule_case import SteeringPolicyHealthRuleCase
from .steering_policy_limit_rule import SteeringPolicyLimitRule
from .steering_policy_limit_rule_case import SteeringPolicyLimitRuleCase
from .steering_policy_priority_answer_data import SteeringPolicyPriorityAnswerData
from .steering_policy_priority_rule import SteeringPolicyPriorityRule
from .steering_policy_priority_rule_case import SteeringPolicyPriorityRuleCase
from .steering_policy_rule import SteeringPolicyRule
from .steering_policy_summary import SteeringPolicySummary
from .steering_policy_weighted_answer_data import SteeringPolicyWeightedAnswerData
from .steering_policy_weighted_rule import SteeringPolicyWeightedRule
from .steering_policy_weighted_rule_case import SteeringPolicyWeightedRuleCase
from .tsig import TSIG
from .tsig_key import TsigKey
from .tsig_key_summary import TsigKeySummary
from .update_domain_records_details import UpdateDomainRecordsDetails
from .update_rr_set_details import UpdateRRSetDetails
from .update_steering_policy_attachment_details import UpdateSteeringPolicyAttachmentDetails
from .update_steering_policy_details import UpdateSteeringPolicyDetails
from .update_tsig_key_details import UpdateTsigKeyDetails
from .update_zone_details import UpdateZoneDetails
from .update_zone_records_details import UpdateZoneRecordsDetails
from .zone import Zone
from .zone_summary import ZoneSummary

# Maps type names to classes for dns services.
dns_type_mapping = {
    "ChangeSteeringPolicyCompartmentDetails": ChangeSteeringPolicyCompartmentDetails,
    "ChangeTsigKeyCompartmentDetails": ChangeTsigKeyCompartmentDetails,
    "ChangeZoneCompartmentDetails": ChangeZoneCompartmentDetails,
    "CreateMigratedDynectZoneDetails": CreateMigratedDynectZoneDetails,
    "CreateSteeringPolicyAttachmentDetails": CreateSteeringPolicyAttachmentDetails,
    "CreateSteeringPolicyDetails": CreateSteeringPolicyDetails,
    "CreateTsigKeyDetails": CreateTsigKeyDetails,
    "CreateZoneBaseDetails": CreateZoneBaseDetails,
    "CreateZoneDetails": CreateZoneDetails,
    "DynectMigrationDetails": DynectMigrationDetails,
    "ExternalMaster": ExternalMaster,
    "MigrationReplacement": MigrationReplacement,
    "Nameserver": Nameserver,
    "PatchDomainRecordsDetails": PatchDomainRecordsDetails,
    "PatchRRSetDetails": PatchRRSetDetails,
    "PatchZoneRecordsDetails": PatchZoneRecordsDetails,
    "RRSet": RRSet,
    "Record": Record,
    "RecordCollection": RecordCollection,
    "RecordDetails": RecordDetails,
    "RecordOperation": RecordOperation,
    "SteeringPolicy": SteeringPolicy,
    "SteeringPolicyAnswer": SteeringPolicyAnswer,
    "SteeringPolicyAttachment": SteeringPolicyAttachment,
    "SteeringPolicyAttachmentSummary": SteeringPolicyAttachmentSummary,
    "SteeringPolicyFilterAnswerData": SteeringPolicyFilterAnswerData,
    "SteeringPolicyFilterRule": SteeringPolicyFilterRule,
    "SteeringPolicyFilterRuleCase": SteeringPolicyFilterRuleCase,
    "SteeringPolicyHealthRule": SteeringPolicyHealthRule,
    "SteeringPolicyHealthRuleCase": SteeringPolicyHealthRuleCase,
    "SteeringPolicyLimitRule": SteeringPolicyLimitRule,
    "SteeringPolicyLimitRuleCase": SteeringPolicyLimitRuleCase,
    "SteeringPolicyPriorityAnswerData": SteeringPolicyPriorityAnswerData,
    "SteeringPolicyPriorityRule": SteeringPolicyPriorityRule,
    "SteeringPolicyPriorityRuleCase": SteeringPolicyPriorityRuleCase,
    "SteeringPolicyRule": SteeringPolicyRule,
    "SteeringPolicySummary": SteeringPolicySummary,
    "SteeringPolicyWeightedAnswerData": SteeringPolicyWeightedAnswerData,
    "SteeringPolicyWeightedRule": SteeringPolicyWeightedRule,
    "SteeringPolicyWeightedRuleCase": SteeringPolicyWeightedRuleCase,
    "TSIG": TSIG,
    "TsigKey": TsigKey,
    "TsigKeySummary": TsigKeySummary,
    "UpdateDomainRecordsDetails": UpdateDomainRecordsDetails,
    "UpdateRRSetDetails": UpdateRRSetDetails,
    "UpdateSteeringPolicyAttachmentDetails": UpdateSteeringPolicyAttachmentDetails,
    "UpdateSteeringPolicyDetails": UpdateSteeringPolicyDetails,
    "UpdateTsigKeyDetails": UpdateTsigKeyDetails,
    "UpdateZoneDetails": UpdateZoneDetails,
    "UpdateZoneRecordsDetails": UpdateZoneRecordsDetails,
    "Zone": Zone,
    "ZoneSummary": ZoneSummary
}
