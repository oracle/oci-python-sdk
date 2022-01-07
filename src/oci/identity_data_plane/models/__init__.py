# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .accessible_compartment_request import AccessibleCompartmentRequest
from .accessible_compartment_response import AccessibleCompartmentResponse
from .association_authorization_request import AssociationAuthorizationRequest
from .auth_service_user import AuthServiceUser
from .authenticate_client_details import AuthenticateClientDetails
from .authenticate_client_result import AuthenticateClientResult
from .authenticate_user_result import AuthenticateUserResult
from .authentication_policy import AuthenticationPolicy
from .authentication_principal import AuthenticationPrincipal
from .authentication_request import AuthenticationRequest
from .authorization_request import AuthorizationRequest
from .bad_user_state_authenticate_user_result import BadUserStateAuthenticateUserResult
from .claim import Claim
from .client_credentials_response import ClientCredentialsResponse
from .common_principal import CommonPrincipal
from .compartment import Compartment
from .compartment_metadata import CompartmentMetadata
from .context_variable import ContextVariable
from .cost_tracking_tag import CostTrackingTag
from .credential_authenticator_info import CredentialAuthenticatorInfo
from .derived_key_response import DerivedKeyResponse
from .entity_status import EntityStatus
from .filter_group_membership_details import FilterGroupMembershipDetails
from .filter_group_membership_result import FilterGroupMembershipResult
from .generate_scoped_access_token_details import GenerateScopedAccessTokenDetails
from .identity_provider import IdentityProvider
from .jwk import JWK
from .on_behalf_of_request import OnBehalfOfRequest
from .password_policy import PasswordPolicy
from .password_reset_authentication_request import PasswordResetAuthenticationRequest
from .permission import Permission
from .permission_context import PermissionContext
from .principal import Principal
from .refresh_request import RefreshRequest
from .resource_principal_session_token_request import ResourcePrincipalSessionTokenRequest
from .security_token import SecurityToken
from .tenant import Tenant
from .tenant_not_found_authenticate_user_result import TenantNotFoundAuthenticateUserResult
from .thick_authorization_response import ThickAuthorizationResponse
from .thin_association_authorization_response import ThinAssociationAuthorizationResponse
from .thin_authorization_response import ThinAuthorizationResponse
from .user import User
from .user_not_found_authenticate_user_result import UserNotFoundAuthenticateUserResult
from .valid_authenticate_user_result import ValidAuthenticateUserResult
from .x509_federation_request import X509FederationRequest

# Maps type names to classes for identity_data_plane services.
identity_data_plane_type_mapping = {
    "AccessibleCompartmentRequest": AccessibleCompartmentRequest,
    "AccessibleCompartmentResponse": AccessibleCompartmentResponse,
    "AssociationAuthorizationRequest": AssociationAuthorizationRequest,
    "AuthServiceUser": AuthServiceUser,
    "AuthenticateClientDetails": AuthenticateClientDetails,
    "AuthenticateClientResult": AuthenticateClientResult,
    "AuthenticateUserResult": AuthenticateUserResult,
    "AuthenticationPolicy": AuthenticationPolicy,
    "AuthenticationPrincipal": AuthenticationPrincipal,
    "AuthenticationRequest": AuthenticationRequest,
    "AuthorizationRequest": AuthorizationRequest,
    "BadUserStateAuthenticateUserResult": BadUserStateAuthenticateUserResult,
    "Claim": Claim,
    "ClientCredentialsResponse": ClientCredentialsResponse,
    "CommonPrincipal": CommonPrincipal,
    "Compartment": Compartment,
    "CompartmentMetadata": CompartmentMetadata,
    "ContextVariable": ContextVariable,
    "CostTrackingTag": CostTrackingTag,
    "CredentialAuthenticatorInfo": CredentialAuthenticatorInfo,
    "DerivedKeyResponse": DerivedKeyResponse,
    "EntityStatus": EntityStatus,
    "FilterGroupMembershipDetails": FilterGroupMembershipDetails,
    "FilterGroupMembershipResult": FilterGroupMembershipResult,
    "GenerateScopedAccessTokenDetails": GenerateScopedAccessTokenDetails,
    "IdentityProvider": IdentityProvider,
    "JWK": JWK,
    "OnBehalfOfRequest": OnBehalfOfRequest,
    "PasswordPolicy": PasswordPolicy,
    "PasswordResetAuthenticationRequest": PasswordResetAuthenticationRequest,
    "Permission": Permission,
    "PermissionContext": PermissionContext,
    "Principal": Principal,
    "RefreshRequest": RefreshRequest,
    "ResourcePrincipalSessionTokenRequest": ResourcePrincipalSessionTokenRequest,
    "SecurityToken": SecurityToken,
    "Tenant": Tenant,
    "TenantNotFoundAuthenticateUserResult": TenantNotFoundAuthenticateUserResult,
    "ThickAuthorizationResponse": ThickAuthorizationResponse,
    "ThinAssociationAuthorizationResponse": ThinAssociationAuthorizationResponse,
    "ThinAuthorizationResponse": ThinAuthorizationResponse,
    "User": User,
    "UserNotFoundAuthenticateUserResult": UserNotFoundAuthenticateUserResult,
    "ValidAuthenticateUserResult": ValidAuthenticateUserResult,
    "X509FederationRequest": X509FederationRequest
}
