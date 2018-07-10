# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from .client_options import ClientOptions
from .create_export_details import CreateExportDetails
from .create_file_system_details import CreateFileSystemDetails
from .create_mount_target_details import CreateMountTargetDetails
from .create_snapshot_details import CreateSnapshotDetails
from .export import Export
from .export_set import ExportSet
from .export_set_summary import ExportSetSummary
from .export_summary import ExportSummary
from .file_system import FileSystem
from .file_system_summary import FileSystemSummary
from .mount_target import MountTarget
from .mount_target_summary import MountTargetSummary
from .snapshot import Snapshot
from .snapshot_summary import SnapshotSummary
from .update_export_details import UpdateExportDetails
from .update_export_set_details import UpdateExportSetDetails
from .update_file_system_details import UpdateFileSystemDetails
from .update_mount_target_details import UpdateMountTargetDetails

# Maps type names to classes for file_storage services.
file_storage_type_mapping = {
    "ClientOptions": ClientOptions,
    "CreateExportDetails": CreateExportDetails,
    "CreateFileSystemDetails": CreateFileSystemDetails,
    "CreateMountTargetDetails": CreateMountTargetDetails,
    "CreateSnapshotDetails": CreateSnapshotDetails,
    "Export": Export,
    "ExportSet": ExportSet,
    "ExportSetSummary": ExportSetSummary,
    "ExportSummary": ExportSummary,
    "FileSystem": FileSystem,
    "FileSystemSummary": FileSystemSummary,
    "MountTarget": MountTarget,
    "MountTargetSummary": MountTargetSummary,
    "Snapshot": Snapshot,
    "SnapshotSummary": SnapshotSummary,
    "UpdateExportDetails": UpdateExportDetails,
    "UpdateExportSetDetails": UpdateExportSetDetails,
    "UpdateFileSystemDetails": UpdateFileSystemDetails,
    "UpdateMountTargetDetails": UpdateMountTargetDetails
}
