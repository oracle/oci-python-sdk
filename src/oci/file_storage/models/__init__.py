# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .change_file_system_compartment_details import ChangeFileSystemCompartmentDetails
from .change_mount_target_compartment_details import ChangeMountTargetCompartmentDetails
from .change_replication_compartment_details import ChangeReplicationCompartmentDetails
from .client_options import ClientOptions
from .create_export_details import CreateExportDetails
from .create_file_system_details import CreateFileSystemDetails
from .create_mount_target_details import CreateMountTargetDetails
from .create_replication_details import CreateReplicationDetails
from .create_snapshot_details import CreateSnapshotDetails
from .export import Export
from .export_set import ExportSet
from .export_set_summary import ExportSetSummary
from .export_summary import ExportSummary
from .file_system import FileSystem
from .file_system_summary import FileSystemSummary
from .mount_target import MountTarget
from .mount_target_summary import MountTargetSummary
from .replication import Replication
from .replication_estimate import ReplicationEstimate
from .replication_summary import ReplicationSummary
from .replication_target import ReplicationTarget
from .replication_target_summary import ReplicationTargetSummary
from .snapshot import Snapshot
from .snapshot_summary import SnapshotSummary
from .source_details import SourceDetails
from .update_export_details import UpdateExportDetails
from .update_export_set_details import UpdateExportSetDetails
from .update_file_system_details import UpdateFileSystemDetails
from .update_mount_target_details import UpdateMountTargetDetails
from .update_replication_details import UpdateReplicationDetails
from .update_snapshot_details import UpdateSnapshotDetails

# Maps type names to classes for file_storage services.
file_storage_type_mapping = {
    "ChangeFileSystemCompartmentDetails": ChangeFileSystemCompartmentDetails,
    "ChangeMountTargetCompartmentDetails": ChangeMountTargetCompartmentDetails,
    "ChangeReplicationCompartmentDetails": ChangeReplicationCompartmentDetails,
    "ClientOptions": ClientOptions,
    "CreateExportDetails": CreateExportDetails,
    "CreateFileSystemDetails": CreateFileSystemDetails,
    "CreateMountTargetDetails": CreateMountTargetDetails,
    "CreateReplicationDetails": CreateReplicationDetails,
    "CreateSnapshotDetails": CreateSnapshotDetails,
    "Export": Export,
    "ExportSet": ExportSet,
    "ExportSetSummary": ExportSetSummary,
    "ExportSummary": ExportSummary,
    "FileSystem": FileSystem,
    "FileSystemSummary": FileSystemSummary,
    "MountTarget": MountTarget,
    "MountTargetSummary": MountTargetSummary,
    "Replication": Replication,
    "ReplicationEstimate": ReplicationEstimate,
    "ReplicationSummary": ReplicationSummary,
    "ReplicationTarget": ReplicationTarget,
    "ReplicationTargetSummary": ReplicationTargetSummary,
    "Snapshot": Snapshot,
    "SnapshotSummary": SnapshotSummary,
    "SourceDetails": SourceDetails,
    "UpdateExportDetails": UpdateExportDetails,
    "UpdateExportSetDetails": UpdateExportSetDetails,
    "UpdateFileSystemDetails": UpdateFileSystemDetails,
    "UpdateMountTargetDetails": UpdateMountTargetDetails,
    "UpdateReplicationDetails": UpdateReplicationDetails,
    "UpdateSnapshotDetails": UpdateSnapshotDetails
}
