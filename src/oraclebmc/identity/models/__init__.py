# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from .add_user_to_group_details import AddUserToGroupDetails
from .api_key import ApiKey
from .availability_domain import AvailabilityDomain
from .compartment import Compartment
from .create_api_key_details import CreateApiKeyDetails
from .create_compartment_details import CreateCompartmentDetails
from .create_group_details import CreateGroupDetails
from .create_identity_provider_details import CreateIdentityProviderDetails
from .create_idp_group_mapping_details import CreateIdpGroupMappingDetails
from .create_policy_details import CreatePolicyDetails
from .create_region_subscription_details import CreateRegionSubscriptionDetails
from .create_saml2_identity_provider_details import CreateSaml2IdentityProviderDetails
from .create_swift_password_details import CreateSwiftPasswordDetails
from .create_user_details import CreateUserDetails
from .group import Group
from .identity_provider import IdentityProvider
from .idp_group_mapping import IdpGroupMapping
from .policy import Policy
from .region import Region
from .region_subscription import RegionSubscription
from .saml2_identity_provider import Saml2IdentityProvider
from .swift_password import SwiftPassword
from .tenancy import Tenancy
from .ui_password import UIPassword
from .update_compartment_details import UpdateCompartmentDetails
from .update_group_details import UpdateGroupDetails
from .update_identity_provider_details import UpdateIdentityProviderDetails
from .update_idp_group_mapping_details import UpdateIdpGroupMappingDetails
from .update_policy_details import UpdatePolicyDetails
from .update_saml2_identity_provider_details import UpdateSaml2IdentityProviderDetails
from .update_state_details import UpdateStateDetails
from .update_swift_password_details import UpdateSwiftPasswordDetails
from .update_user_details import UpdateUserDetails
from .user import User
from .user_group_membership import UserGroupMembership

# Maps type names to classes for identity services.
identity_type_mapping = {
    "AddUserToGroupDetails": AddUserToGroupDetails,
    "ApiKey": ApiKey,
    "AvailabilityDomain": AvailabilityDomain,
    "Compartment": Compartment,
    "CreateApiKeyDetails": CreateApiKeyDetails,
    "CreateCompartmentDetails": CreateCompartmentDetails,
    "CreateGroupDetails": CreateGroupDetails,
    "CreateIdentityProviderDetails": CreateIdentityProviderDetails,
    "CreateIdpGroupMappingDetails": CreateIdpGroupMappingDetails,
    "CreatePolicyDetails": CreatePolicyDetails,
    "CreateRegionSubscriptionDetails": CreateRegionSubscriptionDetails,
    "CreateSaml2IdentityProviderDetails": CreateSaml2IdentityProviderDetails,
    "CreateSwiftPasswordDetails": CreateSwiftPasswordDetails,
    "CreateUserDetails": CreateUserDetails,
    "Group": Group,
    "IdentityProvider": IdentityProvider,
    "IdpGroupMapping": IdpGroupMapping,
    "Policy": Policy,
    "Region": Region,
    "RegionSubscription": RegionSubscription,
    "Saml2IdentityProvider": Saml2IdentityProvider,
    "SwiftPassword": SwiftPassword,
    "Tenancy": Tenancy,
    "UIPassword": UIPassword,
    "UpdateCompartmentDetails": UpdateCompartmentDetails,
    "UpdateGroupDetails": UpdateGroupDetails,
    "UpdateIdentityProviderDetails": UpdateIdentityProviderDetails,
    "UpdateIdpGroupMappingDetails": UpdateIdpGroupMappingDetails,
    "UpdatePolicyDetails": UpdatePolicyDetails,
    "UpdateSaml2IdentityProviderDetails": UpdateSaml2IdentityProviderDetails,
    "UpdateStateDetails": UpdateStateDetails,
    "UpdateSwiftPasswordDetails": UpdateSwiftPasswordDetails,
    "UpdateUserDetails": UpdateUserDetails,
    "User": User,
    "UserGroupMembership": UserGroupMembership
}
