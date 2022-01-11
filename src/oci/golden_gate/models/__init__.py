# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .cancel_deployment_backup_details import CancelDeploymentBackupDetails
from .change_database_registration_compartment_details import ChangeDatabaseRegistrationCompartmentDetails
from .change_deployment_backup_compartment_details import ChangeDeploymentBackupCompartmentDetails
from .change_deployment_compartment_details import ChangeDeploymentCompartmentDetails
from .create_database_registration_details import CreateDatabaseRegistrationDetails
from .create_deployment_backup_details import CreateDeploymentBackupDetails
from .create_deployment_details import CreateDeploymentDetails
from .create_ogg_deployment_details import CreateOggDeploymentDetails
from .database_registration import DatabaseRegistration
from .database_registration_collection import DatabaseRegistrationCollection
from .database_registration_summary import DatabaseRegistrationSummary
from .default_cancel_deployment_backup_details import DefaultCancelDeploymentBackupDetails
from .default_restore_deployment_details import DefaultRestoreDeploymentDetails
from .default_start_deployment_details import DefaultStartDeploymentDetails
from .default_stop_deployment_details import DefaultStopDeploymentDetails
from .deployment import Deployment
from .deployment_backup import DeploymentBackup
from .deployment_backup_collection import DeploymentBackupCollection
from .deployment_backup_summary import DeploymentBackupSummary
from .deployment_collection import DeploymentCollection
from .deployment_summary import DeploymentSummary
from .deployment_upgrade import DeploymentUpgrade
from .deployment_upgrade_collection import DeploymentUpgradeCollection
from .deployment_upgrade_summary import DeploymentUpgradeSummary
from .ogg_deployment import OggDeployment
from .restore_deployment_details import RestoreDeploymentDetails
from .start_deployment_details import StartDeploymentDetails
from .stop_deployment_details import StopDeploymentDetails
from .update_database_registration_details import UpdateDatabaseRegistrationDetails
from .update_deployment_backup_details import UpdateDeploymentBackupDetails
from .update_deployment_details import UpdateDeploymentDetails
from .update_ogg_deployment_details import UpdateOggDeploymentDetails
from .upgrade_deployment_current_release_details import UpgradeDeploymentCurrentReleaseDetails
from .upgrade_deployment_details import UpgradeDeploymentDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_resource import WorkRequestResource

# Maps type names to classes for golden_gate services.
golden_gate_type_mapping = {
    "CancelDeploymentBackupDetails": CancelDeploymentBackupDetails,
    "ChangeDatabaseRegistrationCompartmentDetails": ChangeDatabaseRegistrationCompartmentDetails,
    "ChangeDeploymentBackupCompartmentDetails": ChangeDeploymentBackupCompartmentDetails,
    "ChangeDeploymentCompartmentDetails": ChangeDeploymentCompartmentDetails,
    "CreateDatabaseRegistrationDetails": CreateDatabaseRegistrationDetails,
    "CreateDeploymentBackupDetails": CreateDeploymentBackupDetails,
    "CreateDeploymentDetails": CreateDeploymentDetails,
    "CreateOggDeploymentDetails": CreateOggDeploymentDetails,
    "DatabaseRegistration": DatabaseRegistration,
    "DatabaseRegistrationCollection": DatabaseRegistrationCollection,
    "DatabaseRegistrationSummary": DatabaseRegistrationSummary,
    "DefaultCancelDeploymentBackupDetails": DefaultCancelDeploymentBackupDetails,
    "DefaultRestoreDeploymentDetails": DefaultRestoreDeploymentDetails,
    "DefaultStartDeploymentDetails": DefaultStartDeploymentDetails,
    "DefaultStopDeploymentDetails": DefaultStopDeploymentDetails,
    "Deployment": Deployment,
    "DeploymentBackup": DeploymentBackup,
    "DeploymentBackupCollection": DeploymentBackupCollection,
    "DeploymentBackupSummary": DeploymentBackupSummary,
    "DeploymentCollection": DeploymentCollection,
    "DeploymentSummary": DeploymentSummary,
    "DeploymentUpgrade": DeploymentUpgrade,
    "DeploymentUpgradeCollection": DeploymentUpgradeCollection,
    "DeploymentUpgradeSummary": DeploymentUpgradeSummary,
    "OggDeployment": OggDeployment,
    "RestoreDeploymentDetails": RestoreDeploymentDetails,
    "StartDeploymentDetails": StartDeploymentDetails,
    "StopDeploymentDetails": StopDeploymentDetails,
    "UpdateDatabaseRegistrationDetails": UpdateDatabaseRegistrationDetails,
    "UpdateDeploymentBackupDetails": UpdateDeploymentBackupDetails,
    "UpdateDeploymentDetails": UpdateDeploymentDetails,
    "UpdateOggDeploymentDetails": UpdateOggDeploymentDetails,
    "UpgradeDeploymentCurrentReleaseDetails": UpgradeDeploymentCurrentReleaseDetails,
    "UpgradeDeploymentDetails": UpgradeDeploymentDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestResource": WorkRequestResource
}
