from __future__ import absolute_import

# import models into model package
from .add_user_to_group_request import AddUserToGroupRequest
from .api_key import ApiKey
from .availability_domain import AvailabilityDomain
from .compartment import Compartment
from .create_api_key_request import CreateApiKeyRequest
from .create_compartment_request import CreateCompartmentRequest
from .create_group_request import CreateGroupRequest
from .create_policy_request import CreatePolicyRequest
from .create_user_request import CreateUserRequest
from .error import Error
from .group import Group
from .policy import Policy
from .ui_password import UIPassword
from .update_compartment_request import UpdateCompartmentRequest
from .update_group_request import UpdateGroupRequest
from .update_policy_request import UpdatePolicyRequest
from .update_ui_password_request import UpdateUiPasswordRequest
from .update_user_request import UpdateUserRequest
from .user import User
from .user_group_membership import UserGroupMembership

# Maps type names to classes for identity services.
identity_type_mapping = {
    'AddUserToGroupRequest': AddUserToGroupRequest,
    'ApiKey': ApiKey,
    'AvailabilityDomain': AvailabilityDomain,
    'Compartment': Compartment,
    'CreateApiKeyRequest': CreateApiKeyRequest,
    'CreateCompartmentRequest': CreateCompartmentRequest,
    'CreateGroupRequest': CreateGroupRequest,
    'CreatePolicyRequest': CreatePolicyRequest,
    'CreateUserRequest': CreateUserRequest,
    'Error': Error,
    'Group': Group,
    'Policy': Policy,
    'UIPassword': UIPassword,
    'UpdateCompartmentRequest': UpdateCompartmentRequest,
    'UpdateGroupRequest': UpdateGroupRequest,
    'UpdatePolicyRequest': UpdatePolicyRequest,
    'UpdateUiPasswordRequest': UpdateUiPasswordRequest,
    'UpdateUserRequest': UpdateUserRequest,
    'User': User,
    'UserGroupMembership': UserGroupMembership,
}