# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .availability_domain import AvailabilityDomain
from .blockchain_platform import BlockchainPlatform
from .blockchain_platform_by_hostname import BlockchainPlatformByHostname
from .blockchain_platform_collection import BlockchainPlatformCollection
from .blockchain_platform_component_details import BlockchainPlatformComponentDetails
from .blockchain_platform_summary import BlockchainPlatformSummary
from .change_blockchain_platform_compartment_details import ChangeBlockchainPlatformCompartmentDetails
from .create_blockchain_platform_details import CreateBlockchainPlatformDetails
from .create_osn_details import CreateOsnDetails
from .create_peer_details import CreatePeerDetails
from .metadata_details import MetadataDetails
from .modify_peer_details import ModifyPeerDetails
from .ocpu_allocation_number_param import OcpuAllocationNumberParam
from .ocpu_utilization_info import OcpuUtilizationInfo
from .osn import Osn
from .osn_collection import OsnCollection
from .osn_summary import OsnSummary
from .peer import Peer
from .peer_collection import PeerCollection
from .peer_role import PeerRole
from .peer_summary import PeerSummary
from .replica_details import ReplicaDetails
from .scale_blockchain_platform_details import ScaleBlockchainPlatformDetails
from .scale_storage_details import ScaleStorageDetails
from .scaled_blockchain_platform_preview import ScaledBlockchainPlatformPreview
from .scaled_platform_metering_preview import ScaledPlatformMeteringPreview
from .update_blockchain_platform_details import UpdateBlockchainPlatformDetails
from .update_osn_details import UpdateOsnDetails
from .update_peer_details import UpdatePeerDetails
from .work_request import WorkRequest
from .work_request_collection import WorkRequestCollection
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource
from .work_request_resource_sub_type_detail import WorkRequestResourceSubTypeDetail
from .work_request_summary import WorkRequestSummary

# Maps type names to classes for blockchain services.
blockchain_type_mapping = {
    "AvailabilityDomain": AvailabilityDomain,
    "BlockchainPlatform": BlockchainPlatform,
    "BlockchainPlatformByHostname": BlockchainPlatformByHostname,
    "BlockchainPlatformCollection": BlockchainPlatformCollection,
    "BlockchainPlatformComponentDetails": BlockchainPlatformComponentDetails,
    "BlockchainPlatformSummary": BlockchainPlatformSummary,
    "ChangeBlockchainPlatformCompartmentDetails": ChangeBlockchainPlatformCompartmentDetails,
    "CreateBlockchainPlatformDetails": CreateBlockchainPlatformDetails,
    "CreateOsnDetails": CreateOsnDetails,
    "CreatePeerDetails": CreatePeerDetails,
    "MetadataDetails": MetadataDetails,
    "ModifyPeerDetails": ModifyPeerDetails,
    "OcpuAllocationNumberParam": OcpuAllocationNumberParam,
    "OcpuUtilizationInfo": OcpuUtilizationInfo,
    "Osn": Osn,
    "OsnCollection": OsnCollection,
    "OsnSummary": OsnSummary,
    "Peer": Peer,
    "PeerCollection": PeerCollection,
    "PeerRole": PeerRole,
    "PeerSummary": PeerSummary,
    "ReplicaDetails": ReplicaDetails,
    "ScaleBlockchainPlatformDetails": ScaleBlockchainPlatformDetails,
    "ScaleStorageDetails": ScaleStorageDetails,
    "ScaledBlockchainPlatformPreview": ScaledBlockchainPlatformPreview,
    "ScaledPlatformMeteringPreview": ScaledPlatformMeteringPreview,
    "UpdateBlockchainPlatformDetails": UpdateBlockchainPlatformDetails,
    "UpdateOsnDetails": UpdateOsnDetails,
    "UpdatePeerDetails": UpdatePeerDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestCollection": WorkRequestCollection,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestResourceSubTypeDetail": WorkRequestResourceSubTypeDetail,
    "WorkRequestSummary": WorkRequestSummary
}
