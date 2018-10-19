# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from .app_catalog_listing import AppCatalogListing
from .app_catalog_listing_resource_version import AppCatalogListingResourceVersion
from .app_catalog_listing_resource_version_agreements import AppCatalogListingResourceVersionAgreements
from .app_catalog_listing_resource_version_summary import AppCatalogListingResourceVersionSummary
from .app_catalog_listing_summary import AppCatalogListingSummary
from .app_catalog_subscription import AppCatalogSubscription
from .app_catalog_subscription_summary import AppCatalogSubscriptionSummary
from .attach_boot_volume_details import AttachBootVolumeDetails
from .attach_i_scsi_volume_details import AttachIScsiVolumeDetails
from .attach_paravirtualized_volume_details import AttachParavirtualizedVolumeDetails
from .attach_vnic_details import AttachVnicDetails
from .attach_volume_details import AttachVolumeDetails
from .boot_volume import BootVolume
from .boot_volume_attachment import BootVolumeAttachment
from .boot_volume_backup import BootVolumeBackup
from .boot_volume_kms_key import BootVolumeKmsKey
from .boot_volume_source_details import BootVolumeSourceDetails
from .boot_volume_source_from_boot_volume_backup_details import BootVolumeSourceFromBootVolumeBackupDetails
from .boot_volume_source_from_boot_volume_details import BootVolumeSourceFromBootVolumeDetails
from .bulk_add_virtual_circuit_public_prefixes_details import BulkAddVirtualCircuitPublicPrefixesDetails
from .bulk_delete_virtual_circuit_public_prefixes_details import BulkDeleteVirtualCircuitPublicPrefixesDetails
from .capture_console_history_details import CaptureConsoleHistoryDetails
from .compute_instance_details import ComputeInstanceDetails
from .connect_local_peering_gateways_details import ConnectLocalPeeringGatewaysDetails
from .connect_remote_peering_connections_details import ConnectRemotePeeringConnectionsDetails
from .console_history import ConsoleHistory
from .copy_volume_backup_details import CopyVolumeBackupDetails
from .cpe import Cpe
from .create_app_catalog_subscription_details import CreateAppCatalogSubscriptionDetails
from .create_boot_volume_backup_details import CreateBootVolumeBackupDetails
from .create_boot_volume_details import CreateBootVolumeDetails
from .create_cpe_details import CreateCpeDetails
from .create_cross_connect_details import CreateCrossConnectDetails
from .create_cross_connect_group_details import CreateCrossConnectGroupDetails
from .create_dhcp_details import CreateDhcpDetails
from .create_drg_attachment_details import CreateDrgAttachmentDetails
from .create_drg_details import CreateDrgDetails
from .create_ip_sec_connection_details import CreateIPSecConnectionDetails
from .create_image_details import CreateImageDetails
from .create_instance_configuration_details import CreateInstanceConfigurationDetails
from .create_instance_console_connection_details import CreateInstanceConsoleConnectionDetails
from .create_instance_pool_details import CreateInstancePoolDetails
from .create_instance_pool_placement_configuration_details import CreateInstancePoolPlacementConfigurationDetails
from .create_internet_gateway_details import CreateInternetGatewayDetails
from .create_local_peering_gateway_details import CreateLocalPeeringGatewayDetails
from .create_nat_gateway_details import CreateNatGatewayDetails
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
from .create_volume_backup_details import CreateVolumeBackupDetails
from .create_volume_backup_policy_assignment_details import CreateVolumeBackupPolicyAssignmentDetails
from .create_volume_details import CreateVolumeDetails
from .create_volume_group_backup_details import CreateVolumeGroupBackupDetails
from .create_volume_group_details import CreateVolumeGroupDetails
from .cross_connect import CrossConnect
from .cross_connect_group import CrossConnectGroup
from .cross_connect_location import CrossConnectLocation
from .cross_connect_mapping import CrossConnectMapping
from .cross_connect_port_speed_shape import CrossConnectPortSpeedShape
from .cross_connect_status import CrossConnectStatus
from .delete_virtual_circuit_public_prefix_details import DeleteVirtualCircuitPublicPrefixDetails
from .dhcp_dns_option import DhcpDnsOption
from .dhcp_option import DhcpOption
from .dhcp_options import DhcpOptions
from .dhcp_search_domain_option import DhcpSearchDomainOption
from .drg import Drg
from .drg_attachment import DrgAttachment
from .egress_security_rule import EgressSecurityRule
from .export_image_details import ExportImageDetails
from .export_image_via_object_storage_tuple_details import ExportImageViaObjectStorageTupleDetails
from .export_image_via_object_storage_uri_details import ExportImageViaObjectStorageUriDetails
from .fast_connect_provider_service import FastConnectProviderService
from .get_public_ip_by_ip_address_details import GetPublicIpByIpAddressDetails
from .get_public_ip_by_private_ip_id_details import GetPublicIpByPrivateIpIdDetails
from .ip_sec_connection import IPSecConnection
from .ip_sec_connection_device_config import IPSecConnectionDeviceConfig
from .ip_sec_connection_device_status import IPSecConnectionDeviceStatus
from .i_scsi_volume_attachment import IScsiVolumeAttachment
from .icmp_options import IcmpOptions
from .image import Image
from .image_source_details import ImageSourceDetails
from .image_source_via_object_storage_tuple_details import ImageSourceViaObjectStorageTupleDetails
from .image_source_via_object_storage_uri_details import ImageSourceViaObjectStorageUriDetails
from .ingress_security_rule import IngressSecurityRule
from .instance import Instance
from .instance_configuration import InstanceConfiguration
from .instance_configuration_attach_vnic_details import InstanceConfigurationAttachVnicDetails
from .instance_configuration_attach_volume_details import InstanceConfigurationAttachVolumeDetails
from .instance_configuration_block_volume_details import InstanceConfigurationBlockVolumeDetails
from .instance_configuration_create_vnic_details import InstanceConfigurationCreateVnicDetails
from .instance_configuration_create_volume_details import InstanceConfigurationCreateVolumeDetails
from .instance_configuration_instance_details import InstanceConfigurationInstanceDetails
from .instance_configuration_instance_source_details import InstanceConfigurationInstanceSourceDetails
from .instance_configuration_instance_source_via_boot_volume_details import InstanceConfigurationInstanceSourceViaBootVolumeDetails
from .instance_configuration_instance_source_via_image_details import InstanceConfigurationInstanceSourceViaImageDetails
from .instance_configuration_iscsi_attach_volume_details import InstanceConfigurationIscsiAttachVolumeDetails
from .instance_configuration_launch_instance_details import InstanceConfigurationLaunchInstanceDetails
from .instance_configuration_paravirtualized_attach_volume_details import InstanceConfigurationParavirtualizedAttachVolumeDetails
from .instance_configuration_summary import InstanceConfigurationSummary
from .instance_configuration_volume_source_details import InstanceConfigurationVolumeSourceDetails
from .instance_configuration_volume_source_from_volume_backup_details import InstanceConfigurationVolumeSourceFromVolumeBackupDetails
from .instance_configuration_volume_source_from_volume_details import InstanceConfigurationVolumeSourceFromVolumeDetails
from .instance_console_connection import InstanceConsoleConnection
from .instance_credentials import InstanceCredentials
from .instance_pool import InstancePool
from .instance_pool_placement_configuration import InstancePoolPlacementConfiguration
from .instance_pool_placement_secondary_vnic_subnet import InstancePoolPlacementSecondaryVnicSubnet
from .instance_pool_summary import InstancePoolSummary
from .instance_source_details import InstanceSourceDetails
from .instance_source_via_boot_volume_details import InstanceSourceViaBootVolumeDetails
from .instance_source_via_image_details import InstanceSourceViaImageDetails
from .instance_summary import InstanceSummary
from .internet_gateway import InternetGateway
from .launch_instance_details import LaunchInstanceDetails
from .launch_options import LaunchOptions
from .letter_of_authority import LetterOfAuthority
from .local_peering_gateway import LocalPeeringGateway
from .nat_gateway import NatGateway
from .paravirtualized_volume_attachment import ParavirtualizedVolumeAttachment
from .peer_region_for_remote_peering import PeerRegionForRemotePeering
from .port_range import PortRange
from .private_ip import PrivateIp
from .public_ip import PublicIp
from .remote_peering_connection import RemotePeeringConnection
from .route_rule import RouteRule
from .route_table import RouteTable
from .security_list import SecurityList
from .service import Service
from .service_gateway import ServiceGateway
from .service_id_request_details import ServiceIdRequestDetails
from .service_id_response_details import ServiceIdResponseDetails
from .shape import Shape
from .subnet import Subnet
from .tcp_options import TcpOptions
from .tunnel_config import TunnelConfig
from .tunnel_status import TunnelStatus
from .udp_options import UdpOptions
from .update_boot_volume_backup_details import UpdateBootVolumeBackupDetails
from .update_boot_volume_details import UpdateBootVolumeDetails
from .update_boot_volume_kms_key_details import UpdateBootVolumeKmsKeyDetails
from .update_console_history_details import UpdateConsoleHistoryDetails
from .update_cpe_details import UpdateCpeDetails
from .update_cross_connect_details import UpdateCrossConnectDetails
from .update_cross_connect_group_details import UpdateCrossConnectGroupDetails
from .update_dhcp_details import UpdateDhcpDetails
from .update_drg_attachment_details import UpdateDrgAttachmentDetails
from .update_drg_details import UpdateDrgDetails
from .update_ip_sec_connection_details import UpdateIPSecConnectionDetails
from .update_image_details import UpdateImageDetails
from .update_instance_configuration_details import UpdateInstanceConfigurationDetails
from .update_instance_details import UpdateInstanceDetails
from .update_instance_pool_details import UpdateInstancePoolDetails
from .update_instance_pool_placement_configuration_details import UpdateInstancePoolPlacementConfigurationDetails
from .update_internet_gateway_details import UpdateInternetGatewayDetails
from .update_local_peering_gateway_details import UpdateLocalPeeringGatewayDetails
from .update_nat_gateway_details import UpdateNatGatewayDetails
from .update_private_ip_details import UpdatePrivateIpDetails
from .update_public_ip_details import UpdatePublicIpDetails
from .update_remote_peering_connection_details import UpdateRemotePeeringConnectionDetails
from .update_route_table_details import UpdateRouteTableDetails
from .update_security_list_details import UpdateSecurityListDetails
from .update_service_gateway_details import UpdateServiceGatewayDetails
from .update_subnet_details import UpdateSubnetDetails
from .update_vcn_details import UpdateVcnDetails
from .update_virtual_circuit_details import UpdateVirtualCircuitDetails
from .update_vnic_details import UpdateVnicDetails
from .update_volume_backup_details import UpdateVolumeBackupDetails
from .update_volume_details import UpdateVolumeDetails
from .update_volume_group_backup_details import UpdateVolumeGroupBackupDetails
from .update_volume_group_details import UpdateVolumeGroupDetails
from .update_volume_kms_key_details import UpdateVolumeKmsKeyDetails
from .vcn import Vcn
from .virtual_circuit import VirtualCircuit
from .virtual_circuit_bandwidth_shape import VirtualCircuitBandwidthShape
from .virtual_circuit_public_prefix import VirtualCircuitPublicPrefix
from .vnic import Vnic
from .vnic_attachment import VnicAttachment
from .volume import Volume
from .volume_attachment import VolumeAttachment
from .volume_backup import VolumeBackup
from .volume_backup_policy import VolumeBackupPolicy
from .volume_backup_policy_assignment import VolumeBackupPolicyAssignment
from .volume_backup_schedule import VolumeBackupSchedule
from .volume_group import VolumeGroup
from .volume_group_backup import VolumeGroupBackup
from .volume_group_source_details import VolumeGroupSourceDetails
from .volume_group_source_from_volume_group_backup_details import VolumeGroupSourceFromVolumeGroupBackupDetails
from .volume_group_source_from_volume_group_details import VolumeGroupSourceFromVolumeGroupDetails
from .volume_group_source_from_volumes_details import VolumeGroupSourceFromVolumesDetails
from .volume_kms_key import VolumeKmsKey
from .volume_source_details import VolumeSourceDetails
from .volume_source_from_volume_backup_details import VolumeSourceFromVolumeBackupDetails
from .volume_source_from_volume_details import VolumeSourceFromVolumeDetails

# Maps type names to classes for core services.
core_type_mapping = {
    "AppCatalogListing": AppCatalogListing,
    "AppCatalogListingResourceVersion": AppCatalogListingResourceVersion,
    "AppCatalogListingResourceVersionAgreements": AppCatalogListingResourceVersionAgreements,
    "AppCatalogListingResourceVersionSummary": AppCatalogListingResourceVersionSummary,
    "AppCatalogListingSummary": AppCatalogListingSummary,
    "AppCatalogSubscription": AppCatalogSubscription,
    "AppCatalogSubscriptionSummary": AppCatalogSubscriptionSummary,
    "AttachBootVolumeDetails": AttachBootVolumeDetails,
    "AttachIScsiVolumeDetails": AttachIScsiVolumeDetails,
    "AttachParavirtualizedVolumeDetails": AttachParavirtualizedVolumeDetails,
    "AttachVnicDetails": AttachVnicDetails,
    "AttachVolumeDetails": AttachVolumeDetails,
    "BootVolume": BootVolume,
    "BootVolumeAttachment": BootVolumeAttachment,
    "BootVolumeBackup": BootVolumeBackup,
    "BootVolumeKmsKey": BootVolumeKmsKey,
    "BootVolumeSourceDetails": BootVolumeSourceDetails,
    "BootVolumeSourceFromBootVolumeBackupDetails": BootVolumeSourceFromBootVolumeBackupDetails,
    "BootVolumeSourceFromBootVolumeDetails": BootVolumeSourceFromBootVolumeDetails,
    "BulkAddVirtualCircuitPublicPrefixesDetails": BulkAddVirtualCircuitPublicPrefixesDetails,
    "BulkDeleteVirtualCircuitPublicPrefixesDetails": BulkDeleteVirtualCircuitPublicPrefixesDetails,
    "CaptureConsoleHistoryDetails": CaptureConsoleHistoryDetails,
    "ComputeInstanceDetails": ComputeInstanceDetails,
    "ConnectLocalPeeringGatewaysDetails": ConnectLocalPeeringGatewaysDetails,
    "ConnectRemotePeeringConnectionsDetails": ConnectRemotePeeringConnectionsDetails,
    "ConsoleHistory": ConsoleHistory,
    "CopyVolumeBackupDetails": CopyVolumeBackupDetails,
    "Cpe": Cpe,
    "CreateAppCatalogSubscriptionDetails": CreateAppCatalogSubscriptionDetails,
    "CreateBootVolumeBackupDetails": CreateBootVolumeBackupDetails,
    "CreateBootVolumeDetails": CreateBootVolumeDetails,
    "CreateCpeDetails": CreateCpeDetails,
    "CreateCrossConnectDetails": CreateCrossConnectDetails,
    "CreateCrossConnectGroupDetails": CreateCrossConnectGroupDetails,
    "CreateDhcpDetails": CreateDhcpDetails,
    "CreateDrgAttachmentDetails": CreateDrgAttachmentDetails,
    "CreateDrgDetails": CreateDrgDetails,
    "CreateIPSecConnectionDetails": CreateIPSecConnectionDetails,
    "CreateImageDetails": CreateImageDetails,
    "CreateInstanceConfigurationDetails": CreateInstanceConfigurationDetails,
    "CreateInstanceConsoleConnectionDetails": CreateInstanceConsoleConnectionDetails,
    "CreateInstancePoolDetails": CreateInstancePoolDetails,
    "CreateInstancePoolPlacementConfigurationDetails": CreateInstancePoolPlacementConfigurationDetails,
    "CreateInternetGatewayDetails": CreateInternetGatewayDetails,
    "CreateLocalPeeringGatewayDetails": CreateLocalPeeringGatewayDetails,
    "CreateNatGatewayDetails": CreateNatGatewayDetails,
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
    "CreateVolumeBackupDetails": CreateVolumeBackupDetails,
    "CreateVolumeBackupPolicyAssignmentDetails": CreateVolumeBackupPolicyAssignmentDetails,
    "CreateVolumeDetails": CreateVolumeDetails,
    "CreateVolumeGroupBackupDetails": CreateVolumeGroupBackupDetails,
    "CreateVolumeGroupDetails": CreateVolumeGroupDetails,
    "CrossConnect": CrossConnect,
    "CrossConnectGroup": CrossConnectGroup,
    "CrossConnectLocation": CrossConnectLocation,
    "CrossConnectMapping": CrossConnectMapping,
    "CrossConnectPortSpeedShape": CrossConnectPortSpeedShape,
    "CrossConnectStatus": CrossConnectStatus,
    "DeleteVirtualCircuitPublicPrefixDetails": DeleteVirtualCircuitPublicPrefixDetails,
    "DhcpDnsOption": DhcpDnsOption,
    "DhcpOption": DhcpOption,
    "DhcpOptions": DhcpOptions,
    "DhcpSearchDomainOption": DhcpSearchDomainOption,
    "Drg": Drg,
    "DrgAttachment": DrgAttachment,
    "EgressSecurityRule": EgressSecurityRule,
    "ExportImageDetails": ExportImageDetails,
    "ExportImageViaObjectStorageTupleDetails": ExportImageViaObjectStorageTupleDetails,
    "ExportImageViaObjectStorageUriDetails": ExportImageViaObjectStorageUriDetails,
    "FastConnectProviderService": FastConnectProviderService,
    "GetPublicIpByIpAddressDetails": GetPublicIpByIpAddressDetails,
    "GetPublicIpByPrivateIpIdDetails": GetPublicIpByPrivateIpIdDetails,
    "IPSecConnection": IPSecConnection,
    "IPSecConnectionDeviceConfig": IPSecConnectionDeviceConfig,
    "IPSecConnectionDeviceStatus": IPSecConnectionDeviceStatus,
    "IScsiVolumeAttachment": IScsiVolumeAttachment,
    "IcmpOptions": IcmpOptions,
    "Image": Image,
    "ImageSourceDetails": ImageSourceDetails,
    "ImageSourceViaObjectStorageTupleDetails": ImageSourceViaObjectStorageTupleDetails,
    "ImageSourceViaObjectStorageUriDetails": ImageSourceViaObjectStorageUriDetails,
    "IngressSecurityRule": IngressSecurityRule,
    "Instance": Instance,
    "InstanceConfiguration": InstanceConfiguration,
    "InstanceConfigurationAttachVnicDetails": InstanceConfigurationAttachVnicDetails,
    "InstanceConfigurationAttachVolumeDetails": InstanceConfigurationAttachVolumeDetails,
    "InstanceConfigurationBlockVolumeDetails": InstanceConfigurationBlockVolumeDetails,
    "InstanceConfigurationCreateVnicDetails": InstanceConfigurationCreateVnicDetails,
    "InstanceConfigurationCreateVolumeDetails": InstanceConfigurationCreateVolumeDetails,
    "InstanceConfigurationInstanceDetails": InstanceConfigurationInstanceDetails,
    "InstanceConfigurationInstanceSourceDetails": InstanceConfigurationInstanceSourceDetails,
    "InstanceConfigurationInstanceSourceViaBootVolumeDetails": InstanceConfigurationInstanceSourceViaBootVolumeDetails,
    "InstanceConfigurationInstanceSourceViaImageDetails": InstanceConfigurationInstanceSourceViaImageDetails,
    "InstanceConfigurationIscsiAttachVolumeDetails": InstanceConfigurationIscsiAttachVolumeDetails,
    "InstanceConfigurationLaunchInstanceDetails": InstanceConfigurationLaunchInstanceDetails,
    "InstanceConfigurationParavirtualizedAttachVolumeDetails": InstanceConfigurationParavirtualizedAttachVolumeDetails,
    "InstanceConfigurationSummary": InstanceConfigurationSummary,
    "InstanceConfigurationVolumeSourceDetails": InstanceConfigurationVolumeSourceDetails,
    "InstanceConfigurationVolumeSourceFromVolumeBackupDetails": InstanceConfigurationVolumeSourceFromVolumeBackupDetails,
    "InstanceConfigurationVolumeSourceFromVolumeDetails": InstanceConfigurationVolumeSourceFromVolumeDetails,
    "InstanceConsoleConnection": InstanceConsoleConnection,
    "InstanceCredentials": InstanceCredentials,
    "InstancePool": InstancePool,
    "InstancePoolPlacementConfiguration": InstancePoolPlacementConfiguration,
    "InstancePoolPlacementSecondaryVnicSubnet": InstancePoolPlacementSecondaryVnicSubnet,
    "InstancePoolSummary": InstancePoolSummary,
    "InstanceSourceDetails": InstanceSourceDetails,
    "InstanceSourceViaBootVolumeDetails": InstanceSourceViaBootVolumeDetails,
    "InstanceSourceViaImageDetails": InstanceSourceViaImageDetails,
    "InstanceSummary": InstanceSummary,
    "InternetGateway": InternetGateway,
    "LaunchInstanceDetails": LaunchInstanceDetails,
    "LaunchOptions": LaunchOptions,
    "LetterOfAuthority": LetterOfAuthority,
    "LocalPeeringGateway": LocalPeeringGateway,
    "NatGateway": NatGateway,
    "ParavirtualizedVolumeAttachment": ParavirtualizedVolumeAttachment,
    "PeerRegionForRemotePeering": PeerRegionForRemotePeering,
    "PortRange": PortRange,
    "PrivateIp": PrivateIp,
    "PublicIp": PublicIp,
    "RemotePeeringConnection": RemotePeeringConnection,
    "RouteRule": RouteRule,
    "RouteTable": RouteTable,
    "SecurityList": SecurityList,
    "Service": Service,
    "ServiceGateway": ServiceGateway,
    "ServiceIdRequestDetails": ServiceIdRequestDetails,
    "ServiceIdResponseDetails": ServiceIdResponseDetails,
    "Shape": Shape,
    "Subnet": Subnet,
    "TcpOptions": TcpOptions,
    "TunnelConfig": TunnelConfig,
    "TunnelStatus": TunnelStatus,
    "UdpOptions": UdpOptions,
    "UpdateBootVolumeBackupDetails": UpdateBootVolumeBackupDetails,
    "UpdateBootVolumeDetails": UpdateBootVolumeDetails,
    "UpdateBootVolumeKmsKeyDetails": UpdateBootVolumeKmsKeyDetails,
    "UpdateConsoleHistoryDetails": UpdateConsoleHistoryDetails,
    "UpdateCpeDetails": UpdateCpeDetails,
    "UpdateCrossConnectDetails": UpdateCrossConnectDetails,
    "UpdateCrossConnectGroupDetails": UpdateCrossConnectGroupDetails,
    "UpdateDhcpDetails": UpdateDhcpDetails,
    "UpdateDrgAttachmentDetails": UpdateDrgAttachmentDetails,
    "UpdateDrgDetails": UpdateDrgDetails,
    "UpdateIPSecConnectionDetails": UpdateIPSecConnectionDetails,
    "UpdateImageDetails": UpdateImageDetails,
    "UpdateInstanceConfigurationDetails": UpdateInstanceConfigurationDetails,
    "UpdateInstanceDetails": UpdateInstanceDetails,
    "UpdateInstancePoolDetails": UpdateInstancePoolDetails,
    "UpdateInstancePoolPlacementConfigurationDetails": UpdateInstancePoolPlacementConfigurationDetails,
    "UpdateInternetGatewayDetails": UpdateInternetGatewayDetails,
    "UpdateLocalPeeringGatewayDetails": UpdateLocalPeeringGatewayDetails,
    "UpdateNatGatewayDetails": UpdateNatGatewayDetails,
    "UpdatePrivateIpDetails": UpdatePrivateIpDetails,
    "UpdatePublicIpDetails": UpdatePublicIpDetails,
    "UpdateRemotePeeringConnectionDetails": UpdateRemotePeeringConnectionDetails,
    "UpdateRouteTableDetails": UpdateRouteTableDetails,
    "UpdateSecurityListDetails": UpdateSecurityListDetails,
    "UpdateServiceGatewayDetails": UpdateServiceGatewayDetails,
    "UpdateSubnetDetails": UpdateSubnetDetails,
    "UpdateVcnDetails": UpdateVcnDetails,
    "UpdateVirtualCircuitDetails": UpdateVirtualCircuitDetails,
    "UpdateVnicDetails": UpdateVnicDetails,
    "UpdateVolumeBackupDetails": UpdateVolumeBackupDetails,
    "UpdateVolumeDetails": UpdateVolumeDetails,
    "UpdateVolumeGroupBackupDetails": UpdateVolumeGroupBackupDetails,
    "UpdateVolumeGroupDetails": UpdateVolumeGroupDetails,
    "UpdateVolumeKmsKeyDetails": UpdateVolumeKmsKeyDetails,
    "Vcn": Vcn,
    "VirtualCircuit": VirtualCircuit,
    "VirtualCircuitBandwidthShape": VirtualCircuitBandwidthShape,
    "VirtualCircuitPublicPrefix": VirtualCircuitPublicPrefix,
    "Vnic": Vnic,
    "VnicAttachment": VnicAttachment,
    "Volume": Volume,
    "VolumeAttachment": VolumeAttachment,
    "VolumeBackup": VolumeBackup,
    "VolumeBackupPolicy": VolumeBackupPolicy,
    "VolumeBackupPolicyAssignment": VolumeBackupPolicyAssignment,
    "VolumeBackupSchedule": VolumeBackupSchedule,
    "VolumeGroup": VolumeGroup,
    "VolumeGroupBackup": VolumeGroupBackup,
    "VolumeGroupSourceDetails": VolumeGroupSourceDetails,
    "VolumeGroupSourceFromVolumeGroupBackupDetails": VolumeGroupSourceFromVolumeGroupBackupDetails,
    "VolumeGroupSourceFromVolumeGroupDetails": VolumeGroupSourceFromVolumeGroupDetails,
    "VolumeGroupSourceFromVolumesDetails": VolumeGroupSourceFromVolumesDetails,
    "VolumeKmsKey": VolumeKmsKey,
    "VolumeSourceDetails": VolumeSourceDetails,
    "VolumeSourceFromVolumeBackupDetails": VolumeSourceFromVolumeBackupDetails,
    "VolumeSourceFromVolumeDetails": VolumeSourceFromVolumeDetails
}
