# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .add_packages_to_software_source_details import AddPackagesToSoftwareSourceDetails
from .api_error import ApiError
from .attach_child_software_source_to_managed_instance_details import AttachChildSoftwareSourceToManagedInstanceDetails
from .attach_parent_software_source_to_managed_instance_details import AttachParentSoftwareSourceToManagedInstanceDetails
from .available_software_source_summary import AvailableSoftwareSourceSummary
from .available_update_summary import AvailableUpdateSummary
from .available_windows_update_summary import AvailableWindowsUpdateSummary
from .change_managed_instance_group_compartment_details import ChangeManagedInstanceGroupCompartmentDetails
from .change_scheduled_job_compartment_details import ChangeScheduledJobCompartmentDetails
from .change_software_source_compartment_details import ChangeSoftwareSourceCompartmentDetails
from .create_managed_instance_group_details import CreateManagedInstanceGroupDetails
from .create_scheduled_job_details import CreateScheduledJobDetails
from .create_software_source_details import CreateSoftwareSourceDetails
from .detach_child_software_source_from_managed_instance_details import DetachChildSoftwareSourceFromManagedInstanceDetails
from .detach_parent_software_source_from_managed_instance_details import DetachParentSoftwareSourceFromManagedInstanceDetails
from .erratum import Erratum
from .erratum_summary import ErratumSummary
from .id import Id
from .installable_package_summary import InstallablePackageSummary
from .installed_package_summary import InstalledPackageSummary
from .installed_windows_update_summary import InstalledWindowsUpdateSummary
from .managed_instance import ManagedInstance
from .managed_instance_group import ManagedInstanceGroup
from .managed_instance_group_summary import ManagedInstanceGroupSummary
from .managed_instance_summary import ManagedInstanceSummary
from .package_name import PackageName
from .recurrence import Recurrence
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
from .update_managed_instance_group_details import UpdateManagedInstanceGroupDetails
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
    "AvailableSoftwareSourceSummary": AvailableSoftwareSourceSummary,
    "AvailableUpdateSummary": AvailableUpdateSummary,
    "AvailableWindowsUpdateSummary": AvailableWindowsUpdateSummary,
    "ChangeManagedInstanceGroupCompartmentDetails": ChangeManagedInstanceGroupCompartmentDetails,
    "ChangeScheduledJobCompartmentDetails": ChangeScheduledJobCompartmentDetails,
    "ChangeSoftwareSourceCompartmentDetails": ChangeSoftwareSourceCompartmentDetails,
    "CreateManagedInstanceGroupDetails": CreateManagedInstanceGroupDetails,
    "CreateScheduledJobDetails": CreateScheduledJobDetails,
    "CreateSoftwareSourceDetails": CreateSoftwareSourceDetails,
    "DetachChildSoftwareSourceFromManagedInstanceDetails": DetachChildSoftwareSourceFromManagedInstanceDetails,
    "DetachParentSoftwareSourceFromManagedInstanceDetails": DetachParentSoftwareSourceFromManagedInstanceDetails,
    "Erratum": Erratum,
    "ErratumSummary": ErratumSummary,
    "Id": Id,
    "InstallablePackageSummary": InstallablePackageSummary,
    "InstalledPackageSummary": InstalledPackageSummary,
    "InstalledWindowsUpdateSummary": InstalledWindowsUpdateSummary,
    "ManagedInstance": ManagedInstance,
    "ManagedInstanceGroup": ManagedInstanceGroup,
    "ManagedInstanceGroupSummary": ManagedInstanceGroupSummary,
    "ManagedInstanceSummary": ManagedInstanceSummary,
    "PackageName": PackageName,
    "Recurrence": Recurrence,
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
    "UpdateManagedInstanceGroupDetails": UpdateManagedInstanceGroupDetails,
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
