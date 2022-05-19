# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .add_packages_to_software_source_details import AddPackagesToSoftwareSourceDetails
from .api_error import ApiError
from .attach_child_software_source_to_managed_instance_details import AttachChildSoftwareSourceToManagedInstanceDetails
from .attach_parent_software_source_to_managed_instance_details import AttachParentSoftwareSourceToManagedInstanceDetails
from .autonomous_settings import AutonomousSettings
from .available_software_source_summary import AvailableSoftwareSourceSummary
from .available_update_summary import AvailableUpdateSummary
from .available_windows_update_summary import AvailableWindowsUpdateSummary
from .change_managed_instance_group_compartment_details import ChangeManagedInstanceGroupCompartmentDetails
from .change_scheduled_job_compartment_details import ChangeScheduledJobCompartmentDetails
from .change_software_source_compartment_details import ChangeSoftwareSourceCompartmentDetails
from .crash_event_system_information import CrashEventSystemInformation
from .create_managed_instance_group_details import CreateManagedInstanceGroupDetails
from .create_scheduled_job_details import CreateScheduledJobDetails
from .create_software_source_details import CreateSoftwareSourceDetails
from .detach_child_software_source_from_managed_instance_details import DetachChildSoftwareSourceFromManagedInstanceDetails
from .detach_parent_software_source_from_managed_instance_details import DetachParentSoftwareSourceFromManagedInstanceDetails
from .erratum import Erratum
from .erratum_summary import ErratumSummary
from .event import Event
from .event_collection import EventCollection
from .event_content import EventContent
from .event_report import EventReport
from .event_summary import EventSummary
from .id import Id
from .installable_package_summary import InstallablePackageSummary
from .installed_package_summary import InstalledPackageSummary
from .installed_windows_update_summary import InstalledWindowsUpdateSummary
from .kernel_crash_event import KernelCrashEvent
from .kernel_oops_event import KernelOopsEvent
from .kernel_vm_core_information import KernelVmCoreInformation
from .manage_module_streams_on_managed_instance_details import ManageModuleStreamsOnManagedInstanceDetails
from .managed_instance import ManagedInstance
from .managed_instance_group import ManagedInstanceGroup
from .managed_instance_group_summary import ManagedInstanceGroupSummary
from .managed_instance_summary import ManagedInstanceSummary
from .module_stream import ModuleStream
from .module_stream_details import ModuleStreamDetails
from .module_stream_on_managed_instance_summary import ModuleStreamOnManagedInstanceSummary
from .module_stream_profile import ModuleStreamProfile
from .module_stream_profile_details import ModuleStreamProfileDetails
from .module_stream_profile_on_managed_instance_summary import ModuleStreamProfileOnManagedInstanceSummary
from .module_stream_profile_summary import ModuleStreamProfileSummary
from .module_stream_summary import ModuleStreamSummary
from .package_name import PackageName
from .recurrence import Recurrence
from .related_event_collection import RelatedEventCollection
from .related_event_summary import RelatedEventSummary
from .remove_packages_from_software_source_details import RemovePackagesFromSoftwareSourceDetails
from .scheduled_job import ScheduledJob
from .scheduled_job_summary import ScheduledJobSummary
from .software_package import SoftwarePackage
from .software_package_dependency import SoftwarePackageDependency
from .software_package_file import SoftwarePackageFile
from .software_package_search_summary import SoftwarePackageSearchSummary
from .software_package_summary import SoftwarePackageSummary
from .software_source import SoftwareSource
from .software_source_id import SoftwareSourceId
from .software_source_summary import SoftwareSourceSummary
from .update_event_details import UpdateEventDetails
from .update_managed_instance_details import UpdateManagedInstanceDetails
from .update_managed_instance_group_details import UpdateManagedInstanceGroupDetails
from .update_module_details import UpdateModuleDetails
from .update_module_stream_details import UpdateModuleStreamDetails
from .update_module_stream_profile_details import UpdateModuleStreamProfileDetails
from .update_module_stream_state_details import UpdateModuleStreamStateDetails
from .update_scheduled_job_details import UpdateScheduledJobDetails
from .update_software_source_details import UpdateSoftwareSourceDetails
from .windows_update import WindowsUpdate
from .windows_update_summary import WindowsUpdateSummary
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary

# Maps type names to classes for os_management services.
os_management_type_mapping = {
    "AddPackagesToSoftwareSourceDetails": AddPackagesToSoftwareSourceDetails,
    "ApiError": ApiError,
    "AttachChildSoftwareSourceToManagedInstanceDetails": AttachChildSoftwareSourceToManagedInstanceDetails,
    "AttachParentSoftwareSourceToManagedInstanceDetails": AttachParentSoftwareSourceToManagedInstanceDetails,
    "AutonomousSettings": AutonomousSettings,
    "AvailableSoftwareSourceSummary": AvailableSoftwareSourceSummary,
    "AvailableUpdateSummary": AvailableUpdateSummary,
    "AvailableWindowsUpdateSummary": AvailableWindowsUpdateSummary,
    "ChangeManagedInstanceGroupCompartmentDetails": ChangeManagedInstanceGroupCompartmentDetails,
    "ChangeScheduledJobCompartmentDetails": ChangeScheduledJobCompartmentDetails,
    "ChangeSoftwareSourceCompartmentDetails": ChangeSoftwareSourceCompartmentDetails,
    "CrashEventSystemInformation": CrashEventSystemInformation,
    "CreateManagedInstanceGroupDetails": CreateManagedInstanceGroupDetails,
    "CreateScheduledJobDetails": CreateScheduledJobDetails,
    "CreateSoftwareSourceDetails": CreateSoftwareSourceDetails,
    "DetachChildSoftwareSourceFromManagedInstanceDetails": DetachChildSoftwareSourceFromManagedInstanceDetails,
    "DetachParentSoftwareSourceFromManagedInstanceDetails": DetachParentSoftwareSourceFromManagedInstanceDetails,
    "Erratum": Erratum,
    "ErratumSummary": ErratumSummary,
    "Event": Event,
    "EventCollection": EventCollection,
    "EventContent": EventContent,
    "EventReport": EventReport,
    "EventSummary": EventSummary,
    "Id": Id,
    "InstallablePackageSummary": InstallablePackageSummary,
    "InstalledPackageSummary": InstalledPackageSummary,
    "InstalledWindowsUpdateSummary": InstalledWindowsUpdateSummary,
    "KernelCrashEvent": KernelCrashEvent,
    "KernelOopsEvent": KernelOopsEvent,
    "KernelVmCoreInformation": KernelVmCoreInformation,
    "ManageModuleStreamsOnManagedInstanceDetails": ManageModuleStreamsOnManagedInstanceDetails,
    "ManagedInstance": ManagedInstance,
    "ManagedInstanceGroup": ManagedInstanceGroup,
    "ManagedInstanceGroupSummary": ManagedInstanceGroupSummary,
    "ManagedInstanceSummary": ManagedInstanceSummary,
    "ModuleStream": ModuleStream,
    "ModuleStreamDetails": ModuleStreamDetails,
    "ModuleStreamOnManagedInstanceSummary": ModuleStreamOnManagedInstanceSummary,
    "ModuleStreamProfile": ModuleStreamProfile,
    "ModuleStreamProfileDetails": ModuleStreamProfileDetails,
    "ModuleStreamProfileOnManagedInstanceSummary": ModuleStreamProfileOnManagedInstanceSummary,
    "ModuleStreamProfileSummary": ModuleStreamProfileSummary,
    "ModuleStreamSummary": ModuleStreamSummary,
    "PackageName": PackageName,
    "Recurrence": Recurrence,
    "RelatedEventCollection": RelatedEventCollection,
    "RelatedEventSummary": RelatedEventSummary,
    "RemovePackagesFromSoftwareSourceDetails": RemovePackagesFromSoftwareSourceDetails,
    "ScheduledJob": ScheduledJob,
    "ScheduledJobSummary": ScheduledJobSummary,
    "SoftwarePackage": SoftwarePackage,
    "SoftwarePackageDependency": SoftwarePackageDependency,
    "SoftwarePackageFile": SoftwarePackageFile,
    "SoftwarePackageSearchSummary": SoftwarePackageSearchSummary,
    "SoftwarePackageSummary": SoftwarePackageSummary,
    "SoftwareSource": SoftwareSource,
    "SoftwareSourceId": SoftwareSourceId,
    "SoftwareSourceSummary": SoftwareSourceSummary,
    "UpdateEventDetails": UpdateEventDetails,
    "UpdateManagedInstanceDetails": UpdateManagedInstanceDetails,
    "UpdateManagedInstanceGroupDetails": UpdateManagedInstanceGroupDetails,
    "UpdateModuleDetails": UpdateModuleDetails,
    "UpdateModuleStreamDetails": UpdateModuleStreamDetails,
    "UpdateModuleStreamProfileDetails": UpdateModuleStreamProfileDetails,
    "UpdateModuleStreamStateDetails": UpdateModuleStreamStateDetails,
    "UpdateScheduledJobDetails": UpdateScheduledJobDetails,
    "UpdateSoftwareSourceDetails": UpdateSoftwareSourceDetails,
    "WindowsUpdate": WindowsUpdate,
    "WindowsUpdateSummary": WindowsUpdateSummary,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}
