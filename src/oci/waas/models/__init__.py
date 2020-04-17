# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .access_rule import AccessRule
from .access_rule_criteria import AccessRuleCriteria
from .add_http_response_header_action import AddHttpResponseHeaderAction
from .address_list import AddressList
from .address_list_summary import AddressListSummary
from .address_rate_limiting import AddressRateLimiting
from .block_challenge_settings import BlockChallengeSettings
from .caching_rule import CachingRule
from .caching_rule_criteria import CachingRuleCriteria
from .caching_rule_summary import CachingRuleSummary
from .captcha import Captcha
from .certificate import Certificate
from .certificate_extensions import CertificateExtensions
from .certificate_issuer_name import CertificateIssuerName
from .certificate_public_key_info import CertificatePublicKeyInfo
from .certificate_subject_name import CertificateSubjectName
from .certificate_summary import CertificateSummary
from .change_address_list_compartment_details import ChangeAddressListCompartmentDetails
from .change_certificate_compartment_details import ChangeCertificateCompartmentDetails
from .change_custom_protection_rule_compartment_details import ChangeCustomProtectionRuleCompartmentDetails
from .change_http_redirect_compartment_details import ChangeHttpRedirectCompartmentDetails
from .change_waas_policy_compartment_details import ChangeWaasPolicyCompartmentDetails
from .create_address_list_details import CreateAddressListDetails
from .create_certificate_details import CreateCertificateDetails
from .create_custom_protection_rule_details import CreateCustomProtectionRuleDetails
from .create_http_redirect_details import CreateHttpRedirectDetails
from .create_waas_policy_details import CreateWaasPolicyDetails
from .custom_protection_rule import CustomProtectionRule
from .custom_protection_rule_setting import CustomProtectionRuleSetting
from .custom_protection_rule_summary import CustomProtectionRuleSummary
from .device_fingerprint_challenge import DeviceFingerprintChallenge
from .edge_subnet import EdgeSubnet
from .extend_http_response_header_action import ExtendHttpResponseHeaderAction
from .good_bot import GoodBot
from .header import Header
from .header_manipulation_action import HeaderManipulationAction
from .health_check import HealthCheck
from .http_redirect import HttpRedirect
from .http_redirect_summary import HttpRedirectSummary
from .http_redirect_target import HttpRedirectTarget
from .human_interaction_challenge import HumanInteractionChallenge
from .ip_hash_load_balancing_method import IPHashLoadBalancingMethod
from .js_challenge import JsChallenge
from .load_balancing_method import LoadBalancingMethod
from .origin import Origin
from .origin_group import OriginGroup
from .origin_group_origins import OriginGroupOrigins
from .policy_config import PolicyConfig
from .protection_rule import ProtectionRule
from .protection_rule_action import ProtectionRuleAction
from .protection_rule_exclusion import ProtectionRuleExclusion
from .protection_settings import ProtectionSettings
from .purge_cache import PurgeCache
from .recommendation import Recommendation
from .remove_http_response_header_action import RemoveHttpResponseHeaderAction
from .round_robin_load_balancing_method import RoundRobinLoadBalancingMethod
from .sticky_cookie_load_balancing_method import StickyCookieLoadBalancingMethod
from .threat_feed import ThreatFeed
from .threat_feed_action import ThreatFeedAction
from .update_address_list_details import UpdateAddressListDetails
from .update_certificate_details import UpdateCertificateDetails
from .update_custom_protection_rule_details import UpdateCustomProtectionRuleDetails
from .update_http_redirect_details import UpdateHttpRedirectDetails
from .update_waas_policy_details import UpdateWaasPolicyDetails
from .waas_policy import WaasPolicy
from .waas_policy_custom_protection_rule_summary import WaasPolicyCustomProtectionRuleSummary
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
    "AddHttpResponseHeaderAction": AddHttpResponseHeaderAction,
    "AddressList": AddressList,
    "AddressListSummary": AddressListSummary,
    "AddressRateLimiting": AddressRateLimiting,
    "BlockChallengeSettings": BlockChallengeSettings,
    "CachingRule": CachingRule,
    "CachingRuleCriteria": CachingRuleCriteria,
    "CachingRuleSummary": CachingRuleSummary,
    "Captcha": Captcha,
    "Certificate": Certificate,
    "CertificateExtensions": CertificateExtensions,
    "CertificateIssuerName": CertificateIssuerName,
    "CertificatePublicKeyInfo": CertificatePublicKeyInfo,
    "CertificateSubjectName": CertificateSubjectName,
    "CertificateSummary": CertificateSummary,
    "ChangeAddressListCompartmentDetails": ChangeAddressListCompartmentDetails,
    "ChangeCertificateCompartmentDetails": ChangeCertificateCompartmentDetails,
    "ChangeCustomProtectionRuleCompartmentDetails": ChangeCustomProtectionRuleCompartmentDetails,
    "ChangeHttpRedirectCompartmentDetails": ChangeHttpRedirectCompartmentDetails,
    "ChangeWaasPolicyCompartmentDetails": ChangeWaasPolicyCompartmentDetails,
    "CreateAddressListDetails": CreateAddressListDetails,
    "CreateCertificateDetails": CreateCertificateDetails,
    "CreateCustomProtectionRuleDetails": CreateCustomProtectionRuleDetails,
    "CreateHttpRedirectDetails": CreateHttpRedirectDetails,
    "CreateWaasPolicyDetails": CreateWaasPolicyDetails,
    "CustomProtectionRule": CustomProtectionRule,
    "CustomProtectionRuleSetting": CustomProtectionRuleSetting,
    "CustomProtectionRuleSummary": CustomProtectionRuleSummary,
    "DeviceFingerprintChallenge": DeviceFingerprintChallenge,
    "EdgeSubnet": EdgeSubnet,
    "ExtendHttpResponseHeaderAction": ExtendHttpResponseHeaderAction,
    "GoodBot": GoodBot,
    "Header": Header,
    "HeaderManipulationAction": HeaderManipulationAction,
    "HealthCheck": HealthCheck,
    "HttpRedirect": HttpRedirect,
    "HttpRedirectSummary": HttpRedirectSummary,
    "HttpRedirectTarget": HttpRedirectTarget,
    "HumanInteractionChallenge": HumanInteractionChallenge,
    "IPHashLoadBalancingMethod": IPHashLoadBalancingMethod,
    "JsChallenge": JsChallenge,
    "LoadBalancingMethod": LoadBalancingMethod,
    "Origin": Origin,
    "OriginGroup": OriginGroup,
    "OriginGroupOrigins": OriginGroupOrigins,
    "PolicyConfig": PolicyConfig,
    "ProtectionRule": ProtectionRule,
    "ProtectionRuleAction": ProtectionRuleAction,
    "ProtectionRuleExclusion": ProtectionRuleExclusion,
    "ProtectionSettings": ProtectionSettings,
    "PurgeCache": PurgeCache,
    "Recommendation": Recommendation,
    "RemoveHttpResponseHeaderAction": RemoveHttpResponseHeaderAction,
    "RoundRobinLoadBalancingMethod": RoundRobinLoadBalancingMethod,
    "StickyCookieLoadBalancingMethod": StickyCookieLoadBalancingMethod,
    "ThreatFeed": ThreatFeed,
    "ThreatFeedAction": ThreatFeedAction,
    "UpdateAddressListDetails": UpdateAddressListDetails,
    "UpdateCertificateDetails": UpdateCertificateDetails,
    "UpdateCustomProtectionRuleDetails": UpdateCustomProtectionRuleDetails,
    "UpdateHttpRedirectDetails": UpdateHttpRedirectDetails,
    "UpdateWaasPolicyDetails": UpdateWaasPolicyDetails,
    "WaasPolicy": WaasPolicy,
    "WaasPolicyCustomProtectionRuleSummary": WaasPolicyCustomProtectionRuleSummary,
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
