# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from .attach_i_scsi_volume_details import AttachIScsiVolumeDetails
from .attach_volume_details import AttachVolumeDetails
from .capture_console_history_details import CaptureConsoleHistoryDetails
from .console_history import ConsoleHistory
from .cpe import Cpe
from .create_cpe_details import CreateCpeDetails
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
from .create_volume_backup_details import CreateVolumeBackupDetails
from .create_volume_details import CreateVolumeDetails
from .dhcp_dns_option import DhcpDnsOption
from .dhcp_option import DhcpOption
from .dhcp_options import DhcpOptions
from .drg import Drg
from .drg_attachment import DrgAttachment
from .egress_security_rule import EgressSecurityRule
from .ip_sec_connection import IPSecConnection
from .ip_sec_connection_device_config import IPSecConnectionDeviceConfig
from .ip_sec_connection_device_status import IPSecConnectionDeviceStatus
from .i_scsi_volume_attachment import IScsiVolumeAttachment
from .icmp_options import IcmpOptions
from .image import Image
from .ingress_security_rule import IngressSecurityRule
from .instance import Instance
from .internet_gateway import InternetGateway
from .launch_instance_details import LaunchInstanceDetails
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
from .update_volume_backup_details import UpdateVolumeBackupDetails
from .update_volume_details import UpdateVolumeDetails
from .vcn import Vcn
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
    "CreateVolumeBackupDetails": CreateVolumeBackupDetails,
    "CreateVolumeDetails": CreateVolumeDetails,
    "DhcpDnsOption": DhcpDnsOption,
    "DhcpOption": DhcpOption,
    "DhcpOptions": DhcpOptions,
    "Drg": Drg,
    "DrgAttachment": DrgAttachment,
    "EgressSecurityRule": EgressSecurityRule,
    "IPSecConnection": IPSecConnection,
    "IPSecConnectionDeviceConfig": IPSecConnectionDeviceConfig,
    "IPSecConnectionDeviceStatus": IPSecConnectionDeviceStatus,
    "IScsiVolumeAttachment": IScsiVolumeAttachment,
    "IcmpOptions": IcmpOptions,
    "Image": Image,
    "IngressSecurityRule": IngressSecurityRule,
    "Instance": Instance,
    "InternetGateway": InternetGateway,
    "LaunchInstanceDetails": LaunchInstanceDetails,
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
    "UpdateVolumeBackupDetails": UpdateVolumeBackupDetails,
    "UpdateVolumeDetails": UpdateVolumeDetails,
    "Vcn": Vcn,
    "Vnic": Vnic,
    "VnicAttachment": VnicAttachment,
    "Volume": Volume,
    "VolumeAttachment": VolumeAttachment,
    "VolumeBackup": VolumeBackup
}
