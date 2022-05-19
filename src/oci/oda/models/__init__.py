# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .android_channel import AndroidChannel
from .app_event_channel import AppEventChannel
from .application_channel import ApplicationChannel
from .authentication_provider import AuthenticationProvider
from .authentication_provider_collection import AuthenticationProviderCollection
from .authentication_provider_summary import AuthenticationProviderSummary
from .bot import Bot
from .change_oda_instance_compartment_details import ChangeOdaInstanceCompartmentDetails
from .channel import Channel
from .channel_collection import ChannelCollection
from .channel_summary import ChannelSummary
from .clone_digital_assistant_details import CloneDigitalAssistantDetails
from .clone_skill_details import CloneSkillDetails
from .configure_digital_assistant_parameters_details import ConfigureDigitalAssistantParametersDetails
from .cortana_channel import CortanaChannel
from .create_android_channel_details import CreateAndroidChannelDetails
from .create_android_channel_result import CreateAndroidChannelResult
from .create_app_event_channel_details import CreateAppEventChannelDetails
from .create_app_event_channel_result import CreateAppEventChannelResult
from .create_application_channel_details import CreateApplicationChannelDetails
from .create_application_channel_result import CreateApplicationChannelResult
from .create_authentication_provider_details import CreateAuthenticationProviderDetails
from .create_channel_details import CreateChannelDetails
from .create_channel_result import CreateChannelResult
from .create_cortana_channel_details import CreateCortanaChannelDetails
from .create_cortana_channel_result import CreateCortanaChannelResult
from .create_digital_assistant_details import CreateDigitalAssistantDetails
from .create_digital_assistant_version_details import CreateDigitalAssistantVersionDetails
from .create_facebook_channel_details import CreateFacebookChannelDetails
from .create_facebook_channel_result import CreateFacebookChannelResult
from .create_imported_package_details import CreateImportedPackageDetails
from .create_ios_channel_details import CreateIosChannelDetails
from .create_ios_channel_result import CreateIosChannelResult
from .create_ms_teams_channel_details import CreateMSTeamsChannelDetails
from .create_ms_teams_channel_result import CreateMSTeamsChannelResult
from .create_new_digital_assistant_details import CreateNewDigitalAssistantDetails
from .create_new_skill_details import CreateNewSkillDetails
from .create_oss_channel_details import CreateOSSChannelDetails
from .create_oss_channel_result import CreateOSSChannelResult
from .create_oda_instance_attachment_details import CreateOdaInstanceAttachmentDetails
from .create_oda_instance_details import CreateOdaInstanceDetails
from .create_osvc_channel_details import CreateOsvcChannelDetails
from .create_osvc_channel_result import CreateOsvcChannelResult
from .create_service_cloud_channel_details import CreateServiceCloudChannelDetails
from .create_service_cloud_channel_result import CreateServiceCloudChannelResult
from .create_skill_details import CreateSkillDetails
from .create_skill_parameter_details import CreateSkillParameterDetails
from .create_skill_version_details import CreateSkillVersionDetails
from .create_slack_channel_details import CreateSlackChannelDetails
from .create_slack_channel_result import CreateSlackChannelResult
from .create_test_channel_result import CreateTestChannelResult
from .create_translator_details import CreateTranslatorDetails
from .create_twilio_channel_details import CreateTwilioChannelDetails
from .create_twilio_channel_result import CreateTwilioChannelResult
from .create_web_channel_details import CreateWebChannelDetails
from .create_web_channel_result import CreateWebChannelResult
from .create_webhook_channel_details import CreateWebhookChannelDetails
from .create_webhook_channel_result import CreateWebhookChannelResult
from .default_parameter_values import DefaultParameterValues
from .digital_assistant import DigitalAssistant
from .digital_assistant_collection import DigitalAssistantCollection
from .digital_assistant_parameter import DigitalAssistantParameter
from .digital_assistant_parameter_collection import DigitalAssistantParameterCollection
from .digital_assistant_parameter_summary import DigitalAssistantParameterSummary
from .digital_assistant_parameter_value import DigitalAssistantParameterValue
from .digital_assistant_summary import DigitalAssistantSummary
from .error_body import ErrorBody
from .export_bot_details import ExportBotDetails
from .export_digital_assistant_details import ExportDigitalAssistantDetails
from .export_skill_details import ExportSkillDetails
from .extend_digital_assistant_details import ExtendDigitalAssistantDetails
from .extend_skill_details import ExtendSkillDetails
from .facebook_channel import FacebookChannel
from .import_bot_details import ImportBotDetails
from .import_contract import ImportContract
from .imported_package import ImportedPackage
from .imported_package_summary import ImportedPackageSummary
from .ios_channel import IosChannel
from .ms_teams_channel import MSTeamsChannel
from .metadata_property import MetadataProperty
from .oss_channel import OSSChannel
from .oda_instance import OdaInstance
from .oda_instance_attachment import OdaInstanceAttachment
from .oda_instance_attachment_collection import OdaInstanceAttachmentCollection
from .oda_instance_attachment_owner import OdaInstanceAttachmentOwner
from .oda_instance_attachment_summary import OdaInstanceAttachmentSummary
from .oda_instance_owner import OdaInstanceOwner
from .oda_instance_summary import OdaInstanceSummary
from .osvc_channel import OsvcChannel
from .package import Package
from .package_summary import PackageSummary
from .parameter import Parameter
from .parameter_definition import ParameterDefinition
from .resource_type_default_parameter_values import ResourceTypeDefaultParameterValues
from .resource_type_import_contract import ResourceTypeImportContract
from .resource_type_metadata import ResourceTypeMetadata
from .restricted_operation import RestrictedOperation
from .service_cloud_channel import ServiceCloudChannel
from .skill import Skill
from .skill_collection import SkillCollection
from .skill_parameter import SkillParameter
from .skill_parameter_collection import SkillParameterCollection
from .skill_parameter_summary import SkillParameterSummary
from .skill_summary import SkillSummary
from .slack_channel import SlackChannel
from .storage_location import StorageLocation
from .test_channel import TestChannel
from .translator import Translator
from .translator_collection import TranslatorCollection
from .translator_summary import TranslatorSummary
from .twilio_channel import TwilioChannel
from .update_android_channel_details import UpdateAndroidChannelDetails
from .update_app_event_channel_details import UpdateAppEventChannelDetails
from .update_application_channel_details import UpdateApplicationChannelDetails
from .update_authentication_provider_details import UpdateAuthenticationProviderDetails
from .update_channel_details import UpdateChannelDetails
from .update_cortana_channel_details import UpdateCortanaChannelDetails
from .update_digital_assistant_details import UpdateDigitalAssistantDetails
from .update_digital_assistant_parameter_details import UpdateDigitalAssistantParameterDetails
from .update_facebook_channel_details import UpdateFacebookChannelDetails
from .update_imported_package_details import UpdateImportedPackageDetails
from .update_ios_channel_details import UpdateIosChannelDetails
from .update_ms_teams_channel_details import UpdateMSTeamsChannelDetails
from .update_oss_channel_details import UpdateOSSChannelDetails
from .update_oda_instance_attachment_details import UpdateOdaInstanceAttachmentDetails
from .update_oda_instance_details import UpdateOdaInstanceDetails
from .update_osvc_channel_details import UpdateOsvcChannelDetails
from .update_service_cloud_channel_details import UpdateServiceCloudChannelDetails
from .update_skill_details import UpdateSkillDetails
from .update_skill_parameter_details import UpdateSkillParameterDetails
from .update_slack_channel_details import UpdateSlackChannelDetails
from .update_translator_details import UpdateTranslatorDetails
from .update_twilio_channel_details import UpdateTwilioChannelDetails
from .update_web_channel_details import UpdateWebChannelDetails
from .update_webhook_channel_details import UpdateWebhookChannelDetails
from .web_channel import WebChannel
from .webhook_channel import WebhookChannel
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary

# Maps type names to classes for oda services.
oda_type_mapping = {
    "AndroidChannel": AndroidChannel,
    "AppEventChannel": AppEventChannel,
    "ApplicationChannel": ApplicationChannel,
    "AuthenticationProvider": AuthenticationProvider,
    "AuthenticationProviderCollection": AuthenticationProviderCollection,
    "AuthenticationProviderSummary": AuthenticationProviderSummary,
    "Bot": Bot,
    "ChangeOdaInstanceCompartmentDetails": ChangeOdaInstanceCompartmentDetails,
    "Channel": Channel,
    "ChannelCollection": ChannelCollection,
    "ChannelSummary": ChannelSummary,
    "CloneDigitalAssistantDetails": CloneDigitalAssistantDetails,
    "CloneSkillDetails": CloneSkillDetails,
    "ConfigureDigitalAssistantParametersDetails": ConfigureDigitalAssistantParametersDetails,
    "CortanaChannel": CortanaChannel,
    "CreateAndroidChannelDetails": CreateAndroidChannelDetails,
    "CreateAndroidChannelResult": CreateAndroidChannelResult,
    "CreateAppEventChannelDetails": CreateAppEventChannelDetails,
    "CreateAppEventChannelResult": CreateAppEventChannelResult,
    "CreateApplicationChannelDetails": CreateApplicationChannelDetails,
    "CreateApplicationChannelResult": CreateApplicationChannelResult,
    "CreateAuthenticationProviderDetails": CreateAuthenticationProviderDetails,
    "CreateChannelDetails": CreateChannelDetails,
    "CreateChannelResult": CreateChannelResult,
    "CreateCortanaChannelDetails": CreateCortanaChannelDetails,
    "CreateCortanaChannelResult": CreateCortanaChannelResult,
    "CreateDigitalAssistantDetails": CreateDigitalAssistantDetails,
    "CreateDigitalAssistantVersionDetails": CreateDigitalAssistantVersionDetails,
    "CreateFacebookChannelDetails": CreateFacebookChannelDetails,
    "CreateFacebookChannelResult": CreateFacebookChannelResult,
    "CreateImportedPackageDetails": CreateImportedPackageDetails,
    "CreateIosChannelDetails": CreateIosChannelDetails,
    "CreateIosChannelResult": CreateIosChannelResult,
    "CreateMSTeamsChannelDetails": CreateMSTeamsChannelDetails,
    "CreateMSTeamsChannelResult": CreateMSTeamsChannelResult,
    "CreateNewDigitalAssistantDetails": CreateNewDigitalAssistantDetails,
    "CreateNewSkillDetails": CreateNewSkillDetails,
    "CreateOSSChannelDetails": CreateOSSChannelDetails,
    "CreateOSSChannelResult": CreateOSSChannelResult,
    "CreateOdaInstanceAttachmentDetails": CreateOdaInstanceAttachmentDetails,
    "CreateOdaInstanceDetails": CreateOdaInstanceDetails,
    "CreateOsvcChannelDetails": CreateOsvcChannelDetails,
    "CreateOsvcChannelResult": CreateOsvcChannelResult,
    "CreateServiceCloudChannelDetails": CreateServiceCloudChannelDetails,
    "CreateServiceCloudChannelResult": CreateServiceCloudChannelResult,
    "CreateSkillDetails": CreateSkillDetails,
    "CreateSkillParameterDetails": CreateSkillParameterDetails,
    "CreateSkillVersionDetails": CreateSkillVersionDetails,
    "CreateSlackChannelDetails": CreateSlackChannelDetails,
    "CreateSlackChannelResult": CreateSlackChannelResult,
    "CreateTestChannelResult": CreateTestChannelResult,
    "CreateTranslatorDetails": CreateTranslatorDetails,
    "CreateTwilioChannelDetails": CreateTwilioChannelDetails,
    "CreateTwilioChannelResult": CreateTwilioChannelResult,
    "CreateWebChannelDetails": CreateWebChannelDetails,
    "CreateWebChannelResult": CreateWebChannelResult,
    "CreateWebhookChannelDetails": CreateWebhookChannelDetails,
    "CreateWebhookChannelResult": CreateWebhookChannelResult,
    "DefaultParameterValues": DefaultParameterValues,
    "DigitalAssistant": DigitalAssistant,
    "DigitalAssistantCollection": DigitalAssistantCollection,
    "DigitalAssistantParameter": DigitalAssistantParameter,
    "DigitalAssistantParameterCollection": DigitalAssistantParameterCollection,
    "DigitalAssistantParameterSummary": DigitalAssistantParameterSummary,
    "DigitalAssistantParameterValue": DigitalAssistantParameterValue,
    "DigitalAssistantSummary": DigitalAssistantSummary,
    "ErrorBody": ErrorBody,
    "ExportBotDetails": ExportBotDetails,
    "ExportDigitalAssistantDetails": ExportDigitalAssistantDetails,
    "ExportSkillDetails": ExportSkillDetails,
    "ExtendDigitalAssistantDetails": ExtendDigitalAssistantDetails,
    "ExtendSkillDetails": ExtendSkillDetails,
    "FacebookChannel": FacebookChannel,
    "ImportBotDetails": ImportBotDetails,
    "ImportContract": ImportContract,
    "ImportedPackage": ImportedPackage,
    "ImportedPackageSummary": ImportedPackageSummary,
    "IosChannel": IosChannel,
    "MSTeamsChannel": MSTeamsChannel,
    "MetadataProperty": MetadataProperty,
    "OSSChannel": OSSChannel,
    "OdaInstance": OdaInstance,
    "OdaInstanceAttachment": OdaInstanceAttachment,
    "OdaInstanceAttachmentCollection": OdaInstanceAttachmentCollection,
    "OdaInstanceAttachmentOwner": OdaInstanceAttachmentOwner,
    "OdaInstanceAttachmentSummary": OdaInstanceAttachmentSummary,
    "OdaInstanceOwner": OdaInstanceOwner,
    "OdaInstanceSummary": OdaInstanceSummary,
    "OsvcChannel": OsvcChannel,
    "Package": Package,
    "PackageSummary": PackageSummary,
    "Parameter": Parameter,
    "ParameterDefinition": ParameterDefinition,
    "ResourceTypeDefaultParameterValues": ResourceTypeDefaultParameterValues,
    "ResourceTypeImportContract": ResourceTypeImportContract,
    "ResourceTypeMetadata": ResourceTypeMetadata,
    "RestrictedOperation": RestrictedOperation,
    "ServiceCloudChannel": ServiceCloudChannel,
    "Skill": Skill,
    "SkillCollection": SkillCollection,
    "SkillParameter": SkillParameter,
    "SkillParameterCollection": SkillParameterCollection,
    "SkillParameterSummary": SkillParameterSummary,
    "SkillSummary": SkillSummary,
    "SlackChannel": SlackChannel,
    "StorageLocation": StorageLocation,
    "TestChannel": TestChannel,
    "Translator": Translator,
    "TranslatorCollection": TranslatorCollection,
    "TranslatorSummary": TranslatorSummary,
    "TwilioChannel": TwilioChannel,
    "UpdateAndroidChannelDetails": UpdateAndroidChannelDetails,
    "UpdateAppEventChannelDetails": UpdateAppEventChannelDetails,
    "UpdateApplicationChannelDetails": UpdateApplicationChannelDetails,
    "UpdateAuthenticationProviderDetails": UpdateAuthenticationProviderDetails,
    "UpdateChannelDetails": UpdateChannelDetails,
    "UpdateCortanaChannelDetails": UpdateCortanaChannelDetails,
    "UpdateDigitalAssistantDetails": UpdateDigitalAssistantDetails,
    "UpdateDigitalAssistantParameterDetails": UpdateDigitalAssistantParameterDetails,
    "UpdateFacebookChannelDetails": UpdateFacebookChannelDetails,
    "UpdateImportedPackageDetails": UpdateImportedPackageDetails,
    "UpdateIosChannelDetails": UpdateIosChannelDetails,
    "UpdateMSTeamsChannelDetails": UpdateMSTeamsChannelDetails,
    "UpdateOSSChannelDetails": UpdateOSSChannelDetails,
    "UpdateOdaInstanceAttachmentDetails": UpdateOdaInstanceAttachmentDetails,
    "UpdateOdaInstanceDetails": UpdateOdaInstanceDetails,
    "UpdateOsvcChannelDetails": UpdateOsvcChannelDetails,
    "UpdateServiceCloudChannelDetails": UpdateServiceCloudChannelDetails,
    "UpdateSkillDetails": UpdateSkillDetails,
    "UpdateSkillParameterDetails": UpdateSkillParameterDetails,
    "UpdateSlackChannelDetails": UpdateSlackChannelDetails,
    "UpdateTranslatorDetails": UpdateTranslatorDetails,
    "UpdateTwilioChannelDetails": UpdateTwilioChannelDetails,
    "UpdateWebChannelDetails": UpdateWebChannelDetails,
    "UpdateWebhookChannelDetails": UpdateWebhookChannelDetails,
    "WebChannel": WebChannel,
    "WebhookChannel": WebhookChannel,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}
