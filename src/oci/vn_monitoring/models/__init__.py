# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .access_denied_traffic_node import AccessDeniedTrafficNode
from .add_drg_route_distribution_statement_details import AddDrgRouteDistributionStatementDetails
from .add_drg_route_distribution_statements_details import AddDrgRouteDistributionStatementsDetails
from .add_drg_route_rule_details import AddDrgRouteRuleDetails
from .add_drg_route_rules_details import AddDrgRouteRulesDetails
from .add_network_security_group_security_rules_details import AddNetworkSecurityGroupSecurityRulesDetails
from .add_security_rule_details import AddSecurityRuleDetails
from .added_network_security_group_security_rules import AddedNetworkSecurityGroupSecurityRules
from .adhoc_get_path_analysis_details import AdhocGetPathAnalysisDetails
from .allowed_security_action import AllowedSecurityAction
from .allowed_security_action_details import AllowedSecurityActionDetails
from .allowed_security_configuration import AllowedSecurityConfiguration
from .bulk_add_virtual_circuit_public_prefixes_details import BulkAddVirtualCircuitPublicPrefixesDetails
from .bulk_delete_virtual_circuit_public_prefixes_details import BulkDeleteVirtualCircuitPublicPrefixesDetails
from .change_path_analyzer_test_compartment_details import ChangePathAnalyzerTestCompartmentDetails
from .compartment_internal import CompartmentInternal
from .compute_instance_endpoint import ComputeInstanceEndpoint
from .connect_local_peering_gateways_details import ConnectLocalPeeringGatewaysDetails
from .connect_remote_peering_connections_details import ConnectRemotePeeringConnectionsDetails
from .cpe import Cpe
from .create_cpe_details import CreateCpeDetails
from .create_cross_connect_details import CreateCrossConnectDetails
from .create_cross_connect_group_details import CreateCrossConnectGroupDetails
from .create_dhcp_details import CreateDhcpDetails
from .create_drg_attachment_details import CreateDrgAttachmentDetails
from .create_drg_details import CreateDrgDetails
from .create_drg_route_distribution_details import CreateDrgRouteDistributionDetails
from .create_drg_route_table_details import CreateDrgRouteTableDetails
from .create_ip_sec_connection_details import CreateIPSecConnectionDetails
from .create_internet_gateway_details import CreateInternetGatewayDetails
from .create_ipv6_details import CreateIpv6Details
from .create_local_peering_gateway_details import CreateLocalPeeringGatewayDetails
from .create_network_security_group_details import CreateNetworkSecurityGroupDetails
from .create_path_analyzer_test_details import CreatePathAnalyzerTestDetails
from .create_private_ip_details import CreatePrivateIpDetails
from .create_public_ip_details import CreatePublicIpDetails
from .create_remote_peering_connection_details import CreateRemotePeeringConnectionDetails
from .create_route_table_details import CreateRouteTableDetails
from .create_security_list_details import CreateSecurityListDetails
from .create_service_gateway_details import CreateServiceGatewayDetails
from .create_subnet_details import CreateSubnetDetails
from .create_vcn_details import CreateVcnDetails
from .create_virtual_circuit_details import CreateVirtualCircuitDetails
from .create_virtual_circuit_public_prefix_details import CreateVirtualCircuitPublicPrefixDetails
from .create_vnic_details import CreateVnicDetails
from .cross_connect import CrossConnect
from .cross_connect_group import CrossConnectGroup
from .cross_connect_location import CrossConnectLocation
from .cross_connect_mapping import CrossConnectMapping
from .cross_connect_port_speed_shape import CrossConnectPortSpeedShape
from .cross_connect_status import CrossConnectStatus
from .default_drg_route_tables import DefaultDrgRouteTables
from .delete_virtual_circuit_public_prefix_details import DeleteVirtualCircuitPublicPrefixDetails
from .denied_security_action import DeniedSecurityAction
from .denied_security_action_details import DeniedSecurityActionDetails
from .dhcp_dns_option import DhcpDnsOption
from .dhcp_option import DhcpOption
from .dhcp_options import DhcpOptions
from .dhcp_search_domain_option import DhcpSearchDomainOption
from .drg import Drg
from .drg_attachment import DrgAttachment
from .drg_attachment_id_drg_route_distribution_match_criteria import DrgAttachmentIdDrgRouteDistributionMatchCriteria
from .drg_attachment_info import DrgAttachmentInfo
from .drg_attachment_network_create_details import DrgAttachmentNetworkCreateDetails
from .drg_attachment_network_details import DrgAttachmentNetworkDetails
from .drg_attachment_network_update_details import DrgAttachmentNetworkUpdateDetails
from .drg_attachment_type_drg_route_distribution_match_criteria import DrgAttachmentTypeDrgRouteDistributionMatchCriteria
from .drg_route_distribution import DrgRouteDistribution
from .drg_route_distribution_match_criteria import DrgRouteDistributionMatchCriteria
from .drg_route_distribution_statement import DrgRouteDistributionStatement
from .drg_route_rule import DrgRouteRule
from .drg_route_table import DrgRouteTable
from .drg_routing_configuration import DrgRoutingConfiguration
from .egress_security_list_configuration import EgressSecurityListConfiguration
from .egress_security_rule import EgressSecurityRule
from .egress_traffic_spec import EgressTrafficSpec
from .endpoint import Endpoint
from .fast_connect_provider_service import FastConnectProviderService
from .forwarded_routing_action import ForwardedRoutingAction
from .forwarded_routing_action_details import ForwardedRoutingActionDetails
from .forwarded_routing_configuration import ForwardedRoutingConfiguration
from .get_path_analysis_details import GetPathAnalysisDetails
from .get_public_ip_by_ip_address_details import GetPublicIpByIpAddressDetails
from .get_public_ip_by_private_ip_id_details import GetPublicIpByPrivateIpIdDetails
from .ip_sec_connection import IPSecConnection
from .ip_sec_connection_device_config import IPSecConnectionDeviceConfig
from .ip_sec_connection_device_status import IPSecConnectionDeviceStatus
from .icmp_options import IcmpOptions
from .icmp_protocol_parameters import IcmpProtocolParameters
from .icmp_traffic_protocol_parameters import IcmpTrafficProtocolParameters
from .indeterminate_routing_action import IndeterminateRoutingAction
from .ingress_security_list_configuration import IngressSecurityListConfiguration
from .ingress_security_rule import IngressSecurityRule
from .internet_gateway import InternetGateway
from .ip_address_endpoint import IpAddressEndpoint
from .ipsec_tunnel_drg_attachment_network_details import IpsecTunnelDrgAttachmentNetworkDetails
from .ipv6 import Ipv6
from .letter_of_authority import LetterOfAuthority
from .load_balancer_endpoint import LoadBalancerEndpoint
from .load_balancer_listener_endpoint import LoadBalancerListenerEndpoint
from .local_peering_gateway import LocalPeeringGateway
from .network_load_balancer_endpoint import NetworkLoadBalancerEndpoint
from .network_load_balancer_listener_endpoint import NetworkLoadBalancerListenerEndpoint
from .network_security_group import NetworkSecurityGroup
from .network_security_group_vnic import NetworkSecurityGroupVnic
from .networking_topology import NetworkingTopology
from .no_route_routing_action import NoRouteRoutingAction
from .no_route_routing_action_details import NoRouteRoutingActionDetails
from .nsg_configuration import NsgConfiguration
from .path import Path
from .path_analysis_work_request_result import PathAnalysisWorkRequestResult
from .path_analyzer_test import PathAnalyzerTest
from .path_analyzer_test_collection import PathAnalyzerTestCollection
from .path_analyzer_test_summary import PathAnalyzerTestSummary
from .path_topology import PathTopology
from .persisted_get_path_analysis_details import PersistedGetPathAnalysisDetails
from .port_range import PortRange
from .private_ip import PrivateIp
from .protocol_parameters import ProtocolParameters
from .public_ip import PublicIp
from .query_options import QueryOptions
from .remote_peering_connection import RemotePeeringConnection
from .remote_peering_connection_drg_attachment_network_details import RemotePeeringConnectionDrgAttachmentNetworkDetails
from .remove_drg_route_distribution_statements_details import RemoveDrgRouteDistributionStatementsDetails
from .remove_drg_route_rules_details import RemoveDrgRouteRulesDetails
from .remove_network_security_group_security_rules_details import RemoveNetworkSecurityGroupSecurityRulesDetails
from .route_rule import RouteRule
from .route_table import RouteTable
from .routing_action import RoutingAction
from .security_action import SecurityAction
from .security_list import SecurityList
from .security_rule import SecurityRule
from .service import Service
from .service_gateway import ServiceGateway
from .service_id_request_details import ServiceIdRequestDetails
from .service_id_response_details import ServiceIdResponseDetails
from .stateful_egress_security_list_configuration import StatefulEgressSecurityListConfiguration
from .stateful_ingress_security_list_configuration import StatefulIngressSecurityListConfiguration
from .stateful_nsg_configuration import StatefulNsgConfiguration
from .subnet import Subnet
from .subnet_endpoint import SubnetEndpoint
from .subnet_topology import SubnetTopology
from .tcp_options import TcpOptions
from .tcp_protocol_parameters import TcpProtocolParameters
from .tcp_traffic_protocol_parameters import TcpTrafficProtocolParameters
from .topology import Topology
from .topology_associated_with_entity_relationship import TopologyAssociatedWithEntityRelationship
from .topology_associated_with_relationship_details import TopologyAssociatedWithRelationshipDetails
from .topology_contains_entity_relationship import TopologyContainsEntityRelationship
from .topology_entity_relationship import TopologyEntityRelationship
from .topology_routes_to_entity_relationship import TopologyRoutesToEntityRelationship
from .topology_routes_to_relationship_details import TopologyRoutesToRelationshipDetails
from .traffic_node import TrafficNode
from .traffic_protocol_parameters import TrafficProtocolParameters
from .traffic_route import TrafficRoute
from .tunnel_config import TunnelConfig
from .tunnel_status import TunnelStatus
from .udp_options import UdpOptions
from .udp_protocol_parameters import UdpProtocolParameters
from .udp_traffic_protocol_parameters import UdpTrafficProtocolParameters
from .update_cpe_details import UpdateCpeDetails
from .update_cross_connect_details import UpdateCrossConnectDetails
from .update_cross_connect_group_details import UpdateCrossConnectGroupDetails
from .update_dhcp_details import UpdateDhcpDetails
from .update_drg_attachment_details import UpdateDrgAttachmentDetails
from .update_drg_details import UpdateDrgDetails
from .update_drg_route_distribution_details import UpdateDrgRouteDistributionDetails
from .update_drg_route_distribution_statement_details import UpdateDrgRouteDistributionStatementDetails
from .update_drg_route_distribution_statements_details import UpdateDrgRouteDistributionStatementsDetails
from .update_drg_route_rule_details import UpdateDrgRouteRuleDetails
from .update_drg_route_rules_details import UpdateDrgRouteRulesDetails
from .update_drg_route_table_details import UpdateDrgRouteTableDetails
from .update_ip_sec_connection_details import UpdateIPSecConnectionDetails
from .update_internet_gateway_details import UpdateInternetGatewayDetails
from .update_ipv6_details import UpdateIpv6Details
from .update_local_peering_gateway_details import UpdateLocalPeeringGatewayDetails
from .update_network_security_group_details import UpdateNetworkSecurityGroupDetails
from .update_network_security_group_security_rules_details import UpdateNetworkSecurityGroupSecurityRulesDetails
from .update_path_analyzer_test_details import UpdatePathAnalyzerTestDetails
from .update_private_ip_details import UpdatePrivateIpDetails
from .update_public_ip_details import UpdatePublicIpDetails
from .update_remote_peering_connection_details import UpdateRemotePeeringConnectionDetails
from .update_route_table_details import UpdateRouteTableDetails
from .update_security_list_details import UpdateSecurityListDetails
from .update_security_rule_details import UpdateSecurityRuleDetails
from .update_service_gateway_details import UpdateServiceGatewayDetails
from .update_subnet_details import UpdateSubnetDetails
from .update_vcn_details import UpdateVcnDetails
from .update_virtual_circuit_details import UpdateVirtualCircuitDetails
from .update_vnic_details import UpdateVnicDetails
from .updated_network_security_group_security_rules import UpdatedNetworkSecurityGroupSecurityRules
from .upgrade_status import UpgradeStatus
from .vcn import Vcn
from .vcn_drg_attachment_network_create_details import VcnDrgAttachmentNetworkCreateDetails
from .vcn_drg_attachment_network_details import VcnDrgAttachmentNetworkDetails
from .vcn_drg_attachment_network_update_details import VcnDrgAttachmentNetworkUpdateDetails
from .vcn_routing_configuration import VcnRoutingConfiguration
from .vcn_topology import VcnTopology
from .virtual_circuit import VirtualCircuit
from .virtual_circuit_bandwidth_shape import VirtualCircuitBandwidthShape
from .virtual_circuit_drg_attachment_network_details import VirtualCircuitDrgAttachmentNetworkDetails
from .virtual_circuit_public_prefix import VirtualCircuitPublicPrefix
from .visible_traffic_node import VisibleTrafficNode
from .vlan_endpoint import VlanEndpoint
from .vnic import Vnic
from .vnic_endpoint import VnicEndpoint
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource
from .work_request_result import WorkRequestResult
from .work_request_result_collection import WorkRequestResultCollection
from .work_request_summary import WorkRequestSummary
from .work_request_summary_collection import WorkRequestSummaryCollection

# Maps type names to classes for vn_monitoring services.
vn_monitoring_type_mapping = {
    "AccessDeniedTrafficNode": AccessDeniedTrafficNode,
    "AddDrgRouteDistributionStatementDetails": AddDrgRouteDistributionStatementDetails,
    "AddDrgRouteDistributionStatementsDetails": AddDrgRouteDistributionStatementsDetails,
    "AddDrgRouteRuleDetails": AddDrgRouteRuleDetails,
    "AddDrgRouteRulesDetails": AddDrgRouteRulesDetails,
    "AddNetworkSecurityGroupSecurityRulesDetails": AddNetworkSecurityGroupSecurityRulesDetails,
    "AddSecurityRuleDetails": AddSecurityRuleDetails,
    "AddedNetworkSecurityGroupSecurityRules": AddedNetworkSecurityGroupSecurityRules,
    "AdhocGetPathAnalysisDetails": AdhocGetPathAnalysisDetails,
    "AllowedSecurityAction": AllowedSecurityAction,
    "AllowedSecurityActionDetails": AllowedSecurityActionDetails,
    "AllowedSecurityConfiguration": AllowedSecurityConfiguration,
    "BulkAddVirtualCircuitPublicPrefixesDetails": BulkAddVirtualCircuitPublicPrefixesDetails,
    "BulkDeleteVirtualCircuitPublicPrefixesDetails": BulkDeleteVirtualCircuitPublicPrefixesDetails,
    "ChangePathAnalyzerTestCompartmentDetails": ChangePathAnalyzerTestCompartmentDetails,
    "CompartmentInternal": CompartmentInternal,
    "ComputeInstanceEndpoint": ComputeInstanceEndpoint,
    "ConnectLocalPeeringGatewaysDetails": ConnectLocalPeeringGatewaysDetails,
    "ConnectRemotePeeringConnectionsDetails": ConnectRemotePeeringConnectionsDetails,
    "Cpe": Cpe,
    "CreateCpeDetails": CreateCpeDetails,
    "CreateCrossConnectDetails": CreateCrossConnectDetails,
    "CreateCrossConnectGroupDetails": CreateCrossConnectGroupDetails,
    "CreateDhcpDetails": CreateDhcpDetails,
    "CreateDrgAttachmentDetails": CreateDrgAttachmentDetails,
    "CreateDrgDetails": CreateDrgDetails,
    "CreateDrgRouteDistributionDetails": CreateDrgRouteDistributionDetails,
    "CreateDrgRouteTableDetails": CreateDrgRouteTableDetails,
    "CreateIPSecConnectionDetails": CreateIPSecConnectionDetails,
    "CreateInternetGatewayDetails": CreateInternetGatewayDetails,
    "CreateIpv6Details": CreateIpv6Details,
    "CreateLocalPeeringGatewayDetails": CreateLocalPeeringGatewayDetails,
    "CreateNetworkSecurityGroupDetails": CreateNetworkSecurityGroupDetails,
    "CreatePathAnalyzerTestDetails": CreatePathAnalyzerTestDetails,
    "CreatePrivateIpDetails": CreatePrivateIpDetails,
    "CreatePublicIpDetails": CreatePublicIpDetails,
    "CreateRemotePeeringConnectionDetails": CreateRemotePeeringConnectionDetails,
    "CreateRouteTableDetails": CreateRouteTableDetails,
    "CreateSecurityListDetails": CreateSecurityListDetails,
    "CreateServiceGatewayDetails": CreateServiceGatewayDetails,
    "CreateSubnetDetails": CreateSubnetDetails,
    "CreateVcnDetails": CreateVcnDetails,
    "CreateVirtualCircuitDetails": CreateVirtualCircuitDetails,
    "CreateVirtualCircuitPublicPrefixDetails": CreateVirtualCircuitPublicPrefixDetails,
    "CreateVnicDetails": CreateVnicDetails,
    "CrossConnect": CrossConnect,
    "CrossConnectGroup": CrossConnectGroup,
    "CrossConnectLocation": CrossConnectLocation,
    "CrossConnectMapping": CrossConnectMapping,
    "CrossConnectPortSpeedShape": CrossConnectPortSpeedShape,
    "CrossConnectStatus": CrossConnectStatus,
    "DefaultDrgRouteTables": DefaultDrgRouteTables,
    "DeleteVirtualCircuitPublicPrefixDetails": DeleteVirtualCircuitPublicPrefixDetails,
    "DeniedSecurityAction": DeniedSecurityAction,
    "DeniedSecurityActionDetails": DeniedSecurityActionDetails,
    "DhcpDnsOption": DhcpDnsOption,
    "DhcpOption": DhcpOption,
    "DhcpOptions": DhcpOptions,
    "DhcpSearchDomainOption": DhcpSearchDomainOption,
    "Drg": Drg,
    "DrgAttachment": DrgAttachment,
    "DrgAttachmentIdDrgRouteDistributionMatchCriteria": DrgAttachmentIdDrgRouteDistributionMatchCriteria,
    "DrgAttachmentInfo": DrgAttachmentInfo,
    "DrgAttachmentNetworkCreateDetails": DrgAttachmentNetworkCreateDetails,
    "DrgAttachmentNetworkDetails": DrgAttachmentNetworkDetails,
    "DrgAttachmentNetworkUpdateDetails": DrgAttachmentNetworkUpdateDetails,
    "DrgAttachmentTypeDrgRouteDistributionMatchCriteria": DrgAttachmentTypeDrgRouteDistributionMatchCriteria,
    "DrgRouteDistribution": DrgRouteDistribution,
    "DrgRouteDistributionMatchCriteria": DrgRouteDistributionMatchCriteria,
    "DrgRouteDistributionStatement": DrgRouteDistributionStatement,
    "DrgRouteRule": DrgRouteRule,
    "DrgRouteTable": DrgRouteTable,
    "DrgRoutingConfiguration": DrgRoutingConfiguration,
    "EgressSecurityListConfiguration": EgressSecurityListConfiguration,
    "EgressSecurityRule": EgressSecurityRule,
    "EgressTrafficSpec": EgressTrafficSpec,
    "Endpoint": Endpoint,
    "FastConnectProviderService": FastConnectProviderService,
    "ForwardedRoutingAction": ForwardedRoutingAction,
    "ForwardedRoutingActionDetails": ForwardedRoutingActionDetails,
    "ForwardedRoutingConfiguration": ForwardedRoutingConfiguration,
    "GetPathAnalysisDetails": GetPathAnalysisDetails,
    "GetPublicIpByIpAddressDetails": GetPublicIpByIpAddressDetails,
    "GetPublicIpByPrivateIpIdDetails": GetPublicIpByPrivateIpIdDetails,
    "IPSecConnection": IPSecConnection,
    "IPSecConnectionDeviceConfig": IPSecConnectionDeviceConfig,
    "IPSecConnectionDeviceStatus": IPSecConnectionDeviceStatus,
    "IcmpOptions": IcmpOptions,
    "IcmpProtocolParameters": IcmpProtocolParameters,
    "IcmpTrafficProtocolParameters": IcmpTrafficProtocolParameters,
    "IndeterminateRoutingAction": IndeterminateRoutingAction,
    "IngressSecurityListConfiguration": IngressSecurityListConfiguration,
    "IngressSecurityRule": IngressSecurityRule,
    "InternetGateway": InternetGateway,
    "IpAddressEndpoint": IpAddressEndpoint,
    "IpsecTunnelDrgAttachmentNetworkDetails": IpsecTunnelDrgAttachmentNetworkDetails,
    "Ipv6": Ipv6,
    "LetterOfAuthority": LetterOfAuthority,
    "LoadBalancerEndpoint": LoadBalancerEndpoint,
    "LoadBalancerListenerEndpoint": LoadBalancerListenerEndpoint,
    "LocalPeeringGateway": LocalPeeringGateway,
    "NetworkLoadBalancerEndpoint": NetworkLoadBalancerEndpoint,
    "NetworkLoadBalancerListenerEndpoint": NetworkLoadBalancerListenerEndpoint,
    "NetworkSecurityGroup": NetworkSecurityGroup,
    "NetworkSecurityGroupVnic": NetworkSecurityGroupVnic,
    "NetworkingTopology": NetworkingTopology,
    "NoRouteRoutingAction": NoRouteRoutingAction,
    "NoRouteRoutingActionDetails": NoRouteRoutingActionDetails,
    "NsgConfiguration": NsgConfiguration,
    "Path": Path,
    "PathAnalysisWorkRequestResult": PathAnalysisWorkRequestResult,
    "PathAnalyzerTest": PathAnalyzerTest,
    "PathAnalyzerTestCollection": PathAnalyzerTestCollection,
    "PathAnalyzerTestSummary": PathAnalyzerTestSummary,
    "PathTopology": PathTopology,
    "PersistedGetPathAnalysisDetails": PersistedGetPathAnalysisDetails,
    "PortRange": PortRange,
    "PrivateIp": PrivateIp,
    "ProtocolParameters": ProtocolParameters,
    "PublicIp": PublicIp,
    "QueryOptions": QueryOptions,
    "RemotePeeringConnection": RemotePeeringConnection,
    "RemotePeeringConnectionDrgAttachmentNetworkDetails": RemotePeeringConnectionDrgAttachmentNetworkDetails,
    "RemoveDrgRouteDistributionStatementsDetails": RemoveDrgRouteDistributionStatementsDetails,
    "RemoveDrgRouteRulesDetails": RemoveDrgRouteRulesDetails,
    "RemoveNetworkSecurityGroupSecurityRulesDetails": RemoveNetworkSecurityGroupSecurityRulesDetails,
    "RouteRule": RouteRule,
    "RouteTable": RouteTable,
    "RoutingAction": RoutingAction,
    "SecurityAction": SecurityAction,
    "SecurityList": SecurityList,
    "SecurityRule": SecurityRule,
    "Service": Service,
    "ServiceGateway": ServiceGateway,
    "ServiceIdRequestDetails": ServiceIdRequestDetails,
    "ServiceIdResponseDetails": ServiceIdResponseDetails,
    "StatefulEgressSecurityListConfiguration": StatefulEgressSecurityListConfiguration,
    "StatefulIngressSecurityListConfiguration": StatefulIngressSecurityListConfiguration,
    "StatefulNsgConfiguration": StatefulNsgConfiguration,
    "Subnet": Subnet,
    "SubnetEndpoint": SubnetEndpoint,
    "SubnetTopology": SubnetTopology,
    "TcpOptions": TcpOptions,
    "TcpProtocolParameters": TcpProtocolParameters,
    "TcpTrafficProtocolParameters": TcpTrafficProtocolParameters,
    "Topology": Topology,
    "TopologyAssociatedWithEntityRelationship": TopologyAssociatedWithEntityRelationship,
    "TopologyAssociatedWithRelationshipDetails": TopologyAssociatedWithRelationshipDetails,
    "TopologyContainsEntityRelationship": TopologyContainsEntityRelationship,
    "TopologyEntityRelationship": TopologyEntityRelationship,
    "TopologyRoutesToEntityRelationship": TopologyRoutesToEntityRelationship,
    "TopologyRoutesToRelationshipDetails": TopologyRoutesToRelationshipDetails,
    "TrafficNode": TrafficNode,
    "TrafficProtocolParameters": TrafficProtocolParameters,
    "TrafficRoute": TrafficRoute,
    "TunnelConfig": TunnelConfig,
    "TunnelStatus": TunnelStatus,
    "UdpOptions": UdpOptions,
    "UdpProtocolParameters": UdpProtocolParameters,
    "UdpTrafficProtocolParameters": UdpTrafficProtocolParameters,
    "UpdateCpeDetails": UpdateCpeDetails,
    "UpdateCrossConnectDetails": UpdateCrossConnectDetails,
    "UpdateCrossConnectGroupDetails": UpdateCrossConnectGroupDetails,
    "UpdateDhcpDetails": UpdateDhcpDetails,
    "UpdateDrgAttachmentDetails": UpdateDrgAttachmentDetails,
    "UpdateDrgDetails": UpdateDrgDetails,
    "UpdateDrgRouteDistributionDetails": UpdateDrgRouteDistributionDetails,
    "UpdateDrgRouteDistributionStatementDetails": UpdateDrgRouteDistributionStatementDetails,
    "UpdateDrgRouteDistributionStatementsDetails": UpdateDrgRouteDistributionStatementsDetails,
    "UpdateDrgRouteRuleDetails": UpdateDrgRouteRuleDetails,
    "UpdateDrgRouteRulesDetails": UpdateDrgRouteRulesDetails,
    "UpdateDrgRouteTableDetails": UpdateDrgRouteTableDetails,
    "UpdateIPSecConnectionDetails": UpdateIPSecConnectionDetails,
    "UpdateInternetGatewayDetails": UpdateInternetGatewayDetails,
    "UpdateIpv6Details": UpdateIpv6Details,
    "UpdateLocalPeeringGatewayDetails": UpdateLocalPeeringGatewayDetails,
    "UpdateNetworkSecurityGroupDetails": UpdateNetworkSecurityGroupDetails,
    "UpdateNetworkSecurityGroupSecurityRulesDetails": UpdateNetworkSecurityGroupSecurityRulesDetails,
    "UpdatePathAnalyzerTestDetails": UpdatePathAnalyzerTestDetails,
    "UpdatePrivateIpDetails": UpdatePrivateIpDetails,
    "UpdatePublicIpDetails": UpdatePublicIpDetails,
    "UpdateRemotePeeringConnectionDetails": UpdateRemotePeeringConnectionDetails,
    "UpdateRouteTableDetails": UpdateRouteTableDetails,
    "UpdateSecurityListDetails": UpdateSecurityListDetails,
    "UpdateSecurityRuleDetails": UpdateSecurityRuleDetails,
    "UpdateServiceGatewayDetails": UpdateServiceGatewayDetails,
    "UpdateSubnetDetails": UpdateSubnetDetails,
    "UpdateVcnDetails": UpdateVcnDetails,
    "UpdateVirtualCircuitDetails": UpdateVirtualCircuitDetails,
    "UpdateVnicDetails": UpdateVnicDetails,
    "UpdatedNetworkSecurityGroupSecurityRules": UpdatedNetworkSecurityGroupSecurityRules,
    "UpgradeStatus": UpgradeStatus,
    "Vcn": Vcn,
    "VcnDrgAttachmentNetworkCreateDetails": VcnDrgAttachmentNetworkCreateDetails,
    "VcnDrgAttachmentNetworkDetails": VcnDrgAttachmentNetworkDetails,
    "VcnDrgAttachmentNetworkUpdateDetails": VcnDrgAttachmentNetworkUpdateDetails,
    "VcnRoutingConfiguration": VcnRoutingConfiguration,
    "VcnTopology": VcnTopology,
    "VirtualCircuit": VirtualCircuit,
    "VirtualCircuitBandwidthShape": VirtualCircuitBandwidthShape,
    "VirtualCircuitDrgAttachmentNetworkDetails": VirtualCircuitDrgAttachmentNetworkDetails,
    "VirtualCircuitPublicPrefix": VirtualCircuitPublicPrefix,
    "VisibleTrafficNode": VisibleTrafficNode,
    "VlanEndpoint": VlanEndpoint,
    "Vnic": Vnic,
    "VnicEndpoint": VnicEndpoint,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestResult": WorkRequestResult,
    "WorkRequestResultCollection": WorkRequestResultCollection,
    "WorkRequestSummary": WorkRequestSummary,
    "WorkRequestSummaryCollection": WorkRequestSummaryCollection
}
