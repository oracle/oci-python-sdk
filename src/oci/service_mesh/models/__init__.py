# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .access_logging_configuration import AccessLoggingConfiguration
from .access_policy import AccessPolicy
from .access_policy_collection import AccessPolicyCollection
from .access_policy_rule import AccessPolicyRule
from .access_policy_summary import AccessPolicySummary
from .access_policy_target import AccessPolicyTarget
from .all_virtual_services_access_policy_target import AllVirtualServicesAccessPolicyTarget
from .ca_bundle import CaBundle
from .certificate_authority import CertificateAuthority
from .change_access_policy_compartment_details import ChangeAccessPolicyCompartmentDetails
from .change_ingress_gateway_compartment_details import ChangeIngressGatewayCompartmentDetails
from .change_ingress_gateway_route_table_compartment_details import ChangeIngressGatewayRouteTableCompartmentDetails
from .change_mesh_compartment_details import ChangeMeshCompartmentDetails
from .change_virtual_deployment_compartment_details import ChangeVirtualDeploymentCompartmentDetails
from .change_virtual_service_compartment_details import ChangeVirtualServiceCompartmentDetails
from .change_virtual_service_route_table_compartment_details import ChangeVirtualServiceRouteTableCompartmentDetails
from .create_access_policy_details import CreateAccessPolicyDetails
from .create_ingress_gateway_details import CreateIngressGatewayDetails
from .create_ingress_gateway_mutual_transport_layer_security_details import CreateIngressGatewayMutualTransportLayerSecurityDetails
from .create_ingress_gateway_route_table_details import CreateIngressGatewayRouteTableDetails
from .create_mesh_details import CreateMeshDetails
from .create_mutual_transport_layer_security_details import CreateMutualTransportLayerSecurityDetails
from .create_virtual_deployment_details import CreateVirtualDeploymentDetails
from .create_virtual_service_details import CreateVirtualServiceDetails
from .create_virtual_service_route_table_details import CreateVirtualServiceRouteTableDetails
from .default_virtual_service_routing_policy import DefaultVirtualServiceRoutingPolicy
from .dns_service_discovery_configuration import DnsServiceDiscoveryConfiguration
from .external_service_access_policy_target import ExternalServiceAccessPolicyTarget
from .http_ingress_gateway_traffic_route_rule import HttpIngressGatewayTrafficRouteRule
from .http_virtual_service_traffic_route_rule import HttpVirtualServiceTrafficRouteRule
from .ingress_gateway import IngressGateway
from .ingress_gateway_access_policy_target import IngressGatewayAccessPolicyTarget
from .ingress_gateway_collection import IngressGatewayCollection
from .ingress_gateway_host import IngressGatewayHost
from .ingress_gateway_host_ref import IngressGatewayHostRef
from .ingress_gateway_listener import IngressGatewayListener
from .ingress_gateway_mutual_transport_layer_security import IngressGatewayMutualTransportLayerSecurity
from .ingress_gateway_route_table import IngressGatewayRouteTable
from .ingress_gateway_route_table_collection import IngressGatewayRouteTableCollection
from .ingress_gateway_route_table_summary import IngressGatewayRouteTableSummary
from .ingress_gateway_summary import IngressGatewaySummary
from .ingress_gateway_traffic_route_rule import IngressGatewayTrafficRouteRule
from .ingress_listener_client_validation_config import IngressListenerClientValidationConfig
from .ingress_listener_tls_config import IngressListenerTlsConfig
from .local_file_ca_bundle import LocalFileCaBundle
from .local_file_tls_certificate import LocalFileTlsCertificate
from .mesh import Mesh
from .mesh_collection import MeshCollection
from .mesh_mutual_transport_layer_security import MeshMutualTransportLayerSecurity
from .mesh_summary import MeshSummary
from .mutual_transport_layer_security import MutualTransportLayerSecurity
from .oci_ca_bundle import OciCaBundle
from .oci_tls_certificate import OciTlsCertificate
from .proxy_details import ProxyDetails
from .service_discovery_configuration import ServiceDiscoveryConfiguration
from .tcp_ingress_gateway_traffic_route_rule import TcpIngressGatewayTrafficRouteRule
from .tcp_virtual_service_traffic_route_rule import TcpVirtualServiceTrafficRouteRule
from .tls_certificate import TlsCertificate
from .tls_passthrough_ingress_gateway_traffic_route_rule import TlsPassthroughIngressGatewayTrafficRouteRule
from .tls_passthrough_virtual_service_traffic_route_rule import TlsPassthroughVirtualServiceTrafficRouteRule
from .traffic_rule_target import TrafficRuleTarget
from .update_access_policy_details import UpdateAccessPolicyDetails
from .update_ingress_gateway_details import UpdateIngressGatewayDetails
from .update_ingress_gateway_route_table_details import UpdateIngressGatewayRouteTableDetails
from .update_mesh_details import UpdateMeshDetails
from .update_virtual_deployment_details import UpdateVirtualDeploymentDetails
from .update_virtual_service_details import UpdateVirtualServiceDetails
from .update_virtual_service_route_table_details import UpdateVirtualServiceRouteTableDetails
from .virtual_deployment import VirtualDeployment
from .virtual_deployment_collection import VirtualDeploymentCollection
from .virtual_deployment_listener import VirtualDeploymentListener
from .virtual_deployment_summary import VirtualDeploymentSummary
from .virtual_deployment_traffic_rule_target import VirtualDeploymentTrafficRuleTarget
from .virtual_service import VirtualService
from .virtual_service_access_policy_target import VirtualServiceAccessPolicyTarget
from .virtual_service_collection import VirtualServiceCollection
from .virtual_service_route_table import VirtualServiceRouteTable
from .virtual_service_route_table_collection import VirtualServiceRouteTableCollection
from .virtual_service_route_table_summary import VirtualServiceRouteTableSummary
from .virtual_service_summary import VirtualServiceSummary
from .virtual_service_traffic_route_rule import VirtualServiceTrafficRouteRule
from .virtual_service_traffic_rule_target import VirtualServiceTrafficRuleTarget
from .work_request import WorkRequest
from .work_request_collection import WorkRequestCollection
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary

# Maps type names to classes for service_mesh services.
service_mesh_type_mapping = {
    "AccessLoggingConfiguration": AccessLoggingConfiguration,
    "AccessPolicy": AccessPolicy,
    "AccessPolicyCollection": AccessPolicyCollection,
    "AccessPolicyRule": AccessPolicyRule,
    "AccessPolicySummary": AccessPolicySummary,
    "AccessPolicyTarget": AccessPolicyTarget,
    "AllVirtualServicesAccessPolicyTarget": AllVirtualServicesAccessPolicyTarget,
    "CaBundle": CaBundle,
    "CertificateAuthority": CertificateAuthority,
    "ChangeAccessPolicyCompartmentDetails": ChangeAccessPolicyCompartmentDetails,
    "ChangeIngressGatewayCompartmentDetails": ChangeIngressGatewayCompartmentDetails,
    "ChangeIngressGatewayRouteTableCompartmentDetails": ChangeIngressGatewayRouteTableCompartmentDetails,
    "ChangeMeshCompartmentDetails": ChangeMeshCompartmentDetails,
    "ChangeVirtualDeploymentCompartmentDetails": ChangeVirtualDeploymentCompartmentDetails,
    "ChangeVirtualServiceCompartmentDetails": ChangeVirtualServiceCompartmentDetails,
    "ChangeVirtualServiceRouteTableCompartmentDetails": ChangeVirtualServiceRouteTableCompartmentDetails,
    "CreateAccessPolicyDetails": CreateAccessPolicyDetails,
    "CreateIngressGatewayDetails": CreateIngressGatewayDetails,
    "CreateIngressGatewayMutualTransportLayerSecurityDetails": CreateIngressGatewayMutualTransportLayerSecurityDetails,
    "CreateIngressGatewayRouteTableDetails": CreateIngressGatewayRouteTableDetails,
    "CreateMeshDetails": CreateMeshDetails,
    "CreateMutualTransportLayerSecurityDetails": CreateMutualTransportLayerSecurityDetails,
    "CreateVirtualDeploymentDetails": CreateVirtualDeploymentDetails,
    "CreateVirtualServiceDetails": CreateVirtualServiceDetails,
    "CreateVirtualServiceRouteTableDetails": CreateVirtualServiceRouteTableDetails,
    "DefaultVirtualServiceRoutingPolicy": DefaultVirtualServiceRoutingPolicy,
    "DnsServiceDiscoveryConfiguration": DnsServiceDiscoveryConfiguration,
    "ExternalServiceAccessPolicyTarget": ExternalServiceAccessPolicyTarget,
    "HttpIngressGatewayTrafficRouteRule": HttpIngressGatewayTrafficRouteRule,
    "HttpVirtualServiceTrafficRouteRule": HttpVirtualServiceTrafficRouteRule,
    "IngressGateway": IngressGateway,
    "IngressGatewayAccessPolicyTarget": IngressGatewayAccessPolicyTarget,
    "IngressGatewayCollection": IngressGatewayCollection,
    "IngressGatewayHost": IngressGatewayHost,
    "IngressGatewayHostRef": IngressGatewayHostRef,
    "IngressGatewayListener": IngressGatewayListener,
    "IngressGatewayMutualTransportLayerSecurity": IngressGatewayMutualTransportLayerSecurity,
    "IngressGatewayRouteTable": IngressGatewayRouteTable,
    "IngressGatewayRouteTableCollection": IngressGatewayRouteTableCollection,
    "IngressGatewayRouteTableSummary": IngressGatewayRouteTableSummary,
    "IngressGatewaySummary": IngressGatewaySummary,
    "IngressGatewayTrafficRouteRule": IngressGatewayTrafficRouteRule,
    "IngressListenerClientValidationConfig": IngressListenerClientValidationConfig,
    "IngressListenerTlsConfig": IngressListenerTlsConfig,
    "LocalFileCaBundle": LocalFileCaBundle,
    "LocalFileTlsCertificate": LocalFileTlsCertificate,
    "Mesh": Mesh,
    "MeshCollection": MeshCollection,
    "MeshMutualTransportLayerSecurity": MeshMutualTransportLayerSecurity,
    "MeshSummary": MeshSummary,
    "MutualTransportLayerSecurity": MutualTransportLayerSecurity,
    "OciCaBundle": OciCaBundle,
    "OciTlsCertificate": OciTlsCertificate,
    "ProxyDetails": ProxyDetails,
    "ServiceDiscoveryConfiguration": ServiceDiscoveryConfiguration,
    "TcpIngressGatewayTrafficRouteRule": TcpIngressGatewayTrafficRouteRule,
    "TcpVirtualServiceTrafficRouteRule": TcpVirtualServiceTrafficRouteRule,
    "TlsCertificate": TlsCertificate,
    "TlsPassthroughIngressGatewayTrafficRouteRule": TlsPassthroughIngressGatewayTrafficRouteRule,
    "TlsPassthroughVirtualServiceTrafficRouteRule": TlsPassthroughVirtualServiceTrafficRouteRule,
    "TrafficRuleTarget": TrafficRuleTarget,
    "UpdateAccessPolicyDetails": UpdateAccessPolicyDetails,
    "UpdateIngressGatewayDetails": UpdateIngressGatewayDetails,
    "UpdateIngressGatewayRouteTableDetails": UpdateIngressGatewayRouteTableDetails,
    "UpdateMeshDetails": UpdateMeshDetails,
    "UpdateVirtualDeploymentDetails": UpdateVirtualDeploymentDetails,
    "UpdateVirtualServiceDetails": UpdateVirtualServiceDetails,
    "UpdateVirtualServiceRouteTableDetails": UpdateVirtualServiceRouteTableDetails,
    "VirtualDeployment": VirtualDeployment,
    "VirtualDeploymentCollection": VirtualDeploymentCollection,
    "VirtualDeploymentListener": VirtualDeploymentListener,
    "VirtualDeploymentSummary": VirtualDeploymentSummary,
    "VirtualDeploymentTrafficRuleTarget": VirtualDeploymentTrafficRuleTarget,
    "VirtualService": VirtualService,
    "VirtualServiceAccessPolicyTarget": VirtualServiceAccessPolicyTarget,
    "VirtualServiceCollection": VirtualServiceCollection,
    "VirtualServiceRouteTable": VirtualServiceRouteTable,
    "VirtualServiceRouteTableCollection": VirtualServiceRouteTableCollection,
    "VirtualServiceRouteTableSummary": VirtualServiceRouteTableSummary,
    "VirtualServiceSummary": VirtualServiceSummary,
    "VirtualServiceTrafficRouteRule": VirtualServiceTrafficRouteRule,
    "VirtualServiceTrafficRuleTarget": VirtualServiceTrafficRuleTarget,
    "WorkRequest": WorkRequest,
    "WorkRequestCollection": WorkRequestCollection,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}
