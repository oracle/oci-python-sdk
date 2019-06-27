# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from .access_rule import AccessRule
from .access_rule_criteria import AccessRuleCriteria
from .address_rate_limiting import AddressRateLimiting
from .block_challenge_settings import BlockChallengeSettings
from .captcha import Captcha
from .certificate import Certificate
from .certificate_extensions import CertificateExtensions
from .certificate_public_key_info import CertificatePublicKeyInfo
from .certificate_subject_name import CertificateSubjectName
from .certificate_summary import CertificateSummary
from .change_certificate_compartment_details import ChangeCertificateCompartmentDetails
from .change_waas_policy_compartment_details import ChangeWaasPolicyCompartmentDetails
from .create_certificate_details import CreateCertificateDetails
from .create_waas_policy_details import CreateWaasPolicyDetails
from .device_fingerprint_challenge import DeviceFingerprintChallenge
from .edge_subnet import EdgeSubnet
from .good_bot import GoodBot
from .header import Header
from .human_interaction_challenge import HumanInteractionChallenge
from .js_challenge import JsChallenge
from .origin import Origin
from .policy_config import PolicyConfig
from .protection_rule import ProtectionRule
from .protection_rule_action import ProtectionRuleAction
from .protection_rule_exclusion import ProtectionRuleExclusion
from .protection_settings import ProtectionSettings
from .recommendation import Recommendation
from .threat_feed import ThreatFeed
from .threat_feed_action import ThreatFeedAction
from .update_certificate_details import UpdateCertificateDetails
from .update_waas_policy_details import UpdateWaasPolicyDetails
from .waas_policy import WaasPolicy
from .waas_policy_summary import WaasPolicySummary
from .waf_blocked_request import WafBlockedRequest
from .waf_config import WafConfig
from .waf_config_details import WafConfigDetails
from .waf_log import WafLog
from .waf_meter_datum import WafMeterDatum
from .waf_request import WafRequest
from .waf_traffic_datum import WafTrafficDatum
from .whitelist import Whitelist
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary

# Maps type names to classes for waas services.
waas_type_mapping = {
    "AccessRule": AccessRule,
    "AccessRuleCriteria": AccessRuleCriteria,
    "AddressRateLimiting": AddressRateLimiting,
    "BlockChallengeSettings": BlockChallengeSettings,
    "Captcha": Captcha,
    "Certificate": Certificate,
    "CertificateExtensions": CertificateExtensions,
    "CertificatePublicKeyInfo": CertificatePublicKeyInfo,
    "CertificateSubjectName": CertificateSubjectName,
    "CertificateSummary": CertificateSummary,
    "ChangeCertificateCompartmentDetails": ChangeCertificateCompartmentDetails,
    "ChangeWaasPolicyCompartmentDetails": ChangeWaasPolicyCompartmentDetails,
    "CreateCertificateDetails": CreateCertificateDetails,
    "CreateWaasPolicyDetails": CreateWaasPolicyDetails,
    "DeviceFingerprintChallenge": DeviceFingerprintChallenge,
    "EdgeSubnet": EdgeSubnet,
    "GoodBot": GoodBot,
    "Header": Header,
    "HumanInteractionChallenge": HumanInteractionChallenge,
    "JsChallenge": JsChallenge,
    "Origin": Origin,
    "PolicyConfig": PolicyConfig,
    "ProtectionRule": ProtectionRule,
    "ProtectionRuleAction": ProtectionRuleAction,
    "ProtectionRuleExclusion": ProtectionRuleExclusion,
    "ProtectionSettings": ProtectionSettings,
    "Recommendation": Recommendation,
    "ThreatFeed": ThreatFeed,
    "ThreatFeedAction": ThreatFeedAction,
    "UpdateCertificateDetails": UpdateCertificateDetails,
    "UpdateWaasPolicyDetails": UpdateWaasPolicyDetails,
    "WaasPolicy": WaasPolicy,
    "WaasPolicySummary": WaasPolicySummary,
    "WafBlockedRequest": WafBlockedRequest,
    "WafConfig": WafConfig,
    "WafConfigDetails": WafConfigDetails,
    "WafLog": WafLog,
    "WafMeterDatum": WafMeterDatum,
    "WafRequest": WafRequest,
    "WafTrafficDatum": WafTrafficDatum,
    "Whitelist": Whitelist,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}
