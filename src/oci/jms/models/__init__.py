# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .add_fleet_installation_sites_details import AddFleetInstallationSitesDetails
from .advanced_usage_tracking import AdvancedUsageTracking
from .application_usage import ApplicationUsage
from .application_usage_collection import ApplicationUsageCollection
from .blocklist import Blocklist
from .blocklist_collection import BlocklistCollection
from .blocklist_entry import BlocklistEntry
from .blocklist_target import BlocklistTarget
from .change_fleet_compartment_details import ChangeFleetCompartmentDetails
from .create_blocklist_details import CreateBlocklistDetails
from .create_fleet_details import CreateFleetDetails
from .crypto_analysis_result import CryptoAnalysisResult
from .crypto_analysis_result_collection import CryptoAnalysisResultCollection
from .crypto_analysis_result_summary import CryptoAnalysisResultSummary
from .crypto_event_analysis import CryptoEventAnalysis
from .custom_log import CustomLog
from .deployed_application_usage import DeployedApplicationUsage
from .deployed_application_usage_collection import DeployedApplicationUsageCollection
from .existing_installation_site_id import ExistingInstallationSiteId
from .fleet import Fleet
from .fleet_advanced_feature_configuration import FleetAdvancedFeatureConfiguration
from .fleet_agent_configuration import FleetAgentConfiguration
from .fleet_agent_os_configuration import FleetAgentOsConfiguration
from .fleet_collection import FleetCollection
from .fleet_summary import FleetSummary
from .generate_agent_deploy_script_details import GenerateAgentDeployScriptDetails
from .installation_site import InstallationSite
from .installation_site_collection import InstallationSiteCollection
from .installation_site_summary import InstallationSiteSummary
from .installation_usage import InstallationUsage
from .installation_usage_collection import InstallationUsageCollection
from .java_artifact import JavaArtifact
from .java_family import JavaFamily
from .java_family_collection import JavaFamilyCollection
from .java_family_summary import JavaFamilySummary
from .java_license import JavaLicense
from .java_release import JavaRelease
from .java_release_collection import JavaReleaseCollection
from .java_release_summary import JavaReleaseSummary
from .java_runtime_id import JavaRuntimeId
from .java_server_instance_usage import JavaServerInstanceUsage
from .java_server_instance_usage_collection import JavaServerInstanceUsageCollection
from .java_server_usage import JavaServerUsage
from .java_server_usage_collection import JavaServerUsageCollection
from .jfr_attachment_target import JfrAttachmentTarget
from .jfr_recording import JfrRecording
from .jre_usage import JreUsage
from .jre_usage_collection import JreUsageCollection
from .key_size_algorithm import KeySizeAlgorithm
from .lcm import Lcm
from .library_usage import LibraryUsage
from .library_usage_collection import LibraryUsageCollection
from .managed_instance_usage import ManagedInstanceUsage
from .managed_instance_usage_collection import ManagedInstanceUsageCollection
from .minimum_key_size_settings import MinimumKeySizeSettings
from .new_installation_site import NewInstallationSite
from .operating_system import OperatingSystem
from .post_installation_action_settings import PostInstallationActionSettings
from .principal import Principal
from .remove_fleet_installation_sites_details import RemoveFleetInstallationSitesDetails
from .request_crypto_analyses_details import RequestCryptoAnalysesDetails
from .request_jfr_recordings_details import RequestJfrRecordingsDetails
from .resource_inventory import ResourceInventory
from .scan_java_server_usage_details import ScanJavaServerUsageDetails
from .scan_library_usage_details import ScanLibraryUsageDetails
from .summarized_events_log import SummarizedEventsLog
from .update_fleet_advanced_feature_configuration_details import UpdateFleetAdvancedFeatureConfigurationDetails
from .update_fleet_agent_configuration_details import UpdateFleetAgentConfigurationDetails
from .update_fleet_details import UpdateFleetDetails
from .work_item_collection import WorkItemCollection
from .work_item_summary import WorkItemSummary
from .work_request import WorkRequest
from .work_request_collection import WorkRequestCollection
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource

# Maps type names to classes for jms services.
jms_type_mapping = {
    "AddFleetInstallationSitesDetails": AddFleetInstallationSitesDetails,
    "AdvancedUsageTracking": AdvancedUsageTracking,
    "ApplicationUsage": ApplicationUsage,
    "ApplicationUsageCollection": ApplicationUsageCollection,
    "Blocklist": Blocklist,
    "BlocklistCollection": BlocklistCollection,
    "BlocklistEntry": BlocklistEntry,
    "BlocklistTarget": BlocklistTarget,
    "ChangeFleetCompartmentDetails": ChangeFleetCompartmentDetails,
    "CreateBlocklistDetails": CreateBlocklistDetails,
    "CreateFleetDetails": CreateFleetDetails,
    "CryptoAnalysisResult": CryptoAnalysisResult,
    "CryptoAnalysisResultCollection": CryptoAnalysisResultCollection,
    "CryptoAnalysisResultSummary": CryptoAnalysisResultSummary,
    "CryptoEventAnalysis": CryptoEventAnalysis,
    "CustomLog": CustomLog,
    "DeployedApplicationUsage": DeployedApplicationUsage,
    "DeployedApplicationUsageCollection": DeployedApplicationUsageCollection,
    "ExistingInstallationSiteId": ExistingInstallationSiteId,
    "Fleet": Fleet,
    "FleetAdvancedFeatureConfiguration": FleetAdvancedFeatureConfiguration,
    "FleetAgentConfiguration": FleetAgentConfiguration,
    "FleetAgentOsConfiguration": FleetAgentOsConfiguration,
    "FleetCollection": FleetCollection,
    "FleetSummary": FleetSummary,
    "GenerateAgentDeployScriptDetails": GenerateAgentDeployScriptDetails,
    "InstallationSite": InstallationSite,
    "InstallationSiteCollection": InstallationSiteCollection,
    "InstallationSiteSummary": InstallationSiteSummary,
    "InstallationUsage": InstallationUsage,
    "InstallationUsageCollection": InstallationUsageCollection,
    "JavaArtifact": JavaArtifact,
    "JavaFamily": JavaFamily,
    "JavaFamilyCollection": JavaFamilyCollection,
    "JavaFamilySummary": JavaFamilySummary,
    "JavaLicense": JavaLicense,
    "JavaRelease": JavaRelease,
    "JavaReleaseCollection": JavaReleaseCollection,
    "JavaReleaseSummary": JavaReleaseSummary,
    "JavaRuntimeId": JavaRuntimeId,
    "JavaServerInstanceUsage": JavaServerInstanceUsage,
    "JavaServerInstanceUsageCollection": JavaServerInstanceUsageCollection,
    "JavaServerUsage": JavaServerUsage,
    "JavaServerUsageCollection": JavaServerUsageCollection,
    "JfrAttachmentTarget": JfrAttachmentTarget,
    "JfrRecording": JfrRecording,
    "JreUsage": JreUsage,
    "JreUsageCollection": JreUsageCollection,
    "KeySizeAlgorithm": KeySizeAlgorithm,
    "Lcm": Lcm,
    "LibraryUsage": LibraryUsage,
    "LibraryUsageCollection": LibraryUsageCollection,
    "ManagedInstanceUsage": ManagedInstanceUsage,
    "ManagedInstanceUsageCollection": ManagedInstanceUsageCollection,
    "MinimumKeySizeSettings": MinimumKeySizeSettings,
    "NewInstallationSite": NewInstallationSite,
    "OperatingSystem": OperatingSystem,
    "PostInstallationActionSettings": PostInstallationActionSettings,
    "Principal": Principal,
    "RemoveFleetInstallationSitesDetails": RemoveFleetInstallationSitesDetails,
    "RequestCryptoAnalysesDetails": RequestCryptoAnalysesDetails,
    "RequestJfrRecordingsDetails": RequestJfrRecordingsDetails,
    "ResourceInventory": ResourceInventory,
    "ScanJavaServerUsageDetails": ScanJavaServerUsageDetails,
    "ScanLibraryUsageDetails": ScanLibraryUsageDetails,
    "SummarizedEventsLog": SummarizedEventsLog,
    "UpdateFleetAdvancedFeatureConfigurationDetails": UpdateFleetAdvancedFeatureConfigurationDetails,
    "UpdateFleetAgentConfigurationDetails": UpdateFleetAgentConfigurationDetails,
    "UpdateFleetDetails": UpdateFleetDetails,
    "WorkItemCollection": WorkItemCollection,
    "WorkItemSummary": WorkItemSummary,
    "WorkRequest": WorkRequest,
    "WorkRequestCollection": WorkRequestCollection,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource
}
