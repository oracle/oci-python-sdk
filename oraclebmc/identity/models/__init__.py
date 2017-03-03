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
from .create_policy_details import CreatePolicyDetails
from .create_swift_password_details import CreateSwiftPasswordDetails
from .create_user_details import CreateUserDetails
from .group import Group
from .policy import Policy
from .swift_password import SwiftPassword
from .ui_password import UIPassword
from .update_compartment_details import UpdateCompartmentDetails
from .update_group_details import UpdateGroupDetails
from .update_policy_details import UpdatePolicyDetails
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
    "CreatePolicyDetails": CreatePolicyDetails,
    "CreateSwiftPasswordDetails": CreateSwiftPasswordDetails,
    "CreateUserDetails": CreateUserDetails,
    "Group": Group,
    "Policy": Policy,
    "SwiftPassword": SwiftPassword,
    "UIPassword": UIPassword,
    "UpdateCompartmentDetails": UpdateCompartmentDetails,
    "UpdateGroupDetails": UpdateGroupDetails,
    "UpdatePolicyDetails": UpdatePolicyDetails,
    "UpdateStateDetails": UpdateStateDetails,
    "UpdateSwiftPasswordDetails": UpdateSwiftPasswordDetails,
    "UpdateUserDetails": UpdateUserDetails,
    "User": User,
    "UserGroupMembership": UserGroupMembership
}
