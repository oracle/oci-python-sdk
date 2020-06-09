# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .add_user_to_group_details import AddUserToGroupDetails
from .api_key import ApiKey
from .auth_token import AuthToken
from .authentication_policy import AuthenticationPolicy
from .availability_domain import AvailabilityDomain
from .base_tag_definition_validator import BaseTagDefinitionValidator
from .bulk_action_resource import BulkActionResource
from .bulk_action_resource_type import BulkActionResourceType
from .bulk_action_resource_type_collection import BulkActionResourceTypeCollection
from .bulk_delete_resources_details import BulkDeleteResourcesDetails
from .bulk_delete_tags_details import BulkDeleteTagsDetails
from .bulk_move_resources_details import BulkMoveResourcesDetails
from .change_tag_namespace_compartment_detail import ChangeTagNamespaceCompartmentDetail
from .compartment import Compartment
from .create_api_key_details import CreateApiKeyDetails
from .create_auth_token_details import CreateAuthTokenDetails
from .create_compartment_details import CreateCompartmentDetails
from .create_customer_secret_key_details import CreateCustomerSecretKeyDetails
from .create_dynamic_group_details import CreateDynamicGroupDetails
from .create_group_details import CreateGroupDetails
from .create_identity_provider_details import CreateIdentityProviderDetails
from .create_idp_group_mapping_details import CreateIdpGroupMappingDetails
from .create_network_source_details import CreateNetworkSourceDetails
from .create_o_auth2_client_credential_details import CreateOAuth2ClientCredentialDetails
from .create_policy_details import CreatePolicyDetails
from .create_region_subscription_details import CreateRegionSubscriptionDetails
from .create_saml2_identity_provider_details import CreateSaml2IdentityProviderDetails
from .create_smtp_credential_details import CreateSmtpCredentialDetails
from .create_swift_password_details import CreateSwiftPasswordDetails
from .create_tag_default_details import CreateTagDefaultDetails
from .create_tag_details import CreateTagDetails
from .create_tag_namespace_details import CreateTagNamespaceDetails
from .create_user_details import CreateUserDetails
from .customer_secret_key import CustomerSecretKey
from .customer_secret_key_summary import CustomerSecretKeySummary
from .default_tag_definition_validator import DefaultTagDefinitionValidator
from .dynamic_group import DynamicGroup
from .enum_tag_definition_validator import EnumTagDefinitionValidator
from .fault_domain import FaultDomain
from .fully_qualified_scope import FullyQualifiedScope
from .group import Group
from .identity_provider import IdentityProvider
from .identity_provider_group_summary import IdentityProviderGroupSummary
from .idp_group_mapping import IdpGroupMapping
from .mfa_totp_device import MfaTotpDevice
from .mfa_totp_device_summary import MfaTotpDeviceSummary
from .mfa_totp_token import MfaTotpToken
from .move_compartment_details import MoveCompartmentDetails
from .network_sources import NetworkSources
from .network_sources_summary import NetworkSourcesSummary
from .network_sources_virtual_source_list import NetworkSourcesVirtualSourceList
from .o_auth2_client_credential import OAuth2ClientCredential
from .o_auth2_client_credential_summary import OAuth2ClientCredentialSummary
from .password_policy import PasswordPolicy
from .policy import Policy
from .region import Region
from .region_subscription import RegionSubscription
from .saml2_identity_provider import Saml2IdentityProvider
from .scim_client_credentials import ScimClientCredentials
from .smtp_credential import SmtpCredential
from .smtp_credential_summary import SmtpCredentialSummary
from .swift_password import SwiftPassword
from .tag import Tag
from .tag_default import TagDefault
from .tag_default_summary import TagDefaultSummary
from .tag_namespace import TagNamespace
from .tag_namespace_summary import TagNamespaceSummary
from .tag_summary import TagSummary
from .tagging_work_request import TaggingWorkRequest
from .tagging_work_request_error_summary import TaggingWorkRequestErrorSummary
from .tagging_work_request_log_summary import TaggingWorkRequestLogSummary
from .tagging_work_request_summary import TaggingWorkRequestSummary
from .tenancy import Tenancy
from .ui_password import UIPassword
from .ui_password_information import UIPasswordInformation
from .update_auth_token_details import UpdateAuthTokenDetails
from .update_authentication_policy_details import UpdateAuthenticationPolicyDetails
from .update_compartment_details import UpdateCompartmentDetails
from .update_customer_secret_key_details import UpdateCustomerSecretKeyDetails
from .update_dynamic_group_details import UpdateDynamicGroupDetails
from .update_group_details import UpdateGroupDetails
from .update_identity_provider_details import UpdateIdentityProviderDetails
from .update_idp_group_mapping_details import UpdateIdpGroupMappingDetails
from .update_network_source_details import UpdateNetworkSourceDetails
from .update_o_auth2_client_credential_details import UpdateOAuth2ClientCredentialDetails
from .update_policy_details import UpdatePolicyDetails
from .update_saml2_identity_provider_details import UpdateSaml2IdentityProviderDetails
from .update_smtp_credential_details import UpdateSmtpCredentialDetails
from .update_state_details import UpdateStateDetails
from .update_swift_password_details import UpdateSwiftPasswordDetails
from .update_tag_default_details import UpdateTagDefaultDetails
from .update_tag_details import UpdateTagDetails
from .update_tag_namespace_details import UpdateTagNamespaceDetails
from .update_user_capabilities_details import UpdateUserCapabilitiesDetails
from .update_user_details import UpdateUserDetails
from .user import User
from .user_capabilities import UserCapabilities
from .user_group_membership import UserGroupMembership
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary

# Maps type names to classes for identity services.
identity_type_mapping = {
    "AddUserToGroupDetails": AddUserToGroupDetails,
    "ApiKey": ApiKey,
    "AuthToken": AuthToken,
    "AuthenticationPolicy": AuthenticationPolicy,
    "AvailabilityDomain": AvailabilityDomain,
    "BaseTagDefinitionValidator": BaseTagDefinitionValidator,
    "BulkActionResource": BulkActionResource,
    "BulkActionResourceType": BulkActionResourceType,
    "BulkActionResourceTypeCollection": BulkActionResourceTypeCollection,
    "BulkDeleteResourcesDetails": BulkDeleteResourcesDetails,
    "BulkDeleteTagsDetails": BulkDeleteTagsDetails,
    "BulkMoveResourcesDetails": BulkMoveResourcesDetails,
    "ChangeTagNamespaceCompartmentDetail": ChangeTagNamespaceCompartmentDetail,
    "Compartment": Compartment,
    "CreateApiKeyDetails": CreateApiKeyDetails,
    "CreateAuthTokenDetails": CreateAuthTokenDetails,
    "CreateCompartmentDetails": CreateCompartmentDetails,
    "CreateCustomerSecretKeyDetails": CreateCustomerSecretKeyDetails,
    "CreateDynamicGroupDetails": CreateDynamicGroupDetails,
    "CreateGroupDetails": CreateGroupDetails,
    "CreateIdentityProviderDetails": CreateIdentityProviderDetails,
    "CreateIdpGroupMappingDetails": CreateIdpGroupMappingDetails,
    "CreateNetworkSourceDetails": CreateNetworkSourceDetails,
    "CreateOAuth2ClientCredentialDetails": CreateOAuth2ClientCredentialDetails,
    "CreatePolicyDetails": CreatePolicyDetails,
    "CreateRegionSubscriptionDetails": CreateRegionSubscriptionDetails,
    "CreateSaml2IdentityProviderDetails": CreateSaml2IdentityProviderDetails,
    "CreateSmtpCredentialDetails": CreateSmtpCredentialDetails,
    "CreateSwiftPasswordDetails": CreateSwiftPasswordDetails,
    "CreateTagDefaultDetails": CreateTagDefaultDetails,
    "CreateTagDetails": CreateTagDetails,
    "CreateTagNamespaceDetails": CreateTagNamespaceDetails,
    "CreateUserDetails": CreateUserDetails,
    "CustomerSecretKey": CustomerSecretKey,
    "CustomerSecretKeySummary": CustomerSecretKeySummary,
    "DefaultTagDefinitionValidator": DefaultTagDefinitionValidator,
    "DynamicGroup": DynamicGroup,
    "EnumTagDefinitionValidator": EnumTagDefinitionValidator,
    "FaultDomain": FaultDomain,
    "FullyQualifiedScope": FullyQualifiedScope,
    "Group": Group,
    "IdentityProvider": IdentityProvider,
    "IdentityProviderGroupSummary": IdentityProviderGroupSummary,
    "IdpGroupMapping": IdpGroupMapping,
    "MfaTotpDevice": MfaTotpDevice,
    "MfaTotpDeviceSummary": MfaTotpDeviceSummary,
    "MfaTotpToken": MfaTotpToken,
    "MoveCompartmentDetails": MoveCompartmentDetails,
    "NetworkSources": NetworkSources,
    "NetworkSourcesSummary": NetworkSourcesSummary,
    "NetworkSourcesVirtualSourceList": NetworkSourcesVirtualSourceList,
    "OAuth2ClientCredential": OAuth2ClientCredential,
    "OAuth2ClientCredentialSummary": OAuth2ClientCredentialSummary,
    "PasswordPolicy": PasswordPolicy,
    "Policy": Policy,
    "Region": Region,
    "RegionSubscription": RegionSubscription,
    "Saml2IdentityProvider": Saml2IdentityProvider,
    "ScimClientCredentials": ScimClientCredentials,
    "SmtpCredential": SmtpCredential,
    "SmtpCredentialSummary": SmtpCredentialSummary,
    "SwiftPassword": SwiftPassword,
    "Tag": Tag,
    "TagDefault": TagDefault,
    "TagDefaultSummary": TagDefaultSummary,
    "TagNamespace": TagNamespace,
    "TagNamespaceSummary": TagNamespaceSummary,
    "TagSummary": TagSummary,
    "TaggingWorkRequest": TaggingWorkRequest,
    "TaggingWorkRequestErrorSummary": TaggingWorkRequestErrorSummary,
    "TaggingWorkRequestLogSummary": TaggingWorkRequestLogSummary,
    "TaggingWorkRequestSummary": TaggingWorkRequestSummary,
    "Tenancy": Tenancy,
    "UIPassword": UIPassword,
    "UIPasswordInformation": UIPasswordInformation,
    "UpdateAuthTokenDetails": UpdateAuthTokenDetails,
    "UpdateAuthenticationPolicyDetails": UpdateAuthenticationPolicyDetails,
    "UpdateCompartmentDetails": UpdateCompartmentDetails,
    "UpdateCustomerSecretKeyDetails": UpdateCustomerSecretKeyDetails,
    "UpdateDynamicGroupDetails": UpdateDynamicGroupDetails,
    "UpdateGroupDetails": UpdateGroupDetails,
    "UpdateIdentityProviderDetails": UpdateIdentityProviderDetails,
    "UpdateIdpGroupMappingDetails": UpdateIdpGroupMappingDetails,
    "UpdateNetworkSourceDetails": UpdateNetworkSourceDetails,
    "UpdateOAuth2ClientCredentialDetails": UpdateOAuth2ClientCredentialDetails,
    "UpdatePolicyDetails": UpdatePolicyDetails,
    "UpdateSaml2IdentityProviderDetails": UpdateSaml2IdentityProviderDetails,
    "UpdateSmtpCredentialDetails": UpdateSmtpCredentialDetails,
    "UpdateStateDetails": UpdateStateDetails,
    "UpdateSwiftPasswordDetails": UpdateSwiftPasswordDetails,
    "UpdateTagDefaultDetails": UpdateTagDefaultDetails,
    "UpdateTagDetails": UpdateTagDetails,
    "UpdateTagNamespaceDetails": UpdateTagNamespaceDetails,
    "UpdateUserCapabilitiesDetails": UpdateUserCapabilitiesDetails,
    "UpdateUserDetails": UpdateUserDetails,
    "User": User,
    "UserCapabilities": UserCapabilities,
    "UserGroupMembership": UserGroupMembership,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}
