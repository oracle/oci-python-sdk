# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .application import Application
from .change_network_firewall_compartment_details import ChangeNetworkFirewallCompartmentDetails
from .change_network_firewall_policy_compartment_details import ChangeNetworkFirewallPolicyCompartmentDetails
from .create_network_firewall_details import CreateNetworkFirewallDetails
from .create_network_firewall_policy_details import CreateNetworkFirewallPolicyDetails
from .decryption_profile import DecryptionProfile
from .decryption_rule import DecryptionRule
from .decryption_rule_match_criteria import DecryptionRuleMatchCriteria
from .icmp6_application import Icmp6Application
from .icmp_application import IcmpApplication
from .mapped_secret import MappedSecret
from .network_firewall import NetworkFirewall
from .network_firewall_collection import NetworkFirewallCollection
from .network_firewall_policy import NetworkFirewallPolicy
from .network_firewall_policy_summary import NetworkFirewallPolicySummary
from .network_firewall_policy_summary_collection import NetworkFirewallPolicySummaryCollection
from .network_firewall_summary import NetworkFirewallSummary
from .security_rule import SecurityRule
from .security_rule_match_criteria import SecurityRuleMatchCriteria
from .simple_url_pattern import SimpleUrlPattern
from .ssl_forward_proxy_profile import SslForwardProxyProfile
from .ssl_inbound_inspection_profile import SslInboundInspectionProfile
from .tcp_application import TcpApplication
from .udp_application import UdpApplication
from .update_network_firewall_details import UpdateNetworkFirewallDetails
from .update_network_firewall_policy_details import UpdateNetworkFirewallPolicyDetails
from .url_pattern import UrlPattern
from .vault_mapped_secret import VaultMappedSecret
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary
from .work_request_summary_collection import WorkRequestSummaryCollection

# Maps type names to classes for network_firewall services.
network_firewall_type_mapping = {
    "Application": Application,
    "ChangeNetworkFirewallCompartmentDetails": ChangeNetworkFirewallCompartmentDetails,
    "ChangeNetworkFirewallPolicyCompartmentDetails": ChangeNetworkFirewallPolicyCompartmentDetails,
    "CreateNetworkFirewallDetails": CreateNetworkFirewallDetails,
    "CreateNetworkFirewallPolicyDetails": CreateNetworkFirewallPolicyDetails,
    "DecryptionProfile": DecryptionProfile,
    "DecryptionRule": DecryptionRule,
    "DecryptionRuleMatchCriteria": DecryptionRuleMatchCriteria,
    "Icmp6Application": Icmp6Application,
    "IcmpApplication": IcmpApplication,
    "MappedSecret": MappedSecret,
    "NetworkFirewall": NetworkFirewall,
    "NetworkFirewallCollection": NetworkFirewallCollection,
    "NetworkFirewallPolicy": NetworkFirewallPolicy,
    "NetworkFirewallPolicySummary": NetworkFirewallPolicySummary,
    "NetworkFirewallPolicySummaryCollection": NetworkFirewallPolicySummaryCollection,
    "NetworkFirewallSummary": NetworkFirewallSummary,
    "SecurityRule": SecurityRule,
    "SecurityRuleMatchCriteria": SecurityRuleMatchCriteria,
    "SimpleUrlPattern": SimpleUrlPattern,
    "SslForwardProxyProfile": SslForwardProxyProfile,
    "SslInboundInspectionProfile": SslInboundInspectionProfile,
    "TcpApplication": TcpApplication,
    "UdpApplication": UdpApplication,
    "UpdateNetworkFirewallDetails": UpdateNetworkFirewallDetails,
    "UpdateNetworkFirewallPolicyDetails": UpdateNetworkFirewallPolicyDetails,
    "UrlPattern": UrlPattern,
    "VaultMappedSecret": VaultMappedSecret,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary,
    "WorkRequestSummaryCollection": WorkRequestSummaryCollection
}
