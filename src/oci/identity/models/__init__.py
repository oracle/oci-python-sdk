# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from .add_user_to_group_details import AddUserToGroupDetails
from .api_key import ApiKey
from .auth_token import AuthToken
from .availability_domain import AvailabilityDomain
from .compartment import Compartment
from .create_api_key_details import CreateApiKeyDetails
from .create_auth_token_details import CreateAuthTokenDetails
from .create_compartment_details import CreateCompartmentDetails
from .create_customer_secret_key_details import CreateCustomerSecretKeyDetails
from .create_dynamic_group_details import CreateDynamicGroupDetails
from .create_group_details import CreateGroupDetails
from .create_identity_provider_details import CreateIdentityProviderDetails
from .create_idp_group_mapping_details import CreateIdpGroupMappingDetails
from .create_policy_details import CreatePolicyDetails
from .create_region_subscription_details import CreateRegionSubscriptionDetails
from .create_saml2_identity_provider_details import CreateSaml2IdentityProviderDetails
from .create_smtp_credential_details import CreateSmtpCredentialDetails
from .create_swift_password_details import CreateSwiftPasswordDetails
from .create_tag_details import CreateTagDetails
from .create_tag_namespace_details import CreateTagNamespaceDetails
from .create_user_details import CreateUserDetails
from .customer_secret_key import CustomerSecretKey
from .customer_secret_key_summary import CustomerSecretKeySummary
from .dynamic_group import DynamicGroup
from .fault_domain import FaultDomain
from .group import Group
from .identity_provider import IdentityProvider
from .idp_group_mapping import IdpGroupMapping
from .policy import Policy
from .region import Region
from .region_subscription import RegionSubscription
from .saml2_identity_provider import Saml2IdentityProvider
from .smtp_credential import SmtpCredential
from .smtp_credential_summary import SmtpCredentialSummary
from .swift_password import SwiftPassword
from .tag import Tag
from .tag_namespace import TagNamespace
from .tag_namespace_summary import TagNamespaceSummary
from .tag_summary import TagSummary
from .tenancy import Tenancy
from .ui_password import UIPassword
from .update_auth_token_details import UpdateAuthTokenDetails
from .update_compartment_details import UpdateCompartmentDetails
from .update_customer_secret_key_details import UpdateCustomerSecretKeyDetails
from .update_dynamic_group_details import UpdateDynamicGroupDetails
from .update_group_details import UpdateGroupDetails
from .update_identity_provider_details import UpdateIdentityProviderDetails
from .update_idp_group_mapping_details import UpdateIdpGroupMappingDetails
from .update_policy_details import UpdatePolicyDetails
from .update_saml2_identity_provider_details import UpdateSaml2IdentityProviderDetails
from .update_smtp_credential_details import UpdateSmtpCredentialDetails
from .update_state_details import UpdateStateDetails
from .update_swift_password_details import UpdateSwiftPasswordDetails
from .update_tag_details import UpdateTagDetails
from .update_tag_namespace_details import UpdateTagNamespaceDetails
from .update_user_details import UpdateUserDetails
from .user import User
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
    "AvailabilityDomain": AvailabilityDomain,
    "Compartment": Compartment,
    "CreateApiKeyDetails": CreateApiKeyDetails,
    "CreateAuthTokenDetails": CreateAuthTokenDetails,
    "CreateCompartmentDetails": CreateCompartmentDetails,
    "CreateCustomerSecretKeyDetails": CreateCustomerSecretKeyDetails,
    "CreateDynamicGroupDetails": CreateDynamicGroupDetails,
    "CreateGroupDetails": CreateGroupDetails,
    "CreateIdentityProviderDetails": CreateIdentityProviderDetails,
    "CreateIdpGroupMappingDetails": CreateIdpGroupMappingDetails,
    "CreatePolicyDetails": CreatePolicyDetails,
    "CreateRegionSubscriptionDetails": CreateRegionSubscriptionDetails,
    "CreateSaml2IdentityProviderDetails": CreateSaml2IdentityProviderDetails,
    "CreateSmtpCredentialDetails": CreateSmtpCredentialDetails,
    "CreateSwiftPasswordDetails": CreateSwiftPasswordDetails,
    "CreateTagDetails": CreateTagDetails,
    "CreateTagNamespaceDetails": CreateTagNamespaceDetails,
    "CreateUserDetails": CreateUserDetails,
    "CustomerSecretKey": CustomerSecretKey,
    "CustomerSecretKeySummary": CustomerSecretKeySummary,
    "DynamicGroup": DynamicGroup,
    "FaultDomain": FaultDomain,
    "Group": Group,
    "IdentityProvider": IdentityProvider,
    "IdpGroupMapping": IdpGroupMapping,
    "Policy": Policy,
    "Region": Region,
    "RegionSubscription": RegionSubscription,
    "Saml2IdentityProvider": Saml2IdentityProvider,
    "SmtpCredential": SmtpCredential,
    "SmtpCredentialSummary": SmtpCredentialSummary,
    "SwiftPassword": SwiftPassword,
    "Tag": Tag,
    "TagNamespace": TagNamespace,
    "TagNamespaceSummary": TagNamespaceSummary,
    "TagSummary": TagSummary,
    "Tenancy": Tenancy,
    "UIPassword": UIPassword,
    "UpdateAuthTokenDetails": UpdateAuthTokenDetails,
    "UpdateCompartmentDetails": UpdateCompartmentDetails,
    "UpdateCustomerSecretKeyDetails": UpdateCustomerSecretKeyDetails,
    "UpdateDynamicGroupDetails": UpdateDynamicGroupDetails,
    "UpdateGroupDetails": UpdateGroupDetails,
    "UpdateIdentityProviderDetails": UpdateIdentityProviderDetails,
    "UpdateIdpGroupMappingDetails": UpdateIdpGroupMappingDetails,
    "UpdatePolicyDetails": UpdatePolicyDetails,
    "UpdateSaml2IdentityProviderDetails": UpdateSaml2IdentityProviderDetails,
    "UpdateSmtpCredentialDetails": UpdateSmtpCredentialDetails,
    "UpdateStateDetails": UpdateStateDetails,
    "UpdateSwiftPasswordDetails": UpdateSwiftPasswordDetails,
    "UpdateTagDetails": UpdateTagDetails,
    "UpdateTagNamespaceDetails": UpdateTagNamespaceDetails,
    "UpdateUserDetails": UpdateUserDetails,
    "User": User,
    "UserGroupMembership": UserGroupMembership,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}
