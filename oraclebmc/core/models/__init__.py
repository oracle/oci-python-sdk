# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from .attach_i_scsi_volume_details import AttachIScsiVolumeDetails
from .attach_volume_details import AttachVolumeDetails
from .capture_console_history_details import CaptureConsoleHistoryDetails
from .console_history import ConsoleHistory
from .cpe import Cpe
from .create_cpe_details import CreateCpeDetails
from .create_cross_connect_details import CreateCrossConnectDetails
from .create_cross_connect_group_details import CreateCrossConnectGroupDetails
from .create_dhcp_details import CreateDhcpDetails
from .create_drg_attachment_details import CreateDrgAttachmentDetails
from .create_drg_details import CreateDrgDetails
from .create_ip_sec_connection_details import CreateIPSecConnectionDetails
from .create_image_details import CreateImageDetails
from .create_internet_gateway_details import CreateInternetGatewayDetails
from .create_route_table_details import CreateRouteTableDetails
from .create_security_list_details import CreateSecurityListDetails
from .create_subnet_details import CreateSubnetDetails
from .create_vcn_details import CreateVcnDetails
from .create_virtual_circuit_details import CreateVirtualCircuitDetails
from .create_vnic_details import CreateVnicDetails
from .create_volume_backup_details import CreateVolumeBackupDetails
from .create_volume_details import CreateVolumeDetails
from .cross_connect import CrossConnect
from .cross_connect_group import CrossConnectGroup
from .cross_connect_location import CrossConnectLocation
from .cross_connect_mapping import CrossConnectMapping
from .cross_connect_port_speed_shape import CrossConnectPortSpeedShape
from .cross_connect_status import CrossConnectStatus
from .dhcp_dns_option import DhcpDnsOption
from .dhcp_option import DhcpOption
from .dhcp_options import DhcpOptions
from .dhcp_search_domain_option import DhcpSearchDomainOption
from .drg import Drg
from .drg_attachment import DrgAttachment
from .egress_security_rule import EgressSecurityRule
from .fast_connect_provider_service import FastConnectProviderService
from .ip_sec_connection import IPSecConnection
from .ip_sec_connection_device_config import IPSecConnectionDeviceConfig
from .ip_sec_connection_device_status import IPSecConnectionDeviceStatus
from .i_scsi_volume_attachment import IScsiVolumeAttachment
from .icmp_options import IcmpOptions
from .image import Image
from .ingress_security_rule import IngressSecurityRule
from .instance import Instance
from .instance_credentials import InstanceCredentials
from .internet_gateway import InternetGateway
from .launch_instance_details import LaunchInstanceDetails
from .letter_of_authority import LetterOfAuthority
from .port_range import PortRange
from .route_rule import RouteRule
from .route_table import RouteTable
from .security_list import SecurityList
from .shape import Shape
from .subnet import Subnet
from .tcp_options import TcpOptions
from .tunnel_config import TunnelConfig
from .tunnel_status import TunnelStatus
from .udp_options import UdpOptions
from .update_cpe_details import UpdateCpeDetails
from .update_cross_connect_details import UpdateCrossConnectDetails
from .update_cross_connect_group_details import UpdateCrossConnectGroupDetails
from .update_dhcp_details import UpdateDhcpDetails
from .update_drg_attachment_details import UpdateDrgAttachmentDetails
from .update_drg_details import UpdateDrgDetails
from .update_ip_sec_connection_details import UpdateIPSecConnectionDetails
from .update_image_details import UpdateImageDetails
from .update_instance_details import UpdateInstanceDetails
from .update_internet_gateway_details import UpdateInternetGatewayDetails
from .update_route_table_details import UpdateRouteTableDetails
from .update_security_list_details import UpdateSecurityListDetails
from .update_subnet_details import UpdateSubnetDetails
from .update_vcn_details import UpdateVcnDetails
from .update_virtual_circuit_details import UpdateVirtualCircuitDetails
from .update_volume_backup_details import UpdateVolumeBackupDetails
from .update_volume_details import UpdateVolumeDetails
from .vcn import Vcn
from .virtual_circuit import VirtualCircuit
from .virtual_circuit_bandwidth_shape import VirtualCircuitBandwidthShape
from .vnic import Vnic
from .vnic_attachment import VnicAttachment
from .volume import Volume
from .volume_attachment import VolumeAttachment
from .volume_backup import VolumeBackup

# Maps type names to classes for core services.
core_type_mapping = {
    "AttachIScsiVolumeDetails": AttachIScsiVolumeDetails,
    "AttachVolumeDetails": AttachVolumeDetails,
    "CaptureConsoleHistoryDetails": CaptureConsoleHistoryDetails,
    "ConsoleHistory": ConsoleHistory,
    "Cpe": Cpe,
    "CreateCpeDetails": CreateCpeDetails,
    "CreateCrossConnectDetails": CreateCrossConnectDetails,
    "CreateCrossConnectGroupDetails": CreateCrossConnectGroupDetails,
    "CreateDhcpDetails": CreateDhcpDetails,
    "CreateDrgAttachmentDetails": CreateDrgAttachmentDetails,
    "CreateDrgDetails": CreateDrgDetails,
    "CreateIPSecConnectionDetails": CreateIPSecConnectionDetails,
    "CreateImageDetails": CreateImageDetails,
    "CreateInternetGatewayDetails": CreateInternetGatewayDetails,
    "CreateRouteTableDetails": CreateRouteTableDetails,
    "CreateSecurityListDetails": CreateSecurityListDetails,
    "CreateSubnetDetails": CreateSubnetDetails,
    "CreateVcnDetails": CreateVcnDetails,
    "CreateVirtualCircuitDetails": CreateVirtualCircuitDetails,
    "CreateVnicDetails": CreateVnicDetails,
    "CreateVolumeBackupDetails": CreateVolumeBackupDetails,
    "CreateVolumeDetails": CreateVolumeDetails,
    "CrossConnect": CrossConnect,
    "CrossConnectGroup": CrossConnectGroup,
    "CrossConnectLocation": CrossConnectLocation,
    "CrossConnectMapping": CrossConnectMapping,
    "CrossConnectPortSpeedShape": CrossConnectPortSpeedShape,
    "CrossConnectStatus": CrossConnectStatus,
    "DhcpDnsOption": DhcpDnsOption,
    "DhcpOption": DhcpOption,
    "DhcpOptions": DhcpOptions,
    "DhcpSearchDomainOption": DhcpSearchDomainOption,
    "Drg": Drg,
    "DrgAttachment": DrgAttachment,
    "EgressSecurityRule": EgressSecurityRule,
    "FastConnectProviderService": FastConnectProviderService,
    "IPSecConnection": IPSecConnection,
    "IPSecConnectionDeviceConfig": IPSecConnectionDeviceConfig,
    "IPSecConnectionDeviceStatus": IPSecConnectionDeviceStatus,
    "IScsiVolumeAttachment": IScsiVolumeAttachment,
    "IcmpOptions": IcmpOptions,
    "Image": Image,
    "IngressSecurityRule": IngressSecurityRule,
    "Instance": Instance,
    "InstanceCredentials": InstanceCredentials,
    "InternetGateway": InternetGateway,
    "LaunchInstanceDetails": LaunchInstanceDetails,
    "LetterOfAuthority": LetterOfAuthority,
    "PortRange": PortRange,
    "RouteRule": RouteRule,
    "RouteTable": RouteTable,
    "SecurityList": SecurityList,
    "Shape": Shape,
    "Subnet": Subnet,
    "TcpOptions": TcpOptions,
    "TunnelConfig": TunnelConfig,
    "TunnelStatus": TunnelStatus,
    "UdpOptions": UdpOptions,
    "UpdateCpeDetails": UpdateCpeDetails,
    "UpdateCrossConnectDetails": UpdateCrossConnectDetails,
    "UpdateCrossConnectGroupDetails": UpdateCrossConnectGroupDetails,
    "UpdateDhcpDetails": UpdateDhcpDetails,
    "UpdateDrgAttachmentDetails": UpdateDrgAttachmentDetails,
    "UpdateDrgDetails": UpdateDrgDetails,
    "UpdateIPSecConnectionDetails": UpdateIPSecConnectionDetails,
    "UpdateImageDetails": UpdateImageDetails,
    "UpdateInstanceDetails": UpdateInstanceDetails,
    "UpdateInternetGatewayDetails": UpdateInternetGatewayDetails,
    "UpdateRouteTableDetails": UpdateRouteTableDetails,
    "UpdateSecurityListDetails": UpdateSecurityListDetails,
    "UpdateSubnetDetails": UpdateSubnetDetails,
    "UpdateVcnDetails": UpdateVcnDetails,
    "UpdateVirtualCircuitDetails": UpdateVirtualCircuitDetails,
    "UpdateVolumeBackupDetails": UpdateVolumeBackupDetails,
    "UpdateVolumeDetails": UpdateVolumeDetails,
    "Vcn": Vcn,
    "VirtualCircuit": VirtualCircuit,
    "VirtualCircuitBandwidthShape": VirtualCircuitBandwidthShape,
    "Vnic": Vnic,
    "VnicAttachment": VnicAttachment,
    "Volume": Volume,
    "VolumeAttachment": VolumeAttachment,
    "VolumeBackup": VolumeBackup
}
