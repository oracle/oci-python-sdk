# coding: utf-8

# This is a modified version of the same template from swagger-codegen.
# The original can be found at https://github.com/swagger-api/swagger-codegen.
# The original license is below.
#
#     Copyright 2016 SmartBear Software
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#
#     Ref: https://github.com/swagger-api/swagger-codegen

from __future__ import absolute_import

# python 2 and python 3 compatibility library
from six import iteritems
from io import IOBase

class IdentityApi(object):

    def __init__(self, api_client):
        self.api_client = api_client


    def add_user_to_group(self, add_user_to_group_details, **kwargs):
        """
        AddUserToGroup
        Adds the specified user to the specified group and returns a `UserGroupMembership` object with its own OCID.\n\nAfter you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the\nobject, first make sure its `lifecycleState` has changed to ACTIVE.\n

        :param AddUserToGroupDetails add_user_to_group_details: Request object for adding a user to a group. (required)
        :param str opc_retry_token: A token that uniquely identifies a request so it can be retried in case of a timeout or\nserver error without risk of executing that same action again. Retry tokens expire after 24\nhours, but can be invalidated before then due to conflicting operations (e.g., if a resource\nhas been deleted and purged from the system, then a retry of the original creation request\nmay be rejected).\n
        :return: A Response object with data of type UserGroupMembership
        """

        all_params = ['add_user_to_group_details', 'opc_retry_token']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_user_to_group" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'add_user_to_group_details' is set
        if ('add_user_to_group_details' not in params) or (params['add_user_to_group_details'] is None):
            raise ValueError("Missing the required parameter `add_user_to_group_details` when calling `add_user_to_group`")

        resource_path = '/userGroupMemberships/'
        path_params = {}

        query_params = {}

        header_params = {}
        if 'opc_retry_token' in params:
            header_params['opc-retry-token'] = params['opc_retry_token']

        body_params = None
        if 'add_user_to_group_details' in params:
            body_params = params['add_user_to_group_details']

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_identity_api,
                                            resource_path,
                                            'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='UserGroupMembership')
        return response

    def create_compartment(self, create_compartment_details, **kwargs):
        """
        CreateCompartment
        Creates a new compartment in your tenancy. A compartment is a collection of related resources that can\nbe accessed only by certain groups that have been given permission in a policy. For conceptual\ninformation about compartments and other Identity Service components,\nsee [Overview of the Identity Service](../../../#Identity/Concepts/overview.htm).\n\nYou must specify your tenancy's OCID as the compartment ID in the request object (all Identity Service\nresources reside within the tenancy itself). Remember that the tenancy is simply the root compartment.\nFor information about OCIDs, see [Resource Identifiers](../../../#General/Concepts/identifiers.htm).\n\nYou must also specify a *name* for the compartment, which must be unique across all compartments in\nyour tenancy and cannot be changed. You can use this name or the OCID when writing policies that apply\nto the compartment. For more information about policies, see\n[Policies](../../../#Identity/Concepts/policies.htm).\n\nYou must also specify a *description* for the compartment (although it can be an empty string). It does\nnot have to be unique, and you can change it anytime with [UpdateCompartment](#/en/identity/20160918/Compartment/UpdateCompartment).\n\nAfter you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the\nobject, first make sure its `lifecycleState` has changed to ACTIVE.\n\nTo place a resource in a compartment, simply specify the compartment ID in the \"Create\" request object when\ninitially creating the resource. For example, to launch an instance into a particular compartment, specify\nthat compartment's OCID in the `LaunchInstance` request. You can't move an existing resource from one\ncompartment to another.\n\nFor information about endpoints and signing API requests,\nsee [Making API Requests](../../../#API/Concepts/usingapi.htm).\n

        :param CreateCompartmentDetails create_compartment_details: Request object for creating a new compartment. (required)
        :param str opc_retry_token: A token that uniquely identifies a request so it can be retried in case of a timeout or\nserver error without risk of executing that same action again. Retry tokens expire after 24\nhours, but can be invalidated before then due to conflicting operations (e.g., if a resource\nhas been deleted and purged from the system, then a retry of the original creation request\nmay be rejected).\n
        :return: A Response object with data of type Compartment
        """

        all_params = ['create_compartment_details', 'opc_retry_token']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_compartment" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'create_compartment_details' is set
        if ('create_compartment_details' not in params) or (params['create_compartment_details'] is None):
            raise ValueError("Missing the required parameter `create_compartment_details` when calling `create_compartment`")

        resource_path = '/compartments/'
        path_params = {}

        query_params = {}

        header_params = {}
        if 'opc_retry_token' in params:
            header_params['opc-retry-token'] = params['opc_retry_token']

        body_params = None
        if 'create_compartment_details' in params:
            body_params = params['create_compartment_details']

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_identity_api,
                                            resource_path,
                                            'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='Compartment')
        return response

    def create_group(self, create_group_details, **kwargs):
        """
        CreateGroup
        Creates a new group in your tenancy. A group is a container for users who all need the same permissions.\nFor conceptual information about groups and other Identity Service components,\nsee [Overview of the Identity Service](../../../#Identity/Concepts/overview.htm).\n\nYou must specify your tenancy's OCID as the compartment ID in the request object (remember that the tenancy\nis simply the root compartment). Notice that Identity Service resources reside within the tenancy itself,\nunlike cloud resources such as compute instances, which typically reside within compartments inside the tenancy.\nFor information about OCIDs, see [Resource Identifiers](../../../#General/Concepts/identifiers.htm).\n\nYou must also specify a *name* for the group, which must be unique across all groups in your tenancy and\ncannot be changed. You can use this name or the OCID when writing policies that apply to the group. For more\ninformation about policies, see [Policies](../../../#Identity/Concepts/policies.htm).\n\nYou must also specify a *description* for the group (although it can be an empty string). It does not\nhave to be unique, and you can change it anytime with [UpdateGroup](#/en/identity/20160918/Group/UpdateGroup).\n\nAfter you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the object, first\nmake sure its `lifecycleState` has changed to ACTIVE.\n\nAfter creating the group, you need to put users in it and write policies for it.\nSee [AddUserToGroup](#/en/identity/20160918/UserGroupMembership/AddUserToGroup) and [CreatePolicy](#/en/identity/20160918/Policy/CreatePolicy).\n\nFor information about endpoints and signing API requests, see\n[Making API Requests](../../../#API/Concepts/usingapi.htm).\n

        :param CreateGroupDetails create_group_details: Request object for creating a new group. (required)
        :param str opc_retry_token: A token that uniquely identifies a request so it can be retried in case of a timeout or\nserver error without risk of executing that same action again. Retry tokens expire after 24\nhours, but can be invalidated before then due to conflicting operations (e.g., if a resource\nhas been deleted and purged from the system, then a retry of the original creation request\nmay be rejected).\n
        :return: A Response object with data of type Group
        """

        all_params = ['create_group_details', 'opc_retry_token']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_group" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'create_group_details' is set
        if ('create_group_details' not in params) or (params['create_group_details'] is None):
            raise ValueError("Missing the required parameter `create_group_details` when calling `create_group`")

        resource_path = '/groups/'
        path_params = {}

        query_params = {}

        header_params = {}
        if 'opc_retry_token' in params:
            header_params['opc-retry-token'] = params['opc_retry_token']

        body_params = None
        if 'create_group_details' in params:
            body_params = params['create_group_details']

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_identity_api,
                                            resource_path,
                                            'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='Group')
        return response

    def create_or_reset_ui_password(self, user_id, **kwargs):
        """
        CreateOrResetUIPassword
        Creates a new Console one-time password for the specified user. For more information about user\ncredentials, see [User Credentials](../../../#Identity/Concepts/usercredentials.htm).\n\nUse this operation after creating a new user, or if a user forgets their password. The new one-time\npassword is returned to you in the response, and you must securely deliver it to the user. They'll\nbe prompted to change this password the next time they sign in to the Console.\n\n**Note:** The user's Console login is the unique name you specified when you created the user\n(see [CreateUser](#/en/identity/20160918/User/CreateUser)).\n

        :param str user_id: The user's OCID. (required)
        :param str opc_retry_token: A token that uniquely identifies a request so it can be retried in case of a timeout or\nserver error without risk of executing that same action again. Retry tokens expire after 24\nhours, but can be invalidated before then due to conflicting operations (e.g., if a resource\nhas been deleted and purged from the system, then a retry of the original creation request\nmay be rejected).\n
        :return: A Response object with data of type UIPassword
        """

        all_params = ['user_id', 'opc_retry_token']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_or_reset_ui_password" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `create_or_reset_ui_password`")

        resource_path = '/users/{userId}/uiPassword'
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

        query_params = {}

        header_params = {}
        if 'opc_retry_token' in params:
            header_params['opc-retry-token'] = params['opc_retry_token']

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_identity_api,
                                            resource_path,
                                            'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='UIPassword')
        return response

    def create_policy(self, create_policy_details, **kwargs):
        """
        CreatePolicy
        Creates a new policy in your tenancy. A policy is a document that specifies permissions for the groups\nand compartments in your tenancy. For information about policies and other Identity Service components,\nsee [Overview of the Identity Service](../../../#Identity/Concepts/overview.htm).\n\nYou must specify your tenancy's OCID as the compartment ID in the request object (all Identity Service\nresources reside within the tenancy itself). For information about OCIDs, see\n[Resource Identifiers](../../../#General/Concepts/identifiers.htm).\n\nYou must also specify a *name* for the policy, which must be unique across all policies in your tenancy\nand cannot be changed.\n\nYou must also specify a *description* for the policy (although it can be an empty string). It does not\nhave to be unique, and you can change it anytime with [UpdatePolicy](#/en/identity/20160918/Policy/UpdatePolicy).\n\nYou must specify one or more policy statements in the statements array. For information about writing\npolicies, see [Policies](../../../#Identity/Concepts/policies.htm).\n\nAfter you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the\nobject, first make sure its `lifecycleState` has changed to ACTIVE.\n\nNew policies take effect typically within 10 seconds.\n\nFor information about endpoints and signing API requests,\nsee [Making API Requests](../../../#API/Concepts/usingapi.htm).\n

        :param CreatePolicyDetails create_policy_details: Request object for creating a new policy. (required)
        :param str opc_retry_token: A token that uniquely identifies a request so it can be retried in case of a timeout or\nserver error without risk of executing that same action again. Retry tokens expire after 24\nhours, but can be invalidated before then due to conflicting operations (e.g., if a resource\nhas been deleted and purged from the system, then a retry of the original creation request\nmay be rejected).\n
        :return: A Response object with data of type Policy
        """

        all_params = ['create_policy_details', 'opc_retry_token']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_policy" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'create_policy_details' is set
        if ('create_policy_details' not in params) or (params['create_policy_details'] is None):
            raise ValueError("Missing the required parameter `create_policy_details` when calling `create_policy`")

        resource_path = '/policies/'
        path_params = {}

        query_params = {}

        header_params = {}
        if 'opc_retry_token' in params:
            header_params['opc-retry-token'] = params['opc_retry_token']

        body_params = None
        if 'create_policy_details' in params:
            body_params = params['create_policy_details']

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_identity_api,
                                            resource_path,
                                            'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='Policy')
        return response

    def create_swift_password(self, create_swift_password_details, user_id, **kwargs):
        """
        CreateSwiftPassword
        Creates a new Swift password for the specified user. A user can have up to two Swift passwords at a time. Swift\npasswords never expire. For information about what Swift passwords are for, see\n[Managing User Credentials](../../../#Identity/Tasks/managingcredentials.htm).\n\nYou must specify a *description* for the Swift password (although it can be an empty string). It does not\nhave to be unique, and you can change it anytime with [UpdateSwiftPassword](#/en/identity/20160918/SwiftPassword/UpdateSwiftPassword).\n\nEvery user has permission to create a Swift password for *their own user ID*. An administrator in your organization\ndoes not need to write a policy to give users this ability. To compare, administrators who have permission to the\ntenancy can use this operation to create a Swift password for any user, including themselves.\n

        :param CreateSwiftPasswordDetails create_swift_password_details: Request object for creating a new swift password. (required)
        :param str user_id: The user's OCID. (required)
        :param str opc_retry_token: A token that uniquely identifies a request so it can be retried in case of a timeout or\nserver error without risk of executing that same action again. Retry tokens expire after 24\nhours, but can be invalidated before then due to conflicting operations (e.g., if a resource\nhas been deleted and purged from the system, then a retry of the original creation request\nmay be rejected).\n
        :return: A Response object with data of type SwiftPassword
        """

        all_params = ['create_swift_password_details', 'user_id', 'opc_retry_token']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_swift_password" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'create_swift_password_details' is set
        if ('create_swift_password_details' not in params) or (params['create_swift_password_details'] is None):
            raise ValueError("Missing the required parameter `create_swift_password_details` when calling `create_swift_password`")
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `create_swift_password`")

        resource_path = '/users/{userId}/swiftPasswords/'
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

        query_params = {}

        header_params = {}
        if 'opc_retry_token' in params:
            header_params['opc-retry-token'] = params['opc_retry_token']

        body_params = None
        if 'create_swift_password_details' in params:
            body_params = params['create_swift_password_details']

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_identity_api,
                                            resource_path,
                                            'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='SwiftPassword')
        return response

    def create_user(self, create_user_details, **kwargs):
        """
        CreateUser
        Creates a new user in your tenancy. For conceptual information about users, your tenancy, and other\nIdentity Service components, see [Overview of the Identity Service](../../../#Identity/Concepts/overview.htm).\n\nYou must specify your tenancy's OCID as the compartment ID in the request object (remember that the\ntenancy is simply the root compartment). Notice that Identity Service resources reside within the\ntenancy itself, unlike cloud resources such as compute instances, which typically reside within\ncompartments inside the tenancy. For information about OCIDs, see\n[Resource Identifiers](../../../#General/Concepts/identifiers.htm).\n\nYou must also specify a *name* for the user, which must be unique across all users in your tenancy\nand cannot be changed. If you specify a name that's already in use, you'll get a 409 error.\nThis name will be the user's login to the Console. You might want to pick a\nname that your company's own identity system (e.g., Active Directory, LDAP, etc.) already uses.\nIf you delete a user and then create a new user with the same name, they'll be considered different\nusers because they have different OCIDs.\n\nYou must also specify a *description* for the user (although it can be an empty string).\nIt does not have to be unique, and you can change it anytime with [UpdateUser](#/en/identity/20160918/User/UpdateUser).\nYou can use the field to provide the user's full name, a description, a nickname, or other\ninformation to generally identify the user.\n\nAfter you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the\nobject, first make sure its `lifecycleState` has changed to ACTIVE.\n\nA new user has no permissions until you place the user in one or more groups (see\n[AddUserToGroup](#/en/identity/20160918/UserGroupMembership/AddUserToGroup). If the user needs to access the Console, you need to\nprovide the user a password (see [CreateOrResetUIPassword](#/en/identity/20160918/UIPassword/CreateOrResetUIPassword)).\nIf the user needs to access the Oracle Bare Metal IaaS API, you need to upload a public API signing\nkey for that user (see [UploadApiKey](#/en/identity/20160918/ApiKey/UploadApiKey)).\n\nFor information about endpoints and signing API requests,\nsee [Making API Requests](../../../#API/Concepts/usingapi.htm).\n

        :param CreateUserDetails create_user_details: Request object for creating a new user. (required)
        :param str opc_retry_token: A token that uniquely identifies a request so it can be retried in case of a timeout or\nserver error without risk of executing that same action again. Retry tokens expire after 24\nhours, but can be invalidated before then due to conflicting operations (e.g., if a resource\nhas been deleted and purged from the system, then a retry of the original creation request\nmay be rejected).\n
        :return: A Response object with data of type User
        """

        all_params = ['create_user_details', 'opc_retry_token']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_user" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'create_user_details' is set
        if ('create_user_details' not in params) or (params['create_user_details'] is None):
            raise ValueError("Missing the required parameter `create_user_details` when calling `create_user`")

        resource_path = '/users/'
        path_params = {}

        query_params = {}

        header_params = {}
        if 'opc_retry_token' in params:
            header_params['opc-retry-token'] = params['opc_retry_token']

        body_params = None
        if 'create_user_details' in params:
            body_params = params['create_user_details']

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_identity_api,
                                            resource_path,
                                            'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='User')
        return response

    def delete_api_key(self, user_id, fingerprint, **kwargs):
        """
        DeleteApiKey
        Deletes the specified API signing key for the specified user.\n\nEvery user has permission to use this operation to delete a key for *their own user ID*. An\nAdministrator in your organization does not need to write a policy to give users this ability.\nTo compare, Administrators who have permission to the tenancy can use this operation to delete\na key for any user, including themselves.\n

        :param str user_id: The user's OCID. (required)
        :param str fingerprint: The key's fingerprint. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
        """

        all_params = ['user_id', 'fingerprint', 'if_match']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_api_key" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `delete_api_key`")
        # verify the required parameter 'fingerprint' is set
        if ('fingerprint' not in params) or (params['fingerprint'] is None):
            raise ValueError("Missing the required parameter `fingerprint` when calling `delete_api_key`")

        resource_path = '/users/{userId}/apiKeys/{fingerprint}'
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']
        if 'fingerprint' in params:
            path_params['fingerprint'] = params['fingerprint']

        query_params = {}

        header_params = {}
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_identity_api,
                                            resource_path,
                                            'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type=None)
        return response

    def delete_group(self, group_id, **kwargs):
        """
        DeleteGroup
        Deletes the specified group. The group must be empty.\n\n**IMPORTANT**: To avoid confusion, we recommend you also delete any policies that apply to that group.\nIf you were to later create a new group with the same name as the deleted group, the existing policy\nwould not apply to the new group, because the two groups would have different OCIDs. However, the existence\nof the policy could still cause confusion because your policies might use the name and not the OCID to\nidentify the applicable group.\n

        :param str group_id: The group's OCID. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
        """

        all_params = ['group_id', 'if_match']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_group" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'group_id' is set
        if ('group_id' not in params) or (params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `delete_group`")

        resource_path = '/groups/{groupId}'
        path_params = {}
        if 'group_id' in params:
            path_params['groupId'] = params['group_id']

        query_params = {}

        header_params = {}
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_identity_api,
                                            resource_path,
                                            'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type=None)
        return response

    def delete_policy(self, policy_id, **kwargs):
        """
        DeletePolicy
        Deletes the specified policy. The deletion takes effect typically within 10 seconds.

        :param str policy_id: The policy's OCID. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
        """

        all_params = ['policy_id', 'if_match']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_policy" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params) or (params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `delete_policy`")

        resource_path = '/policies/{policyId}'
        path_params = {}
        if 'policy_id' in params:
            path_params['policyId'] = params['policy_id']

        query_params = {}

        header_params = {}
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_identity_api,
                                            resource_path,
                                            'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type=None)
        return response

    def delete_swift_password(self, user_id, swift_password_id, **kwargs):
        """
        DeleteSwiftPassword
        Deletes the specified Swift password for the specified user.\n

        :param str user_id: The user's OCID. (required)
        :param str swift_password_id: The Swift password's OCID. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
        """

        all_params = ['user_id', 'swift_password_id', 'if_match']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_swift_password" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `delete_swift_password`")
        # verify the required parameter 'swift_password_id' is set
        if ('swift_password_id' not in params) or (params['swift_password_id'] is None):
            raise ValueError("Missing the required parameter `swift_password_id` when calling `delete_swift_password`")

        resource_path = '/users/{userId}/swiftPasswords/{swiftPasswordId}'
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']
        if 'swift_password_id' in params:
            path_params['swiftPasswordId'] = params['swift_password_id']

        query_params = {}

        header_params = {}
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_identity_api,
                                            resource_path,
                                            'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type=None)
        return response

    def delete_user(self, user_id, **kwargs):
        """
        DeleteUser
        Deletes the specified user. The user must not be in any groups.

        :param str user_id: The user's OCID. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
        """

        all_params = ['user_id', 'if_match']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_user" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `delete_user`")

        resource_path = '/users/{userId}'
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

        query_params = {}

        header_params = {}
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_identity_api,
                                            resource_path,
                                            'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type=None)
        return response

    def get_compartment(self, compartment_id, **kwargs):
        """
        GetCompartment
        Gets the specified compartment's information.\n\nThis operation does not return a list of all the resources inside the compartment. There is no single\nAPI operation that does that. Compartments can contain multiple types of resources (instances, block\nstorage volumes, etc.). To find out what's in a compartment, you must call the \"List\" operation for\neach resource type and specify the compartment's OCID as a query parameter in the request. For example,\ncall the `ListInstances` operation in the Cloud Compute Service or the `ListVolumes` operation in\n Cloud Block Storage.\n

        :param str compartment_id: The compartment's OCID. (required)
        :return: A Response object with data of type Compartment
        """

        all_params = ['compartment_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_compartment" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'compartment_id' is set
        if ('compartment_id' not in params) or (params['compartment_id'] is None):
            raise ValueError("Missing the required parameter `compartment_id` when calling `get_compartment`")

        resource_path = '/compartments/{compartmentId}'
        path_params = {}
        if 'compartment_id' in params:
            path_params['compartmentId'] = params['compartment_id']

        query_params = {}

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_identity_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='Compartment')
        return response

    def get_group(self, group_id, **kwargs):
        """
        GetGroup
        Gets the specified group's information.\n\nThis operation does not return a list of all the users in the group. To do that, use\n[ListUserGroupMemberships](#/en/identity/20160918/UserGroupMembership/ListUserGroupMemberships) and provide the group's OCID as a\nquery parameter in the request.\n

        :param str group_id: The group's OCID. (required)
        :return: A Response object with data of type Group
        """

        all_params = ['group_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_group" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'group_id' is set
        if ('group_id' not in params) or (params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `get_group`")

        resource_path = '/groups/{groupId}'
        path_params = {}
        if 'group_id' in params:
            path_params['groupId'] = params['group_id']

        query_params = {}

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_identity_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='Group')
        return response

    def get_policy(self, policy_id, **kwargs):
        """
        GetPolicy
        Gets the specified policy's information.

        :param str policy_id: The policy's OCID. (required)
        :return: A Response object with data of type Policy
        """

        all_params = ['policy_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_policy" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params) or (params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `get_policy`")

        resource_path = '/policies/{policyId}'
        path_params = {}
        if 'policy_id' in params:
            path_params['policyId'] = params['policy_id']

        query_params = {}

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_identity_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='Policy')
        return response

    def get_user(self, user_id, **kwargs):
        """
        GetUser
        Gets the specified user's information.

        :param str user_id: The user's OCID. (required)
        :return: A Response object with data of type User
        """

        all_params = ['user_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_user`")

        resource_path = '/users/{userId}'
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

        query_params = {}

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_identity_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='User')
        return response

    def get_user_group_membership(self, user_group_membership_id, **kwargs):
        """
        GetUserGroupMembership
        Gets the specified UserGroupMembership's information.

        :param str user_group_membership_id: The userGroupMembership's OCID. (required)
        :return: A Response object with data of type UserGroupMembership
        """

        all_params = ['user_group_membership_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_group_membership" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_group_membership_id' is set
        if ('user_group_membership_id' not in params) or (params['user_group_membership_id'] is None):
            raise ValueError("Missing the required parameter `user_group_membership_id` when calling `get_user_group_membership`")

        resource_path = '/userGroupMemberships/{userGroupMembershipId}'
        path_params = {}
        if 'user_group_membership_id' in params:
            path_params['userGroupMembershipId'] = params['user_group_membership_id']

        query_params = {}

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_identity_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='UserGroupMembership')
        return response

    def list_api_keys(self, user_id, **kwargs):
        """
        ListApiKeys
        Gets a list of the API signing keys for the specified user. A user can have a maximum of three keys.\n\nEvery user has permission to use this API call for *their own user ID*.  An Administrator in your\norganization does not need to write a policy to give users this ability.\n

        :param str user_id: The user's OCID. (required)
        :return: A Response object with data of type list[ApiKey]
        """

        all_params = ['user_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_api_keys" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `list_api_keys`")

        resource_path = '/users/{userId}/apiKeys/'
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

        query_params = {}

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_identity_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='list[ApiKey]')
        return response

    def list_availability_domains(self, compartment_id, **kwargs):
        """
        ListAvailabilityDomains
        Gets a list of all the Availability Domains in your tenancy. You must specify your tenancy's OCID\nas the value for the compartment ID (remember that the tenancy is simply the root compartment). See\n[Where to Find Your Tenancy's OCID](../../../#API/Concepts/usingapi.htm#Where_to_Find_Your_Tenancy's_OCID).\nFor information about Availability Domains, see\n[Regions and Availability Domains](../../../#General/Concepts/regions.htm).\n\nFor information about endpoints and signing API requests,\nsee [Making API Requests](../../../#API/Concepts/usingapi.htm).\n

        :param str compartment_id: Your tenancy's OCID (remember that the tenancy is simply the root compartment).\n (required)
        :return: A Response object with data of type list[AvailabilityDomain]
        """

        all_params = ['compartment_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_availability_domains" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'compartment_id' is set
        if ('compartment_id' not in params) or (params['compartment_id'] is None):
            raise ValueError("Missing the required parameter `compartment_id` when calling `list_availability_domains`")

        resource_path = '/availabilityDomains/'
        path_params = {}

        query_params = {}
        if 'compartment_id' in params:
            query_params['compartmentId'] = params['compartment_id']

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_identity_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='list[AvailabilityDomain]')
        return response

    def list_compartments(self, compartment_id, **kwargs):
        """
        ListCompartments
        Gets a list of all the compartments in your tenancy. You must specify your tenancy's OCID as the value\nfor the compartment ID (remember that the tenancy is simply the root compartment).\nSee [Where to Find Your Tenancy's OCID](../../../#API/Concepts/usingapi.htm#Where_to_Find_Your_Tenancy's_OCID).\n

        :param str compartment_id: Your tenancy's OCID (remember that the tenancy is simply the root compartment).\n (required)
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call.\n
        :param int limit: The maximum number of items to return in a paginated \"List\" call.\n
        :return: A Response object with data of type list[Compartment]
        """

        all_params = ['compartment_id', 'page', 'limit']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_compartments" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'compartment_id' is set
        if ('compartment_id' not in params) or (params['compartment_id'] is None):
            raise ValueError("Missing the required parameter `compartment_id` when calling `list_compartments`")

        resource_path = '/compartments/'
        path_params = {}

        query_params = {}
        if 'compartment_id' in params:
            query_params['compartmentId'] = params['compartment_id']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'limit' in params:
            query_params['limit'] = params['limit']

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_identity_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='list[Compartment]')
        return response

    def list_groups(self, compartment_id, **kwargs):
        """
        ListGroups
        Gets a list of all the groups in your tenancy. You must specify your tenancy's OCID as the value for\nthe compartment ID (remember that the tenancy is simply the root compartment).\nSee [Where to Find Your Tenancy's OCID](../../../#API/Concepts/usingapi.htm#Where_to_Find_Your_Tenancy's_OCID).\n

        :param str compartment_id: Your tenancy's OCID (remember that the tenancy is simply the root compartment).\n (required)
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call.\n
        :param int limit: The maximum number of items to return in a paginated \"List\" call.\n
        :return: A Response object with data of type list[Group]
        """

        all_params = ['compartment_id', 'page', 'limit']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_groups" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'compartment_id' is set
        if ('compartment_id' not in params) or (params['compartment_id'] is None):
            raise ValueError("Missing the required parameter `compartment_id` when calling `list_groups`")

        resource_path = '/groups/'
        path_params = {}

        query_params = {}
        if 'compartment_id' in params:
            query_params['compartmentId'] = params['compartment_id']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'limit' in params:
            query_params['limit'] = params['limit']

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_identity_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='list[Group]')
        return response

    def list_policies(self, compartment_id, **kwargs):
        """
        ListPolicies
        Gets a list of all the policies in your tenancy. You must specify your tenancy's OCID as the value\nfor the compartment ID (remember that the tenancy is simply the root compartment).\nSee [Where to Find Your Tenancy's OCID](../../../#API/Concepts/usingapi.htm#Where_to_Find_Your_Tenancy's_OCID).\n\nTo determine which policies apply to a particular group or compartment, you must view the individual\nstatements inside all your policies. There isn't a way to automatically obtain that information via the API.\n

        :param str compartment_id: Your tenancy's OCID (remember that the tenancy is simply the root compartment).\n (required)
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call.\n
        :param int limit: The maximum number of items to return in a paginated \"List\" call.\n
        :return: A Response object with data of type list[Policy]
        """

        all_params = ['compartment_id', 'page', 'limit']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_policies" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'compartment_id' is set
        if ('compartment_id' not in params) or (params['compartment_id'] is None):
            raise ValueError("Missing the required parameter `compartment_id` when calling `list_policies`")

        resource_path = '/policies/'
        path_params = {}

        query_params = {}
        if 'compartment_id' in params:
            query_params['compartmentId'] = params['compartment_id']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'limit' in params:
            query_params['limit'] = params['limit']

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_identity_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='list[Policy]')
        return response

    def list_swift_passwords(self, user_id, **kwargs):
        """
        ListSwiftPasswords
        Gets a list of the Swift passwords for the specified user. The returned object contains the password's OCID, but not\nthe password itself. The actual password is returned only upon creation. A user can have up to two Swift passwords at\na time.\n

        :param str user_id: The user's OCID. (required)
        :return: A Response object with data of type list[SwiftPassword]
        """

        all_params = ['user_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_swift_passwords" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `list_swift_passwords`")

        resource_path = '/users/{userId}/swiftPasswords/'
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

        query_params = {}

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_identity_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='list[SwiftPassword]')
        return response

    def list_user_group_memberships(self, compartment_id, **kwargs):
        """
        ListUserGroupMemberships
        Gets a list of all the `UserGroupMembership` objects in your tenancy. You must specify your tenancy's OCID\nas the value for the compartment ID\n(see [Where to Find Your Tenancy's OCID](../../../#API/Concepts/usingapi.htm#Where_to_Find_Your_Tenancy's_OCID)).\nYou must also then filter the list in one of these ways:\n\n- You can limit the results to just the memberships for a given user by specifying a `userId`.\n- Similarly, you can limit the results to just the memberships for a given group by specifying a `groupId`.\n- You can set both the `userId` and `groupId` to determine if the specified user is in the specified group.\nIf the answer is no, the response is an empty list.\n

        :param str compartment_id: Your tenancy's OCID (remember that the tenancy is simply the root compartment).\n (required)
        :param str user_id: The user's OCID.
        :param str group_id: The group's OCID.
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call.\n
        :param int limit: The maximum number of items to return in a paginated \"List\" call.\n
        :return: A Response object with data of type list[UserGroupMembership]
        """

        all_params = ['compartment_id', 'user_id', 'group_id', 'page', 'limit']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_user_group_memberships" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'compartment_id' is set
        if ('compartment_id' not in params) or (params['compartment_id'] is None):
            raise ValueError("Missing the required parameter `compartment_id` when calling `list_user_group_memberships`")

        resource_path = '/userGroupMemberships/'
        path_params = {}

        query_params = {}
        if 'compartment_id' in params:
            query_params['compartmentId'] = params['compartment_id']
        if 'user_id' in params:
            query_params['userId'] = params['user_id']
        if 'group_id' in params:
            query_params['groupId'] = params['group_id']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'limit' in params:
            query_params['limit'] = params['limit']

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_identity_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='list[UserGroupMembership]')
        return response

    def list_users(self, compartment_id, **kwargs):
        """
        ListUsers
        Gets a list of all the users in your tenancy. You must specify your tenancy's OCID as the value for the\ncompartment ID (remember that the tenancy is simply the root compartment).\nSee [Where to Find Your Tenancy's OCID](../../../#API/Concepts/usingapi.htm#Where_to_Find_Your_Tenancy's_OCID).\n

        :param str compartment_id: Your tenancy's OCID (remember that the tenancy is simply the root compartment).\n (required)
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call.\n
        :param int limit: The maximum number of items to return in a paginated \"List\" call.\n
        :return: A Response object with data of type list[User]
        """

        all_params = ['compartment_id', 'page', 'limit']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_users" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'compartment_id' is set
        if ('compartment_id' not in params) or (params['compartment_id'] is None):
            raise ValueError("Missing the required parameter `compartment_id` when calling `list_users`")

        resource_path = '/users/'
        path_params = {}

        query_params = {}
        if 'compartment_id' in params:
            query_params['compartmentId'] = params['compartment_id']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'limit' in params:
            query_params['limit'] = params['limit']

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_identity_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='list[User]')
        return response

    def remove_user_from_group(self, user_group_membership_id, **kwargs):
        """
        RemoveUserFromGroup
        Removes a user from a group by deleting the corresponding `UserGroupMembership`.

        :param str user_group_membership_id: The userGroupMembership's OCID. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
        """

        all_params = ['user_group_membership_id', 'if_match']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_user_from_group" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_group_membership_id' is set
        if ('user_group_membership_id' not in params) or (params['user_group_membership_id'] is None):
            raise ValueError("Missing the required parameter `user_group_membership_id` when calling `remove_user_from_group`")

        resource_path = '/userGroupMemberships/{userGroupMembershipId}'
        path_params = {}
        if 'user_group_membership_id' in params:
            path_params['userGroupMembershipId'] = params['user_group_membership_id']

        query_params = {}

        header_params = {}
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_identity_api,
                                            resource_path,
                                            'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type=None)
        return response

    def update_compartment(self, compartment_id, update_compartment_details, **kwargs):
        """
        UpdateCompartment
        Updates the specified compartment.

        :param str compartment_id: The compartment's OCID. (required)
        :param UpdateCompartmentDetails update_compartment_details: Request object for updating a compartment. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type Compartment
        """

        all_params = ['compartment_id', 'update_compartment_details', 'if_match']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_compartment" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'compartment_id' is set
        if ('compartment_id' not in params) or (params['compartment_id'] is None):
            raise ValueError("Missing the required parameter `compartment_id` when calling `update_compartment`")
        # verify the required parameter 'update_compartment_details' is set
        if ('update_compartment_details' not in params) or (params['update_compartment_details'] is None):
            raise ValueError("Missing the required parameter `update_compartment_details` when calling `update_compartment`")

        resource_path = '/compartments/{compartmentId}'
        path_params = {}
        if 'compartment_id' in params:
            path_params['compartmentId'] = params['compartment_id']

        query_params = {}

        header_params = {}
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']

        body_params = None
        if 'update_compartment_details' in params:
            body_params = params['update_compartment_details']

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_identity_api,
                                            resource_path,
                                            'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='Compartment')
        return response

    def update_group(self, group_id, update_group_details, **kwargs):
        """
        UpdateGroup
        Updates the specified group.

        :param str group_id: The group's OCID. (required)
        :param UpdateGroupDetails update_group_details: Request object for updating a group. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type Group
        """

        all_params = ['group_id', 'update_group_details', 'if_match']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_group" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'group_id' is set
        if ('group_id' not in params) or (params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `update_group`")
        # verify the required parameter 'update_group_details' is set
        if ('update_group_details' not in params) or (params['update_group_details'] is None):
            raise ValueError("Missing the required parameter `update_group_details` when calling `update_group`")

        resource_path = '/groups/{groupId}'
        path_params = {}
        if 'group_id' in params:
            path_params['groupId'] = params['group_id']

        query_params = {}

        header_params = {}
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']

        body_params = None
        if 'update_group_details' in params:
            body_params = params['update_group_details']

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_identity_api,
                                            resource_path,
                                            'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='Group')
        return response

    def update_policy(self, policy_id, update_policy_details, **kwargs):
        """
        UpdatePolicy
        Updates the specified policy.\n\nPolicy changes take effect typically within 10 seconds.\n

        :param str policy_id: The policy's OCID. (required)
        :param UpdatePolicyDetails update_policy_details: Request object for updating a policy. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type Policy
        """

        all_params = ['policy_id', 'update_policy_details', 'if_match']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_policy" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params) or (params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `update_policy`")
        # verify the required parameter 'update_policy_details' is set
        if ('update_policy_details' not in params) or (params['update_policy_details'] is None):
            raise ValueError("Missing the required parameter `update_policy_details` when calling `update_policy`")

        resource_path = '/policies/{policyId}'
        path_params = {}
        if 'policy_id' in params:
            path_params['policyId'] = params['policy_id']

        query_params = {}

        header_params = {}
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']

        body_params = None
        if 'update_policy_details' in params:
            body_params = params['update_policy_details']

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_identity_api,
                                            resource_path,
                                            'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='Policy')
        return response

    def update_swift_password(self, user_id, swift_password_id, update_swift_password_details, **kwargs):
        """
        UpdateSwiftPassword
        Updates the specified Swift password's description.\n

        :param str user_id: The user's OCID. (required)
        :param str swift_password_id: The Swift password's OCID. (required)
        :param UpdateSwiftPasswordDetails update_swift_password_details: Request object for updating a Swift password. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type SwiftPassword
        """

        all_params = ['user_id', 'swift_password_id', 'update_swift_password_details', 'if_match']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_swift_password" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `update_swift_password`")
        # verify the required parameter 'swift_password_id' is set
        if ('swift_password_id' not in params) or (params['swift_password_id'] is None):
            raise ValueError("Missing the required parameter `swift_password_id` when calling `update_swift_password`")
        # verify the required parameter 'update_swift_password_details' is set
        if ('update_swift_password_details' not in params) or (params['update_swift_password_details'] is None):
            raise ValueError("Missing the required parameter `update_swift_password_details` when calling `update_swift_password`")

        resource_path = '/users/{userId}/swiftPasswords/{swiftPasswordId}'
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']
        if 'swift_password_id' in params:
            path_params['swiftPasswordId'] = params['swift_password_id']

        query_params = {}

        header_params = {}
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']

        body_params = None
        if 'update_swift_password_details' in params:
            body_params = params['update_swift_password_details']

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_identity_api,
                                            resource_path,
                                            'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='SwiftPassword')
        return response

    def update_user(self, user_id, update_user_details, **kwargs):
        """
        UpdateUser
        Updates the specified user.

        :param str user_id: The user's OCID. (required)
        :param UpdateUserDetails update_user_details: Request object for updating a user. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type User
        """

        all_params = ['user_id', 'update_user_details', 'if_match']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_user" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `update_user`")
        # verify the required parameter 'update_user_details' is set
        if ('update_user_details' not in params) or (params['update_user_details'] is None):
            raise ValueError("Missing the required parameter `update_user_details` when calling `update_user`")

        resource_path = '/users/{userId}'
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

        query_params = {}

        header_params = {}
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']

        body_params = None
        if 'update_user_details' in params:
            body_params = params['update_user_details']

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_identity_api,
                                            resource_path,
                                            'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='User')
        return response

    def update_user_state(self, user_id, update_state_details, **kwargs):
        """
        UpdateUserState
        Updates the state of the specified user.

        :param str user_id: The user's OCID. (required)
        :param UpdateStateDetails update_state_details: Request object for updating a user state. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type User
        """

        all_params = ['user_id', 'update_state_details', 'if_match']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_user_state" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `update_user_state`")
        # verify the required parameter 'update_state_details' is set
        if ('update_state_details' not in params) or (params['update_state_details'] is None):
            raise ValueError("Missing the required parameter `update_state_details` when calling `update_user_state`")

        resource_path = '/users/{userId}/state/'
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

        query_params = {}

        header_params = {}
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']

        body_params = None
        if 'update_state_details' in params:
            body_params = params['update_state_details']

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_identity_api,
                                            resource_path,
                                            'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='User')
        return response

    def upload_api_key(self, user_id, create_api_key_details, **kwargs):
        """
        UploadApiKey
        Uploads an API signing key for the specified user.  Each user can have a maximum of three keys.\nEach key must be an RSA public key in PEM format. For more information about the format and how\nto generate a key, see [Signing Requests](../../../#API/Concepts/signingrequests.htm). For more\ninformation about user credentials, see [User Credentials](../../../#Identity/Concepts/usercredentials.htm).\n\nEvery user has permission to use this operation to upload a key for *their own user ID*. An\nAdministrator in your organization does not need to write a policy to give users this ability.\nTo compare, Administrators who have permission to the tenancy can use this operation to upload a\nkey for any user, including themselves.\n\n**Important:** Even though you have permission to upload an API key, you might not yet\nhave permission to do much else. If you try calling an operation unrelated to your own credential\nmanagement (e.g., `ListUsers`, `LaunchInstance`) and receive a 403 error (i.e., unauthorized),\ncheck with an administrator to confirm which Identity Service group(s) you're in and what permissions\nyou have.\n\n**Note:** The resulting `ApiKey` object includes a placeholder, Oracle-assigned description.\nYou can't set or change that value.\n\nAfter you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using\nthe object, first make sure its `lifecycleState` has changed to ACTIVE.\n

        :param str user_id: The user's OCID. (required)
        :param CreateApiKeyDetails create_api_key_details: Request object for uploading an API key for a user. (required)
        :param str opc_retry_token: A token that uniquely identifies a request so it can be retried in case of a timeout or\nserver error without risk of executing that same action again. Retry tokens expire after 24\nhours, but can be invalidated before then due to conflicting operations (e.g., if a resource\nhas been deleted and purged from the system, then a retry of the original creation request\nmay be rejected).\n
        :return: A Response object with data of type ApiKey
        """

        all_params = ['user_id', 'create_api_key_details', 'opc_retry_token']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upload_api_key" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `upload_api_key`")
        # verify the required parameter 'create_api_key_details' is set
        if ('create_api_key_details' not in params) or (params['create_api_key_details'] is None):
            raise ValueError("Missing the required parameter `create_api_key_details` when calling `upload_api_key`")

        resource_path = '/users/{userId}/apiKeys/'
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

        query_params = {}

        header_params = {}
        if 'opc_retry_token' in params:
            header_params['opc-retry-token'] = params['opc_retry_token']

        body_params = None
        if 'create_api_key_details' in params:
            body_params = params['create_api_key_details']

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_identity_api,
                                            resource_path,
                                            'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='ApiKey')
        return response
