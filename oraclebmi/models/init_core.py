from __future__ import absolute_import

# import models into model package
from .attach_i_scsi_volume_request import AttachIScsiVolumeRequest
from .attach_volume_request import AttachVolumeRequest
from .capture_console_history_request import CaptureConsoleHistoryRequest
from .console_history_metadata import ConsoleHistoryMetadata
from .cpe import Cpe
from .create_cpe_request import CreateCpeRequest
from .create_drg_attachment_request import CreateDrgAttachmentRequest
from .create_drg_request import CreateDrgRequest
from .create_ip_sec_connection_request import CreateIPSecConnectionRequest
from .create_internet_gateway_request import CreateInternetGatewayRequest
from .create_route_table_request import CreateRouteTableRequest
from .create_subnet_request import CreateSubnetRequest
from .create_vcn_request import CreateVcnRequest
from .create_volume_request import CreateVolumeRequest
from .drg import Drg
from .drg_attachment import DrgAttachment
from .error import Error
from .ip_sec_connection import IPSecConnection
from .ip_sec_connection_device_config import IPSecConnectionDeviceConfig
from .ip_sec_connection_device_status import IPSecConnectionDeviceStatus
from .i_scsi_volume_attachment import IScsiVolumeAttachment
from .instance import Instance
from .internet_gateway import InternetGateway
from .launch_instance_request import LaunchInstanceRequest
from .route_rule import RouteRule
from .route_table import RouteTable
from .shape import Shape
from .subnet import Subnet
from .tunnel_config import TunnelConfig
from .tunnel_status import TunnelStatus
from .update_instance_request import UpdateInstanceRequest
from .update_internet_gateway_request import UpdateInternetGatewayRequest
from .update_route_table_request import UpdateRouteTableRequest
from .update_volume_request import UpdateVolumeRequest
from .vcn import Vcn
from .vnic import Vnic
from .vnic_attachment import VnicAttachment
from .volume import Volume
from .volume_attachment import VolumeAttachment

# Maps type names to classes for core services.
core_type_mapping = {
    'AttachIScsiVolumeRequest': AttachIScsiVolumeRequest,
    'AttachVolumeRequest': AttachVolumeRequest,
    'CaptureConsoleHistoryRequest': CaptureConsoleHistoryRequest,
    'ConsoleHistoryMetadata': ConsoleHistoryMetadata,
    'Cpe': Cpe,
    'CreateCpeRequest': CreateCpeRequest,
    'CreateDrgAttachmentRequest': CreateDrgAttachmentRequest,
    'CreateDrgRequest': CreateDrgRequest,
    'CreateIPSecConnectionRequest': CreateIPSecConnectionRequest,
    'CreateInternetGatewayRequest': CreateInternetGatewayRequest,
    'CreateRouteTableRequest': CreateRouteTableRequest,
    'CreateSubnetRequest': CreateSubnetRequest,
    'CreateVcnRequest': CreateVcnRequest,
    'CreateVolumeRequest': CreateVolumeRequest,
    'Drg': Drg,
    'DrgAttachment': DrgAttachment,
    'Error': Error,
    'IPSecConnection': IPSecConnection,
    'IPSecConnectionDeviceConfig': IPSecConnectionDeviceConfig,
    'IPSecConnectionDeviceStatus': IPSecConnectionDeviceStatus,
    'IScsiVolumeAttachment': IScsiVolumeAttachment,
    'Instance': Instance,
    'InternetGateway': InternetGateway,
    'LaunchInstanceRequest': LaunchInstanceRequest,
    'RouteRule': RouteRule,
    'RouteTable': RouteTable,
    'Shape': Shape,
    'Subnet': Subnet,
    'TunnelConfig': TunnelConfig,
    'TunnelStatus': TunnelStatus,
    'UpdateInstanceRequest': UpdateInstanceRequest,
    'UpdateInternetGatewayRequest': UpdateInternetGatewayRequest,
    'UpdateRouteTableRequest': UpdateRouteTableRequest,
    'UpdateVolumeRequest': UpdateVolumeRequest,
    'Vcn': Vcn,
    'Vnic': Vnic,
    'VnicAttachment': VnicAttachment,
    'Volume': Volume,
    'VolumeAttachment': VolumeAttachment,
}